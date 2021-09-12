
Misc
====

Actions
-------

Search reddit submissions and subreddits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[WIP]

.. http:get:: [/r/{subreddit}]/search

*scope: read*

Search submissions and/or subreddits on Reddit.

This endpoint returns a :ref:`paginated listing <listings_overview>`.

This endpoint could return an array depending on the value of the `type` parameter.

The `sr_detail` parameter is not supported (despite the offical docs saying so).

If `q` is empty or not specified, an empty listing structure is returned::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "facets": {}, "after": null, "geo_filter": ", "children": [], "before": null}}

The endpoint can sometimes return `"{}"` (string of empty object). For instance if
`params={'q': 'a', 'type': 'sr', 'limit': '1'}` is sent.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "...",".",":ref:`Listing common parameters <listings_overview>`."
   "q","string","A search query."
   "restrict_sr","boolean","If truthy, results are limited to the subreddit
   specified in the URL. If no subreddit is specified in the URL, this parameter
   is ignored.

   This parameter is ignored if `type` is not `link`."
   "sort","string","Submission sort. Either `relevance`, `hot`, `top`, `new`, or `comments`. Default: `relevance`.

   This parameter is ignored if `type` is not `link` (even when `type: link,sr` is used)."
   "type","string","
   If value is `link`, a paginated listing of matching submissions is returned.
   This is the default if the `type` parameter is not specified.

   If value is `sr`, a paginated listing of matching subreddits is returned.
   The functionality is identical to `GET /subreddits/search <subreddit_search_subreddits>`_.

   If value is `user`, an empty paginated listing structure is always returned.
   To search users on Reddit see `GET /users/search <user_search_users>`_.

   If value is a comma delimited list of `link` and `sr`, in any order (`link,sr` or `sr,link`),
   an array of two objects is returned.
   The first is a paginated listing of subreddits that contains up to 3 matching subreddits.
   The second is a paginated listing of submissions.
   This data corresponds to the results shown in the UI (at `<https://www.reddit.com/search>`_).

   If `user` is combined in a comma separated list with `link` or `sr`, `user` is ignored.

   If a comma separated list is provided and any of the strings are invalid, they are ignored.

   If value is an empty string or is an invalid value (i.e., not one of `link`, `sr`, or `user`),
   defaults to `link`.

   This parameter is ignored (defaulting to `link`) if `restrict_sr` is truthy.
   "


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
   :escape: \

   "output_mode","string","Either `rtjson` or `markdown`."
   "markdown_text","string","If `output_mode: rtjson`, the markdown text to convert to rich text JSON."
   "richtext_json","string","If `output_mode: markdown`, the rich text JSON to convert to markdown text."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The `output_mode` parameter was not specified.

   * The value specified for the `output_mode` parameter is not valid."
