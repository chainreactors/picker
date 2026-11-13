---
title: Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass
url: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:44.998062
---

# Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html)

**Ravie Lakshmanan**Nov 12, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDDv_B4B-cVtvwKyLiGQsL804yGC7_xHF7y3yD5_C284fRXBVRAn5Ashy2apgJr-jaoBHRa3ujgXv1jskM53EvP_pFt41CTazYqFT-tQdcukNBeOTzVIpZXVDsdgtup4MJOEdNNZP9SP0FAdIpG1Cnfgo0YgBXzmI_boLV4qSAsVrmYn5wA3GxnPuj21JO/s1700-nu-rw-lo-l85-e365/citrix.jpg)

Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass.

The [critical vulnerabilities](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305) that impact NetScaler ADC and NetScaler Gateway are listed below -

* **CVE-2026-120868** (CVSS score: 9.3) - A memory overflow vulnerability in Packet Processing can lead to unpredictable or erroneous behavior or DoS. (All NetScaler ADC and NetScaler Gateway deployments)
* **CVE-2026-107407** (CVSS score: 9.3) - A memory overflow vulnerability in SMPP traffic can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured with a Load Balancing or Content Switching virtual server of type SMPP)
* **CVE-2026-107408** (CVSS score: 9.3) - A memory corruption vulnerability in DNS / DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured for DNS load balancing and recursive DNS resolution)
* **CVE-2026-107409** (CVSS score: 9.3) - A memory corruption vulnerability in DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured with DNS Load Balancing over HTTPS)
* **CVE-2026-107410** (CVSS score: 9.3) - A memory overflow in NetScaler Push can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as Load Balancing virtual server of type PUSH)
* **CVE-2026-107412** (CVSS score: 9.5) - Multiple memory overflow vulnerabilities can lead to unpredictable or erroneous behavior and DoS. (NetScaler configured as a Gateway or an AAA virtual server)
* **CVE-2026-107415** (CVSS score: 9.3) - A memory overflow vulnerability in Email OTP authentication can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC or NetScaler Gateway configured with an Email Action)
* **CVE-2026-111344** (CVSS score: 9.3) - A memory overflow vulnerability in Endpoint Analysis (EPA/EPAS) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a VPN virtual server or an authentication (AAA) virtual server with Endpoint Analysis)
* **CVE-2026-120864** (CVSS score: 9.3) - A memory overflow vulnerability in ICA proxy can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a Gateway VPN virtual server, an AAA virtual server, or a CR virtual server of type HDX)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

All the issues have been patched in the following versions -

* Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.57 and later releases
* Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.39 and later releases of 13.1
* Citrix NetScaler ADC 14.1-FIPS 14.1-73.58 FIPS and later releases of 14.1-FIPS
* Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1-37.293 and later releases of 13.1-FIPS and 13.1-NDcPP

Also addressed by Citrix are a number of flaws in NetScaler Console and Secure Access Client for Windows and Linux -

* **[CVE-2026-120869](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697320)** (CVSS score: 9.4) - An improper authentication vulnerability in NetScaler Console can allow an unauthenticated attacker to bypass authentication controls to access restricted resources on the appliance. (Fixed in NetScaler Console 14.1-74.34 and later)
* **[CVE-2026-118268](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697280)** (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Windows can allow a low-privileged user to escalate privileges to SYSTEM. (Fixed in Secure Access Client for Windows 26.11.1.6 and later)
* **[CVE-2026-118269](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697281)** (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Linux can allow a low-privileged user to gain root privileges. (Fixed in Secure Access Client for Linux 26.10.4 and later)

The security updates, Citrix said, follow a deeper review of its codebase by integrating artificial intelligence (AI)-assisted code analysis to detect and resolve vulnerabilities with an aim to harden the products before potential threats could materialize.

The company [said](https://community.citrix.com/techzone-blogs/110_security-updates/security-updates-for-netscaler-adc-netscaler-gateway-and-netscaler-console/) it's not aware of any exploits for any of the announced vulnerabilities, but urged customers to apply the updates as they are designed to "enhance the security posture of NetScaler."

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
[![Facebook Messe...