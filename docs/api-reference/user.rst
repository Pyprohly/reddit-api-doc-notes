
User
====

Overview
--------

.. _user-schema:

Schema
~~~~~~

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"

   "id","string","The ID of the user (without the `t2_` prefix)."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "link_karma","integer","Karma accumulated from posting."
   "comment_karma","integer","Karma accumulated from commenting."
   "awardee_karma","integer","Karma accumulated for being awarded."
   "awarder_karma","integer","Karma accumulated for giving awards."
   "total_karma","integer","Same as `link_karma`, `comment_karma`, `awardee_karma`, and `awarder_karma` added."
   "is_gold","boolean","Has Reddit Premium."
   "has_subscribed","boolean","Whether the user has ever subscribed to any subreddits.

   When a user makes their first subreddit subscription, they are automatically subscribed to a list a default
   subreddits. This field is used to determine when this occurs."
   "has_verified_email","boolean","Whether the user has verified their email."
   "hide_from_robots","boolean",""
   "icon_img","string","Avatar image. E.g., `https://www.redditstatic.com/avatars/avatar_default_01_A5A4A4.png`."
   "is_employee","boolean","Is a Reddit admin."
   "is_friend","boolean","Whether the user is a friend of the current user. If there is no user context, always false."
   "is_mod","boolean","Is a moderator of any subreddit."
   "is_blocked","boolean","True if the current account has blocked this user. If there is no user context, always false."
   "is_suspended","?boolean","This field only exists if the user is suspended (in which case it will be true),
   or if the user matches the current user context (in which case it will likely be false).

   When a user is suspended, only a small number of fields are returned. See :ref:`Get by name <user-get-by-name>`."
   "name","string","The user account name. E.g., `""spez""`"
   "verified","boolean",""
   "subreddit","object","See :ref:`Subreddit sub-object <user-subreddit>`."
   "pref_show_snoovatar","boolean",""

.. _my-user-schema:

Additional fields for when the client has a user context and the user object matches that user.

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"

   "can_create_subreddit","boolean",""
   "can_edit_name","boolean",""
   "coins","integer","The number of coins you have."
   "features","object","See :ref:`here <user-features>`."
   "force_password_reset","boolean",""
   "gold_creddits","integer",""
   "gold_expiration","unknown?",""
   "has_android_subscription","boolean",""
   "has_external_account","boolean",""
   "has_gold_subscription","boolean",""
   "has_ios_subscription","boolean",""
   "has_mail","boolean",""
   "has_mod_mail","boolean",""
   "has_paypal_subscription","boolean",""
   "has_stripe_subscription","boolean",""
   "has_subscribed_to_premium","boolean",""
   "has_visited_new_profile","boolean",""
   "in_beta","boolean",""
   "in_chat","boolean",""
   "in_redesign_beta","boolean",""
   "inbox_count","integer",""
   "is_sponsor","boolean",""
   "is_suspended","boolean","True if the user is suspended."
   "new_modmail_exists","boolean",""
   "num_friends","integer","Number of friends in your friends list. See https://www.reddit.com/prefs/friends/."
   "over_18","boolean","Preference option ""I am over eighteen years old and willing to view adult content"" is checked."
   "password_set","boolean",""
   "pref_autoplay","boolean",""
   "pref_clickgadget","integer",""
   "pref_geopopular","string",""
   "pref_nightmode","boolean",""
   "pref_no_profanity","boolean",""
   "pref_show_trending","boolean",""
   "pref_show_twitter","boolean",""
   "pref_top_karma_subreddits","boolean",""
   "pref_video_autoplay","boolean",""
   "suspension_expiration_utc","unknown?",""


Additional fields for when the client has a user context and the object does not match that user.

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"

   "accept_chats","boolean","Whether the user is accepting chat messages."
   "accept_pms","boolean","Whether the user is accepting private messages."


.. _user-features:

