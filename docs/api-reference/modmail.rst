
Modmail
+++++++

Modmail General
===============

Overview
--------

Conversation Schema
~~~~~~~~~~~~~~~~~~~

.. csv-table:: Modmail Conversation Schema
   :header: "Field","Type (hint)","Description"

   "id","string","The conversation ID36."
   "subject","string","The subject line."
   "state","integer","Whether the conversation is new, in-progress, or archived.

   ConversationProgress enum:

   * 0: new
   * 1: in progress
   * 2: archived
   "
   "numMessages","integer","The number of messages in the conversation."
   "isAuto","boolean","True if the conversation was created due to an automated message;
   false if the message was created by a user."
   "isInternal","boolean","Whether this conversation is a moderator discussion."
   "isRepliable","boolean","True if the conversation thread accepts replies."
   "isHighlighted","boolean","True if the conversation is highlighted."
   "legacyFirstMessageId","string?","An ID36 that refers to the first message in the legacy modmail
   thread for this conversation thread. Prepend like so to get the direct message link:
   `https://www.reddit.com/message/messages/{legacyFirstMessageId}`.

   This field can be null in rare cases, such as in the
   ""r/{subreddit} is now enrolled in the New Modmail""
   modmail message from u/reddit."
   "lastUserUpdate","string?","An ISO8601 date string. If `isInternal` is true this should always be `null`.
   Basically, the time of the last message of the participant."
   "lastModUpdate","string?","An ISO8601 date string."
   "lastUpdated","string","An ISO8601 date string. Same as either `lastUserUpdate` or `lastModUpdate`, whichever is newer."
   "lastUnread","string?","An ISO8601 date string of when the conversation was last marked unread.
   Value is `null` if the message is marked read."
   "owner","object","The name and ID of the current subreddit.

   Object fields:

   * `displayName` (string): The name of the subreddit.
   * `type` (string): Always the string `subreddit`.
   * `id` (string): The full ID36 (`t5_` prefixed) of the subreddit.
   "
   "objIds","object array","An array of objects that reference message and mod action items from
   the `messages` and `modActions` keys in the root object encapsulating this conversation object.

   Object fields:

   * `key` (string): Either `messages` or `modActions`.
   * `id` (string): The ID of the message if `key: messages`, otherwise the ID of the mod action (`key: modActions`).

   The content of the array is different depending on whether the object was retrieved from
   `GET /api/mod/conversations` or `GET /api/mod/conversations/{conversation_id}`.

   If the conversation object was retrieved from `GET /api/mod/conversations`,
   this field will only have one object that is a `key: messages` object referencing the
   latest message in the conversation. Notice the object returned by that endpoint does
   not have a `modActions` key, only `messages`.
   "
   "participant","object","Information about the target user.

   If available, some of the information in this object overlaps with the information
   in the user dossier on the conversation aggregate root object.

   Object is empty if this conversation is a moderator discussion (i.e., `isInternal: true`),
   or if it is a to-subreddit conversation from the perspective of a user.

   Object fields:

   * `id` (integer): The integer ID of the user.
   * `name` (string): The name of the user.
   * `isMod` (boolean): If the user is a moderator of the subreddit this conversation is a subject of?
     (Isn't this always false since a message from a moderator will result in an internal modmail conversation?)
   * `isAdmin` (boolean): True if Reddit admin.
   * `isOp` (boolean): Whether this user is the initiator of the conversation.
   * `isParticipant` (boolean): Always true here.
   * `isApproved` (boolean): Whether the user is an approved contributor user of the subreddit.
   * `isHidden` (boolean): .
   * `isDeleted` (boolean): .
   "
   "authors","object array","A list of conversation users that have either messaged
   or perfomed a mod action in the conversation thread.

   There is one entry in the array for every message or mod action taken, hence the array can contain duplicate objects.

   This field is not very useful for anything since message and mod action objects already include
   author information on them.

   This object has fields similar to that of the `participant` field."
   "conversationType","string","Interchange type.

   One of: `sr_sr`, `sr_user`, `internal`."
   "participantSubreddit","object","Information about the relevant subreddit, if applicable.

   Object is empty if this conversation is a moderator discussion (i.e., `isInternal: true`),
   or if the modmail conversation was initiated directly from a user.

   Object fields:

   * `id` (string): The full ID36 (`t5_` prefixed) of the subreddit.
   * `name` (string): The name of the subreddit (not prefixed by `r/`).
   * `keyColor` (string): Can be empty.
   * `primaryColor` (string): Can be empty.
   * `communityIcon` (string): Can be empty.
   * `icon` (string): Can be empty.
   "


Message Schema
~~~~~~~~~~~~~~

.. csv-table:: Modmail Message Schema
   :header: "Field","Type (hint)","Description"

   "id","string","The message ID36."
   "author","object","Author information. Schema same as the `participant` field on the Conversations schema."
   "isInternal","boolean","Always true if this message is in a moderator discussion.
   Otherwise, true if this message is a private moderator note."
   "bodyMarkdown","string","The text content of the message in markdown format."
   "body","string","The content of the message in HTML."
   "date","string","An ISO8601 date string of when the message was created."
   "participatingAs","string","The author's relation to the conversation.

   One of: `moderator`, `participant_user`, `participant_subreddit`."


Modmail Mod Action Schema
~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Modmail Mod Action Schema
   :header: "Field","Type (hint)","Description"

   "id","string","An ID36 for this action."
   "actionTypeId","integer","The action type.

   ModmailModActionType enum:

   * 0: highlight
   * 1: unhighlight
   * 2: archive
   * 3: unarchive
   * 5: mute user
   * 6: unmute user
   * 7: ban user
   * 8: unban user
   * 9: approve user
   * 10: disapprove user
   "
   "date","string","An ISO8601 date string of when the action was performed."
   "author","object","Information about the mod who performed the action.

   Object fields are as follows. The values are non-stale and should always reflect the most recent information.

   * `id` (integer): The user ID of the mod who performed the action.
   * `name` (integer): The name of the mod who performed the action.
   * `isOp` (boolean): True if the user is the initiator of the conversation.
   * `isMod` (boolean): Whether the user is a mod of this subreddit. This could be false if
     action was made and they were removed as mod.
   * `isAdmin` (boolean): True if Reddit admin.
   * `isHidden` (boolean): Always false. A mod cannot perform mod actions anonymously.
   * `isDeleted` (boolean): .
   * `isApproved` (boolean): Whether the user is an approved user of the subreddit.
   * `isParticipant` (boolean): .
   "


User Dossier Schema
~~~~~~~~~~~~~~~~~~~

.. csv-table:: User Dossier Schema
   :header: "Field","Type (hint)","Description"

   "id","string","The full ID36 (`t2_` prefixed) of a user."
   "name","string","The name of the user."
   "created","string","When the user account was created, as an ISO8601 date string."
   "isSuspended","boolean","True if account is suspended."
   "isShadowBanned","boolean","True if account is shadow banned."
   "approveStatus","object","An object containing one key: `isApproved` which is a boolean
   that is true if the user is an approved contributor on the relevent subreddit."
   "muteStatus","object","An object detailing the mute status of the user in the subreddit.

   Sub-object fields:

   * `isMuted` (boolean): True if the user is currently muted on the subreddit.
   * `reason` (string): The mute reason. Empty string if not currently muted.
   * `muteCount` (integer): The number of times the user has been muted in the subreddit.
   * `endDate` (string?): An ISO8601 date string of when the mute ends. Value is `null` if
      the user is not muted.
   "
   "banStatus","object","An object detailing the ban status of the user in the subreddit.

   Sub-object fields:

   * `isBanned` (boolean): True if the user is currently banned on the subreddit.
   * `reason` (string): The ban reason. Empty string if not currently banned.
   * `isPermanent` (boolean): True if the ban is permanent. Value false if user is not banned.
   * `endDate` (string?): An ISO8601 date string of when the ban ends. Value is `null` if
      the user is not banned.
   "
   "recentPosts","object","An object mapping submission full ID36s (`t3_` prefixed) to a bit of
   information about the user's recent submissions to the subreddit.

   The order of the keys in this mapping appears to be insignificant. The UI will sort by
   the `date` field before display.

   The information in this field is associated with the 'Recent Posts:' section in the UI.

   Sub-object fields:

   * `date` (string): An ISO8601 date string of when the submission was created.
   * `title` (string): The title of the submission.
   * `permalink` (string): A URL to the submission.
   "
   "recentComments","object","An object mapping comment full ID36s (`t1_` prefixed) to a bit
   information about the user's recent comments in the subreddit.

   The order of the keys in this mapping appears to be insignificant. The UI will sort by
   the `date` field before display.

   The information in this field is associated with the 'Recent Comments:' section in the UI.

   Sub-object fields:

   * `comment` (string): The comment the user wrote.
   * `date` (string): An ISO8601 date string of when the comment was created.
   * `title` (string): The title of the submission in which the comment resides.
   * `permalink` (string): A URL to the comment.
   "
   "recentConvos","object","Other modmail conversations this user is involved in.
   An object mapping conversation ID36s to a permalink to other conversations.

   The order of the keys in this mapping appears to be insignificant. The UI will sort by
   the `date` field before display.

   The information in this field is associated with the 'Recent Messages (with user):' section in the UI.

   Sub-object fields:

   * `id` (string): The conversation ID36.
   * `date` (string): Always `0001-01-01T00:00:00+00:00`.
   * `subject` (string): The subject line of the conversation.
   * `permalink` (string): A URL to the conversation. E.g., `https://mod.reddit.com/mail/perma/tiebu`.
   "


Actions
-------

Get unread conversation counts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/mod/conversations/unread/count

*scope: modmail*

Get unread conversations counts by mailbox.

Returns a dictionary like the following::

   {"archived": 0,
    "appeals": 0,
    "highlighted": 0,
    "notifications": 2,
    "join_requests": 0,
    "filtered": 0,
    "new": 1,
    "inprogress": 0,
    "mod": 0}

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","500","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``"

.. seealso:: https://www.reddit.com/dev/api/#GET_api_mod_conversations_unread_count


Get moderating subreddits
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /api/mod/conversations/subreddits

*scope: modmail*

Return subreddits the current user is moderating that have modmail enabled.

Returns a JSON object with one key: `subreddits`. Its value is an object that maps subreddit full ID36
strings (with prefix `t5_`) to objects that contain basic subreddit information.

E.g.,::

   {'subreddits': {'t5_g2xi6': {'communityIcon': '',
                                'keyColor': '#ddbd37',
                                'display_name': 'Pyprohly',
                                'name': 'Pyprohly',
                                'subscribers': 2,
                                'primaryColor': '',
                                'id': 't5_g2xi6',
                                'lastUpdated': '2021-10-01T16:12:40.150840+00:00',
                                'icon': None},
                   't5_15c8ty': {'communityIcon': '',
                                 'keyColor': '',
                                 'display_name': 'u/Pyprohly',
                                 'name': 'u_Pyprohly',
                                 'subscribers': 0,
                                 'primaryColor': '',
                                 'id': 't5_15c8ty',
                                 'lastUpdated': None,
                                 'icon': 'https://www.redditstatic.com/avatars/defaults/v2/avatar_default_4.png'},
                   ...}}


.. csv-table:: Subreddit information object
   :header: "Field","Type (hint)","Description"

   "id","string","The subreddit's full ID36 (with prefix `t5_`).

   Same as the `name` field on the :ref:`Subreddit schema <subreddit-schema>`."
   "name","string","The name of the subreddit.

   Same as the `display_name` field on the :ref:`Subreddit schema <subreddit-schema>`."
   "display_name","string","Same as `name` if a regular subreddit. If a user subreddit then the name is prefixed
   with `u/`."
   "keyColor","string","Same as the `key_color` field on the :ref:`Subreddit schema <subreddit-schema>`."
   "primaryColor","string","Same as the `primary_color` field on the :ref:`Subreddit schema <subreddit-schema>`."
   "subscribers","string","Same as the `subscribers` field on the :ref:`Subreddit schema <subreddit-schema>`."
   "lastUpdated","string?","An ISO8601 date string."
   "icon","string?",""
   "communityIcon","string","Same as the `community_icon` field on the :ref:`Subreddit schema <subreddit-schema>`. Can be empty string."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","There is no user context."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_mod_conversations_subreddits


Modmail Conversation
====================

Actions
-------

Get conversations
~~~~~~~~~~~~~~~~~

.. http:get:: /api/mod/conversations

*scope: modmail*

Retrieve a list of conversations by mailbox.

The conversation objects reference only the lastest message.
Use `GET /api/mod/conversations/{convo_id36}` to retrieve all the messages.

Returns a JSON object with 4 keys:

* `viewerId` (string): A string of the full ID36 (`t2_` prefixed) of the current user.
* `conversationIds` (string array): A string array of conversation IDs. The IDs reference the keys in the `conversations` object.
   The order is not the same as in `conversations`. Use this order for iteration.
* `conversations` (object): An object mapping IDs to conversation info objects.
* `messages` (object): An object mapping ID36s to message objects. The conversation objects within the
   `conversations` key reference these messages.

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "after","string","A conversation ID36 as a pagination cursor.
   Pass the last ID36 in `conversationIds` to get the next page."
   "limit","integer","The number of results to retrieve."
   "state","string","The mailbox in which to retrieve conversations for. If not specified, defaults to `all`.

   One of: `all`, `inbox`, `new`, `inprogress`, `archived`, `appeals`, `join_requests`, `highlighted`,
   `mod`, `notifications`, `default`, `filtered`.

   Note: the `default` and `filtered` mailboxes are not accessible though the UI.

   Default: `all`."
   "entity","string","A comma delimited list of subreddit names in which to get conversations for.
   Defaults to all moderated subreddits.

   Cannot be an empty, otherwise a 504 HTTP error is returned after a few seconds delay."
   "sort","string","One of: `recent`, `mod`, `user`, `unread`. Default: `recent`."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "CONVERSATION_NOT_FOUND","404","The conversation ID36 specified by the `after` parameter does not exist.","
   ``{""fields"": [""after""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "
   "INVALID_OPTION","400","The value specified for `state` is invalid.","
   ``{""fields"": [""state""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "504","The string specified by `entity` is empty."

.. seealso:: https://www.reddit.com/dev/api/#GET_api_mod_conversations


.. _modmail-conversation-get:

Get
~~~

.. http:get:: /api/mod/conversations/{convo_id36}

*scope: modmail*

Get a conversation.

Returns a JSON object with 4 keys:

* `conversation` (object): Conversation info.
* `messages` (object): An object mapping ID36s to message objects.
* `modActions` (object): An object mapping action ID36s to mod action info objects.
* `user` (object): A user dossier. Empty object if conversation is an internal moderator discussion and
  there is no user subject.
* `participantSubreddit` (object):
  Aside from the extra `recentConvos` field, the information in this object is just identical
  to that of the `participantSubreddit` field on the conversation info object.

  Similarly, this object is empty when the `participantSubreddit` field on the conversation info object is empty.

  In addition to the fields described in the `participantSubreddit` on the conversation schema:

  * `recentConvos` (mapping object): Contains the same fields as those on the `recentConvos` field
    on the user dossier schema.

    Supposedly the information in this field is meant to be associated with the 'Recent Messages (with subreddit):'
    section in the UI but at the time of this writing the UI always seems to display "No recent messages".

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"

   "markRead","boolean","Mark retrieved conversations as read. Default: false."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "SUBREDDIT_NO_ACCESS","403","You do not have permission to access the specified conversation.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""SUBREDDIT_NO_ACCESS""}``
   "
   "CONVERSATION_NOT_FOUND","404","The specified conversation does not exist.","
   ``{""fields"": [""conversation_id""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#GET_api_mod_conversations_:conversation_id>`_


Create
~~~~~~

.. http:post:: /api/mod/conversations

*scope: modmail*

Create a new conversation.

Creates a conversation thread and the first message. Use this endpoint to create a conversation with
a user, or an internal moderator discussion.

If `to` is not specified, is an empty string, or names a user who is a moderator of the subreddit
specified by the `srName` parameter, the conversation will be a moderator discussion.

Returned object is the same as that of :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`. E.g.:

- `conversation` (object): The newly created conversation object.
- `messages` (object): Mapping of a message ID36 to the newly created message.
- `modActions` (object): Always empty.
- `user` (...): Will be empty if an internal mod conversation.
- `participantSubreddit` (...): Will be empty if an internal mod conversation.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "srName","string","The name of the subreddit in which to create the conversation for."
   "to","string","The modmail recipient name.

   Specify a user name, or a subreddit name prefixed with `r/`.

   To create a moderator conversation, don't specify this parameter, or set it to an empty string.

   If the specified user is a moderator of the subreddit, this parameter is ignored and an
   internal moderator conversation is created instead."
   "subject","string","A subject line for the conversation."
   "body","string","Markdown text."
   "isAuthorHidden","boolean","Whether to expose your user name to the recipient.

   By default the name is exposed. Default: false.

   The UI only offers the ""Hide my username"" option when sending to a user, but the
   option has some effect when creating an internal conversation: the user name will
   be shown but have ""[hidden]"" next to it.

   If this parameter is true when creating a to-subreddit conversation then an API error
   will occur (`UNKNOWN_ERROR`).
   "

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "BAD_SR_NAME","400","The `srName` parameter was not specified or was empty.","
   ``{""fields"": [""srName""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "
   "SUBREDDIT_NOEXIST","400","The subreddit specified by the `srName` parameter does not exist.","
   ``{""fields"": [""srName""], ""explanation"": ""Hmm, that community doesn't exist. Try checking the spelling."", ""message"": ""Bad Request"", ""reason"": ""SUBREDDIT_NOEXIST""}``
   "
   "NO_TEXT","400","* The `subject` parameter was empty or not specified.

   * The `body` parameter was empty or not specified.
   ","
   ``{""fields"": [""subject""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "
   "TOO_LONG","400","* The value specified for `subject` must be 100 characters or fewer
      (despite error message saying under 100).

   * The value specified for `body` must be 10000 characters or fewer
      (despite error message saying under 10000).
   ","
   ``{""fields"": [""subject""], ""explanation"": ""This field must be under 100 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "
   "MUTED_FROM_SUBREDDIT","400","The user specified by `to` is muted from the subreddit.","
   ``{""fields"": [""to""], ""explanation"": null, ""message"": ""Bad Request"", ""reason"": ""MUTED_FROM_SUBREDDIT""}``
   "
   "UNKNOWN_ERROR","400","Attempted to create a to-subreddit conversation when `isAuthorHidden` was true.","
   ``{""explanation"": ""Cannot hide author for subreddit-to-subreddit conversations."", ""message"": ""Bad Request"", ""reason"": ""UNKNOWN_ERROR""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations>`_


Reply
~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}

*scope: modmail*

Create a new message on an existing conversation.

Returned object is the same as that of :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "body","string","Markdown text."
   "isAuthorHidden","boolean","Whether to hide your user name to the recipient. Default: false.

   In an internal mod conversation, the UI will not offer the ""Hide my username"" option,
   but the option has some effect in that ""[hidden]"" will be shown next to the name.

   This open cannot be used to reply a to-subreddit conversation. An API error (`UNKNOWN_ERROR`) will occur.
   The UI does not give an option to hide a reply to a to-subreddit conversation.
   "
   "isInternal","boolean","Whether to create a private moderator note. Default: false.

   This option has no effect in an internal moderator conversation.

   It's not possible to create a hidden private mod note. If true when `isAuthorHidden` is also true,
   an API will occur (`UNKNOWN_ERROR`).
   "

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "CONVERSATION_NOT_FOUND","404","The specified conversation does not exist.","
   ``{""fields"": [""conversation_id""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "
   "SUBREDDIT_NO_ACCESS","403","You do not have permission to access the specified conversation.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""SUBREDDIT_NO_ACCESS""}``
   "
   "NO_TEXT","400","The `body` parameter was empty or not specified.","
   ``{""fields"": [""body""], ""explanation"": ""we need something here"", ""message"": ""Bad Request"", ""reason"": ""NO_TEXT""}``
   "
   "TOO_LONG","400","The value specified for `body` must be 10000 characters or fewer
   (despite error message saying under 10000).","
   ``{""fields"": [""body""], ""explanation"": ""This field must be under 10000 characters"", ""message"": ""Bad Request"", ""reason"": ""TOO_LONG""}``
   "
   "UNKNOWN_ERROR","400","
   1. Both `isAuthorHidden` and `isInternal` were true.

   2. Attempted to reply a to-subreddit conversation when `isAuthorHidden` was true.
   ","
   (1): ``{""explanation"": ""Internal messages cannot have a hidden author"", ""message"": ""Bad Request"", ""reason"": ""UNKNOWN_ERROR""}``

   (2): ``{""explanation"": ""Cannot hide author for subreddit-to-subreddit conversations."", ""message"": ""Bad Request"", ""reason"": ""UNKNOWN_ERROR""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id>`_


.. _modmail-mark-as-read:

Mark as read/unread
~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/read
.. http:post:: /api/mod/conversations/unread

*scope: modmail*

Mark conversations as read.

ID36s specified in the `conversationIds` list that do not exist will be ignored.
If any of the ID36s refer to a conversation you do not have permission over, an `INVALID_CONVERSATION_ID`
API error will occur and none of the conversations will be processed.

The `conversationIds` limit is unknown. Clients should assume a limit of 100 items.

Returns zero bytes on success.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "conversationIds","string","A comma separated list of conversation ID36s."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "Must pass an id or list of ids.","400","The `conversationIds` parameter was not specified","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Bad Request"", ""reason"": ""Must pass an id or list of ids.""}``
   "
   "INVALID_CONVERSATION_ID","403","You do not have permission to mark as read one of the conversations
   specified in the `conversationIds` list.
   The operation is aborted and none of the items will be processed.","
   ``{""fields"": [""conversationIds""], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""INVALID_CONVERSATION_ID""}``
   "
   "UNKNOWN_ERROR","500","The `POST /api/mod/conversations/unread` endpoint was used and one of the IDs contained
   invalid characters. None of the items will be processed.","
   ``{""reason"": ""UNKNOWN_ERROR"", ""message"": ""Internal Server Error""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_read>`_
.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_unread>`_


Mark all as read
~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/bulk/read

*scope: modmail*

Mark all conversations across select mailboxes and subreddits as read.

Subreddit names specified in the `entity` list that do not exist will be ignored, but if
all the subreddits don't exist then a 500 HTTP error will occur. If any of the subreddits
are not moderated by you then a `BAD_SR_NAME` API error will occur, and none of the
conversations will be processed.

The `entity` limit is unknown. Clients should assume a limit of 100 subreddit names.

Returns the list of conversation ID36s (prefixed with `ModmailConversation_`) that were marked as read::

   {"conversation_ids": ["ModmailConversation_1nutdn", "ModmailConversation_1nustm", "ModmailConversation_1nusn0", "ModmailConversation_1nusmh", "ModmailConversation_1gfdx0", "ModmailConversation_1gr9d3"]}

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "state","string","One of: `all`, `appeals`, `notifications`, `inbox`, `filtered`, `inprogress`,
   `mod`, `archived`, `default`, `highlighted`, `join_requests`, `new`. Default: `all`."
   "entity","string","A comma separated list of subreddit names. This parameter is mandatory."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "INVALID_OPTION","400","The value specified for `state` was invalid.","
   ``{""fields"": [""state""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "
   "BAD_SR_NAME","400","* (1) The `entity` parameter was not specified or was empty.

   * (2) One of the subreddits specified in the `entity` parameter is not a subreddit you have access to.
   ","
   (1) ``{""fields"": [""entity""], ""explanation"": ""This community name isn't recognizable. Check the spelling and try again."", ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``

   (2) ``{""fields"": [""entity""], ""explanation"": null, ""message"": ""Bad Request"", ""reason"": ""BAD_SR_NAME""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","None of the subreddit names specified by `entity` exist."

.. note::
   The documentation incorrectly lists this endpoint as `POST /api/mod/bulk_read`, which does not exist.

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_bulk_read>`_


Highlight/unhighlight
~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/highlight
.. http:delete:: /api/mod/conversations/{convo_id36}/highlight

*scope: modmail*

Mark a conversation as highlighted.

The mod actions list in the output will include this action.

Redundant duplicate actions will register as duplicate entries in the conversation.

Returned object is the same as that of :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "CONVERSATION_NOT_FOUND","404","The conversation ID36 does not exist.","
   ``{""fields"": [""conversation_id""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "
   "SUBREDDIT_NO_ACCESS","403","The subreddit associated with the conversation ID36 is not moderated by you.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""SUBREDDIT_NO_ACCESS""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#DELETE_api_mod_conversations_:conversation_id_highlight>`_


Archive/unarchive
~~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/archive
.. http:post:: /api/mod/conversations/{convo_id36}/unarchive

*scope: modmail*

Archive a conversation.

The mod actions list in the output will include this action.

Redundant duplicate actions will register as duplicate entries in the conversation.

Returned object is the same as that of :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "CONVERSATION_NOT_FOUND","404","The conversation ID36 does not exist.","
   ``{""fields"": [""conversation_id""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "
   "INVALID_MOD_PERMISSIONS","403","The subreddit associated with the conversation ID36 is not moderated by you.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""INVALID_MOD_PERMISSIONS""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id_archive>`_


Approve/disapprove user
~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/approve
.. http:post:: /api/mod/conversations/{convo_id36}/disapprove

*scope: modmail*

Approve the user associated with a conversation.

Returned object is mostly the same as that of :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`
except the `participantSubreddit` field on the root and on the `conversation` object is missing.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "USER_REQUIRED","403","There is no user context.","
   ``{""explanation"": ""Please log in to do that."", ""message"": ""Forbidden"", ""reason"": ""USER_REQUIRED""}``
   "
   "CONVERSATION_NOT_FOUND","404","The conversation ID36 does not exist.","
   ``{""fields"": [""conversation_id""], ""explanation"": ""No conversation found."", ""message"": ""Not Found"", ""reason"": ""CONVERSATION_NOT_FOUND""}``
   "
   "INVALID_MOD_PERMISSIONS","403","The subreddit associated with the conversation ID36 is not moderated by you.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Forbidden"", ""reason"": ""INVALID_MOD_PERMISSIONS""}``
   "
   "CANT_RESTRICT_MODERATOR","400","There is no user associated with the conversation.","
   ``{""fields"": [null], ""explanation"": null, ""message"": ""Bad Request"", ""reason"": ""CANT_RESTRICT_MODERATOR""}``
   "
   "USER_DOESNT_EXIST","404","No user is associated with the given conversation.","
   ``{""fields"": [null], ""reason"": ""USER_DOESNT_EXIST"", ""message"": ""Not Found"", ""explanation"": ""that user doesn't exist""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id_approve>`_


.. _modmail-conversation-mute-user:

Mute/unmute user
~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/mute
.. http:post:: /api/mod/conversations/{convo_id36}/unmute

*scope: modmail*

Mute the user associated with a conversation.

Returned object has fields similar to that of
:ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`:

- `conversations`:
  Same as the `conversation` field on :ref:`GET /api/mod/conversations/{convo_id36} <modmail-conversation-get>`.

  Notice the key name is mistakenly plural.

  The `participantSubreddit` field is missing.
- `messages`: ...
- `modActions`: ...
- `user` (?object): Field will not exist if the mute state did not change.

This parameter table applies only when muting:

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "num_hours","integer","Either: 72, 168, 672. (Respectively: 3 days, 7 days, 28 days.) Default: 72 (3 days)."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "...","Same as in `POST /api/mod/conversations/{convo_id36}/approve`.","...","..."
   "INVALID_OPTION","400","The value specified by `num_hours` was invalid.","
   ``{""fields"": [""num_hours""], ""explanation"": ""that option is not valid"", ""message"": ""Bad Request"", ""reason"": ""INVALID_OPTION""}``
   "
   "USER_DOESNT_EXIST","404","No user is associated with the given conversation.","
   ``{""fields"": [null], ""reason"": ""USER_DOESNT_EXIST"", ""message"": ""Not Found"", ""explanation"": ""that user doesn't exist""}``
   "

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id_mute>`_


.. _modmail-conversation-shorten-user-ban:

Shorten user ban
~~~~~~~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/temp_ban

*scope: modmail*

Switch a permanent ban to a temporary one of the user associated with a conversation.

If the user is not permanently banned, an API error will be raised.

Returned object has fields similar to that of
:ref:`POST /api/mod/conversations/{convo_id36}/mute <modmail-conversation-mute-user>`:

- `conversations`
- `messages`
- `modActions`
- `user`: Field should always exist.

.. csv-table:: Form Data / URL Params
   :header: "Field","Type (hint)","Description"

   "duration","integer","The number of days the temporary ban should last. Specify an integer from 1 to 999.
   The UI has the options: 1, 3, 7, or 28 days."

|

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "...","Same as in `POST /api/mod/conversations/{convo_id36}/approve`.","...","..."
   "Participant must be banned.","422","The user associated with the conversation is not banned from the subreddit.","
   ``{""fields"": [null], ""reason"": ""Participant must be banned."", ""message"": ""Unprocessable Entity""}``
   "
   "Participant must be banned permanently.","422","The user associated with the conversation is not permanently banned from the subreddit.","
   ``{""fields"": [null], ""reason"": ""Participant must be banned permanently."", ""message"": ""Unprocessable Entity""}``
   "
   "BAD_NUMBER","400","The number specified by the `duration` parameter was not in range.","
   ``{""fields"": [""duration""], ""explanation"": ""that number isn't in the right range (1 to 999)"", ""message"": ""Bad Request"", ""reason"": ""BAD_NUMBER""}``
   "
   "USER_DOESNT_EXIST","404","No user is associated with the given conversation.","
   ``{""fields"": [null], ""reason"": ""USER_DOESNT_EXIST"", ""message"": ""Not Found"", ""explanation"": ""that user doesn't exist""}``
   "

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"

   "500","The `duration` parameter was not specified."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id_unban>`_


Unban user
~~~~~~~~~~

.. http:post:: /api/mod/conversations/{convo_id36}/unban

*scope: modmail*

Unban the user associated with a conversation from the subreddit.

Returned object is the same as
:ref:`POST /api/mod/conversations/{convo_id36}/temp_ban <modmail-conversation-shorten-user-ban>`.

.. csv-table:: API Errors
   :header: "Error","Status Code","Description","Example"

   "...","Same as in `POST /api/mod/conversations/{convo_id36}/approve`.","...","..."

.. seealso:: `<https://www.reddit.com/dev/api/#POST_api_mod_conversations_:conversation_id_unban>`_
