---
title: Fenix Cybercrime Group Poses as Tax Authorities to Target Latin American Users
url: https://thehackernews.com/2023/07/fenix-cybercrime-group-poses-as-tax.html
source: The Hacker News
date: 2023-07-27
fetch_date: 2025-10-04T11:57:01.409677
---

# Fenix Cybercrime Group Poses as Tax Authorities to Target Latin American Users

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Fenix Cybercrime Group Poses as Tax Authorities to Target Latin American Users](https://thehackernews.com/2023/07/fenix-cybercrime-group-poses-as-tax.html)

**Jul 26, 2023**Ravie LakshmananOnline Security / Malware

[![Fenix Cybercrime Group](data:image/png;base64... "Fenix Cybercrime Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEja-Sd0qyQm16LrK5Qhlp4X6o_758jm__c-QOFOD92XV-kkVmGojYrAeMABIjXSDz8Etez-8fnzjXrSl-KTNEQNYHzxr2iLbG30ymE3o3JFgMBEyC40fscxwgXS_mVRIRlGkXM4pldNlfscB-S_eUUWF16SdCFhSuTITgh2Jr0jSd5PvhGDYCWXcD14IDhd/s790-rw-e365/tax.jpg)

Tax-paying individuals in Mexico and Chile have been targeted by a Mexico-based cybercrime group that goes by the name **Fenix** to breach targeted networks and steal valuable data.

A key hallmark of the operation entails cloning official portals of the Servicio de Administración Tributaria (SAT) in Mexico and the Servicio de Impuestos Internos (SII) in Chile and redirecting potential victims to those sites.

"These fake websites prompt users to download a supposed security tool, claiming it will enhance their portal navigation safety," Metabase Q security researchers Gerardo Corona and Julio Vidal [said](https://www.metabaseq.com/fenix-botnet/) in a recent analysis.

"However, unbeknownst to the victims, this download actually installs the initial stage of malware, ultimately enabling the theft of sensitive information such as credentials."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The goal of Fenix, according to the Latin America-focused cybersecurity firm, is to act as an initial access broker and get a foothold into different companies in the region, and sell the access to ransomware affiliates for further monetization.

Evidence gathered so far points to the threat actor orchestrating phishing campaigns coinciding with government activities during the year since at least the fourth quarter of 2022.

[![Fenix Cybercrime Group](data:image/png;base64... "Fenix Cybercrime Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLnVLRyLmBx-I2bMyEM7wTWXTcVT3-x2ojv2jXWH3gmJ_NEzYGzeli2tvWMRHyOO1J3s_D_mlCVGTBTT9N9__FkzHRXcDsrR-fDRyaQb9ZrP6KE_RmsotbwP3uUK1m29oQrKtJYbDrXagZpOnrltnfyWUFUDnyEIt2IIS_xQdF_XCmgvDaeVaPsseCOvv9/s790-rw-e365/malware.jpg)

The mechanics of the campaign proceeds thus: Visitors landing on the impersonated websites are urged to download software that supposedly safeguards their data while browsing the portal. Alternatively, users are lured via phishing sites set up to download legitimate apps like AnyDesk.

"[Fenix] compromises weak websites using vulnerable WordPress engines and also creates new domains to launch phishing campaigns," the researchers said, adding the group "creates typosquatting domains similar to known apps like AnyDesk, WhatsApp, etc."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

But in reality, the ZIP file containing the purported software is used as a springboard to activate an infection sequence that leads to the execution of an obfuscated PowerShell script, which, in turn, loads and runs a .NET binary, after which the message "Ahora se encuentra protegido" (meaning "Now you are protected" in Spanish) is displayed to keep up the ruse.

The .NET executable subsequently paves the way for establishing persistence on the compromised host and deploying a botnet malware that's capable of running commands received from a remote server, loading a stealer module that exfiltrates credentials stored in web browsers and crypto wallets, and ultimately deleting itself.

"We are seeing new malicious groups being created in LATAM to provide initial access to ransomware gangs," the researchers concluded. "These local actors are not amateur and will increase their technical expertise and therefore more difficult to track, detect and eradicate, it is important to anticipate their actions."

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

[Cyber Crime](https://thehackernews.com/search/label/Cyber%20Crime)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Mexican Hacker](https://thehackernews.com/search/label/Mexican%20Hacker)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2...