
Submission
==========

Overview
--------

.. _submission_schema:

Schema
~~~~~~

.. csv-table:: Submission Object
   :header: "Field","Type (hint)","Description"
   :widths: 8, 6, 30
   :escape: \

   "approved_at_utc","integer?","Unix time when the comment was approved. `null` if not approved or the current user is not a moderator of the subreddit."
   "subreddit","string","The subreddit name. E.g., `IAmA`"
   "selftext","string","The body text of the submission. Empty string if it is a link post."
   "author_fullname?","string","The full ID of the author.

   This attribute is not available if the post was removed or deleted."
   "saved","boolean","Whether the authenticated user has saved this post.

   For clients with no user context this will always be `false`."
   "mod_reason_title","unknown?",""
   "gilded","integer",""
   "clicked","boolean",""
   "title","string","The title of the post."
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "hidden","boolean",""
   "pwls","integer?","Unknown. Possibly stands for \"parent white list status\"?"
   "downs","integer","Always `0`."
   "thumbnail_height","integer?","Thumbnail height. `null` if text post."
   "hide_score","boolean","Whether the score is currently hidden."
   "name","string","The post's full ID (with prefix `t3_`). Also see `id`."
   "quarantine","boolean","Whether the post is in a quarantined subreddit."
   "upvote_ratio","float","Upvote ratio."
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`, `gold_only`, `gold_restricted`, or `user`."
   "ups","integer","Same as `score`."
   "total_awards_received","integer","Number of rewards on the post."
   "media_embed","unknown object",""
   "thumbnail_width","integer?","Thumbnail width. `null` if text post."
   "is_original_content","boolean","Whether the post is marked as OC."
   "user_reports","unknown array",""
   "secure_media","unknown?",""
   "is_reddit_media_domain","boolean","Whether media is reddit hosted, that is
   either i.redd.it for images or v.redd.it for videos. This will always be false for a text post.[needs checking]"
   "is_meta","boolean",""
   "category","unknown?",""
   "secure_media_embed","unknown object",""
   "can_mod_post","boolean",""
   "score","integer","The number of upvotes (minus downvotes). This attribute will work even if `hide_score` is `true`."
   "approved_by","string?","The name of the redditor who approved this post. `null` if not approved or the current user is not a moderator of the subreddit."
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "thumbnail","string","The URL of the post thumbnail. Other possible values include
   `self` (if there is no thumbnail?), or `default` (if the post was removed/deleted?)."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited."
   "gildings","unknown object",""
   "post_hint?","string","E.g., `\"image\"`"
   "content_categories","unknown?",""
   "is_self","boolean","`true` if it is a text post. `false` if link post."
   "mod_note","string?",""
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "wls","integer","Unknown. Often `6`. Possibly stands for \"white list status\"?"
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
   "selftext_html","string?","The HTML of the post. This will be null if it is a link post."
   "likes","boolean?","`null` if no user context.

   If user context: `null` if not voted on, `true` if upvoted, `false` if downvoted."
   "suggested_sort","string?","`null` if suggested sort is not set, or one of `confidence` (best), `top`, `new`, `controversial`, `old`, `qa`."
   "view_count","unknown?",""
   "archived","boolean","Whether the post is archived. Archived posts cannot be commented on, but the author can still edit the OP."
   "no_follow","boolean",""
   "is_crosspostable","boolean","Whether the post can be crossposted. Will be `false` if the post was removed or deleted."
   "pinned","boolean","Whether the post is pinned to the poster's profile."
   "over_18","boolean","Whether the submission has been marked as NSFW."
   "preview?","unknown object","This attribute is not available if the post was removed or deleted."
   "all_awardings","unknown object",""
   "awarders","unknown array",""
   "media_only","boolean",""
   "can_gild","boolean",""
   "spoiler","boolean","Whether the post is marked as a spoiler."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "visited","boolean",""
   "removed_by","string?","The name of the redditor who removed this post. `null` if not removed or the current user is not a moderator of the subreddit."
   "num_reports","unknown?",""
   "distinguished","unknown?",""
   "subreddit_id","string","The full ID of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "mod_reason_by","unknown?",""
   "removal_reason","unknown?",""
   "id","string","The ID of the submission (without the `t3_` prefix). Also see `name`."
   "is_robot_indexable","boolean","Will be `false` if the post was removed or deleted. Possibly `false` for archived posts?[needs checking]"
   "report_reasons","unknown?",""
   "author","string","The redditor name. Possibly `[removed]` if the post was removed
   or `[deleted]` if the post was removed by the author."
   "discussion_type","unknown?",""
   "num_comments","integer","The number of comments."
   "send_replies","boolean","Whether an inbox message will be sent to you when the submission receives a new top-level comment."
   "whitelist_status","string",""
   "contest_mode","boolean","Whether the post is in contest mode or not."
   "mod_reports","unknown array",""
   "permalink","string","The uri of the post without the domain.
   E.g., `/r/IAmA/comments/erd8si/i_was_born_with_two_y_chromosomes_ama/`"
   "parent_whitelist_status","unknown?",""
   "stickied","boolean","Whether the post is a 'stickied' post in the subreddit."
   "url","string","If a text post, it is the url of the submission. If a link post,
   it is the url of the link. Also see `permalink`."
   "subreddit_subscribers","integer","The number of subscribers in the subreddit."
   "created_utc","float","Unix timestamp of when the post was made. Will always be a whole number."
   "num_crossposts","integer","Crosspost count."
   "media","unknown?",""
   "is_video","boolean",""
   "spam?","boolean","`true` if the submission was removed as spam else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "ignore_reports?","boolean","`true` if ignoring reports for the submission, else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "approved?","boolean","`true` if the submission is approved.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."
   "rte_mode?","string","The string 'markdown'.

   Field not available if the post is not a text post.
   Field not available if no user context is available."
   "url_overridden_by_dest?","string","The url of the linked item for the link post (`is_self` is `true`)."
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


