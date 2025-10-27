---
title: twenty-five years of curl
url: https://daniel.haxx.se/blog/2023/03/20/twenty-five-years-of-curl/
source: daniel.haxx.se
date: 2023-03-20
fetch_date: 2025-10-04T10:05:25.169258
---

# twenty-five years of curl

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

# twenty-five years of curl

[March 20, 2023](https://daniel.haxx.se/blog/2023/03/20/twenty-five-years-of-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [11 Comments](https://daniel.haxx.se/blog/2023/03/20/twenty-five-years-of-curl/#comments)

Time flies when you are having fun. Today is [curl](https://curl.se/)‘s 25th birthday.

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/05/curl-symbol.png)

The curl project started out very humbly as a small renamed URL transfer tool that almost nobody knew about for the first few years. It scratched a personal itch of mine,

## Me back then

I made that first curl release and I’ve packaged every single release since. The day I did that first curl release I was 27 years old and I worked as a software engineer for **Frontec Tekniksystem**, where I mostly did contract development on embedded systems for larger Swedish product development companies. For a few years in the late 90s I would for example do quite a few projects at and for the telecom giant Ericsson.

I have enjoyed programming and development ever since I got my first computer in the mid 80s. In the 1990s I had already established a daily schedule where I stayed up late when my better half went to bed at night, and I spent another hour or two on my spare time development. This is basically how I have manged to find time to devote to my projects the first few decades. Less sleep. Less other things.

## Gradually and always improving

The concept behind curl development has always been to gradually and iteratively improve all aspects of it. Keep behavior, but enhance the code, add test cases, improve the documentation. Over and over, year after year. It never stops. As the timeline below helps showing.

Similarly, there was no sudden specific moment when suddenly curl became popular and the number of users skyrocketed. Instead, the number of users and the popularity of the tool and library has gradually and continuously grown. In 1998 there were few users. By 2010 there were hundreds of millions.

We really have no idea exactly how many users or installations of libcurl there are now. It is easy to estimate that it runs in **way more than ten billion installations** purely based on the fact that there are 7 billion smart phones and 1 billion tablets in the world , and we know that each of them run at least one, but likely many more curl installs.

## Before curl

My internet transfer journey started in late 1996 when I downloaded *httpget* 0.1 to automatically download currency rates daily to make my currency exchange converter work correctly for my IRC bot. httpget had some flaws so I sent back fixes, but Rafael, the author, quickly decided I could rather take over maintenance of the thing. So I did.

I added support for GOPHER, change named of the project, added FTP support and then in early 1998 I started adding FTP upload support as well…

## 1998

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/04/old-logo2.jpg)

The original curl logo.

On March 20 1998, curl 4.0 was released and it was already 2,200 lines of code on its birthday because it was built on the projects previously named httpget and urlget. It then supported three protocols: HTTP, GOPHER and FTP and featured 24 glorious command line options.

The first release of curl was not that special event since I had been shipping httpget and urlget releases for over a year already, so while this was a new name it was also “just another release” as I had done many times already.

We would add HTTPS and TELNET support already the first curl year, which also introduced the first ever curl man page. curl started out GPL licensed but I switched to MPL already within that first calendar year 1998.

The first SSL support was powered by SSLeay. The project that in late 1998 would transition over into becoming OpenSSL.

In August 1998, we added curl on the open source directory site freshmeat.net.

The first curl web page was published at `http://www.fts.frontec.se/~dast`. (the oldest version archived by the wayback machine is [from December 1998](https://web.archive.org/web/19981202234521/http%3A//www.fts.frontec.se%3A80/~dast/curl/))

In November 1998 I added a note to the website about the mind-blowing success as the latest release had been downloaded **300 times**! Success and popularity were far from instant.

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/03/massive-popularity.png)

Screenshot from the curl website of November 1998

During this first year, we shipped 20 curl releases. We have never repeated that feat again.

## 1999

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/03/Debian_logo.png)

We created the first configure script, added support for cookies and appeared as a package in Debian Linux.

The curl website moved to `http://curl.haxx.nu`.

We added support for DICT, LDAP and FILE through the year. Now supporting 8 protocols.

In the last days of 1999 we imported the curl code to the cool new service called Sourceforge. All further commit counts in curl starts with this import. December 29, 1999.

## 2000

Privately, I switched jobs early 2000 but continued doing embedded contract development during my days.

The rules for the TLD .se changed and we moved the curl website to `[curl.haxx.se](http://curl.haxx.se)`.

I got married.

In August 2000, we shipped curl 7.1 and things changed. This release introduced the library we decided to call libcurl because we couldn’t come up with a better name. At this point the project were at 17,200 lines of code.

The libcurl API was inspired by how `fopen()` works and returns just an opaque handle, and how `ioctl()`  can be used to set options.

Creating a library out of curl was an idea I had almost from the beginning, as I’ve already before that point realized the power a good library can bring to applications.

The [first CVE for curl](https://curl.se/docs/CVE-2000-0973.html) was reported.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/PHP-logo.png)](https://php.net/)

Users found the library useful and increased the curl uptake. One of the first early adopters of libcurl was the PHP language, which decided to use libcurl as their default HTTP/URL transfer engine.

We created the first test suite.

## 2001

We changed the license and offered curl under the new curl license (effectively MIT) as well as MPL. The idea to slightly modify the curl license was a crazy one, but the reason for that has been forgotten.

We added support for HTTP/1.1 and IPv6.

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/apple-2001.png)

In June, the THANKS file counted 67 named contributors. This is a team effort. We surpassed 1,100 total commits in March and in July curl was 20,000 lines of code.

Apple started bundling curl with Mac OS X when curl 7.7.2 shipped in Mac OS X 10.1.

## 2002

The test suite contained 79 test cases.

We dropped the MPL option. We would never again play the license change game.

We added support for [gzip compression](https://zlib.net/) over HTTP and learned how to use SOCKS proxies.

## 2003

The curl “autobuild” system was introduced: volunteers run scripts on their machines that download, build and run the curl tests frequently and email back the results to our central server for reporting and analyses. Long before modern CI systems made these things so much easier.

We added support for Digest, NTLM and Negotiate authentication ...