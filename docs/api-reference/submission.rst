
Submission
==========

Overview
--------

There are different post types: `text`, `link`, `gallery`, `poll`, `crosspost`.

Use the following checks to distinguish the post type. The order of the checks is significant.

* `gallery`: ``d.get('is_gallery', False)``
* `poll`: ``'poll_data' in d``
* `crosspost`: ``'crosspost_parent' in d``
* `text`: ``d['is_self']``
* `link`: ``'url_overridden_by_dest' in d``

To determine the type of a crosspost you must lookup the post type of the submission in `crosspost_parent`.
This does not have to be done recursively because when you crosspost a crosspost the `crosspost_parent` will be
the original post and not the crosspost you've crossposted.


.. _submission-schema:

Schema
~~~~~~

.. csv-table:: Submission Object
   :header: "Field","Type (hint)","Description"
   :widths: 8, 6, 30

   "approved?","boolean","`true` if the submission is approved.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "approved_at_utc","integer?","Unix time when the comment was approved. `null` if not approved or the current user is not a moderator of the subreddit."
   "approved_by","string?","The name of the redditor who approved this post. `null` if not approved or the current user is not a moderator of the subreddit."
   "subreddit","string","The subreddit name. E.g., `IAmA`"
   "selftext","string","The body text of the submission. Empty string if it is not a text or poll post."
   "selftext_html?","string?","The HTML of the post. This will be null if it is not a text or poll post.

   This key will not exist if the object was returned from `POST /api/editusertext`."
   "author_fullname?","string","The full ID36 of the author.

   This attribute is not available if the post was removed or deleted."
   "saved","boolean","Whether the authenticated user has saved this post.

   For clients with no user context this will always be `false`."
   "gilded","integer",""
   "clicked","boolean",""
   "title","string","The title of the post."
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "hidden","boolean",""
   "downs","integer","Always `0`."
   "thumbnail","string","The post thumbnail as seen in listings.

   When retrieving posts from a listing, the value can sometimes be `image` instead of a URL.

   Value is `default` if the post was removed.

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
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited."
   "gildings","unknown object",""
   "post_hint?","string","The type of post.

   Known values: `self`, `link`, `image`, `hosted:video`, `rich:video`.

   Field does not exist if it is a gallery post. Use the `is_gallery` field instead to determine a gallery post.

   This field does not exist if the `preview` field does not exist. This means this field is not available if
   the post was removed or deleted."
   "is_gallery?","boolean","True if a gallery post.

   This field does not exist if it is not a gallery post. (Hence value should always be true.)"
   "gallery_data?","object","
   Contains information about the gallery items, including captions and link URLs.
   Use the `media_id` in the `media_metadata` field object to get more information about the media items.

   This field does not exist if not a gallery post. This field can be `null` even if `is_gallery` is true.

   The object will have one key, `items`, whose value is an array of gallery item objects.

   Gallery item fields:

   * `id` (integer): Gallery item ID.
   * `media_id` (string): The media ID. Use this to look up more information about the media using the
     `media_metadata` field on the submission object.
   * `caption` (?string): The gallery item caption. Field will not exist if image has no caption.
   * `outbound_url` (?string): An outbound link for the gallery item. Field will not exist if image has no outbound link.
   "
   "media_metadata?","object","Information about media items linked in the post.

   Includes information for image URLs, image file types, and their dimensions.

   This field is only available if the post type is a text post or gallery post.
   If a text post this field will not be present if there is no media in the post.

   Schema:

   * *`(root)`* (object (mapping[string, string])): The keys are media IDs and the values are objects.

     Value sub-object fields:

     - If `status: failed`:

       * `status` (string): `failed`.

     - If `status: valid`:

       * `status` (string): `valid`.
       * `e` (string): `Image` (when `m: image/jpg` or `m: image/png`) or `AnimatedImage` (when `m: image/gif`).
       * `m` (string): Either: `image/jpg`, `image/png`, or `image/gif`.
       * `p` (object array): Array of image previews at different sizes.

         Sub-object fields:

         * `x` (integer): Width of the image.
         * `y` (integer): Height of the image.
         * `u` (string): URL of the image.

       * `s` (object): 'Source'.

         - If `e: Image`:

           * `x` (integer): Width of the image.
           * `y` (integer): Height of the image.
           * `u` (string): URL of the image.

         - If `e: AnimatedImage`:

           * `x` (integer): Width of the image.
           * `y` (integer): Height of the image.
           * `gif` (string): URL to the original image.
           * `mp4` (string): URL to an mp4 version of the original image.

       * `id` (string): The media ID.
   "
   "poll_data?","object","This field does not exist if not a poll post."
   "content_categories","string array?",""
   "is_self","boolean","True if a text post or poll post.

   This field will be false if the post is a crosspost to a text post."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "wls","integer?","Unknown. Often `6`. Possibly stands for ""white list status""?"
   "pwls","integer?","Unknown. Possibly stands for ""parent white list status""?"
   "removed?","boolean","`true` if the submission is removed.

   This will not be `true` if the removed post was indicated as spam! It is recommended to check for `null` in
   `removed_by_category` to tell if a post was removed.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "removed_by_category","string?","`null` if not removed, otherwise possible values:
   `author`, `anti_evil_ops`, `community_ops`, `legal_operations`, `copyright_takedown`,
   `reddit`, `user`, `deleted`, `moderator`, `automod_filtered`.

   See `<https://www.reddit.com/r/redditdev/comments/kypjmk/check_if_submission_has_been_removed_by_a_mod/gjpjyw3/>`_.
   "
   "banned_by","string?","The name of the redditor who removed this post. `null` if not removed or the current user is not a moderator of the subreddit.

   This field was named `banned_by` and not `removed_by` probably because there already is a field on the
   submission schema named `removed_by`."
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
   "pinned","boolean","Whether the post is pinned to the poster's profile.
   This attribute will only be true if the submission object was obtained through a user listing."
   "over_18","boolean","Whether the submission has been marked as NSFW."
   "preview?","object","This field is not available if the post was removed or deleted.

   Object structure:

   * `images` (object array):

     * `id` (string): E.g., `FS-vv_FIA3NcZdqmmxMt_xNXUowdvP3AvuTB3_TUH4o`.
     * `source` (object):

       * `url` (string): A link to the original image.
       * `width` (integer): The original image width.
       * `height` (integer): The original image height.

     * `resolutions` (object array): The same image as in `source` but at different resolutions.

       * `url` (string): A link to the image.
       * `width` (integer): The image width.
       * `height` (integer): The image height.

     * `variants` (object mapping): Mapping of string to objects.

   * `enabled` (boolean)
   * `reddit_video_preview` (?object): Not all video posts have this field.

     Example of a post that has this field:
     `https://www.reddit.com/r/gifsthatkeepongiving/comments/qsdg9f/behold_the_mother_of_all_nerf_guns/`.

     Example from post `#qsdg9f`:

     .. code-block:: text

        {'bitrate_kbps': 800,
         'fallback_url': 'https://v.redd.it/abl95wmjm6z71/DASH_360.mp4',
         'height': 360,
         'width': 640,
         'scrubber_media_url': 'https://v.redd.it/abl95wmjm6z71/DASH_96.mp4',
         'dash_url': 'https://v.redd.it/abl95wmjm6z71/DASHPlaylist.mpd',
         'duration': 30,
         'hls_url': 'https://v.redd.it/abl95wmjm6z71/HLSPlaylist.m3u8',
         'is_gif': True,
         'transcoding_status': 'completed'}

   More info: https://www.reddit.com/r/redditdev/comments/39yr53/reddit_change_new_preview_images_available_for/.

   More info: https://www.reddit.com/r/redditdev/comments/5jfk02/api_change_return_image_previews_for_nsfw_posts/.

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
   "total_awards_received","integer","Number of rewards on the post."
   "top_awarded_type","unknown?",""
   "media_only","boolean",""
   "can_gild","boolean",""
   "spoiler","boolean","Whether the post is marked as a spoiler."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "visited","boolean",""
   "removed_by","unknown?",""
   "distinguished","string?","`null` if not distinguished, otherwise `""moderator""` or `""admin""`."
   "subreddit_id","string","The full ID36 of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "removal_reason",".","See `removal_reason` field on the :ref:`Comment schema <comment-schema>`."
   "mod_reason_by",".","See `mod_reason_by` field on the :ref:`Comment schema <comment-schema>`."
   "mod_reason_title",".","See `mod_reason_title` field on the :ref:`Comment schema <comment-schema>`."
   "mod_note",".","See `mod_note` field on the :ref:`Comment schema <comment-schema>`."
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
   it is the url of the link. If the `url_overridden_by_dest` field exists, this will be the same value as it.

   Also see `permalink`, which is the same as this field but the path only."
   "subreddit_subscribers","integer","The number of subscribers in the subreddit."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "is_video","boolean","True if is is a video (including video gif) post. Otherwise, false.

   This is false if the post is a crosspost to a video post."
   "spam?","boolean","`true` if the submission was removed as spam else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "rte_mode?","string","Either `markdown` or `richtext`.

   Field not available if the post does not belong to the current user.
   Field not available if no user context is available."
   "url_overridden_by_dest?","string","The url of the linked item for a link post.

   The URL of the image if an image post.

   The URL of the video if a video post.

   The URL of the gallery for a gallery post. E.g., `https://www.reddit.com/gallery/oexfaq`.

   In rare cases the value may not be a full URL, it can be a path, for example see post ID `j74mzm`.

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
   "is_crosspostable","boolean","Whether the post can be crossposted. Will be `false` if the post was removed or deleted."
   "num_crossposts","integer","Crosspost count."
   "crosspost_parent?","string","The full ID36 of the crosspost original post.

   This field does not exist if the post is not a crosspost."
   "crosspost_parent_list?","object array","If the submission is a crosspost, the array contains one object
   which is the submission of the original post.

   This field does not exist if the post is not a crosspost."
   "ignore_reports?",".","See same field on :ref:`Comment Schema <comment-schema>`"
   "num_reports",".","See same field on :ref:`Comment Schema <comment-schema>`"
   "user_reports",".","See same field on :ref:`Comment Schema <comment-schema>`"
   "mod_reports",".","See same field on :ref:`Comment Schema <comment-schema>`"
   "report_reasons",".","See same field on :ref:`Comment Schema <comment-schema>`"

