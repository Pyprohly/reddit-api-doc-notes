
Listings
########

.. _listings-overview:

Overview
********

Listings are a protocol for controlling pagination of Reddit content.
Endpoints that return listings share five common parameters:
`after`, `before`, `limit`, `count`, and `show`.
These parameters should be passes as URL query parameters and not form encoded data.

Listing JSON responses contain `after` and `before` fields which are equivalent to the
"next" and "prev" buttons on the site.

The common parameters:

* `after`/`before`: Only one should be specified. The value should be a full ID36.
  This is a cursor value that points to the start (before) or end (after) of the page listing.

* `limit`: The maximum number of items to return for a page.

  If not given, the authenticated user's default will be used.
  This is the \"display *n* links at once\" option under \"link options\"
  in the old Reddit preferences page. It is 25 by default.

  If not given and using a client credentials grant then the default is 25.

  The maximum is 100. Larger numbers will be clamped to the maximum.

  Do not depend on the number of results being fewer than the limit value to know whether your
  listing has reached the end. Use the `null` value of `after` instead.

* `count`: The total number of items already seen in this listing. old.reddit.com's HTML builder
  uses this to determine what numbering to display next to posts. The number specifies what
  number to start with. The `count` parameter is also used to determine if the `before` value
  should be populated.

* `show`: If `all` is passed as the value then filters such as
  "hide links that I have voted on" will be disabled.

To paginate through a listing, start by fetching the first page without specifying values for
`after` or `count`. The response will contain an `after` value which you can pass in as the
`after` value in the next request.

It is a good idea, but not required, to send an updated value for `count` in each request.
It should be set to the total number of items seen already.

The last page will have a `after` key with a `null` value set. Use this to tell if the page
is the last page of the listing.

The first page will have a `before` value of `null`. You can actually induce the API to fill
out the `before` value on the first page by passing a positive `count` integer value though.
If the listing is hot sorted and thus can contain stickied/pinned posts then the count value
must be greater than the number of stickied posts, and the `before` value will be set to the
first stickied post.

Below is a list of SOME listing implementations. It is not complete because some implementations
are detailed in their relevant topic.


Implementations
***************

TODO: Move everything out of here. Putting everything in one place was a bad idea.

Frontpage
=========

Main listings
-------------

Variants
~~~~~~~~

*Best*
^^^^^^

.. http:get:: /
.. http:get:: /best

*Hot*
^^^^^

.. http:get:: /hot

*Rising*
^^^^^^^^

.. http:get:: /rising

*Top*
^^^^^

.. http:get:: /top

*New*
^^^^^

.. http:get:: /new

*Controversial*
^^^^^^^^^^^^^^^

.. http:get:: /controversial

*Gilded*
^^^^^^^^

.. http:get:: /gilded

A listing of comments and submissions.

.. _frontpage-overview:

Overview
~~~~~~~~

*scope: read*

Get a submission listing of your frontpage. This will include submissions from your list of
subscribed subreddits, otherwise, if not logged in, Reddit will decide which subreddits to
retrieve submissions from to populate the listing.

The listings contain only submission objects, except as indicated otherwise.

.. _frontpage-listings-additional-url-params:

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr_detail","boolean","Whether to include in each submission an `sr_detail` key that holds
   an object containing subreddit information in which the submission/comment item belongs.

   This subreddit object has different fields than the ones returned from `/api/info`.
   It has half as many fields and also a couple different ones.

   Note that submission and comment objects already contain the name and ID of the containing
   subreddit which is enough information to fetch a full subreddit object from `/api/info`.

   A string that starts with `0` or `F` or `f` is treated as a falsy string and explicitly
   disables this option. All other strings are truthy."

