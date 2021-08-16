
Submission
==========

Overview
--------

There are different post types: `text`, `link`, `image`, `gallery`, `video`, `poll`, `crosspost`.

Post type distinguish logic:

* `text`: ``d['is_self']``
* `image`: ``d.get('post_hint') == 'image'``
* `video`: ``d['is_video']``
* `gallery`: ``d.get('is_gallery', False)``
* `poll`: ``'poll_data' in d``
* `crosspost`: ``'crosspost_parent' in d``
* `link`: (otherwise)

To determine the type of a crosspost you must lookup the post type of the submission in `crosspost_parent`.
This does not have to be done recursively because when you crosspost a crosspost the `crosspost_parent` will be
the original post and not the crosspost you've crossposted.


.. _submission_schema:

Schema
~~~~~~

.. csv-table:: Submission Object
   :header: "Field","Type (hint)","Description"
   :widths: 8, 6, 30
   :escape: \

   "approved_at_utc","integer?","Unix time when the comment was approved. `null` if not approved or the current user is not a moderator of the subreddit."
   "subreddit","string","The subreddit name. E.g., `IAmA`"
   "selftext","string","The body text of the submission. Empty string if it is not a text or poll post."
   "selftext_html?","string?","The HTML of the post. This will be null if it is not a text or poll post.

   This key will not exist if the object was returned from `POST /api/editusertext`."
   "author_fullname?","string","The full ID36 of the author.

   This attribute is not available if the post was removed or deleted."
   "saved","boolean","Whether the authenticated user has saved this post.

   For clients with no user context this will always be `false`."
   "mod_reason_title","unknown?",""
   "gilded","integer",""
   "clicked","boolean",""
   "title","string","The title of the post."
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "hidden","boolean",""
   "downs","integer","Always `0`."
   "thumbnail","string","The post thumbnail as seen in listings.

   When retrieving posts from a listing, the value can sometimes be `image` instead of a URL.

   Other than a URL, possible values include: (empty string), `self`, `default`, `image`, `nsfw`, `spoiler`.

   It is an empty string when the subreddit's media preferences has thumbnails disabled.
   "
   "thumbnail_width","integer?","Thumbnail width.

   It is possible for this field to be non-null while the
   `thumbnail` field is something like `self` or `default`."
   "thumbnail_height","integer?","Thumbnail height."
   "hide_score","boolean","Whether the score is currently hidden."
   "name","string","The post's full ID36 (with prefix `t3_`). Also see `id`."
   "quarantine","boolean","Whether the post is in a quarantined subreddit."
   "upvote_ratio","float","Upvote ratio."
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`, `gold_only`, `gold_restricted`, or `user`."
   "ups","integer","Same as `score`."
   "total_awards_received","integer","Number of rewards on the post."
   "media_embed","unknown object",""
   "is_original_content","boolean","Whether the post is marked as OC."
   "media","object?","`null` if not a video post.

   Example value for a video post::

      {'reddit_video': {'bitrate_kbps': 2400,
                     'fallback_url': 'https://v.redd.it/1782h5212t971/DASH_720.mp4?source=fallback',
                     'height': 720,
                     'width': 720,
                     'scrubber_media_url': 'https://v.redd.it/1782h5212t971/DASH_96.mp4',
                     'dash_url': 'https://v.redd.it/1782h5212t971/DASHPlaylist.mpd?a=1628262163%2CODUxMmVjYTc2NTBiOTYyYTVkZDQ1ODY2NTU4MGUwODQ4MjVhMjIwODY2MTAyNmQ1YjkzZDI2OTZkZWVlMDA3NA%3D%3D&v=1&f=sd',
                     'duration': 6,
                     'hls_url': 'https://v.redd.it/1782h5212t971/HLSPlaylist.m3u8?a=1628262163%2CZDQ5MTFjZWM2NGM2Yzk0YmUxNGJkYzUzZDI1OWI5YzZkMGIxYWYyMzgzYTM2ZjlkYTY3OWI1ZTM0MDU4NjJhNQ%3D%3D&v=1&f=sd',
                     'is_gif': False,
                     'transcoding_status': 'completed'}}

   Example value for a videogif post::

      {'reddit_video': {'bitrate_kbps': 4800,
                     'fallback_url': 'https://v.redd.it/o4m3p54mps971/DASH_1080.mp4?source=fallback',
                     'height': 1080,
                     'width': 498,
                     'scrubber_media_url': 'https://v.redd.it/o4m3p54mps971/DASH_96.mp4',
                     'dash_url': 'https://v.redd.it/o4m3p54mps971/DASHPlaylist.mpd?a=1628262163%2COTZlZjY1MzAzOTlhZjQ5MTZjNDE4NmZlNGQ2NGQ4OTRlYjFkNDc2MGRjMDI4ZDEyNDUyNGIzYTZmZWM3MWY4Mg%3D%3D&v=1&f=sd',
                     'duration': 2,
                     'hls_url': 'https://v.redd.it/o4m3p54mps971/HLSPlaylist.m3u8?a=1628262163%2CMDA1ZmVjMDM1MTA0M2EzM2U0MjJhZWYxYWIwMjQyMmI2NzE5ZWE0ODI4ZGI5ZWJlYThhOWNjZjFjNmMwYzkwOQ%3D%3D&v=1&f=sd',
                     'is_gif': True,
                     'transcoding_status': 'completed'}}

   "
   "secure_media","object?","Seems to be the same as the `media` field."
   "is_reddit_media_domain","boolean","Whether media is reddit hosted, that is
   either i.redd.it for images or v.redd.it for videos. This will always be false for a text post."
   "is_meta","boolean",""
   "category","unknown?",""
   "secure_media_embed","unknown object",""
   "can_mod_post","boolean",""
   "score","integer","The number of upvotes (minus downvotes). This attribute will work even if `hide_score` is `true`."
   "approved_by","string?","The name of the redditor who approved this post. `null` if not approved or the current user is not a moderator of the subreddit."
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited."
   "gildings","unknown object",""
   "post_hint?","string","The type of post.

   Known values: `self`, `link`, `image`, `hosted:video`, `rich:video`.

   Field does not exist if it is a gallery post.

   This field does not exist if the `preview` key does not exist."
   "is_gallery?","boolean","True if a gallery post.

   This field does not exist if it is not a gallery post. (Hence value should always be true.)

   This is false if the post is a crosspost to a gallery post."
   "gallery_data?","object","This field does not exist if not a gallery post.

   Contains a bit of information about the gallery content, including captions and URLs.
   Contains IDs for accessing the `media_metadata` field object."
   "media_metadata?","object","Information about media items linked in the post.

   Includes information for image URLs, image file types, dimensions.

   This field does not exist if there is no media in the post."
   "poll_data?","object","This field does not exist if not a poll post."
   "content_categories","string array?",""
   "is_self","boolean","True if a text post.

   This is false if the post is a crosspost to a text post."
   "mod_note","string?",""
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "wls","integer?","Unknown. Often `6`. Possibly stands for \"white list status\"?"
   "pwls","integer?","Unknown. Possibly stands for \"parent white list status\"?"
   "removed?","boolean","`true` if the submission is removed.

   This will not be `true` if the removed post was indicated as spam! It is recommended to check for `null` in
   `removed_by_category` to tell if a post was removed.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "removed_by_category","string?","`null` if not removed, otherwise possible values: `author`, `anti_evil_ops`, `community_ops`, `legal_operations`, `copyright_takedown`, `reddit`, `user`, `deleted`, `moderator`, `automod_filtered`.

   `deleted`: The post author, who is not a moderator of the subreddit, deleted the post.
   `author`: The post author, who is a moderator of the subreddit, removed the post.
   `moderator`: A moderator of the subreddit removed the post.
   "
   "banned_by","string?","The name of the redditor who removed this post. `null` if not removed or the current user is not a moderator of the subreddit."
   "banned_at_utc","integer?","Unix time when the comment was removed. `null` if not removed or the current user is not a moderator of the subreddit."
   "ban_note?","string","The message provided by the moderator when the post was removed. The note will be `spam` if the post was indicated to be spam during removal."
   "domain","string","If a link post, the domain of the link. If a text post, it is
   the name of the subreddit prefixed with `self.`, e.g., `self.IAmA`."
   "allow_live_comments","boolean",""
   "likes","boolean?","`null` if no user context.

   If user context: `null` if not voted on, `true` if upvoted, `false` if downvoted."
   "suggested_sort","string?","`null` if suggested sort is not set, or one of `confidence` (best), `top`, `new`, `controversial`, `old`, `qa`."
   "view_count","unknown?",""
   "archived","boolean","Whether the post is archived. Archived posts cannot be commented on, but the author can still edit the OP."
   "no_follow","boolean",""
   "is_crosspostable","boolean","Whether the post can be crossposted. Will be `false` if the post was removed or deleted."
   "pinned","boolean","Whether the post is pinned to the poster's profile."
   "over_18","boolean","Whether the submission has been marked as NSFW."
   "preview?","object","This field is not available if the post was removed or deleted.
   This field is not available if the post is a text post.

   Example for a link post to www.yahoo.com::

      {'images': [{'source': {'url': 'https://external-preview.redd.it/1O1L_JB_3AH6D6LQ-sG0z4Xw3m5w9giImtFik6wLJs0.jpg?auto=webp&s=09218c9750baa74ba3af4f892ae6b67e30677927',
                            'width': 500,
                            'height': 500},
                 'resolutions': [{'url': 'https://external-preview.redd.it/1O1L_JB_3AH6D6LQ-sG0z4Xw3m5w9giImtFik6wLJs0.jpg?width=108&crop=smart&auto=webp&s=f8f365f35593a8ff5a4345f6ac61b70cfef15e52',
                                  'width': 108,
                                  'height': 108},
                                 {'url': 'https://external-preview.redd.it/1O1L_JB_3AH6D6LQ-sG0z4Xw3m5w9giImtFik6wLJs0.jpg?width=216&crop=smart&auto=webp&s=4db450c618f53c6c33778e43b211fad788e7e62a',
                                  'width': 216,
                                  'height': 216},
                                 {'url': 'https://external-preview.redd.it/1O1L_JB_3AH6D6LQ-sG0z4Xw3m5w9giImtFik6wLJs0.jpg?width=320&crop=smart&auto=webp&s=a3493dedbabed68d15d63888f37945dedec7d2af',
                                  'width': 320,
                                  'height': 320}],
                 'variants': {},
                 'id': '16jxFHXnGLmDKC4M3Q9uMUZyOARBNVxPEqecC4TMIC0'}],
     'enabled': False}

   Example for an image post::

      {'images': [{'source': {'url': 'https://preview.redd.it/zz2ief0sqj971.gif?format=png8&s=0813b3075fe7dd364491a91b81dd96f5d003b1e5',
                               'width': 200,
                               'height': 136},
                    'resolutions': [{'url': 'https://preview.redd.it/zz2ief0sqj971.gif?width=108&crop=smart&format=png8&s=f8cd04f4c3810209c3742bc5c3dc0ac2e9105e9f',
                                     'width': 108,
                                     'height': 73}],
                    'variants': {'gif': {'source': {'url': 'https://preview.redd.it/zz2ief0sqj971.gif?s=0be13dfc903efbe51d655a6db6403fc9fd11465b',
                                                    'width': 200,
                                                    'height': 136},
                                         'resolutions': [{'url': 'https://preview.redd.it/zz2ief0sqj971.gif?width=108&crop=smart&s=e57bd0324bd02bcaaf194181ee4aaf1abc7adfc7',
                                                          'width': 108,
                                                          'height': 73}]},
                                 'mp4': {'source': {'url': 'https://preview.redd.it/zz2ief0sqj971.gif?format=mp4&s=d719eac5958b367bc2e99838b8595d36869898de',
                                                    'width': 200,
                                                    'height': 136},
                                         'resolutions': [{'url': 'https://preview.redd.it/zz2ief0sqj971.gif?width=108&format=mp4&s=52fa7201ccad66f04a6ed435405e6f412fb36a20',
                                                          'width': 108,
                                                          'height': 73}]}},
                    'id': 'zPq0TcenApl-k727IqB4zWhcVz5H6JwrszBJ2ClEzAU'}],
        'enabled': True}

   Example for a video post::

      {'images': [{'source': {'url': 'https://external-preview.redd.it/DEHoxCSwTpIlX-Bzp699jKX2qR-1cdBoucdcs2YEPjY.png?format=pjpg&auto=webp&s=1ac508e374e6cbcab5b7e52f3e045131bf376ac2',
                               'width': 720,
                               'height': 720},
                    'resolutions': [{'url': 'https://external-preview.redd.it/DEHoxCSwTpIlX-Bzp699jKX2qR-1cdBoucdcs2YEPjY.png?width=108&crop=smart&format=pjpg&auto=webp&s=da7df866c43dd7b34f1b39d05eb50ec0065de338',
                                     'width': 108,
                                     'height': 108},
                                    {'url': 'https://external-preview.redd.it/DEHoxCSwTpIlX-Bzp699jKX2qR-1cdBoucdcs2YEPjY.png?width=216&crop=smart&format=pjpg&auto=webp&s=a0a11df22e2e279b675ee3a00ad2cb608d6dce12',
                                     'width': 216,
                                     'height': 216},
                                    {'url': 'https://external-preview.redd.it/DEHoxCSwTpIlX-Bzp699jKX2qR-1cdBoucdcs2YEPjY.png?width=320&crop=smart&format=pjpg&auto=webp&s=db4f66be5c1a32fd2bf9fba9a9162c472b2a7d30',
                                     'width': 320,
                                     'height': 320},
                                    {'url': 'https://external-preview.redd.it/DEHoxCSwTpIlX-Bzp699jKX2qR-1cdBoucdcs2YEPjY.png?width=640&crop=smart&format=pjpg&auto=webp&s=03c092d24defa4290babcd0284ba7bdc3afcbc8e',
                                     'width': 640,
                                     'height': 640}],
                    'variants': {},
                    'id': 'rSGWbcTwMb_0RzD2Ms9DqNQ6aIF_j5joM9C3fVgPR-I'}],
        'enabled': False}
   "
   "all_awardings","object array",""
   "awarders","unknown array",""
   "media_only","boolean",""
   "can_gild","boolean",""
   "spoiler","boolean","Whether the post is marked as a spoiler."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "visited","boolean",""
   "removed_by","string?","The name of the redditor who removed this post. `null` if not removed or the current user is not a moderator of the subreddit."
   "distinguished","string?","`null` if not distinguished, otherwise `"moderator"` or `"admin"`."
   "subreddit_id","string","The full ID36 of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "mod_reason_by","unknown?",""
   "removal_reason","unknown?",""
   "id","string","The ID of the submission (without the `t3_` prefix). Also see `name`."
   "is_robot_indexable","boolean","Will be `false` if the post was removed or deleted."
   "author","string","The redditor name. Possibly `[removed]` if the post was removed
   or `[deleted]` if the post was removed by the author."
   "discussion_type","unknown?",""
   "num_comments","integer","The number of comments. May not match the number of visible comments."
   "send_replies","boolean","Whether an inbox message will be sent to you when the submission receives a new top-level comment."
   "whitelist_status","string?","Known values: `no_ads`."
   "parent_whitelist_status","string?","Known values: `no_ads`."
   "contest_mode","boolean","Whether the post is in contest mode or not."
   "permalink","string","The URI of the post without the domain.
   E.g., `/r/IAmA/comments/erd8si/i_was_born_with_two_y_chromosomes_ama/`"
   "stickied","boolean","Whether the post is a 'stickied' post in the subreddit."
   "url","string","If a text post, it is the url of the submission. If a link post,
   it is the url of the link. If `url_overridden_by_dest` field exists, this will be the same value as it.

   Also see `permalink`, which is the same as this field but the path only."
   "subreddit_subscribers","integer","The number of subscribers in the subreddit."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "num_crossposts","integer","Crosspost count."
   "is_video","boolean","True if is is a video (including video gif) post. Otherwise, false.

   This is false if the post is a crosspost to a video post."
   "spam?","boolean","`true` if the submission was removed as spam else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "approved?","boolean","`true` if the submission is approved.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "rte_mode?","string","Either `markdown` or `richtext`.

   Field not available if the post does not belong to the current user.
   Field not available if no user context is available."
   "url_overridden_by_dest?","string","The url of the linked item for the link post.

   The URL of the image if an image post.

   The URL of the video if a video post.

   The URL of the gallery for a gallery post. E.g., `https://www.reddit.com/gallery/oexfaq`.

   In rare cases the URL may be a path, for example, see link post `j74mzm`.

   Field does not exist if not a link post."
   "event_start?","float","Unix timestamp of when the post's event time begins. Key does not exist if
   there is no event metadata on the post. The float is always a whole number.

   When an event is started early this field gets updated."
   "event_end?","float","Unix timestamp of when the post's event time ends. Key does not exist if
   there is no event metadata on the post. The float is always a whole number."
   "event_is_live?","boolean","`true` if the event is live (event is happening now), `false` if not. Field does not exist if there is no event info."
   "is_followed?","boolean","`true` if the event is being followed by the current user.
   Field does not exist if the event is not being followed or there is no user context."
   "author_flair_background_color",".","See same field in Comment schema."
   "author_flair_css_class",".","See same field in Comment schema."
   "author_flair_richtext?",".","See same field in Comment schema."
   "author_flair_type?",".","See same field in Comment schema."
   "author_flair_template_id",".","See same field in Comment schema."
   "author_flair_text",".","See same field in Comment schema."
   "author_flair_text_color",".","See same field in Comment schema."
   "author_patreon_flair?",".","See same field in Comment schema."
   "link_flair_background_color","string","Submission flair's background color hex. E.g., `#46d160`. Empty string if flair has no background color."
   "link_flair_css_class","string?","Post flair CSS class.

   Empty string if flair is configured and no CSS class is set.

   Value `null` if flair not configured."
   "link_flair_richtext","unknown array",""
   "link_flair_text","string?","Post flair text.

   Value `null` if flair not configured."
   "link_flair_text_color","string","Values: `dark`, `light`.

   Starts as `dark`. If no flair set then `dark` is used."
   "link_flair_type","string","Values: `text`, `richtext`."
   "link_flair_template_id?","string","The link flair UUID.

   Field not available if flair not configured.

   Field not available if the post was removed or deleted."
   "crosspost_parent?","string","The full ID36 of the crosspost parent submission.

   This field does not exist if the post is not a crosspost."
   "crosspost_parent_list?","array of submission objects",""
   "ignore_reports?",".","See same field on :ref:`Comment Schema <comment_schema>`"
   "num_reports",".","See same field on :ref:`Comment Schema <comment_schema>`"
   "user_reports",".","See same field on :ref:`Comment Schema <comment_schema>`"
   "mod_reports",".","See same field on :ref:`Comment Schema <comment_schema>`"
   "report_reasons",".","See same field on :ref:`Comment Schema <comment_schema>`"