Actions
-------

.. _get-api-info:

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

   "id","string","A comma-separated list of full ID36s."
   "sr_name","string","A comma-separated list of subreddit names."
   "url","string","a valid URL"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_info


Upload media
~~~~~~~~~~~~

.. http:post:: /api/media/asset

Upload media for use in submissions.

The upload process involves obtaining an upload lease then uploading the
media to the Amazon Simple Storage Service bucket specified in the lease.

Use `POST /api/media/asset` to obtain an upload lease for your media image.
In the response data there will be a field called `action` whose value is a URL but is
missing the `https:` prefix. Prepend `https:` to this URL and add your media image to a field
named `file` in a multipart request, along with the parameters in the `fields` array from the
upload lease as form data in the multipart request.

The `action` is typically `//reddit-uploaded-media.s3-accelerate.amazonaws.com` for this endpoint.
The action endpoint will return XML data. Remember to check for a bad status in the response.
If the media was too large, this endpoint returns 400 Bad Request, and a message indicating this
is included in the XML data.

The media ID is found in `d['asset']['asset_id']` of the lease data.
After uploading your image you can use this ID in submission markdown text as `![img](<media_id> "title")`.

The file name specified by `filepath` doesn't appear to have any significance.
The name of the file when you download it from the site will always be the media ID,
plus the file extension.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "filepath","string","The file name (base name, not a full path) of the image file to upload.
   Example: `image.png`."
   "mimetype","string","The mimetype of the image file to upload. It does not have to match the
   extension of the `filepath`. Example: `image/png`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","A user context is required.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","* The `filepath` or `mimetype` form parameter was not specified or the value was empty.

   * Invalid value specified for `mimetype`, or the type is not supported."


