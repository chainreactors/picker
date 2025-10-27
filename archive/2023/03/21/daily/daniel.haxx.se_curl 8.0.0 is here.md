---
title: curl 8.0.0 is here
url: https://daniel.haxx.se/blog/2023/03/20/curl-8-0-0-is-here/
source: daniel.haxx.se
date: 2023-03-21
fetch_date: 2025-10-04T10:08:54.978368
---

# curl 8.0.0 is here

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/curl-8.0.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.0.0 is here

[March 20, 2023](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-0-is-here/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Exactly one month since [the previous release](https://daniel.haxx.se/blog/2023/02/20/7-88-1-the-second-final-one/), we are happy to give you **curl 8.0.0** released on curl’s [official 25th birthday](https://daniel.haxx.se/blog/2023/03/20/twenty-five-years-of-curl/).

This a major version number bump but without any ground-breaking changes or fireworks. We decided it was about time to reset the minor number down to more a manageable level and doing it exactly on curl’s 25th birthday made it extra fun. **There is no API nor ABI break in this version.**

This is likely the best curl release we ever made.

## Release video presentation

## curl 25 years celebrations

Note the [additional event happening](https://daniel.haxx.se/blog/2023/03/10/curl-25-years-online-celebration/) later on March 20. and [the Fossified podcast episode on curl 25 years](https://pod.fossified.com/2023/03/19/s01e02.html).

## Numbers

**the 215th release
1 changes
28 days (total: 9,131)**
**130 bug-fixes (total: 8,820)**
**189 commits (total: 30,042)
0 new public libcurl function (total: 91)
0 new curl\_easy\_setopt() option (total: 302)**
**0 new curl command line option (total: 250)**
**42 contributors, 23 new (total: 2,841)**
**21 authors, 5 new (total: 1,125)**
**6 security fixes (total: 141)**

## Security

We disclose six new vulnerabilities today, five of them at severity **Low** and one of them at **Medium**.

### [CVE-2023-27533](https://curl.se/docs/CVE-2023-27533.html): TELNET option IAC injection

curl supports communicating using the TELNET protocol and as a part of this it offers users to pass on user name and “telnet options” for the server negotiation.

Due to lack of proper input scrubbing and without it being the documented functionality, curl would pass on user name and telnet options to the server as provided. This could allow users to pass in carefully crafted content that pass on content or do option negotiation without the application intending to do so. In particular if an application for example allows users to provide the data or parts of the data.

### [CVE-2023-27534](https://curl.se/docs/CVE-2023-27534.html): SFTP path ~ resolving discrepancy

curl supports SFTP transfers. curl’s SFTP implementation offers a special feature in the path component of URLs: a tilde (`~`) character as the first path element in the path to denotes a path relative to the user’s home directory. This is supported because of wording in the [once proposed to-become RFC draft](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-scp-sftp-ssh-uri-04) that was to dictate how SFTP URLs work.

Due to a bug, the handling of the tilde in SFTP path did however not only replace it when it is used stand-alone as the first path element but also wrongly when used as a mere prefix in the first element.

Using a path like /~2/foo when accessing a server using the user dan (with home directory /home/dan) would then quite surprisingly access the file `/home/dan2/foo`.

This can be taken advantage of to circumvent filtering or worse.

### [CVE-2023-27535](https://curl.se/docs/CVE-2023-27535.html): FTP too eager connection reuse

libcurl would reuse a previously created FTP connection even when one or more options had been changed that could have made the effective user a very different one, thus leading to the doing the second transfer with wrong credentials.

libcurl keeps previously used connections in a connection pool for subsequent transfers to reuse if one of them matches the setup. However, several FTP settings were left out from the configuration match checks, making them match too easily. The settings in questions are `[CURLOPT_FTP_ACCOUNT](https://curl.se/libcurl/c/CURLOPT_FTP_ACCOUNT.html)`, `[CURLOPT_FTP_ALTERNATIVE_TO_USER](https://curl.se/libcurl/c/CURLOPT_FTP_ALTERNATIVE_TO_USER.html)`, `[CURLOPT_FTP_SSL_CCC](https://curl.se/libcurl/c/CURLOPT_FTP_SSL_CCC.html)` and `[CURLOPT_USE_SSL](https://curl.se/libcurl/c/CURLOPT_USE_SSL.html)` level.

### [CVE-2023-27536](https://curl.se/docs/CVE-2023-27536.html): GSS delegation too eager connection re-use

libcurl would reuse a previously created connection even when the GSS delegation (`[CURLOPT_GSSAPI_DELEGATION](https://curl.se/libcurl/c/CURLOPT_GSSAPI_DELEGATION.html)`) option had been changed that could have changed the user’s permissions in a second transfer.

libcurl keeps previously used connections in a connection pool for subsequent transfers to reuse if one of them matches the setup. However, this GSS delegation setting was left out from the configuration match checks, making them match too easily, affecting krb5/kerberos/negotiate/GSSAPI transfers.

### [CVE-2023-27537](https://curl.se/docs/CVE-2023-27537.html): HSTS double-free

libcurl supports sharing HSTS data between separate “handles”. This sharing was introduced without considerations for do this sharing across separate threads but there was no indication of this fact in the documentation.

Due to missing mutexes or thread locks, two threads sharing the same HSTS data could end up doing a double-free or use-after-free.

### [CVE-2023-27538](https://curl.se/docs/CVE-2023-27538.html): SSH connection too eager reuse still

libcurl would reuse a previously created connection even when an SSH related option had been changed that should have prohibited reuse.

libcurl keeps previously used connections in a connection pool for subsequent transfers to reuse if one of them matches the setup. However, two SSH settings were left out from the configuration match checks, making them match too easily.

## Changes

There is only one actual “change” in this release. This is the first curl release to drop support for building on a systems that lack a working 64 bit data type. curl now requires that ‘`long long`‘ or an equivalent exists.

## Bugfixes

This release cycle was half the length of a regular one but yet we managed to merge an impressive amount of bugfixes. Below I highlight a few that I think deserve a special mention.

### build: drop the use of XC\_AMEND\_DISTCLEAN

A strange description but this change removed an old autotools macro that made configure sometimes “balloon” Makefiles to several gigabytes.

### connect: fix time\_connect and time\_appconnect timer statistics

A regression after the new happy eyeball h2/h3 connect approach was introduced.

### curl.1: list all “global options”

Command line options that survive the use of `--next` are called “global options” and the man page now lists all of them for easier identification.

To accomplish this, there is a new metadata “tag” for this purpose to mark the global options in their corresponding docs files.

### ftp: active mode with SSL, add the filter

Regression: FTPS in active mode did not setup the data connection correctly.

### replaced sscanf() in several parsers

From 24 occurrences of `sscanf()` calls in the code in the previous release, down to just 4 left.

### headers: make curl\_easy\_header and nextheader return different buffers

### http2 bugfixes

* error handling during parallel operations
* fix http2 prior knowledge when reusing connections
* RST and GOAWAY better recognize partial transfers
* avoid upload busy loop

### http: don’t send 100-continue for short PUT requests

Now aligns with and behaves more similar...