
Direct Message
==============

Overview
--------

There are two main categories of messages: composed messages and comment messages.
Composed messages are the direct messages that are composed and sent by users.
Comment messages are automatically generated notifications of a reply to one of your
submissions or comments, or a comment in which you were mentioned.

If the message is a user (or subreddit) message, the container object will have ``kind: t4``,
but if it is a comment message it will have ``kind: t1`` and the `id` field will be a comment ID
instead of a message ID. Given only the data, you can distinguish these two message types by inspecting
the `was_comment` field. It is true for a comment message.

Message modes:

.. code-block:: text

   user > self
   user sub > self
   sub > self  (user is hidden)
   self > user
   self sub > user
   self > sub

Note that subreddits cannot direct message subreddits.

Other than checking the name of `author` and `dest` there's little information that provides an indication
of whether a message is incoming or outgoing, except if the message is an outgoing message to a subreddit.
In the case of an outgoing subreddit message, the `dest` field will start with `#`.


Schema
~~~~~~

.. csv-table:: Message Object
   :header: "Field","Type (hint)","Description"

   "id","string","The ID of the message if the message is a user or subreddit message. If a comment message,
   the ID of the comment."
   "name","string","The `id` field but with `t4_` prepended if a user or subreddit message, or
   `t1_` prepended if a comment message."
   "created_utc","float","Unix timestamp of when the message was made, or comment was made in the case of a comment message. Will always be a whole number."
   "created","float","Legacy. Same as `created_utc` but subtract 28800."
   "author","string?","If a user message, the name of the user who sent the message.

   If a subreddit message, value is `null`.

   If a comment message, the name of the author who made the relevant comment."
   "author_fullname","string?","If a user message, the full ID36 of the user who sent the message, unless
   it was sent by a special user such as `reddit` or `welcomebot` in which case the value will be `null`.
   Hence, this field is not in complete sync with `author`.

   If a subreddit message, value is `null`.

   If a comment message, the full ID36 of the author who made the relevant comment."
   "subject","string","The subject of the message.

   If a comment message then the value will be
   `comment reply` if `type: comment_reply`,
   `post reply` if `type: post_reply`,
   `username mention` if `type: username_mention`,
   ",
   "dest","string","The username of the recipient.

   If the message is a part of a message thread and the message was directed to a subreddit instead of a user,
   this field will contain the subreddit name, prefixed with `#`, instead."
   "body","string","The message content.

   If a comment message, it contains the body of the comment."
   "body_html","","HMTL of the `body` field."
   "subreddit","string?","If a subreddit message, the name of the subreddit in which the message was from.

   If a comment message, the name of the subreddit in which the comment was from.

   Is `null` if a user message."
   "likes","boolean?","Always `null` if a user message or subreddit message.

   If a comment message, determines upvote direction. Same as the `likes` field on the :ref:`comment schema <comment-schema>`."
   "replies","string | object","A listing of replies to this message, or an empty string if there are no replies."
   "score","integer","If a comment object, same as the `score` field on the :ref:`comment schema <comment-schema>`,
   otherwise if a user or subreddit message the value is `0`."
   "num_comments","integer?","If a comment message, same as the `num_comments` field on the :ref:`submission schema <submission-schema>`.

   If a user message or subreddit message, value is `null`."
   "parent_id","string?","If a user or subreddit message, contains the full ID36 (prefixed with `t4_`) of
   the user or subreddit message in which this message was a reply to. If this message is not a reply to another
   message, the value is `null`.

   If a comment message, same as the `parent_id` field on the :ref:`comment schema <comment-schema>`."
   "subreddit_name_prefixed","string?","Is `null` if the `subreddit` field is `null`, else contains the value of
   the `subreddit` field prepended with `r/`."
   "new","boolean","Unread indicator. False if the message has been seen by the user."
   "type","string","Value is `unknown` if a user or subreddit message.

   If a comment message, value is one of `comment_reply`, `post_reply`, or `username_mention`."
   "was_comment","boolean","True if a comment message, false if a user or subreddit message."
   "context","","Empty string if user or subreddit message.

   If a comment message, the value is the path to the relevant comment.

   E.g., `/r/redditdev/comments/o285jq/how_do_i_get_refreshtoken/h28kz3u/?context=3`.
   
   The value will usually have `?context=3` appended.

   The submission ID36 can be obtained from this value."
   "distinguished","string?","`null` if not distinguished, otherwise
   `""moderator""` or `""admin""`, or `""gold-auto""`.

   Is always `moderator` if a subreddit message."
   "link_title?","string","Key does not exist if user or subreddit message.

   If a comment message, same as `title` in the :ref:`submission schema <submission-schema>`."
   "first_message","integer?","The integer ID of the first message in the thread of messages.
   Value is `null` if this is a top-level message."
   "first_message_name","string?","The full ID36 (prefixed with `t4_`) of first message in the thread of messages.
   Value is `null` if this is a top-level message."
   "associated_awarding_id","unknown?",""


