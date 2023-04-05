
Live Thread
===========

Overview
--------

Live Thread Schema
~~~~~~~~~~~~~~~~~~

.. csv-table:: Live Thread Schema
   :header: "Field","Type (hint)","Description"

   "id","string","E.g., `177beztuzebxj`."
   "name","string","The live thread ID with `LiveUpdateEvent_` prepended. E.g., `LiveUpdateEvent_177beztuzebxj`."
   "title","string","The title of the live thread."
   "created_utc","float","Unix timestamp of when the live thread was made. Will always be a whole number."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "description","string","Live thread description as markdown text. This is the text below the title."
   "description_html","string","Live thread description as HTML."
   "resources","string","The sidebar text in markdown."
   "resources_html","string","The sidebar text in HTML."
   "websocket_url","string","Websocket URL. Connect to this websocket to stream live updates."
   "state","string","`live` if active, `complete` if closed."
   "nsfw","boolean","Is live thread marked as NSFW."
   "is_announcement","boolean",""
   "announcement_url","string",""
   "total_views","integer?",""
   "button_cta","string",""
   "viewer_count","integer","The number of subscribers. Value is fuzzed."
   "num_times_dismissable","integer",""
   "viewer_count_fuzzed","boolean","Always true."
   "icon","string","Unused?"


Live Thread Update Schema
~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Live Thread Update Schema
   :header: "Field","Type (hint)","Description"

   "id","string","E.g., `890e9242-d7fb-11eb-b450-0ed185f1b209`."
   "name","string","The live update ID with `LiveUpdate_` prepended. E.g., `LiveUpdate_890e9242-d7fb-11eb-b450-0ed185f1b209`."
   "author","string?","The name of the user who posted the update.

   Value null if the user account was deleted.
   The UI displays deleted accounts as `[deleted]`.
   "
   "body","string","The markdown content body."
   "body_html","string","The content body in HTML."
   "created_utc","float","Unix timestamp of when the live update was made. Will always be a whole number."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "embeds","unknown array",""
   "mobile_embeds","unknown array",""
   "stricken","boolean","True if the update has been stricken."


Actions
-------

Get
~~~

.. http:get:: /live/{thread}/about

*scope: read*

Get a live thread.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_live_{thread}_about>`_


Bulk get
~~~~~~~~

.. http:get:: /api/live/by_id/{threads}

*scope: read*

Get a listing of live events by ID.

Specify a comma-delimited list of live thread IDs in `{threads}`. IDs may be prefixed with `LiveUpdateEvent_`,
i.e., `177beztuzebxj` or `LiveUpdateEvent_177beztuzebxj` will work.

If more than 100 IDs are given, only the first 100 are considered.

The endpoint returns entries in the same order as specified.

If no IDs are given, i.e. `GET /api/live/by_id/` is requested, then a 404 HTTP error is returned.

If one of the IDs specified does not exist then a 500 HTTP error is returned.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","One of the IDs specified does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_live_by_id_{names}>`_


Create
~~~~~~

.. http:post:: /api/live/create

*scope: submit*

Create a new live thread.

Returns the new live thread's ID. Return value example::

   {"json": {"errors": [], "data": {"id": "177ywte7tl86e"}}}

