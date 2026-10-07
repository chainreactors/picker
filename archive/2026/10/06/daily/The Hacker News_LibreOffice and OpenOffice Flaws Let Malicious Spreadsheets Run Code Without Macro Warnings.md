---
title: LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without Macro Warnings
url: https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.167294
---

# LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without Macro Warnings

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without Macro Warnings](https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html)

**Swati Khandelwal**Oct 06, 2026Vulnerability / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYVdFxWk-OP9_vpIdzp0S9ffqMNnyAMbRWKklSryVockcistDlpX5ZcfLGluaqpHqdsu_DoOaFq2J1z5jTVNatxS8aoQjMNS1PoEYOAZrj1V1Spdk67LUZgSlSPlqeEULSVSbHZfkCimWV56E2HKs_IUNrJaYFrPPq0YaXS2sEMBVZNJM0f2ydfUMFREw/s1700-nu-rw-lo-l85-e365/office-sheet.jpg)

A malicious spreadsheet can make LibreOffice and Apache OpenOffice run an attacker's code as soon as the file is opened, security researchers have shown. There is no warning first, of the kind either program shows before it runs a macro.

The attack works only when the program's Java support is enabled. So far, it has only been shown as a proof of concept, and there are no reports of its use in real attacks.

LibreOffice has already [fixed the flaw](https://www.libreoffice.org/security/), which it tracks as CVE-2026-63277, in updates released on October 5. It recommends that users move to version 26.2.5 or 26.8.0. Versions before those are affected.

Apache OpenOffice has not fixed the matching flaw, which it tracks as CVE-2026-59265. Every version up to and including its current release, 4.1.16, is affected, and the project [says a fix is expected](https://www.openwall.com/lists/oss-security/2026/10/02/2) in version 4.1.17, which is still being tested.

Until then, Apache OpenOffice users can block the attack by turning off Java in the program's settings, or by not opening spreadsheets they do not trust.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The attack combines features that each work as intended on their own. A LibreOffice or Apache OpenOffice Calc spreadsheet can hold a "database range", a block of cells that pulls in data from an outside source and refreshes it by itself. That outside source can be a separate database file, called an ODB, named by a web address written into the spreadsheet.

When the spreadsheet is opened, the range refreshes and the program downloads the ODB from that web address. The ODB can name a Java database driver, known as a JDBC driver, and point to where the driver's code lives, which can be a JAR file, a bundle of Java code, or on a remote server. The program then downloads the JAR and starts the driver, which is the attacker's code, inside the program itself.

Each of these is a normal feature. The security problem, the researchers say, is that together they reach code execution without ever asking the user to trust the document, the way the program asks before it runs a macro.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-0eh8Cw5AO6m8AnzlSX8tXcBC6dVeeW55WsOCxC2FAqX9KmjpJk0xKG7-a_fVv8W2AWerfaWKl2TonKW-lUcEB1vnJMTamGb-_gdDszAzxvCDdAU_YqjVSeKp1nyf7N5Uk8GJBOm4Aoifl8AtB7sID9iB7pzV5v1FLbsRl40VXPgqfW030Dg9wDzBtv0/s1700-nu-rw-lo-l85-e365/office.gif)

In the [proof of concept](https://github.com/v12-security/pocs/tree/main/office_jdbc_bugs), the driver simply opens the Calculator app, a harmless stand-in, but the same path can run any Java code the attacker chooses. The researchers tested the attack on Windows and Linux and say it is not tied to one operating system.

In their [demonstration](https://x.com/v12sec/status/2107142692853469503), the malicious files sat on the same machine for convenience. The researchers say a real attack would instead place the database file and the code on an attacker-controlled server.

The flaw in LibreOffice was reported independently by Rick de Jager of the V12 security team and by Thomas Rinsma and Edoardo Geraci of Codean Labs. Apache credits Codean Labs for the matching flaw in OpenOffice. The V12 team has published a proof of concept for both programs, and Caolán McNamara of Collabora Productivity wrote the fix for LibreOffice.

The Hacker News has contacted The Document Foundation, which develops LibreOffice, and the Apache OpenOffice project for comment.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats](https://thehackernews.com/2026/09/weekly-recap-387m-crypto-hack-citrix.html)

[![The Hacker News](data:image/svg+xml;base64...)

Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

[![The Hacker News](data:image/svg+xml;base64...)

RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)

[![The Hacker News](data:image/svg+xml;base64......