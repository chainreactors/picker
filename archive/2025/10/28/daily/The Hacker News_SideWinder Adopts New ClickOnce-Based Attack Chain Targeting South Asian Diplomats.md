---
title: SideWinder Adopts New ClickOnce-Based Attack Chain Targeting South Asian Diplomats
url: https://thehackernews.com/2025/10/sidewinder-adopts-new-clickonce-based.html
source: The Hacker News
date: 2025-10-28
fetch_date: 2025-10-29T03:16:27.351316
---

# SideWinder Adopts New ClickOnce-Based Attack Chain Targeting South Asian Diplomats

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

# [SideWinder Adopts New ClickOnce-Based Attack Chain Targeting South Asian Diplomats](https://thehackernews.com/2025/10/sidewinder-adopts-new-clickonce-based.html)

**Oct 28, 2025**Ravie LakshmananCyber Espionage / Malware

[![ClickOnce-Based Attack Chain](data:image/png;base64... "ClickOnce-Based Attack Chain")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhC3hjuQYF6NrQ5JvlPhwaBdmr4TLCJkOaKfH3-D0_WE_ibmXtG76evHlGv9MN6nAKXgUnRmfkfBILBE5PKFOc4-dH-KVGVA4p_ubK73bo2u6Tbr2M_qZ8VI2xW3q_UBQZ_nanyTEprtqryK4EwtqdzuwWwPhhHyyFKkI9RImjIjCIl8Wg_kBN5GPddporW/s790-rw-e365/cyberattack-paki.jpg)

A European embassy located in the Indian capital of New Delhi, as well as multiple organizations in Sri Lanka, Pakistan, and Bangladesh, have emerged as the target of a new campaign orchestrated by a threat actor known as **SideWinder** in September 2025.

The activity "reveals a notable evolution in SideWinder's TTPs, particularly the adoption of a novel PDF and [ClickOnce](https://thehackernews.com/2025/06/oneclik-malware-targets-energy-sector.html)-based infection chain, in addition to their previously documented Microsoft Word exploit vectors," Trellix researchers Ernesto Fernández Provecho and Pham Duy Phuc [said](https://www.trellix.com/blogs/research/sidewinders-shifting-sands-click-once-for-espionage/) in a report published last week.

The attacks, which involved sending spear-phishing emails in four waves from March through September 2025, are designed to drop malware families such as ModuleInstaller and StealerBot to gather sensitive information from compromised hosts.

While ModuleInstaller serves as a downloader for next-stage payloads, including StealerBot, the latter is a .NET implant that can launch a reverse shell, deliver additional malware, and collect a wide range of data from compromised hosts, including screenshots, keystrokes, passwords, and files.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It should be noted that both ModuleInstaller and StealerBot were first [publicly documented](https://thehackernews.com/2024/10/sidewinder-apt-strikes-middle-east-and.html) by Kaspersky in October 2024 as part of attacks mounted by the hacking group targeting high-profile entities and strategic infrastructures in the Middle East and Africa.

As recently as May 2025, Acronis [revealed](https://thehackernews.com/2025/05/south-asian-ministries-hit-by.html) SideWinder's attacks aimed at government institutions in Sri Lanka, Bangladesh, and Pakistan using malware-laden documents susceptible to known Microsoft Office flaws to launch a multi-stage attack chain and ultimately deliver StealerBot.

The latest set of attacks, observed by Trellix post September 1, 2025, and targeting Indian embassies, entails the use of Microsoft Word and PDF documents in phishing emails with titles such as "Inter-ministerial meeting Credentials.pdf" or "India-Pakistan Conflict -Strategic and Tactical Analysis of the May 2025.docx." The messages are sent from the domain "mod.gov.bd.pk-mail[.]org" in an attempt to mimic the Ministry of Defense of Pakistan.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl3cgdOXfskkE9Z69SXMiOf4rDuzKZKW2nAIqev2BWTSzVsrbCgOpwCD9uQpdebGIVkH35yJ522UjOv0x2iFvkdf_bkW-HSZMnEw966KOPuMUSki7anI3yDvZqOJ_PA2GGXelP6vYMiEAMNkPLJ1RLJqubsM0j8sV6eJ1CPJgyxpGpYJPrtGL_d1Eh8Gpn/s790-rw-e365/attack.jpg)

"The initial infection vector is always the same: a PDF file that cannot be properly seen by the victim or a Word document that contains some exploit," Trellix said. "The PDF files contain a button that urges the victim to download and install the latest version of Adobe Reader to view the document's content."

Doing so, however, triggers the download of a ClickOnce application from a remote server ("mofa-gov-bd.filenest[.]live"), which, when launched, sideloads a malicious DLL ("DEVOBJ.dll"), while simultaneously launching a decoy PDF document to the victims.

The ClickOnce application is a legitimate executable from MagTek Inc. ("ReaderConfiguration.exe") that masquerades as Adobe Reader and is signed with a valid signature to avoid raising any red flags. Furthermore, requests to the command-and-control (C2) server are region-locked to South Asia and the path to download the payload is dynamically generated, complicating analysis efforts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The rogue DLL, for its part, is designed to decrypt and launch a .NET loader named ModuleInstaller, which then proceeds to profile the infected system and deliver the StealerBot malware.

The findings indicate an ongoing effort on the part of the persistent threat actors to refine their modus operandi and circumvent security defenses to accomplish their goals.

"The multi-wave phishing campaigns demonstrate the group's adaptability in crafting highly specific lures for various diplomatic targets, indicating a sophisticated understanding of geopolitical contexts," Trellix said. "The consistent use of custom malware, such as ModuleInstaller and StealerBot, coupled with the clever exploitation of legitimate applications for side-loading, underscores SideWinder's commitment to sophisticated evasion techniques and espionage objectives."

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
[**Share on Whats...