Actions
-------

.. _get_api_info:

Get
~~~

.. http:get:: /api/info

*scope: read*

Return Submission, Comment, and Subreddit resource info.

The `id` parameter will take up to 100 IDs.
Any ID not found will be ignored.
Alphabetic characters in the ID must be lowercase or they will be ignored.
If more than 100 IDs are given, all IDs are ignored.
Duplicates are ignored.

The `sr_name` parameter will take up to 100 names.
Any ID not found will be ignored.
Names are case-insensitive.
If more than 100 names are given, the first 100 are used and the rest are ignored.
Duplicates are ignored.

The `id` and `sr_name` parameters can be used together for a maximum output of 200 items.

The input order will not be the same as the output order. The output order is seemingly random
and differs each time.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","A comma-separated list of full ID36s."
   "sr_name","string","A comma-separated list of subreddit names."
   "url","string","a valid URL"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_info


Upload Media
~~~~~~~~~~~~

.. http:post:: /api/media/asset

Upload media for use in submissions.

The upload process is similar to that of flair emoji image uploads
and the details for that are already documented :ref:`here <emoji_upload>`.
Th returned object structure is just slightly different.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "filepath","string","The file name (base name, not a full path) of the image file to upload.
   Example: `image.png`."
   "mimetype","string","The mimetype of the image file to upload. It does not have to match the
   extension of the `filepath`. Example: `image/png`."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The `filepath` or `mimetype` form parameter was not specified or the value was empty.

   * Invalid value specified for `mimetype`, or the type is not supported."


