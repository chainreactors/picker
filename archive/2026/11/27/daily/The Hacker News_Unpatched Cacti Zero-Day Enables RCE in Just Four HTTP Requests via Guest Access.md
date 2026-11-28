---
title: Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access
url: https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html
source: The Hacker News
date: 2026-11-27
fetch_date: 2026-11-28T09:42:57.435861
---

# Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html)

**Ravie Lakshmanan**Nov 27, 2026Zero-Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy4kFFGLYGbyvO7M_M1gKBjBUm5TF_eT6dIHtCmXKz_cGyC6orRw9XupBLbcQlJTQEEqjZ3q73Cv_Sn9ncPKxOJYU8Poi8Q54-bWKIro4Sp4JYi9hjUjYy71OR1LOV6B5nX8dHK0jYSRJ1p4O1pdMWomZGhCiTKE7MkvrC-gfeINrM-GOab64Bw_MzxA6Z/s1700-nu-rw-lo-l85-e365/cacti.png)

Details have emerged about a new zero-day vulnerability in **Cacti**, an open-source network monitoring tool, that could be exploited to achieve remote code execution.

The proof-of-concept (PoC) exploit, which has yet to be assigned a CVE identifier, has been tracked as **4HTTP2SHELL** and **4HTTP2ROOT**.

"I found a path from a fresh, unauthenticated HTTP session to command execution as the Cacti server user in four requests," a security researcher who goes by the online alias "ek0ms savi0r" [said](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell). "No login. No valid API key. No phishing. Just four HTTP requests against the default guest surface."

The shortcoming affects Cacti Core 1.2.31, the [latest version](https://github.com/Cacti/cacti/releases), when the guest account is enabled. It's worth noting that the [guest account is disabled by default](https://docs.cacti.net/User-Management.md) starting with Cacti version 0.8.7.

At a high level, the vulnerability allows an attacker to abuse the guest access to write an unvalidated value (i.e., non-numeric text) into a setting called "preview\_graphs\_per\_page" via "auth\_profile.php?action=update\_data." The configuration parameter controls how many graphs are displayed per page when viewing graphs in Preview Mode.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The crafted value takes the form of arbitrary SQL strings that can be turned into a [second-order SQL injection](https://portswigger.net/kb/issues/00100210_sql-injection-second-order) by taking advantage of the fact that Cacti does not validate that the user-provided input is actually an integer value. This, in turn, opens the door for arbitrary SQL query execution when the graph preview page ("graph\_view.php") is loaded with default filters.

The SQL query demonstrated by "ek0ms savi0r" is an UPDATE statement to modify a record in Cacti's [poller table](https://github.com/Cacti/cacti/blob/develop/cacti.sql). In the final stage of the attack, the [realtime poller](https://github.com/Cacti/documentation/blob/develop/Settings-Poller.md) endpoint ("graph\_realtime.php") is invoked from the same guest session, which causes the modified row from the poller table to be read and passed as input to PHP's [popen() function](https://www.php.net/manual/en/function.popen.php) without any allowlist or sanitization checks.

The researcher has pointed out four failures that ultimately make it possible to achieve unauthenticated remote code execution -

* The guest can write a numeric setting as an arbitrary string
* The stored default bypasses request validation
* Cacti's PHP PDO database driver accepts stacked statements through the SQL LIMIT clause
* The poller executes a database-stored command string

Successful exploitation of the flaw can allow an attacker to compromise the Cacti server and provide a pivot point to the target network as it exposes sensitive data, or even suppress alerts by modifying the poller table.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Because Cacti often stores credentials and connection details for routers, switches, servers, and other devices across a network, an attacker who reaches this level of command execution can gain a foothold reaching far beyond the monitoring server itself," watchTowr [said](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/) in an advisory.

In the absence of a fix, users are advised to disable the guest account and restrict access to the Cacti web interface to mitigate potential risks. It's also essential to review poller configuration entries for unexpected command values and apply the fixes as soon as they become available.

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

[network security](https://thehackernews.com/search/label/network%20security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [Zero-Day](https://thehackernews.com/search/label/Zero-Day)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://theha...