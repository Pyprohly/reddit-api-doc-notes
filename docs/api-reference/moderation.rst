
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

These endpoints are paginated listings. See :ref:`Listings Overview <listings_overview>`.
This paginated listing supports the `sr_detail` parameter.

* modqueue: Items requiring moderator review, such as reported things and items caught by the spam filter.
* reports: Items that have been reported.
* spam: Items that have been marked as spam or otherwise removed.
* edited: Items that have been edited recently.
* unmoderated: Submissions that have yet to be approved/removed by a mod.

These endpoints return paginated listings (see :ref:`Listings overview <listings_overview>`).

Each listing contains a mix of submissions and comments, except for unmoderated which only contains submissions.

Requires the `posts` moderator permission (otherwise 403 HTTP error).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL (`{subreddit}`)."
   "only","string","Either `links` or `comments`. Use `links` to only see submissions. Use `comments` to only see comments.

   If an invalid option is specified this parameter is ignored."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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

.. _moderator_user_item_schema:

.. csv-table:: Moderator User Item Schema
   :header: "Field","Type (hint)","Description"
   :escape: \

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
   :escape: \

   "id",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "approvedAtUTC","integer","UNIX timestamp of when the user was added."

.. csv-table:: Banned User Item Schema
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
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
   :escape: \

   "id",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "username",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "accountIcon",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "iconSize",".","See :ref:`Moderator User Item Schema <moderator_user_item_schema>`."
   "mutedAtUTC","integer","UNIX timestamp of when the user was muted."
   "mutedBy","string","The name of the moderator who muted the user."
   "reason","string","A moderator note. Empty string if no note."

Endpoint URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "username","string","A username."
   "count","integer","The number of items to return. This is equivalent to the `limit` parameter on listing paginators."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "SUBREDDIT_NOEXIST","The subreddit specified does not exist.

   *\"Hmm, that community doesn't exist. Try checking the spelling.\"* -> subreddit"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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

These endpoints return paginated listings (see :ref:`Listings overview <listings_overview>`)
except for `.../about/moderators` which is non-paginated.

If the `user` parameter is specified, only that user will be returned.
If the user doesn't exist in the regular listing, an empty listing is returned.

If the specified subreddit doesn't exist an empty listing is returned.

.. csv-table:: User Relationship Item Schema
   :header: "Field","Type (hint)","Description"
   :escape: \

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
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL (`{subreddit}`)."
   "user","string","A username."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You don't have access to the subreddit."
   "404","The specified subreddit name is too long (over 21 characters) or contains invalid characters.
   A 'page not found' HTML document is returned. (The behaviour is the same using the URL or the `r` parameter.)"

.. seealso:: `<https://www.reddit.com/dev/api/#GET_about_{where}>`_


Pull moderation actions
~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/about/log

*scope: modlog*

Retrieve recent moderation actions.

This endpoint is a paginated listing. See :ref:`Listings Overview <listings_overview>`.
The `limit` parameter has a max value of 500.

Moderator actions taken within a subreddit are logged. Entries in the mod log last for 3 months before
they become inaccessible.

The optional `type` parameter limits the log entries returned to only those of the specified action type.
The optional `mod` parameter can be a comma-delimited list of moderator names to restrict the results to,
or the string `a` to restrict the results to admin actions taken within the subreddit.

.. csv-table:: Mod action object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Mod action ID. E.g., `ModAction_727b75b0-2214-11ec-99b4-05a9ad5c4e6c`."
   "action","string","The mod action name."
   "mod","string","The name of the moderator who initiated the action."
   "mod_id36","string","The full ID36 of the moderator who initiated the action."
   "created_utc","float","Unix timestamp of when the action was done. Always a whole number."
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
   :escape: \

   "...","...","Common listing parameters. See :ref:`Listings overview <listings_overview>`.

   The `limit` can be up to 500. (Numbers outside the range of 1-500 will be clamped within range.)"
   "type","string","The action type to filter on."
   "mod","string","A comma separated list of moderator names to filter on. The special name '`a`'
   filters on admin actions."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

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

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","There is no user context."
   "NO_USER","The `name` parameter was not specified or was empty.

   *\"please enter a username\"* -> name"
   "USER_DOESNT_EXIST","The user specified by `name` does not exist.

   *\"that user doesn't exist\"* -> name"
   "INVALID_PERMISSIONS","The string specified by the `permissions` parameter is invalid.

   *\"invalid permissions string\"* -> permissions"
   "ALREADY_MODERATOR","*\"That user is already a moderator\"* -> name"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You don't have access to the subreddit you are sending an invite for."


Accept moderator invite
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: [/r/{subreddit}]/api/accept_moderator_invite

*scope: modothers*

