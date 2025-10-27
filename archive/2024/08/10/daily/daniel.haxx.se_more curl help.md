---
title: more curl help
url: https://daniel.haxx.se/blog/2024/08/09/more-curl-help/
source: daniel.haxx.se
date: 2024-08-10
fetch_date: 2025-10-06T18:04:53.621643
---

# more curl help

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/08/daniel-books-wide.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# more curl help

[August 9, 2024](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/#comments)

With the ever-growing number of command line options for curl, the problem of how to provide documentation and help users understand how options work and should be used is a challenge that is worth revisiting regularly. To keep iterating on.

I personally often use the curl manpage to lookup descriptions for options. Often not only to refresh my memory for my own use, but also when I want to quote a piece from it in a response to a user asking questions.

Right now curl supports 265 separate command line options in the latest development version. The text-only version of the manpage is almost 7,000 lines long. Searching the manpage for an option is sometimes also tedious since there are a lot of mentions of options in descriptions for other options. Like in *see also how option blabla can help you accomplish this*. So you might need to hit the key for *next-search* a significant number of times before you find the place you want if the term you search for is in the bottom half of the manpage.

`curl --manual` exists as well, and is convenient since everyone who has the tool automatically also has the documentation for it. But it carries the same challenge.

## Gimme docs for that option only

Starting in curl 8.10.0, planned to ship in September 11, 2024 we introduce this new nifty way to get documentation for only a specific single command line option:

```
curl --help [option]
```

or using the shorter version:

```
curl -h [option]
```

The [option] part above is a command line option. You can write it using the long format, the short format or even in its –no- format. In all ways an option is typed when accepted on a command line, you ask curl to help you with it.

## Screenshots

This seems like a feature worthy of a few screenshots to fully demonstrate it.

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/08/help-location.png)

curl -h –location

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/08/help-cookie-jar.png)

curl -h -c

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/08/help-globoff.png)

curl -h — no-globoff

I hope it will help everyone understand curl options a little better.

## Technical details you did not ask for

The full text version of the manpage is normally stored gzip-compressed in memory to make the binary several hundred kilobytes smaller. To display this output, curl needs to decompress the whole thing from the start and in a streaming manner figure out when to start showing the help and when to stop. This is still blazingly fast even on a not so modern computer.

For a long time we wrote the manpage for curl in directly using nroff format. Back then we generated the text-only version of that (for using with –manual) using nroff at build time. That text output was not stable and reliable enough for us to be able to do this feature. It was not until we switched over the documentation format to text, and later [curldown](https://daniel.haxx.se/blog/2024/01/23/curl-docs-format-evolution/), from which we generate the manpage, that we started to see this possibility. In March 2024, we landed the build updates that finally removed nroff from the build procedure and instead replaced it with a custom written tool. With full control of the input as well as the output, we can now add this feature reliably.

## Future

Like everything, this feature can certainly also be improved further. Possible improvements include:

* Use of a pager so that when the output is more than a screen-full, it pauses and you can move up and down using keys. Right now you need to pipe it manually into *less* or something.
* Dynamic reflowing of the text to better adjust itself to the existing terminal width. The current output is fixed-width designed for eighty column terminals.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[documentation](https://daniel.haxx.se/blog/tag/documentation/)[terminal](https://daniel.haxx.se/blog/tag/terminal/)

# Post navigation

[Previous Postcurl welcomes wcurl to the team](https://daniel.haxx.se/blog/2024/08/08/curl-welcomes-wcurl-to-the-team/)[Next Postverbose, verboser, verbosest](https://daniel.haxx.se/blog/2024/08/12/verbose-verboser-verbosest/)

## One thought on “more curl help”

1. ![](https://secure.gravatar.com/avatar/bdb225de278d5c922d8cbff645808d08ff363f84b3787c0dd6f69a997fc7b514?s=34&d=monsterid&r=g) **Hans F. Nordhaug** says:

   [August 11, 2024 at 10:06](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/#comment-27055)

   Such a great improvement – just love it!

Comments are closed.

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
| 5 | [6](https://daniel.haxx.se/blog/2024/08/06/) | 7 | [8](https://daniel.haxx.se/blog/2024/08/08/) | [9](https://daniel.haxx.se/blog/2024/...