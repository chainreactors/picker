---
title: APT-C-36 Strikes Again: Blind Eagle Hackers Target Key Industries in Colombia
url: https://thehackernews.com/2023/02/apt-c-36-strikes-again-blind-eagle.html
source: The Hacker News
date: 2023-03-01
fetch_date: 2025-10-04T08:23:29.229257
---

# APT-C-36 Strikes Again: Blind Eagle Hackers Target Key Industries in Colombia

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

# [APT-C-36 Strikes Again: Blind Eagle Hackers Target Key Industries in Colombia](https://thehackernews.com/2023/02/apt-c-36-strikes-again-blind-eagle.html)

**Feb 28, 2023**Ravie LakshmananCyber Threat / Malware

[![Blind Eagle](data:image/png;base64... "Blind Eagle")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDV4aReQ3yKrFv9Y6_W7atpLuyzVhr9k9czHHEBCLL6sBJkwcR5VhZ3PqXgp8tYssCm9FpZsAMl9G2eDpGkX-O98unTgz6DWyCzm05ehLdEtHTOWFYu10Z_mZqnUHhLBtUHljP_mBV7uG7vWfl1WtR82zuySlsLS6NgCp7_ZMZqrgeQGin8hyPlldD/s790-rw-e365/hacking.png)

The threat actor known as **Blind Eagle** has been linked to a new campaign targeting various key industries in Colombia.

The activity, which was detected by the BlackBerry Research and Intelligence Team on February 20, 2023, is also said to encompass Ecuador, Chile, and Spain, suggesting a slow expansion of the hacking group's victimology footprint.

Targeted entities include health, financial, law enforcement, immigration, and an agency in charge of peace negotiation in Colombia, the Canadian cybersecurity company said.

Blind Eagle, also known as [APT-C-36](https://attack.mitre.org/groups/G0099/), was [recently covered](https://thehackernews.com/2023/01/blind-eagle-hackers-return-with-refined.html) by Check Point Research, detailing the adversary's advanced toolset comprising Meterpreter payloads that are delivered via spear-phishing emails.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The latest set of attacks involves the group impersonating the Colombian government tax agency, the National Directorate of Taxes and Customs (DIAN), to phish its targets using lures that urge recipients to settle "outstanding obligations."

The craftily designed email messages come with a link pointing to a PDF file that's purportedly hosted on DIAN's website, but actually deploys malware on the targeted system, effectively launching the infection chain.

"The fake DIAN website page contains a button that encourages the victim to download a PDF to view what the site claims to be pending tax invoices," BlackBerry researchers [said](https://blogs.blackberry.com/en/2023/02/blind-eagle-apt-c-36-targets-colombia).

[![Blind Eagle](data:image/png;base64... "Blind Eagle")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixqlINVTM7Ymi4hSyl-AXwQtfl8FPiUdi_TP8bz5l3ggvJXUBGigGRFAPZHWe4DVlYg4nOn3W38uzW3ZZQJ9w07YyqMfwX89Xs0p3RYUdKcFHdjp8hhZFtElOr_oQU3wK9GwmVDARYXF3Ntnc3AkXpCdjJaAV1hRQQLR4Wza-2__UXJs6rcOeH67Fc/s790-rw-e365/form.png)

"Clicking the blue button initiates the download of a malicious file from the Discord content delivery network (CDN), which the attackers are abusing in this phishing scam."

The payload is an obfuscated Visual Basic Script (VBS), which gets executed upon opening the "PDF" file and utilizes PowerShell to retrieve a .NET-based DLL file that ultimately loads AsyncRAT into memory.

"A malicious [remote access trojan] installed on a victim's machine enables the threat actor to connect to the infected endpoint any time they like, and to perform any operations they desire," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also of note is the threat actor's use of [dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/) services like DuckDNS to remotely commandeer the compromised hosts.

Blind Eagle is suspected to be a Spanish-speaking group owing to the use of the language in its spear-phishing emails. However, it's currently unclear where the threat actor is based and whether their attacks are motivated by espionage or financial gain.

"The modus operandi used has mostly stayed the same as the group's previous efforts – it is very simple, which may mean that this group is comfortable with its way of launching campaigns via phishing emails, and feels confident in using them because they continue to work," BlackBerry said.

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

[BlackBerry](https://thehackernews.com/search/label/BlackBerry)[Blind Eagle](https://thehackernews.com/search/label/Blind%20Eagle)[Check Point](https://thehackernews.com/search/label/Check%20Point)[hacking news](https://thehackernews.com/search/label/hacking%20news)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials]...