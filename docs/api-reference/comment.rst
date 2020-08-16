
Comment
=======

Overview
--------

Object
^^^^^^

.. csv-table:: Comment Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "all_awardings","unknown array",""
   "approved_at_utc","integer?","Unix time when the comment was approved. `null` if not approved."
   "approved_by","string?","The name of the redditor who approved this post.[needs checking]"
   "archived","boolean","Whether the post is archived. Archived posts cannot be commented on, but the author can still edit the OP."
   "associated_award","unknown?",""
   "author","string","The redditor name. Possibly `[removed]` if the post was removed by a mod,
   or `[deleted]` if the post was removed by the author."
   "author_flair_background_color","string?",""
   "author_flair_css_class","string?",""
   "author_flair_richtext?","unknown array","This attribute is not available if the post was removed or deleted."
   "author_flair_template_id","unknown?",""
   "author_flair_text","string?",""
   "author_flair_text_color","string?",""
   "author_flair_type?","string","This attribute is not available if the post was removed or deleted."
   "author_fullname?","string","The full ID of the author.

   This attribute is not available if the post was removed or deleted."
   "author_patreon_flair?","boolean","This attribute is not available if the post was removed or deleted."
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "awarders","unknown array",""
   "banned_at_utc","unknown?",""
   "banned_by","unknown?",""
   "body","string","The body text of the comment."
   "body_html","string","The HTML of the comment."
   "can_gild","boolean",""
   "can_mod_post","boolean",""
   "collapsed","boolean","Whether the comment is collapsed by default, i.e., when it has been downvoted significantly."
   "collapsed_because_crowd_control","boolean?",""
   "collapsed_reason","unknown?",""
   "controversiality","integer",""
   "created","float","Legacy. Same as `created_utc` but add 28800."
   "created_utc","float","Unix timestamp of when the post was made."
   "distinguished","unknown?",""
   "downs","integer","Always `0`."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited."
   "gilded","integer",""
   "gildings","unknown object",""
   "id","string","The ID of the comment (without the `t1_` prefix). Also see `name`."
   "is_submitter","boolean","`true` if the author is the submission author."
   "likes","unknown?",""
   "link_id","string","The full ID of the submission in which this comment belongs."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "mod_note","unknown?",""
   "mod_reason_by","unknown?",""
   "mod_reason_title","unknown?",""
   "mod_reports","unknown array",""
   "name","string","The comment's full ID (with prefix `t1_`). Also see `id`."
   "no_follow","boolean",""
   "num_reports","unknown?",""
   "parent_id","string","The full ID of the comment or submission above this one."
   "permalink","string","The uri of the comment without the domain.
   E.g., `/r/ImaginaryLandscapes/comments/iaoshc/floating_eyes_in_the_silent_forest/g1qfxir/`"
   "removal_reason","unknown?",""
   "replies","object | string","A listing object if this object was drawn from a comment tree,
   otherwise an empty string."
   "report_reasons","unknown?",""
   "saved","boolean","Whether the authenticated user has saved this post. For clients with no user context this will always be false."
   "score","integer","The number of upvotes (minus downvotes)."
   "score_hidden","boolean","Whether the score is hidden."
   "send_replies","boolean",""
   "stickied","boolean","Possibly same as `pinned`?[needs checking]"
   "subreddit","string","The subreddit name. E.g., `IAmA`"
   "subreddit_id","string","The full ID of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`,
   "top_awarded_type","unknown?",""
   "total_awards_received","integer","Number of rewards on the comment."
   "treatment_tags","unknown array",""
   "ups","integer","Same as `score`."
   "user_reports","unknown array",""


Actions
-------

Get
^^^

:ref:`See here <get_api_info>`

Create
^^^^^^

.. http:post:: /api/comment

*scope: submit | privatemessages*

Submit a new comment or reply to a message.



******



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


Edit Body
^^^^^^^^^

.. http:post:: /api/editusertext

*scope: edit*

Edit the body text of a text post or comment.

The target entity (with the new body text) is returned in a listing structure,
but if `return_rtjson` is `true` (or any value not `false`) it is not wrapped in a listing.

If `text` and `richtext_json` are used together `richtext_json` will be used.

Editing a richtext post with `text` a markdown post with `richtext_json` or vice versa
will only sometimes switch the `rte_mode` from `markdown` or `richtext`. I don't know what
the criteria is.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "api_type","string","the string ``\"json\"``"
   "return_rtjson","boolean","if not `false`, return the entity object as the top level JSON object"
   "richtext_json","string","a string of RTJSON"
   "text","string","markdown text"
   "thing_id","string","full ID of comment or text post"

|

.. csv-table:: API Errors
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "NO_THING_ID","`thing_id` field wasn't given or the ID doesn't exist"

.. seealso:: https://www.reddit.com/dev/api/#POST_api_editusertext


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

TODO.




Subreddit submission listings
-----------------------------

.. http:get:: /r/{subreddit}[/[{sort}]]
.. http:get:: /r/{subreddit}/hot
.. http:get:: /r/{subreddit}/best
.. http:get:: /r/{subreddit}/rising
.. http:get:: /r/{subreddit}/top
.. http:get:: /r/{subreddit}/new
.. http:get:: /r/{subreddit}/controversial
.. http:get:: /r/{subreddit}/gilded

*scope: read*

If the sort component of the URL is omitted it is treated the same as `/hot`.

The hot listing may include pinned posts at the start of the listing.

`/best` is the same as `/hot`.

The listings contain submission objects except for `/gilded` which can contain
a mix of submission and comment objects.
