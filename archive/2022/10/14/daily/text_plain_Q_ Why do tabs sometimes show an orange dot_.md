---
title: Q: Why do tabs sometimes show an orange dot?
url: https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/
source: text/plain
date: 2022-10-14
fetch_date: 2025-10-03T19:50:26.531073
---

# Q: Why do tabs sometimes show an orange dot?

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Q: Why do tabs sometimes show an orange dot?

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2022-10-132022-10-13](https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/)Posted in[browsers](https://textslashplain.com/category/browsers/), [design](https://textslashplain.com/category/design/), [web](https://textslashplain.com/category/tech/web/)Tags:[Chrome](https://textslashplain.com/tag/chrome/), [Edge](https://textslashplain.com/tag/edge/), [UI](https://textslashplain.com/tag/ui/)

Sometimes, you’ll notice that a background tab has an orange dot on it in Edge (or a blue dot in Chrome). If you click on the tab, the dot disappears.

[![](https://textslashplain.com/wp-content/uploads/2022/10/image-12.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/10/image-12.png)

The center tab has an orange dot which is not a part of the site’s FavIcon

Why?

The dot indicates that the tab [wants “attention”](https://source.chromium.org/chromium/chromium/src/%2B/main%3Achrome/browser/ui/views/tabs/tab.h;l=149;drc=816f6103028b629940ce781fdf99250b9fa50f0e) — more specifically, that there’s a dialog in the tab asking for your attention. This might be a [JavaScript `alert()` or `confirm()` dialog](https://bayden.com/test/dialogs.asp), or a prompt [requesting permission to launch an Application Protocol](https://textslashplain.com/2020/02/20/bypassing-appprotocol-prompts/):

[![](https://textslashplain.com/wp-content/uploads/2022/10/image-13.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/10/image-13.png)

Years ago, the dot also *used* to appear any time the title of a pinned tab changed (because pinned tabs don’t show their titles) but that code was [removed in 2018](https://bugs.chromium.org/p/chromium/issues/detail?id=482776#c38).

Nowadays, web content cannot directly trigger the dot icon (short of showing an `alert()`) but some sites will draw their own indicator by [updating their favicon](https://bayden.com/test/favicon/dynamic.htm) using JavaScript:

[![](https://textslashplain.com/wp-content/uploads/2022/10/image-14.png?w=318)](https://textslashplain.com/wp-content/uploads/2022/10/image-14.png)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2022-10-132022-10-13](https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/)Posted in[browsers](https://textslashplain.com/category/browsers/), [design](https://textslashplain.com/category/design/), [web](https://textslashplain.com/category/tech/web/)Tags:[Chrome](https://textslashplain.com/tag/chrome/), [Edge](https://textslashplain.com/tag/edge/), [UI](https://textslashplain.com/tag/ui/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2022/10/12/capturing-logs-for-debugging-smartscreen/)

[Next Post Next post:](https://textslashplain.com/2022/10/21/microsoft-employees-guide-to-maximizing-donations/)

### Leave a comment [Cancel reply](/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com/feed/ "Subscribe to Posts")

## Blog Stats

* 2,392,648 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (183)
design  (21)
dev  (84)
fiddler  (25)
life  (52)
perf  (20)
politics  (2)
privacy  (26)
reviews  (2)
running  (18)
security  (158)
storytelling  (47)
tech  (34)
travel  (9)
Uncategorized  (16)
web  (151)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.

[View Full Profile →](https://gravatar.com/ericlaw1979)

[text/plain](https://textslashplain.com/),
[A WordPress.com Website](https://wordpress.com/?ref=footer_custom_acom).

* [Comment](https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2022%252F10%252F13%252Fq-why-do-tabs-sometimes-show-an-orange-dot%252F)
* + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2022%252F10%252F13%252Fq-why-do-tabs-sometimes-show-an-orange-dot%252F)
  + [Copy shortlink](https://wp.me/p60i9o-1GJ)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://textslashplain.com/2022/10/13/q-why-do-tabs-sometimes-show-an-orange-dot/)
  + [View post in Reader](https://wordpress.com/reader/blogs/88727790/posts/6493)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

Name (Required)

Website

###

%d

![](https://pixel.wp.com/b.gif?v=noscript)