Create Post
~~~~~~~~~~~

Text
^^^^

Link
^^^^

Image
^^^^^

Video
^^^^^

.. _post_api_submit:

.. http:post:: /api/submit

*scope: submit*

Compose a new text or link submission to a subreddit.

Specify the target subreddit with `sr` and title `title`.

To create a text post, use `kind: self`. A text post ("self-post") is created with `text` or `richtext_json`
used as the text body. An `INVALID_SELFPOST` error is returned if both are specified.

To create a link post, use `kind: link`. A link post is created with `url` as the link.

To create an image post, use `kind: image`. A image post is created using `url` as the image.

Return object example for text, link, and image posts::

   {"json": {"errors": [], "data": {"url": "https://www.reddit.com/r/Pyprohly_test3/comments/om0nwf/my_title/", "drafts_count": 0, "id": "nxaraz", "name": "t3_nxaraz"}}}

Return object example for video posts::

   {"json": {"errors": [], "data": {"websocket_url": "wss://ws-0c2fc51946b39365a.wss.redditmedia.com/i2arnoco52c71?m=AQAASr_0YNe2OENAgcxRDFT6lNowcSPjOboA1bfLsYXZUzts20rI"}}}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "kind","string","Either: `link`, `self`, `image`, `video`, `videogif`. Default: `link`."
   "sr","string","The subreddit name in which to submit to."
   "title","string","Title of the submission. Up to 300 characters long."
   "text","string","The markdown text for a text post."
   "url","string","A valid URL, for a link post."
   "sendreplies","boolean","Receive inbox notifications for replies. Default: true."
   "spoiler","boolean","Mark as spoiler. Default: false."
   "nsfw","boolean","Mark as NSFW. Default: false."
   "original_content","boolean","Mark as original content. Default: false."
   "collection_id","string","The UUID of a collection to add this post to a collection.
   Parameter ignored if empty string."
   "video_poster_url","string","The URL of the thumbnail for a video post. Required when `kind: video`."
   "flair_id","string","A string no longer than 36 characters.
   Parameter ignored if empty string."
   "flair_text","string","A string no longer than 64 characters.
   Parameter ignored if empty string."
   "event_end","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_start","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_tz","string","A pytz timezone e.g. `America/Los_Angeles`.
   Parameter ignored if empty string."
   "ad","boolean","Setting to true appears to post the submission unlisted, accessible only by URL."
   "extension","string","Used for determining which view-type (e.g. `json`, `compact` etc.) to use for the redirect that is generated if the resubmit error occurs."
   "resubmit","boolean","When the 'Restrict how often the same link can be posted' content control setting
   is enabled, if a link with the same URL has already been submitted then an `ALREADY_SUB` API error would
   be returned unless this field is `true`.

   Default: false."
   "richtext_json","string","A string of RTJSON."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "BAD_SR_NAME","the `sr` field, subreddit name, isn't given"
   "SUBREDDIT_NOEXIST","the specified subreddit doesn't exist"
   "SUBREDDIT_NOTALLOWED","you don't have permission to post to the subreddit.
   Quarantined subreddits can be posted to, even if you haven't yet opt-ed in to viewing its content."
   "INVALID_OPTION","the option specified in the `kind` field isn't valid."
   "NO_TEXT","no `title` was specified, is blank, or contains only whitespace"
   "NO_URL","the `url` field isn't given or is too garbled"
   "JSON_PARSE_ERROR","the `richtext_json` value is not in the correct JSON format"
   "INVALID_SELFPOST","both `text` and `richtext_json` were specified"
   "TOO_LONG","the `title` or `text` is too long"
   "NO_SELFS","the subreddit doesn't allow text posts"
   "MISSING_VIDEO_URLS","The `video_poster_url` was empty or not specified when a video post is being made.

   *\"This community requires a video link and a post link\"* -> url"
   "ALREADY_SUB","The given link has already been submitted to the subreddit.

   *\"This community doesn't allow links to be posted more than once, and this link has already been shared\"* -> url"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","The subreddit is private/banned."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_submit


