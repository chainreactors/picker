---
title: Citrix Patches Critical NetScaler Flaw That Could Enable RCE in SAML Deployments
url: https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html
source: The Hacker News
date: 2026-10-09
fetch_date: 2026-10-10T07:58:22.823590
---

# Citrix Patches Critical NetScaler Flaw That Could Enable RCE in SAML Deployments

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

# [Citrix Patches Critical NetScaler Flaw That Could Enable RCE in SAML Deployments](https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html)

**Ravie Lakshmanan**Oct 09, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifRR7IQ4Ngqm8ANJ-DKwW60qeemJlrfrtvhaAwtpzW37_jAkbdctxJEqjw8k_m1KT32ryqoxa1dNYoEPG-E9xNwrbtXqbOjbzmgs3JM9RW68FZMNA8ky14QKTLpEfHop9A4xmXO46fxQaeXZMZzzMQ-qoIXLpMrr8Gbekn3cgNX5xc7bYvMRDYKjDeLf4o/s1700-nu-rw-lo-l85-e365/cit.jpg)

Citrix has [released patches](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697191) for yet another critical security flaw impacting NetScaler ADC and NetScaler Gateway that could result in remote code execution or denial-of-service (DoS) under certain conditions.

"**CVE-2026-107406** is a memory overflow vulnerability that may lead to remote code execution or denial-of-service under specific configuration conditions," Citrix said.

The vulnerability carries a CVSS score of 9.5 out of 10.0. There is no evidence that the issue has been exploited in the wild. Citrix has credited Michael Tucker, Chew Keong Tan, and Alex Bernier of the JPMorgan Chase XOR Team, along with Maxim Suhanov, for discovering and reporting the flaw.

Successful exploitation hinges on the NetScaler deployments being configured as a SAML identity provider (IdP) or service provider (SP). Customers can determine if their instances meet the criteria by checking the configuration for entries like below -

* SAML SP: add authentication samlAction
* SAML IdP: add authentication samlIdPProfile

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The issue impacts the following versions -

* When configured as a SAML IdP -
  + NetScaler ADC and NetScaler Gateway between 14.1-73.37 and 14.1-73.41, inclusive
  + NetScaler ADC 14.1-FIPS between 14.1-73.37 FIPS and 14.1-73.41 FIPS, inclusive
  + NetScaler ADC and NetScaler Gateway between 13.1-64.23 and 13.1-64.28, inclusive
  + NetScaler ADC 13.1-FIPS between 13.1-NDcPP 13.1-37.279 and 13.1- 37.282, inclusive
* When configured as a SAML SP or SAML IdP:
  + NetScaler ADC and NetScaler Gateway before 14.1-73.37
  + NetScaler ADC 14.1-FIPS before 14.1-73.37 FIPS
  + NetScaler ADC and NetScaler Gateway before 13.1-64.23
  + NetScaler ADC 13.1-FIPS before 13.1-NDcPP 13.1-37.279

"Secure Private Access Hybrid deployments using NetScaler instances are also affected by the vulnerability," Citrix [warned](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-customers-immediate-guidance-for-cve-2026-107406-in-netscaler-adc-and-netscaler-gateway-r1631/). "Customers need to upgrade these NetScaler instances to the recommended NetScaler versions to address the vulnerability."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The shortcoming has been [addressed](https://support.citrix.com/external/article/CTX697191/citrix-netscaler-adc-and-citrix-netscale.html) in the versions below -

* Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.46 and later releases
* Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.29 and later releases of 13.1
* Citrix NetScaler ADC 14.1-FIPS 14.1-73.46 FIPS and later releases of 14.1-FIPS
* Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.283 and later releases of 13.1-FIPS and 13.1-NDcPP

The development comes as three different flaws in NetScaler ADC and NetScaler Gateway appliances ([CVE 2026-88771](https://thehackernews.com/2026/10/citrix-netscaler-post-exploitation.html), [CVE 2026-88772](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html), and [CVE 2026-88779](https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html)) have come under active exploitation in the wild.

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

[Identity Security](https://thehackernews.com/search/label/Identity%20Security), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats](https://thehackernews.com/2026/09/weekly-recap-387m-crypto-hack-citrix.html)

[![The Hacker News](data:image/svg+xml;base64...)

Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

[![The Hacker News](data:image/svg+xml;base64...)

RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)

[![The Hacker News](data:image/svg+xml;base64...)

Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Shelves GPT-6.1 Astra After Tests Find Deception and Unaut...