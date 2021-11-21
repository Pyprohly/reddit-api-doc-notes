
Custom Feed
===========

Overview
--------

Schema
~~~~~~

.. csv-table:: Custom Feed Object
   :header: "Field","Type (hint)","Description"

   "display_name","string","The title of the custom feed. 50 characters long."
   "name","string","The custom feed name."
   "can_edit","boolean",""
   "description_html","string","HTML of `description_md` field."
   "num_subscribers","integer","The number of redditors following this custom feed."
   "copied_from","string?","A string if the custom feed has been duplicated, e.g.,
   `/user/siryonkee/m/cruise_ships`, else `null`."
   "icon_url","string","The PNG icon URL."
   "subreddits","object array","An array of objects with one key: `name`.
   E.g., ``[{""name"": ""pics""}, {""name"": ""u_spez""}]``"
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "visibility","string","Either `private` or `public`."
   "over_18","boolean","Is marked as NSFW."
   "path","string","The custom feed URL path. E.g., `/user/pyprohly/m/asdf`"
   "owner","string","Username of the owner. E.g., `Pyprohly`."
   "owner_id","string","The full ID36 of the owner. E.g., `t2_4x25quk`."
   "key_color","string?",""
   "is_subscriber","boolean","Whether the current user is following the custom feed. False if no user context."
   "description_md","string","The custom feed's description."
   "is_favorited","boolean","Whether the current user has favourited the custom feed. False if no user context."


Actions
-------

.. _custom-feed-get:

Get
~~~

.. http:get:: /api/multi/user/{username}/m/{feed_name}

*scope: read*

Fetch a custom feed's information, including subreddit list.

An object is returned. The objects contain two fields: `kind` (with value `LabeledMulti`)
and `data` which contains the properties for the custom feed information.

One of the keys in data is `subreddits` which is an array of objects containing one key named `name` which is
the name of a subreddit in the custom feed. If `expand_srs` parameter is set then a `data` key will also be present
that holds some attributes of the subreddit. These attributes differ from what you get by
:ref:`fetching a subreddit <get-api-info>` object directly (it contains roughly half the attributes). It also slightly
differs from the attributes given by the `sr_detail` parameter in some listing endpoints.

Example output::

   {"kind": "LabeledMulti",
    "data": {...,
             "subreddits": [{"data": {...},
                             "name": "IAmA"},
                            ...]
             ...}}

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "expand_srs","boolean","Whether to provide extra subreddit attributes.

   If false, the `subreddits` key holds an array of objects containing one key: `name`.
   If true, the `subreddits` key holds an array of objects containing keys: `name` and `data`.

   Defaults to false if not specified."

|

.. csv-table:: API Errors
   :header: "Error","Description","Example"

   "MULTI_NOT_FOUND","404","The custom feed specified doesn't exist or you don't have permission to view it.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_multi_{multipath}>`_


List own custom feeds
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/mine

*scope: read*

Fetch a list of custom feeds belonging to the current user.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "expand_srs","boolean","See same parameter in :ref:`Get <custom-feed-get>`."

|

.. csv-table:: API Errors
   :header: "Error","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_mine


List user custom feeds
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/user/{username}

*scope: read*

Fetch a list of custom feeds belonging to a given user.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "expand_srs","boolean","See same parameter in :ref:`Get <custom-feed-get>`."

|

