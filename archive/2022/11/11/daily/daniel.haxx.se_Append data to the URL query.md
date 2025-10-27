---
title: Append data to the URL query
url: https://daniel.haxx.se/blog/2022/11/10/append-data-to-the-url-query/
source: daniel.haxx.se
date: 2022-11-11
fetch_date: 2025-10-03T22:23:34.089856
---

# Append data to the URL query

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

# Append data to the URL query

[November 10, 2022](https://daniel.haxx.se/blog/2022/11/10/append-data-to-the-url-query/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

A new curl option was born: `[--url-query](https://curl.se/docs/manpage.html#--url-query)`.

## How it started

curl offered the `-d` / `--data` option already in its first release back in 1998. curl 4.0. A trusted old friend.

curl also has some companion versions of this option that work slightly differently, but they all have the common feature that they append data to the the request body. Put simply: with these options users construct the body contents to POST. Very useful and powerful. Still today one of the most commonly used curl options, for apparent reasons.

```
curl -d name=mrsmith -d color=blue https://example.com
```

## Convert to query

A few years into curl’s lifetime, in 2001, we introduced the `-G` / `--get` option. This option let you use `-d` to create a data set, but the data is not sent as a POST body anymore but is instead converted to a query string and used in a GET request.

```
curl -G -d name=mrsmith -d color=blue https://example.com
```

This would make curl send a GET request to this URL: `https://example.com/?name=mrsmith&color=blue`

The “query” is the part of the URL that sits on the right side of the question mark (but before the fragment that if it exists starts with the first `#` following the question mark).

## URL-encode

In 2008 we added `--data-urlencode` which made it even easier for users and scripts to use these options correctly as now curl itself can URL-encode the given data instead of relying on the user to do it. Previously, script authors would have to do that encoding before passing the data to curl which was tedious and error prone. This feature also works in combination with `-G` of course.

## How about both?

The `-d` options family make a POST. The `-G` converts it to a GET.

If you want convenient curl command line options to **both** make content to send in the POST body **and**to create query parameters in the URL you were however out of luck. You would then have to go back to use `-d` but handcraft and encode the query parameters “manually”.

Until curl 7.87.0. Due to ship on December 21, 2022. ([this commit](https://github.com/curl/curl/commit/b6e1afd069f0a621b21bf27a461dc5297ce30031))

## `--url-query` is your new friend

This is curl’s 249th command line option and it lets you append parameters to the query part of the given URL, using the same syntax as `--data-urlencode` uses.

Using this, a user can now conveniently create a POST request body and at the same time add a set of query parameters for the URL which the request uses.

A basic example that sends the same POST body and URL query:

```
curl -d name=mrsmith -d color=blue --url-query name=mrsmith --url-query color=blue https://example.com
```

## Syntax

I told you it uses the data-urlencode syntax, but let me remind you how that works. You use `--url-query [data]` where `[data]` can be provided using these different ways:

|  |  |
| --- | --- |
| content | This will make curl URL-encode the content and pass that on. Just be careful so that the content does not contain any = or @ symbols, as that will then make the syntax match one of the other cases below! |
| =content | This will make curl URL-encode the content and pass that on. The preceding = symbol is not included in the data. |
| name=content | This will make curl URL-encode the content part and pass that on. Note that the name part is expected to be URL-encoded already. |
| @filename | This will make curl load data from the given file (including any newlines), URL-encode that data and pass it on in the POST. |
| name@filename | This will make curl load data from the given file (including any newlines), URL-encode that data and pass it on in the POST. The name part gets an equal sign appended, resulting in *name=urlencoded-file-content*. Note that the name is expected to be URL-encoded already. |
| +content | The data is provided as-is unencoded |

For each new `--url-query`, curl will insert an ampersand (&) between the parts it adds to the query.

## Replaces -G

This new friend we call `--url-query` makes `-G` rather pointless, as this is a more powerful option that does everything -G ever did and a lot more. We will of course still keep -G supported and working. Because that is how we work.

A boring fact of life is that new versions of curl trickle out into the world rather slowly to ordinary users. Because of this, we can be certain that scripts and users all over will need to keep using -G for yet another undefined period of time.

## Trace

Finally: remember that if you want curl to show you what it sends in a POST request, the normal `-v` / `--verbose` does not suffice as it will not show you the request body. You then rather need to use [`--trace` or `--trace-ascii`](https://everything.curl.dev/usingcurl/verbose/trace).

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[option of the week](https://daniel.haxx.se/blog/tag/option-of-the-week/)

# Post navigation

[Previous Postthehttpworkshop2022-day3.txt](https://daniel.haxx.se/blog/2022/11/03/thehttpworkshop2022-day3-txt/)[Next Postcurl’s new CA store cache](https://daniel.haxx.se/blog/2022/11/11/curls-new-ca-store-cache/)

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
* Tjark on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1...