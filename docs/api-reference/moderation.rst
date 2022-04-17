
Moderation
==========

Actions
-------

Pull moderation items
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/about/modqueue
.. http:get:: [/r/{subreddit}]/about/reports
.. http:get:: [/r/{subreddit}]/about/spam
.. http:get:: [/r/{subreddit}]/about/edited
.. http:get:: [/r/{subreddit}]/about/unmoderated

*scope: read*

Return a paginated listing of submissions/comments relevant to moderators.

Info: `<https://mods.reddithelp.com/hc/en-us/articles/360010090132#h_01FAGH0J7W9H9F7R7BN890P5D7>`_.

These endpoints are paginated listings. See :ref:`Listings Overview <listings-overview>`.
This paginated listing supports the `sr_detail` parameter.

* modqueue: Items requiring moderator review, such as reported things and items caught by the spam filter.
* reports: Items that have been reported.
* spam: Items that have been marked as spam or otherwise removed.
* edited: Items that have been edited recently.
* unmoderated: Submissions that have yet to be approved/removed by a mod.

These endpoints return paginated listings (see :ref:`Listings overview <listings-overview>`).

Each listing contains a mix of submissions and comments, except for unmoderated which only contains submissions.

Requires the `posts` moderator permission (otherwise 403 HTTP error).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL (`{subreddit}`)."
   "only","string","Either `links` or `comments`. Use `links` to only see submissions. Use `comments` to only see comments.

   If an invalid option is specified this parameter is ignored."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "200","The specified subreddit name is too long (over 21 characters) or contains invalid characters.
   A 'page not found' HTML document is returned. (The behaviour is the same using the URL or the `r` parameter.)"
   "403","* You don't have access to the subreddit.

   * You don't have the 'posts' moderators permission."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_about_{location}>`_


Pull subreddit users
~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/{subreddit}/moderators
.. http:get:: /api/v1/{subreddit}/moderators_invited
.. http:get:: /api/v1/{subreddit}/moderators_editable
.. http:get:: /api/v1/{subreddit}/contributors
.. http:get:: /api/v1/{subreddit}/banned
.. http:get:: /api/v1/{subreddit}/muted

*scope: read*

Get redditors that relate to a subreddit.

These endpoints are a paginated but they don't follow the regular listing structure.

The wikicontributors and wikibanned variants use GraphQL so you'll need to use the legacy endpoints for those.

If the `username` parameter is specified, only that user will be returned if they exist
in the result set.

.. _moderator-user-item-schema:

.. csv-table:: Moderator User Item Schema
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 (`t2_` prefixed) of the subject."
   "username","string","The subject's name."
   "accountIcon","string","URL of the subject's account icon."
   "iconSize","integer array","An array of two intergers. Usually `[256, 256]`."
   "moddedAtUTC","integer","UNIX timestamp of when the user was modded."
   "authorFlairText","string","The flair text of the subject. Empty string if no flair text."
   "postKarma","integer","The post karama of the subject."
   "modPermissions","object","A dictionary of strings to booleans.
   E.g.,::

      {'wiki': True,
       'all': True,
       'chat_operator': True,
       'chat_config': True,
       'posts': True,
       'access': True,
       'mail': True,
       'config': True,
       'flair': True}
   "

.. csv-table:: Contributor User Item Schema
   :header: "Field","Type (hint)","Description"

   "id",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "approvedAtUTC","integer","UNIX timestamp of when the user was added."

.. csv-table:: Banned User Item Schema
   :header: "Field","Type (hint)","Description"

   "id",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "bannedAtUTC","integer","UNIX timestamp of when the user was banned."
   "bannedBy","string","The name of the moderator who banned the user."
   "reason","string?","The ban reason text. `null` if no reason text available."
   "modNote","string?","A moderator note. `null` if no mod note."
   "banMessage","string","The moderator note that was sent to the user when they were banned. Empty string if no message."
   "duration","integer?","The number of days until the ban is lifted. Is `null` if it is a permanent ban."
   "postId","unknown?",""
   "commentId","unknown?",""
   "subredditId","string","The full ID36 (`t5_` prefixed) of the subreddit. Should be the same for all items."

