---
title: no strcpy either
url: https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/
source: daniel.haxx.se
date: 2025-12-29
fetch_date: 2025-12-30T03:25:53.034060
---

# no strcpy either

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/10/sourcecode.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# no strcpy either

[December 29, 2025](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/#respond)

Some time ago I mentioned that we went through the curl source code and eventually got rid of all `strncpy`() calls.

strncpy() is a weird function with a crappy API. It might not null terminate the destination and it *pads* the target buffer with zeroes. Quite frankly, most code bases are probably better off completely avoiding it because each use of it is a potential mistake.

In that particular rewrite when we made strncpy calls extinct, we made *sure* we would either copy the full string properly or return error. It is rare that copying a partial string is the right choice, and if it is, we can just as well `memcpy` it and handle the null terminator explicitly. This meant no case for using strlcpy or anything such either.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/12/Screenshot-2025-12-29-at-17-08-28-curl-Project-status-dashboard.png)

strncpy density in curl over time

## But strcpy?

strcpy however, has its valid uses and it has a less bad and confusing API. The main challenge with strcpy is that when using it we do not specify the length of the target buffer nor of the source string.

This is normally not a problem because in a C program `strcpy` should only be used when we have full control of both.

But *normally* and *always* are not necessarily the same thing. We are but all human and we all do mistakes. Using strcpy implies that there is at least one or maybe two, buffer size checks done prior to the function invocation. In a good situation.

Over time however – let’s imagine we have code that lives on for decades – when code is maintained, patched, improved and polished by many different authors with different mindsets and approaches, those size checks and the function invoke may glide apart. The further away from each other they go, the bigger is the risk that something happens in between that nullifies one of the checks or changes the conditions for the strcpy.

## Enforce checks close to code

To make sure that the size checks cannot be separated from the copy itself we introduced a string copy replacement function the other day that takes the *target buffer*, *target size*, *source buffer* and *source string length* as arguments and only if the copy can be made and the null terminator also fits there, the operation is done.

This made it possible to implement the replacement using memcpy(). Now we can completely ban the use of strcpy in curl source code, like we already did strncpy.

Using this function version is a little more work and more cumbersome than strcpy since it needs more information, but we believe the upsides of this approach will help us have an oversight for the extra pain involved. I suppose we will see how that will fare down the road. Let’s come back in a decade and see how things developed!

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/12/Screenshot-2025-12-29-at-17-08-50-curl-Project-status-dashboard.png)

strcpy density in curl over time

```
void curlx_strcopy(char *dest,
                   size_t dsize,
                   const char *src,
                   size_t slen)
{
  DEBUGASSERT(slen < dsize);
  if(slen < dsize) {
    memcpy(dest, src, slen);
    dest[slen] = 0;
  }
  else if(dsize)
    dest[0] = 0;
}
```

[the strcopy source](https://github.com/curl/curl/blob/master/lib/curlx/strcopy.c)

## AI slop

An additional minor positive side-effect of this change is of course that this should effectively prevent the AI chatbots to report strcpy uses in curl source code and insist it is insecure if anyone would ask (as people still apparently do). It has been proven numerous times already that strcpy in source code is like a honey pot for generating hallucinated vulnerability claims.

Still, this will just make them find something else to make up a report about, so there is probably no net gain. AI slop is not a game we can win.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostA curl 2025 review](https://daniel.haxx.se/blog/2025/12/23/a-curl-2025-review/)

### Leave a Reply [Cancel reply](/blog/2025/12/29/no-strcpy-either/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
1one42six

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/)
  December 29, 2025
* [A curl 2025 review](https://daniel.haxx.se/blog/2025/12/23/a-curl-2025-review/)
  December 23, 2025
* [20,000 issues on GitHub](https://daniel.haxx.se/blog/2025/12/16/20000-issues-on-github/)
  December 16, 2025
* [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/)
  November 13, 2025
* [curl 8.17.0](https://daniel.haxx.se/blog/2025/11/05/curl-8-17-0/)
  November 5, 2025
* [Yes really, curl is still developed](https://daniel.haxx.se/blog/2025/11/04/yes-really-curl-is-still-developed/)
  November 4, 2025

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27356)
* [Verisimilitude](http://verisimilitudes.net) on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27355)
* Willly on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27353)
* Arjun B on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27352)
* Giga on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27351)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27350)
* [Dr. Jochen L. Leidner](https://jochenleidner.com) on [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/comment-page-1/#comment-27349)
* [Daniel Stenberg](https://daniel.haxx.se/) on [AIxCC curl details](https://daniel.haxx.se/blog/2025/10/22/aixcc-curl-details/comment-page-1/#comment-27348)
* [Stephen Paulger](https://newspeak.org.uk) on [AIxCC curl details](https://daniel.haxx.se/blog/2025/10/22/aixcc-curl-details/comment-page-1/#comment-27347)
* Jesse on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27345)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

December 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| 15 | [16](https://daniel.haxx.se/blog/202...