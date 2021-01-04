
Custom Feed
===========

Overview
--------

Schema
~~~~~~

.. csv-table:: Custom Feed Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "display_name","string",""
   "name","string",""
   "can_edit","boolean",""
   "description_html","string",""
   "num_subscribers","integer",""
   "copied_from","unknown?",""
   "icon_url","string",""
   "subreddits","object array","E.g., ``[{\"name\": \"pics\"}, {\"name\": \"u_spez\"}]``"
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "visibility","string","Either `private` or `public`."
   "over_18","boolean",""
   "path","string","E.g., `/user/pyprohly/m/asdf/`"
   "owner","string","Username of the owner. E.g., `Pyprohly`."
   "owner_id","string","The full ID36 of the owner. E.g., `t2_4x25quk`."
   "key_color","string",""
   "is_subscriber","boolean",""
   "description_md","string",""
   "is_favorited","boolean",""


Actions
-------

.. _custom_feed_get:

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
:ref:`fetching a subreddit <get_api_info>` object directly (it contains roughly half the attributes). It also slightly
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
   :escape: \

   "expand_srs","boolean","Whether to provide extra subreddit attributes.

   If false, the `subreddits` key holds an array of objects containing one key: `name`.
   If true, the `subreddits` key holds an array of objects containing keys: `name` and `data`.

   Defaults to false if not specified."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","The custom feed doesn't exist or you don't have permission to view it.

      *that multireddit doesn't exist* -> *multipath*"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_{multipath}


List own custom feeds
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/mine

*scope: read*

Fetch a list of custom feeds belonging to the current user.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "expand_srs","boolean","See same parameter in :ref:`Get <custom_feed_get>`."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_mine


List user custom feeds
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/user/{username}

*scope: read*

Fetch a list of custom feeds belonging to a given user.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "expand_srs","boolean","See same parameter in :ref:`Get <custom_feed_get>`."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "USER_DOESNT_EXIST","   *that user doesn't exist* -> *username*"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_mine


.. _custom_feed_create:

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

.. csv-table:: `model` parameter JSON fields
   :header: "Field","Type (hint)","Description"
   :escape: \

   "display_name?","string","No longer than 50 characters. Defaults to name."
   "description_md?","string","Raw markdown description text. Defaults to empty string."
   "icon_img?","string","One of `png`, `jpg`, `jpeg`?"
   "key_color?","string","6-digit rgb hex color with optional leading hash. E.g., `#AABBCC`. Default: `null`.".
   "subreddits?","object array","An array of objects containing a `name` key whose value is a subreddit name."
   "visibility?","string","One of `private`, `public`, `hidden`. Default: `private`."

The newly created custom feed object is returned, with a 201 HTTP status code.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "model","string","A string of JSON data."
   "expand_srs","boolean","This parameter only works with `PUT` not `POST` requests."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "JSON_PARSE_ERROR","The `model` parameter was not specified or contains badly formatted JSON.

      *unable to parse JSON data* -> *model*"
   "JSON_INVALID","The JSON structure specified by the `model` parameter is unexpected.

      *unexpected JSON structure* -> *subreddits*"
   "MULTI_CANNOT_EDIT","* The username specified does not exist.

   * You don't have permission to create a custom feed there.

      *you can't change that multireddit* -> *multipath*"
   "MULTI_EXISTS","A `POST` HTTP request was used and the custom feed already exists.

   A HTTP 409 Conflict status code is returned.

      *that multireddit already exists* -> *multipath*"
   "BAD_IMAGE","Bad value for `icon_img` in `model` parameter.

      *image problem* -> *icon_img*"
   "TOO_LONG","The text specified by `display_name` is over 50 characters.

      *this is too long (max: 50)* -> *display_name*"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_multi_{multipath}


Update
~~~~~~

See :ref:`Create <custom_feed_create>`.

Use a PUT request to update.


Delete
~~~~~~

.. http:delete:: /api/multi/user/{username}/m/{feed_name}

*scope: subscribe*

Delete a custom feed.

