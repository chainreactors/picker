---
title: PivotTables For InfoSec Dummies
url: https://trustedsec.com/blog/pivottables-for-infosec-dummies
source: TrustedSec
date: 2025-08-06
fetch_date: 2025-10-07T00:49:25.344050
---

# PivotTables For InfoSec Dummies

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
* [PivotTables For InfoSec Dummies](https://trustedsec.com/blog/pivottables-for-infosec-dummies)

August 05, 2025

# PivotTables For InfoSec Dummies

Written by
Philip DuBois

Application Security Assessment
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PivotTablesForInfoSecDummies_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1753900476&s=a964ea10972b75d82bd53a53c2ff58fc)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#4f703c3a2d252a2c3b720c272a2c246a7d7f203a3b6a7d7f3b27263c6a7d7f2e3d3b262c232a6a7d7f293d20226a7d7f1b3d3a3c3b2a2b1c2a2c6a7d7e692e223f742d202b36721f2639203b1b2e2d232a3c6a7d7f09203d6a7d7f062129201c2a2c6a7d7f0b3a2222262a3c6a7c0e6a7d7f273b3b3f3c6a7c0e6a7d096a7d093b3d3a3c3b2a2b3c2a2c612c20226a7d092d2320286a7d093f2639203b3b2e2d232a3c6229203d62262129203c2a2c622b3a2222262a3c "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpivottables-for-infosec-dummies "Share on Facebook")
* [Share on X](http://twitter.com/share?text=PivotTables%20For%20InfoSec%20Dummies%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpivottables-for-infosec-dummies "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpivottables-for-infosec-dummies&mini=true "Share on LinkedIn")

Plenty of people know how to toss an IP address and port list into Excel for sorting and searching but don’t get a chance to take it to a deeper level. Excel pivot tables are a great next step to explore, offering a simple yet potent interface for data analysis. Dynamic pivot tables can be friendlier than on-the-fly bash with `grep`, `cut`, `sort`, `uniq`, `sed`, and `awk` commands. Additionally, Excel can be more accessible than alternatives, especially for newcomers to the security space.

During initial assessment recon, I commonly run [***SpooNMAP***](https://github.com/trustedsec/spoonmap) and save the ***Nmap*** output to an XML file. A handy tool, [***Nmap-xml2csv***](https://github.com/NetsecExplained/Nmap-XML-to-CSV), creates a simple CSV file from that XML data, which imports nicely into Excel. For this example, we’re using a fictional scan from the private side of a multi-branch office DMZ network.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PivotTables_DuBois/image001.png?w=320&q=90&auto=format&fit=max&dm=1754077323&s=418a81c7d39373d50b9149598a59fbb4)

Figure 1 - Sample Nmap CSV Export

Although the Excel interface has changed over time (and will likely continue to change), a high-level setup generally involves highlighting the CSV data and inserting the pivot table. (I personally prefer to put tables in new tabs if offered the opportunity.)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PivotTables_DuBois/image002.png?w=320&q=90&auto=format&fit=max&dm=1754077325&s=64ca8421b717acb5f2865e09dc154ee3)

Figure 2 - Easy Pivot Table Setup

After it is created, the table will appear empty. A new interface will be available that allows us to slice and dice data dynamically.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PivotTables_DuBois/image003.png?w=320&q=90&auto=format&fit=max&dm=1754077325&s=8cfd2cffe1f4871338acc4970a2632b5)

Figure 3 - Table Loaded and Ready

Let’s start with a simple summary to see how much of each service was picked up on the scan. By dragging the “Service” down to “Rows” and then again dragging “Service” down to “Σ Values,” we get a summation of the instances of each service picked up in the ***Nmap*** scan. (Continue on in the article if you get a “Sum” instead of a “Count” within the “Σ Values” box.) In this example, several things look interesting for a DMZ.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PivotTables_DuBois/image004.png?w=320&q=90&auto=format&fit=max&dm=1754077326&s=3e54d6dba1f5d61a0bdedb5c2472446a)

Figure 4 - Basic Services Summary

While the obvious Windows boxes living in a DMZ raise my eyebrow, I’m a bit more interested in the relatively high quantity of ISAKMP services. Let’s get some details on that. Let’s move “Service” to “Filter” and drag “IP” to “Rows”. After the data shows up, we can adjust the filter to show only isakmp and sort the IP rows in ascending order.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PivotTables_DuBois/image005.png?w=320&q=90&auto=format&fit=max&dm=1754077327&s=26e183d9e89ad82a114af9fe5b32e3c4)

Figure 5 - First Peek

After making sure the auto-calculated g...