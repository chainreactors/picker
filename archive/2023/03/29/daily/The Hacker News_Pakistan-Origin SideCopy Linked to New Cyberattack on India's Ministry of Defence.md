---
title: Pakistan-Origin SideCopy Linked to New Cyberattack on India's Ministry of Defence
url: https://thehackernews.com/2023/03/pakistan-origin-sidecopy-linked-to-new.html
source: The Hacker News
date: 2023-03-29
fetch_date: 2025-10-04T11:03:35.015108
---

# Pakistan-Origin SideCopy Linked to New Cyberattack on India's Ministry of Defence

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

# [Pakistan-Origin SideCopy Linked to New Cyberattack on India's Ministry of Defence](https://thehackernews.com/2023/03/pakistan-origin-sidecopy-linked-to-new.html)

**Mar 28, 2023**Ravie LakshmananAdvanced Persistent Threat

[![Pakistani Hackers](data:image/png;base64... "Pakistani Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9JVo5ndAfxmwzzJZEpXnfQ84nTkRbbxZq6C0Fie5dYmvFibIOkMky8sV_w3j7qZZe-wJkO1aWQkuEYcPJ1gi8FzQ_6IOtr4AUA5JJkyGJiDdLLGS0c4LKm3r8d5CSpIxrvZPIdxsfnDGNU7ikBNw2iB8181UPv4yM-jw-n25bqdRBnUuqlOF8H-GH/s790-rw-e365/hacking.png)

An advanced persistent threat (APT) group that has a track record of targeting India and Afghanistan has been linked to a new phishing campaign that delivers Action RAT.

According to Cyble, which [attributed](https://blog.cyble.com/2023/03/21/notorious-sidecopy-apt-group-sets-sights-on-indias-drdo/) the operation to **SideCopy**, the activity cluster is designed to target the Defence Research and Development Organization ([DRDO](https://www.drdo.gov.in/about-drdo)), the research and development wing of India's Ministry of Defence.

Known for emulating the infection chains associated with [SideWinder](https://thehackernews.com/2023/02/researchers-link-sidewinder-group-to.html) to deliver its own malware, SideCopy is a threat group of Pakistani origin that shares overlaps with [Transparent Tribe](https://thehackernews.com/2022/11/researchers-detail-new-malware-campaign.html). It has been active since at least 2019.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack sequences mounted by the group involve using spear-phishing emails to gain initial access. These messages come bearing a ZIP archive file that contains a Windows shortcut file (.LNK) masquerading as information about the [K-4 ballistic missile](https://en.wikipedia.org/wiki/K-4_%28missile%29) developed by DRDO.

Executing the .LNK file leads to the retrieval of an HTML application from a remote server, which, in turn, displays a decoy presentation, while also stealthily deploying the Action RAT backdoor.

The malware, in addition to gathering information about the victim machine, is capable of running commands sent from a command-and-control (C2) server, including harvesting files and dropping follow-on malware.

[![Pakistani Hackers](data:image/png;base64... "Pakistani Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgU-owzGGNkVVetWesl8pYoscZB1EaIyngQkd4o-gdKLHfGtIxhAkON4Snt2Jm3jpXE0g6pNJ1e7NfpX8UxxAV9KSbhE4vKOA3vWFhUMlKIAHuLgFeB2rhJMqeDEKkUZbPvkMnR6Wk-fLALaLS7z0LuFHKwlsBP90Lr2Mt318y1UF24zeHyc0NQaAoc/s790-rw-e365/drdo.png)

Also deployed is a new information-stealing malware referred to as AuTo Stealer that's equipped to gather and exfiltrate Microsoft Office files, PDF documents, database and text files, and images over HTTP or TCP.

"The APT group continuously evolves its techniques while incorporating new tools into its arsenal," Cyble noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time SideCopy has employed Action RAT in its attacks directed against India. In December 2021, Malwarebytes [disclosed](https://thehackernews.com/2021/12/researchers-detail-how-pakistani.html) a set of intrusions that breached a number of ministries in Afghanistan and a shared government computer in India to steal sensitive credentials.

The latest findings arrive a month after the adversarial crew was [spotted](https://nsfocusglobal.com/indian-government-agencies-targeted-in-phishing-attacks-by-apt-group-sidecopy/) [targeting Indian government agencies](https://thehackernews.com/2023/02/researchers-warn-of-reverserat-backdoor.html) with a remote access trojan dubbed ReverseRAT.

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[Cyble](https://thehackernews.com/search/label/Cyble)[DRDO](https://thehackernews.com/search/label/DRDO)[Pakistani Hackers](https://thehackernews.com/search/label/Pakistani%20Hackers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to T...