Gallery
^^^^^^^

.. http:post:: /api/submit_gallery_post

*scope: submit*

Submit a gallery post.

This endpoint expects JSON data, unlike `POST /api/submit`.

Return object example::

   {
       "json": {
           "errors": [],
           "data": {
               "url": "https://www.reddit.com/r/Pyprohly_test3/comments/oexfaq/my_gallery/",
               "id": "t3_oexfaq"
           }
       }
   }

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "title",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "items","object array","The gallery items.

   Example::
      [
         {
           "caption": "pepperoonie",
           "outbound_url": "www.google.com",
           "media_id": "zpkqrrfo3m971"
         },
         {
           "caption": "nothing you cant do",
           "outbound_url": "https://www.google.com",
           "media_id": "qg54xsfo3m971"
         }
      ]
   "
   "sendreplies",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "spoiler",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "nsfw",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "original_content",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "collection_id","string","The UUID of a collection to add this post to a collection.
   Parameter ignored if empty string."
   "flair_id","string","A string no longer than 36 characters.
   Parameter ignored if empty string."
   "flair_text","string","A string no longer than 64 characters.
   Parameter ignored if empty string."
   "event_end","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_start","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_tz","string","A pytz timezone e.g. `America/Los_Angeles`.
   Parameter ignored if empty string."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "placeholder","The gallery must contain more than one entry.

   *\"List is too short.\"* -> items"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","JSON data was not provided."