Features sub-object
~~~~~~~~~~~~~~~~~~~

.. csv-table:: User.features Object
   :header: "Field","Type (hint)","Description"

   "awards_on_streams","boolean",""
   "chat","boolean",""
   "chat_group_rollout","boolean",""
   "chat_subreddit","boolean",""
   "chat_user_settings","boolean",""
   "do_not_track","boolean",""
   "econ_wallet_service","boolean",""
   "expensive_coins_package","boolean",""
   "is_email_permission_required","boolean",""
   "mod_awards","boolean",""
   "mod_service_mute_reads","boolean",""
   "mod_service_mute_writes","boolean",""
   "modlog_copyright_removal","boolean",""
   "mweb_nsfw_xpromo","object",""
   "mweb_xpromo_interstitial_comments_android","boolean",""
   "mweb_xpromo_interstitial_comments_ios","boolean",""
   "mweb_xpromo_modal_listing_click_daily_dismissible_android","boolean",""
   "mweb_xpromo_modal_listing_click_daily_dismissible_ios","boolean",""
   "mweb_xpromo_revamp_v3","object",""
   "noreferrer_to_noopener","boolean"
   "premium_subscriptions_table","boolean"
   "promoted_trend_blanks","boolean"
   "report_service_handles_report_writes_to_db_for_awards","boolean"
   "report_service_handles_report_writes_to_db_for_helpdesk_reports","boolean"
   "report_service_handles_report_writes_to_db_for_som","boolean"
   "report_service_handles_report_writes_to_db_for_spam","boolean"
   "report_service_handles_self_harm_reports","boolean"
   "reports_double_write_to_report_service","boolean"
   "reports_double_write_to_report_service_for_awards","boolean"
   "reports_double_write_to_report_service_for_helpdesk_reports","boolean"
   "reports_double_write_to_report_service_for_modmail_reports","boolean"
   "reports_double_write_to_report_service_for_sendbird_chats","boolean"
   "reports_double_write_to_report_service_for_som","boolean"
   "reports_double_write_to_report_service_for_spam","boolean"
   "reports_double_write_to_report_service_for_users","boolean"
   "resized_styles_images","boolean"
   "show_amp_link","boolean"
   "spez_modal","boolean"


.. _user-subreddit:

Subreddit sub-object
~~~~~~~~~~~~~~~~~~~~

.. csv-table:: User.features Object
   :header: "Field","Type (hint)","Description"

   "banner_img","string",""
   "banner_size","unknown?",""
   "coins","integer",""
   "community_icon","unknown?",""
   "default_set","boolean",""
   "description","string",""
   "disable_contributor_requests","boolean",""
   "display_name","string","The name of the subreddit. This will be your user account name prepended with `u_`. E.g., `u_Pyprohly`.",""
   "display_name_prefixed","string","Your user account name prepended with `u/`. E.g., `u/Pyprohly`.",""
   "free_form_reports","boolean",""
   "header_img","unknown?",""
   "header_size","unknown?",""
   "icon_color","string","E.g., `#A5A4A4`."
   "icon_img","string","Avatar image. E.g., `https://www.redditstatic.com/avatars/avatar_default_01_A5A4A4.png`."
   "icon_size","integer array","Array of two integers."
   "is_default_banner","boolean",""
   "is_default_icon","boolean",""
   "key_color","string",""
   "link_flair_enabled","boolean",""
   "link_flair_position","string",""
   "name","string","The comment's full ID (with prefix `t5_`)."
   "over_18","boolean",""
   "previous_names","unknown array",""
   "primary_color","string",""
   "public_description","string",""
   "restrict_commenting","boolean",""
   "restrict_posting","boolean",""
   "show_media","boolean",""
   "submit_link_label","string",""
   "submit_text_label","string",""
   "submit_text_label","string",""
   "subreddit_type","string","The string `""user""`."
   "subscribers","integer",""
   "title","string",""
   "url","string","E.g., `""/user/Pyprohly/""`"
   "user_is_banned","boolean",""
   "user_is_contributor","boolean",""
   "user_is_moderator","boolean",""
   "user_is_muted","boolean",""
   "user_is_subscriber","boolean",""


