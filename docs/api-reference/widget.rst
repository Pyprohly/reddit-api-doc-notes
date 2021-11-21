
Subreddit Widget
================

Schemas
-------

Text area widget
~~~~~~~~~~~~~~~~

*Creating*:

* `id` (>> string): The widget ID.
* `kind` (string): `textarea`.
* `styles` (?object):
  Sub-field values can be empty strings. If `null` is specified as a value for the sub keys
  it is treated as an empty string. The sub-field values are `null` during object retrieval
  when `styles` was not specified during creation.

  * `headerColor` (string?):  A color hex string. E.g., `#AA22cc`.
  * `backgroundColor` (string?): A color hex string. E.g., `#AA22cc`.

* `shortName` (string): A title for this widget. Specify a string no longer than 30 characters.
* `text` (string): Markdown text.
* `textHtml` (>> string): An HTML string of the `text` field.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.


Button widget
~~~~~~~~~~~~~

*Creating*:

* `id` (>> string): The widget ID.
* `kind` (string): `button`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `description` (string): A description for this widget.
* `descriptionHtml` (>> string): An HTML string of the `description` field.
* `buttons` (object array): A list of button objects.
  Must contain at least one object otherwise a `TOO_SHORT` API error occurs.

  - If `kind: text`:

    * `kind` (string): `text`.
    * `text` (string): Max 30 characters.
    * `url` (string): The link URL.
    * `textColor` (?string? >> ?string): Text color. Specify a color hex.
      Empty string is allowed and registers as an empty string in the output. A `null` is treated as an empty string.
      In the UI, if not specified, or a empty string or null, the `color` field will be used as the default value,
      but this is not reflected in the widget data.
    * `fillColor` (?string? >> ?string): Fill color. Specify a color hex.
      Empty string is allowed and registers as an empty string in the output. A `null` is treated as an empty string.
    * `color` (string? >> string): Stroke color. Specify a color hex.
      Empty string is allowed and registers as an empty string in the output. A `null` is treated as an empty string.
    * `hoverState` (?object): Hover state button style properties.

      - If `kind: text`: All properties behave same as outer.

        * `kind` (string): `text`.
        * `text` (string)
        * `textColor` (string)
        * `fillColor` (string)
        * `color` (string)

      - If `kind: image`: All properties behave same as outer.

        * `kind` (string): `image`.
        * `url` (string): The image URL. It is documented as `imageUrl` but this is incorrect.
        * `width` (integer)
        * `height` (integer)

  - If `kind: image`:

    * `kind` (string): `image`.
    * `text` (string): Max 30 characters.
    * `linkUrl` (string): The link URL.
    * `url` (string): The image URL. It is documented as `imageUrl` but it's actually `url`.
    * `width` (integer): Specify the image width.
    * `height` (integer): Specify the image height.
    * `hoverState` (?object): Like in `kind: text` above.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.


Image widget
~~~~~~~~~~~~

*Creating*:

* `id` (>> string): The widget ID.
* `kind` (string): `image`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `data` (object array): A list of image information.

  * `url` (string): A URL of a Reddit-hosted image.
  * `width` (integer): Specify the image width.
  * `height` (integer): Specify the image height.
  * `linkUrl` (string?): An optional link URL. This field is actually mandatory but you can specify
    either an empty string or `null` for no link. (The UI sends an empty string if not specified.)

* `websocketUrl` (>> string): This field only appears on widget creation.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.
* The `websocketUrl` field will not be present.


Community list widget
~~~~~~~~~~~~~~~~~~~~~

*Creating*:

The `data` field will be an array of objects in the output.