Poll
^^^^

.. http:post:: /api/submit_poll_post

*scope: submit*

Submit a poll post.

This endpoint expects JSON data.

Return object example::

   {
       "json": {
           "errors": [],
           "data": {
               "url": "https://www.reddit.com/r/Pyprohly_test3/comments/of0f7u/poll/",
               "id": "t3_of0f7u"
           }
       }
   }

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "title",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "text",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "options","string array","The poll options.

   Example::
      [
        "apple",
        "orange",
        "bacon"
      ]
   "
   "duration","integer","The number of days the poll runs for.

   Valid values are 1 to 7. If a number is specified outside this range it is clamped within range.

   This field is required. The UI default is 3 days.
   "
   "sendreplies",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "spoiler",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "nsfw",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "original_content",".","Same as in :ref:`POST /api/submit <post_api_submit>`."
   "collection_id","string","The UUID of a collection to add this post to a collection.
   Parameter ignored if empty string."
   "flair_id","string","A string no longer than 36 characters.
   Parameter ignored if empty string."
   "flair_text","string","A string no longer than 64 characters.
   Parameter ignored if empty string."
   "event_end","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_start","string","A datetime string e.g. `2018-09-11T12:00:00`.
   Parameter ignored if empty string."
   "event_tz","string","A pytz timezone e.g. `America/Los_Angeles`.
   Parameter ignored if empty string."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "JSON_PARSE_ERROR","JSON data was not provided.

   *\"Sorry, something went wrong. Double-check things and try again.\"* -> json"
   "TOO_FEW_OPTIONS","*\"you need at least 2 poll options\"* -> options"
   "placeholder","The duration parameter was not specified.

   *\"Missing value\"* -> duration"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","The `options` parameter was not specified."


