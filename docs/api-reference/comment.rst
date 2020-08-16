
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

See :ref:`here <get_api_info>`.


Create
^^^^^^

.. http:post:: /api/comment

*scope: submit | privatemessages*

Submit a new comment or reply to a message.

The target entity (with the new body text) is returned in a listing structure,
unless `return_rtjson` is truthy in which case it is not wrapped in a listing.

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

.. seealso:: https://www.reddit.com/dev/api/#POST_api_comment


Delete
^^^^^^

See :ref:`here <post_api_del>`.


Edit Body
^^^^^^^^^

See :ref:`here <post_api_editusertext>`.


Lock
^^^^

See :ref:`here <post_api_lock>`.


Vote
^^^^

See :ref:`here <post_api_vote>`.


Save
^^^^

See :ref:`here <post_api_save>`.


Mark NSFW
^^^^^^^^^

See :ref:`here <post_api_marknsfw>`.


Mark Spoiler
^^^^^^^^^^^^

See :ref:`here <post_api_spoiler>`.


Distinguish
^^^^^^^^^^^

See :ref:`here <post_api_distinguish>`.


Set Inbox Replies
^^^^^^^^^^^^^^^^^

See :ref:`here <post_api_sendreplies>`.