* `id` (>> string): The widget ID.
* `kind` (string): `community-list`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `data` (string array >> object array): Input a list of subreddit names.
  The output will be a object array containing partial subreddit objects.

  Sub-object fields:

  * name (string): The name of the subreddit. Same as the `display_name` field on the :ref:`Subreddit schema <subreddit-schema>`.
  * type (string): Always `subreddit`?
  * subscribers (integer): Same as the `subscribers` field on the :ref:`Subreddit schema <subreddit-schema>`.
  * iconUrl (string): Same as the `icon_img` field on the :ref:`Subreddit schema <subreddit-schema>`.
  * communityIcon (string): Same as the `community_icon` field on the :ref:`Subreddit schema <subreddit-schema>`.
  * primaryColor (string): Same as the `primary_color` field on the :ref:`Subreddit schema <subreddit-schema>`.
  * isNSFW (boolean): Same as the `over18` field on the :ref:`Subreddit schema <subreddit-schema>`.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.


Calendar widget
~~~~~~~~~~~~~~~

*Creating*:

An array, `data`, will exist in the output.

* `id` (>> string): The widget ID.
* `kind` (string): `calendar`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `googleCalendarId` (string): A Google email address.
* `requiresSync` (boolean)
* `configuration` (object):

  * `numEvents` (integer): A number from 1 to 50. Default: 10.
  * `showTitle` (boolean)
  * `showDescription` (boolean)
  * `showLocation` (boolean)
  * `showDate` (boolean)
  * `showTime` (boolean)

* `data` (>> unknown array)

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.


Post flair widget
~~~~~~~~~~~~~~~~~

*Creating*:

The output will have a `templates` key which is a mapping of flair template UUIDs to post flair choices.

* `id` (>> string): The widget ID.
* `kind` (string): `post-flair`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `display` (string): Either `cloud` or `list`.
* `order` (string array): A list of flair template UUIDs.
* `templates` (>> object): A mapping of flair template UUIDs to post flair choices.

   * `templateId` (string): Flair template UUID.
   * `type` (string): Always `richtext`?
   * `text` (string): The flair text.
   * `backgroundColor` (string): A hex color value.
   * `textColor` (string): Either `dark` or `light`.
   * `richtext` (object): A richtext object.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.


Custom CSS widget
~~~~~~~~~~~~~~~~~

*Creating*:

* `id` (>> string): The widget ID.
* `kind` (string): `custom`.
* `styles` (?object): See text area widget.
* `shortName` (string): Max 30 characters.
* `text` (string): Max 10000 characters.
* `css` (string): Max 100000 characters.
* `height` (integer?): A number from 50 to 500. Numbers outside this range will be clamped.
  Can be `null`. An empty string is treated as a `null`.
* `imageData` (object array): Specify an empty array if no image data.

  * `url` (string): A URL of a Reddit-hosted image.
  * `width` (integer?): The image width.
    Can be `null`. An empty string is treated as a `null`.
  * `height` (integer?): The image height.
    Can be `null`. An empty string is treated as a `null`.
  * `name` (integer): A name so you can reference it in the CSS.
    Names should be unique consisting of alphanumeric and '-' characters only.
    Must be no longer than 20 characters,

* `websocketUrl` (>> string): This field only appears on widget creation.

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will always be present.
* The `websocketUrl` field will not be present.


Community details widget
~~~~~~~~~~~~~~~~~~~~~~~~

*Creating*:

This special widget type cannot be created.

*Updating*:

The endpoint requires the `shortName` field but it isn't actually used anywhere on the site.
The title of the widget will always be `About Community`. The UI doesn't give you an option to
change this field but the value that this field starts with in each subreddit is `Community Details`
and the UI uses the current value each time when updating the widget.

* `id` (>> string): The widget ID.
* `kind` (string): `id-card`.
* `styles` (?object): See text area widget.
* `shortName` (string): A title for this widget. The website uses `Subreddit Rules`.
* `subscribersText` (string): A string no longer than 30 characters. A `null` value is treated as an empty string.
* `currentlyViewingText` (string): A string no longer than 30 characters. A `null` value is treated as an empty string.

*Retrieving*:

* All fields in *Updating* output.
* The `styles` field will always be present.
* `description` (string): The public description of the subreddit.
  Same as the `public_description` field of the :ref:`Subreddit schema <subreddit-schema>`.
* `subscribersCount` (integer): The number of subscribers of the subreddit.
  Same as the `subscribers` field of the :ref:`Subreddit schema <subreddit-schema>`
* `currentlyViewingCount` (integer): The number of subscribers of the subreddit.
  Same as the `active_user_count` field of the :ref:`Subreddit schema <subreddit-schema>`.


Moderator list widget
~~~~~~~~~~~~~~~~~~~~~

*Creating*:

This special widget type cannot be created.

*Updating*:

* `id` (>> string): The widget ID.
* `kind` (string): `moderators`.
* `styles` (?object): See text area widget.

Notice this is the only widget that doesn't have `shortName`.

*Retrieving*:

* All fields in *Updating* output.
* The `styles` field will always be present.
* `totalMods` (integer): The number of subreddit moderators.
* `mods` (object array): A list of moderators and their flair information.
  List is empty if logged out or current user is banned from the subreddit.

  * name (string): The user name of the moderator.
  * authorFlairType (string): Always `text`?.
  * authorFlairText (string?): The flair text. Empty string if flair not set. Is `null`
    if the user has never had a flair before in the subreddit.
  * authorFlairTextColor (string): Either `dark` or `light`.
  * authorFlairBackgroundColor (string)': E.g., `#ffd635`. Empty string if not set.
  * authorFlairRichText (object array): Rich text object.


Rules widget
~~~~~~~~~~~~

*Creating*:

This special widget type cannot be created.

*Updating*:

The endpoint requires the `shortName` field but it isn't actually used when displaying the widget.
The website will send `Subreddit Rules` here regardless but `r/{subreddit} Rules` is displayed as the widget title.

* `id` (>> string): The widget ID.
* `kind` (string): `subreddit-rules`.
* `styles` (?object): See text area widget.
* `shortName` (string): A title for this widget. The website uses `Subreddit Rules`.
* `display` (string): Either `full` or `compact`.

*Retrieving*:

* All fields in *Updating* output.
* The `styles` field will always be present.
* `data` (object array): A list of rules.

  Note: unlike the `GET /r/{subreddit}/about/rules` :ref:`Subreddit Rule Object <subreddit-get-rules>`,
  this sub-object is missing the `kind` field. The `violationReason` field also behaves slightly differently.

  * priority (integer): Same as the `priority` field on the
    `GET /r/{subreddit}/about/rules` :ref:`Subreddit Rule Object <subreddit-get-rules>`.
  * description (string): Same as the `description` field on the Subreddit Rule Object.
  * descriptionHtml (string): Same as the `description_html` field on the Subreddit Rule Object.
  * shortName (string): Same as the `short_name` field on the Subreddit Rule Object.
  * violationReason (string?): Similar to the `violation_reason` field on the Subreddit Rule Object,
    but if the violation reason is not set then this value is `null`.
  * createdUtc (float): Same as the `created_utc` field on the Subreddit Rule Object.


Overview
--------

Reddit Help Info: https://mods.reddithelp.com/hc/en-us/articles/360010364372-Sidebar-Widgets.

Actions
-------

Upload image
~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/widget_image_upload_s3

*scope: structuredstyles*

Upload an image for use in a widget.

This endpoint is used for obtaining an upload lease.

The upload process is similar to Flair Emoji image uploads. See :ref:`here <emoji-upload>`.

The `action` is typically `//reddit-subreddit-uploaded-media.s3-accelerate.amazonaws.com` for this endpoint.


.. _widget-create:

Create
~~~~~~

.. http:post:: /r/{subreddit}/api/widget

*scope: structuredstyles*

Add a widget to a subreddit.

This endpoint takes JSON data. The structure of the JSON payload depends on the kind of widget being created.