Create
~~~~~~

.. http:post:: /api/submit

*scope: submit*

Compose a new submission to a subreddit.

Specify the target subreddit with `sr` and title `title`.

If `kind` is `"self"`, a text post ("self-post") is created with `text` or `richtext_json`
used as the body. An `INVALID_SELFPOST` error is returned if both are specified.

If `kind` is `"link"`, a link post is created with `url` as the link.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "ad","boolean","Setting to `true` appears to post the submission unlisted, accessible only by URL."
   "app","unknown",""
   "collection_id","string","(beta) the UUID of a collection"
   "event_end","string","(beta) a datetime string e.g. `2018-09-11T12:00:00`"
   "event_start","string","(beta) a datetime string e.g. `2018-09-11T12:00:00`"
   "event_tz","string","(beta) a pytz timezone e.g. `America/Los_Angeles`"
   "extension","unknown","This field is apparently used when the `resubmit` error occurs, but
   that error cannot be reproduced?"
   "flair_id","string","a string no longer than 36 characters"
   "flair_text","string","a string no longer than 64 characters"
   "g-recaptcha-response","unknown",""
   "kind","string","one of `link`, `self`, `image`, `video`, `videogif`"
   "nsfw","boolean","mark as NSFW"
   "resubmit","boolean","Ostensibly, if a link with the same URL has already been submitted
   to the specified subreddit then an error would be returned unless this field is `true`.
   This doesn't appear to be the case however."
   "richtext_json","string","a string of RTJSON"
   "sendreplies","boolean","Receive inbox notifications for replies. `true` if not specified."
   "spoiler","boolean","mark as spoiler"
   "sr","string","the subreddit name"
   "text","string","markdown text, for a text post."
   "title","string","Title of the submission. Up to 300 characters long."
   "url","string","a valid URL, for a link post."
   "video_poster_url","string",""

|

.. csv-table:: API Errors
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

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","The subreddit is private/banned."

.. seealso:: https://www.reddit.com/dev/api/#POST_api_submit


.. _post_api_del:

Delete
~~~~~~

.. http:post:: /api/del

*scope: edit*

Delete a Comment or Submission.

This endpoint does not produce any kind of return value.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","the full ID of a comment or submission"

|

.. csv-table:: API Errors
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
will only sometimes switch the `rte_mode` from `markdown` or `richtext`. I don't know what
the criteria is.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "return_rtjson","boolean","If truthy (a string that starts with `0` or `F` or `f` is treated as falsy),
   return the entity object as the top level JSON object."
   "richtext_json","string","A string of RTJSON"
   "text","string","Markdown text"
   "thing_id","string","Full ID of a comment or text post"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "NO_THING_ID","`thing_id` field wasn't given or the ID doesn't exist"

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

   "id","string","the full ID of a comment or submission"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","Something went wrong. The full ID doesn't exist, you don't have permission to lock the target, etc."

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

   "id","string","full ID of a Submission or Comment"
   "dir","integer or string","vote direction. one of `1`, `0`, or `-1`"
   "rank","integer","unknown purpose"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","no `id` was given or the target could not be found"
   "500","returned after a long wait if (1) `dir` was not specified,
   (2) a non-integer argument is specified for `dir`"

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

   "id","string","full ID of a Submission or Comment"
   "category","string","a category name. premium only feature?"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_save


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

   "id","string","full ID of a Submission or Comment"

|

.. csv-table:: API Errors
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

   "id","string","full ID of a Submission or Comment"