.. _submission-create-post:

Create post
~~~~~~~~~~~

Text
^^^^

Link
^^^^

Image
^^^^^

Video
^^^^^

.. _post-api-submit:

.. http:post:: /api/submit

*scope: submit*

Compose a new text or link submission to a subreddit.

Specify the target subreddit with `sr` and title `title`.

To create a text post, use `kind: self`. A text post ("self-post") is created with `text` or `richtext_json`
used as the text body. An `INVALID_SELFPOST` error is returned if both are specified.

To create a link post, use `kind: link`. A link post is created with `url` as the link.

To create an image post, use `kind: image`. Specify the image URL with `url`.

To create an video post, use `kind: video`. Specify the video URL with `url`. The video thumbnail image must
also be specified using `video_poster_url`.

Return object example for text and link posts::

   {"json": {"errors": [], "data": {"url": "https://www.reddit.com/r/Pyprohly_test3/comments/om0nwf/my_title/", "drafts_count": 0, "id": "nxaraz", "name": "t3_nxaraz"}}}

Return object example for image posts::

   {"json": {"errors": [], "data": {"user_submitted_page": "https://www.reddit.com/user/Pyprohly/submitted/", "websocket_url": "wss://ws-078822fa467f2f8bb.wss.redditmedia.com/rte_images/a0lp5306pmv71?m=AQAA1-Z2Ye5o9vuN_PHYTUdavycbStw62tNSLLjnbqypaYKHuW3G"}}}

