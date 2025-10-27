---
title: curl 8.2.0
url: https://daniel.haxx.se/blog/2023/07/19/curl-8-2-0/
source: daniel.haxx.se
date: 2023-07-20
fetch_date: 2025-10-04T11:55:48.230192
---

# curl 8.2.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/07/curl-8.2.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.2.0

[July 19, 2023](https://daniel.haxx.se/blog/2023/07/19/curl-8-2-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Welcome to another curl release. You know how this dance goes…

## Numbers

**the 220th release
5 changes
50 days (total: 9,252)**
**122 bug-fixes (total: 9,167)**
**177 commits (total: 30,606)
0 new public libcurl function (total: 91)
1 new curl\_easy\_setopt() option (total: 303)**
**4 new curl command line option (total: 255)**
**55 contributors, 34 new (total: 2,922)**
**35 authors, 20 new (total: 1,170)**
**1 security fixes (total: 146)**

## Release presentation

## Security

### fopen race condition (medium)

[CVE-2023-32001](https://curl.se/docs/CVE-2023-32001.html). libcurl can be told to save cookies, HSTS and/or alt-svc data to files. When doing this, it called `stat()` followed by `fopen()` in a way that made it vulnerable to a TOCTOU (Time of Check, Time of Use) race condition problem.

By exploiting this flaw, an attacker could trick the victim to create or overwrite protected files holding this data in ways it was not intended to.

## Changes

### curl: add –ca-native and –proxy-ca-native

The command line tool (and library) got new options to ask it to use the systems “native” CA storage. Currently only work on Windows when curl is built to use an OpenSSL fork.

### curl: add –trace-ids

This option makes the trace log files include connection and transfer identifiers, which greatly helps debugging transfers doing many (parallel) transfers.

### CURLOPT\_MAIL\_RCPT\_ALLOWFAILS replaces CURLOPT\_MAIL\_RCPT\_ALLLOWFAILS

Provide the option without the typo!

### add –haproxy-clientip flag to set client IPs

Now users of the tool (and library) pass on specific IP addresses instead of simply using the current one.

### add CURLINFO\_CONN\_ID and CURLINFO\_XFER\_ID

Two options that allows the application to extract the connection and transfer “Id” of the current transfer, presumably from a [debugfunction callback](https://curl.se/libcurl/c/CURLOPT_DEBUGFUNCTION.html) and the likes.

## Bugfixes

We have again fixed more than a hundred problems in this release cycle. Here follows a subset that I suspect might be among the most interesting ones.

### examples: we’ve added and extended numerous

The ambition is to gradually over time provide examples that show use of all [curl\_easy\_setopt](https://curl.se/libcurl/c/easy_setopt_options.html) options. We are still way off from that.

### http2: numerous smaller and larger fixes

Several regressions and cleanups have been done that improves how HTTP/2 works compared to previous releases.

### http2: send HEADER and DATA together

When sending POST requests, libcurl now does a better job in putting the initial outgoing HEADER and DATA frames together, most likely in the same TLS frame.

### http3: upload EAGAIN handling

EAGAIN handling for HTTP/3 uploads was fixed, like it was for HTTP/2 as well.

### http: fix the outgoing Cookie: header length check

The check that would prevent too long outgoing cookie headers was off by up to a few hundred bytes.

### libssh2: use custom memory functions (again)

Bring back use of custom memory functions with libssh2 as otherwise it actually cannot be used with a debug build of curl (or when libssh2 is used as a DLL on windows) due to naive presumptions in the libssh2 API.

### runtests: many improvements, leading to -j

Introducing [parallel tests](https://daniel.haxx.se/blog/2023/06/08/parallel-curl-tests/).

### sectransp: fix EOF handling

A regression caused curl misbehave on end of connection using TLS when built to use Secure Transport.

### timeval: use CLOCK\_MONOTONIC\_RAW if available

For platforms with this clock option, curl now prefers that in an effort to avoid a time that can go backwards.

### tool\_writeout\_json: fix encoding of control characters

The output of control codes in the generated JSON with `--json` now works better.

### urlapi: have \*set(PATH) prepend a slash if one is missing

Setting a path using the URL API without a leading slash would previously generate a broken URL when it was extracted. Starting now, libcurl will prepend a slash if there is none.

### urlapi: scheme must start with alpha

The URL parser would previously allow a few other characters to start a scheme as well. No more.

### tool\_parsecfg: accept line lengths up to 10M

The [config file](https://everything.curl.dev/cmdline/configfile) parser now allows lines to be up to 10 megabytes. For those odd users generating files with huge data components embedded.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postcurl user survey 2023 analysis](https://daniel.haxx.se/blog/2023/06/17/curl-user-survey-2023-analysis/)[Next Postcurl 8.2.1](https://daniel.haxx.se/blog/2023/07/26/curl-8-2-1/)

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
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27317)
* Yoann Ricordel on [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/comment-page-1/#comment-27316)
* Ond?ej Surý on [Hello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/comment-page-1/#comment-27315)
* H. Stefan on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27314)
* Tjark on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27313)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

July 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| ...