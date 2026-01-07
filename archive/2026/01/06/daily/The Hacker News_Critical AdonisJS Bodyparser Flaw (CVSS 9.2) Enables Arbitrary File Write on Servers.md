---
title: Critical AdonisJS Bodyparser Flaw (CVSS 9.2) Enables Arbitrary File Write on Servers
url: https://thehackernews.com/2026/01/critical-adonisjs-bodyparser-flaw-cvss.html
source: The Hacker News
date: 2026-01-06
fetch_date: 2026-01-07T03:30:45.952452
---

# Critical AdonisJS Bodyparser Flaw (CVSS 9.2) Enables Arbitrary File Write on Servers

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Critical AdonisJS Bodyparser Flaw (CVSS 9.2) Enables Arbitrary File Write on Servers](https://thehackernews.com/2026/01/critical-adonisjs-bodyparser-flaw-cvss.html)

**Jan 06, 2026**Ravie LakshmananVulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzO1cc-SgAdpaPJsJZj5THeCL4mn7tPUZbghNoDdS-5-NM8bsS9s-Rrp3VwPIm0bEP0qP4kasNmPfuo4Thkd1gWc-8tjPHwjb1lfacgHdfFvtPz2RXzqD-Ny9LecUi5kU4NHXxYkjzuAKSvToFOfBQjSwHcA43UzcfY__3PwwgO8muoNhYJ7Qr6qrOSP_U/s790-rw-e365/adonis-security.jpg)

Users of the "[@adonisjs/bodyparser](https://www.npmjs.com/package/%40adonisjs/bodyparser)" npm package are being advised to update to the latest version following the disclosure of a critical security vulnerability that, if successfully exploited, could allow a remote attacker to write arbitrary files on the server.

Tracked as CVE-2026-21440 (CVSS score: 9.2), the flaw has been described as a path traversal issue affecting the AdonisJS multipart file handling mechanism. "@adonisjs/bodyparser" is an npm package associated with AdonisJS, a Node.js framework for developing web apps and API servers with TypeScript. The library is used to [process AdonisJS HTTP request body](https://docs.adonisjs.com/guides/basics/request).

"If a developer uses MultipartFile.move() without the second options argument or without explicitly sanitizing the filename, an attacker can supply a crafted filename value containing traversal sequences, writing to a destination path outside the intended upload directory," the project maintainers [said](https://github.com/adonisjs/core/security/advisories/GHSA-gvq6-hvvp-h34h) in an advisory released last week. "This can lead to arbitrary file write on the server."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

However, successful exploitation hinges on a reachable upload endpoint. The problem, at its core, resides in a function named "[MultipartFile.move(location, options)](https://api.adonisjs.com/classes/_adonisjs_bodyparser.index.MultipartFile#move)" that allows a file to be moved to the specified location. The "options" parameter holds two values: the name of a file and an overwrite flag indicating "true" or "false."

The issue arises when the name parameter is not passed as input, causing the application to default to an unsanitized client filename that opens the door to path traversal. This, in turn, allows an attacker to choose an arbitrary destination of their liking and overwrite sensitive files, if the overwrite flag is set to "true."

"If the attacker can overwrite application code, startup scripts, or configuration files that are later executed/loaded, RCE [remote code execution] is possible," AdonisJS said. "RCE is not guaranteed and depends on filesystem permissions, deployment layout, and application/runtime behavior."

The issue, discovered and reported by Hunter Wodzenski (@[wodzen](https://github.com/wodzen)) impacts the following versions -

* <= 10.1.1 (Fixed in 10.1.2)
* <= 11.0.0-next.5 (Fixed in 11.0.0-next.6)

### Flaw in jsPDF npm Library

The development coincides with the disclosure of another path traversal vulnerability in an npm package named jsPDF ([CVE-2025-68428](https://nvd.nist.gov/vuln/detail/CVE-2025-68428), CVSS score: 9.2) that could be exploited to pass unsanitized paths and retrieve the contents of arbitrary files in the local file system the node process is running.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The vulnerability has been patched in jsPDF version 4.0.0 released on January 3, 2026. As workarounds, it's advised to use the [--permission flag](https://nodejs.org/api/permissions.html) to restrict access to the file system. A researcher named Kwangwoon Kim has been acknowledged for reporting the bug.

"The file contents are included verbatim in the generated PDFs," Parallax, the developers of the JavaScript PDF generation library, [said](https://github.com/parallax/jsPDF/security/advisories/GHSA-f8cm-6447-x5h2). "Only the node.js builds of the library are affected, namely the dist/jspdf.node.js and dist/jspdf.node.min.js files."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JavaScript](https://thehackernews.com/search/label/JavaScript)[node.js](https://thehackernews.com/search/label/node.js)[npm Packages](https://thehackernews.com/search/label/npm%20Packages)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Path Traversal](https://thehackernews.com/search/label/Path%20Traversal)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Application Security](https://thehackernews.com/search/label/Web%20Application%20Security)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Wor...