.. csv-table:: Muted User Item Schema
   :header: "Field","Type (hint)","Description"

   "id",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator-user-item-schema>`."
   "mutedAtUTC","integer","UNIX timestamp of when the user was muted."
   "mutedBy","string","The name of the moderator who muted the user."
   "reason","string","A moderator note. Empty string if no note."

Endpoint URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "username","string","A username."
   "count","integer","The number of items to return. This is equivalent to the `limit` parameter on listing paginators."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "SUBREDDIT_NOEXIST","400","","
   ``{""fields"": [""subreddit""], ""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You don't have access to the subreddit."


(Legacy) Pull subreddit users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/about/moderators
.. http:get:: [/r/{subreddit}]/about/contributors
.. http:get:: [/r/{subreddit}]/about/wikicontributors
.. http:get:: [/r/{subreddit}]/about/banned
.. http:get:: [/r/{subreddit}]/about/muted
.. http:get:: [/r/{subreddit}]/about/wikibanned

*scope: read*

Get redditors that relate to a subreddit.

These endpoints return paginated listings (see :ref:`Listings overview <listings-overview>`)
except for `.../about/moderators` which is non-paginated.

If the `user` parameter is specified, only that user will be returned.
If the user doesn't exist in the regular listing, an empty listing is returned.

If the specified subreddit doesn't exist an empty listing is returned.

.. csv-table:: User Relationship Item Schema
   :header: "Field","Type (hint)","Description"

   "rel_id","string","Use this for listing pagination."
   "id","string","The full ID36 of the user."
   "name","string","The user's username."
   "date","float","The UNIX timestamp of when the relationship was created. Always a whole number."
   "days_left?","integer?","For the `banned` and `wikibanned` listings only.

   The number of days until the ban is lifted. Is `null` if it is a permanent ban."
   "note","string","For the `banned`, `muted`, and `wikibanned` listings only.

   For `banned` and `wikibanned`, this will be the ban reason plus the mod note separated by a colon and space.
   E.g., f'{ban_reason}: {note}'.

   For `muted`, the mod note.

   Empty string if no note."

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL (`{subreddit}`)."
   "user","string","A username."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You don't have access to the subreddit."
   "404","The specified subreddit name is too long (over 21 characters) or contains invalid characters.
   A 'page not found' HTML document is returned. (The behaviour is the same using the URL or the `r` parameter.)"

.. seealso:: `<https://www.reddit.com/dev/api/#GET_about_{where}>`_


Pull moderation action log entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/about/log

*scope: modlog*

Retrieve recent moderation actions from the mod log.

This endpoint is a paginated listing. See :ref:`Listings Overview <listings-overview>`.
The `limit` parameter has a max value of 500.

Moderator actions taken within a subreddit are logged. Entries in the mod log last for 3 months before
they become inaccessible.

The optional `type` parameter limits the log entries returned to only those of the specified action type.
The optional `mod` parameter can be a comma-delimited list of moderator names to restrict the results to,
or the string `a` to restrict the results to admin actions taken within the subreddit.

.. csv-table:: Mod action object
   :header: "Field","Type (hint)","Description"

   "id","string","Mod action ID. E.g., `ModAction_727b75b0-2214-11ec-99b4-05a9ad5c4e6c`."
   "created_utc","float","Unix timestamp of when the action was done. Always a whole number."
   "action","string","The mod action name."
   "mod_id36","string","The full ID36 of the moderator who initiated the action."
   "mod","string","The name of the moderator who initiated the action."
   "subreddit","string","Name of the subreddit the action was performed in. Since you get the actions
   by subreddit, all actions should have the same value."
   "subreddit_name_prefixed","string","Same as `subreddit` field but prefixed with `r/`."
   "sr_id36","string","The ID36 of the subreddit."
   "description","string","Content depends on the action. This field is always an empty string on some action types."
   "details","string","Content depends on the action. This field is always an empty string on some action types."
   "target_author","string","Content depends on the action. This field is always an empty string on some action types."
   "target_body","string?","Content depends on the action. Value `null` on action types that don't use this field."
   "target_fullname","string?","Content depends on the action. Value `null` on action types that don't use this field."
   "target_permalink","string?","Content depends on the action. Value `null` on action types that don't use this field."
   "target_title","string?","Content depends on the action. Value `null` on action types that don't use this field."