Accept an invitation to moderate a subreddit.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","There is no user context."
   "NO_INVITE_FOUND","You don't have an invitation for the subreddit.

   *\"there is no pending invite for that subreddit.\"*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator_invite`"
   "name","string","Name of a target user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","There is no user context."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

   "id","string","The full ID36 of a subreddit (prefixed with `t5_`)."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

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
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator`"
   "name","string","Name of a target user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","There is no user context."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","`moderator`: change permissions of a moderator.

   `moderator_invite`: change permissions of a moderator invite."
   "name","string","Name of a target user."
   "permissions","string","A permission description. See `POST /api/friend`.

   Default: `+all`."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","There is no user context."
   "USER_DOESNT_EXIST","The user specified by `name` does not exist.

   *\"that user doesn't exist\"* -> name"
   "INVALID_PERMISSION_TYPE","The user specified by `name` isn't a moderator (if `type: moderator`)
   or mod invitee (if `type: moderator_invite`).

   *\"permissions don't apply to that type of user\"* -> type"
   "NO_USER","The `name` parameter was not specified or was empty.

   *\"please enter a username\"* -> name"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

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
   This ban message shows in the PM under a section called "Note from the moderators:".

   Default: empty string."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."
   "BAD_NUMBER","The number specified for `duration` is not in the range 1 to 999.

   *\"that number isn't in the right range (1 to 999)\"* -> duration"
   "TOO_LONG","* The value specified by `ban_reason` is over 100 characters.

   * The value specified by `note` is over 300 characters.

   *\"This field must be under 100 characters\"* -> ban_reason"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","The `id` or `name` parameter was not specified."
   "403","* The non subreddit form of the URL was used and `r` was not specified or was empty.

   * You don't have access to the subreddit you are operating on."
   "404","The subreddit specified by `r` does not exist. A 'page not found' HTML document is also returned."
   "500","* The `name` parameter was not specified, was empty, or the name contains invalid characters.

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
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "type","string","Either: `banned`, `muted`, `contributor`, `wikibanned`, `wikicontributor`."
   "id","string","The full ID36 of a target user (prefixed with `t2_`)."
   "name","string","Name of a target user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

   "id","string","The full ID36 of a subreddit (prefixed with `t5_`)."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

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
   :escape: \

   "id","string","The full ID36 of a post or comment (prefixed with `t3_` or `t1_`)."
   "reason","string","The report reason text to snooze on."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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
   :escape: \

   "title","string","A title for this removal reason."
   "message","string","The removal reason message."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "MOD_REQUIRED","* The current user is not a moderator of the target subreddit.

   * There is no user context.

   *\"You must be a moderator to do that.\"*"
   "NO_TEXT","* The `title` parameter was not specified or was empty.

   * The `message` parameter was not specified or was empty.

   *\"we need something here\"* -> title"
   "TOO_LONG","* The value specified for `title` is over 50 characters.

   * The value specified for `message` is over 10000 characters.

   *\"This field must be under 50 characters\"* -> title"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

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

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "SUBREDDIT_NOEXIST","The target subreddit does not exist.

   *\"Hmm, that community doesn't exist. Try checking the spelling.\"*"
   "MOD_REQUIRED","* The current user is not a moderator of the target subreddit.

   * There is no user context.

   *\"You must be a moderator to do that.\"*"
   "NO_TEXT","* The `title` parameter was not specified or was empty.

   * The `message` parameter was not specified or was empty.

   *\"we need something here\"* -> title"


Update removal reason
~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /api/v1/{subreddit}/removal_reasons/{reason_id}

*scope: (unknown)*

Update a removal reason's title and message.

Both parameters title and message must be specified otherwise a `NO_TEXT` API error is returned.

Returns zero bytes on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "title","string","A title for this removal reason."
   "message","string","The removal reason message."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "SUBREDDIT_NOEXIST","The target subreddit does not exist.

   *\"Hmm, that community doesn't exist. Try checking the spelling.\"* -> subreddit"
   "MOD_REQUIRED","* The current user is not a moderator of the target subreddit.

   * There is no user context.

   *\"You must be a moderator to do that.\"*"
   "NO_TEXT","* The `title` parameter was not specified or was empty.

   * The `message` parameter was not specified or was empty.

   *\"we need something here\"* -> title"
   "INVALID_ID","* The specified removal reason ID was not found.

   * The specified removal reason ID contained invalid characters (e.g., it contained uppercase letters).

   *\"The specified id is invalid\"* -> reason_id"
   "TOO_LONG","* The value specified for `title` is over 50 characters.

   * The value specified for `message` is over 10000 characters.

   *\"This field must be under 50 characters\"* -> title"


Delete removal reason
~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /api/v1/{subreddit}/removal_reasons/{reason_id}

*scope: (unknown)*

Delete a removal reason.

Returns zero bytes on success. If the specified ID did not exist it is treated as a success.

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "SUBREDDIT_NOEXIST","The target subreddit does not exist.

   *\"Hmm, that community doesn't exist. Try checking the spelling.\"* -> subreddit"
   "MOD_REQUIRED","* The current user is not a moderator of the target subreddit.

   * There is no user context.

   *\"You must be a moderator to do that.\"*"
   "INVALID_ID","* The specified removal reason ID contained invalid characters (e.g., it contained uppercase letters).

   *\"The specified id is invalid\"* -> reason_id"
