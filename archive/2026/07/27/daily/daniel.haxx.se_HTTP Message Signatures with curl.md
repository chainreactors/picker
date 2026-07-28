---
title: HTTP Message Signatures with curl
url: https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/
source: daniel.haxx.se
date: 2026-07-27
fetch_date: 2026-07-28T04:58:52.823422
---

# HTTP Message Signatures with curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/07/message-in-a-bottle.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# HTTP Message Signatures with curl

[July 27, 2026](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/#comments)

The recently published [RFC 9421](https://datatracker.ietf.org/doc/html/rfc9421) describes how to do *HTTP Message Signatures*, and [starting just now](https://github.com/curl/curl/commit/a55731050e8c3dbea0b96205cf916443118f6acb), curl experimentally supports them.

## Message Signatures

The specification describes this as *a mechanism for creating, encoding, and verifying digital signatures or message authentication codes over components of an HTTP message.* It is a way to verify that selected parts of the HTTP request arrives unmodified and exactly the same as when the request was created by the client.

These days, it is very common that there are layers of proxies, load balancers, front-ends, CDNs, web firewalls and what not in between the client and the ultimate application. With HTTP Message Signatures, there can be assurances that the headers are components of the request end are unaltered.

## Command line

This functionality comes with four new command line options to allow users to use its full power:

`[--httpsig-algo](https://curl.se/docs/manpage.html#--httpsig-algo)` allows the user to specify which algorithm to use, with *ed25519* being used by default. The only other algorithm supported right now is *hmac-sha256*.

`[--httpsig-key](https://curl.se/docs/manpage.html#--httpsig-key)` specifies the key to use when signing the request.

`[--httpsig-keyid](https://curl.se/docs/manpage.html#--httpsig-keyid)` is the key identifier, a string that is passed on in the headers.

`[--httpsig-headers](https://curl.se/docs/manpage.html#--httpsig-headers)` details exactly which parts of the request and which headers that should be signed. If not set, it defaults to signing the method, authority, path and query.

With these four new flags added to the list, curl supports 278 different command line options.

## libcurl

The corresponding options of course also exist as options for [curl\_easy\_setopt](https://curl.se/libcurl/c/curl_easy_setopt.html):

* `[CURLOPT_HTTPSIG_ALGORITHM](https://curl.se/libcurl/c/CURLOPT_HTTPSIG_ALGORITHM.html)`: signing algorithm (“ed25519” or “hmac-sha256”)
* `[CURLOPT_HTTPSIG_KEY](https://curl.se/libcurl/c/CURLOPT_HTTPSIG_KEY.html)`: the key to use for the signing
* `[CURLOPT_HTTPSIG_KEYID](https://curl.se/libcurl/c/CURLOPT_HTTPSIG_KEYID.html)`: key identifier for Signature-Input
* `[CURLOPT_HTTPSIG_HEADERS](https://curl.se/libcurl/c/CURLOPT_HTTPSIG_HEADERS.html)`: a space-separated list of components to sign

## Experimental

This feature is marked *experimental*. This means that it need to be explicitly enabled in the build to appear, and that we strongly discourage use of it in production as we reserve the rights to change it before it gets supported for real. We use the experimental phases as a time for people to test it, to tweak it and to learn what we should fix so that we then can support this to the end of time. We do not guarantee any backward compatibility for experimental features.

Please test this feature and tell us how you experienced it! The more tests and more feedback we get, the faster we can get moved out of the experimental phase to have it present *for real* for everyone.

## Ships

This feature is already merged into git and will be part of the pending curl 8.22.0 release. As experimentally supported.

## Credits

This feature was graciously brought to us by Sameeh Jubran.

Top image by [Antonios Ntoumas](https://pixabay.com/users/atlantios-4957810/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3437294) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3437294)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP](https://daniel.haxx.se/blog/tag/http/)

# Post navigation

[Previous Post1,500 curl authors](https://daniel.haxx.se/blog/2026/07/25/1500-curl-authors/)

## 2 thoughts on “HTTP Message Signatures with curl”

1. ![](https://secure.gravatar.com/avatar/88a24dd149ea68676a65e79acfb941d8c438161f7dc12237fd4e052e55e92e6f?s=34&d=monsterid&r=g) **Nun Your Beeswax Inc.** says:

   [July 27, 2026 at 09:19](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/#comment-27544)

   I’m not sure whether PUTI realizes or not that AI generated posts, apart from being downright insulting, are easily recognizable.

   [Reply](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/?replytocom=27544#respond)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [July 27, 2026 at 09:23](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/#comment-27545)

      @Nun: yes thanks, I have since removed all of PUTI’s comments on this blog since they added nothing and seemed to be AI generated.

      [Reply](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/?replytocom=27545#respond)

### Leave a Reply [Cancel reply](/blog/2026/07/27/http-message-signatures-with-curl/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
five7eightsix9

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/)
  July 27, 2026
* [1,500 curl authors](https://daniel.haxx.se/blog/2026/07/25/1500-curl-authors/)
  July 25, 2026
* [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/)
  July 16, 2026
* [Workshop Basel day two](https://daniel.haxx.se/blog/2026/07/15/workshop-basel-day-two/)
  July 15, 2026
* [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/)
  July 14, 2026
* [Do excellent vulnerability reports](https://daniel.haxx.se/blog/2026/06/29/do-excellent-vulnerability-reports/)
  June 29, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27545)
* Nun Your Beeswax Inc. on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27544)
* Matthias Hörmann on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27539)
* entronid on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27538)
* Willy on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27537)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27536)
* Jeffrey Bosboom on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/w...