|

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "...","...","Common listing parameters. See :ref:`Listings overview <listings-overview>`.

   The `limit` can be up to 500. (Numbers outside the range of 1-500 will be clamped within range.)"
   "type","string","The action type to filter on."
   "mod","string","A comma separated list of moderator names to filter on. The special name '`a`'
   filters on admin actions."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","You do not have permission to view the mod log of the specified subreddit."


Send moderator invite
~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/friend

*scope: modothers*

Send a moderator invite.

Returns `{"json": {"errors": []}}` on success.
If the user is already invited, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator_invite` or `moderator`"
   "name","string","Name of a target user."
   "permissions","string","A permission description. E.g., `+update,+edit,-manage`.
   Negated permissions can be obmitted, e.g., `+update,+edit,-manage` is the same as `+update,+edit`.

   Permissions: `all`, `access`, `chat_config`, `chat_operator`, `config`, `flair`, `mail`, `posts`, `wiki`.

   To send an invitation with no permissions, `-all` won't work, it is treated the same as `+all`.
   Instead use `-access` or any other valid permission name.

   Default: `+all`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_USER","200","The `name` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_USER"", ""please enter a username"", ""name""]]}}``
   "
   "USER_DOESNT_EXIST","200","The user specified by `name` does not exist.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""name""]]}}``
   "
   "INVALID_PERMISSIONS","200","","
   ``{""json"": {""errors"": [[""INVALID_PERMISSIONS"", ""invalid permissions string"", ""permissions""]]}}``
   "
   "ALREADY_MODERATOR","200","","
   ``{""json"": {""errors"": [[""ALREADY_MODERATOR"", ""That user is already a moderator"", ""name""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","You don't have access to the subreddit you are sending an invite for.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "500","The `type` parameter was not specified.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "


Accept moderator invite
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/accept_moderator_invite

*scope: modothers*

Accept an invitation to moderate a subreddit.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_INVITE_FOUND","200","You don't have a pendning invitation for the subreddit.","
   ``{""json"": {""errors"": [[""NO_INVITE_FOUND"", ""there is no pending invite for that subreddit"", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The non subreddit form of the URL was used and `r` was not specified or was empty."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_accept_moderator_invite


Revoke moderator invite
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/unfriend

*scope: modothers*

Revoke a moderator invite.

Returns empty JSON object on success.
If the user is already invited, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator_invite`"
   "name","string","Name of a target user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","The `name` parameter was not specified, was empty, the name contains invalid characters,
   or the user of the name doesn't exist."
   "403","You don't have access to the subreddit you are revoking an invite for."


Leave moderator
~~~~~~~~~~~~~~~

.. http:post:: /api/leavemoderator

*scope: modself*

Abdicate moderator status in a subreddit.

Be careful with this endpoint. It's possible for a subreddit to not have any moderators.

