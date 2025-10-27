---
title: Researchers Demonstrate How EDR and Antivirus Can Be Weaponized Against Users
url: https://thehackernews.com/2022/12/researchers-demonstrate-how-edr-and.html
source: The Hacker News
date: 2022-12-13
fetch_date: 2025-10-04T01:21:11.035054
---

# Researchers Demonstrate How EDR and Antivirus Can Be Weaponized Against Users

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

# [Researchers Demonstrate How EDR and Antivirus Can Be Weaponized Against Users](https://thehackernews.com/2022/12/researchers-demonstrate-how-edr-and.html)

**Dec 12, 2022**Ravie LakshmananEndpoint Detection / Data Security

[![EDR and Antivirus](data:image/png;base64... "EDR and Antivirus")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj9qNzO0SqHJMEn9ZW2rXcsVX38_K-q9qMcex2-iDsE8ke9ik__AZsU4G_OwvS1aHghqf09oc21uEbI1R2LLJKuzXBVvE1-abXAHQlxGzNZR0gOrK9FKdfGYA_Ff4NQJiETlvqy367PPl0DFA1gPpjuBUHY8dT40OBHOQSpgHG5GF2Jm4Cmqn4RfkS/s790-rw-e365/av.png)

High-severity security vulnerabilities have been disclosed in different endpoint detection and response (EDR) and antivirus (AV) products that could be exploited to turn them into data wipers.

"This wiper runs with the permissions of an unprivileged user yet has the ability to wipe almost any file on a system, including system files, and make a computer completely unbootable," SafeBreach Labs researcher Or Yair [said](https://www.safebreach.com/resources/blog/safebreach-labs-researcher-discovers-multiple-zero-day-vulnerabilities/). "It does all that without implementing code that touches the target files, making it fully undetectable."

EDR software, by design, are capable of continually scanning a machine for potentially suspicious and malicious files, and taking appropriate action, such as deleting or quarantining them.

The idea, in a nutshell, is to trick vulnerable security products into deleting legitimate files and directories on the system and render the machine inoperable by making use of specially crafted paths.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This is achieved by taking advantage of what's called a [junction point](https://learn.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions) (aka soft link), where a directory serves as an alias to another directory on the computer.

Put differently, between the window the EDR software identifies a file as malicious and attempts to delete the file from the system, the attacker uses a junction to point the software towards a different path, like C:\ drive.

The approach, however, didn't result in a wipe as EDRs prevented further access to a file after it was flagged as malicious. What's more, should the rogue file be deleted by the user, the software was clever enough to detect the deletion and stop itself from acting on it.

The ultimate solution arrived in the form of a wiper tool, dubbed [Aikido](https://github.com/SafeBreach-Labs/aikido_wiper), that triggers the privileged delete by creating a malicious file at a decoy directory and not granting it any permission, causing the EDRs to postpone the delete until next reboot.

Given this new attack interval, all an adversary has to do is delete the directory containing the rogue file, create a junction to point to the target directory to be deleted, and reboot the system.

Successful weaponization of the technique could result in the deletion of system files like drivers, preventing the operating system from booting. It can also be abused to remove all files from administrator user directories.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Out of 11 security products that were tested, six were found vulnerable to the zero-day wiper exploit, prompting the vendors to release updates to address the shortcoming -

* [**CVE-2022-37971**](https://nvd.nist.gov/vuln/detail/CVE-2022-37971) (CVSS score: 7.1) - Microsoft Defender and Defender for Endpoint
* [**CVE-2022-45797**](https://nvd.nist.gov/vuln/detail/CVE-2022-45797) (CVSS score: 7.1) - Trend Micro Apex One
* [**CVE-2022-4173**](https://nvd.nist.gov/vuln/detail/CVE-2022-4173) (CVSS score: 8.8) - Avast and AVG Antivirus

"The wiper executes its malicious actions using the most trusted entity on the system — the EDR or AV," Yair said. "EDRs and AVs do not prevent themselves from deleting files."

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

[Antivirus](https://thehackernews.com/search/label/Antivirus)[avast](https://thehackernews.com/search/label/avast)[AVG](https://thehackernews.com/search/label/AVG)[EDR Software](https://thehackernews.com/search/label/EDR%20Software)[Microsoft Defender](https://thehackernews.com/search/label/Microsoft%20Defender)[Trend Micro](https://thehackernews.com/search/label/Trend%20Micro)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/m...