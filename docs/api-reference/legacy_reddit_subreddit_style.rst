
Legacy Reddit Subreddit Style
=============================

Actions
-------

Get stylesheet object
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/about/stylesheet

*scope: (unknown)*

Get a subreddit's stylesheet information.

This endpoint can be called without being a moderator of the target subreddit. You don't even have to be logged in.

If the target subreddit does not exist, an empty listing object is returned::

   {"kind": "Listing", "data": {"after": None, "dist": 0, "modhash": ", "geo_filter": ", "children": [], "before": None}}

Schema:

* `subreddit_id` (string): The subreddit's full ID36 (`t5_` prefixed).
* `stylesheet` (string): The CSS content.
* `images` (object array): Information about the stylesheet's images.

  * `name` (string): Name of the image. E.g., `B16F1EE2-D3B8-4D89-A515-78E3A7A90A43`.
  * `url` (string): The url of the image.
  * `link` (string): Same as `name` but affixed with `url(%%` and `%%)`. E.g., `url(%%cat-image%%)`.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."


Get stylesheet raw css
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/stylesheet

*scope: (unknown)*

Get the raw stylesheet CSS text of a subreddit.

The CSS is a minified version of the CSS that `GET [/r/{subreddit}]/about/stylesheet` returns.

This endpoint returns a 404 HTTP error if the subreddit's stylesheet page is empty.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The subreddit does not have a stylesheet set."


Edit stylesheet
~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/subreddit_stylesheet

*scope: modconfig*

Update a subreddit's stylesheet.

The stylesheet can also be updated by editing the `config/stylesheet` wiki page.

Returns ``{"json": {"errors": []}}`` on success.

If `stylesheet_contents` is empty or not specified it is treated as a success and the stylesheet
will not be changed in any way.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."
   "op","string","Specify 'save'.

   The other documented option is `preview` but specifying this will cause the endpoint to
   succeed with no change occuring.

   If not specified, the endpoint succeeds with no change occuring."
   "stylesheet_contents","string","The new stylesheet CSS content.

   If not specified, defaults to empty string."
   "reason","string","An edit message for the wiki page revision. A 256 character limit."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_CSS","200","The CSS provided was badly formatted.","
   ``{""json"": {""errors"": [[""BAD_CSS"", ""invalid css"", ""stylesheet_contents""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_subreddit_stylesheet


.. _upload-stylesheet-image:

Upload stylesheet image
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/upload_sr_img

*scope: modconfig*

Upload an image for use in the subreddit stylesheet, set the subreddit icon, mobile icon, or mobile banner.

* `upload_type: img`: Upload a subreddit stylesheet image. The `name` parameter must be used.
* `upload_type: header`: Set the subreddit icon.
* `upload_type: icon`: Set the subreddit mobile icon.
* `upload_type: banner`: Set the subreddit mobile banner.

When `upload_type: img`, if an image with the specified `name` already exists, it will be replaced.
This does not affect the stylesheet immediately but will take effect the next time the stylesheet is saved.

Returns a structure like the following on success::

   {"errors": [], "img_src": "https://b.thumbs.redditmedia.com/eG0kU0JZnNN5gvF-yw7CKaMi8oXTI6XmMgToSmckkLs.png", "errors_values": []}

The URL of the (non-stylesheet) subreddit images can be retrieved via :ref:`subreddit schema <subreddit-schema>` fields:

* Icon: `header_img`.
* Mobile icon: `icon_img`.
* Mobile banner: `banner_img`.

.. csv-table:: Multipart Form Data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."
   "upload_type","string","Either: `img`, `header`, `icon`, `banner`.

   Default: `img`. If an invalid value is specified, the default will be used."
   "file","binary","The image file to upload. Max size: 500 KiB."
   "name","string","A name for the image for a stylesheet image upload.

   Ignored unless `upload_type: img`. If `upload_type: img` then parameter must be specified otherwise
   a `BAD_CSS_NAME` API error occurs."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_CSS_NAME","200","* The `name` parameter was not specified.

   * The value provided for `name` is invalid.","
   ``{""errors"": [""BAD_CSS_NAME""], ""img_src"": """", ""errors_values"": [""bad image name""]}``
   "
   "IMAGE_ERROR","200","The value provided for `name` is invalid.","
   ``{""errors"": [""IMAGE_ERROR""], ""img_src"": """", ""errors_values"": [""Invalid image or general image error""]}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to upload an image to the specified subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_upload_sr_img


Delete stylesheet image
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/delete_sr_img

*scope: modconfig*

Delete an image from the subreddit's stylesheet custom image set.

The image will no longer count against the subreddit's image limit, however the actual image data may still be accessible
for an unspecified amount of time. If the image is currently referenced by the subreddit's stylesheet, that stylesheet
will no longer validate and won't be submittable until the image reference is removed.

If the specified image does not exist, it is treated as a success.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."
   "img_name","string","A stylesheet image name."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to delete an image from the specified subreddit."
   "500","The `img_name` parameter was not specified."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_delete_sr_img


Set icon
~~~~~~~~

See :ref:`upload-stylesheet-image`. Use `upload_type: header`.


.. _legacy-reddit-subreddit-style-unset-icon:

Unset icon
~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/delete_sr_header

*scope: modconfig*

Remove the subreddit's icon.

The site-wide default icon image will be shown again after this call.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL.
   If both are specified, the one in the URL takes preference."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to delete an image from the specified subreddit."


Set mobile icon
~~~~~~~~~~~~~~~

See :ref:`upload-stylesheet-image`. Use `upload_type: icon`.


Unset mobile icon
~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/delete_sr_icon

Same deal as in :ref:`legacy-reddit-subreddit-style-unset-icon`.


Set mobile banner
~~~~~~~~~~~~~~~~~

See :ref:`upload-stylesheet-image`. Use `upload_type: banner`.


Unset mobile banner
~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/delete_sr_banner

Same deal as in :ref:`legacy-reddit-subreddit-style-unset-icon`.
