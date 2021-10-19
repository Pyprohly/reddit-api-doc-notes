
Comment
=======

Overview
--------

.. _comment_schema:

Schema
~~~~~~

.. csv-table:: Comment Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "all_awardings","unknown array",""
   "approved_at_utc",".","See `approved_at_utc` field on the Submission schema."
   "approved_by",".","See `approved_by` field on the Submission schema."
   "archived","boolean","Whether the post is archived. Archived posts cannot be commented on, but the author can still edit the OP."
   "associated_award","unknown?",""
   "author","string","The redditor name. Possibly `[removed]` if the post was removed
   or `[deleted]` if the post was removed by the author."
   "author_fullname?","string","The full ID of the author.

   This attribute is not available if the post was removed or deleted."
   "author_premium?","boolean","Whether or not the submitter has Reddit Premium.

   This attribute is not available if the post was removed or deleted."
   "awarders","unknown array",""
   "banned_at_utc",".","See `banned_at_utc` field on the Submission schema.""
   "banned_by",".","See `banned_by` field on the Submission schema.""
   "body","string","The body text of the comment."
   "body_html","string","The HTML of the comment."
   "can_gild","boolean",""
   "can_mod_post","boolean",""
   "collapsed","boolean","Whether the comment is collapsed by default, i.e., when it has been downvoted significantly."
   "collapsed_because_crowd_control","boolean?",""
   "collapsed_reason","unknown?",""
   "controversiality","integer",""
   "created","float","Legacy. Same as `created_utc` but subtract 28800. Will always be a whole number."
   "created_utc","float","Unix timestamp of when the post was made."
   "distinguished","string?","`null` if not distinguished, otherwise `"moderator"` or `"admin"`."
   "downs","integer","Always `0`."
   "edited","boolean | float","`false` if the post wasn't edited, otherwise a Unix timestamp of when it was edited. Always a whole number."
   "gilded","integer",""
   "gildings","unknown object",""
   "id","string","The ID of the comment (without the `t1_` prefix). Also see `name`."
   "is_submitter","boolean","`true` if the author is the submission author."
   "likes","boolean?","`null` if no user context.

   If user context: `null` if not voted on, `true` if upvoted, `false` if downvoted."
   "link_id","string","The full ID of the submission in which this comment belongs."
   "locked","boolean","Whether the post has been locked. https://www.reddit.com/r/modnews/comments/3qguqv/moderators_lock_a_post/"
   "removal_reason","unknown?","Appears to be unused; always `null`. Perhaps it would have been used for the removal reason message (but removal messages can be sent multiple times)."
   "mod_reason_by","string?","The name of the moderator who applied the removal reason to this submission.

   Value is `null` if the post does not have a removal reason *or* mod note set.
   If the post gets re-approved, the value gets reset to `null`."
   "mod_reason_title","string?","The removal reason title.

   Value is `null` if the post does not have a removal reason set.
   If the post gets re-approved, the value gets reset to `null`."
   "mod_note","string?","The removal reason moderator note.
   Value can be `null` if an empty string was sent as the mod note.

   Value is `null` if the post does not have a mod note set.
   If the post gets re-approved, the value gets reset to `null`."
   "name","string","The comment's full ID (with prefix `t1_`). Also see `id`."
   "no_follow","boolean",""
   "parent_id","string","The full ID of the comment or submission above this one."
   "permalink","string","The uri of the comment without the domain.
   E.g., `/r/ImaginaryLandscapes/comments/iaoshc/floating_eyes_in_the_silent_forest/g1qfxir/`"
   "replies","object | string","A listing object if this object was drawn from a comment tree
   and there are comment replies, otherwise an empty string."
   "saved","boolean","Whether the authenticated user has saved this comment. For clients with no user context this will always be false."
   "score","integer","The number of upvotes (minus downvotes)."
   "score_hidden","boolean","Whether the score is hidden."
   "send_replies","boolean","Whether an inbox message will be sent to you when the comment receives a reply."
   "stickied","boolean","Whether the comment is 'stickied' in the thread. If `true` then the `distinguished` should also be not `null`."
   "subreddit","string","The subreddit name. E.g., `IAmA`."
   "subreddit_id","string","The full ID of the subreddit that was posted to. E.g., `t5_2qzb6` for `r/IAmA`."
   "subreddit_name_prefixed","string","Same as the `subreddit` field but prefixed with `r/`. E.g., `r/IAmA`."
   "subreddit_type","string","One of `public`, `private`, `restricted`, `archived`, `employees_only`, `gold_only`, `gold_restricted`, or `user`."
   "top_awarded_type","unknown?",""
   "total_awards_received","integer","Number of rewards on the comment."
   "treatment_tags","unknown array",""
   "ups","integer","Same as `score`."
   "rte_mode?","string","The string 'markdown'.

   Field not available if the post is not a text post.
   Field not available if no user context is available."
   "removed?",".","See `removed` field on the Submission schema."
   "approved?",".","See `approved` field on the Submission schema."
   "spam?","boolean","`true` if the submission is marked as spam else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   (or there's no user context)."

   "author_flair_background_color","string?","See `user_flair_background_color` field on the Subreddit schema.

   Additionally: value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "author_flair_css_class","string?","See `user_flair_css_class` field on the Subreddit schema.

   Additionally: value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "author_flair_richtext","unknown array","See `user_flair_richtext` field on the Subreddit schema."
   "author_flair_type","string","This attribute is not available if the post was removed or deleted."
   "author_flair_template_id","string?","See `user_flair_template_id` field on the Subreddit schema.

   Additionally: value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "author_flair_text","string?","See `user_flair_text` field on the Subreddit schema.

   Additionally: value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "author_flair_text_color","string?","See `user_flair_text_color` field on the Subreddit schema.

   Additionally: value `null` when user flairs are disabled in the subreddit (`user_flair_enabled_in_sr` is false)."
   "author_patreon_flair?","boolean","This attribute is not available if the post was removed or deleted."
   "ignore_reports?","boolean","`true` if ignoring reports for this item, else `false`.

   This field is not available if the current user is not a moderator of the subreddit
   or there's no user context."
   "num_reports","integer?","The number of reports on this item.

   This field is `null` if the current user is not a moderator of the subreddit
   or there's no user context."
   "user_reports","array array","An array of user reports.

   Each sub-array contains 4 elements.

   An example of 2 user reports::

      [[\"spam\", 3, False, True], [\"trolling\", 1, False, True]]

   The meaning of the fields are as follows::

      [
         reportReason: string,
         numberOfReports: integer,
         snoozeStatus: boolean,
         canSnooze: boolean,
      ]

   (Source: `<https://www.reddit.com/r/redditdev/comments/olqo5s/what_do_the_boolean_values_represent_in_the_user/>`_)

   The array is empty if the current user is not a moderator of the subreddit
   or there's no user context."
   "mod_reports","array array","An array of mod reports.

   The sub-arrays contains two elements: the report reason text, and the name of the reporting moderator.

   An example of 3 moderator reports::

      [[\"spam\", \"Pyprohly\"], [\"Looks like spam to me\", \"SomeMod\"], [\"sus\", \"SomeOtherMod\"]]

   The array is empty if the current user is not a moderator of the subreddit
   or there's no user context."
   "report_reasons","string array?","This field is deprecated.

   If there are no reports on this item, it is an empty array.

   If there are reports on this item, the value is::

      [\"This attribute is deprecated. Please use mod_reports and user_reports instead.\"]

   This field is `null` if the current user is not a moderator of the subreddit
   or there's no user context."


Actions
-------

Get
~~~

See :ref:`here <get_api_info>`.


.. _comment_create:

Create
~~~~~~

.. http:post:: /api/comment

*scope: submit | privatemessages*

Comment on a submission, reply to a comment, or reply to a message.

The newly created comment object is returned in a structure like the following::

   {"json": {"errors": [], "data": {
         "things": [
            {"kind": "t1", "data": {"author_flair_background_color": "", ...}}
         ]}}}

If `return_rtjson` is truthy then the data is not wrapped in that strucuture and is provided directly. E.g.,::

   {"author_flair_background_color": "", ...}

But the `return_rtjson` parameter is ignored when replying to a message.

Commenting on a submission requires the `submit` scope.
Replying to a comment also requires the `submit` scope.
Sending a message requires the `privatemessages` scope.

.. csv-table:: Form Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "thing_id","string","The full ID36 of a comment, submission, or message."
   "text","string","Markdown text."
   "richtext_json","string","A string of RTJSON to use instead of `text`."
   "return_rtjson","boolean","If truthy (a string that starts with `0` or `F` or `f` is treated as falsy),
   return the newly created object as the top level JSON object instead of being wrapped in a listing.

   If `thing_id` is a message (starting with `t4_`), this parameter is ignored."

|

.. csv-table:: API Errors (variant 2)
   :header: "Error","Description"
   :escape: \

   "USER_REQUIRED","you must login"
   "NO_THING_ID","`thing_id` field wasn't given or the ID doesn't exist"
   "NO_TEXT","* Neither `text` nor `richtext_json` was specified.

   * `text` was specified but was empty.

   \"*NO_TEXT: we need something here -> text*\""
   "TOO_OLD","The target is older than 6 months and cannot be replied to.

   \"that's a piece of history now; it's too late to reply to it -> parent\""

.. seealso:: https://www.reddit.com/dev/api/#POST_api_comment


Delete
~~~~~~

See :ref:`here <post_api_del>`.


Edit body
~~~~~~~~~

See :ref:`here <post_api_editusertext>`.


Lock
~~~~

See :ref:`here <post_api_lock>`.


Vote
~~~~

See :ref:`here <post_api_vote>`.


Save
~~~~

See :ref:`here <post_api_save>`.


Distinguish
~~~~~~~~~~~

See :ref:`here <post_api_distinguish>`.


Set inbox replies
~~~~~~~~~~~~~~~~~

See :ref:`here <post_api_sendreplies>`.


Approve
~~~~~~~

See :ref:`here <post_api_approve>`.


Remove
~~~~~~

See :ref:`here <post_api_remove>`.


Ignore reports
~~~~~~~~~~~~~~

See :ref:`here <submission_ignore_reports>`.


.. _comment_set_removal_reason:

Set removal reason
~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/modactions/removal_reasons

*scope: (unknown)*

Set a removal reason on a removed submission/comment.

See the `mod_reason_by`, `mod_reason_title`, and `mod_note` fields on the
:ref:`Comment schema <comment_schema>`.

If the target is not a removed item, this endpoint has no effect.

Any ID that doesn't exist in `item_ids` will be ignored.
If any of the IDs in `item_ids` don't belong to a subreddit you moderate
then a HTTP 403 status error is returned and none of the targets will be processed.

The maximum limit for `item_ids` is yet to be discovered.
It doesn't appear to be possible to perform this operation in bulk through the UI anyway.

This endpoint wants JSON data.

Returns zero bytes on success.

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "item_ids","string array","An array of full ID36s of comments or submissions to process.
   Alternatively, or additionally, elements can be a comma separated list of ID36s."
   "reason_id","string?","A removal reason ID.

   If a `null` value or empty string is provided the reason will not be changed.
   This field is still mandatory however (a `JSON_MISSING_KEY` API error is returned if missing).
   If not specified, the UI provides a `null` value here."
   "mod_note","string?","A moderator note.

   If a `null` value or empty string is provided the mod note will not be changed.
   This field is still mandatory however (a `JSON_MISSING_KEY` API error is returned if missing).
   If not specified, the UI provides an empty string value here."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "JSON_MISSING_KEY","* The `item_ids` parameter was not specified.

   * The `reason_id` parameter was not specified.

   * The `mod_note` parameter was not specified.

   * A `null` value or empty stings were given for both `reason_id` and `mod_note`
     at the same time.

   *\"JSON missing key: \"reason_id\"\"* -> reason_id"
   "NO_THING_ID","* The `item_ids` array was empty.

   * None of the IDs specified in the `item_ids` array were valid.

   *\"id not specified\"*"
   "INVALID_ID","The reason ID specified by `reason_id` is invalid or does not exist.

   *\"The specified id is invalid\"* -> reason_id"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","An ID specified in the `item_ids` array does not belong to a subreddit you moderate."


.. _comment_send_removal_reason:

Send removal reason
~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/v1/modactions/removal_link_message
.. http:post:: /api/v1/modactions/removal_comment_message

*scope: (unknown)*

Send a removal reason to a user for a removed submission/comment of theirs.

This action can be performed multiple times. (The UI does not normally let you do this.)

Use `.../removal_link_message` to target a submission.
Use `.../removal_comment_message` to target a comment.

Example of a modmail message (`type: private`), for `title: "Self Promotion"`,
`message: "Self promoting posts are prohibited."`:

.. code-block:: text

   Your post from Pyprohly_test3 was removed because of: 'Self Promotion'

   Hi u/Pyprohly, Self promoting posts are prohibited.
   Original post: /r/Pyprohly_test3/comments/oo4sk4/poll2/

Unlike the `POST /api/v1/modactions/removal_reasons` endpoint, the ID you specify must be a
removed item otherwise an `INVALID_ID` API error is produced.

Returns the comment object that was created if `type: public` was specified.
Returns an empty JSON object for `type: private` and `type: private_exposed`.

.. csv-table:: JSON Data
   :header: "Field","Type (hint)","Description"
   :escape: \

   "type","string","One of the following:

   * `public`: creates a stickied comment on the post.
   * `private`: sends a modmail message.
   * `private_exposed`: sends a modmail message. The invoker's username is revealed."
   "item_id","string array","An array containing one full ID36 of a submission
   (if using `removal_link_message`) or comment (if using `removal_comment_message`).

   If more elements are specified they will be ignored."
   "title","string","A title for the removal reason.

   If `type: public` the title is ultimately unused.

   Can't be empty. A `NO_TEXT` API error is returned if an empty string is specified."
   "message","string","A message for the comment body for `type: public` or body of the
   modmail message for `type: private`.

   Can be empty string."

|

.. csv-table:: API Errors (variant 1)
   :header: "Error","Description"
   :escape: \

   "JSON_MISSING_KEY","* The `type` parameter was not specified.

   * The `item_id` parameter was not specified.

   * The `title` parameter was not specified.

   * The `message` parameter was not specified.

   *\"JSON missing key: \"message\"\"* -> message"
   "INVALID_ID","* The ID specified in the `item_id` array is invalid.

   * The ID specified in the `item_id` array is not a removed item."
   "INVALID_OPTION","The value specified for `type` was invalid.

   *\"that option is not valid\"* -> type"
   "NO_TEXT","The value for the `title` parameter was empty or `null`.

   *\"we need something here\"* -> title"
   "NO_THING_ID","The `item_id` array was empty.

   *\"id not specified\"*"

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "403","* The target specified by the ID in the `item_id` array does not belong to a subreddit you moderate.

   * The target specified by the ID in the `item_id` array was a comment ID when using the
     `removal_link_message` endpoint, or vice versa.
   "
