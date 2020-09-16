
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

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_prefs


Set preferences
~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/me/prefs

*scope: account*

Set preference settings for the logged in user.

Returns the updated preferences.

For boolean values, a string that starts with `0` or `F` or `f` is treated as falsy.

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "BAD_NUMBER","E.g., when setting the `numsites` preference to a non-number or outside the valid range (1 to 100)."

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#PATCH_api_v1_me_prefs


Get karma breakdown
~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/me/karma

*scope: mysubreddits*

Return a breakdown of subreddit karma.

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
   "granted_at","integer",""
   "icon_40","string","E.g., `https://www.redditstatic.com/awards2/3_year_club-40.png`"
   "icon_70","string","E.g., `https://www.redditstatic.com/awards2/3_year_club-70.png`"
   "id","string","Trophie ID."
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

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_friends_{username}

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

.. seealso:: https://www.reddit.com/dev/api/#PUT_api_v1_me_friends_{username}


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

.. seealso:: https://www.reddit.com/dev/api/#DELETE_api_v1_me_friends_{username}
