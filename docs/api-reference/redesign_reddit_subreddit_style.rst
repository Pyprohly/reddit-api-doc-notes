
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

   "filepath","string","The file name (either a base name or a full path) of the image file to upload.
   Example: `image.png`."
   "mimetype","string","The mimetype of the image file to upload. It does not have to match the
   extension of the `filepath`. Example: `image/png`."
   "imagetype","string","Either `bannerBackgroundImage`, `bannerPositionedImage`, `secondaryBannerPositionedImage`,
   or `mobileBannerImage`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "INVALID_OPTION","400","An invalid value was provided for `imagetype`","
   ``{""fields"": [""imagetype""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "


Configure banner settings
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/structured_styles/{subreddit}

*scope: (unknown)*

Set banner images in a subreddit.

If any of the image parameters were used
(`bannerBackgroundImage`, `bannerPositionedImage`, `secondaryBannerPositionedImage`, or `mobileBannerImage`)
then a JSON object with one key `websocketUrl` is returned.
Otherwise, an empty JSON object is returned on success.

Use an empty string to remove an image.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "bannerHeight","string","Either `small`, `medium`, `large`. If given value is not valid, `small` is used."
   "bannerBackgroundColor","string","A hex color. If given value is not valid, `#33a8ff` is used."
   "bannerBackgroundImage","string","The location of the new banner image."
   "bannerBackgroundImagePosition","string","Either `cover` or `tiled`. If given value is not valid, `cover` is used."
   "bannerPositionedImage","string","The location of the new banner overlay image."
   "bannerPositionedImagePosition","string","Either `left`, `centered`, or `right`."
   "secondaryBannerPositionedImage","string","The location of the new banner overlay hover image."
   "mobileBannerImage","string","The location of the new mobile banner image."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "INVALID_ARGUMENT","400","The specified image location was incorrect.","
   ``{""fields"": [""bannerBackgroundImage""], ""explanation"": ""Invalid value for bannerBackgroundImage"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ARGUMENT""}``
   "