Actions
-------

.. _user-get-by-name:

Get by name
~~~~~~~~~~~

.. http:get:: /user/{username}/about

*scope: read*

Get information about a user by account name.

`{username}` is case-insensitive.

If the target user is suspended, only these fields are returned:

* name (string): The user account's name.
* is_suspended (boolean): true.
* is_blocked (boolean): Same as on the user object schema.
* awardee_karma (integer): Same as on the user object schema.
* awarder_karma (integer): Same as on the user object schema.
* total_karma (integer): Same as on the user object schema.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","A user with the specified name was not found."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_user_{username}_about>`_


Get user summary by ID
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/user_data_by_account_ids

*scope: privatemessages*

Bulk get partial user objects by (full) IDs.

This endpoint returns a JSON object that maps user full IDs to partial user objects.

Specify the IDs with the `ids` parameter.
IDs must be prefixed with `t2_`.
Any ID that can't be resolved will be ignored.
Alphabetic characters in IDs must be all lowercase or they will be ignored.
Duplicate IDs will be ignored.

This endpoint will process as many IDs as it can so long as the total URL length is
less than about 6544 characters.
This means you can request up to a little over 450 IDs at a time assuming each ID
string is the largest observed length for a user ID at this time of this writing
(8 characters excluding `t2_`).

It is recommended that clients request in batches of up to 300 IDs at a time.

This end point returns an object with the following fields:

.. csv-table:: Partial user objects
   :header: "Field","Type (hint)","Description"

   "comment_karma","integer","Karma accumulated from commenting."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "link_karma","integer","Karma accumulated from posting."
   "name","string","The user account name. E.g., `spez`"
   "profile_color","string",""
   "profile_img","string","Avatar image. Same value as the `icon_img` field in normal user objects.
   E.g., `https://www.redditstatic.com/avatars/avatar_default_01_A5A4A4.png`."
   "profile_over_18","boolean",""

|

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "ids","string","A comma separated list of user full IDs (each being prefixed by `t2_`)."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","The requested URL length is too long (over 6544 characters)."
   "404","None of the IDs matched any user."
   "414","The requested URL length is way too long (over 8216 characters)."


.. _user-listings:

Pull user listings
~~~~~~~~~~~~~~~~~~

* *Overview*:

.. http:get:: /user/{username}
.. http:get:: /user/{username}/overview

A listing of submissions and comments.

Available publicly for any user.

* *Submitted*:

.. http:get:: /user/{username}/submitted

A listing of submissions.

Available publicly for any user.

* *Comments*:

.. http:get:: /user/{username}/comments

A listing of comments.

Available publicly for any user.

This does not support the `sr_detail` parameter.

Comment objects have extra fields. See :ref:`here <frontpage-new-comments-comment-object>`.

* *Gilded*:

.. http:get:: /user/{username}/gilded

A listing of submissions and comments.

Available publicly for any user.

* *Gildings given*:

.. http:get:: /user/{username}/gilded/given

A listing of submissions and comments.

* *Upvoted*:

.. http:get:: /user/{username}/upvoted

A listing of submissions.

Only available publicly for a given user if their 'make my votes public' privacy option is checked.

* *Downvoted*:

.. http:get:: /user/{username}/downvoted

A listing of submissions.

Only available publicly for a given user if their 'make my votes public' privacy option is checked.

* *Hidden*:

.. http:get:: /user/{username}/hidden

A listing of submissions.

Not available publicly for any user.

* *Saved*:

.. http:get:: /user/{username}/saved

A listing of submissions and comments.

Not available publicly for any user.

|
|

*scope: history*

User listings.

See :ref:`Additional URL Params <frontpage-listings-additional-url-params>`.

