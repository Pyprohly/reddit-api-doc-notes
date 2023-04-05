
Subreddit
=========

Overview
--------

.. _subreddit-schema:

Schema
~~~~~~

This table only applies to subreddits that are not private or banned.
The `GET /r/{subreddit}/about` endpoint will return an error if the target subreddit is private or banned.
On the other hand, `GET /api/info` will return an object with the same keys as documented in the table below
but with many of the values being `null`.

.. csv-table:: Subreddit Object (`GET /r/{subreddit}/about`)
   :header: "Field","Type (hint)","Description"

   "accounts_active",".","Deprecated. Then number of online users. Same as `active_user_count`."
   "active_user_count","integer?","The number of online users who are subscribed to the subreddit.

   Value is `null` if object was retrieved from a search."
   "accounts_active_is_fuzzed","boolean",""
   "advertiser_category","string","E.g., `""Technology""`"
   "all_original_content","boolean",""
   "allow_discovery","boolean",""
   "allow_galleries","boolean","True if gallery posts are allowed."
   "allow_images","boolean",""
   "allow_polls","boolean","True if poll posts are allowed."
   "allow_predictions","boolean",""
   "allow_videogifs","boolean",""
   "allow_videos","boolean",""
   "header_img","string?","The legacy reddit subreddit icon image URL.

   Value is `null` if the subreddit icon has never been set before. If it's been set and has been removed
   the value will be an empty string."
   "header_size","integer array?","The legacy reddit subreddit icon image width and height.

   Value is `null` if a subreddit icon image is not currently set."
   "header_title","string?","The hover text of the legacy reddit subreddit icon image.

   Value is `null` if a the subreddit icon image hover text has never been set before.
   If it's been set and has been removed the value will be an empty string."
   "icon_img","string?","The legacy reddit subreddit mobile icon image.

   Value is `null` if the subreddit icon has never been set before. If it's been set and has been removed
   the value will be an empty string."
   "icon_size","integer array?","The legacy reddit subreddit mobile icon image width and height.

   Value is `null` if a subreddit icon image is not currently set."
   "banner_img","string?","The legacy reddit subreddit mobile banner image.

   Value is `null` if the subreddit icon has never been set before. If it's been set and has been removed
   the value will be an empty string."
   "banner_size","integer array?","The legacy reddit subreddit mobile banner image width and height.

   Value is `null` if a subreddit icon image is not currently set."
   "banner_background_image","string","The url of the background banner image."
   "banner_background_color","string","E.g., `#7193ff`"
   "mobile_banner_image","string",""
   "community_icon","string",""
   "collapse_deleted_comments","boolean",""
   "comment_score_hide_mins","integer",""
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "description","string","Subreddit description text in markdown."
   "description_html","string","Same as `description` but HTML formatted."
   "disable_contributor_requests","boolean",""
   "display_name","string","The name of the subreddit. E.g., `AskReddit`"
   "display_name_prefixed","string","The name of the subreddit prefixed with `r/`. E.g., `r/AskReddit`.
   For user subreddits the `u/` prefix is used. E.g., `r/Pyprohly`."
   "emojis_custom_size","unknown?",""
   "emojis_enabled","boolean",""
   "free_form_reports","boolean",""
   "has_menu_widget","boolean","True if the subreddit has a menu widget active, otherwise false.

   Value is false if the object was retrieved from a search."
   "hide_ads","boolean",""
   "id","string","The ID36 of the subreddit (without the `t5_` prefix)."
   "is_crosspostable_subreddit","boolean",""
   "is_enrolled_in_new_modmail","unknown?",""
   "key_color","string","E.g., `#ddbd37`. Can be an empty string."
   "primary_color","string","E.g., `#223a55`. Can be an empty string."
   "lang","string","E.g., `en`"
   "name","string","The subreddit's full ID36 (with prefix `t5_`). Also see `id`."
   "notification_level","string","E.g., `low`"
   "original_content_tag_enabled","boolean",""
   "over18","boolean","Whether the subreddit is marked as NSFW."
   "public_description","string",""
   "public_description_html","string",""
   "public_traffic","boolean","Whether the subreddit's traffic page is publicly-accessible."
   "quarantine","boolean","Is the subreddit quarantined."
   "restrict_commenting","boolean",""
   "restrict_posting","boolean",""
   "show_media","boolean",""
   "show_media_preview","boolean",""
   "spoilers_enabled","boolean",""
   "submission_type","string","One of `any`, `link`, `self`."
   "submit_text","string","The text shown in the submission form for the subreddit. Endpoint: `/r/{subreddit}/api/submit_text`"
   "submit_text_html","unknown?",""
   "submit_text_label","string?","Custom label text for the ""Submit a new text post"" button.

   This can sometimes be `null`. Not sure why. When you create a new subreddit the value starts as an empty string.

   In old Reddit this is the ""Custom label for submit text post button"" subreddit option.
   "
   "submit_link_label","string?","Custom label text for the ""Custom label for submit link button"" button.

   Can possibly be `null`? Not sure, but `submit_text_label` is observed to be `null` sometimes.
   When you create a new subreddit the value starts as an empty string.

   In old Reddit this is the ""Custom label for submit text post button"" subreddit option."
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`, `gold_only`, `gold_restricted`, or `user`."
   "subscribers","integer","The number of subscribers."
   "suggested_comment_sort","string?","Either: `confidence` (best), `new`, `old`, `top`, `qa`, `controversial`, or `live`.

   Value `null` if not set."
   "title","string","The title of the subreddit. 'Community name'. 100 characters max."
   "url","string","E.g., `/r/AskReddit/`"
   "user_has_favorited","boolean?","Current user has favourited the subreddit. `null` if no user context."
   "user_is_banned","boolean?","Current user is banned from the subreddit. `null` if no user context."
   "user_is_contributor","boolean?","Current user is an approved contributor to the subreddit. `null` if no user context."
   "user_is_moderator","boolean?","Current user is a moderator of the subreddit. `null` if no user context."
   "user_is_muted","boolean?","Current user is muted in the subreddit. `null` if no user context."
   "user_is_subscriber","boolean?","Current user is subscribed to the subreddit. `null` if no user context."
   "user_sr_theme_enabled","boolean","Whether the current user allows subreddit custom CSS.

   This is the ""allow subreddits to show me custom themes"" preference in old reddit."
   "videostream_links_count","integer",""
   "whitelist_status","string","E.g., `all_ads`"
   "wiki_enabled","boolean",""
   "wls","integer",""
   "user_flair_enabled_in_sr","boolean?","Whether user flairs are enabled in the subreddit.

   In old Reddit this is the flair option that says ""enable user flair in this subreddit"".

   Value is false if object was retrieved from a search.

   Notice that this field name ends with `_in_sr` because `user_flair_enabled` is already being used for something else."
   "link_flair_enabled","boolean","Whether post flairs are enabled in the subreddit.

   In old Reddit, this field is tied to the 'link flair position' flair setting: the value is false when set to `none`."
   "can_assign_user_flair","boolean","Whether or not users can assign a flair to themselves in this subreddit.

   If false, only a moderator can assign flairs to users.

   In old Reddit this is the flair option that says ""allow users to assign their own flair""."
   "can_assign_link_flair","boolean","Whether or not users can assign a flair to their submission in this subreddit.

   If false, only a moderator can assign flairs to submissions.

   In old Reddit this is the flair option that says ""allow submitters to assign their own link flair""."
   "user_flair_position","string","Either `left`, or `right` or empty string.

   Starts off as `right` in new subreddits.

   Can be set to an empty string via API calls (see `POST /r/{subreddit}/api/flairconfig`) but not through the UI.

   If an empty string then all user flairs are hidden, despite the `user_flair_enabled_in_sr` setting.
   "
   "link_flair_position","string","Either `left`, or `right`, or empty string if `link_flair_enabled` is false (the 'none' option in the old Reddit UI)."
   "user_can_flair_in_sr","boolean?","Whether or not the current user is allowed to set their user flair in this subreddit. This will be true if the 'allow users to assign their own' user flair option is enabled, or if the current user is a moderator of the subreddit with the 'flair' permission. If neither of these conditions are true, this field value will be `null`.

   Value is `null` if there is no user context. Value is `null` if the object was retrieved from a search."
   "user_flair_richtext","unknown array","Richtext object."
   "user_flair_template_id","string?","Current user's flair template UUID.

   Value `null` when:

   * The flair isn't using a template.
   * User flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false).
   "
   "user_flair_type","string","Current user's flair type: either `text` or `richtext`."
   "user_flair_text","string?","The current user's flair text for the subreddit.

   Value `null` when:

   * There is no user context.
   * User flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false).
   * A flair has never been assigned to the current user before in this subreddit.
   "
   "user_flair_css_class","string?","The current user's flair CSS class.

   When a flair template is being used, the value of this field will be that of the CSS class designated by the template. If the flair template does not specify a CSS class then the value will be `null`.

   When no flair template is being used, the value starts as `null`. If a CSS class was ever manually assigned (by a moderator), this field will never be `null` again while a flair template isn't being used, and clearing the CSS class results in this field being an empty string.

   Value is `null` when there is no user context.

   Value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "user_flair_background_color","string?","Current user's flair background color hex string. E.g., `#46d160`.

   If a flair template is not being used then the value will be an empty string.

   If a flair template is being used and the background color is unset then the value is the string `""transparent""`.

   Value `null` when:

   * There is no user context.
   * User flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false).
   * A flair has never been assigned to the current user before in this subreddit.
   "
   "user_flair_text_color","string?","Color scheme. Either `dark`, `light`, or empty string.

   Value is empty string if a flair template is not being used (i.e., `user_flair_template_id` is `null`).

   Value `null` when:

   * There is no user context.
   * User flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false).
   * A flair has never been assigned to the current user before in this subreddit.
   "
   "user_sr_flair_enabled","boolean?","Whether or not the current user has opted to display their user flair in this subreddit (the 'Show my flair on this subreddit' option in the legacy UI).

   Value `null` when:

   * There is no user context.
   * Object was retrieved from a search.
   "


