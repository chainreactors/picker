---
title: WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session
url: https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:54.097936
---

# WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session](https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPBWV1XNsTGB5ImLNRGJTygk0-82k7xTHmuOr7lTivRRDcF83ddu4jLOpdkQYMq7VB3j5SMpA9zBRvM3-SUkDLBhN5-j-Z6UltcTnVfXOxHDzfBYWiw_fRiRefAYa1XSiFu5JMzb06dwqV4PhKaZkPt3vKZFHQjdVFUgbr2B3nOEoFs_qHe6zwGayHM2I/s1700-nu-rw-lo-l85-e365/wordpress-comment.jpg)

A new flaw in WordPress core let an anonymous visitor leave a comment that planted a hidden script on the page. If a logged-in administrator later opened that page, the script could run code on the site's server.

WordPress fixed the flaw, tracked as [CVE-2026-93485](https://www.cve.org/CVERecord?id=CVE-2026-93485) and called "**Comment2Shell**," on September 17 in [version 7.1.1](https://wordpress.org/news/2026/09/wordpress-7-1-1-maintenance-and-security-release/) and told site owners to update right away. There is no sign it has been used in attacks, and it is not on the U.S. government's list of actively exploited software flaws.

Patchstack, the company that assigned that identifier, rated the flaw 7.1 out of 10 on the CVSS scale.

WordPress checks a comment for dangerous HTML when it is saved, then reformats it when the page is shown, and the flaw sat in the gap between those two steps.

Rafie Muhammad, the security researcher who reported the bug, laid out the full chain in [a write-up](https://idnsec.com/research/comment2shell-zero-click-pre-auth-xss-to-rce-in-wordpress-core/) on September 21. The trick was a line break placed inside the attribute of an allowed HTML tag in the comment.

When WordPress reformatted the comment for display, one of its steps broke that tag apart and moved the attacker's text into a spot where the browser treated it as a live event handler. The handler ran automatically as the page loaded, with no click required.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The script ran in the browser of whoever opened the page, whether or not they were logged in, and it acted with that person's access level to the site.

Running code on the server needed one more condition. A logged-in administrator had to open the page carrying the comment.

The script could then use the administrator's own session to upload a plugin containing a web shell, a small file that executes whatever commands an attacker sends. Uploading a plugin this way is a known route from an administrator's browser to control of the server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRCOnP5nuFPeUceIcq2anDN9x7ACXA6CFXDrx3K4SuMV28VavLLjw-9kkzy5hTaW-LN2q07hIoUPOb8xiazj85JP7NZ6TZbpb3dH6jzAEK87CnqkYHqco9Awgupfr1vzVyvvyBm6Mqeh5jvrkcmz6mei3cG7ykbBIwXs8jfoRcBuhSfVjLMJOydcMw6go/s1700-nu-rw-lo-l85-e365/comment2shell-poc.gif)

The attack also depended on how a site displayed its comments. It worked on sites that use a block theme, which has been the default in WordPress since Twenty Twenty-Two. Some classic themes were affected too, where they format comments through the same step; the write-up names Twenty Twenty-One as one.

For any of this to happen, the comment had to appear on the page first. WordPress described the flaw as exploitable only "subject to comment approval."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis-_OADpk-7QUnBg7Kdd-Aw6UZd3ky5DXli-5H8MMRyXCTYkg5lw2RfwxuKC3bk7opG_Xe9bVeAdfvmmOjt2bo4OscOzbBcK27x1bTduxoXA-DHgSI1Vma3AZR3J5BvGh-5jTsmnHvUKqaSGaPNS2eTNE277qsYUgLdPnQXpVF5a_BXHWnt0wsxHgMLyc/s1700-nu-rw-lo-l85-e365/comment2shell-working.gif)

By default, a comment from a new author is held until someone approves it, so it does not appear on its own. But the researcher described ways around that check, letting a comment reach the page without approval. As Patchstack put it, ["moderation isn't a security control."](https://patchstack.com/articles/wordpress-7-1-1-maintenance-and-security-release/)

### What to do

Update to WordPress 7.1.1, or to the latest release on your branch if it still gets security fixes. The affected versions run from 4.7 through 7.1, and these are the fixed releases for the current branches:

* WordPress 7.1: update to 7.1.1
* WordPress 7.0: update to 7.0.5
* WordPress 6.9: update to 6.9.8
* Older branches, back to 4.7: install the fixed release for your branch, as far back as 4.7.36, [listed for each branch in WordPress's release documentation](https://wordpress.org/documentation/wordpress-version/version-7-1-1/)

A site that cannot update at once can shut the way in by closing comments on posts or turning comments off across the site, and a web application firewall or a security plugin may block the crafted comment.

Neither WordPress nor the researcher published a separate workaround. Muhammad recommended simply updating WordPress core, noting that 7.1.1 is a security release. Updating fixes the flaw, but it does not undo any change an attacker already made. A site with reason to think it was targeted should also look for plugins or files it does not recognize.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

WordPress 7.1.1 fixed 11 security problems in all. This comment flaw was the only one that an attacker with no account could access, and most of the others required a logged-in user with some level of access.

The same release fixed a second flaw, called [Click2Shell](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html), in which a crafted link could make WordPress install a theme and, together with a second weakness in that theme, run code on the server. It, too, required a logged-in administrator to open the link.

WordPress core has had other serious flaws this year. In July, a bug called [wp2shell]...