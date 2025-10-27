---
title: option parsing in curl
url: https://daniel.haxx.se/blog/2025/07/31/option-parsing-in-curl/
source: daniel.haxx.se
date: 2025-08-01
fetch_date: 2025-10-07T00:15:53.798847
---

# option parsing in curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2020/02/curl-cmdlines-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# option parsing in curl

[July 31, 2025](https://daniel.haxx.se/blog/2025/07/31/option-parsing-in-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

We have always had a custom command line option parser in curl. It is fast and uncomplicated and gives us the perfect mix of flexibility and function. It also saves us from importing or using code with another license.

In one aspect it has behaved slightly different than many other command line parsers: the way it accepts arguments to long options.

*Long options* are the options provided using a name that starts with two dashes and are often not single-letters. Example:

```
curl --user-agent "curl/2000" https://example.com/
```

The example above tells curl to use the user agent curl/2000 in the transfer. The argument provided to the `--user-agent` option is provided separated with a space.

When instead using the short version of the same option, the argument can be specified with a space in between *or not*:

```
curl -A curl/2000 https://example.com/
```

or

```
curl -Acurl/2000 https://example.com/
```

## What about equals sign?

A common paradigm and syntax style for accepting long options in command line tools is the “equals sign” approach. When you provide an argument to a long option you do this by appending an equals sign followed by the argument to the option; with no space. Like this:

```
curl --user-agent="curl/2000" https://example.com/
```

This example uses double quotes but they are of course not necessary if there is no space or similar in the argument.

## Bridging the gap

To make life easier for future users, curl now also support this latter style – starting in curl 8.16.0. With this syntax supported, curl accepts a more commonly used style and therefore should induce less surprises to users. To make it easier to write curl command lines.

I emphasize that change this is an improvement for *future users*, because I really don’t think it is a good idea for most user to switch to this syntax immediately. This of course because all the older curl versions that are still used widely around the word do not support it.

I think it is better if we **wait a year or two until we start using this option style in** curl documentation and example command lines. To give time for users to upgrade to a version that has support for it.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostOutput nothing with –out-null](https://daniel.haxx.se/blog/2025/07/30/output-nothing-with-out-null/)[Next Postcurl adds parallel host control](https://daniel.haxx.se/blog/2025/08/01/curl-adds-parallel-host-control/)

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

July 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | [3](https://daniel.haxx.se/blog/2025/07/03/) | 4 | 5 | 6 |
| 7 | [8](https://daniel.haxx.se/blog/2025/07/08/) | 9 | [10](https://daniel.haxx.se/blog/2025/07/10/) | [11](https://daniel.haxx.se/blog/2025/07/11/) | [12](https://daniel.haxx.se/blog/2025/07/12/) | [13](https://daniel.haxx.se/blog/2025/07/13/) |
| [14](https://daniel.haxx.se/blog/2025/07/14/) | 15 | [16](https://daniel.haxx.se/blog/2025/07/16/) | 17 | 18 | 19 | 20 |
| 21 | 22 | [23](https://daniel.haxx.se/blog/2025/07/23/) | 24 | 25 | 26 | 27 |
| [28](https://daniel.haxx.se/blog/2025/07/28/) | [29](https://daniel.haxx.se/blog/2025/07/29/) | [30](https://daniel.haxx.se/blog/2025/07/30/) | [31](https://daniel.haxx.se/blog/2025/07/31/) |  | | |

[« Jun](https://daniel.haxx.se/blog/2025/06/)

[Aug »](https://daniel.haxx.se/blog/2025/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)