---
title: OSI approved the curl license
url: https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/
source: daniel.haxx.se
date: 2026-10-15
fetch_date: 2026-10-16T06:35:55.907002
---

# OSI approved the curl license

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/05/old-document.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# OSI approved the curl license

[October 15, 2026](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/#respond)

curl started out GPL licensed, as direct inheritance from its httpget days, but in October 1998 we switched to the Mozilla Public License (MPL).

In 2001, we added the MIT license as an additional license to optionally use in addition to MPL. We made curl *dual licensed* because clearly the MPL license caused problems for some users – primarily because it was deemed not compatible with GPL.

In 2002 we dropped the MPL option and curl was from then on licensed only under the MIT license. Kind of.

## The twist

Because of reasons we cannot recall anymore, I decided to ever so slightly edit the language in the MIT license text around that time. (I strongly discourage anyone else from doing this, and if my time machine was functional I would go back and correct this decision.)

The license text we then kept referring to and thinking about as an MIT license, was in fact not exactly MIT anymore. No one objected at the time. I can’t remember anyone really considering the implications at the time. Maybe because not that many people noticed or cared. It was *in essence* still the MIT license.

## Much later

Decades later, the [SPDX project](https://spdx.dev/) quite correctly and *ruthlessly* made the distinction between a proper MIT and a modified MIT matter: they created a separate and unique identified to the license curl uses. It may be *almost* like MIT but they deemed the differences big enough to say that [the curl license](https://spdx.org/licenses/curl.html) is a special beast. It is since then known as the curl license.

`SPDX-License-Identifier: curl`

## Sort of MIT but not

I have over the years casually kept referring to the license as MIT since it helps users understand even though it is technically incorrect. Open Source people in general tend to know the MIT license and the implications of using it.

A drawback with having our own license is that it was not immediately recognized and known as Open Source or Free Software; not acknowledged and verified by FSF nor OSI.

## OSI approved

On April 17, 2026. The Open Source Initiative [approved the curl license](https://opensource.org/license/curl). It is since then officially arguably slightly more *Open Source* than before.

I don’t think anyone ever doubted or that it was actually much of a drawback in adoption or usage, but it feels good to finally have this checkmark.

## Why now?

I write about this *now* (many months after the fact) because I totally forgot that this was happening and I only recently realized OSI approved it back in April.

## The curl license verbatim

```
COPYRIGHT AND PERMISSION NOTICE

Copyright (c) 1996 - 2026, Daniel Stenberg, daniel@haxx.se, and many contributors, see the THANKS file.

All rights reserved.

Permission to use, copy, modify, and distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF THIRD PARTY RIGHTS. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of a copyright holder shall not be used in advertising or otherwise to promote the sale, use or other dealings
in this Software without prior written authorization of the copyright holder.
```

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[FSF](https://daniel.haxx.se/blog/tag/fsf/)[GPL](https://daniel.haxx.se/blog/tag/gpl/)[Licensing](https://daniel.haxx.se/blog/tag/licensing/)[Open Source](https://daniel.haxx.se/blog/tag/open-source/)

# Post navigation

[Previous PostA curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)

### Leave a Reply [Cancel reply](/blog/2026/10/15/osi-approved-the-curl-license/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
fourone8one2

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)
  October 15, 2026
* [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)
  October 14, 2026
* [A UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
  October 14, 2026
* [curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/)
  October 14, 2026
* [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)
  October 13, 2026
* [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/)
  October 12, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27559)
* Jeremy Robst on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27558)
* [Daniel Stenberg](https://daniel.haxx.se/) on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27556)
* Andrei on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27555)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27551)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27550)
* Nick on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27549)
* [Moritz Buhl](https://moritzbuhl.de) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27547)
* [Daniel Stenberg](https://daniel.haxx.se/) on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27545)
* Nun Your Beeswax Inc. on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27544)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

October 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | 6 | [7](https://...