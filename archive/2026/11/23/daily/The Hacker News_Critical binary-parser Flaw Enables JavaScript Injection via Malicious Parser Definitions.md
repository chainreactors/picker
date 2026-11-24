---
title: Critical binary-parser Flaw Enables JavaScript Injection via Malicious Parser Definitions
url: https://thehackernews.com/2026/11/critical-binary-parser-flaw-enables.html
source: The Hacker News
date: 2026-11-23
fetch_date: 2026-11-24T11:49:19.719042
---

# Critical binary-parser Flaw Enables JavaScript Injection via Malicious Parser Definitions

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

# [Critical binary-parser Flaw Enables JavaScript Injection via Malicious Parser Definitions](https://thehackernews.com/2026/11/critical-binary-parser-flaw-enables.html)

**Ravie Lakshmanan**Nov 23, 2026Vulnerability / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ_LYD1NyoPDf8MFXggODpgd2hvazxjShSZltgrLUVic7V-ZIQSjXIzFrkUx0FNoUjlxlIYocEd1AZwGx66uqGWEUyd1TMSlDmxUu8M_r6jdYkmWDZjbszL2WsK7LJzrwI-NgsI7EaLe9WkLwNLGKj8ww3tTOY4X4JPug3RWQqoypUiEpZjVXgBhhcLuZG/s1700-nu-rw-lo-l85-e365/js-cve.jpg)

A critical security flaw has been disclosed in the popular [binary-parser](https://www.npmjs.com/package/binary-parser) library that could allow an attacker who controls parser definitions to execute arbitrary code.

The vulnerability, tracked as **CVE-2026-134814** (CVSS score: 9.2 / 8.1), is a case of code injection impacting binary-parser versions prior to 2.3.1.

"Binary-parser before 2.3.1 contains a code injection vulnerability that allows attackers controlling parser definitions to inject JavaScript through string-typed options passed unvalidated by Context.generateOption()," according to a [description](https://nvd.nist.gov/vuln/detail/cve-2026-134814) of the flaw in the NIST National Vulnerability Database (NVD).

"Attackers can supply crafted length, lengthInBytes, key, tag, offset, or namely() alias values to execute arbitrary JavaScript in the Node.js process when the parser is compiled."

According to an advisory released by the project maintainer on November 11, 2026, the problem arose from the fact that some user-controlled string options were inserted directly into the generated JavaScript code without adequate validation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The parser options include -

* length
* lengthInBytes
* key
* tag
* offset, and
* the alias passed to namely()

"Parsing untrusted binary data with a trusted parser definition is not affected," Keichi Takahashi, who maintains the library, [said](https://github.com/keichi/binary-parser/security/advisories/GHSA-xmxc-6c22-m377). "These options are now validated as identifier paths (e.g. foo, $parent.len). Expressions such as 'len - 1' are rejected; use a function instead."

CVE-2026-134814 can also be viewed as an incomplete fix for [CVE-2026-1245](https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html) (CVSS score: 6.5), another code injection vulnerability that was fixed back in January 2026 and resulted from insufficient validation of field names and encoding parameters.

"[The flaw] allows attackers controlling parser definitions to inject and execute arbitrary JavaScript within the host Node.js process upon parser compilation," Upwind Security [said](https://x.com/UpwindMDR/status/2124765459371237532) in an X post. Users are advised to update to the latest version of the library for optimal protection.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Code Injection](https://thehackernews.com/search/label/Code%20Injection), [JavaScript](https://thehackernews.com/search/label/JavaScript), [node.js](https://thehackernews.com/search/label/node.js), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands + 17 More Stories](https://thehackernews.com/2026/11/threatsday-gpt-62-jailbreak-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution](https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication](https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html)

[![The Hacker News](data:image/svg+xml;base64...)

Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Control of Sites](https://thehackernews.com/2026/11/drupal-patches-critical-installe...