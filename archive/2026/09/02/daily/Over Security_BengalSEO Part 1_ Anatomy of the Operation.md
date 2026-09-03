---
title: BengalSEO Part 1: Anatomy of the Operation
url: https://thedfirreport.com/2026/08/24/bengalseo-part-1-anatomy-of-the-operation/
source: Over Security
date: 2026-09-02
fetch_date: 2026-09-03T07:02:52.513153
---

# BengalSEO Part 1: Anatomy of the Operation

Our next Digital Forensics Challenge is on September 26th

[Click here to signup](https://dfirlabs.thedfirreport.com/dfirchallenge)
X

[![](https://thedfirreport.com/wp-content/uploads/DFIR-REPORT-Logo@2x.png)

![](https://thedfirreport.com/wp-content/uploads/DFIR-White-Logo.png)](https://thedfirreport.com)

* [Public Reports](https://thedfirreport.com/reports/)
* Products

  + - [Products Overview](https://thedfirreport.com/products/)
    - [Threat Intel](https://thedfirreport.com/products/threat-intel/)
      * [Threat Feed](https://thedfirreport.com/products/threat-feed/)
      * [Private DFIR Reports](https://thedfirreport.com/products/threat-intel/private-dfir-reports/)
      * [All Intel](https://thedfirreport.com/products/threat-intel/all-intel/)
      * [Active Defense](https://thedfirreport.com/products/active-defense/)
    - [DFIR Labs](https://thedfirreport.com/products/dfir-labs/)
    - [Case Artifacts](https://thedfirreport.com/products/case-artifacts/)
  + - -
    - [Detection Pack](https://thedfirreport.com/products/detection-pack/)
    - [AI Training Ground](https://thedfirreport.com/products/ai-training-ground/)
  + - -

      bruteratel

      [From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/)

      [Read More](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/)
    - -

      dragonforce

      [Blurring the Lines: Intrusion Shows Connection With Three Major Ransomware Gangs](https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/)

      [Read More](https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/)
* Services

  + - [Services Overview](https://thedfirreport.com/services/)
    - [Training](https://thedfirreport.com/services/training/)
      * [Threat Hunting](https://thedfirreport.com/services/training/threat-hunting/)
  + - -
    - [Professional Services](https://thedfirreport.com/services/professional-services/)
      * [Integration](https://thedfirreport.com/services/professional-services/integration/)
      * [CTI Program Advisory](https://thedfirreport.com/services/professional-services/cti-program-advisory/)
      * [Incident Response Playbook](https://thedfirreport.com/services/professional-services/incident-response-playbook/)
* Company

  + - [About us](https://thedfirreport.com/company/about-us/)
    - [Contact Us](https://thedfirreport.com/company/contact-us/)
  + - [Collaboration](https://thedfirreport.com/company/collaboration/)
    - [Careers](https://thedfirreport.com/company/careers/)
* [Analysts](https://thedfirreport.com/company/analysts/)

* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/auth/login)
* [Get in Touch](https://thedfirreport.com/company/contact-us/)

* [Public Reports](https://thedfirreport.com/reports/)
* Products
  + [Products Overview](https://thedfirreport.com/products/)
  + Threat Intel
    - [Threat intel Overview](https://thedfirreport.com/products/threat-intel/)
    - [Threat Feed](https://thedfirreport.com/products/threat-feed/)
    - [Private DFIR Reports](https://thedfirreport.com/products/threat-intel/private-dfir-reports/)
    - [All Intel](https://thedfirreport.com/products/threat-intel/all-intel/)
    - [Active Defense](https://thedfirreport.com/products/active-defense/)
  + [DFIR Labs](https://thedfirreport.com/products/dfir-labs/)
  + [Case Artifacts](https://thedfirreport.com/products/case-artifacts/)
  + [Detection Pack](https://thedfirreport.com/products/detection-pack/)
  + [AI Training Ground](https://thedfirreport.com/products/ai-training-ground/)
* Services
  + [Service Overview](https://thedfirreport.com/services/)
  + [Training](https://thedfirreport.com/services/training/)
    - [Threat Hunting](https://thedfirreport.com/services/training/threat-hunting/)
  + [Professional Services](https://thedfirreport.com/services/professional-services/)
    - [Integration](https://thedfirreport.com/services/professional-services/integration/)
    - [CTI Program Advisory](https://thedfirreport.com/services/professional-services/cti-program-advisory/)
    - [Incident Response Playbook](https://thedfirreport.com/services/professional-services/incident-response-playbook/)
* Company
  + [Company Overview](https://thedfirreport.com/company/)
  + [About us](https://thedfirreport.com/company/about-us/)
  + [Contact Us](https://thedfirreport.com/company/contact-us/)
  + [Careers](https://thedfirreport.com/company/careers/)
* [Analyst](/company/analysts/)
* [SQL Brute Force Leads to BlueSky Ransomware](https://thedfirreport.com/2023/12/04/sql-brute-force-leads-to-bluesky-ransomware/)
* [From OneNote to RansomNote: An Ice Cold Intrusion](https://thedfirreport.com/2024/04/01/from-onenote-to-ransomnote-an-ice-cold-intrusion/)

![](https://thedfirreport.com/wp-content/uploads/pr_39750_pt1_001.png)

[scam](https://thedfirreport.com/category/scam/)

# BengalSEO Part 1: Anatomy of the Operation

August 24, 2026

## Key Takeaways

* In March 2026, a widespread SEO Poisoning campaign leading to malware deployment and tech support scams was identified by the DFIR Report.
* This campaign was attributed to a scam operation operating out of Rajasthan, India, which our team has dubbed BengalSEO
* Two IT Service Provider companies and their owners were identified as the main drivers for the BengalSEO operations.
* This group utilizes its extensive SEO and web development capabilities to create and promote lure pages with multiple Black Hat SEO techniques.
* These lure pages then tie into a sophisticated Traffic Distribution System to direct, track, and filter traffic to payloads and tech support scams.
* This includes deploying a custom malware strain our team has named MayaBot, used to further scam operations.

## The DFIR Report Offerings

Check out our Products [here](https://thedfirreport.com/products/) and our Services [here](https://thedfirreport.com/services/). Want a demo, more information on our services, pricing or just want to chat? [Get in Touch](https://thedfirreport.com/company/contact-us/)

**[Contact us](https://thedfirreport.com/contact/)** today for pricing or a demo!

## Case Summary

In March 2026, our team identified an SEO poisoning campaign leading to malware deployment and tech support scams. Further research into this campaign revealed a sophisticated and widespread scam operation that has been operating since at least 2015. Our team attributes this operation, with high confidence, to a group of core individuals and IT service providers operating out of Rajasthan, India, which our team tracks collectively as BengalSEO.

Using indicators gathered from the identified SEO poisoning campaign, our team was able to correlate this activity with information posted on scam hunting forums. This discovery led our team to a company named WeConnect Solutions LLC (previously iConnect Soft Solutions LLC), which operates a tech support call center located in Kota, Rajasthan. Additional research into this company allowed our team to identify its core members, history, and links to supporting companies involved in the operation.

A second company named Garage2Global was identified, which had the same owners and operated out of the same office building. Garage2Global advertises itself as a legitimate SEO, Web & Mobile App Development, and Digital Marketing services provider; however, our research uncovered extensive evidence indicating Garage2Global develops malicious web infrastructure used in SEO poisoning campaigns as part of the BengalSEO scam operation.

Our team assesses these two companies and their owners to be the primary drivers of the current operation; however, our research implicates multiple companies and individuals that have contributed to or benefited from the...