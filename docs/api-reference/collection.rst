
Collection
==========

Overview
--------

A subreddit collection. Collections contain submissions.

See `<https://mods.reddithelp.com/hc/en-us/articles/360027311431-Collections>`_.

In addition to the two "get" endpoints listed here, collection objects can be obtained by fetching a
subreddit object. If the subreddit has any collections then the object will have a `collections` field.


Schema
~~~~~~

.. csv-table:: Submission Object
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "subreddit_id","string","The full ID36 (prefixed with `t5_`) of the subreddit the collection belongs."
   "author_id","string","The full ID36 (prefixed with `t2_`) of the author of the collection."
   "author_name","string","Name of the author of the collection."
   "title","string","The title of this collection."
   "description","string","The description of the collection set by the author."
   "created_at_utc","float","The UNIX timestamp of when the collection was created."
   "last_update_utc","float","The UNIX timestamp of when the last post was added. This field is not updated in
   any other circumstance such as updating the title or description."
   "display_layout","string?","Either `null`, `""TIMELINE""`, or `""GALLERY""`.

   A new collection will have this field value be `null` which is treated the same as `""TIMELINE""`."
   "link_ids","string array","The full ID36s of the submissions contained in the collection."
   "permalink","string","An absolute permalink for this collection."
   "primary_link_id?","string","The full ID36 of the first submission listed in the `sorted_links` structure.

   This field will not exist if the collection is empty.

   This field is only available when getting the collection information directly via UUID
   using `/api/v1/collections/collection`."
   "sorted_links?","listing object","A listing structure of submission objects for the submissions
   contained in this collection.

   This field is only available when fetching a collection directly by UUID using the
   `GET /api/v1/collections/collection` endpoint and the `include_links` option is `true`."


Actions
-------

Get
~~~

.. http:get:: /api/v1/collections/collection

*scope: read*

Get a collection.

If the given `collection_id` was not found then ``{"json": {"errors": []}}`` is returned.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The UUID of a collection."
   "include_links","boolean","Whether to include the `sorted_links` field in the collection object.

   Default: true. (Any value matching `/^[fF0]/` is falsy.)"

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "NO_TEXT","200","The `collection_id` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_collections_collection


Get subreddit collections' details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/collections/subreddit_collections

*scope: read*

Get a list of collections' details from the subreddit.