Actions
-------

Get by ID
~~~~~~~~~

Use `GET /api/info`. See :ref:`here <get-api-info>`.


Get by name
~~~~~~~~~~~

Since `2020-10-21`
(`this post <https://www.reddit.com/r/redditdev/comments/jfltfx/any_way_of_speeding_up_my_api_requests/g9le48w/>`_)
the `GET /api/info` endpoint can be used to get subreddit objects by name, and also in bulk too.

However, there is a difference between the endpoints: non-public subreddits can be retrieved
with `GET /api/info` but not with `GET /r/{subreddit}/about`, which returns a 403 error,
although many of the fields in the subreddit object may be `null` rather than the type
reported in the schema table above.

-----

.. http:get:: /r/{subreddit}/about

*scope: read*

Return information about the subreddit by name.

Returns a JSON object with two keys: `kind` and `data`.
The value of `kind` is `t5`, and then `data` is your subreddit object.

If the subreddit is not found then the endpoint returns an empty listing (strangely)::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "children": [], "after": null, "before": null}}

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "private","403","The target subreddit is private.","
   ``{""reason"": ""private"", ""message"": ""Forbidden"", ""error"": 403}``
   "
   "banned","404","The target subreddit is banned.","
   ``{""reason"": ""banned"", ""message"": ""Not Found"", ""error"": 404}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "302","The subreddit does not exist."
   "404","* You specified the name of a special subreddit: `all`, `popular`, `friends`, `mod`.

   * The specified subreddit name was too long or contained invalid characters. This will return a 'page not found' HTML document."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_r_{subreddit}_about>`_


