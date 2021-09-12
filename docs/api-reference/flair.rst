
Flair
=====

Actions
-------

Assign user flair
~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/flair

*scope: modflair*

Assign a flair to a user or submission.

Use either the `name` parameter to assign a flair to a user, or `link` to set a submission's flair.
If both are specified, `link` will take preference and `name` will be ignored.

Both `text` and `css_class` should be specified. Each defaults to an empty string if not specified.
If both values are empty strings or if neither parameters are specified then the user's flair is revoked.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","Some redditor username."
   "link","string","A full ID36 of a submission in the subreddit."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used."
   "css_class","string","A CSS class. No longer than 100 characters."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "BAD_FLAIR_TARGET","* The `name` or `link` parameter was not specified.

   * The username specified by `name` does not exist.

   * The submission specified by `link` does not exist.

   *\"not a valid flair target\"* -> name"
   "BAD_CSS_NAME","The CSS class specified by `css_class` was longer than 100 characters.

   The CSS class specified by `css_class` contained invalid characters.

   *\"invalid css name\"* -> css_class"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The current user does not have permission to set flairs in the specified subreddit.

   * The submission targeted by `link` does not belong to the current subreddit."
   "404","(Sends HTML document.) The subreddit specified in the URL does not exist."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flair


Assign post flair
~~~~~~~~~~~~~~~~~

See `Assign user flair`_.

Use the `link` parameter.


Revoke user flair
~~~~~~~~~~~~~~~~~

See `Assign user flair`_.

Use the `name` parameter and don't specify the `text` or `css_class` parameters.

|

Alternatively:

.. http:post:: /r/{subreddit}/api/deleteflair

*scope: modflair*

Revoke a flair from a user.

Nothing happens if the specified user does not have a flair.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","Some redditor username."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","The name specified by `name` contained invalid characters.
   Note, the `POST /r/{subreddit}/api/flair` endpoint would return a BAD_FLAIR_TARGET API error instead
   so consider this when deciding to use this endpoint or that one."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_deleteflair


Revoke post flair
~~~~~~~~~~~~~~~~~

See `Assign user flair`_.

Use the `link` parameter and don't specify the `text` or `css_class` parameters.


Bulk update (assign/revoke) user flairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/flaircsv

*scope: modflair*

Set the flair on multiple users in a subreddit at once.

The parameter `flair_csv` expects a CSV string which has up to 100 lines of the form `user,flairtext,cssclass`.
Lines beyond the 100th are ignored.

