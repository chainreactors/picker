---
title: Opera Browser Fixes Big Security Hole That Could Have Exposed Your Information
url: https://thehackernews.com/2024/10/opera-browser-fixes-big-security-hole.html
source: The Hacker News
date: 2024-10-31
fetch_date: 2025-10-06T18:58:09.528528
---

# Opera Browser Fixes Big Security Hole That Could Have Exposed Your Information

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Opera Browser Fixes Big Security Hole That Could Have Exposed Your Information](https://thehackernews.com/2024/10/opera-browser-fixes-big-security-hole.html)

**Oct 30, 2024**Ravie Lakshmanan Browser Security / Vulnerability

[![Opera Browser](data:image/png;base64... "Opera Browser")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRyMsVeMT7VtRd_QXkviMkb25Nd_aEb6Sw7aJ9whsaekrv8OhxD5u1HDlUW4MqfEDS6NijHlJGrVQL0M6g0zqXzR66MS7oqrKGIbzx4ahexyKFjzFyo93IZo44_Jt6MpJRzwW0dX21ufgAWSDsZMcVqQidGbjRE8GB4y_Xx-JFtIHlaL6iyYpAB7dK3wT9/s790-rw-e365/attack.png)

A now-patched security flaw in the Opera web browser could have enabled a malicious extension to gain unauthorized, full access to private APIs.

The attack, codenamed **CrossBarking**, could have made it possible to conduct actions such as capturing screenshots, modifying browser settings, and account hijacking, Guardio Labs said.

To demonstrate the issue, the company said it managed to publish a seemingly harmless browser extension to the Chrome Web Store that could then exploit the flaw when installed on Opera, making it an instance of a cross-browser-store attack.

"This case study not only highlights the perennial clash between productivity and security but also provides a fascinating glimpse into the tactics used by modern threat actors operating just below the radar," Nati Tal, head of Guardio Labs, [said](https://labs.guard.io/crossbarking-how-an-opera-0-day-could-have-been-exploited-by-a-cross-browser-extension-store-db3e6d6e6aa8) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The issue has been [addressed](https://blogs.opera.com/desktop/2024/09/opera-113-0-5230-132-stable-update/) by Opera as of September 24, 2024, following responsible disclosure. That said, this is not the first time security flaws have been identified in the browser.

Earlier this January, details emerged of a vulnerability tracked as [MyFlaw](https://thehackernews.com/2024/01/opera-myflaw-bug-could-let-hackers-run.html) that takes advantage of a legitimate feature called My Flow to execute any file on the underlying operating system.

The latest attack technique hinges on the fact that several of Opera-owned publicly-accessible subdomains have privileged access to private APIs embedded in the browser. These domains are used to support Opera-specific features like Opera Wallet, Pinboard, and others, as well as those that are used in internal development.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs6FCh8ZMaVMAL0b3vCYPaJTWBJR64n5JDZwPeLKxqD1CWQW3dME_-eYrI0u6UT2_YEeNh0LTe1wY2Pjlw2xiLgsiCa76kzD-ekqJJri7WLfwZi4U4SKMriGdLeazdPGdYbfy_c2nBdI78UEapbJxPng0Ivw0C1IjybadqWUJC394TiCiYzB1pi3_fOysK/s790-rw-e365/1000073803.png)

The names of some of the domains, which also include certain third-party domains, are listed below -

* crypto-corner.op-test.net
* op-test.net
* gxc.gg
* opera.atlassian.net
* pinboard.opera.com
* instagram.com
* yandex.com

While sandboxing ensures that the browser context remains isolated from the rest of the operating system, Guardio's research found that [content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts) present within a browser extension could be used to inject malicious JavaScript into the overly permissive domains and gain access to the private APIs.

"The content script does have access to the DOM (Document Object Model)," Tal explained. "This includes the ability to dynamically change it, specifically by adding new elements."

Armed with this access, an attacker could take screenshots of all open tabs, extract session cookies to hijack accounts, and even modify a browser's DNS-over-HTTPS (DoH) settings to resolve domains through an attacker-controlled DNS server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This could then set the stage for potent adversary-in-the-middle (AitM) attacks when victims attempt to visit bank or social media sites by redirecting them to their malicious counterparts instead.

The malicious extension, for its part, could be published as something innocuous to any of the add-on catalogs, including the Google Chrome Web Store, from where users could download and add it to their browsers, effectively triggering the attack. It, however, requires permission to run JavaScript on any web page, particularly the domains that have access to the private APIs.

With [rogue browser extensions](https://thehackernews.com/2024/08/new-malware-hits-300000-users-with.html) repeatedly infiltrating the official stores, not to mention some legitimate ones that [lack transparency](https://www.wizcase.com/blog/privacy-overreach-of-ai-browser-extensions/) into their data collection practices, the findings underscore the need for caution prior to installing them.

"Browser extensions wield considerable power — for better or for worse," Tal said. "As such, policy enforcers must rigorously monitor them."

"The current review model falls short; we recommend bolstering it with additional manpower and continuous analysis methods that monitor an extension's activity even post-approval. Additionally, enforcing real identity verification for developer accounts is crucial, so simply using a free email and a prepaid credit card is insufficient for registration."

### Update

When reached for comment, Opera shared the following statement with The Hacker News -

*The vulnerability in question was discovered as part of our ongoing work with third-party researchers to identify security flaws and fix them before they have had a chance to be exploited by bad actors. Responsible disclosure is a best practice in cybersecurity, helping software providers stay ahead of threats and allowing researchers to raise awareness about these important issues.*

*It's important to note that the vulnerability that Guardio identified could put a user at risk of attack if the...