Create
~~~~~~

.. http:post:: /api/site_admin

*scope: modconfig*

Create or configure a subreddit.

.. note::

   To configure an existing subreddit's options it is recommended to use `PATCH /api/v1/subreddit/update_settings`
   which allows you to modify a subset of options, without needing to specify all the options.

If `sr` is specified, the request will attempt to modify the specified subreddit.
If not, a subreddit with name `name` will be created.

When configuring a subreddit, this endpoint expects all values to be supplied on every request.
If modifying a subset of options, it may be useful to get the current settings from `GET /about/edit` first.

Returns ``{"json": {"errors": []}}`` on success.

Mandatory parameters:

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "name","string","The new subreddit's name. This parameter is ignored if `sr` is specified and it is a valid ID."
   "sr","string","The full ID36 of an existing subreddit. This parameter is ignored if the ID is not valid."
   "title","string","Mandatory. The title of the subreddit."
   "wikimode","string","Mandatory. One of `disabled`, `modonly`, `anyone`."
   "link_type","string","Mandatory. One of `any`, `link`, `self`."
   "type","string","Mandatory. One of `gold_restricted`, `archived`, `restricted`, `private`,
   `employees_only`, `gold_only`, `public`, `user`."
   "\.\.\.","\.\.\.","\.\.\."

