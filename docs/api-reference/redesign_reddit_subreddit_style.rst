
Redesign Reddit Subreddit Style
===============================

Actions
-------

Upload asset
~~~~~~~~~~~~

.. http:post:: /api/v1/style_asset_upload_s3/{subreddit}

*scope: (unknown)*

Upload an image for use in the Reddit redesign UI.

This endpoint is used for obtaining an upload lease.

The upload process is similar to Flair Emoji image uploads, but the endpoint wants an extra `imagetype` parameter.
See :ref:`Emoji upload <emoji-upload>`.

The `action` is typically `//reddit-subreddit-uploaded-media.s3-accelerate.amazonaws.com` for this endpoint.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "imagetype","string","Either `bannerBackgroundImage`, `bannerPositionedImage`, `secondaryBannerPositionedImage`,
   or `mobileBannerImage`."
   "filepath","string","The file name (either a base name or a full path) of the image file to upload.
   Example: `image.png`."
   "mimetype","string","The mimetype of the image file to upload. It does not have to match the
   extension of the `filepath`. Example: `image/png`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "BAD_IMAGE","400","* The file extension of the file name specified by `filepath` is invalid
     (because doesn't end with `.png` or `.jpg`, etc.).

   * The specified `mimetype` is invalid.","
   ``{""fields"": [""filepath""], ""explanation"": ""image problem"", ""message"": ""Bad Request"", ""reason"": ""BAD_IMAGE""}``
   "
   "INVALID_OPTION","400","An invalid value was provided for `imagetype`","
   ``{""fields"": [""imagetype""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "


Modify banner image settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/structured_styles/{subreddit}

*scope: (unknown)*

Set banner images in a subreddit.

If any of the image parameters were used
(`bannerBackgroundImage`, `bannerPositionedImage`, `secondaryBannerPositionedImage`, or `mobileBannerImage`)
then a JSON object with one key `websocketUrl` is returned.
Otherwise, an empty JSON object is returned on success.

Parameters that are not specified are ignored.

Use an empty string to set a setting to its default (e.g., to remove an image).

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "bannerHeight","string","Either `small`, `medium`, `large`. If given value is not valid, `small` is used."
   "bannerBackgroundColor","string","A hex color. If given value is not valid, `#33a8ff` is used."
   "bannerBackgroundImage","string","The location of the a banner image."
   "bannerBackgroundImagePosition","string","Either `cover` or `tiled`. If given value is not valid, `cover` is used."
   "bannerPositionedImage","string","The location of the a banner overlay image."
   "bannerPositionedImagePosition","string","Either `left`, `centered`, or `right`."
   "secondaryBannerPositionedImage","string","The location of the a banner overlay hover image."
   "mobileBannerImage","string","The location of the a mobile banner image."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "INVALID_ARGUMENT","400","The specified image location was incorrect.","
   ``{""fields"": [""bannerBackgroundImage""], ""explanation"": ""Invalid value for bannerBackgroundImage"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ARGUMENT""}``
   "
