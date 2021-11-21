
Comment Tree
============

Actions
-------

Get submission comment tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/comments/{submission}
.. http:get:: [/r/{subreddit}]/comments/{submission}/_/{comment}

*scope: read*

Get the comment tree for a submission.

`{subreddit}` can be obmitted. If given it must be correctly match the subreddit for the
article ID otherwise an empty listing will be returned.
`{submission}` is the ID36 of the submission to get the comment tree of.

If no `{submission}` is specified then the frontpage or subreddit's new comments will be returned.
See :ref:`here <front-page-new-comments>` and :ref:`here <subreddit-new-comments>`.
Clients should check for an empty string input.

This endpoint returns an array of two listings.

The first listing contains one element, the submission object.
See :ref:`Submission <submission-schema>` schema.
It contains an extra field: '`num_duplicates`'.

The second listing is a list of the top level comments.
See :ref:`Comment <comment-schema>` schema.
Their `replies` field will likely contain a listing structure containing comment replies
and may also contain a 'More comments' object as the last element.
If there are no replies then `replies` will be an empty string.

Comment objects contain an extra field: '`depth`'.
Top-level comments will have a depth of `0`, second level `1`, and so on.
Be aware, when getting the comment tree of a comment, the comments will start with a `depth` of 0.

In any listing of the tree, a 'More comments' object, if present, will always be the last element.

A 'continue this thread' 'more comment' object:

.. csv-table:: 'continue this thread' More Comments Object
   :header: "Field","Type (hint)","Description"

   "count","integer","Always 0."
   "name","string","Always `""t1__""`."
   "id","string","Always `""_""`."
   "parent_id","string","Parent submission or comment full ID36."
   "depth","integer","The depth at which this object's parent occurs.
   E.g., if this more comment object is attached to a top-level comment, its depth will be 1."
   "children","string array","Always an empty array."

Example::

   {"kind": "more", "data": {"count": 0, "name": "t1__", "id": "_", "parent_id": "t1_g836nug", "depth": 1, "children": []}}

When found in a listing it will typically be the only element.

To retrieve more comments from this 'more comments' object, use this endpoint again,
specifying `parent_id` as the `comment` parameter value (or use the `{comment}` variant URL).

A 'load more comments' 'more comment' object:

.. csv-table:: 'load more comments' More Comments Object
   :header: "Field","Type (hint)","Description"

   "count","integer","The number of comments this node is stubbing;
   the number of comments that are children of `parent_id`."
   "name","string","The full ID36 of the first item in `children`."
   "id","string","The ID of this object. It will match the ID36 of the first item in `children`."
   "parent_id","string","Parent comment full ID36."
   "depth","integer","The depth at which this object's parent occurs.
   E.g., if this more comment object is attached to a top-level comment, its depth will be 1."
   "children","string array","The IDs of some of the comments to expand.
   This contains only the top-level sub-comments so the number of elements doesn't match `count`."

Example::

   {"kind": "more", "data": {"count": 103, "name": "t1_g83z4le", "id": "g83z4le", "parent_id": "t1_g8343ao", "depth": 4, "children": ["g83z4le", "g83wl0j", "g83nmx0", "g83k77q", "g83butp", "g842b0t", "g842ncg", "g83kmoz", "g83msyh", "g84535q"]}}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "comment","integer","ID36 of a comment. Assume this comment as the root.

   The `/comments/{submission}/_/{comment}` URL can be used instead of this parameter.
   If both are used together then the parameter will take preference.

   Care must be taken when using this parameter: if the comment does not exist then the parameter
   will be ignored and the root comments will be returned instead.
   Clients should assert that the first comment's `parent_id` starts with `t1_` and should reject
   the data otherwise (i.e., it starts with `t3_`).
   "
   "context","integer","If `comment` is specified, the number of parent comments to include.
   An integer from 0 to 8. Any number higher than 8 is treated the same as 8."
   "depth","integer","The number of levels deep to retrieve comments for.
   A value of 0 is ignored.
   A value of 1 means to only retrieve top-level comments.
   A value of 2 means to retrieve comments one level deep.
   And so on.
   The maximum is 10, which is also the default if the parameter is not specified.
   Any value higher than 10 is treated the same as 10."
   "limit","integer","Restrict the number of comments to retrieve."
   "showedits","boolean",""
   "showmore","boolean",""
   "sort","string","One of `confidence` ('best'), `top`, `new`, `controversial`, `old`, `random`, `qa`, `live`.

   If not given or not a valid sort value (including empty string), the default is the 'sort comments by'
   preference of the logged in user. Otherwise, if there is no user context the default is `confidence`."
   "threaded","boolean",""
   "truncate","integer","An integer from 0 to 50. Seems to behave the same as `limit` but won't return
   a more comment object at the top-level."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "404","The given submission ID could not be found.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "


Get more comment tree comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/morechildren

Retrieve comments omitted from a comment tree.

When a comment tree is rendered, the most relevant comments are selected for display and the remaining
comments are stubbed out with more-comment links: either 'load more comments' or 'continue this thread'.
This endpoint is used to retrieve the comments represented by the 'load more comments' stubs.

Two parameters are required: `link_id` and `children`. `link_id` is the full ID36 of the comments'
submission. `children` is a comma-delimited list of comment ID36s to be fetched.

If `id` is passed, it should be the ID of the more-comments object the call is replacing. This is needed
only for the HTML UI's purposes and is optional otherwise.

Comment objects contain an extra field: '`depth`'.

'More comments' objects may appear in various places in the the array.

Elements are ordered in pre-order DFS traversal order, the same as on the site.

.. note::
   You may only make one request at a time to this API endpoint.
   Higher concurrency will result in an error being returned.

.. note::
   This endpoint returns a flat array of comment objects, with potential more-comment objects scattered
   throughout the array. Comment objects' `replies` field will always be empty (an empty string)
   and so you have to manually construct the tree using the comments' `parent_id` fields.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "link_id","string","The full ID36 of the comments' submission."
   "children","string","A comma-delimited list of comment ID36s."
   "id","string","The ID of the associated 'more children' object."
   "sort","string","One of `confidence` ('best'), `top`, `new`, `controversial`, `old`, `random`, `qa`, `live`.

   If not given or not a valid sort value (including empty string), the default is the 'sort comments by'
   preference of the logged in user. Otherwise, if there is no user context the default is `confidence`.

   This should ideally be the same as the sort given in the original `/comments` call."
   "depth","integer","The number of levels deep to retrieve comments for.
   A value of 0 is ignored.
   A value of 1 will return 0 items.
   A value of 2 means to retrieve comments one level deep.
   And so on."
   "limit_children","boolean","If truthy (any string matching `/^[0Ff]/` is falsy),
   only return the children requested, and not sub-comments.

   This is kind of the same as specifying `depth: 1` but more-comment objects won't be present.

   If this is specified with the `depth` parameter this will take precedence."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "400","There are too many comment ID36s (`children` parameter) for the server to handle.

   For example, see the large thread linked in
   `this <https://www.reddit.com/r/redditdev/comments/7si641/praw_530_toolarge_received_413_http_response_when/>`_
   submission.",""
   "403","* The submission ID from `link_id` does not exist.

   * The `link_id` parameter was not specified.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