This endpoint takes a lot of parameters see
`the official documentation <https://www.reddit.com/dev/api/#POST_api_site_admin>`_ for a complete list.

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_TEXT","200","* The `name` or `sr` parameter was not specified.

   * The `name` parameter was specified but was empty.

   * The `title` parameter was not specified.

   * The ID specified by `sr` is not valid.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""name""]]}}``
   "
   "SUBREDDIT_EXISTS","200","The subreddit name specified by `name` already exists.","
   ``{""json"": {""errors"": [[""SUBREDDIT_EXISTS"", ""that subreddit already exists"", ""name""]]}}``
   "
   "BAD_SR_NAME","200","The subreddit name specified by `name` is invalid.","
   ``{""json"": {""errors"": [[""BAD_SR_NAME"", ""This community name isn't recognizable. Check the spelling and try again."", ""name""]]}}``
   "
   "INVALID_OPTION","The `wikimode`, `link_type`, and `type` parameters were not specified or have an invalid value.",""

.. seealso:: https://www.reddit.com/dev/api/#POST_api_site_admin


Get settings
~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/about/edit

*scope: modconfig*

Get the settings of a subreddit.

In the API, this returns the current settings of the subreddit. It can be used in `POST /api/site_admin`.

Example output structure::

   {"kind": "subreddit_settings",
    "data": {"default_set": false,
             "toxicity_threshold_chat_level": 1,
             "crowd_control_chat_level": 1,
             "disable_contributor_requests": false,
             "subreddit_id": "t5_g495e",
             ...}}

For a subreddit that does not exist, an empty listing structure is returned::

   {"kind": "Listing",
    "data": {"modhash": null,
             "dist": 0,
             "children": [],
             "after": null,
             "before": null}}

For a subreddit that you do not have permission to view subreddit settings for, a HTTP 404 error is returned.

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "302","The specified subreddit does not exist."
   "404","* There is no user context.
   * You don't have permission to view this subreddit's settings."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_r_{subreddit}_about_edit>`_


Update settings
~~~~~~~~~~~~~~~

.. http:patch:: /api/v1/subreddit/update_settings

*scope: modconfig*

Update a subreddit's settings.

This endpoint takes JSON data.
Settings are provided as key/value entries in the JSON data.
Specify the target subreddit by providing a full ID36 value to an `sr` key.

See `Get settings`_ for a clue on the valid options.

Returns an empty JSON object on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "SUBREDDIT_REQUIRED","200","* The `sr` parameter was not specified.

   * The subreddit specified by `sr` does not exist.","
   ``{""json"": {""errors"": [[""SUBREDDIT_REQUIRED"", ""you must specify a subreddit"", ""sr""]]}}``
   "
   "MOD_REQUIRED","200","The current user is not a moderator of the subreddit specified by the `sr` parameter.","
   ``{""json"": {""errors"": [[""MOD_REQUIRED"", ""You must be a moderator to do that."", ""sr""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","No JSON data was received."


Get trending subreddit names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: https://reddit.com/api/trending_subreddits.json

*scope: (any)*

DEPRECATED: This endpoint does not work.

Return a list of trending subreddits, link to the comment in r/trendingsubreddits, and the comment count of that link.

Example output::

   {"subreddit_names": ["lotr", "Mandalorian", "blackfriday", "marvelmemes", "rpghorrorstories"],
    "comment_count": 1,
    "comment_url": "/r/trendingsubreddits/comments/k2itz2/trending_subreddits_for_20201128_rlotr/"}

.. note:: The documented endpoint `GET /api/trending_subreddits` always results in a HTTP 400 error.

.. seealso:: https://www.reddit.com/dev/api/#GET_api_trending_subreddits


Get similar subreddits
~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/similar_subreddits

*scope: (any)*

Get a list of similar subreddits.

Returns subreddit objects in a listing structure.

If a specified subreddit ID does not exist or is invalid, it is ignored.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "sr_fullnames","string","A comma-separated string of subreddit (`t5_` prefixed) full ID36s.

   The maximum limit is unknown."
   "max_recs","integer","The maximum number of entries to return. Default: 10.

   The parameter name stands for 'max. records', or maybe even 'max. recommendations'."


Subscribe
~~~~~~~~~

.. http:post:: /api/subscribe

*scope: subscribe*

Subscribe or unsubscribe from subreddits.

Use `action=sub` to subscribe. Use `action=unsub` to unsubscribe. The user must have access to the subreddit
to be able to subscribe to it.

The `skip_initial_defaults` parameter can be set to a true value to prevent automatically subscribing to the current
set of defaults when the user makes their first subscription (when `has_subscribed` attribute is false on the account).
Attempting to set it for an unsubscribe action will result in a 400 HTTP error.

If both `sr` and `sr_name` are used together, `sr` will take precedence and `sr_name` will be ignored.

If all subreddits specified by the `sr` or `sr_name` parameters don't exist, a 404 HTTP error is returned.

If any of the subreddits specified cannot be accessed, or is a special subreddit such as `popular`, `all`, or `random`,
then the entire action is aborted, no subreddits will be subscribe/unsubscribed to. A 403 HTTP error is returned.

The limit of the number of subreddits you can specify at once is unknown. This endpoint becomes increasingly unstable
the more items you specify at a time. Request processing times slow down and various errors begin to occur. If the
client doesn't timeout first:

* If over approximately 250 items are specified at once, a 503 HTTP error may be returned (with a *"Our CDN was unable
  to reach our servers"* HTML document being sent) but the action should succeed.

* If over approximately 460 items are specified at once, a 400 HTTP error may be returned (with a HTML document being
  sent) and the action is aborted.

This is a slow endpoint. It takes about 5.5 seconds to process 100 items.

Returns an empty JSON object on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "action","string","Either `sub` or `unsub`. Default if not specified: `unsub`."
   "sr","string","A comma separated list of subreddit full ID36s (prefixed with `t5_`)."
   "sr_name","string","A comma separated list of subreddit names."
   "skip_initial_defaults","boolean","Prevent automatically subscribing the user to the current set of
   defaults when they take their first subscription."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_subscribe

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","The `skip_initial_defaults` parameter was true when `action=unsub`."
   "403","* A subreddit specified in `sr` or `sr_name` could not be accessed.

   * A subreddit specified in `sr_name` was a special subreddit name such as `popular`, `all`, or `random`."
   "404","* The `sr` or `sr_name` parameter was not specified.

   * All subreddits specified by the `sr` or `sr_name` parameter do not exist."
   "503","Sends *""Our CDN was unable to reach our servers""* HTML document. When over approximately 250 items are specified at once."


.. _subreddit-get-rules:

Get rules
~~~~~~~~~

.. http:get:: /r/{subreddit}/about/rules

*scope: read*

Get a subreddit's rules.

An object is returned with three fields: `rules`, `site_rules`, and `site_rules_flow`.
The `rules` object is an array of rule objects specific to the target subreddit.
The `site_rules` and `site_rules_flow` fields are the same regardless of which subreddit is targeted.

Returns an empty listing object if the subreddit is not found::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "children": [], "after": null, "before": null}}

Rule objects have the following attributes:

.. csv-table:: Rules Object
   :header: "Field","Type (hint)","Description"

   "priority","integer","Value matches its index in the array."
   "kind","string","One of `all`, `link`, or `comment`.

   Applies to.

   * `all`: Posts & Comments.
   * `link`: Posts only.
   * `comment`: Comments only."
   "description","string","Rule description text. Up to 500 characters."
   "description_html?","string","Same as `description` but HTML formatted.

   This field won't exist if `description` is empty."
   "short_name","string","Short description. Up to 100 characters."
   "violation_reason","string","Violation reason text. Up to 100 characters.

   Value matches `short_name` if left empty in the UI. It's unfortunately not possible
   to tell if this field is empty through the API."
   "created_utc","float","Unix timestamp of when the rule was created. Always a whole number."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","The subreddit specified could not be accessed."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_r_{subreddit}_about_rules>`_


Get post requirements
~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/v1/{subreddit}/post_requirements

*scope: submit*

Fetch moderator-designated requirements to post to the subreddit.

Moderators may enable certain restrictions, such as minimum title length, when making a submission to their subreddit.

Clients may use the values returned by this endpoint to pre-validate fields before making a request to
`POST /api/submit`. This may allow the client to provide a better user experience to the user, for example by
creating a text field in their app that does not allow the user to enter more characters than the max title length.

A non-exhaustive list of possible requirements a moderator may enable:

* `body_blacklisted_strings` (string array):. Users may not submit posts that contain these words.
* `body_restriction_policy` (string): One of `required`, `notAllowed`, or `none`, meaning that a text post body is
  required, not allowed, or optional, respectively.
* `domain_blacklist` (string array): Users may not submit links to these domains
* `domain_whitelist` (string array): Users submissions MUST be from one of these domains
* `is_flair_required` (boolean): If True, flair must be set at submission time.
* `title_blacklisted_strings` (string array): Submission titles may NOT contain any of the listed strings.
* `title_required_strings` (string array): Submission title MUST contain at least ONE of the listed strings.
* `title_text_max_length` (integer): Maximum length of the title field.
* `title_text_min_length` (integer): Minimum length of the title field.

Example output for post requirement settings that have not been changed::

   {"title_regexes": [],
    "body_blacklisted_strings": [],
    "title_blacklisted_strings": [],
    "body_text_max_length": null,
    "title_required_strings": [],
    "guidelines_text": null,
    "gallery_min_items": null,
    "domain_blacklist": [],
    "domain_whitelist": [],
    "title_text_max_length": null,
    "body_restriction_policy": "none",
    "link_restriction_policy": "none",
    "guidelines_display_policy": null,
    "body_required_strings": [],
    "title_text_min_length": null,
    "gallery_captions_requirement": "none",
    "is_flair_required": false,
    "gallery_max_items": null,
    "gallery_urls_requirement": "none",
    "body_regexes": [],
    "link_repost_age": null,
    "body_text_min_length": null}

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "SUBREDDIT_NOEXIST","404","The specified subreddit does not exist.","
   ``{""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Not Found"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "
   "SUBREDDIT_NO_ACCESS","403","The specified subreddit is private or banned.","
   ``{""explanation"": ""you aren't allowed access to this subreddit"", ""message"": ""Forbidden"", ""reason"": ""SUBREDDIT_NO_ACCESS""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_v1_{subreddit}_post_requirements>`_


Get submit text
~~~~~~~~~~~~~~~

.. http:get:: /r/{subreddit}/api/submit_text

*scope: submit*

Get the submission text for the subreddit.

This text is set by the subreddit moderators and intended to be displayed on the submission form.

Returns an object with two fields: `submit_text` and `submit_text_html`. These are the same as those found on
the subreddit schema.

If the subreddit is not found then the endpoint returns an empty listing::

   {"kind": "Listing", "data": {"modhash": null, "dist": 0, "children": [], "after": null, "before": null}}

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","The subreddit specified could not be accessed because it is private."
   "404","The subreddit specified could not be accessed because it is banned."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_submit_text


Search subreddits by name (returning subreddit names)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/search_reddit_names
.. http:post:: /api/search_reddit_names

*scope: read*

List subreddit names that begin with a query string.

Subreddits whose names begin with `query` will be returned.

The GET and POST endpoints are equivalent but POST also accepts form-encoded data.

Subreddits that are banned or private are included.

Returns an object with one field, `names`, which is an array of subreddit names.

.. csv-table:: URL Params / Form Data
   :header: "Field","Type (hint)","Description"

   "query","string","A string up to 50 characters long to match the start of subreddit names.
   The match is case insensitive."
   "exact","boolean","If true, only an exact match will be returned. Exact matches are inclusive of `over_18`
   subreddits, but not `hide_ad` subreddits when `include_unadvertisable` is false."
   "include_over_18","boolean","Whether to filter NSFW subreddits.

   This parameter is ignored if there is a user context. If there is a user context the value is taken from the
   ""include not safe for work (NSFW) search results in searches"" preference option.

   This parameter is ignored and enabled if the `exact` parameter is true.

   Default: true."
   "include_unadvertisable","boolean","If false, subreddits that have `hide_ads` set to `true` or are on
   the `anti_ads_subreddits` list will be filtered. Default: ??? [needs checking]"
   "search_query_id","string","unknown"
   "typeahead_active","boolean?","unknown"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","`exact` true was specified and the subreddit name could not be found."


Search subreddits by name (returning partial subreddit objects)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/search_subreddits

*scope: read*

List partial subreddit objects that begin with a query string.

Same as `(GET/POST) /api/search_reddit_names` but returns partial subreddit objects
instead of strings.

On success, returns an object with one field: `subreddits` whose value is
an array of partial subreddit objects.

Subreddits that are banned or private are included.
Interestingly, this endpoint can be used to determine the subscriber count of private subreddits.

.. csv-table:: Partial Subreddit Object
   :header: "Field","Type (hint)","Description"

   "name","string","The subreddit name."
   "subscriber_count",".","Same as the `subscribers` field on the Subreddit schema."
   "active_user_count",".","Same as on Subreddit schema."
   "icon_img",".","Same as on Subreddit schema."
   "key_color",".","Same as on Subreddit schema."
   "allow_images",".","Same as on Subreddit schema."
   "is_chat_post_feature_enabled","boolean",""
   "allow_chat_post_creation","boolean",""

.. csv-table:: URL Params / Form Data
   :header: "Field","Type (hint)","Description"

   "...",".","Same as in `GET /api/search_reddit_names`."

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "...","Same as in `GET /api/search_reddit_names`."


.. _subreddit-search-subreddits:

Search subreddits by name and description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /subreddits/search

*scope: read*

Search subreddits by name or description.

This endpoint returns a :ref:`paginated listing <listings-overview>`.

Matches substrings of `display_name` and `public_description` fields of subreddit objects.

If the parameter `q` is not specified, this endpoint returns `"{}"`
(i.e., a string of an empty JSON object).

The `sr_detail` parameter is not supported (despite the offical docs saying so).

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "...",".",":ref:`Listing common parameters <listings-overview>`."
   "q","string","A search query. Matches user name beginnings or descriptions."
   "(sort)","string","Documented parameter but doesn't seem to do anything.

   Either `relevance` or `activity`."
   "(show_users)","boolean","Documented parameter but doesn't seem to do anything.

   If true, user subreddits are included in the search?"