Actions
-------

Get messages
~~~~~~~~~~~~

.. http:get:: /message/inbox
.. http:get:: /message/unread
.. http:get:: /message/messages
.. http:get:: /message/sent
.. http:get:: /message/comments
.. http:get:: /message/selfreply
.. http:get:: /message/mentions

*scope: privatemessages*

This endpoint is a listing. See :ref:`Listings overview <listings-overview>`.

Listing collection type:

* `GET /message/inbox`: composed | comment
* `GET /message/unread`: composed | comment
* `GET /message/messages`: composed
* `GET /message/sent`: composed
* `GET /message/comments`: comment
* `GET /message/selfreply`: comment
* `GET /message/mentions`: comment

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "mark","boolean","Whether to mark items as read."

.. seealso:: `<https://www.reddit.com/dev/api/#GET_message_{where}>`_


Send
~~~~

.. http:post:: /api/compose

*scope: privatemessages*

Send a direct message to a user.

Using the `from_sr` parameter will cause a subreddit message to be sent.
The authenticated user must be a moderator of the subreddit that has the `mail` permission.

When using the `from_sr` parameter, if the target user specified by `to` is a moderator of the subreddit
specified by `from_sr`, nothing happens and the action is treated as a success,
unless the target user is the authenticated user.

Returns ``{"json": {"errors": []}}`` on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "to","string","The user or subreddit to send the message to.

   To message a user, specify the name of a user, optionally prefixed with `u/` or `/u/`.

   To message a subreddit, specify the name of a subreddit prefixed with either `#`, `r/`, or `/r/`."
   "subject","string","A string no longer than 100 characters."
   "text","string","The message body."
   "from_sr","string","The name of a subreddit. The name may begin with `r/` or `/r/`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "
   "NO_USER","200","The `to` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_USER"", ""please enter a username"", ""to""]]}}``
   "
   "NO_SUBJECT","200","The `subject` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_SUBJECT"", ""please enter a subject"", ""subject""]]}}``
   "
   "NO_TEXT","200","The `text` parameter was not specified or was empty.","
   ``{""json"": {""errors"": [[""NO_TEXT"", ""we need something here"", ""text""]]}}``
   "
   "USER_DOESNT_EXIST","200","The user name specified by the `to` parameter does not exist.","
   ``{""json"": {""errors"": [[""USER_DOESNT_EXIST"", ""that user doesn't exist"", ""to""]]}}``
   "
   "SUBREDDIT_NOEXIST","200","The subreddit specified by `from_sr` does not exist.","
   ``{""json"": {""errors"": [[""SUBREDDIT_NOEXIST"", ""Hmm, that community doesn't exist. Try checking the spelling."", ""from_sr""]]}}``
   "
   "NO_SR_TO_SR_MESSAGE","200","The `to` and `from_sr` were both specified and both refer to subreddits.","
   ``{""json"": {""errors"": [[""NO_SR_TO_SR_MESSAGE"", ""you can't send a message from a subreddit to another subreddit"", ""from""]]}}``
   "
   "NOT_WHITELISTED_BY_USER_MESSAGE","200","The target user has direct messages from strangers disabled.

   This setting can be configured at `<https://old.reddit.com/prefs/blocked>`_ by setting ""Show private messages from""
   to ""Only trusted users"".

   `<https://www.reddit.com/r/redditdev/comments/h17rgd/new_error_code_when_sending_message_not/>`_","
   ``{""json"": {""errors"": [[""NOT_WHITELISTED_BY_USER_MESSAGE"", ""can't send a message to that user"", ""to""]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "403","The `from_sr` parameter was specified and the current user is not a moderator of that subreddit.","
   ``{""message"": ""Forbidden"", ""error"": 403}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_compose


Reply
~~~~~

Reply to a message.

See :ref:`Comment Create <comment-create>`. Use a `t4_` ID for `thing_id`.


Delete
~~~~~~

.. http:post:: /api/del_msg

*scope: privatemessages*

Delete messages from the recipient's view of their inbox.

If the `id` parameter was not specified, is invalid, or the ID doesn't exist, the action is treated as a success.

Returns an empty JSON object on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a message (starting with `t4_`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_del_msg


Mark as read
~~~~~~~~~~~~

.. http:post:: /api/read_message
.. http:post:: /api/unread_message

*scope: privatemessages*

Mark an inbox item as read.

Marking an already marked as read item is treated as a success.

Returns an empty JSON object on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a message (`t4`), or comment (`t1`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","There is no user context."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description","Example"

   "400","The `id` parameter was not specified, is invalid, or the ID doesn't exist.","
   ``{""message"": ""Bad Request"", ""error"": 400}``
   "

.. seealso::
   https://www.reddit.com/dev/api/#POST_api_read_message
   https://www.reddit.com/dev/api/#POST_api_unread_message


Mark all as read
~~~~~~~~~~~~~~~~

.. http:post:: /api/read_all_messages

*scope: privatemessages*

Mark all messages as read.

Returns empty JSON object on success.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_read_all_messages


Collapse
~~~~~~~~

.. http:post:: /api/collapse_message
.. http:post:: /api/uncollapse_message

*scope: privatemessages*

Collapse a message.

If the `id` parameter was not specified, the action is treated as a success.

If any of the specified IDs are invalid or don't exist, the entire operation is cancelled and all IDs are ignored.

!! TODO: What is `id`\ s limit?

Returns an empty JSON object on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","A comma-separated list of full IDs of messages (`t4`), or comments (`t1`)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

.. seealso::
   https://www.reddit.com/dev/api/#POST_api_collapse_message
   https://www.reddit.com/dev/api/#POST_api_uncollapse_message


Block
~~~~~

.. http:post:: /api/block

*scope: privatemessages*

Block the author of a Submission, Comment, or Message.
This endpoint can also block messages from Subreddits.

To block a user directly by ID or name, see :ref:`here <account-block-user>` instead.

If the ID specified by `id` is invalid, the action is treated as a success.

This endpoint does not process user IDs but if the ID specified by `id` matches that of an
existing user's full ID36, then a 500 HTTP status error is raised.

Returns an empty JSON object on success.

.. csv-table:: Form data
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 of a submission, comment, message, or subreddit."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","200","There is no user context.","
   ``{""json"": {""errors"": [[""USER_REQUIRED"", ""Please log in to do that."", null]]}}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The full ID of an existing user (beginning with `t2_`) was provided.
   This endpoint is not meant for user IDs","
   ``{""message"": ""Internal Server Error"", ""error"": 500}``
   "

.. seealso:: https://www.reddit.com/dev/api/#POST_api_block


Unblock subreddit
~~~~~~~~~~~~~~~~~

.. http:post:: /api/unblock_subreddit

*scope: privatemessages*

???

.. seealso:: https://www.reddit.com/dev/api/#POST_api_unblock_subreddit
