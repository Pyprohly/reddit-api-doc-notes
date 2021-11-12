
Wiki
++++

Wiki Page
=========

Overview
--------

Wiki page schema
~~~~~~~~~~~~~~~~

.. csv-table:: Wiki page schema
   :header: "Field","Type (hint)","Description"

   "content_md","string","The wiki page markdown content."
   "content_html","string","The wiki page content as HTML."
   "may_revise","boolean","Whether the current user may edit the wiki page."
   "revision_id","string","The revivsion UUID."
   "revision_date","integer","The UNIX timestamp of when the revision was commited."
   "revision_by","object","The author of the revision.

   The object is similar to the :ref:`User schema <user-schema>` except it's missing the
   `awardee_karma`, `awarder_karma`, and `total_karma` fields."
   "reason","string?","The revision message. Value is `null` if no message."


Wiki page revision schema
~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Wiki page revision schema
   :header: "Field","Type (hint)","Description"

   "id","string","The revision UUID."
   "page","string","The page name this revision belongs to."
   "timestamp","integer","The UNIX timestamp of when the revision was commited."
   "author","object","The author of the revision.

   The object is similar to the :ref:`User schema <user-schema>` except it's missing the
   `awardee_karma`, `awarder_karma`, and `total_karma` fields."
   "reason","string?","The revision message. Up to 256 characters long. Value is `null` if no message."
   "revision_hidden","boolean","Whether the revision is hidden."


Actions
-------

Get
~~~

.. http:get:: /r/{subreddit}/wiki/{page}

*scope: wikiread*

Get a wiki page.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "v","string","Specify a revision ID with this parameter to get the wiki page at that revision point."
   "v2","string","Documented but seems to have no effect in the JSON API."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PAGE_NOT_CREATED","404","The specified wiki page does not exist.","
   ``{""reason"": ""PAGE_NOT_CREATED"", ""message"": ""Not Found""}``
   "
   "INVALID_REVISION","404","The revision UUID specified by `v` does not exist.","
   ``{""reason"": ""PAGE_NOT_CREATED"", ""message"": ""Not Found""}``
   "


Edit
~~~~

.. http:post:: /r/{subreddit}/api/wiki/edit

*scope: wikiedit*

Edit a wiki page.

If the specifed content matches the current content of the wiki page, the edit will not go through.

Returns empty JSON object on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "page","string","The name of a page. If it doesn't exist it will be created.

   If not specified or an empty string, defaults to `index`."
   "content","string","Specify markdown text."
   "previous","string","A revision UUID as an ancestor for this edit in a three-way merge."
   "reason","string","An edit message for this revision. Empty string is treated the same as not specifying the parameter."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "WIKI_CREATE_ERROR","400","You do not have permission to edit the wiki page.","
   ``{""reason"": ""WIKI_CREATE_ERROR"", ""message"": ""Bad Request""}``
   "


Revert
~~~~~~

.. http:post:: /r/{subreddit}/api/wiki/revert

*scope: modwiki*

Revert a wiki page to a previous revision.

This creates a new edit with content matching that of the specified revision.

If multiple requests specifying the same revision UUID are made, only the first one will have an effect,
since the content will be the same.

The revision message will be something like 'reverted back 53 minutes'.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "page","string","The name of a page. If it doesn't exist it will be created.

   If not specified or an empty string, defaults to `index`."
   "revision","string","A wiki page revision UUID."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "INVALID_REVISION","400","* The reivision UUID specified does not exist.

   * The `revision` parameter was not specified.","
   ``{""reason"": ""INVALID_REVISION"", ""message"": ""Bad Request""}``
   "


.. _wiki-get-revisions:

Get revisions
~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/wiki/revisions/{page}

*scope: wikiread*

Get wiki page revision log.

This endpoint returns a :ref:`paginated listing <listings-overview>`.

The `sr_detail` parameter is not supported (despite being documented).

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PAGE_NOT_CREATED","404","The wiki page specified in the URL does not exist.","
   ``{""reason"": ""PAGE_NOT_FOUND"", ""message"": ""Not Found""}``
   "
   "WIKI_DISABLED","403","The specified subreddit does not have wikis enabled.","
   ``{""reason"": ""WIKI_DISABLED"", ""message"": ""Forbidden""}``
   "
   "private","403","You do not have access to the specified subreddit; it is private.","
   ``{""reason"": ""private"", ""message"": ""Forbidden"", ""error"": 403}``
   "


