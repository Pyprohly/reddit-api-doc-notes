
Flair Emoji
===========

Overview
--------

Put little images in your flairs with flair emojis.

Reddit help article: `<https://mods.reddithelp.com/hc/en-us/articles/360010560371-Emojis>`_.


Schema
~~~~~~

.. csv-table:: Custom Feed Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "url","string","The emoji image file."
   "created_by","string","The full ID36 (prefixed with `t2_`) of the user who added the emoji."
   "mod_flair_only","boolean","Whether the emoji can only be used by a moderator."
   "post_flair_allowed","boolean","Whether the emoji can be used on post flairs."
   "user_flair_allowed","boolean","Whether the emoji can be used on user flairs."


Actions
-------

Get subreddit emojis
~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/{subreddit}/emojis/all

*scope: read*

Get a list of all emojis for a subreddit.

The response includes reddit-wide 'snoomoji' emojis as well as custom emojis for the
subreddit specified in the request URL.

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The specified subreddit cannot be accessed."
   "500","The specified subreddit does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_v1_{subreddit}_emojis_all>`_


.. _emoji-upload:

Upload
~~~~~~

.. http:post:: /api/v1/{subreddit}/emoji_asset_upload_s3

*scope: structuredstyles*

Upload an emoji image.

Uploading and adding an emoji to a subreddit is two separate steps. The uploading step
can further be broken down into two steps: obtaining an upload lease and then uploading the
emoji image to the Amazon Simple Storage Service bucket specified in the lease.

Use `POST /api/v1/{subreddit}/emoji_asset_upload_s3` to obtain an upload lease for your emoji
image. In the response data there will be a field called `action` whose value is a URL but is
missing the `https:` prefix. Prepend `https:` to this URL and add your emoji image to a field
named `file` in a multipart request, along with the parameters in the `fields` array from the
upload lease as form data in the multipart request.

The `action` is typically `//reddit-uploaded-emoji.s3-accelerate.amazonaws.com` for this endpoint.
The action endpoint will return XML data. Remember to check for a bad status in the response.
If the media was too large, this endpoint returns 400 Bad Request, and a message indicating this
is included in the XML data.

The `s3_key` for use in the adding stage is the value of `s3UploadLease.fields.key` in the lease.

The file name specified by `filepath` doesn't appear to have any significance.
The name of the file when you download it from the site will always be the name of the emoji,
plus the file extension.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "filepath","string","The file name (base name, not a full path) of the image file to upload.
   Example: `image.png`."
   "mimetype","string","The mimetype of the image file to upload. It does not have to match the
   extension of the `filepath`. Example: `image/png`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","* The `filepath` or `mimetype` form parameter was not specified or the value was empty.

   * The file extension in the name specified by `filepath` is not supported.

   * Invalid value specified for `mimetype`, or the type is not supported."
   "403","The specified subreddit cannot be accessed."
   "500","The specified subreddit does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_v1_{subreddit}_emoji_asset_upload_s3.json>`_


Add
~~~

.. http:post:: /api/v1/{subreddit}/emoji

*scope: structuredstyles*

Add a new emoji to a subreddit.

By specifying the name of an existing emoji the permissions on that emoji can be changed,
but in general this endpoint should not be used to modify the permissions of an emoji since
this endpoint requires knowing the S3 key of the emoji, which cannot be re-obtained if lost.

The name of an emoji cannot be changed with this endpoint. If the same S3 key is used with a different
`name` value then a new emoji will be created.

If the `s3_key` is not valid the request will appear to succeed but no emoji will be added to the subreddit.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "s3_key","string","The key of the Amazon S3 bucket containing the emoji image."
   "name","string","A name for the emoji. Up to 24 characters. This will be the text used to write the emoji. E.g., `:name:`."
   "mod_flair_only","boolean","Whether the emoji can only be used by mods. Default: false."
   "post_flair_allowed","boolean","Whether the emoji can be used on post flairs. Default: true."
   "user_flair_allowed","boolean","Whether the emoji can be used on user flairs. Default: true."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The `s3_key` parameter was not specified or was empty.

   * More than 24 characters were used for the `name` parameter.

   * The `name` specified was invalid because it contains a space or other invalid characters.
     Name can only contain letters, numbers, underscores, or hyphens."
   "403","You do not have permission to add an emoji to the specified subreddit."
   "500","* The `name` parameter was not specified or was empty.

   * The specified subreddit does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_v1_{subreddit}_emoji.json>`_


Modify emoji permissions
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/{subreddit}/emoji_permissions

Change emoji permissions.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","The target emoji name."
   "mod_flair_only","boolean","Whether the emoji can only be used by mods. Default: false."
   "user_flair_allowed","boolean","Whether the emoji can be used on user flairs. Default: true."
   "post_flair_allowed","boolean","Whether the emoji can be used on post flairs. Default: true."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You do not have permission to make changes to the specified subreddit."
   "404","The emoji specified by `name` does not exist."
   "500","* The `name` parameter was not specified or was empty.

   * The specified subreddit does not exist."


Delete
~~~~~~

.. http:delete:: /api/v1/{subreddit}/emoji/{emoji_name}

*scope: structuredstyles*

Delete a flair emoji.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The specified emoji does not exist.

   * The specified subreddit does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_v1_{subreddit}_emoji_{emoji_name}>`_


Set custom emoji size
~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/{subreddit}/emoji_custom_size

*scope: structuredstyles*

Enable subreddit custom emoji sizing on the subreddit.

Omit either `width` or `height` parameters to disable custom emoji sizing.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "width","integer","An integer from 16 to 40.

   Parameter is ignored if a non-number is passed."
   "height","integer","Likewise."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You do not have permission to make changes to the specified subreddit."
   "500","The specified subreddit does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_v1_{subreddit}_emoji_custom_size>`_


Enable/disable emojis in subreddit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/enable_emojis_in_sr

Enable/disable flair emojis in a subreddit.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "subreddit","string","The target subreddit name."
   "enable","boolean","True for enable, false for disable. Default: false."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You do not have permission to set emoji options in the target subreddit."
   "500","* The `subreddit` parameter was not specified or was empty.

   * The specified subreddit does not exist."
