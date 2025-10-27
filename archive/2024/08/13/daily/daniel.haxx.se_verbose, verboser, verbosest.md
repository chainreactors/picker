---
title: verbose, verboser, verbosest
url: https://daniel.haxx.se/blog/2024/08/12/verbose-verboser-verbosest/
source: daniel.haxx.se
date: 2024-08-13
fetch_date: 2025-10-06T18:06:23.507234
---

# verbose, verboser, verbosest

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/12/command-line-option-of-the-week.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# verbose, verboser, verbosest

[August 12, 2024](https://daniel.haxx.se/blog/2024/08/12/verbose-verboser-verbosest/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

A key feature for a tool like curl is its ability to help the user diagnose command lines and operations that do not work the way the user intended them to.

*When I do XYZ, why does it not work?*

The command line option `-v` and its longer version `--verbose` have been supported by curl since day one for this purpose. A boolean flag that when used shows what is going on by outputting extra information from the execution.

I need to emphasize the *boolean* part here. Up until curl 8.10.0, this option was a plain boolean. You either did not get verbose output or you got it. There was no levels or ways to increase or decrease the amount of information shown. Just a binary one or zero. On or off.

But starting in 8.10.0 the story is different.

## The world

Meanwhile, there is a universe of additional command line tools *out there*. Many other tools *also* offers a `-v` option for outputting verbose tracing information. In many other tools, the `-v` is not a boolean but instead you might get additional output if you add more vs. `-vv` shows a little more, `-vvv` even more etc.

Users are fairly trained on this. To the extent that we often get to see users use -vvv etc on curl command lines in bug reports etc. The curl command line parser accepts more of them fine (any amount really), but repeating them just enables the boolean again and again to no extra effect.

When we asked users for their favorite command line option in the annual [curl user survey in May 2024](https://daniel.haxx.se/blog/2024/06/17/curl-user-survey-2024-analysis/), a noticeable amount of respondents said `-vv` or `-vvv`. *Even though they do nothing extra than -v.* I think this shows to which extent people are trained to and are used to having these options for command line tools.

## Make curl do what you think it did

Therefore.

In curl 8.10.0, coming on September 11, 2024, we introduce support for `-vv`, `-vvv` and `-vvvv`. One, two, three or four vs. (Maybe we add more in the future.)

If you write the v-letters consecutive next to each other like that, you increase the logging level; the amount of verbose output curl shows. It might then possibly do something in the style that many users already expected it to do.

The extra logging it can do in 8.10.0 is actually nothing new, what is new is that you can get to it by simply using `-vv` and friends. The old style of getting such extra verbose tracing is to instead use a selected combination of [–trace-time](https://curl.se/docs/manpage.html#--trace-time), [–trace-ascii](https://curl.se/docs/manpage.html#--trace-ascii) and [–trace-config](https://curl.se/docs/manpage.html#--trace-config).

## Backwards compatibility

In curl we care deeply about backwards compatibility and not breaking users existing scripts and use cases when we ship new versions. This change is perhaps on the border of possibly doing this, so we have tried to tread as gently as we can to make sure that risk is slim.

This is why doing something like `curl -v -v` will not increase the level, because a user might have one of the switches in ~/.curlrc, another one on the command line and a third one in a custom file read with curl’s -K option etc. We want the extra output level to be explicitly asked for.

Using a single `-v` after a `-vv` or `-vvv` resets the level back to the original lowest-but-enabled for the same reason. The `--no-verbose` option also still works, even though the option is not strictly a boolean anymore and curl normally otherwise only supports the `--no-` prefix for boolean command line options.

## Credits

Stefan Eissing wrote [the pull-request](https://github.com/curl/curl/pull/13977) that landed this change.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postmore curl help](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/)[Next Postslow TCP connect on Windows](https://daniel.haxx.se/blog/2024/08/14/slow-tcp-connect-on-windows/)

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

August 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2024/08/06/) | 7 | [8](https://daniel.haxx.se/blog/2024/08/08/) | [9](https://daniel.haxx.se/blog/2024/08/09/) | 10 | 11 |
| [12](https://daniel.haxx.se/blog/2024/08/12/) | 13 | [14](https://daniel.haxx.se/blog/2024/08/14/) | 15 | 16 | [17](https://daniel.haxx.se/blog/2024/08/17/) | 18 |
| [19](https://daniel.haxx.se/blog/2024/08/19/) | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Jul](https://daniel.haxx.se/blog/2024/07/)

[Sep »](https://daniel.haxx.se/blog/2024/09/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)