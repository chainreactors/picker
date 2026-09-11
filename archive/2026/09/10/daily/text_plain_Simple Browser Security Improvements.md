---
title: Simple Browser Security Improvements
url: https://textslashplain.com/2026/09/10/simple-browser-security-improvements/
source: text/plain
date: 2026-09-10
fetch_date: 2026-09-11T06:51:48.731892
---

# Simple Browser Security Improvements

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Simple Browser Security Improvements

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-09-102026-09-10](https://textslashplain.com/2026/09/10/simple-browser-security-improvements/)Posted in[browsers](https://textslashplain.com/category/browsers/), [design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/)

Security Engineering is all about tradeoffs:

* [Security vs. Privacy](https://textslashplain.com/2023/10/04/security-tradeoffs-privacy/)
* Security vs. Performance
* Security vs. Compatibility
* Security vs. Usability

Web Browsers attempt to achieve an absolutely bananas goal: Allow safe execution of untrusted content on a user’s device.

Browsers are a huge vector for compromise of users’ devices and personal information, owing to the power and complexity. Much of the vulnerability induced by browsers occur where tradeoffs were either made poorly initially, or where the tradeoff would be made differently knowing what we know now.

So, what should we do? Here’s a modest list of proposals, many of which could be achieved in less than one dev day:

1. Disallow [random websites from going fullscreen](https://textslashplain.com/2023/09/12/attack-techniques-fullscreen-abuse/) without permission
2. Allow simple Enterprise control of what [types of files](https://textslashplain.com/2023/04/05/file-types/) are allowed to download — current controls are [comically underpowered](https://textslashplain.com/2021/05/19/download-blocking-by-file-type/#:~:text=for%20dangerous%20content.-,Group%20Policies,-DownloadRestrictions%20is%20a). (<https://issues.chromium.org/issues/40265750>)
3. Block download UI launch of [high-risk file types](https://textslashplain.com/2024/05/20/attack-techniques-full-trust-script-downloads/) that the OS has inexplicably failed to secure
4. Introduce a pre-fetch security check to allow security software to block malicious requests (similar to [this](https://textslashplain.com/2025/06/10/apple-url-filter-api/))
5. Call [AMSI](https://textslashplain.com/2024/10/25/defensive-technology-antimalware-scan-interface-amsi/) to [detect malicious content copied to the clipboard](https://textslashplain.com/2025/04/15/vibe-coding-for-security/) (<https://issues.chromium.org/issues/440381280>)
6. Call AMSI when installing a new [browser extension](https://textslashplain.com/2024/03/07/browser-extensions-powerful-and-potentially-dangerous/) or restarting the browser to allow local security software insight of what code can impact the user’s browsing experience
7. Stop supporting [UserInfo in URLs](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/) or introduce a warning
8. Disallow user-navigation to `javascript:` URLs or introduce a warning (<https://issues.chromium.org/issues/559142626>)
9. Further restrict notification permissions to prevent [scams and spam](https://textslashplain.com/2022/09/27/badware-techniques-notification-spam/)
10. *more to come, I’m sure*

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/09/10/simple-browser-security-improvements/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/09/10/simple-browser-security-improvements/?share=facebook)

### Like this:

Like Loading…

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-09-102026-09-10](https://textslashplain.com/2026/09/10/simple-browser-security-improvements/)Posted in[browsers](https://textslashplain.com/category/browsers/), [design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
The Windows Security App](https://textslashplain.com/2026/08/31/the-windows-security-app/)

### Leave a Reply[Cancel reply](/2026/09/10/simple-browser-security-improvements/#respond)

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

[![RSS feed](https://textslashplain.com/wp-content/plugins/jetpack/images/rss/orange-small.png) RSS - Posts](https://textslashplain.com/feed/ "Subscribe to posts")

## Blog Stats

* 2,512,443 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (186)
design  (26)
dev  (87)
fiddler  (26)
life  (55)
perf  (20)
politics  (2)
privacy  (27)
reviews  (2)
running  (20)
security  (177)
storytelling  (50)
tech  (39)
travel  (9)
Uncategorized  (16)
web  (154)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.

[View Full Profile →](https://gravatar.com/ericlaw1979)

[text/plain](https://textslashplain.com/),
[Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered).

## Discover more from text/plain

Subscribe now to keep reading and get access to the full archive.

Type your email…

Subscribe

Continue reading

%d