
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


List trophies
~~~~~~~~~~~~~

.. http:get:: /api/v1/me/trophies

*scope: identity*

Return a list of trophies for the current user.

.. csv-table:: Trophy Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "award_id","string?",""
   "description","string?",""
   "granted_at","integer",""
   "icon_40","string","E.g., `https://www.redditstatic.com/awards2/3_year_club-40.png`"
   "icon_70","string","E.g., `https://www.redditstatic.com/awards2/3_year_club-70.png`"
   "id","",""
   "name","string","E.g., `Three-Year Club`"
   "url","string?",""

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_v1_me_trophies
