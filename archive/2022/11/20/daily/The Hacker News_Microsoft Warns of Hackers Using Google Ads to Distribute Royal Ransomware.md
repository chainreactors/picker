---
title: Microsoft Warns of Hackers Using Google Ads to Distribute Royal Ransomware
url: https://thehackernews.com/2022/11/microsoft-warns-of-hackers-using-google.html
source: The Hacker News
date: 2022-11-20
fetch_date: 2025-10-03T23:18:13.696318
---

# Microsoft Warns of Hackers Using Google Ads to Distribute Royal Ransomware

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

# [Microsoft Warns of Hackers Using Google Ads to Distribute Royal Ransomware](https://thehackernews.com/2022/11/microsoft-warns-of-hackers-using-google.html)

**Nov 19, 2022**Ravie Lakshmanan

[![Royal Ransomware](data:image/png;base64... "Royal Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZxPcpN43GXSu6zlyXaWj9ggFPAJrUbqPzdQdObOs1dbdPUub3UrAUPBclfBxTeKY1woetGJRXkUF-tNidu4os2LPhSjwV3gsR3aRDTHfhJOh2BOYUU_b-t2FshnbZVkIjLbAP3A7v45SvmLs3nghQzOdF6j6TI77zBajGuCpvb1HnVRklCKBawp0X/s790-rw-e365/royal-ransomware.png)

A developing threat activity cluster has been found using Google Ads in one of its campaigns to distribute various post-compromise payloads, including the recently discovered [Royal ransomware](https://www.fortinet.com/blog/threat-research/ransomware-roundup-royal-ransomware).

Microsoft, which spotted the updated malware delivery method in late October 2022, is tracking the group under the name **DEV-0569**.

"Observed DEV-0569 attacks show a pattern of continuous innovation, with regular incorporation of new discovery techniques, defense evasion, and various post-compromise payloads, alongside increasing ransomware facilitation," the Microsoft Security Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2022/11/17/dev-0569-finds-new-ways-to-deliver-royal-ransomware-various-payloads/) in an analysis.

The threat actor is known to rely on malvertising to point unsuspecting victims to malware downloader links that pose as software installers for legitimate apps like Adobe Flash Player, AnyDesk, LogMeIn, Microsoft Teams, and Zoom.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware downloader, a strain referred to as [BATLOADER](https://thehackernews.com/2022/02/new-seo-poisoning-campaign-distributing.html), is a dropper that functions as a conduit to distribute next-stage payloads. It has been observed to share overlaps with another malware called [ZLoader](https://thehackernews.com/2022/04/microsoft-disrupts-zloader-cybercrime.html).

[![Royal Ransomware](data:image/png;base64... "Royal Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxUxM-JCnj_HdlaryYKsQLLOEp5QEZUhVXJ4_SC1gbSxKJiknBc0UGY6SZfy8rC-2Q2sFjELQ84osNXMDL1w2mRMw0RdlWPbjhQ402Gju9T8Wrarpmwcfam50ShjudRJDWR_HjWjhZGUZIJFoqvTJDuvC7DkmaMXwjd9SIx5i-3cJNBuZjI_udT2Bo/s790-rw-e365/software-download.png)

A recent analysis of BATLOADER by [eSentire](https://www.esentire.com/blog/batloader-facilitates-fraud-hands-on-keyboard-attacks) and [VMware](https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html) called out the malware's stealth and persistence, in addition to its use of search engine optimization (SEO) poisoning to lure users to download the malware from compromised websites or attacker-created domains.

Alternatively, phishing links are shared through spam emails, fake forum pages, blog comments, and even [contact forms](https://thehackernews.com/2021/04/hackers-using-websites-contact-forms-to.html) present on targeted organizations' websites.

[![Royal Ransomware](data:image/png;base64... "Royal Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE4-AtSQatdMIfZmgv55ukN1hMyPdLoJTWk-K_xCXbQGjR18LhEc4qBlR0Lc0ocQQoR2CAjVtorAnnuwf7dI3JE3Y55V0s_wq9H2IPouxj6InFsL-_DAaeZTnHBQMmNOMoVqlaYg_ERHHmQK0XiUJgX56GUhqPpKCH6fxiTvLDEPYsoftRoCpPkQr3/s790-rw-e365/royal-ransomware.png)

"DEV-0569 has used varied infection chains using PowerShell and batch scripts that ultimately led to the download of malware payloads like information stealers or a legitimate remote management tool used for persistence on the network," the tech giant noted.

"The management tool can also be an access point for the staging and spread of ransomware."

Also utilized is a tool known as NSudo to launch programs with elevated privileges and impair defenses by adding registry values that are designed to disable antivirus solutions.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The use of Google Ads to deliver BATLOADER selectively marks a diversification of the DEV-0569's distribution vectors, enabling it to reach more targets and deliver malware payloads, the company pointed out.

It further positions the group to serve as an [initial access broker](https://thehackernews.com/2021/06/ransomware-attackers-partnering-with.html) for other ransomware operations, joining the likes of malware such as [Emotet](https://thehackernews.com/2022/10/emotet-botnet-distributing-self.html), [IcedID](https://thehackernews.com/2022/10/black-basta-ransomware-hackers.html), and [Qakbot](https://thehackernews.com/2022/11/researchers-find-links-bw-black-basta.html).

"Since DEV-0569's phishing scheme abuses legitimate services, organizations can also leverage mail flow rules to capture suspicious keywords or review broad exceptions, such as those related to IP ranges and domain-level allow lists," Microsoft said.

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

[DEV-0569](https://thehackernews.com/search/label/DEV-0569)[Google Ads](https://thehackernews.com/search/label/Google%20Ads)[Malware](https://theh...