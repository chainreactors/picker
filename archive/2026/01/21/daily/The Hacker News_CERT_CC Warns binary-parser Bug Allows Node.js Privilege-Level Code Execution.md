---
title: CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution
url: https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html
source: The Hacker News
date: 2026-01-21
fetch_date: 2026-01-22T03:36:34.313184
---

# CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution

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

# [CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution](https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html)

**Ravie Lakshmanan**Jan 21, 2026Open Source / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidgbhveMnZAVV1RKf0coJN00ixwRd8lYIUz58lpP4qC-LhuOGvgZ7IG87XxkhQaR6bnvCY_Sl5yQ2yQyAr_V9oVZ9eCHWpOszGUOLyKWkygMpSyxAs0H7Zlu56FhRnBNeLW34FA_-1G3pcpoj81hDxxHr1MBJl7MD0UBDau3Nl43IVX-r2RsWDBksVyflV/s1600-e365/binary-parser.jpg)

A security vulnerability has been disclosed in the popular [binary-parser npm library](https://github.com/keichi/binary-parser) that, if successfully exploited, could result in the execution of arbitrary JavaScript.

The vulnerability, tracked as **[CVE-2026-1245](https://www.cve.org/CVERecord?id=CVE-2026-1245)** (CVSS score: N/A), affects all versions of the module prior to [version 2.3.0](https://www.npmjs.com/package/binary-parser?activeTab=versions), which addresses the issue. Patches for the flaw were released on November 26, 2025.

Binary-parser is a widely used parser builder for JavaScript that allows developers to parse binary data. It supports a wide range of common data types, including integers, floating-point values, strings, and arrays. The package attracts approximately 13,000 downloads on a weekly basis.

According to an [advisory](https://kb.cert.org/vuls/id/102648) released by the CERT Coordination Center (CERT/CC), the vulnerability has to do with a [lack of sanitization](https://github.com/keichi/binary-parser/pull/283) of user-supplied values, such as parser field names and encoding parameters, when the JavaScript parser code is dynamically generated at runtime using the "Function" constructor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

It's worth noting that the npm library builds JavaScript source code as a string that represents the parsing logic and compiles it using the Function constructor and caches it as an executable function to parse buffers efficiently.

However, as a result of CVE-2026-1245, an attacker-controlled input could make its way to the generated code without adequate validation, causing the application to parse untrusted data, resulting in the execution of arbitrary code. Applications that use only static, hard-coded parser definitions are not affected by the flaw.

"In affected applications that construct parser definitions using untrusted input, an attacker may be able to execute arbitrary JavaScript code with the privileges of the Node.js process," CERT/CC said. "This could allow access to local data, manipulation of application logic, or execution of system commands depending on the deployment environment."

Security researcher Maor Caplan has been credited with discovering and reporting the vulnerability. Users of binary-parser are advised to upgrade to version 2.3.0 and avoid passing user-controlled values into parser field names or encoding parameters.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JavaScript](https://thehackernews.com/search/label/JavaScript)[node.js](https://thehackernews.com/search/label/node.js)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[secure coding](https://thehackernews.com/search/label/secure%20coding)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:image/svg+xml;base64... "n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens")

n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

[![New Advanced Linux VoidLink Malware Targets Cloud and container Environments](data:image/svg+xml;base64... "New Advanced Linux VoidLink Malware Targets Cloud and container Environments")

New Advanced Linux VoidLink Malware Targets Cloud and container Environments](https://thehackernews.com/2026/01/new-advanced-linux-voidlink-malware.html)

[![Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow](data:image/svg+xml;base64... "Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow")

Critical Node.js Vulnerability Can Cause Server Crashes via async\_hooks Stack Overflow](https://thehackernews.com/2026/01/critical-nodejs-vulnerability-can-cause.html)

[![Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](data:image/svg+xml;base64... "Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution")

Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html)

[![Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login](data:image/svg+xml;base64... "Palo Alto Fixes GlobalProtect DoS Flaw Tha...