.. csv-table:: API Errors
   :header: "Error","Description","Example"

   "USER_DOESNT_EXIST","400","The specified user does not exist.","
   ``{""fields"": [""username""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_mine


.. _custom-feed-create:

Create
~~~~~~

.. http:post:: /api/multi/user/{username}/m/{feed_name}
.. http:put:: /api/multi/user/{username}/m/{feed_name}

*scope: subscribe*

Create a custom feed.

Use POST to create a custom feed.
Responds with a `MULTI_EXISTS` API error and HTTP 409 Conflict if it already exists.

Use PUT to create or update a custom feed.
The `expand_srs` parameter only works with `PUT` requests.

Custom feed attributes are specified using the `model` parameter which takes JSON data.
A desciption of the valid JSON keys as follows:

.. csv-table:: JSON fields for `model` parameter
   :header: "Field","Type (hint)","Description"

   "display_name?","string","No longer than 50 characters. Defaults to feed name."
   "description_md?","string","Raw markdown description text. Defaults to empty string."
   "icon_img?","string","One of `png`, `jpg`, `jpeg`?"
   "key_color?","string","6-digit rgb hex color with optional leading hash. E.g., `#AABBCC`. Default: `null`."
   "subreddits?","object array","An array of objects containing a `name` key whose value is a subreddit name."
   "visibility?","string","One of `private`, `public`, `hidden`. Default: `private`."

The newly created custom feed object is returned, with a 201 HTTP status code.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "model","string","A string of JSON data."
   "expand_srs","boolean","This parameter only works with `PUT` not `POST` requests."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "JSON_PARSE_ERROR","400","The `model` parameter was not specified or contains badly formatted JSON.","
   ``{""fields"": [""model""], ""explanation"": ""Sorry, something went wrong. Double-check things and try again."", ""message"": ""Bad Request"", ""reason"": ""JSON_PARSE_ERROR""}``
   "
   "MULTI_CANNOT_EDIT","403","* The username specified does not exist.

   * You don't have permission to create a custom feed there.","
   ``{""fields"": [""multipath""], ""explanation"": ""you can't change that multireddit"", ""message"": ""Forbidden"", ""reason"": ""MULTI_CANNOT_EDIT""}``
   "
   "MULTI_EXISTS","409","A `POST` HTTP request was used and the custom feed already exists.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit already exists"", ""message"": ""Conflict"", ""reason"": ""MULTI_EXISTS""}``
   "
   "BAD_IMAGE","400","Bad value for `icon_img` in `model` parameter.","
   ``{""fields"": [""icon_img""], ""explanation"": ""image problem"", ""message"": ""Bad Request"", ""reason"": ""BAD_IMAGE""}``
   "
   "JSON_INVALID","400","The JSON structure specified by the `model` parameter is unexpected.","
   ``{""explanation"": ""unexpected JSON structure"", ""message"": ""Bad Request"", ""reason"": ""JSON_INVALID""}``
   "
   "TOO_LONG","400","The text specified by `display_name` is over 50 characters.","
   ``{""fields"": [""display_name""], ""explanation"": ""This field must be under 50 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_multi_{multipath}>`_


Update
~~~~~~

See :ref:`Create <custom-feed-create>`.

Use a PUT request to update.


Delete
~~~~~~

.. http:delete:: /api/multi/user/{username}/m/{feed_name}

*scope: subscribe*

Delete a custom feed.

Returns zero bytes on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","* The custom feed name specified does not exist.

   * The username specified does not exist.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "
   "MULTI_CANNOT_EDIT","403","You don't have permission to delete the specified custom feed because it does not belong to you.","
   ``{""fields"": [""multipath""], ""explanation"": ""you can't change that multireddit"", ""message"": ""Forbidden"", ""reason"": ""MULTI_CANNOT_EDIT""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_multi_{multipath}>`_


Duplicate
~~~~~~~~~

.. http:post:: /api/multi/copy

*scope: subscribe*

Copy a custom feed.

The description for the new custom feed will be like "copied from u/spez" etc. unless overridden by the
`description_md` parameter.

Returns the newly created custom feed object.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "from","A custom feed path. E.g., `/user/Pyprohly/m/test2`. It must be `/user/` and not `/u/`."
   "to","Destination custom feed path."
   "display_name","string","A new display name for the copied custom feed. A string no longer than 50 characters.
   If not specified, the feed name is used."
   "description_md","string","New description text for the copied custom feed. If not specified, the description
   will be like `copied from u/spez`."
   "expand_srs","boolean","See same parameter in :ref:`Get <custom-feed-get>`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","The `from` parameter was not specified or the path specified was not found.","
   ``{""fields"": [""from""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "
   "BAD_MULTI_PATH","400","* (1) The `to` parameter was not specified.

   * (2) The path specified by `to` parameter was not valid.","
   (1): ``{""explanation"": ""invalid multi path"", ""message"": ""Bad Request"", ""reason"": ""BAD_MULTI_PATH""}``

   (2): ``{""fields"": [""to""], ""explanation"": ""invalid multi path"", ""message"": ""Bad Request"", ""reason"": ""BAD_MULTI_PATH""}``
   "
   "MULTI_EXISTS","409","The destination custom feed (at `to`) aleady exists.","
   ``{""fields"": [""to""], ""explanation"": ""that multireddit already exists"", ""message"": ""Conflict"", ""reason"": ""MULTI_EXISTS""}``
   "
   "TOO_LONG","400","The text specified by `display_name` is over 50 characters.","
   ``{""fields"": [""display_name""], ""explanation"": ""This field must be under 50 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_multi_copy


Get description
~~~~~~~~~~~~~~~

.. http:get:: /api/multi/user/{username}/m/{feed_name}/description

*scope: read*

Get only a custom feed's description.

Example output::

   {"kind": "LabeledMultiDescription",
    "data": {"body_html": "<!-- SC_OFF --><div class="md"><p>My "
                          "description</p>\n"
                          "</div><!-- SC_ON -->",
             "body_md": "My description"}}

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","* The custom feed name specified does not exist.

   * The username specified does not exist.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_multi_{multipath}_description>`_


Set description
~~~~~~~~~~~~~~~

.. http:put:: /api/multi/user/{username}/m/{feed_name}/description

*scope: read*

Change a custom feed's description.

The `model` parameter takes a JSON object with one key: `body_md`. The value should be the new
markdown text description for the custom feed.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "model","string","A string of JSON data."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","* The custom feed name does not exist.

   * The username specified does not exist.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "
   "JSON_PARSE_ERROR","400","The `model` parameter was not specified or contains badly formatted JSON.","
   ``{""fields"": [""model""], ""explanation"": ""Sorry, something went wrong. Double-check things and try again."", ""message"": ""Bad Request"", ""reason"": ""JSON_PARSE_ERROR""}``
   "
   "JSON_MISSING_KEY","400","The JSON specified by the `model` parameter is missing the `body_md` key.","
   ``{""fields"": [""body_md""], ""explanation"": ""JSON missing key: \""body_md\"""", ""message"": ""Bad Request"", ""reason"": ""JSON_MISSING_KEY""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#PUT_api_multi_{multipath}_description>`_


Check subreddit in custom feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: read*

Tell if a subreddit is in a custom feed.

* If the specified subreddit is in the custom feed, an object like ``{'name': 'IAmA'}`` is returned.
* If the specified subreddit exists and isn't in the custom feed a 500 HTTP error is raised.
* If the specified subreddit doesn't exist at all then a `SUBREDDIT_NOEXIST` API error is returned.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","* The custom feed name does not exist.

   * The username specified does not exist.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "
   "SUBREDDIT_NOEXIST","400","The specified subreddit does not exist at all.","
   ``{""fields"": [""srname""], ""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "500","The specified subreddit exists and isn't in the custom feed.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_multi_{multipath}_r_{srname}>`_


Add to custom feed
~~~~~~~~~~~~~~~~~~

.. http:put:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: subscribe*

Add a subreddit to a custom feed.

The `{username}` component of the URL is mostly ignored, it doesn't have to match the current user's name.

If the feed name specified by the `{feed_name}` component of the URL doesn't exist, it will be created.
The new custom feed name will be lower cased and it will contain the subreddit specified.

The endpoint takes a mandatory `model` parameter that requires a `name` key with a value that is supposedly
meant to be the target subreddit name, but the subreddit name is already specified in the URL and the `model`
parameter seems to be ignored. You can just always send ``{"name": "abc"}``.

Returns an object like ``{"name": "pics"}`` on success.

If the custom feed already contains the subreddit it is treated as a success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "model","string","A string of JSON data."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "SUBREDDIT_NOEXIST","400","The specified subreddit (in the URL) does not exist.","
   ``{""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "
   "BAD_SR_NAME","400","The value specified by `model`s `name` key is not valid.","
   ``{""fields"": [""name""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#PUT_api_multi_{multipath}_r_{srname}>`_


Bulk add to custom feed
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/multi/add_srs_bulk

*scope: subscribe*

Bulk add subreddits to a custom feed.

Returns the custom feed object.

If any of the subreddit names in `sr_names` doesn't exist, the request will fail with a 500 HTTP
(and none of the subreddits will be added).

The `sr_names` limit is unknown. Clients should assume a limit of 100 subreddit names.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "path","string","A string of the form `/user/{user}/m/{feed}`."
   "sr_names","string","A comma delimited list of subreddit names to add."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "500","* The `path` parameter was not specified or was empty.

   * The `sr_names` parameter was not specified or was empty.

   * The custom feed doesn't exist.

   * The username specified does not exist.

   * One of the subreddits specified in the `sr_names` list does not exist.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "


Remove from custom feed
~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: subscribe*

Remove a subreddit from a custom feed.

If the specified subreddit does not exist then it is treated as a success.

Returns zero bytes on success.

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "MULTI_NOT_FOUND","404","* The custom feed name does not exist.

   * The username specified does not exist.","
   ``{""fields"": [""multipath""], ""explanation"": ""that multireddit doesn't exist"", ""message"": ""Not Found"", ""reason"": ""MULTI_NOT_FOUND""}``
   "
   "MULTI_CANNOT_EDIT","403","You don't have permission to modify the specified custom feed.","
   ``{""fields"": [""multipath""], ""explanation"": ""you can't change that multireddit"", ""message"": ""Forbidden"", ""reason"": ""MULTI_CANNOT_EDIT""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_multi_{multipath}_r_{srname}>`_
