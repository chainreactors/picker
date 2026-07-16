---
title: Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws
url: https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html
source: The Hacker News
date: 2026-07-15
fetch_date: 2026-07-16T04:58:59.504266
---

# Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws](https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html)

**Ravie Lakshmanan**Jul 15, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMjCjGBZhkRcB4m5BQu0Fcn-Qjs1_VPnfOlt3oFxu7CKMZ5Wc1JpvZEvhVSorBJW-AWV1pACLDkg4rFmCCcdH6vDk-pmD5ai0ZewlmPyeWPnfsmTcg-D3UJXdT902oUD32DjSm5CrBsnf2rcVTQPUo5o-LJRKUlsjOwPNfYMpN7kOfmNhnyw552cv-Gtqk/s1700-e365/adobes.jpg)

Mozilla has [released](https://www.mozilla.org/en-US/security/advisories/mfsa2026-67/) updates to address two critical flaws in Firefox for which it warned that exploit code has been published.

The vulnerabilities are listed below -

* **CVE-2026-15718**, an invalid pointer in the JavaScript: WebAssembly component
* **CVE-2026-15719**, a site isolation in the DOM: Navigation component

"We are aware that exploit code for this is public, however we are not aware of any attacks in the wild abusing this flaw," Mozilla said in an advisory. Both vulnerabilities have been addressed in Firefox version 152.0.6.

The release comes as Google [shipped](https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_0353146366.html) fixes for 15 security flaws, including two critical use-after-free bugs in [Ozone](https://chromium.googlesource.com/chromium/src/%2B/main/docs/ozone_overview.md) ([CVE-2026-15764](https://nvd.nist.gov/vuln/detail/CVE-2026-15764) and [CVE-2026-15765](https://nvd.nist.gov/vuln/detail/CVE-2026-15765)), a cross-platform abstraction layer that allows the browser to interact natively with various display servers and windowing systems. It supports Linux, ChromeOS, and Fuchsia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"Use after free in Ozone in Google Chrome on Linux prior to 150.0.7871.125 allowed a remote attacker who convinced a user to engage in specific UI gestures to potentially exploit heap corruption via a crafted HTML page," according to a description of CVE-2026-15764 in the NIST National Vulnerability Database (NVD).

The shortcomings have been patched in Chrome version 150.0.7871.124/.125 for Windows and Mac and 150.0.7871.124 for Linux.

In a related development, Adobe has published security updates for 88 vulnerabilities, including multiple critical-severity bugs in ColdFusion, Commerce, Experience Manager, and Illustrator. Of these, eight impact [Adobe ColdFusion](https://helpx.adobe.com/in/security/products/coldfusion/apsb26-82.html) -

* **CVE-2026-48318** (CVSS score: 9.9) - A path traversal vulnerability that could lead to arbitrary code execution
* **CVE-2026-48322** (CVSS score: 9.6) - A code injection vulnerability that could lead to arbitrary code execution
* **CVE-2026-48284** (CVSS score: 9.6) - An improper input validation vulnerability that could lead to arbitrary code execution
* **CVE-2026-48321** (CVSS score: 9.3) - An incorrect authorization vulnerability that could lead to privilege escalation
* **CVE-2026-48325** (CVSS score: 9.3) - A missing authentication for a critical function vulnerability that could lead to arbitrary code execution
* **CVE-2026-48319** (CVSS score: 9.1) - A path traversal vulnerability that could lead to arbitrary code execution
* **CVE-2026-48324** (CVSS score: 9.1) - An SQL injection vulnerability that could lead to arbitrary code execution
* **CVE-2026-48327** (CVSS score: 9.0) - An incorrect authorization vulnerability that could lead to arbitrary code execution

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The CodeFusion flaws have been remediated in versions ColdFusion 2025 Update 11 and ColdFusion 2023 Update 22. Also fixed by Adobe are two critical flaws each in [Adobe Commerce and Magento Open Source](https://helpx.adobe.com/in/security/products/magento/apsb26-73.html) and [Adobe Experience Manager](https://helpx.adobe.com/in/security/products/experience-manager/apsb26-74.html) -

* **CVE-2026-48356** (CVSS score: 9.6) - A file upload vulnerability in Adobe Commerce and Magento Open Source that could lead to privilege escalation
* **CVE-2026-48358** (CVSS score: 9.1) - An improper encoding or escaping of output vulnerability in Adobe Commerce and Magento Open Source that could lead to arbitrary code execution
* **CVE-2026-48259** (CVSS score: 9.6) - A server-side request forgery vulnerability in Adobe Experience Manager that could lead to arbitrary code execution
* **CVE-2026-48359** (CVSS score: 9.6) - An improper restriction of XML external entity reference vulnerability in Adobe Experience Manager that could lead to arbitrary code execution

Elsewhere, Broadcom has [released](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/37926) a fix for a critical authentication bypass vulnerability in VMware Avi Load Balancer (**CVE-2026-47865**, CVSS score: 9.8) that a malicious user with network access can exploit to access the Avi Control plane. Filip Waeytens of the NATO Cyber Security Centre (NCSC) has been credited with discovering and reporting the flaw.

Although none of the vulnerabilities have been marked as actively exploited, it's essential that organizations install the latest updates, given that threat actors are known to weaponize flaws in these products in attacks.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post....