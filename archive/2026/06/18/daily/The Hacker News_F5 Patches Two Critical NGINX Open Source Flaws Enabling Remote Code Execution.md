---
title: F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution
url: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
source: The Hacker News
date: 2026-06-18
fetch_date: 2026-06-19T07:09:16.769986
---

# F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html)

**Ravie Lakshmanan**Jun 18, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxYclMMaAOBe1jlW_s0S1SfdX3sPrGB9MZ7R9Hfo2ktoF9DiLqPA5ZYmFAyGmzws5eNmqopdPw7bBV7TTO8KgS2C8CJU8cgHNXw0ERAvk8sGRLYXH7M98eqxDM9c-rQTU0Hlj8ISEmSWMCnw6OqJMyhgxxLHCFPwP1JugZ3bCJow7AfTZ40kOo8XpY3WdF/s1700-e365/f5.jpg)

F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems.

The vulnerabilities are listed below -

* **[CVE-2026-42530](https://www.cve.org/CVERecord?id=CVE-2026-42530)** (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx\_http\_v3\_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is configured to use the HTTP/3 QUIC module to reopen a QPACK encoder stream by means of a specially crafted HTTP/3 session, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.
* **[CVE-2026-42055](https://www.cve.org/CVERecord?id=CVE-2026-42055)** (CVSS v4 score: 9.2) - A heap-based buffer overflow vulnerability in the ngx\_http\_proxy\_v2\_module and ngx\_http\_grpc\_module modules that could be triggered by a remote unauthenticated attacker when the proxy\_http\_version to 2 or grpc\_pass directives are used to proxy HTTP/2 traffic, the ignore\_invalid\_headers directive is set to off, and the large\_client\_header\_buffers directive size is larger than 2 MB, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Both shortcomings have been patched in the following versions -

* [CVE-2026-42530](https://my.f5.com/manage/s/article/K000161616)
  -
  + NGINX Open Source 1.31.0 - 1.31.1 (Fixed in 1.31.2)
  + NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4)
  + NGINX Gateway Fabric 1.3.0 - 1.6.2
  + NGINX Instance Manager 2.17.0 - 2.22.0
  + NGINX Ingress Controller 5.0.0 - 5.5.0
  + NGINX Ingress Controller 4.0.0 - 4.0.1
  + NGINX Ingress Controller 3.5.0 - 3.7.2
* [CVE-2026-42055](https://my.f5.com/manage/s/article/K000161584)
  -
  + NGINX Plus 37.0.0 - 37.0.1 (Fixed in 37.0.2.1)
  + NGINX Plus R33 - R36 (Fixed in R36 P6)
  + NGINX Open Source 1.31.1 (Fixed in 1.31.2)
  + NGINX Open Source 1.30.0 - 1.30.2 (Fixed in 1.30.3)
  + NGINX Instance Manager 2.17.0 - 2.22.0
  + F5 WAF for NGINX 5.9.0 - 5.13.1
  + NGINX App Protect WAF 5.2.0 - 5.8.0
  + NGINX App Protect WAF 4.10.0 - 4.16.0
  + F5 DoS for NGINX 4.9.0
  + NGINX App Protect DoS 4.3.0 - 4.7.0
  + NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4)
  + NGINX Gateway Fabric 1.3.0 - 1.6.2
  + NGINX Ingress Controller 5.0.0 - 5.5.0
  + NGINX Ingress Controller 4.0.0 - 4.0.1
  + NGINX Ingress Controller 3.5.0 - 3.7.2

As mitigations, F5 has outlined the following actions -

* CVE-2026-42530 - Disable HTTP/3
* CVE-2026-42055 - Remove the ignore\_invalid\_headers off directive from the configuration, or reduce the large\_client\_header\_buffers directive size below 2 MB

Although F5 makes no mention of the vulnerabilities being exploited in the wild, security flaws in F5 products have been repeatedly exploited by bad actors.

As recently as last month, another critical security defect in NGINX Plus and NGINX Open Source ([CVE-2026-42945](https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html), CVSS score: 9.2), also called NGINX Rift, came under [active exploitation](https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html) within days after public disclosure.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [F5 Networks](https://thehackernews.com/search/label/F5%20Networks), [HTTP/2](https://thehackernews.com/search/label/HTTP/2), [HTTP/3](https://thehackernews.com/search/label/HTTP/3), [NGINX](https://thehackernews.com/search/label/NGINX), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Server](https://thehackernews.com/search/label/Web%20Server)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now")

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html)

[![Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](data:image/svg+xml;base64... "Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models")

Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-...