Additional URL params for *Hot*:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "g","string","Geo filter.

   Valid options:
   GLOBAL, US, AR, AU, BG, CA, CL, CO, HR, CZ, FI, FR, DE, GR, HU, IS, IN, IE, IT, JP,
   MY, MX, NZ, PH, PL, PT, PR, RO, RS, SG, ES, SE, TW, TH, TR, GB, US_WA, US_DE, US_DC,
   US_WI, US_WV, US_HI, US_FL, US_WY, US_NH, US_NJ, US_NM, US_TX, US_LA, US_NC, US_ND,
   US_NE, US_TN, US_NY, US_PA, US_CA, US_NV, US_VA, US_CO, US_AK, US_AL, US_AR, US_VT,
   US_IL, US_GA, US_IN, US_IA, US_OK, US_AZ, US_ID, US_CT, US_ME, US_MD, US_MA, US_OH,
   US_UT, US_MO, US_MN, US_MI, US_RI, US_KS, US_MT, US_MS, US_SC, US_KY, US_OR, US_SD

   Default: `GLOBAL`
   "

Additional URL params for *Top* and *Controversial*:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "t","string","Time filter.

   Valid options:
   `all`, `hour`, `day`, `week`, `month`, `year`

   Default: `all`
   "

.. seealso:: https://www.reddit.com/dev/api/#section_listings

.. _front-page-new-comments:

*New comments*
--------------

.. http:get:: /comments

A listing of comments.

This listing does not support the `sr_detail` parameter.

Comment objects have the following extra fields:

.. _frontpage-new-comments-comment-object:

.. csv-table:: Comment Object extra fields
   :header: "Field","Type (hint)","Description"
   :escape: \

   "num_comments","integer","The number of comments in the submission containing this comment."
   "quarantine","boolean","Whether this comment is in a quarantined subreddit."
   "over_18","boolean","Whether the submission of this comment has been marked as NSFW."
   "link_title","string","Title of the submission containing this comment."
   "link_author","string","The submission redditor name. Possibly `[removed]` if the post was removed
   or `[deleted]` if the post was removed by the author."
   "link_url","string","Equivalent to the Submission object `url` field. If a text post, it is the url of the submission. If a link post, it is the url of the link. Also see permalink."
   "link_permalink","string","The url of the submission. Unlike the Submission object `permalink` field this url will include the domain name."


Subreddit threads
=================

Main listings
-------------

Variants
~~~~~~~~

*Hot*
^^^^^

.. http:get:: /r/{subreddit}
.. http:get:: /r/{subreddit}/hot
.. http:get:: /r/{subreddit}/best

(`/best` is the same as `/hot`.)

*Rising*
^^^^^^^^

.. http:get:: /r/{subreddit}/rising

*Top*
^^^^^

.. http:get:: /r/{subreddit}/top

*New*
^^^^^

.. http:get:: /r/{subreddit}/new

*Controversial*
^^^^^^^^^^^^^^^

.. http:get:: /r/{subreddit}/controversial

*Gilded*
^^^^^^^^

.. http:get:: /r/{subreddit}/gilded

A listing of comments and submissions.

Overview
~~~~~~~~

*scope: read*

If the sort component of the URL is omitted it is treated the same as `/hot`
(unlike frontpage listings where the default is *best*).

The hot listing may include pinned posts at the start of the listing.

`/best` returns the same listing as `/hot`.

The listings contain only submission objects, except as indicated otherwise.

All 'additional URL param' tables in the :ref:`frontpage listings section <frontpage-overview>` apply.

.. seealso:: https://www.reddit.com/dev/api/#section_listings

.. _subreddit-new-comments:

*New comments*
--------------

.. http:get:: /r/{subreddit}/comments

A listing of comments. This listing does not support the `sr_detail` parameter.

Comment objects have extra fields. See :ref:`here <frontpage-new-comments-comment-object>`.


Account
=======

User listings
-------------

Variants
~~~~~~~~

.. _account-listings-friends:

*Friends*
^^^^^^^^^

.. http:get:: /api/v1/me/friends
.. http:get:: /prefs/friends

`GET /prefs/friends` is the same as `GET /api/v1/me/friends` but it returns an array containing
two 'UserList' structures. The first structure matches that of `GET /api/v1/me/friends`.
The second one is always empty, nobody knows what it's for.

.. _account-listings-blocked:

*Blocked*
^^^^^^^^^

.. http:get:: /prefs/blocked

.. note::
   Although `/api/v1/me/blocked` is documented the endpoint doesn't exist and requesting against it returns 404.

*Trusted*
^^^^^^^^^

