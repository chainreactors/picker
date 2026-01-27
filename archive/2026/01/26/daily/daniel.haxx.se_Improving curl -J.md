---
title: Improving curl -J
url: https://daniel.haxx.se/blog/2026/01/27/improving-curl-j/
source: daniel.haxx.se
date: 2026-01-26
fetch_date: 2026-01-27T03:37:29.992126
---

# Improving curl -J

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

# Improving curl -J

[January 27, 2026](https://daniel.haxx.se/blog/2026/01/27/improving-curl-j/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/01/27/improving-curl-j/#respond)

We introduced [curl’s `-J` option](https://curl.se/docs/manpage.html#-J), also known as `--remote-header-name` back in February 2010. A decent amount of years ago.

The option is used in combination with `-O` (`--remote-name`) when downloading data from a HTTP(S) server and instructs curl to use the filename in the incoming `Content-Disposition:` header when saving the content, instead of the filename of the URL passed on the command line (if provided). That header would later be explained further in [RFC 6266](https://datatracker.ietf.org/doc/html/rfc6266).

The idea is that for some URLs the server can provide a more suitable target filename than what the URL contains from the beginning. Like when you do a command similar to:

```
curl -O -J https://example.com/download?id=6347d
```

*Without* -J, the content would be save in the target output filename called ‘download’ – since curl strips off the query part.

*With* -J, curl parses the server’s response header that contains a better filename; in the example below *fun.jpg*.

```
Content-Disposition: filename="fun.jpg";
```

## But redirects?

The above approach mentioned works pretty well, but has several limitations. One of them being that the obvious that if the site instead of providing a Content-Disposition header perhaps only redirects the client to a new URL to the download from, curl does not pick up the new name but instead keeps using the one from the originally provided URL.

This is not what most users want and not what they expect. As a consequence, we have had this potential improvement mentioned in the TODO file for many years. Until [today](https://github.com/curl/curl/pull/20430).

We have now merged a change that makes curl with -J pick up the filename from Location: headers and it uses that filename if no Content-Disposition.

This means that if you now rerun a similar command line as mentioned above, but this one is allowed to follow redirects:

```
curl -L -O -J https://example.com/download?id=6347d
```

And that site redirects curl to the actual download URL for the tarball you want to download:

```
HTTP/1 301 redirect

Location: https://example.org/release.tar.gz
```

… curl now saves the contents of that transfer in a local file called `release.tar.gz`.

If there is *both* a redirect and a Content-Disposition header, the latter takes precedence.

## The filename is set remotely

Since this gets the filename from the server’s response, you give up control of the name to someone else. This can of course potentially mess things up for you. curl ignores all provided directory names and only uses the filename part.

If you want to save the download in a dedicated directory other than the current one, use [–output-dir](https://curl.se/docs/manpage.html#--output-dir).

As an additional precaution, using -J implies that curl avoids to clobber, overwrite, any existing files already present using the same filename unless you also use [–clobber](https://curl.se/docs/manpage.html#--no-clobber).

## What name did it use?

Since the selected final name used for storing the data is selected based on contents of a header passed from the server, using this option in a scripting scenario introduces the challenge: what filename did curl actually use?

A user can easily extract this information with curl’s [-w option](https://everything.curl.dev/usingcurl/verbose/writeout.html). Like this:

```
curl -w '%{filename_effective}' -O -J -L https://example.com/download?id=6347d
```

This command line outputs the used filename to stdout.

Tweak the command line further to instead direct that name to stderr or to a specific file etc. Whatever you think works.

## Remaining restrictions

The content-disposition RFC mentioned above details a way to provide a filename encoded as UTF-8 using something like the below, which includes a U+20AC Euro sign:

```
Content-Disposition: filename*= UTF-8''%e2%82%ac%20rates
```

curl still does not support this *filename\** style of providing names. This limitation remains because curl cannot currently convert that provided name into a local filename using the provided characters – with certainty.

Room for future improvement!

## Ships

This -J improvement ships in curl 8.19.0, coming in March 2026.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP](https://daniel.haxx.se/blog/tag/http/)

# Post navigation

[Previous PostThe end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)

### Leave a Reply [Cancel reply](/blog/2026/01/27/improving-curl-j/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
fourfive3threesix

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Improving curl -J](https://daniel.haxx.se/blog/2026/01/27/improving-curl-j/)
  January 27, 2026
* [The end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)
  January 26, 2026
* [libcurl memory use some years later](https://daniel.haxx.se/blog/2026/01/21/libcurl-memory-use-some-years-later/)
  January 21, 2026
* [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/)
  January 19, 2026
* [My first 20,000 curl commits](https://daniel.haxx.se/blog/2026/01/17/my-first-20000-curl-commits/)
  January 17, 2026
* [More HTTP/3 focus, one backend less](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/)
  January 17, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [The end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/comment-page-1/#comment-27394)
* [Piotr P. Karwasz](https://logging.apache.org/) on [The end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/comment-page-1/#comment-27393)
* [Verisimilitude](http://verisimilitudes.net) on [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/comment-page-1/#comment-27392)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/comment-page-1/#comment-27391)
* [Verisimilitude](http://verisimilitudes.net) on [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/comment-page-1/#comment-27390)
* [Tristan Nitot](https://standblog.org/) on [libcurl memory use some years later](https://daniel.haxx.se/blog/2026/01/21/libcurl-memory-use-some-years-later/comment-page-1/#comment-27389)
* [Daniel Stenberg](https://daniel.haxx.se/) on [libcurl memory use some years later](https://daniel.haxx.se/blog/2026/01/21/libcurl-memory-use-some-years-later/comment-page-1/#comment-27387)
* [Brad Knowles](http://www.shub-internet.org) on [libcurl memory use some years later](https://daniel.haxx.se/blog/2026/01/21/libcurl-memory-use-some-years-later/comment-page-1/#comment-27386)
* David Newgas on [libcurl memory use some years later](https://daniel.haxx.se/blog/2026/01/21/libcurl-m...