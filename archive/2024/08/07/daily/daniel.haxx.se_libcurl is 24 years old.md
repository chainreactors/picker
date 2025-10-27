---
title: libcurl is 24 years old
url: https://daniel.haxx.se/blog/2024/08/06/libcurl-is-24-years-old/
source: daniel.haxx.se
date: 2024-08-07
fetch_date: 2025-10-06T18:03:42.284070
---

# libcurl is 24 years old

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/09/old-machine.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# libcurl is 24 years old

[August 6, 2024](https://daniel.haxx.se/blog/2024/08/06/libcurl-is-24-years-old/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

On Monday August 7, 2000 at 14:49 UTC, we announced the release of the first libcurl version ever. Exactly twenty-four years ago today. We called it version 7.1. The simple reason we did a point one release as the first one was that we had shipped a whole range of 7.0 beta versions before that day and I wanted to make it clear to everyone that this was a bump up from those. To avoid confusions.

The last release we did before libcurl was born was called 6.5.2, which we did 139 days before 7.1 was uploaded (in March 2000). The longest release interval in the entire history of curl. Never before or after, have we spent that long time to prepare a single new curl release.

> Howdy
>
> I just put the curl 7.1 tarball on the curl site. It’ll take a while more for it to appear on the mirrors and for our friends to send in binary archives or report where there are updated archives for various platforms.

The [original announcement](https://curl.se/mail/archive-2000-08/0024.html). Not many frills there.

## Contributors

Most of the work that went into the creation of libcurl was done by me alone. While we already had contributors and lots of people helping out with bug reports and features, this kind of heavy lifting and huge refactor was not really a team effort. I spent the summer splitting the monolithic command line tool into two components: a library and a command line tool that uses the library.

Since the last days of 1999 the curl source code was hosted on Sourceforge using CVS so at least all this was done in a public source code repository with version control.

## Why libcurl

I had already years before this time understood the powers of using shared libraries and how they are good ways to offer features and functionality to applications. I got an article published in a technical Amiga magazine in the early 1990s about how to do shared libraries on AmigaOS.

As the command line tool curl started to get somewhere and was already two years old at that point (the curl tool was born on March 20 1998), I imagined that there could be an application or two that could benefit from getting easy access to doing Internet transfers. It was just a gut feeling and a guess. I did not know. I did not research this or anything, I just took the plunge and figured we will eventually realize if I was right or wrong.

With me having written some portable libraries in the past already, curl was already written with the mindset that it could at time point get converted to a library + command line tool. This eased the conversion.

Already on day one libcurl built and ran on numerous operating systems offering the same API.

## Name

When I decided to make a library from the core of the curl tool I opened the discussion to see if someone had any ideas for what this library should be called. Naming is hard and I had no particularly bright ideas myself so we quite soon landed on the simplest take possible. Let’s just call it *libcurl*.

## API

How do you design an internet transfer library API?

I had this idea to offer multiple different API “sets” but I figured I needed to start with something basic. It ended up getting called the “easy” interface because it was intended to be straight-forward to use and I decided I could always add something more advanced later. I wanted to provide a fairly low level API and if someone wanted something more high-level, such an API can get built on top of this.

I knew that I wanted the API to be somewhat extensible without having to change the API all the time, and I found inspiration in how the ioctl() and fcntl() and similar functions work. I made [curl\_easy\_setopt](https://curl.se/libcurl/c/curl_easy_setopt.html)() follow that pattern. For good and bad.

I wanted the API to be decently protocol agnostic, since curl could already handle several different ones and I figured it could be appreciated by users who might not always be Internet protocol experts.

Mostly due to luck we managed to ship an API that even though it has its quirks has survived remarkably well.

## Using C

There was never any consideration to use another language than C for the library and there was really no decent options to select from either. In theory I suppose C++ could have been used, but I have never been a friend of C++ so I rather not. Not then, not now.

There was never even a discussion about what language to use.

## Resilience

The API that gradually was created in that summer of 2000 turned out to be fairly good and has survived and done surprisingly good.

There are 17 API functions still in use today that were introduced in 7.1. In fact, much code written for the API from back then can still be compiled and run using the latest libcurl!

At the time of the first libcurl release there was about 17,000 lines of product code. Today, twenty-four years later, we recently surpassed 171,000 lines.

The API has over the years even proved itself to endure “revolutionary” protocol changes such as HTTP/2 introducing multiplexing multiple transfers over the same connection and HTTP/3, which switches from TCP to UDP. This, mostly because it offers a high enough abstraction level.

## Users

The same month we shipped the first libcurl ever, the PHP project built the first libcurl binding. When PHP 4.0.2 was released on August 29 2000, curl was a bundled, blessed and official extension. PHP’s early and unconditional adoption of libcurl helped us get users, get testing, get bugreports and helped us mature.

Soon other users, projects, tools and devices adopted libcurl and built things using it. Gradually, it grew in popularity.

## multi interface

In the spring of 2002, we expanded the libcurl API with the “multi” API. Using this API family, libcurl offers an unlimited number of concurrent parallel Internet transfers in the same thread.

In 2006, we later expanded the multi interface to offer the multi\_action way, which expands the API to allow use of event-based mechanisms for the event loop, like epoll etc, thus allowing scaling up parallel transfers to the thousands or more without sacrificing performance.

## SONAME

Put simply, SONAME is the version number of the binary interface. We bumped it several times in the early years as we adjusted API details that we did not get right from the beginning.

Years later (in 2006), we did the last major SONAME bump and by then libcurl had enough usage to make a lot of people squeal and complain about the agony that bump caused. That event and its reactions was a strong contributing factor to me making the decision: To as far as we possibly can *never again break the ABI*. So far we have managed to stick to this promise and goal – barring bugs of course.

*Every libcurl program since 2006 can be compiled against the latest libcurl.* Of course, the underlying protocols (especially TLS) and URLs etc have changed and moved significantly since then which makes most URLs from that time to not work anymore.

## Higher level API

I think in many ways my original hopes of others doing higher level APIs to build on top of what libcurl provides has been realized primarily through the means of language bindings.

We have records of *at least* [65 different language bindings created for libcurl](https://everything.curl.dev/bindings/in...