.. _post_api_del:

Delete
~~~~~~

.. http:post:: /api/del

*scope: edit*

Delete a Comment or Submission.

This endpoint does not produce any kind of return value. If the target doesn't exist or isn't valid,
nothing happens.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","The full ID36 of a comment or submission."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_del


.. _post_api_editusertext:

Edit Body
~~~~~~~~~

.. http:post:: /api/editusertext

*scope: edit*

Edit the body text of a text post or comment.

The target entity (with the new body text) is returned in a listing structure,
unless `return_rtjson` is truthy in which case it is not wrapped in a listing.

If `text` and `richtext_json` are used together `richtext_json` will be used.

Editing a richtext post with `text` a markdown post with `richtext_json` or vice versa
will only sometimes switch the `rte_mode` from `markdown` or `richtext`.
I don't know what the criteria is :P.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "thing_id","string","Full ID36 of a comment or text post"
   "text","string","Markdown text"
   "richtext_json","string","A string of RTJSON"
   "return_rtjson","boolean","If truthy (a string that starts with `0` or `F` or `f` is treated as falsy),
   return the entity object as the top level JSON object."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "NO_THING_ID","`thing_id` field wasn't given or the ID doesn't exist"
   "placeholder","The submission specified by `thing_id` isn't a text post and can't be edited.

   *\"placeholder: This post can't be edited\"* -> text"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_editusertext


.. _post_api_lock:

Lock
~~~~

.. http:post:: /api/lock
.. http:post:: /api/unlock

*scope: modposts*

Lock a comment or submission.

Locking prevents the submission/comment from receiving new comments.
Nothing happens if the target is already locked.

https://www.reddit.com/r/modnews/comments/brgr8i/
moderators_you_may_now_lock_individual_comments/

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","the full ID36 of a comment or submission"

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","Something went wrong. The full ID36 doesn't exist, you don't have permission to lock the target, etc."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_lock


.. _post_api_vote:

Vote
~~~~

.. http:post:: /api/vote

*scope: vote*

Cast a vote on a Submission or Comment.

`dir` is the direction of the vote:

* `1`: upvote
* `0`: un-vote
* `-1`: downvote

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","full ID36 of a Submission or Comment"
   "dir","integer or string","vote direction. one of `1`, `0`, or `-1`"
   "rank","integer","unknown purpose"

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","No `id` was given or the target could not be found."
   "500","* `dir` was not specified.

   * A non-integer argument is specified for `dir`."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_vote


.. _post_api_save:

Save
~~~~

.. http:post:: /api/save
.. http:post:: /api/unsave

*scope: save*

Save a Submission or Comment.

Returns an empty JSON object.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","The full ID36 of a submission or comment."
   "category","string","A category name. Requires Reddit Premium. Ignored if no Reddit Premium."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The category name specified was invalid."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_save


Hide
~~~~

.. http:post:: /api/hide
.. http:post:: /api/unhide

*scope: report*

Hide a submission.

If *any* of the list of submission IDs don't exist then the endpoint will
return a HTTP 400 status error and none of the submissions will be hidden.
This can be annoying since if the list is long it can be hard to tell which
ID is the culprit.

As a recommendation, clients should provide no more than 300 IDs at a time.

Returns an empty JSON object.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","A comma-separated string of submission full ID36s."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","* The `id` parameter was not specified.

   * The value specified for `id` was empty.

   * If any of the `id`\ s specified were not found."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_hide


.. _post_api_marknsfw:

Mark NSFW
~~~~~~~~~

.. http:post:: /api/marknsfw
.. http:post:: /api/unmarknsfw

*scope: modposts*

Mark a Submission as NSFW.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a Submission."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","you do not have mod privileges to mark the target"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_marknsfw


.. _post_api_spoiler:

Mark Spoiler
~~~~~~~~~~~~

.. http:post:: /api/spoiler
.. http:post:: /api/unspoiler

*scope: modposts*

Mark a Submission as spolier.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a Submission."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","you do not have mod privileges to mark the target"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_spoiler


.. _post_api_distinguish:

Distinguish
~~~~~~~~~~~

.. http:post:: /api/distinguish

*scope: modposts*

Distinguish a Submission or Comment by decorating the author's name:
giving it a different color, and putting a sigil beside it.

Only moderators of the subreddit can do this. This can be useful to draw attention to and
confirm the identity of the user in the context of their submission/comment.

Distinguish options:

* `yes` - **moderator** distinguish (`[M]`). Green text.
   The target submission/comment's author must be a moderator of the subreddit the submission/comment is in.