|

.. csv-table:: API Errors
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
giving it a different color, and putting a 'sigil' beside it.

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

   "id","string","full ID of a Submission or Comment"
   "how","string","one of `yes`, `admin`, `no`, `special`"
   "sticky","boolean","make a comment sticky"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "400","if `sticky` was specified and is `true` (or a truthy value) and `id` refers to submission rather than a comment"
   "403","`how` was not given, was of an invalid value, or you do not have the right mod privileges"
   "404","no `id` was given or the target could not be found"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_distinguish


Set Sticky
~~~~~~~~~~

.. http:post:: /api/set_subreddit_sticky

*scope: modposts*

Set or unset a Submission as sticky, either in its subreddit or to your user profile.

Stickied posts are pinned to the top of the subreddit in the default 'hot' listing.
On a user profile, they show as a pinned post at the top of the listing.

The `num` argument is used when stickying (i.e., `state` is `true`). It specifies
which position the post is to be placed in the existing list of stickied posts.
In a subreddit, there can be 2 sticked posts at a time, `num` can be either `1` or `2`.
On a user profile, there can be 4 sticked posts at a time, `num` can be from `1` to `4`.
If a number is specified outside a range, it will be clamped within range.

When stickying and `num` is not specified:

* When subreddit stickying, the post will be appended to the bottom of the sticky list.
  If the list was full then the bottom-most post will be replaced.
* When user profile stickying, the post will be added to the top of the sticky list.
  If the list was full then the bottom-most post will be evicted.

If `state` is not specified then it is assumed to be `false` and the post will be unstickied.

You cannot reorder sticky posts directly. You must unsticky them then re-sticky them.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","full ID of a Submission"
   "state","boolean","whether to sticky (`true`) or unsticky (`false`) this post"
   "num","integer","an integer position"
   "to_profile","boolean","if `true` sticky the post to your user profile instead of its subreddit"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","you do not have permission to sticky that post"
   "409","you are trying to sticky a post that is already stickied"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_set_subreddit_sticky


Set Contest Mode
~~~~~~~~~~~~~~~~

.. http:post:: /api/set_contest_mode

*scope: modposts*

Set or unset "contest mode" for a submission's comments.

In contest mode, upvote counts are hidden and comments are displayed in a random order.

If `state` is not specified, `false` is assumed.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","full ID of a Submission"
   "state","boolean","whether to enable or disable contest mode"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","ID not found, or you do not have permission to enable/disable contest mode for this post"

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

   "id","string","full ID of a Submission"
   "sort","string","one of `confidence`, `top`, `new`, `controversial`, `old`, `random`, `qa`, `live`, `blank`"

|

.. csv-table:: API Errors
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

   "id","string","full ID of a Submission or Comment"
   "state","boolean","whether to enable or disable inbox replies"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_sendreplies


Set Event Times
~~~~~~~~~~~~~~~

.. http:post:: /api/event_post_time

*scope: modposts*

Add or modify post event times.

Specify only `event_start` to change only the starting date.
The same cannot be done for `event_end`, a 500 HTTP error will occur.

If both `event_start` and `event_end` are specified then the `event_start` must be before `event_end`
otherwise a `MIN_EVENT_TIME` API error is returned.
It's possible however to make a second request specifying only `event_start` to modify the start date
so that `event_start` is after `event_end`. If this happens then the time difference can be longer than
7 days.

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


.. _post_api_approve:

Approve
~~~~~~~

.. http:post:: /api/approve

*scope: modposts*

Approve a post or comment.

A removed target can be approved. If so it will be re-inserted into appropriate listings and
any reports on the approved thing will be discarded.

Returns an empty JSON object on success.

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

Returns an empty JSON object on success.

Approving a post/comment affects it's attributes:

.. csv-table:: Object attribute changes
   :header: "Field","Description"
   :escape: \

   "approved","Becomes `true`. (Value start as `false`.)"
   "approved_by","Name of the redditor who approved. (Value start as `null`.)"
   "approved_at_utc","The unix timestamp of when the item was approved. (Value starts as `null`.)"

|

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

Removing a post/comment affects it's attributes:

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

   "removed_by_category","The removed by category. It will be `author` even if the remover was the author even if the
   author is a moderator. (Value starts as `null`.)"
   "is_crosspostable","Becomes `false`. (Value starts as `true`.)"
   "is_robot_indexable","Becomes `false`. (Value starts as `true`.)"

|

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","Full ID36 of a post or comment."
   "spam","boolean","Indicate whether the post should be removed as spam.

   Default: `true`."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","* The target specified by the `id` parameter does not belong to a subreddit you have permission to approve.

   * The `id` parameter was not specified."
