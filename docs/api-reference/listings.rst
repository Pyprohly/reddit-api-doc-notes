
Listings
========

Overview
--------

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


Listing implementations
-----------------------

Frontpage listings
^^^^^^^^^^^^^^^^^^

Variants
~~~~~~~~

*Best*
""""""

.. http:get:: /
.. http:get:: /best

*Hot*
"""""

.. http:get:: /hot

*Rising*
""""""""

.. http:get:: /rising

*New*
"""""

.. http:get:: /new

*Top*
"""""

.. http:get:: /top

*Controversial*
"""""""""""""""

.. http:get:: /controversial

*Gilded*
""""""""

.. http:get:: /gilded

.. _frontpage_overview:

Overview
~~~~~~~~

*scope: read*

If the URL path is `/` (or omitted entirely), it is treated the same as `/best`.

Get a submission listing of your frontpage. This will include submissions from your list of
subscribed subreddits, otherwise, if not logged in, Reddit will decide which subreddits to
retrieve submissions from to populate the listing.

Additional URL params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr_detail","string","Whether to include in each submission an `sr_detail` key that maps
   to an object containing subreddit information in which the submission item belongs.

   A string that starts with `0` or `F` or `f` is treated as a falsy string and explicitly
   disables this option. All other strings are truthy."

Additional URL params for `/hot`:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "g","string","Geo filter.

   Valid options:
   GLOBAL, US, AR, AU, BG, CA, CL, CO, HR, CZ, FI, GR, HU, IS, IN, IE, JP, MY, MX, NZ,
   PH, PL, PT, PR, RO, RS, SG, SE, TW, TH, TR, GB, US_WA, US_DE, US_DC, US_WI, US_WV,
   US_HI, US_FL, US_WY, US_NH, US_NJ, US_NM, US_TX, US_LA, US_NC, US_ND, US_NE, US_TN,
   US_NY, US_PA, US_CA, US_NV, US_VA, US_CO, US_AK, US_AL, US_AR, US_VT, US_IL, US_GA,
   US_IN, US_IA, US_OK, US_AZ, US_ID, US_CT, US_ME, US_MD, US_MA, US_OH, US_UT, US_MO,
   US_MN, US_MI, US_RI, US_KS, US_MT, US_MS, US_SC, US_KY, US_OR, US_SD

   Default: `GLOBAL`
   "

Additional URL params for `/top` and `/controversial`:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "t","string","Time filter.

   Valid options:
   `all`, `hour`, `day`, `week`, `month`, `year`

   Default: `all`
   "

.. seealso:: https://www.reddit.com/dev/api/#section_listings


Subreddit submission listings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variants
~~~~~~~~

*Hot*
"""""

.. http:get:: /r/{subreddit}
.. http:get:: /r/{subreddit}/hot

*Best*
""""""

.. http:get:: /r/{subreddit}/best

*Rising*
""""""""

.. http:get:: /r/{subreddit}/rising

*Top*
"""""

.. http:get:: /r/{subreddit}/top

*New*
"""""

.. http:get:: /r/{subreddit}/new

*Controversial*
"""""""""""""""

.. http:get:: /r/{subreddit}/controversial

*Gilded*
""""""""

.. http:get:: /r/{subreddit}/gilded

Overview
~~~~~~~~

*scope: read*

If the sort component of the URL is omitted it is treated the same as `/hot`
(unlike frontpage listings where the default is *best*).

The hot listing may include pinned posts at the start of the listing.

`/best` returns the same listing as `/hot`.

The listings contain submission objects. `/gilded` is a
a mix of submission and comment objects.

All the 'additional URL param' tables in the :ref:`frontpage listings section <frontpage_overview>` apply.

.. seealso:: https://www.reddit.com/dev/api/#section_listings


Account listings
^^^^^^^^^^^^^^^^

Variants
~~~~~~~~

*Friends*
"""""""""

.. http:get:: /api/v1/me/friends
.. http:get:: /prefs/friends

`/prefs/friends` is the same as `/api/v1/me/friends` but it returns a list of two
'UserList' listing structures where the second one is empty. The first listing
structure matches that of `/api/v1/me/friends`.

*Blocked*
"""""""""

.. http:get:: /prefs/blocked

.. note::
   Although `/api/v1/me/blocked` is documented requesting against this endpoint returns a 404.

*Trusted*
"""""""""

.. http:get:: /prefs/messaging

Returns a list of two 'UserList' listing structures. The fist listing structure is the blocked users
list (same as returned by `/prefs/blocked`). The second listing is the trusted users list.

See `/api/add_whitelisted` for adding a user to the trusted users list.

Overview
~~~~~~~~

If the client is not logged in then the endpoints return the string `"{}"`.
Notice this is a string of an empty JSON object.

The user objects contained in the listings have the following fields:

.. csv-table:: User Item Object
   :header: "Field","Type (hint)","Description"
   :escape: \

   "date","float","Unix timestamp of when this item was added to the list. Will always be a whole number."
   "rel_id","string","Unknown. E.g., `r9_1w4acm`"
   "name","string","The name of the user."
   "id","string","The full ID of the user. E.g., `t2_4x25quk`"

Also see User listings for more relevant listings.