Collection objects from this endpoint don't have the `primary_link_id` or `sorted_links` fields.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "sr_fullname","string","A full ID36 (prefixed with `t5_`) of a subreddit."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "SUBREDDIT_NOEXIST","200","* The `sr_fullname` parameter was not specified.

   * The subreddit specified by the `sr_fullname` parameter could not be found.","
   ``{""json"": {""errors"": [[""SUBREDDIT_NOEXIST"", ""Hmm, that community doesn't exist. Try checking the spelling."", ""sr_fullname""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_collections_subreddit_collections


Create
~~~~~~

.. http:post:: /api/v1/collections/create_collection

*scope: modposts*

Create a collection.

Returns the newly created collection JSON object.
The collection object will not have the `primary_link_id` or `sorted_links` fields.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "sr_fullname","string","A full ID36 (prefixed with `t5_`) of a subreddit."
   "title","string","Title of the submission up to 300 characters long."
   "description","string","A string no longer than 500 characters."
   "display_layout","string","One of `TIMELINE`, `GALLERY`. Default is `TIMELINE`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "SUBREDDIT_NOEXIST","200","* The `sr_fullname` parameter was not specified.

   * The `sr_fullname` subreddit doesn't exist.","
   ``{""json"": {""errors"": [[""SUBREDDIT_NOEXIST"", ""Hmm, that community doesn't exist. Try checking the spelling."", ""sr_fullname""]]}}``
   "
   "NO_TEXT","200","The `title` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""title""]]}}``
   "
   "TOO_LONG","200","* (1) The specified title was longer than 300 characters.

   * The specified description was longer than 500 characters.","
   (1): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 300 characters"", ""title""]]}}``
   "
   "INVALID_OPTION","200","The value specified for `display_layout` is not valid. The options are case-sensitive.","
   ``{""json"": {""errors"": [[""INVALID_OPTION"", ""that option is not valid"", ""display_layout""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_create_collection


Delete
~~~~~~

.. http:post:: /api/v1/collections/delete_collection

*scope: modposts*

Delete a collection.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "NO_TEXT","200","The `collection_id` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_ID","200","The `collection_id` specified does not exist.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_ID"", ""That collection doesn't exist"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_ID","200","The `collection_id` specified does not exist.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_ID"", ""That collection doesn't exist"", ""collection_id""]]}}``
   "
   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "


Add post
~~~~~~~~

.. http:post:: /api/v1/collections/add_post_to_collection

*scope: modposts*

Add a submission to a collection.

Collections have a capacity of 100 posts. Attempting to add to a full collection will
result in an `INVALID_COLLECTION_UPDATE` API error.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "link_fullname","string","A full ID36 of a submission."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `collection_id` parameter was not specified or was empty string.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_UPDATE","200","* The `collection_id` specified does not exist.

   * The submission specified by `link_fullname` already exists in the collection.

   * The submission specified by `link_fullname` does not match the collection's subreddit.

   * The collection is full (it contains 100 posts).","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_UPDATE"", ""That collection couldn't be updated"", ""collection_id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "404","* The `link_fullname` parameter was not specified. 

   * The `link_fullname` submission full ID36 does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "
   "500","The `collection_id` specified is not a UUID.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_add_post_to_collection


Remove post
~~~~~~~~~~~

.. http:post:: /api/v1/collections/remove_post_in_collection

*scope: modposts*

Remove a submission from a collection.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "link_fullname","string","A full ID36 of a submission."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `collection_id` parameter was not specified.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_UPDATE","200","* The `collection_id` specified does not exist.

   * The submission specified by `link_fullname` does not exist in the collection.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_UPDATE"", ""That collection couldn't be updated"", ""collection_id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "404","* The `link_fullname` parameter was not specified. 

   * The `link_fullname` submission full ID36 does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "
   "500","The `collection_id` specified is not a UUID.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_remove_post_in_collection


Reorder
~~~~~~~

.. http:post:: /api/v1/collections/reorder_collection

*scope: modposts*

Reorder posts in a collection.

`link_ids` is a comma separated list of submission full ID36s.
An error is returned (`INVALID_COLLECTION_UPDATE`) if an ID in the list is not found in the collection.
If only a subset of the IDs in the collection are specified then those submissions will be moved
to the top of the collection in the order specified. The rest are moved down, maintaining their order.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "link_ids","string","A comma separated list of submission full ID36s."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "INVALID_COLLECTION_UPDATE","200","One of the full ID36s specified in the `link_ids` list does not exist in the collection.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_UPDATE"", ""That collection couldn't be updated"", ""collection_id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "404","* The `collection_id` parameter was not specified or was empty.

   * The `collection_id` specified does not exist.

   * The `collection_id` specified is invalid.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_reorder_collection


Update title
~~~~~~~~~~~~

.. http:post:: /api/v1/collections/update_collection_title

*scope: modposts*

Update a collection's title.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "title","string","The new title for the collection, up to 300 characters long."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","* (1) The `collection_id` parameter was not specified.

   * The `title` parameter was not specified or was empty.","
   (1): ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","* (1) The specified `collection_id` was over 36 characters.

   * The specified `title` was over 300 characters.","
   (1): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_ID","200","The `collection_id` specified does not exist.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_ID"", ""That collection doesn't exist"", ""collection_id""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_update_collection_title


Update description
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/collections/update_collection_description

*scope: modposts*

Update a collection's description.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "description","string","The new description for the collection, up to 500 characters long.

   If not specified an empty string will be used."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `collection_id` parameter was not specified.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","* (1) The specified `collection_id` was over 36 characters.

   * (2) The specified `description` was over 500 characters.","
   (1): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``

   (2): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 500 characters"", ""description""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_ID","200","The `collection_id` specified does not exist.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_ID"", ""That collection doesn't exist"", ""collection_id""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_update_collection_description


Update display layout
~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/collections/update_collection_display_layout

*scope: modposts*

Update a collection's display layout.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "display_layout","string","Options: `TIMELINE` or `GALLERY`. (Case-sensitive.)

   If not specified or an empty string, the `display_layout` field on the collection object
   will be set to `null`, which is treated the same as `""TIMELINE""`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `collection_id` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "
   "INVALID_COLLECTION_ID","200","The `collection_id` specified does not exist.","
   ``{""json"": {""errors"": [[""INVALID_COLLECTION_ID"", ""That collection doesn't exist"", ""collection_id""]]}}``
   "
   "INVALID_OPTION","200","The value specified for `display_layout` was not valid. Options are case-sensitive.","
   ``{""json"": {""errors"": [[""INVALID_OPTION"", ""that option is not valid"", ""display_layout""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_v1_collections_update_display_layout


Follow/unfollow
~~~~~~~~~~~~~~~

.. http:post:: /api/v1/collections/follow_collection

*scope: subscribe*

Follow or unfollow a collection.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "collection_id","string","The collection's UUID."
   "follow","boolean","Follow the collection if truth value specified (a string is truthy if 
   it matches `/^[^fF0]/`), otherwise unfollow.

   If the parameter is not specified then the default is to unfollow."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `collection_id` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""collection_id""]]}}``
   "
   "TOO_LONG","200","The specified `collection_id` was over 36 characters.","
   ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 36 characters"", ""collection_id""]]}}``
   "
   "TOO_SHORT","200","The specified `collection_id` was under 36 characters.","
   ``{""json"": {""errors"": [[""TOO_SHORT"", ""this is too short (min: 36)"", ""collection_id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "500","The `collection_id` specified does not exist or was invalid.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "
