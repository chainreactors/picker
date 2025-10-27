---
title: Cyber Espionage Campaign Hits Russian Aerospace Sector Using EAGLET Backdoor
url: https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html
source: The Hacker News
date: 2025-07-26
fetch_date: 2025-10-07T00:05:02.387882
---

# Cyber Espionage Campaign Hits Russian Aerospace Sector Using EAGLET Backdoor

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

# [Cyber Espionage Campaign Hits Russian Aerospace Sector Using EAGLET Backdoor](https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html)

**Jul 25, 2025**Ravie LakshmananCyber Espionage / Malware

[![Cyber Espionage](data:image/png;base64... "Cyber Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIFdsp-9cbSTNjCCNdogLSst63_-7ag4wXClQ0eTg_gvQletIyTVeCwX00fK27vMQNqVTFq9UiwD73aCTVfU85_BAZSsm75dcGyD6pux2CS-Ui9_im9JuUdnru8SfhKoPzUirbYZJHdOQJRMey9b-jroo19-CBMhmNpUUfwNI_xfk-kJVF6KrhRVZ2pyPB/s790-rw-e365/defense.jpg)

Russian aerospace and defense industries have become the target of a cyber espionage campaign that delivers a backdoor called EAGLET to facilitate data exfiltration.

The activity, dubbed Operation **CargoTalon**, has been assigned to a threat cluster tracked as **UNG0901** (short for Unknown Group 901).

"The campaign is aimed at targeting employees of Voronezh Aircraft Production Association (VASO), one of the major aircraft production entities in Russia via using товарно-транспортная накладная (TTN) documents — critical to Russian logistics operations," Seqrite Labs researcher Subhajeet Singha [said](https://www.seqrite.com/blog/operation-cargotalon-ung0901-targets-russian-aerospace-defense-sector-using-eaglet-implant/) in an analysis published this week.

The attack commences with a spear-phishing email bearing cargo delivery-themed lures that contain a ZIP archive, within which is a Windows shortcut (LNK) file that uses PowerShell to display a decoy Microsoft Excel document, while also deploying the EAGLET DLL implant on the host.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The decoy document, per Seqrite, references Obltransterminal, a Russian railway container terminal operator that was [sanctioned](https://home.treasury.gov/news/press-releases/jy2117) by the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) in February 2024.

EAGLET is designed to gather system information and establish a connection to a hard-coded remote server ("185.225.17[.]104") in order to process the HTTP response from the server and extract the commands to be executed on the compromised Windows machine.

The implant supports shell access and the ability to upload/download files, although the exact nature of the next-stage payloads delivered through this method is unknown, given that the command-and-control (C2) server is currently offline.

Seqrite said it also uncovered similar campaigns targeting the Russian military sector with EAGLET, not to mention source code and targeting overlaps with another threat cluster tracked as [Head Mare](https://thehackernews.com/2025/03/kaspersky-links-head-mare-to-twelve.html) that's known to target Russian entities.

This includes the functional parallels between EAGLET and [PhantomDL](https://thehackernews.com/2024/09/hacktivists-exploits-winrar.html), a Go-based backdoor with a shell and file download/upload feature, as well as the similarities in the naming scheme used for the phishing message attachments.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as the Russian state-sponsored hacking group called [UAC-0184](https://thehackernews.com/2024/10/pro-ukrainian-hackers-strike-russian.html) (aka Hive0156) has been attributed to a fresh attack wave targeting victims in Ukraine with Remcos RAT as recently as this month.

While the threat actor has a history of delivering Remcos RAT since early 2024, newly spotted [attack chains distributing the malware](https://thehackernews.com/2024/02/new-idat-loader-attacks-using.html) have been simplified, employing weaponized LNK or PowerShell files to retrieve the decoy file and the Hijack Loader (aka IDAT Loader) payload, which then launches Remcos RAT.

"Hive0156 delivers weaponized Microsoft LNK and PowerShell files, leading to the download and execution of Remcos RAT," IBM X-Force [said](https://www.ibm.com/think/x-force/hive0156-continues-remcos-campaigns-against-ukraine), adding it "observed key decoy documents featuring themes that suggest a focus on the Ukrainian military and evolving to a potential wider audience."

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

[aerospace](https://thehackernews.com/search/label/aerospace)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Defense Industry](https://thehackernews.com/search/label/Defense%20Industry)[Malware](https://thehackernews.com/search/label/Malware)[Phishing](https://thehackernews.com/search/label/Phishing)[powershell](https://thehackernews.com/search/label/powershell)[Seqrite Labs](https://thehackernews.com/search/label/Seqrite%20Labs)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effecti...