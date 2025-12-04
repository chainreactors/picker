---
title: Security Surfaces
url: https://textslashplain.com/2025/12/03/security-surfaces/
source: text/plain
date: 2025-12-03
fetch_date: 2025-12-04T03:17:46.379894
---

# Security Surfaces

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Security Surfaces

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-12-032025-12-03](https://textslashplain.com/2025/12/03/security-surfaces/)Posted in[design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Chrome](https://textslashplain.com/tag/chrome/), [security](https://textslashplain.com/tag/security/), [UX](https://textslashplain.com/tag/ux/)

An important concept in Usable Security is whether a given UI represents a “security surface.” Formally, **a security surface is a User Interface component in which the user is presented with information they rely upon to make a security decision.** For example, in the browser, the URL in the address bar is a security surface. Importantly, a **spoofing issue** in a security surface ***usually* represents a security vulnerability.**

Just as importantly, not all UI surfaces are security surfaces. There are always many other UI surfaces in which similar information may be presented that are not (and cannot be) security surfaces.

Unfortunately, knowing which surfaces are security surfaces and which are not is simultaneously

1. **Critically important** – *If you think an untrustworthy surface is trustworthy, you might get burned*.
2. **Unintuitive** – *There’s usually no indication that a surface is untrustworthy.*

Eight years ago, Chromium wrote a document [listing the Chrome browser’s security surfaces](https://docs.google.com/document/d/11-SXwzCGBlk8q1cNtb7peZjb2UjRPrKSFhOfZhTOz24/edit?pli=1&tab=t.0#heading=h.1z4bmn246gst). *Approximately* no one has ever seen it.

### Non-Security Surfaces

Perhaps the most famous non-security surface is the “status bubble” shown at the bottom left of the browser window that’s designed to show the user where a given link will go:

[![](https://textslashplain.com/wp-content/uploads/2025/12/image-1.png?w=549)](https://textslashplain.com/wp-content/uploads/2025/12/image-1.png)

The Chromium “Status Bubble”

There are many reasons why this UI cannot be a security surface.

The primary issue is that it’s [below the line-of-death](https://textslashplain.com/2017/01/14/the-line-of-death/), in a visual area of the page that an attacker can control to paint anything they like. The line-of-death is a major reason why many UIs cannot be considered security surfaces — if an attacker has control over what the user sees, a UI cannot be “secure.”

But even without that line-of-death problem, there are other vulnerabilities: most obviously, JavaScript can cancel a navigation when it begins, or it can rewrite the target of a link as the user clicks on it. Or the link could point to a redirector site (e.g. `bit.ly`) rather than the ultimate destination. etc.

### Challenging Security Surfaces: The “URL Bar”

Perhaps the most complicated security surface in existence is the browser’s address bar, known in Chromium-based browsers as the “Omnibox”.

[![](https://textslashplain.com/wp-content/uploads/2025/12/image.png?w=521)](https://textslashplain.com/wp-content/uploads/2025/12/image.png)

The “omnibox” in modern Edge

That *omni*box naming reflects why this is such a tricky security surface: Because it tries to do multiple things: It tries to be a **security surface** which shows the current security context of the currently-loaded page (e.g. `https://example.com`), but it *also* tries to be a **information surface** which shows the full URL of the page (e.g. `https://example.com/folder/page.html?query=a#fragment`), and it tries to be an **input surface** that allows the user to input a new URL or search query. Only certain portions of the URL information are security-relevant, and the remainder of the URL could be used to [confuse the user](https://chromium.googlesource.com/chromium/src/%2B/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md) about the security-relevant parts.

Making matters even *more* complicated, the omnibox also has to deal with asynchronicity — what should be shown in the box when the user is in the middle of a navigation, where the user’s entered URL isn’t yet loaded and the current URL isn’t yet unloaded?

### Windows LNK Inspection

Earlier this year, a security vulnerability report was [filed](https://msrc.microsoft.com/update-guide/advisory/ADV25258226) complaining that Windows File Explorer would not show the full target of a `.lnk` file if the target was longer than 260 characters.

[![](https://textslashplain.com/wp-content/uploads/2025/12/image-2-1.png?w=398)](https://textslashplain.com/wp-content/uploads/2025/12/image-2-1.png)

Windows File Explorer’s .lnk Properties Dialog

The reporter complained that without accurate information in the UI, a user couldn’t know whether a LNK file was safe.

This is true, but it’s also the case that the user isn’t being asked to make a security decision in this dialog; the UI where the user *is* asked to make a security decision doesn’t even show the target at all:

[![](https://textslashplain.com/wp-content/uploads/2025/12/image-3.png?w=510)](https://textslashplain.com/wp-content/uploads/2025/12/image-3.png)

Windows Security Warning prompt when opening a LNK file from the Internet Zone

Even in the *exceptionally unlikely* event that a user uses Explorer’s LNK inspection UI, very few users could actually make a safe determination based on the information within. Ultimately the guidance in the Security Warning prompt is the right advice: “*If you do not trust the source, do not open*.”

The Windows team ended up fixing the display truncation earlier this year, but not as a security fix, just a [general quality-improvement for Windows 11 24H2+](https://blog.0patch.com/2025/12/microsoft-silently-patched-cve-2025.html).

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2025/12/03/security-surfaces/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2025/12/03/security-surfaces/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-12-032025-12-03](https://textslashplain.com/2025/12/03/security-surfaces/)Posted in[design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Chrome](https://textslashplain.com/tag/chrome/), [security](https://textslashplain.com/tag/security/), [UX](https://textslashplain.com/tag/ux/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Defensive Technology: Ransomware Data Recovery](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/)

### Leave a comment [Cancel reply](/2025/12/03/security-surfaces/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Real-World Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com/feed/ "Subscribe to Posts")

## Blog Stats

* 2,420,671 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browser...