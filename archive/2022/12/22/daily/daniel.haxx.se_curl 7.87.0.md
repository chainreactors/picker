---
title: curl 7.87.0
url: https://daniel.haxx.se/blog/2022/12/21/curl-7-87-0/
source: daniel.haxx.se
date: 2022-12-22
fetch_date: 2025-10-04T02:13:38.716392
---

# curl 7.87.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/curl-7.87.0.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 7.87.0

[December 21, 2022](https://daniel.haxx.se/blog/2022/12/21/curl-7-87-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

## Numbers

**the 212th release
5 changes
56 days (total: 9,042)**
**155 bug-fixes (total: 8,492)**
**238 commits (total: 29,571)
0 new public libcurl function (total: 91)
2 new curl\_easy\_setopt() option (total: 302)**
**1 new curl command line option (total: 249)**
**83 contributors, 40 new (total: 2,771)**
**42 authors, 20 new (total: 1,101)**
**2 security fixes (total: 132)**
**Bug Bounties total: 48,580 USD**

## Release presentation

At 10:00 CET (9:00 UTC) on December 21, Daniel live-streams the [release presentation on twitch](https://www.twitch.tv/curlhacker). This paragraph will later be replaced by a link to the YouTube version of that video.

## Security

Two security advisories this time around, severity low and medium.

### [CVE-2022-43551: Another HSTS bypass via IDN](https://curl.se/docs/CVE-2022-43551.html)

The HSTS logic could be bypassed if the host name in the given URL first uses IDN characters that get replaced to ASCII counterparts as part of the IDN conversion. Like using the character UTF-8 U+3002 (IDEOGRAPHIC FULL STOP) instead of the common ASCII full stop (U+002E). Then in a subsequent request, it does not detect the HSTS state and makes a clear text transfer. Because it would store the info IDN encoded but look for it IDN decoded.

### [CVE-2022-43552: HTTP Proxy deny use-after-free](https://curl.se/docs/CVE-2022-43552.html)

When an HTTP PROXY denied to tunnel SMB or TELNET, curl would use a heap-allocated struct after it had been freed in its transfer shutdown code path.

## Changes

### [–url-query](https://daniel.haxx.se/blog/2022/11/10/append-data-to-the-url-query/)

curl’s 249th command line option adds data to the query part of the URL.

### [CURLOPT\_QUICK\_EXIT](https://curl.se/libcurl/c/CURLOPT_QUICK_EXIT.html)

Tell libcurl to not wait for any DNS threads on exit.

### CURL\_WRITEFUNC\_ERROR

New and easier way to signal write callback errors.

### [CURLOPT\_CA\_CACHE\_TIMEOUT](https://curl.se/libcurl/c/CURLOPT_CA_CACHE_TIMEOUT.html)

libcurl can now cache the CA store in memory, as [I blogged about separately](https://daniel.haxx.se/blog/2022/11/11/curls-new-ca-store-cache/).

### feature names added to curl\_version\_info\_data

The struct returned by [curl\_version\_info](https://curl.se/libcurl/c/curl_version_info.html) now returns all built-in features listed by name. This is a preparation to allow applications to adapt slowly and get ready for the future moment when the features can no longer fit in in the 32 bit fields previously used for this purpose.

## Bugfixes

### Better base64

The encoder now allocates the output using a more appropriate size, and both [the encoder and decoder implementations are **much** faster](https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/).

### hyper

We fixed a few issues in the hyper backend and are down to just 12 remaining disabled tests to address.

### gen.pl: fix the linkifier

This script generates the `curl.1` man page and make sure to properly mark references correctly, so that the man page can get rendered as we webpage with correct links etc on the website. This time we made it work better and therefore more cross-references in the man page is now linked correctly in the web version.

### tool: override the numeric locale and set “C” by force

In previous curl versions it mistakenly used the locale when parsing floating point numbers, which then made the tool hard to use in scripts which would run in multiple locales. An example is the timeout option specified with `-m / --max-time` as number of seconds with a fraction. Now it requires the decimal separator to always be a dot/period independently of the user’s locale.

### tool: timeout in the read callback

The command line tool can now timeout reading data better, for example when using telnet:// with a timeout option and the user does not press any key and nothing happens over the network.

### curl\_get\_line: allow last line without newline char

Because of a somewhat lazy recent fix, the .netrc parsed and other users of the nternal `curl_get_line()` function would ignore the last line if it did not end with a newline. This is no more.

### support growing FTP files with CURLOPT\_IGNORE\_CONTENT\_LENGTH

If this option is set, also known as `--ignore-content-length` on the command line, curl will not complain if the size grows from the moment the FTP transfer starts until it ends. Thus allowing it to grow while being transferred.

### do not send PROXY more than once

The HAproxy protocol line could get sent more than once and thus break stuff.

### feature deprecation warnings in gcc

A number of outdated libcurl options and functions are now tagged as deprecated, which will cause compiler warnings when used in application code for users of gcc 6.1 or later. Deprecated here means that we recommend using other, more modern, alternatives.

### parse numbers with fixed known base 10

In several places in curl and libcurl source code we would allow numbers to be specified using octal or hexadecimal while decimal was the only expected and documented base. In order to minimize surprises and for consistency, we now limited them as far as possible to only accepting decimal numbers.

### rewind BEFORE request instead of AFTER previous

When curl is used to send a request, for example a POST, and there is reason for it to send it again, like if there is a redirect or an ongoing authentication process, it would previously rewind the stream at the end of that transfer first transfer in order to have it done when the next transfer is about to get done. Now, it instead does the rewind first in the second request. This, because there are times when the second request are not done, and the rewind may not work. So, such a failing rewind can be avoided by not doing it until it is strictly necessary.

### noproxy

Several independent regressions were fixed – in spite of the new set of test cases added for testing this feature in the previous release. Noproxy is the support for the `NO_PROXY` environment variable and related options.

### openssl: prefix errors with ‘[lib]/[version]:’

To help users understand errors and their origins a little better, libcurl will now prefix error messages originating from OpenSSL (and forks) with the name of the flavor and its version number.

### RTSP auth works again

This functionality was broken a few versions back and now it has finally been fixed again.

### runtests: –no-debuginfod now disables DEBUGINFOD\_URLS

valgrind and gdb support downloading stuff at the moment of need if this environment variable is set. Previously the curl test running script would unset that variable unconditionally, but now it will not and instead offer an option that unsets it – for the cases where the environment variable causes problems (such as performance slowdowns).

### HTTP/3 tests

We finally have the first infrastructure merged for doing and running HTTP/3 specific tests in the curl test suite. Now we can better avoid regressions going forward. This is only the beginning and I expect us to expand and grow these tests going forward.

### determine the correct fopen option for -D

When saving response headers into a dedicated file with curl’s `-D`, –dump-header option, curl would be inconsistent about when to cr...