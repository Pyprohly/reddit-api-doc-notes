
Frontpage listings
------------------

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
