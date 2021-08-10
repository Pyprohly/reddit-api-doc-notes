
My Account
==========

Overview
--------

Schema
~~~~~~

When the client has a user context then,
in addition to the attributes listed in the table :ref:`here <my_user_schema>`:

.. csv-table:: Account Object
   :header: "Field","Type (hint)","Description"
   :escape: \

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
   :escape: \

   "features","object","Note, this object has some keys that differ from the one described in the table :ref:`here <user_features>`."


Actions
-------

Get identity
~~~~~~~~~~~~

.. http:get:: /api/v1/me

*scope: identity*

Get information about the authenticated user.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me


Get preferences
~~~~~~~~~~~~~~~

.. http:get:: /api/v1/me/prefs

*scope: identity*

Retrieve the preference settings of the logged in user.

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_prefs


Set preferences
~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/me/prefs

*scope: account*

Set preference settings for the logged in user.

This endpoint expects JSON data.

Returns the updated preferences, as you would get from `GET /api/v1/me/prefs`.

For boolean values, a string that starts with `0` or `F` or `f` is treated as falsy.

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "JSON_PARSE_ERROR","The JSON provided was invalid."

.. seealso:: https://www.reddit.com/dev/api/#PATCH_api_v1_me_prefs


Get karma breakdown
~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/me/karma

*scope: mysubreddits*

Return a breakdown of subreddit karma.

.. csv-table:: Karma Breakdown Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr","string","Subreddit name."
   "comment_karma","integer","Karma accumulated from commenting."
   "link_karma","integer","Karama accumulated from posting."

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_karma


.. _account_list_trophies:

List trophies
~~~~~~~~~~~~~

.. http:get:: /api/v1/me/trophies

*scope: identity*

Return a list of trophies for the current user.

Returns a 'TrophyList' listing structure.

.. csv-table:: Trophy Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "award_id","string?",""
   "description","string?",""
   "granted_at","integer?",""
   "icon_40","string","The URL of a 41x41 px icon for the trophy. E.g., `https://www.redditstatic.com/awards2/3_year_club-40.png`"
   "icon_70","string","The URL of a 71x71 px icon for the trophy. E.g., `https://www.redditstatic.com/awards2/3_year_club-70.png`"
   "id","string","Trophie ID36."
   "name","string","E.g., `Three-Year Club`"
   "url","string?",""

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

See also `/api/v1/user/{username}/trophies`.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_trophies


Get friend
~~~~~~~~~~

.. http:get:: /api/v1/me/friends/{username}

*scope: mysubreddits*

Get information about a specific 'friend', such as notes.

Replace `{username}` with the (case-insensitive) name of a user.

Returns an object with the following fields:

.. _user_item_object_table:

.. csv-table:: User Item Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "date","float","Unix timestamp of when this item was added to the list. Will always be a whole number."
   "rel_id","string","Some unknown string. E.g., `r9_1w4acm`"
   "name","string","The name of the user."
   "id","string","The full ID of the user. E.g., `t2_4x25quk`"

|

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","This is documented but it doesn't seem to do anything."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "NOT_FRIEND","\"you are not friends with that user -> id\""
   "USER_DOESNT_EXIST","\"that user doesn't exist -> id\""

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_v1_me_friends_{username}>`_


List friends
~~~~~~~~~~~~

See :ref:`Friends Account listing <account_listings_friends>`.


Add friend
~~~~~~~~~~

.. http:put:: /api/v1/me/friends/{username}

*scope: subscribe*

Create or update a "friend" relationship.

This endpoint can add/change a note on a friend.
Making a note requires Reddit Premium.

Returns the user object on success. See the table :ref:`here <user_item_object_table>`.

Adding a friend who is already a friend does nothing but get the user item object
(i.e., without updating the 'date' field).

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","A username. This field isn't required.
   If specified this must match the name in the URL placeholder or
   a BAD_USERNAME error will be returned."
   "note","string","A string no longer than 300 characters. Reddit Premium is required."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "JSON_PARSE_ERROR","JSON data was not provided.

   \"unable to parse JSON data -> json\""
   "USER_DOESNT_EXIST","\"that user doesn't exist -> id\""
   "BAD_USERNAME","The `{username}` in the path placeholder and the
   `name` field in the JSON data did not match.

   \"invalid user name -> name\""
   "GOLD_REQUIRED","You tried to add a note but don't have Reddit Premium.

   \"you must have an active reddit gold subscription to do that -> note\""
   "NO_TEXT","An empty string was specified for 'note'."

.. seealso:: `<https://www.reddit.com/dev/api/#PUT_api_v1_me_friends_{username}>`_


Remove friend
~~~~~~~~~~~~~

.. http:delete:: /api/v1/me/friends/{username}

*scope: subscribe*

Stop being friends with a user.

Returns zero data on success.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","This is documented but it doesn't seem to do anything."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "NOT_FRIEND","That user is not a friend."

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_v1_me_friends_{username}>`_


List blocked
~~~~~~~~~~~~

See :ref:`Blocked Account listing <account_listings_blocked>`.


.. _account_block_user:

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
   :escape: \

   "account_id","string","Full ID36 (prefixed with `t2_`) of a user."
   "name","string","A case-insensitive user name."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* `account_id` nor `name` was specified.

   * You tried to block yourself.

   * The user or account ID doesn't exist."

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
   :escape: \

   "type","string","`enemy`"
   "container","string","The current user's full ID36."
   "id","string","Full ID36 of the target."
   "name","string","Name of a target user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The `id` or `name` parameter was not specified.

   * The the user specified by `id` or `name` doesn't exist."
   "500","An invalid value was specified for `type`."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_unfriend


Add trusted user
~~~~~~~~~~~~~~~~

.. http:post:: /api/add_whitelisted

Add a user to your trusted users list.

Trusted users will always be able to send you PMs.

On success, the endpoint returns `{'json': {'errors': []}}`.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","The name of the user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login

   \"Please log in to do that.\""
   "CANT_WHITELIST_AN_ENEMY","\"You can't add a blocked user as a trusted user.\""
   "USER_DOESNT_EXIST","The specified user in `name` does not exist or the `name` field was not specified.

   \"that user doesn't exist\""


Remove trusted user
~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/remove_whitelisted

Remove a user from your trusted users list.

On success, the endpoint returns `"{}"` (a string of an empty JSON object).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "name","string","The name of the user."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","HTTP status","Description"
   :escape: \

   "USER_REQUIRED","200","you must login

   \"Please log in to do that.\""


Get saved categories
~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/saved_categories

Get saved categories.

Requires Reddit Premium.

Saved categories are automatically removed when the last item using it is removed for the saved list.

Example output::

   {'categories': [{'category': 'asdf'}, {'category': 'zxcv'}]}

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The current user does not have Reddit Premium."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_saved_categories
