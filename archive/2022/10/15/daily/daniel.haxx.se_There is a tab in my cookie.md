---
title: There is a tab in my cookie
url: https://daniel.haxx.se/blog/2022/10/14/there-is-a-tab-in-my-cookie/
source: daniel.haxx.se
date: 2022-10-15
fetch_date: 2025-10-03T19:56:55.163024
---

# There is a tab in my cookie

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/chocolate-chip-cookies.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# There is a tab in my cookie

[October 14, 2022](https://daniel.haxx.se/blog/2022/10/14/there-is-a-tab-in-my-cookie/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [3 Comments](https://daniel.haxx.se/blog/2022/10/14/there-is-a-tab-in-my-cookie/#comments)

An HTTP *cookie*, is just a name + value pair sent from the server to the client. That pair is stored and is sent back to the server in subsequent requests when conditions match.

Cookies were first invented and used in the 1990s. Sources seem to agree that the first browser to support them, was Netscape 0.9beta released in September 1994. Internet Explorer added support in October 1995.

After many years and several failed specification attempts, they were eventually documented in [RFC 6265](https://daniel.haxx.se/blog/2011/04/28/the-cookie-rfc-6265/) in 2011. They have been debated, criticized and misunderstood since virtually forever. Mostly because of the abuse/tracking they (used to?) allow in browsers. Less so because of how they actually work over the wire.

## curl

curl has supported cookies since the 1990s as well (October 1998 to be specific), and it is a frequently used feature among curl users everywhere. Not the least because the login pattern of the web has become HTTP POST with credentials with a session cookie returned on success – and curl is often used to mimic or reproduce such operations to allow for automated processes and more.

For curl, it is important to remain interoperable and compatible with cookies the same way browsers do them so that users can keep doing these things.

## What to accept

Not very long ago, I blogged about [a cookie change we had to do](https://daniel.haxx.se/blog/2022/09/05/a-bug-that-was-23-years-old-or-not/) because curl’s former liberal attitude towards what a cookie might contain turned out to be a possible vector for mischief. That flaw was basically a direct result of curl never totally adapting to the language in RFC 6265 because we typically do not change what seems to work and has not been reported to be wrong.

In that curl change, we started rejecting incoming cookies that contain “control codes” but we let ASCII code 9 through. ASCII code 9 is the tab character. Generally considered *white space*. We let it through because we checked the source code for two major browsers and they since they do, curl does as well.

## Tab where?

But accepting tabs in the cookie line is one thing. The next question then comes where exactly in the cookie line should it be acceptable?

In the currently ongoing security audit for curl, our friends at [Trail of Bits](https://www.trailofbits.com/) figured out that if a cookie is sent to curl with a tab in the name (literally inside the name and not before or after, like foo<tab>bar) curl would save that wrongly if saved to a file. This, because curl saves cookies in a tab-separated file format, the so called Netscape cookie file format, and it has no escape mechanism or anything. A tab in the cookie name causes the cookie to later get treated wrongly when the file is later loaded again.

## Interop status

The file format curl uses for saving cookies is the same as the original format Netscape and then early Firefox used back in the old days. Since this format does not support tabs, I believe it is reasonable to assume the early browsers did not accept tabs in names or content.

I checked how (current) Chrome and Firefox handle cookies like this by creating a test page that sends cookies to the browser.

Chrome rejects cookies with tabs in name or content. They are simply not accepted or stored.

Firefox rejects cookies with tabs in name, but strangely enough it *strips* tabs from the content and otherwise let them through.

(Safari doesn’t work on Linux so I ignored that)

This, even if my reading of the RFC 6265 seems to say that they should be fine. They should be kept when “internal” to a name or content. I believe curl followed the spec here better than the browsers.

But clearly **tabs in cookie names or content is not an interoperable concept on the web**.

## Adding or removing

With all this in my luggage, I decided to [bring this question to the team working on the cookie spec update](https://github.com/httpwg/http-extensions/issues/2262). The [rfc6265bis](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-10) effort.

I figured that this non-interoperable state and support situation could be worth highlighting or perhaps make a bit stricter in the spec update.

In that issue on GitHub, I was instead informed that recently changed language in their RFC draft rather made browser implementers keen on *adding* support for this kind of tabs in cookies.

Instead of admitting defeat and documenting that tabs in cookie names and values do not work correctly, we would rather continue limping along pretending this will work.

The HTTP community have supported cookies for almost **thirty years** without tabs working correctly inside cookies.

Adding (clearer) support for them in a spec would be good in the sense that more defined behavior is a good thing, but since we have decades of this non or perhaps spotty support the already deployed software and long tail of clients will not adapt to any such new wording rapidly. Even if accepted in the new spec, it will take ages until cookies could be done interoperable with tabs inside.

I believe we are better off just documenting that tabs **SHOULD NOT** be used in cookie name or content as they will not interop. Because that is the truth and will be for a long time no matter what we do today or tomorrow.

My comments in that issue at least seem to have brought reason for maybe reconsider the draft wording. Maybe.

## Why!

Someone might ask the excellent question “*why* would anyone want to use a tab in the name or content?”, but quite frankly, I cannot think of any good or legitimate reason other than maybe laziness or a lack of proper filtering.

There is no sound technical reason why this needs to be done.

## An executive decision

To fix the breakage curl does when saving cookies like this, and to align better with *existing* browsers, we decided to rather [make curl reject incoming cookies that have tabs in names or content](https://github.com/curl/curl/pull/9659). Starting in the next release: 7.86.0.

We needed to do *something*. I believe going with the more strict approach is the better one here and now.

If the rfc6265bis draft ends up ultimately keeping the language “encouraging” tab support and browser authors decide to follow, then I presume we will have reason to revisit this decision later on and perhaps take curl in the other direction instead. I think we can handle that, even if I believe it would be the wrong thing for the ecosystem.

## Credits

Cookie image by [StockSnap](https://pixabay.com/users/stocksnap-894430/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2599637) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2599637)

[Chrome](https://daniel.haxx.se/blog/tag/chrome/)[cookies](https://daniel.haxx.se/blog/tag/cookies/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Firefox](https://daniel.haxx.se/blog/tag/firefox/)

# Post navigation

[Previous PostThe first 300 setopts](https://daniel.haxx.se/blog/2022/09/28/the-first-300-setopts/)[Next PostRewriting...