Returns `{}` on success.
If the specified `id` is not valid or the user is already not a moderator
of the target subreddit, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a subreddit (prefixed with `t5_`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_leavemoderator


Remove moderator
~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/unfriend

*scope: modothers*

Remove a moderator.

Returns empty JSON object on success.
If the given user is not a moderator of the subreddit, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator`"
   "name","string","Name of a target user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","The `name` parameter was not specified, was empty, the name contains invalid characters,
   or the user of the name doesn't exist."
   "403","You don't have access to the subreddit you are revoking an invite for."


Set moderator permissions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/setpermissions

*scope: modothers*

Set the permissions of a moderator or moderator invite.

Returns `{"json": {"errors": []}}` on success.
If the user is already invited, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator`: change permissions of a moderator.

   `moderator_invite`: change permissions of a moderator invite."
   "name","string","Name of a target user."
   "permissions","string","A permission description. See `POST /api/friend`.

   Default: `+all`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_USER","200","The `name` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_USER"", ""please enter a username"", ""name""]]}}``
   "
   "USER_DOESNT_EXIST","200","The user specified by `name` does not exist.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""name""]]}}``
   "
   "INVALID_PERMISSION_TYPE","200","The user specified by `name` isn't a moderator (if `type: moderator`)
   or mod invitee (if `type: moderator_invite`).","
   ``{""json"": {""errors"": [[""INVALID_PERMISSION_TYPE"", ""permissions don't apply to that type of user"", ""type""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You don't have access to the subreddit you are revoking an invite for."
   "404","The subreddit specified by `r` does not exist. A 'page not found' HTML document is also returned."


Ban user
~~~~~~~~

Use `POST [/r/{subreddit}]/api/friend` with `type: banned` form data.

----------

.. http:post:: [/r/{subreddit}]/api/friend

*scope: modcontributors*

Create a relationship between a user and subreddit.

Using `type: wikibanned` or `type: modcontributors` additionally requires the `modwiki` scope.

When banning an already banned user (as to change the ban reason or note), if the duration is changed
then a new PM will be issued to the target user informing them of the duration change.

Returns `{"json": {"errors": []}}` on success.
If the user is already in the relationship, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","Either: `banned`, `muted`, `contributor`, `wikibanned`, `wikicontributor`."
   "name","string","Name of a target user."
   "ban_reason","string","For when `type`: `banned`, `wikibanned`.

   The bad reason. No longer than 100 characters.

   Default: empty string."
   "note","string","For when `type`: `banned`, `muted`, `wikibanned`.

   A moderator note. No longer than 300 characters.

   Default: empty string."
   "duration","integer","For when `type`: `banned`, `wikibanned`.

   The duration of the ban. Specify a number from 1 to 999 as the number of days.
   To make a ban permanent, specify an empty string, or omit this parameter.

   To change the duration of a ban, re-issue a request to this endpoint with a new duration.
   A PM is sent to the target user informing them of the ban duration change.

   Default: empty string."
   "ban_message","string","For when `type`: `banned`.

   The note to include in the ban PM, as markdown text.

   Note that a PM is always sent to the banned user when a ban is issued.
   This ban message shows in the PM under a section called ""Note from the moderators:"".

   Default: empty string."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "BAD_NUMBER","200","The number specified for `duration` is not in the range 1 to 999,
   when `type: banned` or `type`: `wikibanned`.","
   ``{""json"": {""errors"": [[""BAD_NUMBER"", ""that number isn't in the right range (1 to 999)"", ""duration""]]}}``
   "
   "TOO_LONG","200","* (1) The value specified by `ban_reason` is over 100 characters.

   * The value specified by `note` is over 300 characters.","
   (1): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 100 characters"", ""ban_reason""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","The `id` or `name` parameter was not specified."
   "403","* The non subreddit form of the URL was used and `r` was not specified or was empty.

   * You don't have access to the subreddit you are operating on."
   "404","The subreddit specified by `r` does not exist. A 'page not found' HTML document is also returned."
   "500","* The `type` parameter was not specified.

   * The `name` parameter was not specified, was empty, or the name contains invalid characters.

   * The user specified by `name` does not exist, or was deleted, banned, etc."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_friend

----------

.. http:post:: [/r/{subreddit}]/api/unfriend

*scope: modcontributors*

Remove a relationship between a user and subreddit.

Using `type: wikibanned` or `type: modcontributors` additionally requires the `modwiki` scope.

If both `id` and `name` are used together, `id` will take precedence and `name` will be ignored.

Returns an empty JSON object on success.
If the user is not already in the relationship, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","Either: `banned`, `muted`, `contributor`, `wikibanned`, `wikicontributor`."
   "id","string","The full ID36 of a target user (prefixed with `t2_`)."
   "name","string","Name of a target user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","* The `id` or `name` parameter was not specified.

   * The `id` or `name` parameter was not specified, was empty, the name contains invalid characters,
     or the user of the name doesn't exist."
   "403","* The non subreddit form of the URL was used and `r` was not specified or was empty.

   * You don't have access to the subreddit you are operating on."
   "404","The subreddit specified by `r` does not exist. A 'page not found' HTML document is also returned."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_unfriend


Unban user
~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/unfriend` with `type: banned` form data.


Mute user
~~~~~~~~~

Use `POST [/r/{subreddit}]/api/friend` with `type: muted` form data.


Unmute user
~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/unfriend` with `type: muted` form data.


Add approved contributor
~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/friend` with `type: contributor` form data.


Leave approved contributor
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/leavecontributor

*scope: modself*

Abdicate approved contributor status in a subreddit.

Returns `{}` on success.
If the specified `id` is not valid or the user is already not an approved contributor
of the target subreddit, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a subreddit (prefixed with `t5_`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_leavecontributor


Remove approved contributor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/unfriend` with `type: contributor` form data.


Ban wiki contributor
~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/friend` with `type: wikicontributor` form data.


Unban wiki contributor
~~~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/unfriend` with `type: wikibanned` form data.


Add approved wiki contributor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/friend` with `type: wikibanned` form data.


Remove approved wiki contributor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `POST [/r/{subreddit}]/api/unfriend` with `type: wikicontributor` form data.


Snooze reports
~~~~~~~~~~~~~~

.. http:post:: /api/snooze_reports
.. http:post:: /api/unsnooze_reports

*scope: modposts*

Prevent future reports on a post/comment from causing notifications for 7 days.

Specify a report reason text to snooze reports on. For 7 days, any user who submits a report
reason with the matching snoozed reason text not be escalated to moderators.

Returns `{}` on success. If the target is already snoozed/unsnoozed, it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a post or comment (prefixed with `t3_` or `t1_`)."
   "reason","string","The report reason text to snooze on."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* The `id` parameter was not specified.

   * The target specified by `id` was not found, or points to an item you are not a moderator of."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_snooze_reports


Create removal reason
~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/{subreddit}/removal_reasons

*scope: (unknown)*

Create a removal reason.

Info: `<https://mods.reddithelp.com/hc/en-us/articles/360010094892-Removal-Reasons>`_.

Returns a JSON object on success, like the following::

   {"id": "17hx52nzlartd"}

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "title","string","A title for this removal reason."
   "message","string","The removal reason message."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "MOD_REQUIRED","400","* There is no user context.

   * The current user is not a moderator of the target subreddit.","
   ``{""explanation"": ""You must be a moderator to do that."", ""message"": ""Bad Request"", ""reason"": ""MOD_REQUIRED""}``
   "
   "NO_TEXT","400","* The `title` parameter was not specified or was empty.

   * The `message` parameter was not specified or was empty.","
   ``{""fields"": [""title""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "
   "TOO_LONG","400","* (1) The value specified for `title` is over 50 characters.

   * The value specified for `message` is over 10000 characters.","
   (1): ``{""fields"": [""title""], ""explanation"": ""This field must be under 50 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The target subreddit does not exist."


Retrieve removal reasons
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/{subreddit}/removal_reasons

*scope: (unknown)*

Get a list of removal reasons.

Returns a JSON object on success, like the following::

   {"data": {"17hxgacq8byjh": {"message": "Self promoting posts are prohibited.",
                            "id": "17hxgacq8byjh",
                            "title": "Self Promotion"},
             "17hxexsxbr0ye": {"message": "onions onions yay yay",
                               "id": "17hxexsxbr0ye",
                               "title": "Only onions allowed"},
             "17hxg7deji23d": {"message": "Olives are a no no",
                               "id": "17hxg7deji23d",
                               "title": "No olive related content"},
             "17hxgpamf6jpf": {"message": "Party on dudes!",
                               "id": "17hxgpamf6jpf",
                               "title": "Be excellent to each other"}},
    "order": ["17hxexsxbr0ye", "17hxg7deji23d", "17hxgacq8byjh", "17hxgpamf6jpf"]}

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "MOD_REQUIRED","400","* There is no user context.

   * The current user is not a moderator of the target subreddit.","
   ``{""explanation"": ""You must be a moderator to do that."", ""message"": ""Bad Request"", ""reason"": ""MOD_REQUIRED""}``
   "
   "SUBREDDIT_NOEXIST","400","The target subreddit does not exist.","
   ``{""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "


Update removal reason
~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /api/v1/{subreddit}/removal_reasons/{reason_id}

*scope: (unknown)*

Update a removal reason's title and message.

Both parameters title and message must be specified otherwise a `NO_TEXT` API error is returned.

Returns zero bytes on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "title","string","A title for this removal reason."
   "message","string","The removal reason message."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "MOD_REQUIRED","400","* There is no user context.

   * The current user is not a moderator of the target subreddit.","
   ``{""explanation"": ""You must be a moderator to do that."", ""message"": ""Bad Request"", ""reason"": ""MOD_REQUIRED""}``
   "
   "SUBREDDIT_NOEXIST","400","The target subreddit does not exist.","
   ``{""fields"": [""subreddit""], ""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "
   "NO_TEXT","400","* The `title` parameter was not specified or was empty.

   * The `message` parameter was not specified or was empty.","
   ``{""fields"": [""title""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "
   "INVALID_ID","400","* The specified removal reason ID was not found.

   * The specified removal reason ID contained invalid characters (e.g., it contained uppercase letters).","
   ``{""fields"": [""reason_id""], ""explanation"": ""The specified id is invalid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ID""}``
   "
   "TOO_LONG","400","* The value specified for `title` is over 50 characters.

   * The value specified for `message` is over 10000 characters.","
   ``{""fields"": [""title""], ""explanation"": ""This field must be under 50 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "


Delete removal reason
~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /api/v1/{subreddit}/removal_reasons/{reason_id}

*scope: (unknown)*

Delete a removal reason.

Returns zero bytes on success. If the specified ID did not exist it is treated as a success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "INVALID_ID","400","The specified removal reason ID contained invalid characters (e.g., it contained uppercase letters).","
   ``{""fields"": [""reason_id""], ""explanation"": ""The specified id is invalid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ID""}``
   "
   "MOD_REQUIRED","400","* There is no user context.

   * The current user is not a moderator of the target subreddit.","
   ``{""explanation"": ""You must be a moderator to do that."", ""message"": ""Bad Request"", ""reason"": ""MOD_REQUIRED""}``
   "
   "SUBREDDIT_NOEXIST","400","The target subreddit does not exist.","
   ``{""fields"": [""subreddit""], ""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "


Create moderation user note
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/notes

*scope: modnote*

Create a user note.

More info: https://www.reddit.com/r/modnews/comments/t8vafc/announcing_mod_notes/.

Returns the created note. Example output::

   {"created": {"subreddit_id": "t5_g495e",
                "operator_id": "t2_4x25quk",
                "mod_action_data": {"action": null,
                                    "reddit_id": null,
                                    "details": null,
                                    "description": null},
                "subreddit": "Pyprohly_test3",
                "user": "test",
                "operator": "Pyprohly",
                "id": "ModNote_0b168fe2-c0fe-4542-be9d-4008991a853a",
                "user_note_data": {"note": "asdf",
                                   "reddit_id": null,
                                   "label": null},
                "user_id": "t2_1tlb",
                "created_at": 1650098853,
                "type": 'NOTE'}}

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "subreddit","string","The target subreddit name."
   "user","string","The target user name."
   "note","string","The content of the note. Max 250 characters."
   "label","string","Options: `BOT_BAN`, `PERMA_BAN`, `BAN`, `ABUSE_WARNING`, `SPAM_WARNING`, `SPAM_WATCH`,
   `SOLID_CONTRIBUTOR`, `HELPFUL_USER`.
   "
   "reddit_id","string","A full ID36 of a comment (`t1`) or submission (`t3`). Can be any comment or submission,
   even one outside of the subreddit."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_DOESNT_EXIST","400","The user name specified by `user` does not exist.","
   ``{""fields"": [""user""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "
   "BAD_SR_NAME","400","The subreddit specified by `subreddit` does not exist.","
   ``{""fields"": [""subreddit""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "
   "NO_TEXT","400","The `note` parameter was not specified or was empty.","
   ``{""fields"": [""note""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "
   "TOO_LONG","400","The value for the `note` parameter was too long, over 250 characters.","
   ``{""fields"": [""note""], ""explanation"": ""This field must be under 250 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "
   "INVALID_OPTION","400","The value specified for `label` is invalid.","
   ``{""fields"": [""label""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "
   "NO_THING_ID","400","The value specified for `reddit_id` is invalid.","
   ``{""fields"": [""reddit_id""], ""explanation"": ""id not specified"", ""message"": ""Bad Request"", ""reason"": ""NO_THING_ID""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You are not a moderator of the target subreddit.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_mod_notes


Delete moderation note
~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /api/mod/notes

*scope: modnote*

Delete a moderation note.

This endpoint can be used to delete either user or action type notes.

This endpoint must be given three pieces of information: the note ID, the subreddit name and the user name.
If the `subreddit` or `user` information is incorrect, the endpoint will raise a 500 HTTP error.

Returns the following on success::

   {"deleted": True}

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "note_id","string","The ID of the note to be deleted. It should be prefixed with `ModNote_`."
   "subreddit","string","The target subreddit name."
   "user","string","The target user name."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PARAMETER_REQUIRED","400","The `note_id` parameter was not specified or was empty.","
   ``{""fields"": [""note_id""], ""explanation"": ""The parameter \""note_id\"" is required."", ""message"": ""Bad Request"", ""reason"": ""PARAMETER_REQUIRED""}``
   "
   "INVALID_ID","400","The value specified by `note_id` was invalid.","
   ``{""fields"": [""note_id""], ""explanation"": ""The specified id is invalid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_ID""}``
   "
   "USER_DOESNT_EXIST","400","The `user` parameter was not specified or was empty.","
   ``{""fields"": [""user""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "
   "BAD_SR_NAME","400","The `subreddit` parameter was not specified or was empty.","
   ``{""fields"": [""subreddit""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The `subreddit` or `user` specified is incorrect for the given note ID.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: https://www.reddit.com/dev/api/#DELETE_api_mod_notes


Pull moderation notes
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/mod/notes

*scope: modnote*

Get moderation notes of a user in a subreddit.

The endpoint returns *moderation notes* which could be a combination of *user notes* (when `type: NOTE`)
or *action notes*.

Example return object when both the specified user and subreddit exist but you do not have permission to
view the relevant data, or no data exists for that user::

   {"mod_notes": [], "start_cursor": None, "end_cursor": None, "has_next_page": False}

Return object schema:

* `mod_notes` (object array): An array of moderation notes.
* `start_cursor` (string?): The pagination cursor of the first moderation note.
* `end_cursor` (string?): The pagination cursor of the last moderation note.
* `has_next_page` (boolean): True if more results exist.

|

.. csv-table:: Mod note object
   :header: "Field","Type (hint)","Description"

   "id","string","Mod note ID. E.g., `ModNote_e610966c-279a-11ec-812d-f1e67fc3cfa1`."
   "created_at","integer","Unix timestamp of when the mod note entry was made. Always a whole number."
   "type","string","The mod note type. Possible values same as the `filter` parameter of the `GET /api/mod/notes` endpoint."
   "cursor?","string","A pagination cursor to be used as the value of the `before` parameter
   in the `GET /api/mod/notes` endpoint.

   This field only exists from notes that come from the `GET /api/mod/notes` endpoint."
   "subreddit_id","string","The full ID36 (`t5_` prefixed) of the subreddit."
   "subreddit","string","The name of the subreddit."
   "operator_id","string","The full ID36 (`t2_` prefixed) of the moderator who actioned the note."
   "operator","string","The name of the moderator who actioned the note."
   "user_id","string","The full ID36 (`t2_` prefixed) of the user who this note applies."
   "user","string","The name of the user who this note applies."
   "mod_action_data","object","Moderation action data. The information in this object is only useful
   if the note is an action note, not a user note.

   The only field value that is not `null` when the note is a user note is the `reddit_id` field, but
   this field is duplicated at `(root).user_note_data.reddit_id` anyway.

   Schema:

      * `action` (string?): The name of the action. In lowercase. Value is `null` if `type: NOTE` on the root.
      * `reddit_id` (string?): The full ID36 of some relevant object, either a comment or submission.
        Value should always match `(root).user_note_data.reddit_id`. Value may be `null`.
      * `details` (string?): The full ID36 . Value is `null` if `type: NOTE` on the root.
      * `description` (string?): The full ID36 . Value is `null` if `type: NOTE` on the root.
   "
   "user_note_data","object","User note data. The information in this object is only useful
   if the note is a user note, not an action note.

   Schema:

      * `note` (string?): The content of the user note. Value `null` if root object does not represent a user note.
      * `label` (string?): Note label.

        Possible values: `ABUSE_WARNING`, `SPAM_WARNING`, `SPAM_WATCH`,
        `SOLID_CONTRIBUTOR`, `HELPFUL_USER`, `BOT_BAN`, `PERMA_BAN`, `BAN`.

        Value is `null` if no label was assigned to this note, or the note object not a user note.

      * `reddit_id` (string?): The full ID36 of a comment or submission object if one was assigned to this note
        during creation. Value should always match `(root).mod_action_data.reddit_id`.
   "

|

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "limit","string","The number of entries to return. Default: 25, max: 100."
   "before","string","A pagination cursor."
   "subreddit","string","The target subreddit name."
   "user","string","The target user name."
   "filter","string","One of: `NOTE`, `APPROVAL`, `REMOVAL`, `BAN`, `MUTE`, `INVITE`, `SPAM`, `CONTENT_CHANGE`, `MOD_ACTION`, `ALL`. Default: `ALL`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_DOESNT_EXIST","400","The user name specified by `user` does not exist.","
   ``{""fields"": [""user""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "
   "BAD_SR_NAME","400","The subreddit specified by `subreddit` does not exist.","
   ``{""fields"": [""subreddit""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "
   "INVALID_OPTION","400","An invalid value was specified for the `filter` parameter.","
   ``{""fields"": [""filter""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_mod_notes


Get latest moderation user note of user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/mod/notes/recent

*scope: modnote*

Get the most recently written user note for some user.

Both parameters should be comma separated lists of equal lengths. The entries from both lists will be zipped together.
If one list is longer than the other the excess entries will be ignored.

If either subreddit or user does not exist then a `null` will be output in the list. But if only one pair of arguments
were given then a 400 HTTP error is returned instead.

Up to 500 pairs of subreddit names and usernames are accepted at a time.

The response contains a list of mod notes in the order that subreddits and users were given.
If no note exists for a given pair, `null` will take its place in the list.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "subreddits","string","A comma separated list of subreddit names."
   "users","string","A comma separated list of moderator names."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "PARAMETER_REQUIRED","400","(1): The `subreddits` parameter was not specified or was empty.

   (2): The `users` parameter was not specified or was empty.","
   (1): ``{""fields"": [""subreddits""], ""explanation"": ""The parameter \""subreddits\"" is required."", ""message"": ""Bad Request"", ""reason"": ""PARAMETER_REQUIRED""}``

   (2): ``{""fields"": [""accounts""], ""explanation"": ""The parameter \""accounts\"" is required."", ""message"": ""Bad Request"", ""reason"": ""PARAMETER_REQUIRED""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","Only one pair of arguments were given and either the subreddit or user specified do not exist.","
   ``{""message"": ""Bad Request"", ""error"": 400}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_mod_notes_recent