Returns zero bytes on success.

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"
   "MULTI_CANNOT_EDIT","You don't have permission to delete that custom feed.

      *you can't change that multireddit* -> *multipath*"

.. seealso:: https://www.reddit.com/dev/api/#DELETE_api_multi_{multipath}


Duplicate
~~~~~~~~~

.. http:post:: /api/multi/copy

*scope: subscribe*

Copy a custom feed.

The description for the new custom feed will be "copied from u/spez" etc. unless overridden by the
`description_md` parameter.

Returns the newly created custom feed object.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "from","A custom feed path. E.g., `/user/Pyprohly/m/test2`."
   "to","Destination custom feed path."
   "display_name","string","A new display name for the copied custom feed. A string no longer than 50 characters."
   "description_md","string","New description text for the copied custom feed."
   "expand_srs","boolean","See same parameter in :ref:`Get <custom_feed_get>`."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","The `from` parameter was not specified or the path specified was not found.

      *that multireddit doesn't exist* -> *from*"
   "BAD_MULTI_PATH","The `to` parameter was not specified.

      *invalid multi path*"
   "MULTI_EXISTS","The destination custom feed aleady exists.

   A HTTP 409 Conflict status code is returned.

      *that multireddit already exists* -> *to*"
   "TOO_LONG","The text specified by `display_name` is over 50 characters.

      *this is too long (max: 50)* -> *display_name*"

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

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_{multipath}_description


Set description
~~~~~~~~~~~~~~~

.. http:put:: /api/multi/user/{username}/m/{feed_name}/description

*scope: read*

Change a custom feed's description.

The `model` parameter takes a JSON object with one key: `body_md`. The value should be the new
markdown text description for the custom feed.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "model","string","A string of JSON data."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"
   "JSON_PARSE_ERROR","The `model` parameter was not specified or contains badly formatted JSON.

      *unable to parse JSON data* -> *model*"
   "JSON_MISSING_KEY","The JSON specified by the `model` parameter is missing the `body_md` key.

      *JSON missing key: \"body_md\"* -> *body_md*"

.. seealso:: https://www.reddit.com/dev/api/#PUT_api_multi_{multipath}_description


Check subreddit in custom feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: read*

Tell if a subreddit is in a custom feed.

If the specified subreddit exists in the custom feed, an object like ``{'name': 'IAmA'}`` is returned.
Otherwise a SUBREDDIT_NOEXIST API error is returned.

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"
   "SUBREDDIT_NOEXIST","The specified subreddit does not exist in the target custom feed.

   A HTTP 400 Bad Request status code is returned.

      *that subreddit doesn't exist* -> *srname*"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_multi_{multipath}_r_{srname}


Add subreddit to custom feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: subscribe*

Add a subreddit to a custom feed.

Returns an object like ``{"name": "pics"}`` on success. (The value is the `{sr_name}` component of the request URL.)

The endpoint takes a `model` parameter that requires a `name` key with a value that is supposedly meant to be
the target subreddit name, but the subreddit name is already specified in the URL and this `model` parameter
seems to otherwise be ignored. Just always send ``{"name": "aa"}``.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "model","string","A string of JSON data."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"
   "SUBREDDIT_NOEXIST","The specified subreddit (the `{sr_name}` component of the request URL)
   does not exist.

      *that subreddit doesn't exist*"
   "BAD_SR_NAME","The value specified by `model`s `name` key is not valid.

     *that name isn't going to work* -> *name*"

.. seealso:: https://www.reddit.com/dev/api/#PUT_api_multi_{multipath}_r_{srname}


Remove subreddit from custom feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /api/multi/user/{username}/m/{feed_name}/r/{sr_name}

*scope: subscribe*

Remove a subreddit from a custom feed.

If the specified subreddit does not exist then nothing happens.

Returns zero bytes on success.

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"
   "MULTI_NOT_FOUND","* The custom feed doesn't exist.

   * The username specified does not exist.

      *that multireddit doesn't exist* -> *multipath*"

.. seealso:: https://www.reddit.com/dev/api/#DELETE_api_multi_{multipath}_r_{srname}