Get discussions
~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/wiki/discussions/{page}

*scope: wikiread*

Get link submissions linking to a particular wiki page.

This endpoint returns a :ref:`paginated listing <listings-overview>`.

The `sr_detail` parameter is not supported (despite being documented).

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PAGE_NOT_CREATED","404","The wiki page specified in the URL does not exist.","
   ``{""reason"": ""PAGE_NOT_FOUND"", ""message"": ""Not Found""}``
   "
   "private","403","You do not have access to the specified subreddit; it is private.","
   ``{""reason"": ""private"", ""message"": ""Forbidden"", ""error"": 403}``
   "


Get settings
~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/wiki/settings/{page}

*scope: modwiki*

Get link submissions linking to a particular wiki page.

Retrieve the current permission settings for a wiki page.

.. csv-table:: Wiki page settings
   :header: "Field","Type (hint)","Description"

   "permlevel","integer","The permission level specifing who can edit this wiki page.

   0: use subreddit wiki permissions
   1: only approved wiki contributors for this page may edit
   2: only mods may edit and view"
   "editors","object array","A list of editors for the wiki page."
   "listed","boolean","True if the wiki page is listed in the wiki page list."

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PAGE_NOT_CREATED","404","The wiki page specified in the URL does not exist.","
   ``{""reason"": ""PAGE_NOT_FOUND"", ""message"": ""Not Found""}``
   "
   "MOD_REQUIRED","403","You are not a moderator of the specified subreddit.","
   ``{""reason"": ""MOD_REQUIRED"", ""message"": ""Forbidden"", ""explanation"": ""You must be a moderator to do that.""}``
   "
   "banned","404","The specified subreddit is banned.","
   ``{""reason"": ""banned"", ""message"": ""Not Found"", ""error"": 404}``
   "


Set settings
~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/wiki/settings/{page}

*scope: modwiki*

Update the permissions and visibility of a particular wiki page.

Returns the new settings.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "permlevel","integer","The permission level."
   "listed","boolean","Whether the wiki page should be publicly listed. Default: false."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","The `permlevel` parameter was not specified."


.. _wiki-add-editor:

Add editor
~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/wiki/alloweditor/add

*scope: modwiki*

Add a user as an editor for this wiki page.

If the user is already added, it is treated as a success.

Returns an empty JSON object.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "page","string","The name of a page.

   If not specified or an empty string, defaults to `index`."
   "username","string","The name of a user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "UNKNOWN_USER","404","* The specified user does not exist.

   * The `username` parameter was not specified.","
   ``{""reason"": ""UNKNOWN_USER"", ""message"": ""Not Found""}``
   "


Remove editor
~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/wiki/alloweditor/del

Details are the same as :ref:`wiki-add-editor`.


Wiki General
============

Actions
-------

Get all revisions
~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/wiki/revisions

Get a revision log for all wiki pages.

Details are the same as :ref:`getting wiki page specific revisions <wiki-get-revisions>`.


List wiki pages
~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/wiki/pages

*scope: wikiread*

Get a list of wiki pages in a subreddit.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "private","403","You do not have access to the specified subreddit: it is private.","
   ``{""reason"": ""private"", ""message"": ""Forbidden"", ""error"": 403}``
   "
   "banned","404","You do not have access to the specified subreddit: it is banned.","
   ``{""reason"": ""banned"", ""message"": ""Not Found"", ""error"": 404}``
   "


Toggle revision visibility
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/wiki/hide

*scope: modwiki*

Toggle the public visibility of a wiki page revision.

Returns a JSON object containing one key, `status`, whose value is a boolean
indicating whether the wiki page revision is now hidden.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "page","string","The name of a page. If it doesn't exist it will be created.

   If not specified or an empty string, defaults to `index`."
   "revision","string","A wiki page revision UUID."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PAGE_NOT_CREATED","404","The specified wiki page does not exist.","
   ``{""reason"": ""PAGE_NOT_FOUND"", ""message"": ""Not Found""}``
   "
   "INVALID_REVISION","404","The revision UUID specified by `v` does not exist.","
   ``{""reason"": ""PAGE_NOT_CREATED"", ""message"": ""Not Found""}``
   "
