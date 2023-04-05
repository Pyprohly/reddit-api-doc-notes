
Submission Draft
================

Overview
--------

Draft Schema
~~~~~~~~~~~~

.. csv-table:: Draft Schema
   :header: "Field","Type (hint)","Description"

   "id","string","A UUID for this draft. E.g., `5d5e1684-08db-11ec-a00d-ae86119e02bc`."
   "kind","string","Either: `markdown`, `richtext`, `link`."
   "created","integer","UNIX timestamp in milliseconds of when the draft was created."
   "modified","integer","UNIX timestamp in milliseconds of when the draft was last modified."
   "is_public_link","boolean","Whether the draft is public."
   "subreddit","string?","The full ID36 (`t5_` prefixed) of the target subreddit.

   Value is `null` if subreddit not chosen yet."
   "title",".","Same as `title` parameter on `POST /api/submit` endpoint."
   "body","string | object","A string of markdown text if `kind: markdown`.
   A richtext JSON object if `kind: richtext`."
   "send_replies",".","Same as `sendreplies` parameter on `POST /api/submit` endpoint."
   "spoiler",".","Same as `spoiler` parameter on `POST /api/submit` endpoint."
   "nsfw",".","Same as `nsfw` parameter on `POST /api/submit` endpoint."
   "original_content",".","Same as `original_content` parameter on `POST /api/submit` endpoint."
   "flair","object?","See 'Draft Flair Info Schema'.

   Value is `null` if no flair selected."
   "content_category","unknown?",""
   "optional_text","string?",""

.. csv-table:: Draft Flair Info Schema
   :header: "Field","Type (hint)","Description"

   "templateId","string","Flair template UUID."
   "type","string","Values: `text`, `richtext`."
   "text","string","The flair text. This will override the template's text."
   "backgroundColor","string","A hex color, e.g. `#a23114`. May be an empty string."
   "textColor","string","Color scheme. Either `dark` or `light`."
   "richtext","array",""


Actions
-------

Create
~~~~~~

.. http:post:: /api/v1/draft

*scope: (unknown)*

Create a draft.

Returns an object like the following::

   {"json": {"errors": [], "data": {"drafts_count": 6, "id": "3f15e9c4-08f2-11ec-9be4-0ac9176c85f9"}}}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "kind","string","* `markdown` or `richtext` -> text post.
   * `link` -> link post."
   "is_public_link","boolean","Whether the draft should be public. Default: false."
   "subreddit","string","The full ID36 (`t5_` prefixed) of the target subreddit."
   "title",".","Same as `title` parameter on `POST /api/submit` endpoint."
   "body","string","* If `kind: markdown`, a string of markdown text.
   * If `kind: markdown`, a string of a richtext object.
   * If `kind: link`, a URL."
   "send_replies",".","Similar to the `sendreplies` parameter on `POST /api/submit` endpoint,
   but the default value is false instead of true."
   "spoiler",".","Same as `spoiler` parameter on `POST /api/submit` endpoint."
   "nsfw",".","Same as `nsfw` parameter on `POST /api/submit` endpoint."
   "original_content",".","Same as `original_content` parameter on `POST /api/submit` endpoint."
   "flair_id",".","Same as `flair_id` parameter on `POST /api/submit` endpoint."
   "flair_text","string","A flair text override."
   "flair_text_color","string","The value of this parameter has no effect.

   The UI sends the flair text color of the flair template (`flair_id`), either `light` or `dark`.
   If the `flair_id` parameter was not specified, an empty string is sent."
   "flair_background_color","string","The value of this parameter has no effect.

   The UI sends the rgb hex color, e.g. `#0dd3bb`, of the specified flair template (`flair_id`).
   If the `flair_id` parameter was not specified, or the template doesn't specify a backgroundd color,
   an empty string is sent."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "JSON_PARSE_ERROR","200","`kind: richtext` was specified and the `body` parameter was not specified,
   empty, or contained an invalid JSON string.","
   ``{""json"": {""errors"": [[""JSON_PARSE_ERROR"", ""Sorry, something went wrong. Double-check things and try again."", ""body""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The `kind` parameter was not specified or the value is invalid."


Retrieve my drafts
~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/drafts

*scope: (unknown)*

Retrieve the current user's drafts.

Returns a JSON object with two keys: `drafts` which is an array of draft objects,
and `subreddits` which is an array of subreddit objects in which the drafts reference.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "


Read public draft
~~~~~~~~~~~~~~~~~

.. http:get:: https://gateway.reddit.com/desktopapi/v1/draftpreviewpage/{user}/{draft_id}

*scope: (unknown)*

Read a public draft.

There is no `https://oauth.reddit.com` API endpoint for reading public drafts but the browser makes
this `https://gateway.reddit.com` call that contains public draft information.

In the returned JSON, the draft can be found under `root['drafts'][draft_id]`.
The key names in this draft object are different from as described in Draft Schema above,
but otherwise the data is the same.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "FORBIDDEN","403","* There is no user context.
   * The specified draft does not exist.
   * You do not have permission to view the draft.","
   ::

      {
        ""code"": 403,
        ""reason"": ""FORBIDDEN"",
        ""explanation"": ""Forbidden""
      }
   "
   "BAD_GATEWAY","502","The specified UUID is not valid.","
   ::

      {
        ""code"": 502,
        ""reason"": ""BAD_GATEWAY"",
        ""explanation"": ""Unprocessable Entity""
      }
   "
   "NOT_FOUND","404","The specified draft could not be found.","
   ::

      {
        ""code"": 404,
        ""reason"": ""NOT_FOUND"",
        ""explanation"": ""not_found""
      }
   "


Update
~~~~~~

.. http:put:: /api/v1/draft

*scope: (unknown)*

Update a draft.

Every parameter should be specified otherwise their effective default will used!

Returns an object like the following::

   {"json": {"errors": [], "data": {"drafts_count": 6, "id": "3f15e9c4-08f2-11ec-9be4-0ac9176c85f9"}}}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","The UUID of an existing draft."
   "...",".","Parameters are the same as in `POST /api/v1/draft`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "...","Same as in `POST /api/v1/draft`."


Delete
~~~~~~

.. http:delete:: /api/v1/draft

*scope: (unknown)*

Delete a draft.

Returns an object like the following::

   {"json": {"errors": [], "data": {"drafts_count": 6, "id": "3f15e9c4-08f2-11ec-9be4-0ac9176c85f9"}}}

The ID returned is that of the deleted draft.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "draft_id","string","The UUID of a draft."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "INVALID_DRAFT_ID","200","The `draft_id` parameter was not specified.","
   ``{""json"": {""errors"": [[""INVALID_DRAFT_ID"", ""Draft id isn't valid"", ""draft_id""]]}}``
   "
   "VALIDATION_ERRORS","422","- The specified draft does not exist.
   - The specified draft UUID is not valid.","
   ``{""explanation"": ""ValidationErrors(errors=[ValidationError(reason=u'Invalid draft_id.', field=u'draft_id', short_name=None)])"", ""message"": ""Unprocessable Entity"", ""reason"": ""VALIDATION_ERRORS""}``
   "
   "UNKNOWN_THRIFT_ERROR","403","The specified draft no longer exists.","
   ``{""explanation"": ""There was a connection error with Thrift: BadRequest(message=u'Draft does not exist.')"", ""message"": ""Forbidden"", ""reason"": ""UNKNOWN_THRIFT_ERROR""}``
   "
