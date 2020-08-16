
Submission
==========

Overview
--------

Object
^^^^^^

.. csv-table:: Submission Object
   :header: "Field","Type (hint)","Description"
   :widths: 8, 6, 30
   :escape: \

   "approved_at_utc","integer?","Unix time when the comment was approved. `null` if not approved."
   "subreddit","string","The subreddit name. E.g., `IAmA`"
   "selftext","string","The body text of the submission. Empty string if it is a link post."
   "author_fullname?","string","The full ID of the author.

   This attribute is not available if the post was removed or deleted."
   "saved","boolean","Whether the authenticated user has saved this post. For clients with no user context this will always be false."
   "mod_reason_title","unknown?",""
   "gilded","integer",""
   "clicked","boolean",""
   "title","string","The title of the post."
   "link_flair_richtext","unknown array",""
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "hidden","boolean",""
   "pwls","integer","Unknown. Often `6`. Possibly stands for \"parent white list status\"?"
   "link_flair_css_class","unknown?",""
   "downs","integer","Always `0`."
   "thumbnail_height","integer","Thumbnail height."
   "hide_score","boolean","Whether the upvote count is currently hidden."
   "name","string","The post's full ID (with prefix `t3_`). Also see `id`."
   "quarantine","boolean","Whether the post is in a quarantined subreddit."
   "link_flair_text_color","string",""
   "author_flair_background_color","string?",""
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`,
   `gold_only`, or `gold_restricted`."
   "ups","integer","Same as `score`."
   "total_awards_received","integer","Number of rewards on the post."
   "media_embed","unknown object",""
   "thumbnail_width","integer","Thumbnail width."
   "author_flair_template_id","unknown?",""
   "is_original_content","boolean","Whether the post is marked as OC."
   "user_reports","unknown array",""
   "secure_media","unknown?",""
   "is_reddit_media_domain","boolean","Whether media was uploaded to a reddit media host, that is
   either i.redd.it for images or v.redd.it for videos. This will always be false for a text post.[needs checking]"
   "is_meta","boolean",""
   "category","unknown?",""
   "secure_media_embed","unknown object",""
   "link_flair_text","string?","Post flair text."
   "can_mod_post","boolean",""
   "score","integer","The number of upvotes (minus downvotes)."
   "approved_by","string?","The name of the redditor who approved this post.[needs checking]"
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "thumbnail","string","The URL of the post thumbnail. Other possible values include
   `self` (if there is no thumbnail?), or `default` (if the post was removed/deleted?)."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited."
   "author_flair_css_class","string?",""
   "author_flair_richtext?","unknown array","This attribute is not available if the post was removed or deleted."
   "gildings","unknown object",""
   "post_hint?","string","`\"self\"` if a text post. `\"link\"` if a link post.

   This attribute is not available if the post was removed or deleted."
   "content_categories","unknown?",""
   "is_self","boolean","`true` if it is a text post. `false` if link post."
   "mod_note","unknown?",""
   "created","float","Legacy. Same as `created_utc` but add 28800."
   "link_flair_type","string","Possible values: `text`, `richtext`, ...?"
   "wls","integer","Unknown. Often `6`. Possibly stands for \"white list status\"?"
   "removed_by_category","unknown?",""
   "banned_by","unknown?",""
   "author_flair_type?","string","This attribute is not available if the post was removed or deleted."
   "domain","string","If a link post, the domain of the link. If a text post, it is
   the name of the subreddit prefixed with `self.`, e.g., `self.IAmA`."
   "allow_live_comments","boolean",""
   "selftext_html","string?","The HTML of the post. This will be null if it is a link post."
   "likes","unknown?",""
   "suggested_sort","unknown?",""
   "banned_at_utc","unknown?",""
   "view_count","unknown?",""
   "archived","boolean","Whether the post is archived. Archived posts cannot be commented on, but the author can still edit the OP."
   "no_follow","boolean",""
   "is_crosspostable","boolean","Whether the post can be crossposted. Will be `false` if the post was removed or deleted."
   "pinned","boolean","Possibly same as `stickied`?"
   "over_18","boolean","Whether the submission has been marked as NSFW."
   "preview?","unknown object","This attribute is not available if the post was removed or deleted."
   "all_awardings","unknown object",""
   "awarders","unknown array",""
   "media_only","boolean",""
   "link_flair_template_id?","string","The link flair UUID.

   This attribute is not available if the post was removed or deleted."
   "can_gild","boolean",""
   "spoiler","boolean","Whether the post is marked as a spoiler."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "author_flair_text","string?",""
   "visited","boolean",""
   "removed_by","unknown?",""
   "num_reports","unknown?",""
   "distinguished","unknown?",""
   "subreddit_id","string","The full ID of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "mod_reason_by","unknown?",""
   "removal_reason","unknown?",""
   "link_flair_background_color","string",""
   "id","string","The ID of the submission (without the `t3_` prefix). Also see `name`."
   "is_robot_indexable","boolean","Possibly always `false` for archived posts?[needs checking]"
   "report_reasons","unknown?",""
   "author","string","The redditor name. Possibly `[removed]` if the post was removed by a mod,
   or `[deleted]` if the post was removed by the author."
   "discussion_type","unknown?",""
   "num_comments","integer","The number of comments."
   "send_replies","boolean",""
   "whitelist_status","string",""
   "contest_mode","boolean","Whether the post is in contest mode or not."
   "mod_reports","unknown array",""
   "author_patreon_flair?","boolean","This attribute is not available if the post was removed or deleted."
   "author_flair_text_color","string?",""
   "permalink","string","The uri of the post without the domain.
   E.g., `/r/IAmA/comments/erd8si/i_was_born_with_two_y_chromosomes_ama/`"
   "parent_whitelist_status","string",""
   "stickied","boolean","Possibly same as `pinned`?[needs checking]"
   "url","string","If a text post, it is the url of the submission. If a link post,
   it is the url of the link. Also see `permalink`."
   "subreddit_subscribers","integer","The number of subscribers in the subreddit."
   "created_utc","float","Unix timestamp of when the post was made."
   "num_crossposts","integer",""
   "media","unknown?",""
   "is_video","boolean",""