Additional URL params for *Overview*, *Submitted*, and *Comments*:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "sort","string","One of: `hot`, `new`, `top`, `controversial`.

   For *Overview* and *Comments* listings, `new` is the default.
   For *Submitted*, `hot` is the default."

Additional URL params for *Saved*:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "type","string","Filter for either `links` or `comments`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The user name was not found."
   "403","You don't have permission to view this listing."


Report
~~~~~~

.. http:post:: /api/report_user

*scope: report*

Report a user. Reporting a user brings it to the attention of a Reddit admin.

[WIP]

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "user","string","A valid, existing reddit username"
   "details","string","JSON data"
   "reason","string","a string no longer than 100 characters"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_report_user


.. _user-list-trophies:

List trophies
~~~~~~~~~~~~~

.. http:get:: /api/v1/user/{username}/trophies

*scope: read*

Get a list of trophies for a user.

Returns a 'TrophyList' structure.

For a description of the Trophy object schema, see :ref:`here <account-list-trophies>`.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_DOESNT_EXIST","400","The user name specified by `user` does not exist.","
   ``{""fields"": [""id""], ""explanation"": ""that user doesn't exist"", ""message"": ""Bad Request"", ""reason"": ""USER_DOESNT_EXIST""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_v1_user_{username}_trophies>`_


.. _user-search-users:

Search users
~~~~~~~~~~~~

.. http:get:: /users/search

*scope: read*

Search users by name or description.

This endpoint returns a :ref:`paginated listing <listings-overview>`.

The listing contains user objects but they are missing the `awardee_karma`, `awarder_karma`, `total_karma` fields.

If the parameter `q` is not specified, this endpoint returns `"{}"`
(i.e., a string of an empty JSON object).

The `sr_detail` parameter is not supported (despite the offical docs saying so).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "...",":ref:`Listing common parameters <listings-overview>`."
   "q","string","A search query. Matches user name beginnings or descriptions."
   "(sort)","string","Documented parameter but doesn't seem to do anything.

   Either `relevance` or `activity`."


Check user exists
~~~~~~~~~~~~~~~~~

.. http:get:: /api/username_available

*scope: (any)*

Check whether a user name exists.

Valid usernames match `/[A-Za-z0-9_-]{3,20}/`.

Returns `true` or `false`.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "user","string","A username."

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "BAD_USERNAME","200","* The `user` param was not specified or is empty.

   * The username specified contains illegal characters.","
   ``{""json"": {""errors"": [[""BAD_USERNAME"", ""invalid user name"", ""user""]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#GET_api_username_available


List moderated subreddits
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /user/{user}/moderated_subreddits

*scope: (unknown)*

Get a list of partial subreddit objects that the target user is a moderator of.

This endpoint isnt very reliable on users with big lists.

Example output::

   {'kind': 'ModeratedList',
    'data': [{'banner_img': '',
              'community_icon': '',
              'display_name': 'RedditWarp',
              'title': 'RedditWarp',
              'over_18': False,
              'icon_size': None,
              'primary_color': '',
              'icon_img': '',
              'display_name_prefixed': 'r/RedditWarp',
              'sr_display_name_prefixed': 'r/RedditWarp',
              'subscribers': 1,
              'whitelist_status': None,
              'subreddit_type': 'public',
              'key_color': '',
              'name': 't5_3a9ph7',
              'created': 1603244493.0,
              'url': '/r/RedditWarp/',
              'sr': 'RedditWarp',
              'created_utc': 1603215693.0,
              'banner_size': None,
              'mod_permissions': [],
              'user_can_crosspost': True,
              'user_is_subscriber': True},
              ...,
              ]}

The `user_is_subscriber` field is not available when there is no user context.

The `created` and `created_utc` fields aren't available if the subreddit is
a user subreddit (i.e., `subreddit_type: user`).

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","A user with the specified name was not found."
