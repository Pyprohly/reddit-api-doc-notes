
Listings
========

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
