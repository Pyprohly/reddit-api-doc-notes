
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

.. http:get:: [/]
.. http:get:: /best
.. http:get:: /hot
.. http:get:: /rising
.. http:get:: /new
.. http:get:: /top
.. http:get:: /controversial
.. http:get:: /gilded

*scope: read*

If the URL path is `/` (or omitted entirely), it is treated the same as `/best`.

Get a submission listing of your frontpage. This will include submissions from your list of
subscribed subreddits, otherwise, if not logged in, Reddit will decide which subreddits to
retrieve submissions from to populate the listing.

Additional URL Params:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "sr_detail","string","Whether to include in each submission an `sr_detail` key that maps
   to an object containing subreddit information in which the submission item belongs.

   A string that starts with `0` or `F` or `f` is treated as a falsy string and explicitly
   disables this option. All other strings are truthy."

Additional URL Params for `/hot`:

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

Additional URL Params for `/top` and `/controversial`:

.. csv-table:: URL Params
   :header: "Field","Type (hint)","Description"
   :escape: \

   "t","string","Time filter.

   Valid options:
   `all`, `hour`, `day`, `week`, `month`, `year`

   Default: `all`
   "


Subreddit submission listings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

`/best` returns the same listing as `/hot`.

The listings contain submission objects except for `/gilded` which can contain
a mix of submission and comment objects.