* `admin` - **admin** distinguish (`[A]`). Red text. Only admin accounts can do this.
* `no` - remove distinguishes.
* `special` - add a user-specific distinguish... ???

The first time a top-level comment is moderator distinguished the author
will get a notification in their inbox linking to the comment.

`sticky` is a boolean flag for comments, which will stick the distingushed comment to the top of all comments threads.
Only one comment may be stickied at a time. If a comment is marked sticky when
there is already a stickied comment it will override that stickied comment.
Only top-level comments may be stickied.

The target entity is returned in a listing structure.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a Submission or Comment."
   "how","string","One of `yes`, `admin`, `no`, `special`. Error if not specified."
   "sticky","boolean","Make a comment stickied to the top of the thread. Default false."

|

.. csv-table:: API Errors
   :header: "Error","Variant","Description"
   :escape: \

   "USER_REQUIRED","2","you must login"
   "COMMENT_NOT_STICKYABLE","1","The target comment can't be stickied because it is not a top-level comment.

   *\"This comment is not stickyable. Ensure that it is a top level comment.\"*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","If `sticky` was specified and is `true` (or a truthy value) and `id` refers to submission rather than a comment."
   "403","The `how` parameter was not given, was of an invalid value, or you do not have the right mod privileges."
   "404","No `id` was given or the target could not be found."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_distinguish


Set Sticky
~~~~~~~~~~

.. http:post:: /api/set_subreddit_sticky

*scope: modposts*

Set or unset a Submission as sticky, either in its subreddit or to your user profile.

Stickied posts are pinned to the top of the subreddit in the default 'hot' listing.
On a user profile, they show as a pinned post at the top of the listing.

The `num` argument is used when stickying (i.e., `state` is true). It specifies
which position the post is to be placed in the existing list of stickied posts.
If a stickied post is already occupying that position, it will be **replaced** (the post
in that position will be unsticked).
In a subreddit, there can be 2 sticked posts at a time, `num` can be either `1` or `2`.
On a user profile, there can be 4 sticked posts at a time, `num` can be from `1` to `4`.
If a number is specified outside a range, it will be clamped.

When stickying and `num` is not specified:

* When subreddit stickying, the post will be appended to the **bottom** of the sticky list.
  If the list is full then the bottom-most post will be **replaced**.
* When user profile stickying, the post will be added to the **top** of the sticky list.
  If the list is full then the bottom-most post will be **evicted**, like a queue.

Stickying a post that is already stickied causes a 409 (Conflict) HTTP error.
Unstickying a post that isn't stickied does nothing.

If `state` is not specified then it is assumed to be `false` and the post will be unstickied.

You cannot reorder sticky posts directly. You must unsticky them then re-sticky them.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a Submission."
   "state","boolean","True to sticky, false to unsticky. Default false."
   "num","integer","An integer position. Ignored if `state` is false."
   "to_profile","boolean","If true, sticky the post to your user profile instead of its subreddit."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","You do not have permission to sticky that post."
   "409","You are trying to sticky a post that is already stickied."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_subreddit_sticky


Set Contest Mode
~~~~~~~~~~~~~~~~

.. http:post:: /api/set_contest_mode

*scope: modposts*

Set or unset "contest mode" for a submission's comments.

In contest mode, upvote counts are hidden and comments are displayed in a random order.

If `state` is not specified, `false` is assumed.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a Submission."
   "state","boolean","Whether to enable (true) or disable (false) contest mode."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","ID not found, or you do not have permission to enable/disable contest mode for this post."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_contest_mode


Set Suggested Sort
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/set_suggested_sort

*scope: modposts*

Set or unset the suggested sort for a submission's comments.

When set, all redditors will see comments in the suggested sort by default.
They can still manually change back to their preferred sort if they choose.

If `sort` is `blank`, not given, or an unknown value, the suggested sort will be unset.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","full ID36 of a Submission"
   "sort","string","one of `confidence`, `top`, `new`, `controversial`, `old`, `random`, `qa`, `live`, `blank`"

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","ID not found, or you do not have permission to set the suggestd sort for this post"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_suggested_sort


.. _post_api_sendreplies:

Set Inbox Replies
~~~~~~~~~~~~~~~~~

.. http:post:: /api/sendreplies

*scope: edit*

Enable or disable inbox replies for a Submission or Comment.

If `state` is not provided, `true` (enable) is assumed.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","A full ID36 of a Submission or Comment."
   "state","boolean","Whether to enable or disable inbox replies."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_sendreplies


Set Event Time
~~~~~~~~~~~~~~

.. http:post:: /api/event_post_time

*scope: modposts*

Add or modify post event times.

The datetimes provided must not contain milliseconds otherwise a `BAD_TIME` API error is returned.

Specify only `event_start` to change only the starting date.
The same cannot be done for `event_end`, a 500 HTTP error will occur.

If both `event_start` and `event_end` are specified then the `event_start` must be before `event_end`
otherwise a `MIN_EVENT_TIME` API error is returned.
It's possible however to make a second request specifying only `event_start` to modify the start date
so that `event_start` is after `event_end`. If this happens then the time difference can be longer than
7 days.

The endpoint returns a JSON object containing the Unix timestamps of the start and end times of the event.
It's a bit odd that the Unix timestamps are in milliseconds given that the the endpoint does not accept
date time strings with millisecond information. Also, the `event_start` and `event_end` fields of submission object are in seconds. Perhaps it's a good idea to ignore the output of this endpoint.

