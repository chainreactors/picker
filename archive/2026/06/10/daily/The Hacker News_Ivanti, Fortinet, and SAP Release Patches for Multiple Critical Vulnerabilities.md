---
title: Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities
url: https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
source: The Hacker News
date: 2026-06-10
fetch_date: 2026-06-11T06:37:05.675894
---

# Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities

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

# [Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities](https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html)

**Ravie Lakshmanan**Jun 10, 2026Vulnerability / Patch Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs2l0GUUy91D4hHU067eYWpRzvSJGcfOkHce2jcVXZGWI9sld0hgaomhoKTc3dYEXEbz05oZQ5mFzo34eXp-wNJ2j_ofUjXjR7ZR5obszwH7bCRRmah9Q9HY3RSDrwrAf8QD162ca7nvxTRELWzcVW8AbbVMpXJfHXtaYEiSxXAw49VpCG8ep33SbGeLSF/s1700-e365/ivanti.jpg)

Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure.

The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It's tracked as **CVE-2026-25089** (CVSS score: 9.1).

"An improper neutralization of special elements used in an OS command vulnerability [CWE-78] in FortiSandbox, FortiSandbox Cloud and FortiSandbox PaaS WEB UI may allow an unauthenticated attacker to execute unauthorized commands via specifically crafted HTTP requests," Fortinet [said](https://fortiguard.fortinet.com/psirt/FG-IR-26-141).

The issue impacts the following products and versions -

* FortiSandbox 5.0.0 through 5.0.5 (Upgrade to 5.0.6 or above)
* FortiSandbox 4.4.0 through 4.4.8 (Upgrade to 4.4.9 or above)
* FortiSandbox Cloud 5.0.4 through 5.0.5 (Upgrade to 5.0.6 or above)
* FortiSandbox PaaS 5.0.4 through 5.0.5 (Upgrade to 5.0.6 or above)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

On Tuesday, Ivanti also [published](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US) fixes for two critical security flaws impacting Ivanti Sentry (formerly MobileIron Sentry) -

* **CVE-2026-10520** (CVSS score: 10.0) - An operating system command injection vulnerability before versions R10.5.2, R10.6.2, and R10.7.1 that allows a remote unauthenticated user to achieve root-level remote code execution.
* **CVE-2026-10523** (CVSS score: 9.9) - An authentication bypass vulnerability before versions R10.5.2, R10.6.2, and R10.7.1 that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access.

watchTowr Labs, which published additional details of CVE-2026-10520, said an attacker could exploit the vulnerability by issuing a specially crafted HTTP request to the "/mics/api/v2/sentry/mics-config/handleMessage" endpoint, which is then interpreted as a MICS configuration command and executed by a backend component named "handleExecute()."

The patch shipped by Ivanti incorporates additional controls that block access to the vulnerable endpoint, causing unauthenticated requests to be redirected to the login page.

"Ivanti did not just remove attacker control over the vulnerable execution path," security researcher Sonny Macdonald [said](https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/). "They also added a layer of protection in front of it to make reaching the endpoint significantly more difficult. In other words: they added authentication."

Rounding off the list of updates is SAP, which [pushed out fixes](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/june-2026.html) for four critical vulnerabilities in NetWeaver AS ABAP and ABAP Platform, as well as SAP Commerce Cloud and SAP Data Hub -

* **CVE-2026-44748** (CVSS score: 9.9) - XML signature wrapping vulnerability in SAML authentication in SAP NetWeaver AS ABAP and ABAP Platform
* **CVE-2026-27671** (CVSS score: 9.8) - Memory corruption vulnerability in Application Server ABAP of SAP NetWeaver and ABAP Platform
* **CVE-2026-22732** (CVSS score: 9.1) - Potential Spring security vulnerability within SAP Commerce Cloud and SAP Data Hub
* **CVE-2026-40128** (CVSS score: 9.0) - Directory traversal vulnerability in SAP NetWeaver Application Server Java (Web Container)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"The application allows an authenticated attacker with normal privileges to obtain a valid signed message and send modified signed XML documents with tampered identity information to the verifier," SAP security company Onapsis [said](https://onapsis.com/blog/sap-security-patch-day-june-2026/).

"Due to an improper XML signature verification, the manipulated identity information is accepted, leading to unauthorized access to sensitive user data and potential disruption of normal system usage."

As for CVE-2026-27671, the defect allows an unauthenticated attacker to send a crafted RFC request that exploits how the SAP kernel validates the RFC protocol to achieve memory corruption.

There is no evidence that any of the aforementioned flaws have been exploited in the wild. However, it's always a safe practice to update to the latest version for optimal protection.

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

[Command Inject...