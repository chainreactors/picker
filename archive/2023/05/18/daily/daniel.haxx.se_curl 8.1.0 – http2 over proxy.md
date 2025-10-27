---
title: curl 8.1.0 – http2 over proxy
url: https://daniel.haxx.se/blog/2023/05/17/curl-8-1-0-http2-over-proxy/
source: daniel.haxx.se
date: 2023-05-18
fetch_date: 2025-10-04T11:40:01.608443
---

# curl 8.1.0 – http2 over proxy

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/05/curl-8.1.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.1.0 – http2 over proxy

[May 17, 2023](https://daniel.haxx.se/blog/2023/05/17/curl-8-1-0-http2-over-proxy/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

We are back with the first release since that crazy March day when we did *two* releases on the same day. First [8.0.0](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-0-is-here/) shipped that bumped the major version for the first time in decades. Then [curl 8.0.1](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/) followed just hours after, due to a serious mess-up in the factory lines.

## Release video presentation

## Numbers

**the 217th release
3 changes
58 days (total: 9,189)**
**185 bug-fixes (total: 9,006)**
**322 commits (total: 30,367
0 new public libcurl function (total: 91)
0 new curl\_easy\_setopt() option (total: 302)**
**1 new curl command line option (total: 251)**
**64 contributors, 35 new (total: 2,875)**
**37 authors, 17 new (total: 1,142)**
**4 security fixes (total: 145)**

## Security

We disclose four new curl security vulnerabilities today, three of them at severity **Low** and one of them at **Medium**. This also means that 3,840 USD was awarded as bug bounties in this release cycle.

### UAF in SSH sha256 fingerprint check

[[CVE-2023-28319](https://curl.se/docs/CVE-2023-28319.html)] libcurl offers a feature to verify an SSH server’s public key using a SHA 256 hash. When this check fails, libcurl would free the memory for the fingerprint before it returns an error message containing the (now freed) hash.

### siglongjmp race condition

[[CVE-2023-28320](https://curl.se/docs/CVE-2023-28320.html)] libcurl provides several different backends for resolving host names, selected at build time. If it is built to use the synchronous resolver, it allows name resolves to time-out slow operations using `alarm()` and `siglongjmp()`.

When doing this, libcurl used a global buffer that was not mutex protected and a multi-threaded application might therefore crash or otherwise misbehave.

### IDN wildcard match

[[CVE-2023-28321](https://curl.se/docs/CVE-2023-28321.html)] curl supports matching of wildcard patterns when listed as “Subject Alternative Name” in TLS server certificates. curl can be built to use its own name matching function for TLS rather than one provided by a TLS library. This private wildcard matching function would match IDN (International Domain Name) hosts incorrectly and could as a result accept patterns that otherwise should mismatch.

### more POST-after-PUT confusion

[[CVE-2023-28322](https://curl.se/docs/CVE-2023-28322.html)] When doing HTTP(S) transfers, libcurl might erroneously use the read callback ([CURLOPT\_READFUNCTION](https://curl.se/libcurl/c/CURLOPT_READFUNCTION.html)) to ask for data to send, even when the [CURLOPT\_POSTFIELDS](https://curl.se/libcurl/c/CURLOPT_POSTFIELDS.html) option has been set, if the same handle previously was used to issue a PUT request which used that callback.

This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the second transfer.

## Changes

This release has only three real changes. One bigger and two smaller:

### HTTP/2 over proxy

libcurl can now negotiate and use HTTP/2 when it is told to use a HTTPS proxy (details in the [CURLOPT\_PROXYTYPE man page](https://curl.se/libcurl/c/CURLOPT_PROXYTYPE.html)), and the command line tool can of course switch it on using the `[--proxy-http2](https://curl.se/docs/manpage.html#--proxy-http2)` option. Explained more in [this blog post](https://daniel.haxx.se/blog/2023/04/14/curl-speaks-http-2-with-proxy/).

### refuse to resolve the .onion TLD

When a host name ending with `.onion` is passed on to the name resolver functions, they will cause an error and will not be resolved. Like [RFC 7686](https://www.rfc-editor.org/rfc/rfc7686.html) tells us.

### curl’s -w option can now output URL components

The list of variables was extended by a whole range of new ones. Possibly best learned by checking out [the writeout section in everything curl](https://everything.curl.dev/usingcurl/verbose/writeout).

## Bugfixes

The official counter says we did more than 180 bugfixes in his release cycle. Here follows some of my favorites:

### checksrc fixes

We made it better at checking the code style for three distinct code situations – and then updated the source code accordingly.

### cmake fixes

* bring in the network library on Haiku
* do not add zlib headers for OpenSSL
* make config version 8 compatible with 7
* set SONAME for SunOS too

### only do transfer-encoding compression if asked to

Transfer encodings other than “chunked” are rarely used. Up until now libcurl would still activate automatic decompression if such was used, even if it was not asked for by the application.

### bring back support for SFTP path ending in /~

A regression made a URL that ends with `/~` no longer make a directory listing because the URL does not end with a slash. Now we bring back that behavior, even if it goes a little against the standard behavior.

### never allocate dynbufs larger than “too big”

The general dynamic buffer system no longer allocates more memory than what the specific buffer is allowed to grow to. An optimization.

### various gskit compile errors in OS400

Makes curl build fine there again.

### enforce a maximum DNS cache size independent of timeout value

The DNS cache entries are purged on age only (default 60 seconds). With this new code, libcurl limits caps the maximum total amount of DNS cache entries to 30,000.

### libssh2: fix crash in keyboard callback

Better SCP and SFTP when built with libssh2.

### libssh: tell it to use SFTP non-blocking

Better SCP and SFTP when built with libssh.

### add multi-ignore logic to multi\_socket\_action

The improved signal ignore logic for [curl\_multi\_perform](https://curl.se/libcurl/c/curl_multi_perform.html) in 8.0.0 is now also done for [curl\_multi\_socket\_action](https://curl.se/libcurl/c/curl_multi_socket_action.html). For better performance.

### remove PENDING + MSGSENT handles from the main linked list

Not yet activated transfers and the transfers that are already completed, are now moved away off the main linked list. For performance.

### runtests: prepare for parallel

Lots of cleanups and smaller fixes have been merged during this cycle in preparation for the pending introduction of parallel tests.

### verify socketpair with a random value

The custom socketpair implementation used for platforms without a native one, was changed to use truly random values when verifying that the pipe works.

### Fix ‘Location:’ formatting for early VTE terminals

The special terminal highlighting of the URL that is shown in the `Location:` header is now disabled for some terminals that can’t display it properly.

### urlapi polish

Several different bugs and improvements were made. Including:

* cleanups and performance improvements
* detect and error on illegal IPv4 addresses
* prevent setting invalid schemes
* URL encoding for the URL missed the fragment

### enhanced WebSocket en-/decoding

Parts of the websocket parser code was rewritten to fix bugs.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Post30,000 GitHub stars](https://daniel.haxx.se/blog/2023/05/11/30000-github-st...