Return object example for video posts::

   {"json": {"errors": [], "data": {"websocket_url": "wss://ws-0c2fc51946b39365a.wss.redditmedia.com/i2arnoco52c71?m=AQAASr_0YNe2OENAgcxRDFT6lNowcSPjOboA1bfLsYXZUzts20rI"}}}

.. csv-table:: Form Data or URL Params
   :header: "Field","Type (hint)","Description"

   "kind","string","Either: `link`, `self`, `image`, `video`, `videogif`,
   `crosspost`. Default: `link`."
   "sr","string","The subreddit name in which to submit to. Can be prefixed with `r/` or `/r/`."
   "title","string","Title of the submission. Up to 300 characters long."
   "text","string","The markdown text for a text post."
   "url","string","A valid URL, for a link post."
   "crosspost_parent","string","For when `type: crosspost`, the full ID36 of a submission."
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

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "BAD_SR_NAME","200","The `sr` parameter was not specified.","
   ``{""json"": {""errors"": [[""BAD_SR_NAME"", ""This community name isn't recognizable. Check the spelling and try again."", ""sr""]]}}``
   "
   "SUBREDDIT_NOEXIST","200","The specified subreddit does not exist.","
   ``{""json"": {""errors"": [[""SUBREDDIT_NOEXIST"", ""Hmm, that community doesn't exist. Try checking the spelling."", ""sr""]]}}``
   "
   "SUBREDDIT_NOTALLOWED","200","* You don't have permission to post to the subreddit.

   * You are trying to submit an image or video post to a NSFW subreddit.

   Note, quarantined subreddits can be posted to, even if you haven't yet opt-ed in to viewing its content.","
   ``{""json"": {""errors"": [[""SUBREDDIT_NOTALLOWED"", ""This community only allows trusted members to post here"", ""sr""]]}}``
   "
   "INVALID_OPTION","200","The option specified in the `kind` field isn't valid.","
   ``{""json"": {""errors"": [[""INVALID_OPTION"", ""that option is not valid"", ""sr""]]}}``
   "
   "NO_TEXT","200","The `title` parameter was not specified, was blank, or contained only whitespace.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""title""]]}}``
   "
   "NO_URL","200","`kind: link` and the `url` parameter was not specified, or the URL is invalid.","
   ``{""json"": {""errors"": [[""NO_URL"", ""a url is required"", ""url""]]}}``
   "
   "JSON_PARSE_ERROR","200","`kind: richtext` and the `richtext_json` field was not in the correct JSON format","
   ``{""json"": {""errors"": [[""JSON_PARSE_ERROR"", ""Sorry, something went wrong. Double-check things and try again."", ""richtext_json""]]}}``
   "
   "INVALID_SELFPOST","200","Both the `text` and `richtext_json` parameters were specified.","
   ``{""json"": {""errors"": [[""INVALID_SELFPOST"", ""This request to self-post is invalid"", ""text""]]}}``
   "
   "TOO_LONG","200","* The `title` parameter must be under 300 characters.

   * The `text` parameter must be under 40000 characters.","
   (1): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 300 characters"", ""title""]]}}``

   (2): ``{""json"": {""errors"": [[""TOO_LONG"", ""This field must be under 40000 characters"", ""text""]]}}``
   "
   "NO_SELFS","200","The subreddit doesn't allow text posts.","
   ``{""json"": {""errors"": [[""NO_SELFS"", ""This community doesn't allow text posts"", ""sr""]]}}``
   "
   "MISSING_VIDEO_URLS","200","The `video_poster_url` was not specified, empty, or was an invalid value
   when a video post is being made.","
   ``{""json"": {""errors"": [[""MISSING_VIDEO_URLS"", ""This community requires a video link and a post link"", ""url""]]}}``
   "
   "ALREADY_SUB","200","The given link has already been submitted to the subreddit.","
   ``{""json"": {""errors"": [[""ALREADY_SUB"", ""This community doesn't allow links to be posted more than once, and this link has already been shared"", ""url""]]}}``
   "
   "NO_VIDEOS","200","The subreddit does not have video posting enabled.","
   ``{""json"": {""errors"": [[""ALREADY_SUB"", ""This community doesn't allow videos"", ""sr""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

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

   "sr",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "title",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "items","object array","The gallery items.

   Sub-object fields:

   * `media_id` (string): The media ID.
   * `caption` (?string): A caption.
   * `outbound_url` (?string): An outbound link for the gallery item.

   Empty strings are treated as if the field was not specified. The UI sends empty strings for `caption` and `outbound_url`
   if no value is specified.

   Example::

      [
         {
           ""caption"": ""pepperoonie"",
           ""outbound_url"": ""www.google.com"",
           ""media_id"": ""zpkqrrfo3m971""
         },
         {
           ""caption"": ""nothing you cant do"",
           ""outbound_url"": ""https://www.google.com"",
           ""media_id"": ""qg54xsfo3m971""
         }
      ]

   The array must have more than one item otherwise an API error will occur.

   The `media_id` on each gallery item must be unique otherwise a 500 HTTP error will occur.
   "
   "sendreplies",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "spoiler",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "nsfw",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "original_content",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
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

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "placeholder","200","* The `title` parameter was not specified.

   * The gallery must contain more than one entry.","
   ``{""json"": {""errors"": [[""placeholder"", ""This field cannot be empty."", ""post_metadata.title""], [""placeholder"", ""List is too short."", ""items""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","* JSON data was not provided.

   * The `sr` parameter was not specified.

   * The same `media_id` was used multiple times."


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

   "sr",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "title",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "text",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "options","string array","The poll options.

   Example::

      [
        ""apple"",
        ""orange"",
        ""bacon""
      ]
   "
   "duration","integer","The number of days the poll runs for.

   Valid values are 1 to 7. If a number is specified outside this range it is clamped within range.

   This field is required. The UI default is 3 days.
   "
   "sendreplies",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "spoiler",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "nsfw",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
   "original_content",".","Same as in :ref:`POST /api/submit <post-api-submit>`."
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

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "JSON_PARSE_ERROR","200","JSON data was not provided.","
   ``{""json"": {""errors"": [[""JSON_PARSE_ERROR"", ""Sorry, something went wrong. Double-check things and try again."", ""json""]]}}``
   "
   "placeholder","200","* The `title` parameter was not specified.

   * The `duration` parameter was not specified.","
   ``{""json"": {""errors"": [[""placeholder"", ""This field cannot be empty."", ""post_metadata.title""], [""placeholder"", ""Missing value"", ""duration""]]}}``
   "
   "TOO_FEW_OPTIONS","200","Need at least 2 poll options.","
   ``{""json"": {""errors"": [[""TOO_FEW_OPTIONS"", ""you need at least 2 poll options"", ""options""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","* The `sr` parameter was not specified.

   * The `options` parameter was not specified."


Crosspost
~~~~~~~~~

Use `POST /api/submit` with `type: crosspost` and the `crosspost_parent` parameter.


.. _post-api-del:

Delete
~~~~~~

.. http:post:: /api/del

*scope: edit*

Delete a Comment or Submission.

This endpoint does not produce any kind of return value. If the target doesn't exist or isn't valid,
nothing happens.

When a submission is deleted it's text content (if a text post) will be set to "[deleted]" and the submission
will be unlisted from its subreddit. Users can still otherwise view and reply to deleted to submissions if they
have a direct link to it.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a comment or submission."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_del


.. _post-api-editusertext:

Edit body
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

   "thing_id","string","Full ID36 of a comment or text post"
   "text","string","Markdown text"
   "richtext_json","string","A string of RTJSON"
   "return_rtjson","boolean","If truthy (a string that starts with `0` or `F` or `f` is treated as falsy),
   return the entity object as the top level JSON object."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_THING_ID","200","The `thing_id` parameter wasn't given or the ID doesn't exist.","
   ``{""json"": {""errors"": [[""NO_THING_ID"", ""ID not specified"", ""thing_id""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The submission specified by `thing_id` isn't a text post and can't be edited."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_editusertext


.. _post-api-lock:

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

   "id","string","the full ID36 of a comment or submission"

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","Something went wrong. The full ID36 doesn't exist, you don't have permission to lock the target, etc."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_lock


.. _post-api-vote:

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

   "id","string","full ID36 of a Submission or Comment"
   "dir","integer or string","vote direction. one of `1`, `0`, or `-1`"
   "rank","integer","unknown purpose"

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","No `id` was given or the target could not be found."
   "500","* `dir` was not specified.

   * A non-integer argument is specified for `dir`."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_vote


.. _post-api-save:

Save
~~~~

.. http:post:: /api/save
.. http:post:: /api/unsave

*scope: save*

Save a Submission or Comment.

Returns an empty JSON object.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a submission or comment."
   "category","string","A category name. Requires Reddit Premium. Ignored if no Reddit Premium."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

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

   "id","string","A comma-separated string of submission full ID36s."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","* The `id` parameter was not specified.

   * The value specified for `id` was empty.

   * If any of the `id`\ s specified were not found."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_hide


.. _post-api-marknsfw:

Mark NSFW
~~~~~~~~~

.. http:post:: /api/marknsfw
.. http:post:: /api/unmarknsfw

*scope: modposts*

Mark a Submission as NSFW.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","Full ID36 of a Submission."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* The `id` parameter was not specified.

   * You do not have mod privileges to mark the target"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_marknsfw


.. _post-api-spoiler:

Mark spoiler
~~~~~~~~~~~~

.. http:post:: /api/spoiler
.. http:post:: /api/unspoiler

*scope: modposts*

Mark a Submission as spolier.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","Full ID36 of a Submission."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* The `id` parameter was not specified.

   * You do not have mod privileges to mark the target"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_spoiler


.. _post-api-distinguish:

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

   "id","string","Full ID36 of a Submission or Comment."
   "how","string","One of `yes`, `admin`, `no`, `special`. Error if not specified."
   "sticky","boolean","Make a comment stickied to the top of the thread. Default false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "400","If `sticky` was specified and is `true` (or a truthy value) and `id` refers to submission rather than a comment."
   "403","* The `how` parameter was not specified or was of an invalid value.

   * You do not have permission to modify the target."
   "404","No `id` was given or the target could not be found."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_distinguish


.. _submission-set-sticky:

Set sticky
~~~~~~~~~~

.. http:post:: /api/set_subreddit_sticky

*scope: modposts*

Set or unset a Submission as sticky in its subreddit.

Stickied posts are shown at the top of the subreddit in the default 'Hot' listing.

In a subreddit, there can be at most 2 sticked posts at a time.

When stickying (i.e., `state` parameter is true), the `num` parameter indicates which of the
two positions the new post should occupy. If there is a sticked post in the slot specified by
`num`, it will be replaced. Otherwise the post will be placed in the bottom-most slot.
If the number specified by `num` is outside the valid range it will be clamped within range.

To be more specific, when `num` is specified, if there are fewer sticked posts than the value
specified for `num`, or the parameter is not specified, the new post is placed in the bottom-most
slot. If there is a post already occupying the specified position, it will be replaced (the post
in that position will be unsticked).

If `num` is not specified, the bottom-most slot will be used if available.
If the list is at maximum length, the bottom-most slot will be replaced with the new post.

.. note::
   This behaviour is different for profile pinning which prepends the new post to the top of the list
   and evicts the least recently added post (which is at the bottom of the list).

Stickying a post that is already stickied causes a 409 (Conflict) HTTP error.
Unstickying a post that isn't stickied does nothing.

If `state` is not specified then it is assumed to be `false` and the post will be unstickied.

You cannot reorder sticky posts directly. You must unsticky them then re-sticky them.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a Submission."
   "state","boolean","True to sticky, false to unsticky. Default: false."
   "num","integer","An integer position. Ignored when `state` is false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to sticky that post."
   "409","The post is already stickied."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_subreddit_sticky


Pin to profile
~~~~~~~~~~~~~~

.. http:post:: /api/set_subreddit_sticky

*scope: modposts*

Pin or unpin a post you created to your user profile.

Pinned posts show up at the start of the 'Overview',
or 'Submitted' (old UI) / 'POSTS' (redesign UI) user profile listings.

A user can have at most 4 pinned posts at a time.

The rules for the `num` parameter are the same as in :ref:`subreddit stickying <submission-set-sticky>`.

If `num` is not specified, the new post is inserted at the top of the list.
If the list is at maximum length, least recently pinned post will be evicted.
It acts like a queue.

.. note::
   This feature uses the same endpoint as :ref:`subreddit stickying <submission-set-sticky>`
   but there are stark differences in insertion behaviour when `num` is not specified.
   To summarise these differences:

   * When subreddit stickying: the post will be placed at the **bottom** of the list.
     If the list is full then the bottom-most post will be **replaced**.
   * When user profile pinning: the post will be placed at the **top** of the list.
     If the list is full then the bottom-most post will be **evicted**.

Pinning a post that is already pinned causes a 409 (Conflict) HTTP error.
Unpinning a post that isn't pinned does nothing.

If `state` is not specified then it is assumed to be false and the post will be unpinned.

You cannot reorder pinned posts directly. You must unpin and re-pin them.

This endpoint is the same as for stickying a post in a subreddit.
When `to_profile` is true, the `num` has not effect.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a Submission."
   "to_profile","boolean","Specify a truthy value."
   "state","boolean","True to sticky, false to unsticky. Default: false."
   "num","integer","An integer position. Ignored when `state` is false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","You do not have permission to pin that post."
   "409","The post is already pinned."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_subreddit_sticky


Set contest mode
~~~~~~~~~~~~~~~~

.. http:post:: /api/set_contest_mode

*scope: modposts*

Set or unset "contest mode" for a submission's comments.

In contest mode, upvote counts are hidden and comments are displayed in a random order.

If `state` is not specified, `false` is assumed.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","Full ID36 of a Submission."
   "state","boolean","Whether to enable (true) or disable (false) contest mode."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","ID not found, or you do not have permission to enable/disable contest mode for this post."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_contest_mode


Set suggested sort
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/set_suggested_sort

*scope: modposts*

Set or unset the suggested sort for a submission's comments.

When set, all redditors will see comments in the suggested sort by default.
They can still manually change back to their preferred sort if they choose.

If `sort` is `blank`, not given, or an unknown value, the suggested sort will be unset.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","full ID36 of a Submission"
   "sort","string","one of `confidence`, `top`, `new`, `controversial`, `old`, `random`, `qa`, `live`, `blank`"

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","ID not found, or you do not have permission to set the suggestd sort for this post"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_suggested_sort


.. _post-api-sendreplies:

Set inbox replies
~~~~~~~~~~~~~~~~~

.. http:post:: /api/sendreplies

*scope: edit*

Enable or disable inbox replies for a Submission or Comment.

If `state` is not provided, `true` (enable) is assumed.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","A full ID36 of a Submission or Comment."
   "state","boolean","Whether to enable or disable inbox replies."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_sendreplies


Set event time
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

   "id","string","Full ID36 of a post."
   "event_start","string","A datetime in ISO 8601 format. E.g., `2018-09-11T12:00:00`.

   If value is empty the parameter is ignored."
   "event_end","string","A datetime in ISO 8601 format. E.g., `2018-09-11T12:00:00`.

   If value is empty the parameter is ignored."
   "event_tz","string","A timezone. E.g., `America/Los_Angeles`.

   If not specified, defaults to `UTC`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "BAD_TIME","200","* The value specified for `event_start` or `event_end` is in a bad format.

   * The date string specified for `event_start` or `event_end` is in the past.

   Note that this error will always indicate `event_start` is wrong even if it's `event_end` that needs fixing.","
   ``{""json"": {""errors"": [[""BAD_TIME"", ""This time is invalid"", ""event_start""]]}}``
   "
   "INVALID_TIMEZONE","200","The value specified for `event_tz` is invalid.","
   ``{""json"": {""errors"": [[""INVALID_TIMEZONE"", ""This timezone is invalid"", ""event_tz""]]}}``
   "
   "MAX_EVENT_TIME","200","The event can't be longer than 7 days.","
   ``{""json"": {""errors"": [[""MAX_EVENT_TIME"", ""This event can't be longer than 7 days"", ""event_end""]]}}``
   "
   "MIN_EVENT_TIME","200","The event must last at least 30 minutes","
   ``{""json"": {""errors"": [[""MIN_EVENT_TIME"", ""This event must last at least 30 minutes"", ""event_end""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","The `id` parameter was not specified."
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

   "fullname","string","The full ID36 of a submission."
   "follow","boolean","True to follow, false to unfollow. Default: false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","The submission specified by the `fullname` parameter is not an event."
   "404","The submission specified by the `fullname` parameter does not exist."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_follow_post


.. _post-api-approve:

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

   "removed","Resets to `false`."
   "removed_by_category","Resets to `null`."
   "banned_by","Resets to `null`."
   "banned_at_utc","Resets to `null`."
   "ban_note","Field no longer exists."
   "spam","Resets to `false`."
   "is_crosspostable","Resets to `true`."
   "is_robot_indexable","Resets to `true`."
   "mod_reason_by","Resets to `null`."
   "mod_reason_title","Resets to `null`."
   "mod_note","Resets to `null`."

Approving a post/comment affects it's attributes:

.. csv-table:: Object attribute changes
   :header: "Field","Description"

   "approved","Becomes `true`. (Value starts as `false`.)"
   "approved_by","Name of the redditor who approved. (Value starts as `null`.)"
   "approved_at_utc","The unix timestamp of when the item was approved. (Value starts as `null`.)"

Returns an empty JSON object on success.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","Full ID36 of a post or comment."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "404","* The target specified by the `id` parameter does not belong to a subreddit you have permission to approve.

   * The `id` parameter was not specified."


.. _post-api-remove:

Remove
~~~~~~

.. http:post:: /api/remove

*scope: modposts*

As a moderator, remove a post, comment, or modmail message.

Returns an empty JSON object on success.

Removing a post/comment affects its attributes:

.. csv-table:: Object attribute changes
   :header: "Field","Description"

   "removed","Becomes `true`."
   "banned_by","Name of the redditor who removed. (Value start as `null`.)"
   "banned_at_utc","The unix timestamp of when the item was removed. (Value starts as `null`.)"
   "ban_note","Ban note.

   Value is `spam` if `spam` parameter was `true`.

   Value is `remove not spam` if `spam` parameter was `false`.

   Value is `confirm spam` if a removal was made with the `spam` parameter as `false` then again with
   the `spam` parameter as `true`. If the order is reversed then the the note will be `remove not spam`."
   "spam","Becomes `true` if `spam` parameter was `true`."

Extra attributes for posts only:

.. csv-table:: Object attribute changes
   :header: "Field","Description"

   "removed_by_category","The removed by category. It will be `author` even if the remover is a moderator. (Value starts as `null`.)"
   "is_crosspostable","Becomes `false`. (Value starts as `true`.)"
   "is_robot_indexable","Becomes `false`. (Value starts as `true`.)"

|

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"

   "id","string","Full ID36 of a post or comment."
   "spam","boolean","Indicate whether the post should be removed as spam. Default: true."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

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


.. _submission-ignore-reports:

Ignore reports
~~~~~~~~~~~~~~

.. http:post:: /api/ignore_reports
.. http:post:: /api/unignore_reports

*scope: modposts*

Prevent future reports on a post/comment from causing notifications.

Ignoring reports will not cause notifications or make the ignored thing show up in the various moderation listings.

See the `ignore_reports`, `num_reports`, `user_reports`, `mod_reports`, and `report_reasons` fields on the Submission schema.

Returns `{}` on success. If the target is already ignored/unignored it is treated as a success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a post or comment (prefixed with `t3_` or `t1_`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "403","* The `id` parameter was not specified.

   * The target specified by `id` was not found, or points to an item you are not a moderator of."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_ignore_reports


Set removal reason
~~~~~~~~~~~~~~~~~~

See :ref:`here <comment-set-removal-reason>`.


Send removal reason
~~~~~~~~~~~~~~~~~~~

See :ref:`here <comment-send-removal-reason>`.


Get duplicates
~~~~~~~~~~~~~~

.. http:get:: [/r/{subreddit}]/duplicates/{article}

*scope: read*

Gets the crossposts for a submission.

Returns an array of two listings. The first one contains one element which is the originating submission
specified by `{article}`. The second one contains a list of 'duplicates' which could be crosspost type
posts, or just regular link posts that have linked to the same URL.

`{subreddit}` can be obmitted. If given it must be correctly match the subreddit for the article ID
otherwise an empty listing will be returned.
`{article}` is a submission ID36.

See :ref:`Additional URL Params <frontpage-listings-additional-url-params>`.

More additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "sort","string","Either `num_comments` or `new`. Default: `num_comments`."
   "crossposts_only","boolean","If truthy (any string matching `/^[^0Ff]/`), return only crosspost type submissions
   in the second listing. These crossposts may not necessarily be crossposting the originating submission specified
   by `{article}`, they are just the duplicates that are crosspost type posts."
   "sr","string","Filter the duplicates list by an exact subreddit name. If the subreddit name specified doesn't
   exist then this parameter is ignored and all posts are returned."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","Fetching some submissions results in a 403. E.g., `124srz`.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "
   "404","The article ID could not be found.","
   ``{""message"": ""Not Found"", ""error"": 404}``
   "
