---
title: New MongoDB Flaw Lets Unauthenticated Attackers Read Uninitialized Memory
url: https://thehackernews.com/2025/12/new-mongodb-flaw-lets-unauthenticated.html
source: The Hacker News
date: 2025-12-27
fetch_date: 2025-12-28T03:35:13.327146
---

# New MongoDB Flaw Lets Unauthenticated Attackers Read Uninitialized Memory

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [New MongoDB Flaw Lets Unauthenticated Attackers Read Uninitialized Memory](https://thehackernews.com/2025/12/new-mongodb-flaw-lets-unauthenticated.html)

**Dec 27, 2025**Ravie LakshmananDatabase Security / Vulnerability

[![MongoDB Flaw](data:image/png;base64... "MongoDB Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyT_32t0dBjwnGTamsqSrB1jdPxZFMFb_GMzemmxXBm3HbtqrnJNx4VqVUF8tMKdHStEwTAU-PLcOHDKsbHvF9SSVig_OGEnWFKl81BORRb5h34UUFitJuYJOF-Trvrq-nFm5m-AzFe_dQRWYJgCOTJvzVnSzXCRgEAshv0EHR35OKUxGHr3qYg-M1vQHV/s790-rw-e365/mongodb.jpg)

A high-severity security flaw has been disclosed in MongoDB that could allow unauthenticated users to read uninitialized heap memory.

The vulnerability, tracked as **CVE-2025-14847** (CVSS score: 8.7), has been described as a case of [improper handling of length parameter inconsistency](https://cwe.mitre.org/data/definitions/130.html), which arises when a program fails to appropriately tackle scenarios where a length field is inconsistent with the actual length of the associated data.

"Mismatched length fields in Zlib compressed protocol headers may allow a read of uninitialized heap memory by an unauthenticated client," according to a [description](https://www.cve.org/CVERecord?id=CVE-2025-14847) of the flaw in CVE.org.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

The flaw impacts the following versions of the database -

* MongoDB 8.2.0 through 8.2.3
* MongoDB 8.0.0 through 8.0.16
* MongoDB 7.0.0 through 7.0.26
* MongoDB 6.0.0 through 6.0.26
* MongoDB 5.0.0 through 5.0.31
* MongoDB 4.4.0 through 4.4.29
* All MongoDB Server v4.2 versions
* All MongoDB Server v4.0 versions
* All MongoDB Server v3.6 versions

The issue has been addressed in MongoDB versions 8.2.3, 8.0.17, 7.0.28, 6.0.27, 5.0.32, and 4.4.30.

"An client-side exploit of the Server's zlib implementation can return uninitialized heap memory without authenticating to the server," MongoDB [said](https://jira.mongodb.org/browse/SERVER-115508). "We strongly recommend upgrading to a fixed version as soon as possible."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

If immediate update is not an option, it's recommended to [disable zlib compression](https://www.mongodb.com/docs/drivers/node/current/connect/connection-options/network-compression/) on the MongoDB Server by starting mongod or mongos with a [networkMessageCompressors](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--networkMessageCompressors) or a [net.compression.compressors](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-net.compression.compressors) option that explicitly omits zlib. The other compressor options supported by MongoDB are snappy and zstd.

"CVE-2025-14847 allows a remote, unauthenticated attacker to trigger a condition in which the MongoDB server may return uninitialized memory from its heap," OP Innovate [said](https://op-c.net/blog/mongodb-zlib-protocol-vulnerability-cve-2025-14847/). "This could result in the disclosure of sensitive in-memory data, including internal state information, pointers, or other data that may assist an attacker in further exploitation."

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

[Cloud Infrastructure](https://thehackernews.com/search/label/Cloud%20Infrastructure)[CVE](https://thehackernews.com/search/label/CVE)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[database security](https://thehackernews.com/search/label/database%20security)[encryption](https://thehackernews.com/search/label/encryption)[network security](https://thehackernews.com/search/label/network%20security)[Open Source Software](https://thehackernews.com/search/label/Open%20Source%20Software)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](data:image/svg+xml;base64... "Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats")

Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)

[![Google to Shut Down Dark Web Monitoring Tool in February 2026](data:image/svg+xml;base64... "Google to Shut Down Dark Web Monitoring Tool in February 2026")

Google to Shut Down Dark Web Monitoring Tool in February 2026](https://thehackernews.com/2025/12/google-to-shut-down-dark-web-monitoring.html)

[![React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors](data:image/svg+xml;base64... "React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors")

React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html)

[![Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass](data:image/svg+xml;base64... "Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass")

Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass](https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html)

[![Com...