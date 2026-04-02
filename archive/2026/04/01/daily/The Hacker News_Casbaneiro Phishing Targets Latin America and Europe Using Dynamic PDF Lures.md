---
title: Casbaneiro Phishing Targets Latin America and Europe Using Dynamic PDF Lures
url: https://thehackernews.com/2026/04/casbaneiro-phishing-targets-latin.html
source: The Hacker News
date: 2026-04-01
fetch_date: 2026-04-02T04:31:35.928795
---

# Casbaneiro Phishing Targets Latin America and Europe Using Dynamic PDF Lures

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Casbaneiro Phishing Targets Latin America and Europe Using Dynamic PDF Lures](https://thehackernews.com/2026/04/casbaneiro-phishing-targets-latin.html)

**Ravie Lakshmanan**Apr 01, 2026Malware / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpJd0tgZX0EzqjxkNOrJsyGRUV4N21qsJC30j2VYYargUXl2tPz_BidXWWmAG9Wfb5f683WOOle2CElerewagtzAAI8sbcJ9XrCbtgcSRtWF-itSYXH4hbTKvOIrjW9PKSgqi00rOrFCHRWzkWaWmP0qPH0vjrJ2LbbcXgl9aQv3n3tzcT45pdSPMcP54S/s1700-e365/pdf-malware.jpg)

A multi-pronged phishing campaign is targeting Spanish-speaking users in organizations across Latin America and Europe to deliver Windows banking trojans like [Casbaneiro](https://thehackernews.com/2023/07/casbaneiro-banking-malware-goes-under.html) (aka Metamorfo) via another malware called [Horabot](https://thehackernews.com/2025/05/horabot-malware-targets-6-latin.html).

The activity has been attributed to a Brazilian cybercrime threat actor tracked as [Augmented Marauder and Water Saci](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html). The e-crime group was [first documented](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html) by Trend Micro in October 2025.

"This threat group employs a wider-ranging attack model focused on a bespoke delivery and propagation mechanism that includes WhatsApp, [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) techniques, and email-centric phishing," BlueVoyant security researchers Thomas Elkins and Joshua Green [said](https://www.bluevoyant.com/blog/augmented-marauders-multi-pronged-casbaneiro-campaigns) in a technical breakdown published Tuesday.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

"It is now evident that while these Brazil-based operators heavily leverage script-based WhatsApp automation to compromise retail and consumer users in Latin America, they concurrently maintain and deploy an advanced, email-hijacking engine to penetrate enterprise perimeters there and Europe as well."

The starting point of the campaign is a phishing email that employs court summons-themed messages to deceive recipients into opening a password-protected PDF attachment. Clicking on an embedded link in the document directs the victim to a malicious link and initiates an automatic download of a ZIP archive, which, in turn, leads to the execution of interim HTML Application (HTA) and VBS payloads.

The VBS script is designed to carry out environment and anti-analysis checks similar to those found in Horabot artifacts, including checks for Avast antivirus software, and proceeds to retrieve next-stage payloads from a remote server. Among the downloaded files are AutoIt-based loaders, each of which extracts and runs encrypted payload files with ".ia" or ".at" extensions to eventually launch two malware families: Casbaneiro ("staticdata.dll") and Horabot ("at.dll").

While Casbaneiro is the primary payload, Horabot is used as a propagation mechanism for the malware. Casbaneiro's Delphi DLL module contacts a command-and-control (C2) server to fetch a PowerShell script that employs Horabot to distribute the malware via phishing emails to harvested contacts from Microsoft Outlook.

"Rather than distributing a static file or hardcoded link as seen in older Horabot campaigns, this script initiates an HTTP POST request to a remote PHP API (hxxps://tt.grupobedfs[.]com/.../gera\_pdf.php), passing a randomly generated four-digit PIN," BlueVoyant said.

"The server dynamically forges a bespoke, password-protected PDF impersonating a Spanish judicial summons, which is returned to the infected host. The script then iterates over the filtered email list, utilizing the compromised user's own email account to send a tailored phishing email with the newly generated PDF attached."

Also used in tandem is a secondary Horabot-related DLL ("at.dll") that functions as a spam and account hijacking tool targeting Yahoo, Live, and Gmail accounts to send phishing emails via Outlook. Horabot is [assessed](https://thehackernews.com/2023/06/new-botnet-malware-horabot-targets.html) to be put to use in attacks targeting Latin America since at least November 2020.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Water Saci has a history of using WhatsApp Web as a distribution vector for disseminating banking trojans like Maverick and Casbaneiro in a worm-like manner. However, recent campaigns highlighted by Kaspersky have [leveraged](https://securelist.com/horabot-campaign/119033/) the ClickFix social engineering tactic to dupe users into running malicious HTA files with the end goal of deploying Casbaneiro and the Horabot spreader.

"Taken together, the integration of ClickFix social engineering, alongside dynamic PDF generation and WhatsApp automation, demonstrates an agile adversary that is continually innovating and executing diverse attack paths to bypass modern security controls," the researchers concluded.

"This adversary is maintaining a bifurcated, multi-pronged attack infrastructure, dynamically deploying the WhatsApp-centric Maverick chain and concurrently utilizing both ClickFix and email-based Horabot attack paths."

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
[**Share on...