|

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "title","string","A string no longer than 120 characters."
   "description","string","Markdown. Default: empty string."
   "resources","string","Markdown. Default: empty string."
   "nsfw","boolean","Whether to mark the live thread as NSFW. Default false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `title` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""title""]]}}``
   "
   "RATELIMIT","200","You must wait one minute before creating another live thread.","
   ``{""json"": {""errors"": [[""RATELIMIT"", ""Looks like you've been doing that a lot. Take a break for 51 seconds before trying again."", ""ratelimit""]]}}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_create>`_


Configure
~~~~~~~~~

.. http:post:: /api/live/{thread}/edit

*scope: livemanage*

Configure the live thread.

Requires the `settings` live thread permission.

All parameters must be specified otherwise they will be set to their effective defaults.

Returns ``{"json": {"errors": []}}`` on success.

|

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "title","string","A string no longer than 120 characters."
   "description","string","Markdown. Default: empty string."
   "resources","string","Markdown. Default: empty string."
   "nsfw","boolean","Whether to mark the live thread as NSFW. Default false."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You do not have the `settings` live thread permission.
   * You do not have permission.
   "
   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_edit>`_


Close
~~~~~

.. http:post:: /api/live/{thread}/close_thread

*scope: livemanage*

Permanently close the live thread, disallowing future updates.

Requires the `close` permission.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You do not have the `close` permission.
   * The live thread is already closed.
   "
   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_close_thread>`_


Get currently featured live thread
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/live/happening_now

*scope: read*

Get the currently featured live thread.

Returns an empty 204 response if no thread is currently being featured.

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_live_happening_now>`_


Get thread live update
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /live/{thread}/updates/{update}

*scope: read*

Get a specific live update in a live thread.

Returns a listing.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread ID or live update ID does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_live_{thread}_updates_{update_id}>`_


Get thread live updates
~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /live/{thread}

*scope: read*

Get a listing of live updates in a live thread.

This endpoint is a listing. See :ref:`Listings overview <listings-overview>`.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_live_{thread}>`_


Post live update
~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/update

*scope: submit*

Post a live update to the thread.

Requires the `update` permission.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "body","string","Markdown text."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","The `body` parameter was not specified or the value was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""body""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_update>`_


Strike live update
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/strike_update

*scope: edit*

Strike (mark incorrect and cross out) the content of a live update.

Requires that specified update must have been authored by the user
or that you have the `edit` permission.

Striken updates cannot be unstriken.

If an already striken item is striken it is treated as a success.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","The ID of a single live update. The ID must be prefixed with `LiveUpdate_`.
   E.g., `LiveUpdate_ff87068e-a126-11e3-9f93-12313b0b3603`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_THING_ID","200","* The `id` parameter was not specified or was empty.

   * The live update specified by `id` does not exist.","
   ``{""json"": {""errors"": [[""NO_THING_ID"", ""ID not specified"", ""id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You don't have permission to strike the live update."
   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_strike_update>`_


Delete live update
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/delete_update

*scope: edit*

Delete a live update.

Requires that specified update must have been authored by the current user
or that you have the `edit` permission.

If an already deleted update is specified, the action will be treated as a success.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","The ID of a single live update. The ID must be prefixed with `LiveUpdate_`.
   E.g., `LiveUpdate_ff87068e-a126-11e3-9f93-12313b0b3603`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_THING_ID","200","* The `id` parameter was not specified or was empty.

   * The live update specified by `id` does not exist.","
   ``{""json"": {""errors"": [[""NO_THING_ID"", ""ID not specified"", ""id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You don't have permission to delete the live update."
   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_delete_update>`_


List contributors
~~~~~~~~~~~~~~~~~

.. http:get:: /live/{thread}/contributors

*scope: read*

Get a list of users that contribute to a thread.

If the invoking user has the `manage` permission, the endpoint returns an array of two user list objects.
The first user list contains a list of the current contributors to the live thread and their permissions.
The second user list contains a list of pending contributor invitations and their permissions.

If the invoking user does not have the `manage` permission, the endpoint returns a single user list object
that contains a list of the current contributors to the live thread and their permissions.

Example return value when the invoking user has the `manage` permission::

   [{"kind": "UserList",
     "data": {"children": [{"rel_id": null,
                            "permissions": ["all"],
                            "id": "t2_4x25quk",
                            "name": "Pyprohly"}]}},
    {"kind": "UserList",
     "data": {"children": [{"rel_id": null,
                            "permissions": ["settings",
                                            "edit",
                                            "manage",
                                            "update",
                                            "discussions",
                                            "close"],
                            "id": "t2_1kc4pi1k",
                            "name": "BatchBot"}]}}]

Example return value when the invoking user does not have the `manage` permission::

   {"kind": "UserList",
    "data": {"children": [{"rel_id": null,
                           "permissions": ["all"],
                           "id": "t2_cf4dj0vp",
                           "name": "BreakingSn00ze"}]}}

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_live_{thread}_contributors>`_


Send contributor invite
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/invite_contributor

*scope: livemanage*

Invite a user to contribute to the live thread.

Requires the `manage` live thread permission.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "type","string","Specify `liveupdate_contributor_invite` or `liveupdate_contributor`."
   "name","string","The name of a user."
   "permissions","string","A permission description. E.g., `+update,+edit,-manage`.
   Negated permissions can be obmitted, e.g., `+update,+edit,-manage` is the same as `+update,+edit`.

   Permissions: `all`, `close`, `discussions`, `edit`, `manage`, `settings`, `update`.

   Default: empty string. On the interface it'll say 'no permissions'."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "NO_USER","200","The `name` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_USER"", ""please enter a username"", ""name""]]}}``
   "
   "USER_DOESNT_EXIST","200","The user specified by `name` does not exist.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""name""]]}}``
   "
   "INVALID_PERMISSION_TYPE","200","The `type` parameter was not specified or is invalid.","
   ``{""json"": {""errors"": [[""INVALID_PERMISSION_TYPE"", ""permissions don't apply to that type of user"", ""type""]]}}``
   "
   "LIVEUPDATE_ALREADY_CONTRIBUTOR","200","The user specified by `name` is already a contributor or has already been invited.","
   ``{""json"": {""errors"": [[""LIVEUPDATE_ALREADY_CONTRIBUTOR"", ""that user is already a contributor"", ""name""]]}}``
   "
   "INVALID_PERMISSIONS","200","The string specified by the `permissions` parameter is invalid.","
   ``{""json"": {""errors"": [[""INVALID_PERMISSIONS"", ""invalid permissions string"", ""permissions""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You do not have the `manage` permission."
   "404","The specified live thread does not exist."
   "500","The permission string has a leading or trailing comma."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_invite_contributor>`_


Accept contributor invite
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/accept_contributor_invite

*scope: livemanage*

Accept an invitation to contribute to a live thread.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "LIVEUPDATE_NO_INVITE_FOUND","200","You don't have an invitation for the specified live thread.","
   ``{""json"": {""errors"": [[""LIVEUPDATE_NO_INVITE_FOUND"", ""there is no pending invite for that thread"", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_create>`_


Revoke contributor invite
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/rm_contributor_invite

*scope: livemanage*

Revoke an outstanding contributor invite.

Requires the `manage` live thread permission.

If attempting to remove the invite for a user that was not invited, the action is treated as a success.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of the user to revoke an invitation for."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You do not have the `manage` permission.
   * You do not have permission."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_accept_contributor_invite>`_


Leave contributor
~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/leave_contributor

*scope: livemanage*

Abdicate contributorship of the thread.

It is possible to leave a live thread and not have any contributors to it.

If leaving a live thread you were not a contributor to, the action is treated as a success.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: API Errors
   :header: "Error","Description"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_leave_contributor>`_


Remove contributor
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/rm_contributor

*scope: livemanage*

Revoke another user's contributorship.

Requires the `manage` live thread permission.

It is possible to remove your own contributorship, having the same effect as
`POST /api/live/{thread}/leave_contributor`.

If the user specified by the `id` parameter is not a contributor, the action is treated as a success.
If the ID of a non-existing user is specified, a 500 HTTP error is returned.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of the user to revoke contributorship for."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You are not a contributor to the live thread that has the `manage` permission."
   "404","The specified live thread does not exist."
   "500","The `id` parameter was not specified, was invalid, or empty."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_rm_contributor>`_


Set contributor permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/set_contributor_permissions

*scope: livemanage*

Change a contributor or a contributor invite's permissions.

Requires the `manage` live thread permission.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "type","string","Specify `liveupdate_contributor` to change the permissions for a contributor.

   Specify `liveupdate_contributor_invite` to change the permissions for a contributor invite."
   "name","string","The name of a user."
   "permissions","string","A permission description. E.g., `+update,+edit,-manage`.
   Negated permissions can be obmitted, e.g., `+update,+edit,-manage` is the same as `+update,+edit`.

   Permissions: `all`, `close`, `discussions`, `edit`, `manage`, `settings`, `update`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_USER","200","The `name` parameter was empty.","
   ``{""json"": {""errors"": [[""NO_USER"", ""please enter a username"", ""name""]]}}``
   "
   "USER_DOESNT_EXIST","200","The user specified by `name` does not exist.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""name""]]}}``
   "
   "INVALID_PERMISSION_TYPE","200","The `type` parameter was not specified or is invalid.","
   ``{""json"": {""errors"": [[""INVALID_PERMISSION_TYPE"", ""permissions don't apply to that type of user"", ""type""]]}}``
   "
   "INVALID_PERMISSIONS","200","The string specified by the `permissions` parameter is invalid.","
   ``{""json"": {""errors"": [[""INVALID_PERMISSIONS"", ""invalid permissions string"", ""permissions""]]}}``
   "
   "LIVEUPDATE_NO_INVITE_FOUND","200","`type: liveupdate_contributor_invite` was specified and the
   user specified by `name` does not have an invite.","
   ``{""json"": {""errors"": [[""LIVEUPDATE_NO_INVITE_FOUND"", ""there is no pending invite for that thread"", ""user""]]}}``
   "
   "LIVEUPDATE_NOT_CONTRIBUTOR","200","`type: liveupdate_contributor` was specified and the user specified by `name`
   is not a contributor.","
   ``{""json"": {""errors"": [[""LIVEUPDATE_NOT_CONTRIBUTOR"", ""that user is not a contributor"", ""user""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* There is no user context.
   * You do not have the `manage` live thread permission."
   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_set_contributor_permissions>`_


List discussions
~~~~~~~~~~~~~~~~

.. http:get:: /live/{thread}/discussions

*scope: read*

Get a listing of Submissions linking to this thread.

This endpoint is a listing. See :ref:`Listings overview <listings-overview>`.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The specified live thread does not exist."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_live_{thread}_discussions>`_


Hide discussion
~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/hide_discussion

*scope: livemanage*

\.\.\.

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_hide_discussion>`_


Unhide discussion
~~~~~~~~~~~~~~~~~

.. http:post:: /api/live/{thread}/unhide_discussion

*scope: livemanage*

\.\.\.

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_unhide_discussion>`_


Report
~~~~~~

.. http:post:: /api/live/{thread}/report

*scope: report*

\.\.\.

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_live_{thread}_report>`_
