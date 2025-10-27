---
title: The curl fragment trick
url: https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/
source: daniel.haxx.se
date: 2022-12-24
fetch_date: 2025-10-04T02:25:58.112125
---

# The curl fragment trick

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

# The curl fragment trick

[December 23, 2022](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/#comments)

curl supports *globbing* in the sense that you can provide ranges or lists in the URL that will make curl iterate, loop, over all the different variations and do a separate transfer for each.

For example, get ten images in a numeric range:

```
curl "https://example.com/image[1-10].jpg" -O
```

Or get them when named after some weekdays:

```
curl "https://example.com/{Monday,Tuesday,Friday}.jpg" -O
```

## Naming the output

The examples above use `-O` which makes curl use the same name for the destination file as is used the effective URL. Convenient, but not always what you want.

curl also allows you to refer to the number or name from the range or list and use that when naming your output files, which helps you do better globbing.

For example, maybe the file name part of the URL is actually the same and you iterate over another difference in the URL. Like this:

```
curl "https://example.com/{Monday,Tuesday,Friday}/image" -o #1.jpg
```

The `#1` part in the example is a reference back to the first list/range, as you can do multiple ones and even using mixed types and you can then use multiple #-references in the same command line. To illustrate, here is a simple example using two iterators to download three hundred images:

```
curl "https://{red,blue,green}.example.com/image[1-100].jpg" -o "#2-#1-stored.jpg"
```

There is actually no upper limit to how many transfers you can do like this with curl, other than that the numeric ranges only deal with up to 64 bit numbers.

## Hundreds? Maybe go parallel

If you actually do come up with a command line that needs to transfer several hundred or more resources, then maybe consider adding `-Z, --parallel` to the mix so that curl performs many transfers simultaneously, in parallel. This can drastically reduce the total time needed for completing the task.

curl runs up to 50 transfers in parallel by default when this option is used, but you can also tweak this amount with `--parallel-max`.

## A fragment trick

Okay, so now we finally arrive at the fragment and *the trick* mentioned in the title.

If you want to do several repeated transfers but not actually change the URL then the examples above do not satisfy you as they change the URL for every new transfer.

A neat trick is then to add a fragment part to the URL you use, and then do the globbing there. The fragment is the rightmost part of a URL that starts with a `#`-character and continues to the end of the URL.

A fragment can always be added to a URL, but the fragment is never actually transmitted over the network so the remote server is not aware of it.

Get *the same* URL ten times, saved in different target files:

```
curl "https://example.com/index.html#[1-10]" -o #1.html
```

If you rather name the outputs according some scheme, you can of course just list them in the glob:

```
curl "https://example.com/index.html#{mercury,venus,earth,mars}" -o #1.html
```

## Maybe slower

In cases where you transfer the same URL many times, chances are you want to do this because the content changes at some interval. Perhaps you then do not want them all to be done as fast as possible as then the contents may not have updated.

To help you pace the transfers to get the same thing over and over in a more controlled manner, curl offers `[--rate](https://daniel.haxx.se/blog/2022/05/23/curl-offers-repeated-transfers-at-slower-pace/)`. With this you can tell curl to not do it faster than N transfers per given period.

If the URL contents update every 5 minutes, then doing the transfer 12 times per hour seems suitable. Let’s do it 2016 times to have the operation run non-stop for a week:

```
curl "https://example.com/index.html#[1-2016]" --rate 12/h -o "#1.html"
```

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostThe 2022 curl security audit](https://daniel.haxx.se/blog/2022/12/21/the-2022-curl-security-audit/)[Next PostAt 17000 curl commits](https://daniel.haxx.se/blog/2022/12/27/at-17000-curl-commits/)

## 4 thoughts on “The curl fragment trick”

1. ![](https://secure.gravatar.com/avatar/83fb201d5ca2081f058b24a53b94d5348367e9172d67441cbf0c136785ce8ebd?s=34&d=monsterid&r=g) **Nic** says:

   [December 23, 2022 at 17:22](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/#comment-26535)

   Does the last example need `-o #1.html` or am I missing some magic?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [December 23, 2022 at 17:24](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/#comment-26536)

      @Nic: probably, if you actually want each different download in separate files.

      Thanks, added that now for clarity.
2. ![](https://secure.gravatar.com/avatar/cadfd0e942e66c0195089108c0a7e332dd904a12d622f6e50ce029710fd358c9?s=34&d=monsterid&r=g) **[Alex](https://ladydebug.com)** says:

   [December 23, 2022 at 22:52](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/#comment-26537)

   Very useful information. One question. I frequently using -I option to get HTTP response headers, how I can see request headers as well.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [December 23, 2022 at 23:25](https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/#comment-26538)

      @Alex: you can just add `-v` to get to see the request as well. Or maybe more fancy with `--trace` or `--trace-ascii`…

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
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](...