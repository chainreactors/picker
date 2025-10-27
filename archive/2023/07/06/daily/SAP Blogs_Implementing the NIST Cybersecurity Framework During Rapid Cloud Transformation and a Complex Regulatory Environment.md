---
title: Implementing the NIST Cybersecurity Framework During Rapid Cloud Transformation and a Complex Regulatory Environment
url: https://blogs.sap.com/2023/07/05/implementing-the-nist-cybersecurity-framework-during-rapid-cloud-transformation-and-a-complex-regulatory-environment/
source: SAP Blogs
date: 2023-07-06
fetch_date: 2025-10-04T11:53:17.776235
---

# Implementing the NIST Cybersecurity Framework During Rapid Cloud Transformation and a Complex Regulatory Environment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Implementing the NIST Cybersecurity Framework Duri...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158498&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implementing the NIST Cybersecurity Framework During Rapid Cloud Transformation and a Complex Regulatory Environment](/t5/technology-blog-posts-by-sap/implementing-the-nist-cybersecurity-framework-during-rapid-cloud/ba-p/13552088)

![JayThvV](https://avatars.profile.sap.com/3/3/id3354bd25bcc342bba21b539e4aa1ad4537cfc604317839a7bc64a32b204ce9a3_small.jpeg "JayThvV")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[JayThvV](https://community.sap.com/t5/user/viewprofilepage/user-id/160843)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158498)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158498)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552088)

‎2023 Jul 05
11:50 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158498/tab/all-users "Click here to see who gave kudos to this post.")

5,810

* SAP Managed Tags
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [Cloud Operations](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Operations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)

* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [Cloud Operations

  Topic](/t5/c-khhcw49343/Cloud%2BOperations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)

View products (3)

Managing cybersecurity risks is challenging in any climate. Doing it in the middle of rapid cloud transformation adds additional complexity and need for agility. Understanding the direction the company strategy was pointing the company in, to better manage the associated cybersecurity risks, SAP decided to implement the NIST Cybersecurity Framework (NIST CSF). Recently, Ernst & Young and SAP jointly published [Keeping SAP Customers Secure Around the Globe - Taking a Risk-Based Approach to Protect Customer Dat...](https://www.sap.com/documents/2023/05/4a7c091f-747e-0010-bca6-c68f7e60039b.html)(EY/SAP), a brochure that describes lessons learnt and initial benefits of SAP's NIST Cybersecurity Framework (NIST CSF) implementation.

What the brochure only hints at through the collaboration and dialogue across the organization is how this implementation took place against a backdrop of rapid technological and organizational change of rapid cloud transformation. In this article, I go deeper into how NIST CSF provides a stable structure to drive continuous improvement in our cloud security posture, while allowing the flexibility and agility for cloud transformation with ever-changing and evolving policies and compliance audit requirements.

# Flexible and Globally Applicable

As the EY/SAP brochure says:
> The implementation of NIST CSF is a forward-thinking approach helping SAP transition from a compliance and risk assessment mindset into a more adaptive and responsive posture of managing cybersecurity risk to deal with ever-changing cyber threats.

This transition is particularly important as SAP continues to evolve from a software provider to a cloud services provider, experiencing rapid growth in Cloud ERP and customers migrating on-premise SAP systems to the cloud. Therefore, beyond the ever-changing cyber threats we are all presented with at any moment, SAP also assumes new risks now that we increasingly operate the systems that are critical to our customers to conduct business.

SAP implemented NIST CSF version 1.1 as described in [Framework for Improving Critical Infrastructure Cybersecurity](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf) (NIST CSF v1.1). Version 2.0 is currently in draft form and SAP is actively involved in the feedback round. While version 2.0 is still not explicitly cloud aware, the framework is intended to be flexible enough to accommodate technological changes. As NIST CSF v1.1 states:
> The Framework remains effective and supports technical innovation because it is technology neutral, while also referencing a variety of existing standards, guidelines, and practices that evolve with technology. By relying on those global standards, guidelines, and practices developed, managed, and updated by industry, the tools and methods available to achieve the Framework outcomes will scale across borders, acknowledge the global nature of cybersecurity risks, and evolve with technological advances and business requirements.

The flexible nature of the framework as well as applicability globally are important to SAP. Managing cybersecurity risk during ongoing cloud transformation implies constant change. NIST CSF provides a stable framework that describes the necessary capabilities to manage cybersecurity risk, where the underlying security policies and processes can evolve with technological changes. But it also accommodates continuous changes in the global regulatory environment and associated compliance audits, as different jurisdictions around the world adopt similar but varying security regulations, requirements and guidelines. Since SAP offers its cloud solutions everywhere apart from sanctioned countries and territories, and many of our customers are in the public or regulated private sector and themselves are subject to 3rd party audits, NIST CSF's ability to scale across borders is particularly beneficial.

# NIST CSF Overview

NIST CSF v1.1 is a fairly easy read as far as such documents go. In short. NIST CSF is a self-assessment framework that provides a common taxonomy and mechanism for organizations to:

1. Describe their current cybersecurity posture

2. Describe their target state for cybersecurity

3. Identify and prioritize opportunities for improvement within the context of a
   continuous and repeatable process

4. Assess progress toward the target state

5. Communicate among internal and external stakeholders about cybersecurity risk

The communication aspect cannot be underestimated in a large, complex organization where it isn't always easy to get everyone on the same page or who is responsible for what. Such challenges are amplified in the middle of cloud transformation and organizational change. NIST CSF is also very helpful in external communication with customers and partners as well as auditors globally, many of whom are familiar with the framework or at least can easily find online resources on the NIST website if they aren't.

The framework categorizes cybersecurity functions and capabilities necessary to manage cybersecurity risk appropriate to the business risks the organization is exposed to and at a level of sophistication it is willing and able to bear. Specifically,
> [t]he Framework Core ...