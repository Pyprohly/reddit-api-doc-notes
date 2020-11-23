
Subreddit
=========

Overview
--------

Schema
~~~~~~

.. csv-table:: Subreddit Object
   :header: "Field","Type (hint)","Description"
   :widths: 8, 6, 30
   :escape: \

   "accounts_active","integer","Then number of online users. Same as `active_user_count`."
   "accounts_active_is_fuzzed","boolean",""
   "active_user_count","integer","Then number of online users. Same as `accounts_active`."
   "advertiser_category","string","E.g., `\"Technology\"`"
   "all_original_content","boolean",""
   "allow_discovery","boolean",""
   "allow_galleries","boolean",""
   "allow_images","boolean",""
   "allow_polls","boolean",""
   "allow_predictions","boolean",""
   "allow_videogifs","boolean",""
   "allow_videos","boolean",""
   "banner_background_color","string","E.g., `#7193ff`"
   "banner_background_image","string","The url of the background banner image."
   "banner_img","string",""
   "banner_size","unknown?",""
   "collapse_deleted_comments","boolean",""
   "comment_score_hide_mins","integer",""
   "community_icon","string",""
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "description","string","Subreddit description text in markdown."
   "description_html","string","Subreddit description text HTML formatted."
   "disable_contributor_requests","boolean",""
   "display_name","string","The name of the subreddit. E.g., `AskReddit`"
   "display_name_prefixed","string","The name of the subreddit prefixed with `r/`. E.g., `r/AskReddit`"
   "emojis_custom_size","unknown?",""
   "emojis_enabled","boolean",""
   "free_form_reports","boolean",""
   "has_menu_widget","boolean",""
   "header_img","string",""
   "header_size","integer array (2)",""
   "header_title","string",""
   "hide_ads","boolean",""
   "icon_img","string",""
   "icon_size","unknown?",""
   "id","string","The ID36 of the subreddit (without the `t5_` prefix)."
   "is_crosspostable_subreddit","boolean",""
   "is_enrolled_in_new_modmail","unknown?",""
   "key_color","string",""
   "lang","string","E.g., `en`"
   "mobile_banner_image","string",""
   "name","string","The subreddit's full ID (with prefix `t5_`). Also see `id`."
   "notification_level","string","E.g., `low`"
   "original_content_tag_enabled","boolean",""
   "over18","boolean","Whether the subreddit is marked as NSFW."
   "primary_color","string","E.g., `#223a55`"
   "public_description","string",""
   "public_description_html","string",""
   "public_traffic","boolean",""
   "quarantine","boolean","Is the subreddit quarantined."
   "restrict_commenting","boolean",""
   "restrict_posting","boolean",""
   "show_media","boolean",""
   "show_media_preview","boolean",""
   "spoilers_enabled","boolean",""
   "submission_type","string","One of `any`, `link`, `self`."
   "submit_link_label","string",""
   "submit_text","string","The text shown in the submission form for the subreddit. Endpoint: `/r/{subreddit}/api/submit_text`"
   "submit_text_html","unknown?",""
   "submit_text_label","string",""
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`, `gold_only`, `gold_restricted`, or `user`."
   "subscribers","integer","The number of subscribers."
   "suggested_comment_sort","string?","`null` if no sort, or one of `confidence` (best), `old`, `top`, `qa`, `controversial`, or `new`."
   "title","string","The title of the subreddit. 'Community name'. 100 characters max."
   "url","string","E.g., `/r/AskReddit/`"
   "user_has_favorited","boolean?","Current user has favourited the subreddit. `null` if no user context."
   "user_is_banned","boolean?","Current user is banned from the subreddit. `null` if no user context."
   "user_is_contributor","boolean?","Current user is a contributor to the subreddit. `null` if no user context."
   "user_is_moderator","boolean?","Current user is a moderator of the subreddit. `null` if no user context."
   "user_is_muted","boolean?","Current user is muted in the subreddit. `null` if no user context."
   "user_is_subscriber","boolean?","Current user is subscribed to the subreddit. `null` if no user context."
   "user_sr_theme_enabled","boolean",""
   "videostream_links_count","integer",""
   "whitelist_status","string","E.g., `all_ads`"
   "wiki_enabled","boolean",""
   "wls","integer",""

   "user_flair_enabled_in_sr","boolean","Whether user flairs are enabled in the subreddit.

   In old Reddit this is the flair option that says \"enable user flair in this subreddit\"."
   "can_assign_link_flair","boolean","Whether or not users can assign a flair to their submission in this subreddit. If false, only a moderator can assign flairs to submissions.

   In old Reddit this is the flair option that says \"allow submitters to assign their own link flair\"."
   "can_assign_user_flair","boolean","Whether or not users can assign a flair to themselves in this subreddit. If false, only a moderator can assign flairs to users.

   In old Reddit this is the flair option that says \"allow users to assign their own flair\"."
   "link_flair_enabled","boolean","True if link flairs are enabled. This field is tied to the 'link flair position' flair setting: this field is false when set to `none`."
   "link_flair_position","string","Either `left`, or `right`, or empty string if `link_flair_enabled` is false (the 'none' option in the old Reddit UI)."
   "user_can_flair_in_sr","boolean?","Whether or not the current user is allowed to set their user flair in this subreddit. This will be true if the 'allow users to assign their own' user flair option is enabled, or if the current user is a moderator of the subreddit with the 'flair' permission. If neither of these conditions are satisfied, this field value will be `null`.

   Can also be `null` if there is no user context."
   "user_flair_background_color","string?","Current user's flair background color hex string. E.g., `#46d160`.

   If a flair template is not being used then the value will be an empty string.

   If a flair template is being used and the background color is unset then the value is the string `\"transparent\"`.

   Value `null` when:

   * A flair has never been assigned to the current user before in this subreddit.

   * There is no user context."
   "user_flair_css_class","string?","The current user's flair CSS class.

   Value starts as `null`.

   If not using a flair template and a CSS class is not set, the value is a empty string.

   If using a flair template and a CSS class is not set, the value is `null`.
   If the CSS class is removed the value will be an empty string (it will never return to `null` again!).

   Also value `null` when there is no user context."
   "user_flair_position","string","Either `left`, or `right` or empty string. Starts off as `right` in new subreddits.

   Can be set to an empty string via API calls (see `POST /r/{subreddit}/api/flairconfig`) but not through the UI.
   If an empty string then all user flairs are hidden, despite the `user_flair_enabled_in_sr` setting."
   "user_flair_richtext","unknown array","Richtext object."
   "user_flair_template_id","string?","Current user's flair template UUID.

   Value `null` when:

   * The flair isn't using a template.

   * User flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "user_flair_text","string?","The current user's flair text for the subreddit.

   Value `null` when:

   * A flair has never been assigned to the current user before in this subreddit.

   * There is no user context."
   "user_flair_text_color","string?","Either `dark` or `light`.

   Value `null` when:

   * A flair has never been assigned to the current user before in this subreddit.

   * There is no user context."
   "user_flair_type","string","Current user's flair type: either `text` or `richtext`. It is `text` by default."
   "user_sr_flair_enabled","boolean?","Whether or not the current user has opted to display their user flair in this subreddit (the 'Show my flair on this subreddit' option in the legacy UI).

   Value `null` when:

   * A flair has never been assigned to the current user before in this subreddit.

   * There is no user context."

Actions
-------

Get by ID
~~~~~~~~~

See :ref:`here <get_api_info>`.


Get by name
~~~~~~~~~~~

.. http:get:: /r/{subreddit}/about

*scope: read*

Return information about the subreddit by name.

Returns a JSON object with two keys: `kind` and `data`.
The value of `kind` is `t5`, and then `data` is your subreddit object.

If the subreddit is not found then the endpoint returns an empty listing (strangely)::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "children": [], "after": null, "before": null}}

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You don't have permission to access this subreddit."
   "404","* You specified the name of a special subreddit: `all`, `popular`, `friends`, `mod`.

   * The subreddit name specified contains invalid characters. This will return a 'page not found' HTML document."

.. seealso:: https://www.reddit.com/dev/api/#GET_r_{subreddit}_about


Create
~~~~~~

\.\.\.
