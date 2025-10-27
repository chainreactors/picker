---
title: When on Workstation, Do as the Local Browsers Do!
url: https://trustedsec.com/blog/when-on-workstation-do-as-the-local-browsers-do
source: TrustedSec
date: 2024-09-04
fetch_date: 2025-10-06T18:31:45.142406
---

# When on Workstation, Do as the Local Browsers Do!

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [When on Workstation, Do as the Local Browsers Do!](https://trustedsec.com/blog/when-on-workstation-do-as-the-local-browsers-do)

September 03, 2024

# When on Workstation, Do as the Local Browsers Do!

Written by
Megan Nilsen

Purple Team Adversarial Detection & Countermeasures

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WorkstationLocalBrowsers_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1724872908&s=f591594594827bc30f4d6971118388c4)

Table of contents

* [1    Introduction](#Introduction)
* [2    Browser Extensions](#Extensions)
* [3    Sensitive Data Extraction](#Extraction)
* [4    Examining (Other) Potential Log Sources](#Sources)
* [5    Conclusion](#Conclusion)
* [6    References](#References)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#81bef2f4e3ebe4e2f5bcc2e9e4e2eaa4b3b1eef4f5a4b3b1f5e9e8f2a4b3b1e0f3f5e8e2ede4a4b3b1e7f3eeeca4b3b1d5f3f4f2f5e4e5d2e4e2a4b3b0a7e0ecf1bae3eee5f8bcd6e9e4efa4b3b1eeefa4b3b1d6eef3eaf2f5e0f5e8eeefa4b3c2a4b3b1c5eea4b3b1e0f2a4b3b1f5e9e4a4b3b1cdeee2e0eda4b3b1c3f3eef6f2e4f3f2a4b3b1c5eea4b3b0a4b2c0a4b3b1e9f5f5f1f2a4b2c0a4b3c7a4b3c7f5f3f4f2f5e4e5f2e4e2afe2eeeca4b3c7e3edeee6a4b3c7f6e9e4efaceeefacf6eef3eaf2f5e0f5e8eeeface5eeace0f2acf5e9e4acedeee2e0edace3f3eef6f2e4f3f2ace5ee "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhen-on-workstation-do-as-the-local-browsers-do "Share on Facebook")
* [Share on X](http://twitter.com/share?text=When%20on%20Workstation%2C%20Do%20as%20the%20Local%20Browsers%20Do%21%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhen-on-workstation-do-as-the-local-browsers-do "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhen-on-workstation-do-as-the-local-browsers-do&mini=true "Share on LinkedIn")

## 1    Introduction

Web browsers are common targets for many different APTs. Tools like [Redline Malware](https://www.infosecinstitute.com/resources/malware-analysis/redline-stealer-malware-full-analysis/) or penetration testing tools such as [SharpChrome](https://github.com/GhostPack/SharpDPAPI.git) or [SharpChromium](https://github.com/djhohnstein/SharpChromium) steal sensitive data like cookies and saved login data, and many others target the installation of browser extensions that can allow for exfiltration of data or other browser-related exploits.

To boot, building detections on browser abuse can be challenging and riddled with false positives due to the sheer volume of data that can waste analyst time and prevent timely identification of key IOCs that may stop more widespread compromise.

This post will seek to provide organizations with high-fidelity template detections based on classic Splunk SPL queries to assist with detecting this activity. It should be noted that this post is not a comprehensive study on all telemetry available to identify these attacks; rather, we will focus on the most accessible means of detection.

It should also be noted that TrustedSec also has community detections that provide some alternate detection opportunities as well as [SIGMA](https://github.com/cybergoatpsyops/detections/tree/main/techniques/webCredentialHarvest) detections written by Leo Bastidas [@cyberGoatPysOps](https://x.com/cyberGoatPsyOps?t=VEgyLCPmNyfiCye_wl8McQ&s=09). While the detections we will build within this blog post are different, they can be used in addition to the original work done by TrustedSec and Leo.

## 2    Browser Extensions

### 2.1      Configuring Auditing and SACLS—Browser Extension Installation

Before we can execute attacks, we need to ensure our lab is configured with the proper auditing and SACLs to build the detections within Splunk.

To start, you will need to enable Windows Event ID 4657 in order to detect modifications to the Registry. Ensure you have Registry modification auditing enabled within GPO at the following location:

***Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object Access***

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Workstation_Nilsen/Figure-1.png?w=320&q=90&auto=format&fit=max&dm=1724873117&s=1dfccf794d384b5d84c9e668daab3ec5)

Figure 1 - Enabling Registry Auditing

In addition, navigate to Global Object Access Auditing and also enable and configure the SACL.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Workstation_Nilsen/Figure-2.png?w=320&q=90&auto=format&fit=max&dm=1724873119&s=5bcddb3ac27cfafc9e599f...