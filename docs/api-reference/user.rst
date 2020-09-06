
User
====

Overview
--------

Schema
~~~~~~

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "awardee_karma","integer",""
   "awarder_karma","integer",""
   "comment_karma","integer","Karma accumulated from commenting."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "has_subscribed","boolean",""
   "has_verified_email","boolean",""
   "hide_from_robots","boolean",""
   "icon_img","string","Avatar image. E.g., `https://www.redditstatic.com/avatars/avatar_default_01_A5A4A4.png`."
   "id","string","The ID of the user (without the `t2_` prefix)."
   "is_employee","boolean",""
   "is_friend","boolean",""
   "is_gold","boolean",""
   "is_mod","boolean",""
   "link_karma","integer","Karma accumulated from posting."
   "name","string","The user account name. E.g., `"spez"`"
   "total_karma","integer","Post karma plus comment karma. Same as `post_karma` and `comment_karma` fields added."
   "verified","boolean",""


.. _my_user_schema:

Additional fields for when the client has a user context and the user object matches that user.

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "can_create_subreddit","boolean",""
   "can_edit_name","boolean",""
   "coins","integer","The number of coins you have."
   "features","object","See :ref:`here <user_features>`."
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
   "is_suspended","boolean",""
   "new_modmail_exists","boolean",""
   "num_friends","integer","Number of friends in your friends list. See https://www.reddit.com/prefs/friends/."
   "over_18","boolean","Preference option \"I am over eighteen years old and willing to view adult content\" is checked."
   "password_set","boolean",""
   "pref_autoplay","boolean",""
   "pref_clickgadget","integer",""
   "pref_geopopular","string",""
   "pref_nightmode","boolean",""
   "pref_no_profanity","boolean",""
   "pref_show_snoovatar","boolean",""
   "pref_show_trending","boolean",""
   "pref_show_twitter","boolean",""
   "pref_top_karma_subreddits","boolean",""
   "pref_video_autoplay","boolean",""
   "suspension_expiration_utc","unknown?",""


Additional fields for when the client has a user context and the object does not match that user.

.. csv-table:: User Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "accept_chats","boolean","Whether the user is accepting chat messages."
   "accept_pms","boolean","Whether the user is accepting private messages."


.. _user_features:

Features sub-object
~~~~~~~~~~~~~~~~~~~

.. csv-table:: User.features Object
   :header: "Field","Type (hint)","Description"
   :escape: \

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


.. _user_subreddit:

Subreddit sub-object
~~~~~~~~~~~~~~~~~~~~

.. csv-table:: User.features Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "banner_img","string",""
   "banner_size","unknown?",""
   "coins","integer",""
   "community_icon","unknown?",""
   "default_set","boolean",""
   "description","string",""
   "disable_contributor_requests","boolean",""
   "display_name","The name of the subreddit. This will be your user account name prepended with `u_`. E.g., `u_Pyprohly`.",""
   "display_name_prefixed","Your user account name prepended with `u/`. E.g., `u/Pyprohly`.",""
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
   "subreddit_type","string","The string `\"user\"`."
   "subscribers","integer",""
   "title","string",""
   "url","string","E.g., `\"/user/Pyprohly/\"`"
   "user_is_banned","boolean",""
   "user_is_contributor","boolean",""
   "user_is_moderator","boolean",""
   "user_is_muted","boolean",""
   "user_is_subscriber","boolean",""


Actions
-------

Get by name
~~~~~~~~~~~

.. http:get:: /user/{username}/about

*scope: read*

Get information about a user by account name.

`{username}` is case-insensitive.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","A user with the specified name was not found."

.. seealso:: https://www.reddit.com/dev/api/#GET_user_{username}_about


Get partial by ID
~~~~~~~~~~~~~~~~~

.. http:get:: /api/user_data_by_account_ids

*scope: privatemessages*

Bulk get partial user objects by (full) IDs.

This endpoint returns a JSON object that maps user full IDs to partial user objects.

Specify the IDs with the `ids` parameter.
IDs must be prefixed with `t2_`.
Any ID that can't be resolved will be ignored.
Alphabetic characters in IDs must be all lowercase or they will be ignored.
Duplicate IDs will be ignored.

This endpoint will process as many IDs as it can as long as the total URL length is
less than the 7220 character limit.
This means you can request up to a little over 500 IDs at a time assuming each ID
string is the largest observed length for a user ID at this time of this writing.
Clients should be able to safely request in batches of up to 500 IDs at a time.

This end point returns an object with the following fields:

.. csv-table:: Partial user objects
   :header: "Field","Type (hint)","Description"
   :escape: \

   "comment_karma","integer","Karma accumulated from commenting."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "link_karma","integer","Karma accumulated from posting."
   "name","string","The user account name. E.g., `"spez"`"
   "profile_color","string",""
   "profile_img","string","Avatar image. Same value as the `icon_img` field in normal user objects.
   E.g., `https://www.redditstatic.com/avatars/avatar_default_01_A5A4A4.png`."
   "profile_over_18","boolean",""

|

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "ids","string","A comma separated list of user full IDs (each being prefixed by `t2_`)."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "414","The requested URL length is too long (over 7219 characters)."

\.\.\.
