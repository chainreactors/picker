---
title: curl 7.88.0 seven stops here
url: https://daniel.haxx.se/blog/2023/02/15/curl-7-88-0-seven-stops-here/
source: daniel.haxx.se
date: 2023-02-16
fetch_date: 2025-10-04T06:46:00.563253
---

# curl 7.88.0 seven stops here

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/curl-7.88.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 7.88.0 seven stops here

[February 15, 2023](https://daniel.haxx.se/blog/2023/02/15/curl-7-88-0-seven-stops-here/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Welcome to the final and last release in the series seven. The next release is planned and intended to become version 8.

## Numbers

**the 213th release
5 changes
56 days (total: 9,098)**
**173 bug-fixes (total: 8,665)**
**250 commits (total: 29,821)
0 new public libcurl function (total: 91)
0 new curl\_easy\_setopt() option (total: 302)**
**1 new curl command line option (total: 250)**
**78 contributors, 41 new (total: 2,812)**
**42 authors, 18 new (total: 1,119)**
**3 security fixes (total: 135)**

## Release presentation

## Security

This time we bring you three security fixes. All of them covering cases for which we have had problems reported and fixed before, but these are new subtle variations.

* [CVE-2023-23914](https://curl.se/docs/CVE-2023-23914.html): HSTS ignored on multiple requests

* [CVE-2023-23915](https://curl.se/docs/CVE-2023-23915.html): HSTS amnesia with –parallel

* [CVE-2023-23916](https://curl.se/docs/CVE-2023-23916.html): HTTP multi-header compression denial of service

## Changes

* Two changes for HTTP/3: `[CURL_HTTP_VERSION_3ONLY](https://curl.se/libcurl/c/CURLOPT_HTTP_VERSION.html)` was added for the library and `[--http3-only](https://curl.se/docs/manpage.html#--http3-only)` was added to the tool.
* Two changes for HSTS: [the HSTS cache can now be shared](https://curl.se/libcurl/c/CURLSHOPT_SHARE.html) between libcurl handles, and subsequently the curl tool now shares the HSTS between transfers.
* The URL API got the new flag `CURLU_PUNYCODE` which allows and application to [get the punycode version](https://curl.se/libcurl/c/curl_url_get.html) of a host name/URL.
* curl `-w` now offers %{certs} and %{num\_certs} which [outputs the server certificate](https://daniel.haxx.se/blog/2022/12/28/curl-w-certs/)(s).

## Bugfixes

While we count over 140 individual bugfixes merged for this release, here follows a curated subset of some of the more interesting ones.

### http/3 happy eyeballs

When asking for HTTP/3, curl will now also try older HTTP versions with a slight delay so that if HTTP/3 does not work, it might still succeed with and use an older version.

### update all copyright lines and remove year ranges

[Mentioned separately](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/).

### allow up to 10M buffer size

An application can now set drastically larger download buffers. For high speed/localhost transfers of some protocols this might sometimes make a difference.

### curl: output warning at –verbose output for debug-enabled version

To help users realize when they use a debug build of curl, it now outputs a warning at the top of the `--verbose` output. We strongly discourage users to ship or use such builds in production.

### websocket: multiple bugfixes

WebSocket support remains an experimental feature in curl but it is getting better. Several smaller and bigger bugs were squashed. Please continue to try it and report any problems and we can probably consider removing the experimental label soon.

### dict: URL decode the entire path always

If you used a DICT URL it would sometimes do wrong as it previously only URL decoded parts of the path when using it. Now it correctly decodes the entire thing.

### URL-encode/decode much faster

The libcurl functions for doing these conversions were sped up significantly. In the order of 3x and 7x.

### haxproxy: send before TLS handhshake

The haproxy details are now properly sent before the TLS handshake takes place.

### HTTP/[23]: continue upload when state.drain is set

Fixes a stalling problem when data is being uploaded and downloaded at the same time.

### http2: aggregate small SETTINGS/PRIO/WIN\_UPDATE frames

Optimizes outgoing frames for HTTP/2 into doing more in fewer sends.

### openssl: store the CA after first send (ClientHello)

By changing the order of things, curl is better off spending CPU cycles while waiting for the server’s response and thereby making the entire handshake process complete faster.

### curl: repair –rate

A regression in 7.87.0 made this feature completely broken. Now back on track again.

### HTTP/2 much faster multiplexed transfers

By improving the handling of multiple concurrent streams over a single connection, curl now performs such transfers *much* faster than before. Sometimes an almost 3x speedup.

### noproxy: support for space-separated names is deprecated

The parser that parses the “noproxy” string accepts plain space (without comma) as separators, while hardly any other tool or library does. This matters because it can be set in an environment variable. This accepted space-only separation is now marked as **deprecated**.

### nss: implement data\_pending method

The NSS backend was improved to work better for cases when the socket has been drained of data and only the NSS internal buffers has it, which could lead to curl getting stalled or losing data. Note: **NSS support is marked for removal** later in 2023.

### socketpair: allow localhost MITM sniffers

curl has an internal socketpair emulation function for Windows. The way it worked did not allow MITM sniffers, but instead return error if such a thing was detected. It turns out too many users run tools on Windows that do this, so we have changed the logic to accept their presence and use.

### tests-httpd: infra to run curl against an apache httpd

An entirely new line of tests that opens up new ways to test and verify our HTTP implementations in ways we could not do before. It uses pytest and an apache httpd server with special test modules.

### curl: fix hiding of command line secrets

A regression.

### curl: fix error code on bad URL

If you would use an invalid URL for upload, curl would erroneously report the problem as “out of memory” which unsurprisingly greatly confused users.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostClosing the NASA loop](https://daniel.haxx.se/blog/2023/02/07/closing-the-nasa-loop/)[Next Post7.88.1 the second final one](https://daniel.haxx.se/blog/2023/02/20/7-88-1-the-second-final-one/)

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#commen...