
My Account
==========

Overview
--------

Schema
~~~~~~

When the client has a user context then,
in addition to the attributes listed in the table :ref:`here <my-user-schema>`:

.. csv-table:: Account Object
   :header: "Field","Type (hint)","Description"

   "seen_layout_switch","boolean",""
   "seen_redesign_modal","boolean",""
   "oauth_client_id","string","Your client ID."
   "seen_give_award_tooltip","boolean",""
   "seen_premium_adblock_modal","boolean",""
   "linked_identities","unknown array",""
   "seen_subreddit_chat_ftux","boolean",""


When the client is not in a user context:

.. csv-table:: Account Object
   :header: "Field","Type (hint)","Description"

   "features","object","Note, this object has some keys that differ from the one described in the table :ref:`here <user-features>`."


Actions
-------

Get identity
~~~~~~~~~~~~

.. http:get:: /api/v1/me

*scope: identity*

Get information about the authenticated user.

If there is no current user, this endpoint still returns the `features` key.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me


Get preferences
~~~~~~~~~~~~~~~

.. http:get:: /api/v1/me/prefs

*scope: identity*

Retrieve the preference settings of the logged in user.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_prefs


Set preferences
~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/me/prefs

*scope: account*

Set preference settings for the logged in user.

This endpoint expects JSON data.

Returns the updated preferences, as you would get from `GET /api/v1/me/prefs`.