Returned object example::

   {"event_is_live": false, "event_start": 1623381648000, "event_end": 1623392449000}

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a post."
   "event_start","string","A datetime in ISO 8601 format. E.g., `2018-09-11T12:00:00`.

   If value is empty the parameter is ignored."
   "event_end","string","A datetime in ISO 8601 format. E.g., `2018-09-11T12:00:00`.

   If value is empty the parameter is ignored."
   "event_tz","string","A timezone. E.g., `America/Los_Angeles`.

   If not specified, defaults to `UTC`."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "BAD_TIME","* The value specified for `event_start` or `event_end` is in a bad format.

   * The date string specified for `event_start` or `event_end` is in the past.

   Note that this error will always indicate `event_start` is wrong even if its `event_end` that needs fixing.

   \"This time is invalid\" -> event_start"
   "INVALID_TIMEZONE","*\"This timezone is invalid\"* -> *event_tz*"
   "MAX_EVENT_TIME","*\"This event can't be longer than 7 days\"* -> *event_end*"
   "MIN_EVENT_TIME","*\"This event must last at least 30 minutes\"* -> *event_end*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","The `event_start` parameter was not specified."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_event_post_time


Follow post event
~~~~~~~~~~~~~~~~~

.. http:post:: /api/follow_post

*scope: subscribe*

Follow or unfollow a post event.

Followers will receive a push notification when the event starts.

Returns an empty JSON object on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "fullname","string","The full ID36 of a submission."
   "follow","boolean","True to follow, false to unfollow. Default: false."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","   *Please log in to do that.*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","The submission specified by the `fullname` parameter is not an event."
   "404","The submission specified by the `fullname` parameter does not exist."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_follow_post


.. _post_api_approve:

Approve
~~~~~~~

.. http:post:: /api/approve

*scope: modposts*

Approve a post or comment.

A removed target can be approved. If so it will be re-inserted into appropriate listings and
any reports on the approved thing will be discarded.

A removed post's attributes will change as follows:

.. csv-table:: Object attribute changes
   :header: "Field","Description"
   :escape: \

   "removed","Resets to `false`."
   "removed_by_category","Resets to `null`."
   "banned_by","Resets to `null`."
   "banned_at_utc","Resets to `null`."
   "ban_note","Field no longer exists."
   "spam","Resets to `false`."
   "is_crosspostable","Resets to `true`."
   "is_robot_indexable","Resets to `true`."

Approving a post/comment affects it's attributes:

.. csv-table:: Object attribute changes
   :header: "Field","Description"
   :escape: \

   "approved","Becomes `true`. (Value starts as `false`.)"
   "approved_by","Name of the redditor who approved. (Value starts as `null`.)"
   "approved_at_utc","The unix timestamp of when the item was approved. (Value starts as `null`.)"

Returns an empty JSON object on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a post or comment."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","* The target specified by the `id` parameter does not belong to a subreddit you have permission to approve.

   * The `id` parameter was not specified."


.. _post_api_remove:

Remove
~~~~~~

.. http:post:: /api/remove

*scope: modposts*

As a moderator, remove a post, comment, or modmail message.

Returns an empty JSON object on success.

Removing a post/comment affects its attributes:

.. csv-table:: Object attribute changes
   :header: "Field","Description"
   :escape: \

   "banned_by","Name of the redditor who removed. (Value start as `null`.)"
   "banned_at_utc","The unix timestamp of when the item was removed. (Value starts as `null`.)"
   "ban_note","Ban note.

   Value is `spam` if `spam` parameter was `true`.

   Value is `remove not spam` if `spam` parameter was `false`.

   Value is `confirm spam` if a removal was made with the `spam` parameter as `false` then again with
   the `spam` parameter as `true`. If the order is reversed then the the note will be `remove not spam`.
   "
   "spam","Becomes `true` if `spam` parameter was `true`."

Extra attributes for posts only:

.. csv-table:: Object attribute changes
   :header: "Field","Description"
   :escape: \

   "removed_by_category","The removed by category. It will be `author` even if the remover is a moderator. (Value starts as `null`.)"
   "is_crosspostable","Becomes `false`. (Value starts as `true`.)"
   "is_robot_indexable","Becomes `false`. (Value starts as `true`.)"

|

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a post or comment."
   "spam","boolean","Indicate whether the post should be removed as spam. Default: true."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","* The target specified by the `id` parameter does not belong to a subreddit you have permission to approve.

   * The `id` parameter was not specified."


Report
~~~~~~

.. http:post:: /api/report

*scope: report*

\.\.\.

.. seealso:: https://www.reddit.com/dev/api/#POST_api_report


Report award
~~~~~~~~~~~~

.. http:post:: /api/report_award

*scope: report*

\.\.\.

.. seealso:: https://www.reddit.com/dev/api/#POST_api_report_award


.. _submission_ignore_reports:

Ignore reports
~~~~~~~~~~~~~~

.. http:post:: /api/ignore_reports
.. http:post:: /api/unignore_reports

*scope: modposts*

Prevent future reports on a post/comment from causing notifications.

Ignoring reports will not cause notifications or make the ignored thing show up in the various moderation listings.

Returns `{}` on success. If the target is already ignored/unignored it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","The full ID36 of a post or comment (prefixed with `t3_` or `t1_`)."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","A user context is required."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The `id` parameter was not specified.

   * The target specified by `id` was not found, or points to an item you are not a moderator of."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_ignore_reports
