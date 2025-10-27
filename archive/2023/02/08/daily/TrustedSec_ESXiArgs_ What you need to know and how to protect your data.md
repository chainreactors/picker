---
title: ESXiArgs: What you need to know and how to protect your data
url: https://www.trustedsec.com/blog/esxiargs-what-you-need-to-know-and-how-to-protect-your-data/
source: TrustedSec
date: 2023-02-08
fetch_date: 2025-10-04T06:00:25.002889
---

# ESXiArgs: What you need to know and how to protect your data

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
* [ESXiArgs: What you need to know and how to protect your data](https://trustedsec.com/blog/esxiargs-what-you-need-to-know-and-how-to-protect-your-data)

February 07, 2023

# ESXiArgs: What you need to know and how to protect your data

Written by
Tyler Hudak,
Liz Waddell,
Justin Vaicaro,
Steven Erwin,
Shane Hartman,
Olivia Cate and
Thomas Millar

Incident Response
Incident Response & Forensics
Threat Hunting

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ESXiArgs_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695565415&s=44067a5af9273b5c15d951789dfc23dc)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#36094543545c5355420b755e53555d130406594342130406425e5f451304065744425f555a531304065044595b1304066244434542535265535513040710575b460d5459524f0b73656e5f77445145130577130406615e57421304064f59431304065853535213040642591304065d5859411304065758521304065e59411304064259130406464459425355421304064f594344130406525742571305771304065e42424645130577130470130470424443454253524553551855595b130470545a595113047053454e5f574451451b415e57421b4f59431b585353521b42591b5d5859411b5758521b5e59411b42591b464459425355421b4f5943441b52574257 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-what-you-need-to-know-and-how-to-protect-your-data "Share on Facebook")
* [Share on X](http://twitter.com/share?text=ESXiArgs%3A%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20your%20data%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-what-you-need-to-know-and-how-to-protect-your-data "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-what-you-need-to-know-and-how-to-protect-your-data&mini=true "Share on LinkedIn")

## **Threat Overview**

Around February 03, 2023, a ransomware campaign called “ESXiArgs” emerged that targeted Internet-facing VMware ESXi servers running versions older than 7.0. Though not confirmed, it has been reported by the [French CERT](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2023-ALE-015/) (CERT-FR), [BleepingComputer](https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide/), and other sources that the campaign leverages [CVE-2021-21974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21974), which is a three-year-old vulnerability in the OpenSLP component of the ESXi instance. The vulnerability allows for remote code execution (RCE) and is currently being used to deploy ransomware; however, as with any vulnerability allowing RCE, it has the potential for additional attacks. The ransomware in this campaign targets virtual machine volumes within the ***/vmfs/volumes*** directory, encrypting their virtual disks and memory files, encrypting their virtual disks and memory files. The encryptor is executed by a bash script placed in ***/tmp/*** as part of the attack. The execution flow of the script is described below, and the TrustedSec Research team will also be publishing an in-depth analysis of the encryptor itself.

If CVE-2021-21974 is the initial attack vector used in this campaign, then the following ESXi platforms are at risk:

* ESXi 7.x versions earlier than ESXi70U1c-17325551
* ESXi versions 6.7.x earlier than ESXi670-202102401-SG
* ESXi versions 6.5.x earlier than ESXi650-202102101-SG

Note: Versions ESXi versions 6.0 and 5.5 have also reportedly been impacted by this campaign; however, TrustedSec has not yet been able to confirm the validity of these claims at this time.

An overview of the execution flow of the encryption deployment script is depicted in the chart below.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Fig1_update.png)

**Update:** CISA has released a recovery script, ESXiArgs-Recover, to assist in the rebuilding of virtual machines in impacted environments. The script works by leveraging unencrypted flat files (which appear to be untouched in this campaign) to rebuild a VM’s .vmdk file. More information can be found on the project’s GitHub page: <https://github.com/cisagov/ESXiArgs-Recover>.

## **Ransomware Deployment Script** **Technical Analysis**

TrustedSec examined the ESXiArgs deployment script found on impacted systems - [***encrypt.sh***](https://www.virustotal.com/gui/file/10c3b6b03a9bf105d264a8e7f30dcab0a6c59a414529b0af0a6bd9f1d2984459) - and identified the following execution steps:

* Sets the staging directory to ***/tmp/*** which contains the following attack files:
  + [***encrypt***](https://www.virustotal.com/gui/fi...