.. http:get:: /prefs/trusted

Returns a list of two 'UserList' list structures. The first list structure is the blocked users
list (same as returned by `/prefs/blocked`). The second list is the trusted users list.

See `/api/add_whitelisted` for adding a user to the trusted users list.

*Messaging*
^^^^^^^^^^^

.. http:get:: /prefs/messaging

Returns a list of two 'UserList' structures.
The first structure contains a list of blocked users (same as returned by `GET /prefs/blocked`).
The second structure contains a list of trusted users (same as returned by `GET /prefs/trusted`).

Overview
~~~~~~~~

*scope: read*

Listings contain user objects that have the following fields:

.. csv-table:: User Item Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "date","float","Unix timestamp of when this item was added to the list. Will always be a whole number."
   "rel_id","string","Some unknown string. E.g., `r9_1w4acm`"
   "name","string","The name of the user."
   "id","string","The full ID of the user. E.g., `t2_4x25quk`"


|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "500","The `sr_detail` parameter was used and its value is truthy (matches `/^[^fF0]/`)."

If the client is not logged in then the endpoints return the string `"{}"`.
Notice this is a string of an empty JSON object.

Also see :ref:`User listings <user-listings>` for more relevant listings.

.. seealso:: `<https://www.reddit.com/dev/api/#GET_prefs_{where}>`_


Subreddit listings
------------------

Variants
~~~~~~~~

*Subscribed*
^^^^^^^^^^^^

.. http:get:: /subreddits/mine/subscriber

Subreddits the user is subscribed to.

*Contributor*
^^^^^^^^^^^^^

.. http:get:: /subreddits/mine/contributor

Subreddits the user is an approved user in.

*Moderator*
^^^^^^^^^^^

.. http:get:: /subreddits/mine/moderator

Subreddits the user is a moderator of.

*Streams*
^^^^^^^^^

.. http:get:: /subreddits/mine/streams

Subscribed to subreddits that contain hosted video links.

Overview
~~~~~~~~

*scope: mysubreddits*

Listings return Subreddit objects.

If the client is not logged in then the endpoints return the string `"{}"`.
Notice this is a string of an empty JSON object.

See :ref:`Additional URL Params <frontpage-listings-additional-url-params>`.


Subreddit
=========

Main listings
-------------

Variants
~~~~~~~~

*Popular*
^^^^^^^^^

.. http:get:: /subreddits
.. http:get:: /subreddits/popular

*New*
^^^^^

.. http:get:: /subreddits/new

*Default*
^^^^^^^^^

.. http:get:: /subreddits/default

*Premium*
^^^^^^^^^

.. http:get:: /subreddits/premium
.. http:get:: /subreddits/gold

Returns an empty listing structure if the user does not have Reddit Premium.

Overview
~~~~~~~~

*scope: read*

Subreddit listings.

Returns a 'Listing' listing kind.

Does not support `sr_detail` param (that would be silly).

User subreddit listings
-----------------------

Variants
~~~~~~~~

*Popular*
^^^^^^^^^

.. http:get:: /users/popular

*New*
^^^^^

.. http:get:: /users/new

Overview
~~~~~~~~

*scope: read*

Get user subreddits.

'Popular' sorts on the activity of the subreddit.
'New' sorts the subreddits on creation date, newest first.


Submission
==========

*Duplicates*
------------

.. http:get:: [/r/{subreddit}]/duplicates/{article}

*scope: read*

Return a listing of 'other discussions' for the submission.

`{subreddit}` can be obmitted. If given it must be correctly match the subreddit for the
article ID otherwise an empty listing will be returned.
`{article}` is a submission ID36.

See :ref:`Additional URL Params <frontpage-listings-additional-url-params>`.

More additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "crossposts_only","boolean","If truthy (any string matching `/^[^0Ff]/`), return only crossposts."
   "sort","string","One of `num_comments`, `new`."
   "sr","string","Filter by subreddit name. If the subreddit name specified doesn't exist then
   no filter will be applied and all posts will be returned."

|

.. csv-table:: HTTP Errors
   :header: "Status Code","Description"
   :escape: \

   "404","The article ID could not be found."
