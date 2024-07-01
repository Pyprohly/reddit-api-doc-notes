
Miscellaneous
=============

Actions
-------

OAuth2 Scopes
~~~~~~~~~~~~~

.. http:get:: /api/v1/scopes

*scope: (any)*

Retrieve descriptions of reddit's OAuth2 scopes.

If no scopes are given, information on all scopes are returned.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "scopes","string","A space separated list of scopes."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "400","An invalid scope string was specified.","
   ``This is an error that should never occur.  You win.``
   "


Search reddit submissions and subreddits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/search

*scope: read*

Search for submissions and/or subreddits on Reddit.

Use `GET /search` to search all of Reddit.
Use `GET [/r/{subreddit}]/search` and pass `restrict_sr: 1` to search within a subreddit.

This endpoint returns a :ref:`paginated listing <listings-overview>`.

The `sr_detail` parameter is not supported (despite the offical docs saying so).

If `q` is empty or not specified, an empty listing structure is returned::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "facets": {}, "after": null, "geo_filter": "", "children": [], "before": null}}

The endpoint can sometimes return `"{}"` (string of empty object). For instance if
``params={'q': 'a', 'type': 'sr', 'limit': '1'}`` is sent.
This might only happen when `type: sr`, not sure.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "...",".",":ref:`Listing common parameters <listings-overview>`."
   "q","string","A search query."
   "restrict_sr","boolean","If truthy, results are limited to the subreddit
   specified in the URL. If no subreddit is specified in the URL, this parameter
   is ignored, hence, you can always send this parameter.

   This parameter is ignored if `type` is not `link`.

   Default: false."
   "type","string","One of: `link`, `sr`, or `user`. Default: `link`.

   The documentation says this parameter takes a comma-separated list, but this is no longer the case.
   You used to able to get an array of paginated listings by specifying a comma-separated list.
   If you specify a comma-separated list of `link`, `sr`, `user`, one will be chosen in that order of
   precedence. If any of the strings are invalid options, they are ignored.

   If `link` is specified, a paginated listing of matching submissions is returned.
   This is the default if the parameter is not specified.

   If `sr` is specified, a paginated listing of matching subreddits is returned.
   The functionality is identical to `GET /subreddits/search <subreddit_search_subreddits>`_.

   If `user` is specified, an empty paginated listing structure is always returned.
   To search users on Reddit use `GET /users/search <user_search_users>`_ instead.

   So basically, only `link` is useful.
   "
   "t","string","Time filter. Valid options: `all`, `hour`, `day`, `week`, `month`, `year`. Default: `all`."
   "sort","string","Submission sort. Either `relevance`, `hot`, `top`, `new`, or `comments`. Default: `relevance`.

   This parameter is ignored if `type` is not `link`."


Convert rich text json to markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert markdown to rich text json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/convert_rte_body_format

*scope: (unknown)*

Convert rich text json to markdown or vice versa.

Example output for `output_mode: rtjson`::

   {
      "output": {"document": [{"c": [{"e": "text", "t": "asdf"}], "e": "par"}]},
      "output_mode": "rtjson",
      "assets": []
   }

Example output for `output_mode: markdown`::

   {
      "output": "asdf\n\n&#x200B;",
      "output_mode": "markdown",
      "assets": []
   }

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "output_mode","string","Either `rtjson` or `markdown`."
   "markdown_text","string","If `output_mode: rtjson`, the markdown text to convert to rich text JSON."
   "richtext_json","string","If `output_mode: markdown`, the rich text JSON to convert to markdown text."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","* The `output_mode` parameter was not specified.

   * The value specified for the `output_mode` parameter is not valid."
