---
title: “Not Secure” Warning for IE Mode
url: https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/
source: text/plain
date: 2022-11-17
fetch_date: 2025-10-03T23:01:12.191339
---

# “Not Secure” Warning for IE Mode

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# “Not Secure” Warning for IE Mode

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2022-11-162022-11-16](https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[Edge](https://textslashplain.com/tag/edge/), [https](https://textslashplain.com/tag/https/), [IEMode](https://textslashplain.com/tag/iemode/), [Internet Explorer](https://textslashplain.com/tag/internet-explorer/), [mixed content](https://textslashplain.com/tag/mixed-content/)

A customer recently wrote to ask whether there was any way to suppress the red “**/!\ Not Secure**” warning shown in the omnibox when IE Mode loads a HTTPS site containing non-secure images:

[![](https://textslashplain.com/wp-content/uploads/2022/11/image-5.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/11/image-5.png)

Notably, this warning isn’t seen when the page is loaded in modern Edge mode or in Chrome, because all non-secure “optionally-blockable” resource requests are upgraded to use HTTPS. If HTTPS upgrade doesn’t work, the image is simply blocked.

[![](https://textslashplain.com/wp-content/uploads/2022/11/image-4.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/11/image-4.png)

The customer observed that when loading this page in the legacy Internet Explorer application, no “Not Secure” notice was shown in IE’s address bar– instead, the lock icon just silently disappeared, as if the page were served over HTTP.

*Background: There are two kinds of mixed content, passive (images, css) and active (scripts). Passive mixed content is less dangerous than active: a network attacker can replace the contents of a HTTP-served image, but only impact that image. In contrast, a network attacker can replace the contents of a HTTP-served script and use that script to completely rewrite the whole page. By default, IE silently* allows *passive mixed content (hiding the lock) while* blocking *active mixed content (preserving the lock, because the non-secure download was blocked).*

The customer wondered whether there was a policy they could set to prevent the red warning for passive mixed content in Edge’s IE Mode. Unfortunately, the answer is “not directly.”

IE Mode is not sensitive to the Edge [policies](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#overridesecurityrestrictionsoninsecureorigin), so only the IE Settings controlling mixed content apply in this scenario.

When the IE Mode object communicates up to the Edge host browser, the security state of the page in IEMode is represented by an enum containing just three values: `Unsecure,` `Mixed`, and `Secure`. Unsecure is used for HTTP, Secure is used for HTTPS, and `Mixed` is used whenever the page loaded with mixed content, either active **or** passive. As a consequence, there’s presently no way for the Edge host application to mimic the old IE behavior, because it doesn’t know whether IEMode *displayed* passive mixed content, or *ran* active mixed content.

Because both states are munged together, the code that chooses the UI warning state selects the most alarming option:

`content_status |= SSLStatus::RAN_INSECURE_CONTENT;`

…and that’s status is treated as a more severe problem:

```
SecurityLevel kDisplayedInsecureContentWarningLevel = WARNING;
SecurityLevel kRanInsecureContentLevel = DANGEROUS;
```

Now, even if the Edge UI code assumed the more benign `DISPLAYED_INSECURE_CONTENT` status, the browser would just show the same “Not secure” text in grey rather than red– the warning text would still be shown.

In terms of what a customer can do about this behavior (and assuming that they don’t want to actually secure their web content): they can change the IE Mode configuration to block the images in one of two ways:

Option #1: Change [IE Zone settings](https://textslashplain.com/2020/01/30/security-zones-in-edge/) to block mixed content. All mixed content is silently blocked and the lock is preserved:

[![](https://textslashplain.com/wp-content/uploads/2022/11/image-7.png?w=443)](https://textslashplain.com/wp-content/uploads/2022/11/image-7.png)

Option #2: Change IE’s Advanced > Security Settings to “Block insecure images with other mixed content”, you see the lock is preserved and the IE-era notification bar is shown at the bottom of the page:

[![](https://textslashplain.com/wp-content/uploads/2022/11/image-8.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/11/image-8.png)

Stay secure out there!

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2022-11-162022-11-16](https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[Edge](https://textslashplain.com/tag/edge/), [https](https://textslashplain.com/tag/https/), [IEMode](https://textslashplain.com/tag/iemode/), [Internet Explorer](https://textslashplain.com/tag/internet-explorer/), [mixed content](https://textslashplain.com/tag/mixed-content/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Microsoft Employee’s Guide to Maximizing Donations](https://textslashplain.com/2022/10/21/microsoft-employees-guide-to-maximizing-donations/)

[Next Post Next post:
Thoughts on Twitter](https://textslashplain.com/2022/11/17/thoughts-on-twitter/)

### Leave a comment [Cancel reply](/2022/11/16/not-secure-warning-for-ie-mode/#respond)

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

* 2,396,273 hits

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

* [Comment](https://textslashplain.com/2022/11/16/not-secure-warning-for-ie-mode/#respo...