CSV newlines can be `\r\n` or `\n`. (The `\r` in `\r\n` won't be counted towards any limit.)

If both the `flairtext` and `cssclass` values are the empty string, the user's flair is cleared.
Returns an array of objects indicating if each flair setting was applied, or a reason for the failure.

Example return value::

   [{"status": "added flair for user aaaa",
     "errors": {},
     "ok": true,
     "warnings": {}},
    {"status": "added flair for user bbbb",
     "errors": {},
     "ok": true,
     "warnings": {}},
    {"status": "skipped",
     "errors": {"user": "unable to resolve user `zjsargoquifanz', ignoring"},
     "ok": false,
     "warnings": {},
    {"status": "skipped",
     "errors": {"row": "improperly formatted row, ignoring"},
     "ok": false,
     "warnings": {}}]

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_csv","A CSV string of flair information in the form of `user,flairtext,cssclass`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have permission to set flairs in the specified subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flaircsv


Create user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/flairtemplate_v2

*scope: modflair*

Create or update a flair template.

If an invalid value is specified for any parameter, its default will be used.

Returns the newly created or updated flair template object. E.g.,::

   {"text": "",
    "allowableContent": "all",
    "modOnly": false,
    "cssClass": "",
    "id": "c47e779e-266b-11eb-a76e-0e92b471a041",
    "textEditable": false,
    "overrideCss": false,
    "richtext": [],
    "maxEmojis": 10,
    "flairType": "USER_FLAIR",
    "backgroundColor": "#d3d6da",
    "textColor": "dark",
    "type": "text"}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_template_id","string","Edit the flair with this ID. If the specified ID does not exist then it will be
   ignored and a new flair template will be created."
   "flair_type","string","Either `USER_FLAIR`, or `LINK_FLAIR`.

   With the `flair_template_id` parameter, a flair's type can be changed.

   Default: `USER_FLAIR`."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   Default: `\"\"`."
   "text_editable","boolean","Whether users will be able to edit flair text.

   Default: `false`."
   "css_class","string","A CSS class. No longer than 100 characters.

   Default: `\"\"`."
   "text_color","string","Either `light` or `dark`.

   Default: `dark`."
   "allowable_content","string","One of `all`, `emoji`, `text`.

   Default: `all`."
   "background_color","string","A 6-digit rgb hex color, e.g. `#aabbcc`, with an optional hash at the start.

   If the string is invalid, an empty string is used (background color disabled).

   Default: `#d3d6da`."
   "max_emojis","integer","An integer between 1 and 10.

   Default: 10."
   "mod_only","boolean","Whether flair is only available for mods to select.

   Default: `false`."
   "override_css?","boolean","Purpose unknown. Always false, even when passing `override_css: 1` when creating a user flair template.

   Post flair templates do not have this attribute."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have permission to set flairs in the specified subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flairtemplate_v2


|
|

.. http:post:: /r/{subreddit}/api/flairtemplate

*scope: modflair*

Deprecated.

Create or update a flair template.

If an invalid value is specified for any parameter, its default will be used.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_template_id","string","Edit the flair with this ID.

   If the specified ID does not exist then this parameter will be ignored and a new flair template will be created."
   "flair_type","string","Either `USER_FLAIR`, or `LINK_FLAIR`.

   With the `flair_template_id` parameter, a flair's type can be changed.

   Default: `USER_FLAIR`."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   Default: `\"\"`."
   "text_editable","boolean","Whether users will be able to edit flair text.

   Default: `false`."
   "css_class","string","A CSS class. No longer than 100 characters.

   Default: `\"\"`."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "BAD_CSS_NAME","The CSS class specified by `css_class` was longer than 100 characters.

   The CSS class specified by `css_class` contained invalid characters.

   *\"invalid css name\"* -> css_class"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flairtemplate


Create post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Create user flair template`_.

Specify `LINK_FLAIR` for the `flair_type` parameter.


Update user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Create user flair template`_.

Specify the `flair_template_id`.


Update post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Update user flair template`_.


Assign user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/selectflair

*scope: flair*

Assign a flair template to a user/post.

This endpoint can be used like `POST /r/{subreddit}/api/flair` when `flair_template_id` is not specified.
If `flair_template_id` is not specified then `background_color` and `text_color` are ignored.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_template_id","string","A flair ID."
   "name","string","Some redditor username."
   "link","string","A full ID36 of a submission in the subreddit."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   If the flair is not editable then this has no effect
   (unless the current user is a moderator with the subreddit flair permission)."
   "css_class","string","This parameter seems to have no effect?"
   "background_color","string","A rgb hex color, e.g. `#aabbcc`, with an optional hash at the start."
   "text_color","string","Either `light` or `dark`."
   "return_rtson","string","?"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The specified flair ID does not exist.

   * The specified flair ID is a post flair when `name` is used, or a user flair when `link` is used.

   * The current user does not have permission to assign the specified flair ID."
   "404","* Neither the `name` nor `link` parameters were specified.

   * The `name` specified was not found or contains invalid characters."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_selectflair


Assign post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Assign user flair template`_.

Specify the `link` parameter.


Revoke user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Assign user flair template`_.

Specify only the `name` parameter.


Revoke post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Assign user flair template`_.

Specify only the `link` parameter.


Delete user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/deleteflairtemplate

*scope: modflair*

Delete a flair template.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_template_id","string","A flair ID."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have flair mod permission in the subreddit."
   "404","The `flair_template_id` specified does not exist."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_deleteflairtemplate


Delete post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Delete user flair template`_.


Delete all user flair templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/clearflairtemplates

*scope: modflair*

Delete all flair templates.

Specify `USER_FLAIR` for `flair_type` to delete all user flair templates.
Specify `LINK_FLAIR` to delete all post flair templates.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_type","string","Either `USER_FLAIR` or `LINK_FLAIR`. Defaults `USER_FLAIR` if not specified or some other value is used."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have flair mod permission in the subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_clearflairtemplates


Delete all post flair templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Delete all user flair templates`_.

Specify `LINK_FLAIR` for the `flair_type` parameter.


Configure subreddit flair settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/flairconfig

*scope: modflair*

Configure subreddit flair settings.

All parameters must specified. If a parameter is not specified or is an invalid value its default will be used.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_enabled","boolean","Whether user flairs are enabled in the subreddit.

   This controls the `user_flair_enabled_in_sr` field on subreddit objects.

   Default: `false`."
   "flair_position","string","Either `left`, `right`, or empty string.

   This controls the `user_flair_position` field on subreddit objects.

   Default: `\"\"`."
   "flair_self_assign_enabled","boolean","Forced false if `flair_enabled` is false.

   This controls the `can_assign_user_flair` field on subreddit objects.

   Default: `false`."
   "link_flair_position","string","Either `left`, `right`, or empty string.

   This controls the `link_flair_position` field on subreddit objects.

   Default: `\"\"`."
   "link_flair_self_assign_enabled","boolean","Forced false if `link_flair_position` is empty string.

   This controls the `can_assign_link_flair` field on subreddit objects.

   Default: `false`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have flair mod permission in the subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flairconfig


Reorder user flair templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:patch:: /api/flair_template_order
.. http:patch:: /api/v1/{subreddit}/flair_template_order/{flair_type}

*scope: modflair*

Reorder flair templates.

Flair template IDs should be given as a JSON array in the request body.

The array must contain every flair ID. If you fail to supply an ID a 400 HTTP error is returned.

If you duplicate an ID the flair will have multiple references in the UI.

If using the `/api/v1/{subreddit}/flair_template_order/{flair_type}` form, the `{flair_type}`
must be specified, otherwise a 404 is returned.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "subreddit","string","The target subreddit."
   "flair_type","string","Either `USER_FLAIR` or `LINK_FLAIR`.

   If not specified, defaults to `USER_FLAIR`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* A flair template ID is missing from the provided list.

   * No JSON array was provided in the request body."
   "500","* The subreddit specified by the `subreddit` parameter or the `{subreddit}` URL placeholder does not exist.

   * The `subreddit` parameter was not specified."

.. seealso:: https://www.reddit.com/dev/api/#PATCH_api_flair_template_order


Reorder post flair templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Reorder user flair templates`_. Use `flair_type=LINK_FLAIR`.


Get user flair templates
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/api/user_flair_v2

*scope: flair*

Return a list of available user flair templates in a subreddit.

Current user must be a mod of the subreddit.

E.g.,::

   [{"allowable_content": "all",
     "text": "asdf",
     "text_color": "dark",
     "mod_only": false,
     "background_color": "transparent",
     "id": "e4ef846a-272d-11eb-b7f1-0e21dbc9573f",
     "css_class": "",
     "max_emojis": 10,
     "richtext": [],
     "text_editable": false,
     "override_css": false,
     "type": "text"},
   ...]

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","You must login to use this endpoint."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The current user is not a moderator of the subreddit.

   * The current user cannot access the subreddit, e.g., because it is a private subreddit."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_user_flair_v2


|
|

.. http:get:: /r/{subreddit}/api/user_flair

*scope: flair*

Deprecated.

Return a list of available user flairs in a subreddit.

Current user must be a mod of the subreddit.

E.g.,::

   [{"text": "asdf",
     "richtext": [],
     "text_editable": False,
     "override_css": False,
     "css_class": "",
     "type": "text",
     "id": "22e43042-fc6d-11e8-862d-0e2e63c9b776"},
   ...]

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","You must login to use this endpoint."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The current user is not a moderator of the subreddit.

   * The current user cannot access the subreddit, e.g., because it is a private subreddit."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_user_flair


Get post flairs templates
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/api/link_flair_v2

See `Get user flair templates`_ for details.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_link_flair_v2


|
|

.. http:get:: /r/{subreddit}/api/link_flair

See `Get user flair templates`_ for details.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_link_flair


Get user flair choices
~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/flairselector

*scope: flair*

Return a user or post's flair options.

An object of two fields, `current` and `choices`, is returned. `current` contains an object representing the
flair configuration of the current user.

In the `current` object:
* The `flair_template_id` field may incorrectly be `null` until the flair is updated.
* The `flair_css_class` field may be `null` if a flair is assigned and the template
doesn't have a CSS class set.
* If `flair_template_id` is `null` then no flair template is assigned.
* If `flair_css_class`, `flair_text`, and `flair_position` are empty strings, and `flair_template_id` is `null` then
no flair is assigned. Just checking `flair_text` is an empty string is adequate since the flair text can't be empty.
* There is no `flair_text_editable` field.

Example output::

   {"current": {"flair_css_class": "",
                "flair_template_id": null,
                "flair_text": "",
                "flair_position": ""},
    "choices": [{"flair_css_class": "",
                 "flair_template_id": "e4ef846a-272d-11eb-b7f1-0e21dbc9573f",
                 "flair_text_editable": false,
                 "flair_position": "",
                 "flair_text": "asdf"},
                 ...]}

If user/post flairs are disabled or the current user is a moderators that doesn't have the flair permission
then the following object is returned::

   {"current": {"flair_css_class": "",
                "flair_template_id": null,
                "flair_text": "",
                "flair_position": ""},
    "choices": []}

If there is no user context, this endpoint returns `"{}"` (i.e., a string of an empty JSON object).

.. csv-table:: Form Data (or URL Params)
   :header: "Field","Type (hint)","Description"
   :escape: \

   "is_newlink","boolean","Whether to return information on post flairs or user flairs.
   If truthy then return information for post flairs. If not specified then defaults to false.

   If the `link` parameter is specified and its ID is valid then this parameter is ignored."
   "link","string","A submission full ID36. If specified and the ID exists then objects will
   be on post flairs instead of user flairs.

   If the given ID doesn't exist then this parameter is ignored. Thus, it is a good idea to pass
   `is_newlink=1` to ensure that information returned is on post flairs."
   "name","string","A redditor username. If not specified, defaults to the current user if available."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The submission specified by the full ID36 `link` does not belong to this subreddit."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flairselector


Get post flair choices
~~~~~~~~~~~~~~~~~~~~~~

See `Get user flair choices`_.

Specify a truthy value for the `is_newlink` parameter.


Get user flair association
~~~~~~~~~~~~~~~~~~~~~~~~~~

Determine the flair text for a user in a subreddit.

See `Get user flair associations`_.

Use the `name` parameter (with `limit=1`).


Get user flair associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/api/flairlist

*scope: modflair*

Return user flair associations for a subreddit.

This endpoint will return an object with a `users` field that is an array of
flair association items that look like::

   {"flair_css_class": null, "user": "Pyprohly", "flair_text": "fghj"}

All fields are strings, but the `flair_css_class` field can be `null`. For information on when the
`flair_css_class` field is `null`, see the `user_flair_css_class` field on the Subreddit schema.

If there are more items in the listing then the root object will contain a `next` field
that should be used as the `after` parameter value to retrieve the next page of results.
Subsequent pages will have a `prev` field that can be used for the `before` parameter
to go backwards in the listing.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "before","...","See :ref:`Listings overview <listings_overview>`."
   "after","...","See :ref:`Listings overview <listings_overview>`."
   "limit","integer","See :ref:`Listings overview <listings_overview>`.

   The max is 1000."
   "name","string","A username. If the given name doesn't have a flair association then the parameter is ignored
   (i.e., as if it weren't specified).

   If using this parameter it is recommended to specify `limit=1` so that if the name is not found
   then only 1 item is returned instead of (up to) 25."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_flairlist


Show my flair
~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/api/setflairenabled

*scope: flair*

Set the "Show my flair on this subreddit" option for the current user.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "flair_enabled","boolean","Truthy (any string matching `/^[^0Ff]/`) to enable, falsy to disable.

   If not specified then defaults to false."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","You must login to use this endpoint."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","(Sends HTML document.) The subreddit specified in the URL does not exist."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_setflairenabled

