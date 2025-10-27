---
title: Experts Reveal Google Cloud Platform's Blind Spot for Data Exfiltration Attacks
url: https://thehackernews.com/2023/03/experts-reveal-google-cloud-platforms.html
source: The Hacker News
date: 2023-03-07
fetch_date: 2025-10-04T08:52:07.642311
---

# Experts Reveal Google Cloud Platform's Blind Spot for Data Exfiltration Attacks

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

# [Experts Reveal Google Cloud Platform's Blind Spot for Data Exfiltration Attacks](https://thehackernews.com/2023/03/experts-reveal-google-cloud-platforms.html)

**Mar 06, 2023**Ravie LakshmananCloud Computing / Data Safety

[![Google Cloud Platform'](data:image/png;base64... "Google Cloud Platform'")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0PMpGRIvSHCt1Hw-np7fZEO5z-QkvPpzs9xoE4bUbI-iviths4IvQa-EpUdgBublbgsXVbHsgXer72bRdOjoLqMRpIui5GP6xp2tqV2dzpOY--ZuSk0I5u7twSGD6MrjYaPyBxufp-Z5PASSnZbcaX7V0ChUQU5WhPN45Ogjloxz5soB3scGiizvD/s790-rw-e365/Google.png)

Malicious actors can take advantage of "insufficient" forensic visibility into Google Cloud Platform (GCP) to exfiltrate sensitive data, a new research has found.

"Unfortunately, GCP does not provide the level of visibility in its storage logs that is needed to allow any effective forensic investigation, making organizations blind to potential data exfiltration attacks," cloud incident response firm Mitiga [said](https://www.mitiga.io/blog/mitiga-security-advisory-insufficient-forensic-visibility-in-gcp-storage) in a report.

The attack banks on the prerequisite that the adversary is able to gain control of an identity and access management (IAM) entity in the targeted organization by methods like social engineering to access the GCP environment.

The crux of the problem is that GCP's [storage access logs](https://cloud.google.com/storage/docs/access-logs) do not provide adequate transparency with regards to potential file access and read events, instead grouping them all as a single "Object Get" activity.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The same event is used for a wide variety of types of access, including: Reading a file, downloading a file, copying a file to an external server, [and] reading the metadata of the file," Mitiga researcher Veronica Marinov said.

This lack of distinction could enable an attacker to harvest sensitive data without being detected, mainly because there is no way to differentiate between malicious and legitimate user activity.

[![Data Exfiltration Attacks](data:image/png;base64... "Data Exfiltration Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV9Hw4UhUcMj1DyrYglLoYXkbYj5RLMrR9dc0SNJAsyaw_V9uz5u1lO2xcwugF_so4u0XQyJxkgrD7W6iiBAxEm622iQBNK79aang1blb_X0Gwj4ONq4nSKyiu69YvS1bqFRLW7KKikCOf-TWnjTJ4FFRuppUTVFlDTfIdDxuECdDQP4BM8LSc5lJ5/s790-rw-e365/logs.png)

In a [hypothetical attack](https://www.mitiga.io/blog/google-cloud-platform-exfiltration-a-threat-hunting-guide), a threat actor can use Google's command line interface ([gsutil](https://cloud.google.com/storage/docs/gsutil)) to transfer valuable data from the victim organization's storage buckets to an external storage bucket within the attacker organization.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Google has since provided mitigation recommendations, which range from Virtual Private Cloud ([VPC](https://cloud.google.com/vpc-service-controls)) Service Controls to using [organization restriction headers](https://cloud.google.com/resource-manager/docs/organization-restrictions/test-org-restrictions) to limit cloud resource requests.

The disclosure comes as Sysdig unearthed a sophisticated attack campaign dubbed [SCARLETEEL](https://thehackernews.com/2023/03/hackers-exploit-containerized.html) that's targeting containerized environments to perpetrate theft of proprietary data and software.

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

[Cloud computing](https://thehackernews.com/search/label/Cloud%20computing)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Data Safety](https://thehackernews.com/search/label/Data%20Safety)[Google Cloud](https://thehackernews.com/search/label/Google%20Cloud)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "C...