For boolean values, a string that starts with `0` or `F` or `f` is treated as falsy.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "JSON_PARSE_ERROR","400","The provided JSON was invalid.","
   ``{""fields"": [""json""], ""explanation"": ""Sorry, something went wrong. Double-check things and try again."", ""message"": ""Bad Request"", ""reason"": ""JSON_PARSE_ERROR""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#PATCH_api_v1_me_prefs


Get karma breakdown
~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/me/karma

*scope: mysubreddits*

Return the current user's karma breakdown by subreddit.

The entries are sorted in descending order by comment karma plus
submission karma.

.. csv-table:: Karma Breakdown Object
   :header: "Field","Type (hint)","Description"

   "sr","string","Subreddit name."
   "comment_karma","integer","Karma accumulated from commenting."
   "link_karma","integer","Karama accumulated from posting."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_karma


.. _account-list-trophies:

List trophies
~~~~~~~~~~~~~

.. http:get:: /api/v1/me/trophies

*scope: identity*

Return a list of trophies for the current user.

Returns a 'TrophyList' listing structure.

.. csv-table:: Trophy Object
   :header: "Field","Type (hint)","Description"

   "id","string?","An ID36. Not all trophies have a value (`null`)."
   "description","string?","Trophy description. `null` if no description."
   "icon_40","string","The URL of a 41x41 px icon for the trophy. E.g., `https://www.redditstatic.com/awards2/3_year_club-40.png`."
   "icon_70","string","The URL of a 71x71 px icon for the trophy. E.g., `https://www.redditstatic.com/awards2/3_year_club-70.png`."
   "award_id","string?","Different from the `id` field. An ID36 with an unknown purpose. Not all trophies have a value (`null`)."
   "name","string","E.g., `Three-Year Club`."
   "granted_at","integer?","Maybe the UNIX timestamp of when the trophy was given? Not all trophies have a value (`null`)."
   "url","unknown?",""

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "

See also :ref:`GET /api/v1/user/{username}/trophies <user-list-trophies>`.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_trophies


Get friend
~~~~~~~~~~

.. http:get:: /api/v1/me/friends/{username}

*scope: mysubreddits*

Get information about a specific 'friend', such as notes.

Replace `{username}` with the (case-insensitive) name of a user.

Returns an object with the following fields:

.. _user-item-object-table:

.. csv-table:: User Item Object
   :header: "Field","Type (hint)","Description"

   "date","float","Unix timestamp of when this item was added to the list. Will always be a whole number."
   "rel_id","string","Some unknown string. E.g., `r9_1w4acm`"
   "name","string","The name of the user."
   "id","string","The full ID of the user. E.g., `t2_4x25quk`"

|

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","This is documented but it doesn't seem to do anything."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "NOT_FRIEND","400","You are not friends with the specified user.","
   ``{""fields"": [""id""], ""explanation"": ""you are not friends with that user"", ""message"": ""Bad Request"", ""reason"": ""NOT_FRIEND""}``
   "
   "USER_DOESNT_EXIST","400","The specified user does not exist.","
   ``{""fields"": [""id""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_v1_me_friends_{username}>`_


List friends
~~~~~~~~~~~~

See :ref:`Friends Account listing <account-listings-friends>`.


Add friend
~~~~~~~~~~

.. http:put:: /api/v1/me/friends/{username}

*scope: subscribe*

Create or update a friend relationship.

This endpoint can add/change a note on a friend.
Making a note requires Reddit Premium.

Returns the updated user object on success. See the table :ref:`here <user-item-object-table>`.

Adding a friend who is already a friend does nothing but get the user item object
(i.e., without updating the 'date' field).

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"

   "name","string","A username. This field isn't required but if specified this must match the name in the URL
   otherwise a `BAD_USERNAME` API error will be raised."
   "note","string","A string no longer than 300 characters. Reddit Premium is required."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "JSON_PARSE_ERROR","400","JSON data was not provided.","
   ``{""fields"": [""json""], ""explanation"": ""Sorry, something went wrong. Double-check things and try again."", ""message"": ""Bad Request"", ""reason"": ""JSON_PARSE_ERROR""}``
   "
   "USER_DOESNT_EXIST","400","The specified user does not exist.","
   ``{""fields"": [""id""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "
   "BAD_USERNAME","400","The `{username}` in the URL and the `name` field in the JSON data provided did not match.","
   ``{""fields"": [""name""], ""explanation"": ""invalid user name"", ""message"": ""Bad Request"", ""reason"": ""BAD_USERNAME""}``
   "
   "GOLD_REQUIRED","400","You tried to add a note but you don't have Reddit Premium.","
   ``{""fields"": [""note""], ""explanation"": ""you must have an active reddit gold subscription to do that"", ""message"": ""Bad Request"", ""reason"": ""GOLD_REQUIRED""}``
   "
   "NO_TEXT","400","An empty string was specified for the `note`.","
   ``{""fields"": [""note""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#PUT_api_v1_me_friends_{username}>`_


Remove friend
~~~~~~~~~~~~~

.. http:delete:: /api/v1/me/friends/{username}

*scope: subscribe*

Stop being friends with a user.

Returns zero data on success.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "id","string","This is documented but it doesn't seem to do anything."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "NOT_FRIEND","400","The user specified is not a friend.","
   ``{""fields"": [""id""], ""explanation"": ""you are not friends with that user"", ""message"": ""Bad Request"", ""reason"": ""NOT_FRIEND""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_v1_me_friends_{username}>`_


List blocked
~~~~~~~~~~~~

See :ref:`Blocked Account listing <account-listings-blocked>`.


.. _account-block-user:

Block user
~~~~~~~~~~

.. http:post:: /api/block_user

*scope: account*

Block a user.

Specify an account full ID36 (with `account_id`) or user name (with `name`) to block.
If both parameters are specified together then `account_id` will be used.

An object like the following is returned on success::

   {
      "date": 1627236824.0,
      "icon_img": "https://www.redditstatic.com/avatars/avatar_default_10_7E53C1.png",
      "id": "t2_ojpl",
      "name": "speed"
   }

If the user is already blocked then an empty JSON object is returned on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "account_id","string","Full ID36 (prefixed with `t2_`) of a user."
   "name","string","A case-insensitive user name."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "400","* `account_id` nor `name` was specified.

   * The username or user ID given doesn't exist.

   * You tried to block yourself.","
   ``{""message"": ""Bad Request"", ""error"": 400}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_block_user


Unblock user
~~~~~~~~~~~~

.. http:post:: /api/unfriend

*scope: privatemessages*

Unblock a user.

The user can either be passed in by name (`name`) or by full ID36 (`id`). If both `id` and `name` are
specified, `id` will take preference and `name` is ignored.

The `container` parameter must be specified and should be the current user's full ID36.

Returns an empty JSON object on success.
If the target specified by `id` or `name` isn't blocked, it is treated as a success.
If `container` is not specified, or is specified incorrectly, no action is performed, and it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "type","string","`enemy`"
   "container","string","The current user's full ID36."
   "id","string","Full ID36 of the target."
   "name","string","Name of a target user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "400","* The `id` or `name` parameter was not specified.

   * The the user specified by `id` or `name` doesn't exist.","
   ``{""message"": ""Bad Request"", ""error"": 400}``
   "
   "500","The `type` parameter was not specified or was an invalid value.","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_unfriend


Add trusted user
~~~~~~~~~~~~~~~~

.. http:post:: /api/add_whitelisted

Add a user to your trusted users list.

Trusted users will always be able to send you PMs.

On success, the endpoint returns ``{"json": {"errors": []}}``.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "name","string","The name of the user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "CANT_WHITELIST_AN_ENEMY","200","The specified user is on your blocked list.","
   ``{""json"": {""errors"": [[""CANT_WHITELIST_AN_ENEMY"", ""You can't add a blocked user as a trusted user."", ""name""]]}}``
   "
   "USER_DOESNT_EXIST","200","The specified user in `name` does not exist or the `name` field was not specified.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""name""]]}}``
   "


Remove trusted user
~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/remove_whitelisted

Remove a user from your trusted users list.

On success, the endpoint returns `"{}"` (a string of an empty JSON object).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "name","string","The name of the user."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "


Get saved categories
~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/saved_categories

Get saved categories.

Requires Reddit Premium.

Saved categories are automatically removed when the last item using it is removed for the saved list.

Example output::

   {"categories": [{"category": "asdf"}, {"category": "zxcv"}]}

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","The current user does not have Reddit Premium.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_saved_categories
