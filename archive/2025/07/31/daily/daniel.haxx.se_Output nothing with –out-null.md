---
title: Output nothing with –out-null
url: https://daniel.haxx.se/blog/2025/07/30/output-nothing-with-out-null/
source: daniel.haxx.se
date: 2025-07-31
fetch_date: 2025-10-06T23:39:33.522955
---

# Output nothing with –out-null

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

# Output nothing with –out-null

[July 30, 2025](https://daniel.haxx.se/blog/2025/07/30/output-nothing-with-out-null/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Downloading data from a remote URL is probably the single most common operation people do with curl.

Often, users then add various additional options to the command line to extract information from that transfer but may also decide that the actually fetched data *is not interesting*. Sometimes they don’t get the accurate meta-data if the full download is not made, sometimes they run performance measurements where the actual content is not important, and so on. Users sometimes have reasons for not saving their downloads.

They do downloads where the actual downloaded content is tossed away. On GitHub alone, we can find almost one million command lines doing such curl invokes.

curl of course offers multiple ways to discard the downloaded data, but the maybe most straight-forward way is to write the contents to a *null device* such as `/dev/null` on \*nix systems or `NUL:` on windows. Like this:

```
curl https://example.com/ --output /dev/null
```

or using the short option

```
curl https://example.com/ -o /dev/null
```

In many cases we can accomplish the same thing with a shell redirect – which also redirects multiple URLs at once:

```
curl https://example.com/ >/dev/null
```

## Improving nothing

The command line above is perfectly fine and works fine and has been doing so for decades. It does however have two drawbacks:

1. **Lack of portability.** curl runs on most operating systems and most options and operations work identically, to the degree that you can often copy command lines back and forth between machines without thinking much about it. Outputting data to /dev/null is however not terribly portable and trying that operation on Windows for example will cause the command line to fail.
2. **Performance**. It may not look like much, but completely avoiding writing the data instead of writing it to `/dev/null` makes benchmarks show a measurable improvement. So if you don’t want the data, why not do the operation faster rather than slower?

The shell redirect approach has the same drawbacks.

## Usage

The new option is used as follows, where it needs one `--out-null` occurrence per URL it wants to redirect.

```
curl https://example.com/ --out-null
```

This allows you to for example send one to null and save the other:

```
curl https://example.com/ --out-null https://example.net/ --output save-data
```

## Coming in 8.16.0

This command line option debuts in curl 8.16.0, shipping in September 2025.

## Credits

Stefan Eissing [brought this option](https://github.com/curl/curl/pull/17800). He also [benchmarked this option](https://github.com/icing/blog/blob/main/curl-platform-perf.md).

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostCarving out msh3](https://daniel.haxx.se/blog/2025/07/29/carving-out-msh3/)[Next Postoption parsing in curl](https://daniel.haxx.se/blog/2025/07/31/option-parsing-in-curl/)

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