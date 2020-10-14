
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
   "can_assign_link_flair","boolean",""
   "can_assign_user_flair","boolean",""
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
   "link_flair_enabled","boolean",""
   "link_flair_position","string","E.g., `left`"
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
   "user_can_flair_in_sr","unknown?",""
   "user_flair_background_color","unknown?",""
   "user_flair_css_class","unknown?",""
   "user_flair_enabled_in_sr","boolean",""
   "user_flair_position","string","E.g., `right`"
   "user_flair_richtext","unknown array",""
   "user_flair_template_id","unknown?",""
   "user_flair_text","unknown?",""
   "user_flair_text_color","unknown?",""
   "user_flair_type","string",""
   "user_has_favorited","boolean?","Current user has favourited the subreddit. `null` if no user context."
   "user_is_banned","boolean?","Current user is banned from the subreddit. `null` if no user context."
   "user_is_contributor","boolean?","Current user is a contributor to the subreddit. `null` if no user context."
   "user_is_moderator","boolean?","Current user is a moderator of the subreddit. `null` if no user context."
   "user_is_muted","boolean?","Current user is muted in the subreddit. `null` if no user context."
   "user_is_subscriber","boolean?","Current user is subscribed to the subreddit. `null` if no user context."
   "user_sr_flair_enabled","boolean?","`null` if no user context."
   "user_sr_theme_enabled","boolean",""
   "videostream_links_count","integer",""
   "whitelist_status","string","E.g., `all_ads`"
   "wiki_enabled","boolean",""
   "wls","integer",""


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
