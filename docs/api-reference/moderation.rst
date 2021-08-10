
Moderation
==========

Actions
-------

Pull subreddit users
~~~~~~~~~~~~~~~~~~~~
/api/v1/{subreddit}/banned

.. http:get:: [/r/{subreddit}]/about/banned
.. http:get:: [/r/{subreddit}]/about/muted
.. http:get:: [/r/{subreddit}]/about/contributors
.. http:get:: [/r/{subreddit}]/about/wikibanned
.. http:get:: [/r/{subreddit}]/about/wikicontributors

*scope: read*

This endpoint is a listing. See :ref:`Listings overview <listings_overview>`.

Get redditors that relate to a subreddit.

If the `user` parameter is specified, the listing will contain at most one entry,
the user specified. If the user doesn't exist in the regular listing, an empty listing is returned.

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

   For `muted`, the mod note."

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "user","string","A username."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You don't have access to the subreddit you are revoking an invite for."
   "404","The specified subreddit does not exist, contains invalid characters, is too long. A 'page not found' HTML document may also be returned."


Get subreddit moderators
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/about/moderators

*scope: read*

Get a list of subreddit moderators.

If the `user` parameter is specified, the list will contain at most one entry,
the user specified. If the user doesn't exist in the regular list, an empty list is returned.

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "r","string","The target subreddit. An alternative to specifying the subreddit name in the URL."
   "user","string","A username."


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