Actions
-------

.. _get_api_info:

Get
^^^

.. http:get:: /api/info

*scope: read*

Return Submission, Comment, and Subreddit resource info.

`id` will process up to 100 IDs. Any ID not found will be ignored.
Alphabetic characters in the ID must be lowercase.
If more than 100 IDs are given, a blank listing structure is returned.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "id","string","a comma-separated list of full IDs"
   "url","string","a valid URL"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_info


Create
^^^^^^

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
   "api_type","string","the string ``\"json\"``"
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

   "USER_REQUIRED","you must login to make a submission"
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
^^^^^^

.. http:post:: /api/del

*scope: edit*

Delete a Comment or Submission.

This endpoint does not produce any kind of return value.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
   "id","string","the full ID of a comment or submission"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_del


.. _post_api_editusertext:

Edit Body
^^^^^^^^^

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
^^^^

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

   "api_type","string","the string ``\"json\"``"
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
^^^^

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
^^^^

.. http:post:: /api/save
.. http:post:: /api/unsave

*scope: save*

Save a Submission or Comment.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^

.. http:post:: /api/marknsfw
.. http:post:: /api/unmarknsfw

*scope: modposts*

Save a Submission or Comment.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^^^

.. http:post:: /api/spoiler
.. http:post:: /api/unspoiler

*scope: modposts*

Save a Submission or Comment.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^^

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

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^

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

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^^^^^^^

.. http:post:: /api/set_contest_mode

*scope: modposts*

Set or unset "contest mode" for a submission's comments.

In contest mode, upvote counts are hidden and comments are displayed in a random order.

If `state` is not specified, `false` is assumed.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^^^^^^^^^

.. http:post:: /api/set_suggested_sort

*scope: modposts*

Set or unset the suggested sort for a submission's comments.

When set, all redditors will see comments in the suggested sort by default.
They can still manually change back to their preferred sort if they choose.

If `sort` is `blank`, not given, or an unknown value, the suggested sort will be unset.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
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
^^^^^^^^^^^^^^^^^

.. http:post:: /api/sendreplies

*scope: edit*

Enable or disable inbox replies for a Submission or Comment.

If `state` is not provided, `true` (enable) is assumed.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
   "id","string","full ID of a Submission or Comment"
   "state","boolean","whether to enable or disable inbox replies"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_sendreplies


Get More Comments
^^^^^^^^^^^^^^^^^

.. http:post:: /api/morechildren

TODO.
