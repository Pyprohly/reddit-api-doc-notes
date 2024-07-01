
Flair
=====

Actions
-------

Assign user flair
~~~~~~~~~~~~~~~~~

The `POST /r/{subreddit}/api/selectflair` endpoint (See `Assign user flair template`_)
can do everything the `POST /r/{subreddit}/api/flair` endpoint can and more. Use that instead.

|

.. http:post:: /r/{subreddit}/api/flair

*scope: modflair*

Assign a flair to a user or submission.

Use either the `name` parameter to assign a flair to a user, or `link` to set a submission's flair.
If both are specified, `link` will take preference and `name` will be ignored.

Both `text` and `css_class` should be specified. Each defaults to an empty string if not specified.

If the target is using a flair template, it will be removed.

You can remove a user flair by not providing a value for `text` and `css_class` parameters.
This also works to remove template flairs.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "name","string","Some redditor username."
   "link","string","A full ID36 of a submission in the subreddit."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used."
   "css_class","string","A CSS class. No longer than 100 characters."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_FLAIR_TARGET","200","* Neither the `name` nor `link` parameters were specified.
   * The user specified by `name` does not exist.
   * The submission specified by `link` does not exist.","
   ``{""json"": {""errors"": [[""BAD_FLAIR_TARGET"", ""not a valid flair target"", ""name""]]}}``
   "
   "BAD_CSS_NAME","200","- The CSS class specified by `css_class` was longer than 100 characters.
   - The CSS class specified by `css_class` contained invalid characters.","
   ``{""json"": {""errors"": [[""BAD_CSS_NAME"", ""invalid css name"", ""css_class""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","* There is no user context.

   * The current user does not have permission to set flairs in the specified subreddit.

   * The submission targeted by `link` does not belong to the specified subreddit.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The subreddit specified in the URL does not exist.","*(HTML document)*"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flair


Assign post flair
~~~~~~~~~~~~~~~~~

See `Assign user flair`_.

Use the `link` parameter.


Revoke user flair
~~~~~~~~~~~~~~~~~

To revoke a user flair, you can use the `POST /r/{subreddit}/api/flair` endpoint
(`Assign user flair`_) and not specify the `text` or `css_class` parameters.

This is recommended even though the UI does not do this.
However, it does effectively do this for post flairs.

|

Alternatively, here is an alternative endpoint that does a similar thing.
This is what the UI uses to unset a user's flair.

.. http:post:: /r/{subreddit}/api/deleteflair

*scope: modflair*

Revoke a flair from a user.

Nothing happens if the specified user does not have a flair.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "name","string","Some redditor username."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","There is no user context.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "500","The username specified by `name` contained invalid characters.

   Note, the `POST /r/{subreddit}/api/flair` endpoint would return a
   `BAD_FLAIR_TARGET` API error instead so consider this when deciding
   to use this endpoint or that one. Perhaps this one is more broken.
   ","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

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

   "flair_csv","A CSV string of flair information in the form of `user,flairtext,cssclass`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","* There is no user context.

   * The current user does not have permission to set flairs in the specified subreddit.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The specified subreddit does not exist."

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

   "flair_type","string","Either `USER_FLAIR`, or `LINK_FLAIR`.

   With the `flair_template_id` parameter, a flair's type can be changed.

   Default: `USER_FLAIR`."
   "flair_template_id","string","Edit the flair with this ID. If the specified ID does not exist then it will be
   ignored and a new flair template will be created."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   Interestingly, it's possible to create a flair template with empty text
   using this endpoint, but not through the UI.

   Default: empty string."
   "css_class","string","A CSS class. No longer than 100 characters.

   Default: empty string."
   "background_color","string","
   A 6-digit rgb hex color. E.g. `#fb8559`.

   For user flair templates, the background color can be unset and the
   value will be the string `""transparent""`. Post flairs cannot be transparent.

   For user flairs, the default value is `""transparent""`.
   For post flairs, the default value will be `#d3d6da`,
   but on the UI the default is `#DADADA`.
   "
   "text_color","string","Either `light` or `dark`.

   Default: `dark`."
   "mod_only","boolean","Whether flair is only available for mods to select.

   Default: `false`."
   "text_editable","boolean","Whether users will be able to edit their flair text.

   Default: `false`."
   "allowable_content","string","One of `all`, `emoji`, `text`.

   Default: `all`."
   "max_emojis","integer","An integer from 1 to 10.

   Default: 10."
   "override_css?","boolean","Purpose unknown. Always false, even when passing `override_css: 1` when creating a user flair template.

   Post flair templates do not have this attribute."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","* There is no user context.

   * The current user does not have permission to set flairs in the specified subreddit.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The specified subreddit does not exist."

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

   "flair_template_id","string","Edit the flair with this ID.

   If the specified ID does not exist then this parameter will be ignored and a new flair template will be created."
   "flair_type","string","Either `USER_FLAIR`, or `LINK_FLAIR`.

   With the `flair_template_id` parameter, a flair's type can be changed.

   Default: `USER_FLAIR`."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   Default: empty string."
   "css_class","string","A CSS class. No longer than 100 characters.

   Default: empty string."
   "text_editable","boolean","Whether users will be able to edit the flair text.

   Default: `false`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_CSS_NAME","200","The CSS class specified by `css_class` was longer than 100 characters.

   The CSS class specified by `css_class` contained invalid characters.","
   ``{""json"": {""errors"": [[""BAD_CSS_NAME"", ""invalid css name"", ""css_class""]]}}``
   "

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

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "name","string","Some redditor username."
   "link","string","A full ID36 of a submission in the subreddit."
   "flair_template_id","string","A flair ID."
   "text","string","Flair text. No longer than 64 characters. If longer than 64 characters then the
   parameter is ignored and an empty string is used.

   If the flair is not editable then this has no effect
   (unless the current user is a moderator with the subreddit flair permission)."
   "css_class","string","This parameter seems to have no effect?"
   "background_color","string","A rgb hex color, e.g. `#aabbcc`."
   "text_color","string","Either `light` or `dark`."
   "return_rtson","string","?"

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_CSS_NAME","200","- The CSS class specified by `css_class` was longer than 100 characters.
   - The CSS class specified by `css_class` contained invalid characters.","
   ``{""json"": {""errors"": [[""BAD_CSS_NAME"", ""invalid css name"", ""css_class""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","* The specified flair ID does not exist.
   * The specified flair ID is a post flair when `name` is used, or a user flair when `link` is used.
   * You do not have permission to assign the specified flair ID.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","* Neither the `name` nor `link` parameters were specified.
   * The specified subreddit does not exist.
   * The specified user by `name` does not exist.
   * The specified submission by `link` does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_selectflair


Assign post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST /r/{subreddit}/api/selectflair` (See `Assign user flair template`_).
Specify the `link` parameter.


Revoke user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST /r/{subreddit}/api/selectflair` (See `Assign user flair template`_).
Specify only the `name` parameter.
This is what the UI does.


Revoke post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST /r/{subreddit}/api/selectflair` (See `Assign user flair template`_).
Specify only the `link` parameter.
This is what the UI does.


Delete user flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/deleteflairtemplate

*scope: modflair*

Delete a flair template.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "flair_template_id","string","A flair ID."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","- There is no user context.

   - You do not have permission.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","- The specified subreddit does not exist.
   - The specified flair UUID does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_deleteflairtemplate


Delete post flair template
~~~~~~~~~~~~~~~~~~~~~~~~~~

The process for deleting a post flair template is exactly the same as for user flair templates.
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

   "flair_type","string","Either `USER_FLAIR` or `LINK_FLAIR`.

   Defaults to `USER_FLAIR` if not specified or some other value is used."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","You do not have permission.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The specified subreddit does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "

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

All parameters should specified. If a parameter is not specified or is an invalid value,
its default will be used.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "flair_enabled","boolean","Whether user flairs are enabled in the subreddit.

   This controls the `user_flair_enabled_in_sr` field on subreddit objects.

   Default: `false`."
   "flair_position","string","Either `left`, `right`, or empty string.

   This controls the `user_flair_position` field on subreddit objects.

   Default: empty string."
   "flair_self_assign_enabled","boolean","
   Whether users are allowed to assign their own user flairs.

   This value is forced false if `flair_enabled` is false
   (but not if `flair_position` is an empty string).

   This controls the `can_assign_user_flair` field on subreddit objects.

   Default: `false`."
   "link_flair_position","string","Either `left`, `right`, or empty string.

   This controls the `link_flair_position` field on subreddit objects.

   Default: empty string."
   "link_flair_self_assign_enabled","boolean","
   Whether users are allowed to assign their own user flairs.

   This value is forced false if `link_flair_position` is empty string.

   This controls the `can_assign_link_flair` field on subreddit objects.

   Default: `false`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","You do not have permission.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The specified subreddit does not exist.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_flairconfig


Reorder user flair templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:patch:: /api/flair_template_order
.. http:patch:: /api/v1/{subreddit}/flair_template_order/{flair_type}

*scope: modflair*

Reorder flair templates.

Flair template IDs should be given as a JSON array in the request body.

The array must contain every flair UUID, otherwise a 400 HTTP error is returned.

If you duplicate an ID the flair will have multiple references in the UI.

If using the `/api/v1/{subreddit}/flair_template_order/{flair_type}` form, the `{flair_type}`
must be specified, otherwise a 404 is returned.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "subreddit","string","The target subreddit."
   "flair_type","string","Either `USER_FLAIR` or `LINK_FLAIR`.

   If not specified, defaults to `USER_FLAIR`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

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

.. csv-table:: Flair Template Object
   :header: "Field","Type (hint)","Description"

   "id","str","A UUID."
   "type","str","Either `text` or `richtext`."
   "mod_only","boolean","True if only moderators can select this flair."
   "text","string","The flair text. This text is available even if `type: richtext`."
   "background_color","str","The flair background color hex string. E.g., `#46d160`.

   If a user flair template, the background color can be unset and the
   value will be the string `""transparent""`.

   For post flairs, they can't be `transparent`.
   "
   "text_color","string","Either `light` or `dark`."
   "allowable_content","string","`all` if both text and emojis are allowed in the flair text,
   `emoji` if only emojis are allowed, `text` if only text is allowed."
   "css_class","string","CSS class. Empty string if no CSS class."
   "max_emojis","integer","The maximum number of emojis allowed in the flair text.
   10 is the limit."
   "text_editable","boolean","Whether users are allowed to edit the flair text."

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

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* You do not have permission."

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

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* You do not have permission."

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

An object of two fields, `current` and `choices`, is returned.

The `current` object represents the current user's flair information. If the `name`
parameter is specified, the flair information of the user with that name in the
subreddit will be used instead. But if the user doesn't exist, the `name` parameter
is ignored and the current user's flair information is used! Note that specifying
`name` only works if the current user is a moderator of the subreddit, otherwise a
403 HTTP error is returned.

The `flair_template_id` field in the `current` object is actually incorrect!
It's just a guess. It scans the user flair templates list from top down and chooses
the first flair template's UUID with a matching text and CSS class. If no match is
found then the value will be null. But when using a flair template and the CSS class
is empty then the value will always be null.

Maybe it's best to just ignore the `current` object because of how janky it is.

If `link` and `name` are specified together, `link` takes preference and `name`
is ignored.

If `link` is used, the `current` object will always be blank! The `flair_template_id`
and `flair_text` fields will be `null` and `flair_css_class` will be an empty string.
I think this is the only time `flair_text` will be null instead of an empty string.
The `flair_position` field will still be accurate.

The `choices` list will always be in terms of the current user. The `name` parameter
only affects the `current` object.

In the `current` object, the `flair_css_class` field may be `null` if a flair template
is assigned and the template doesn't have a CSS class set.

The `flair_position` value is based on the subreddit's configuration and is the same
as the `user_flair_position` field on the Subreddit schema, so it's value will be the
same on all the objects.

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

If there is no user context, a 302 HTTP status is raised, otherwise if you follow the redirect,
this endpoint returns `"{}"` (i.e., a string of an empty JSON object).

.. csv-table:: Form Data (or URL Params)
   :header: "Field","Type (hint)","Description"

   "is_newlink","boolean","Whether to return information on post flairs or user flairs.
   If truthy then return information for post flairs. If not specified then defaults to false.

   If the `link` parameter is specified and its ID is valid then this parameter is ignored."
   "link","string","A submission full ID36. If specified and the ID exists then objects will
   be on post flairs instead of user flairs.

   If the given ID doesn't exist then this parameter is ignored. Thus, it is a good idea to pass
   `is_newlink=1` to ensure that post flair information is always returned."
   "name","string","A redditor username. If not specified, defaults to the current user if available."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "302","There is no user context."
   "403","- You tried to use `name`, targeting another user, and you are not a moderator of the subreddit.
   - The submission specified by `link` does not belong to this subreddit."
   "404","The specified subreddit does not exist."

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

Return user flair associations in a subreddit.

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

   "before","...","See :ref:`Listings overview <listings-overview>`."
   "after","...","See :ref:`Listings overview <listings-overview>`."
   "limit","integer","See :ref:`Listings overview <listings-overview>`.

   The max is 1000."
   "name","string","A username. If the user doesn't exist, or have a flair association then
   the parameter is ignored (i.e., as if it weren't specified).

   When using this parameter it is recommended to specify `limit=1` so that if the name is not found
   then only 1 item is returned instead of (up to) 25."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "302","The specified subreddit does not exist."
   "403","- There is no user context.
   - You are not a moderator of the subreddit."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_flairlist


Show my flair
~~~~~~~~~~~~~

.. http:post:: /r/{subreddit}/api/setflairenabled

*scope: flair*

Set the "Show my flair on this subreddit" option for the current user.

Returns `{"json": {"errors": []}}` on success.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "flair_enabled","boolean","Truthy (any string matching `/^[^0Ff]/`) to enable, falsy to disable.

   If not specified then defaults to false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "404","The subreddit specified in the URL does not exist.","*(HTML document)*"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_setflairenabled


Post appearance
~~~~~~~~~~~~~~~

Upload image
^^^^^^^^^^^^

.. http:post:: /api/v1/{subreddit}/flair_style_asset_upload_s3/{post_flair}

*scope: (unknown)*

Upload an image for use in modifying a post flair's post appearance.

This endpoint is used for obtaining an upload lease.

The upload process is similar to Flair Emoji image uploads, but the endpoint wants an extra `imagetype` parameter.
See :ref:`Emoji upload <emoji-upload>`.

The `action` is typically `//reddit-subreddit-uploaded-media.s3-accelerate.amazonaws.com` for this endpoint.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "imagetype","string","Either `postPlaceholderImage` or `postBackgroundImage`."
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


Config
^^^^^^

.. http:put:: /api/v1/{subreddit}/flair_styles/{post_flair}

*scope: flair*

Set the post appearance options for a post flair template.

All parameters should specified. If a parameter is not specified or is an invalid value,
its default will be used.

Returns an empty JSON object on success, or a JSON object with a
`websocketUrl` field on success if either `postPlaceholderImage`
or `postBackgroundImage` were specified with valid URL locations.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "postTitleColor","string","A hex color. If the given value is not valid,
   the default is used. Default: `#222222`."
   "postBackgroundColor","string","A hex color. If the given value is not valid,
   the default is used. Default: `#FFFFFF`."
   "postPlaceholderImage","string","The URL location of an a uploaded post appearance thumbnail image."
   "postBackgroundImage","string","The URL location of an a uploaded post appearance background image."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