Typically the output JSON has the same shape as the input, with an additional `id` field on the root.
For example, the `styles` field will not exist in the output if it wasn't in the input,
however it will always be present when retrieving the widget through `GET /r/{subreddit}/api/widgets`.


Update
~~~~~~

.. http:put:: /r/{subreddit}/api/widget/{widget_id}

*scope: structuredstyles*

Update a widget.

Updating a widget is the same process as creating but use `PUT` instead of `POST` and specify the widget ID
in the URL. In general, you must specify all the widget's fields even if you want to update only some of them.

Some widgets can only be updated and not created such as the community details and moderator list widgets.


.. _widget-create-menu-bar-tabs:

Create menu bar tabs
~~~~~~~~~~~~~~~~~~~~

Use the `POST /r/{subreddit}/api/widget` endpoint. See :ref:`Create widget <widget-create>`.

Menu bar schema:

*Creating*:

The `styles` field will be ignored.

* `id` (>> string): The widget ID.
* `kind` (string): `menu`.
* `showWiki` (?boolean >> boolean): Default: false. Non-boolean values are converted to a boolean.
* `data` (?object-array):
  It's possible to not send this field but doing so will cause the redesign Reddit UI to not load
  until the widget is deleted or is updated to have `data`.

  - If link tab:

    * `text` (string): Max 20 characters.
    * `url` (string): A link URL.

  - If submenu tab:

    * `text` (string): Max 20 characters.
    * `children` (object array):

      * `text` (string)
      * `url` (string)

*Updating*:

Same as *Creating*.

*Retrieving*:

* All fields in *Creating* output.
* The `styles` field will be present, even though its values cannot be set in any way.


Update menu bar tabs
~~~~~~~~~~~~~~~~~~~~

Use the `PUT /r/{subreddit}/api/widget/{widget_id}` endpoint.

See :ref:`Create menu bar tabs <widget-create-menu-bar-tabs>` for the input schema.


Retrieve
~~~~~~~~

.. http:get:: /r/{subreddit}/api/widgets

*scope: structuredstyles*

Retrieve all widgets in a subreddit.

If the target subreddit does not exist, an empty listing structure is returned::

   {"kind": "Listing", "data": {"after": null, "dist": 0, "modhash": null, "geo_filter": ", "children": [], "before": null}}

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "progressive_images","boolean","If true (default), image links in `type: image` widgets contain a `?format=pjpg` URL query string.

   E.g., true:

   `https://styles.redditmedia.com/t5_g495e/styles/image_widget_644tga5ke7w71.jpg?format=pjpg&s=3ccd8901192f99e5bf8c1a426066fefea3ee944f`

   E.g., false:

   `https://styles.redditmedia.com/t5_g495e/styles/image_widget_644tga5ke7w71.jpg`

   Default: true."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to view the widgets of the target subreddit."


Delete
~~~~~~

.. http:delete:: /r/{subreddit}/api/widget/{widget_id}

*scope: structuredstyles*

Delete a widget.

Returns zero bytes on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "WIDGET_NOEXIST","400","The widget specified by the ID does not exist.","
   ``{""fields"": [""widget_id""], ""explanation"": ""That widget doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""WIDGET_NOEXIST""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* You are not a moderator of the target subreddit.

   * There is no user context."


Reorder
~~~~~~~

.. http:patch:: /r/{subreddit}/api/widget_order/sidebar

*scope: structuredstyles*

Reorder the widgets in the sidebar.

Specify a JSON array of widget IDs. The array must contain all existing widget IDs (except for the community details
and moderator list widgets) and no ID must be duplicated otherwise an `INVALID_ARGUMENT` API error is returned.

Returns zero bytes on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "INVALID_ARGUMENT","400","The array does not contain all the expected widget IDs.","
   ``{""explanation"": ""Invalid value for order"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ARGUMENT""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* You are not a moderator of the target subreddit.

   * There is no user context."
