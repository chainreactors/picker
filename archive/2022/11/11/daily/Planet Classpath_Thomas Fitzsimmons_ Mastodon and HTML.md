---
title: Thomas Fitzsimmons: Mastodon and HTML
url: https://www.fitzsim.org/blog/?p=465
source: Planet Classpath
date: 2022-11-11
fetch_date: 2025-10-03T22:21:32.533663
---

# Thomas Fitzsimmons: Mastodon and HTML

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Mastodon and HTML

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [November 10, 2022November 16, 2022](https://www.fitzsim.org/blog/?p=465)
[Leave a comment on Mastodon and HTML](https://www.fitzsim.org/blog/?p=465#respond)

**Request to Mastodon instance operators: Provide a read-only anonymous HTML-only mode.**

*Update 2022-11-17: Mastodon supports RSS; try just tacking “.rss” onto the end of a Mastodon URL.  It doesn’t seem to work for comment threads, but it does work for main threads. For example*

```
M-x gnus ENTER G R https://mastodon.social/@markmccaughrean.rss ENTER
```

*will create a Gnus group containing the author’s Mastodon posts.  This is a nice workaround, though I do still hope logged-out HTML-only browsing will be possible again, post 4.x.  Thanks to the helpful people on the #mastodon IRC channel for the above suggestion.*

I’ve been following some Mastodon instances for several months. In Emacs, I type:

```
ESCAPE x eww ENTER https://mastodon.ar.al/@aral ENTER
```

and, without any authentication requirement, I’m greeted with a read-only HTML view of the instance, for example:

![Example toot in Mastodon v3.5.3 HTML-only mode.](https://www.fitzsim.org/screenshots/mastodon-v3.5.3-html-mode.png)

Example toot in Mastodon v3.5.3 HTML-only mode.

This week I tried another instance

```
ESCAPE x eww ENTER https://mastodon.social/@markmccaughrean ENTER
```

and I am blocked by:

![Mastodon v4.0.0rc1 "please enable JavaScript" message.](https://www.fitzsim.org/screenshots/mastodon-v4.0.0rc1-javascript-mode.png)

Mastodon v4.0.0rc1 “please enable JavaScript” message.

Is this a new default? I was surprised that read-only anonymous HTML-only mode (ala Twitter classic and Nitter) is not supported by all Mastodon instances.

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[November 10, 2022November 16, 2022](https://www.fitzsim.org/blog/?p=465)Posted in[Requests](https://www.fitzsim.org/blog/?cat=10)

## Post navigation

[Previous Post Previous post:
uLisp on the SMART Response XE](https://www.fitzsim.org/blog/?p=460)

[Next Post Next post:
Thunderbird and OpenPGP](https://www.fitzsim.org/blog/?p=477)

## Leave a comment

### [Cancel reply](/blog/?p=465#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)