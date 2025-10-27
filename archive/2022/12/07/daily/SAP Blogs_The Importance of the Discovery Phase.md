---
title: The Importance of the Discovery Phase
url: https://blogs.sap.com/2022/12/06/the-importance-of-the-discovery-phase/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:17.762126
---

# The Importance of the Discovery Phase

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* The Importance of the Discovery Phase

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68384&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The Importance of the Discovery Phase](/t5/enterprise-resource-planning-blog-posts-by-members/the-importance-of-the-discovery-phase/ba-p/13567845)

![MJolton](https://avatars.profile.sap.com/1/c/id1c2ebf0b6c1708af5b6a7794e386b1593d5ff2d59bd45424f8c9c31b558bb20e_small.jpeg "MJolton")

[MJolton](https://community.sap.com/t5/user/viewprofilepage/user-id/134544)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68384)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68384)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567845)

‎2022 Dec 06
10:21 PM

[16
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68384/tab/all-users "Click here to see who gave kudos to this post.")

8,707

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)

View products (2)

One of the most overlooked, yet most important phases of a new S/4HANA Cloud implementation is the Discovery phase (which actually starts before the true implementation work).  SAP has recently taken a couple of actions that further highlight the importance of this phase.  So, let’s take a quick review of the Discovery Phase, why it is so important, and how SAP’s recent actions make it even more relevant going forward.

![](/legacyfs/online/storage/blog_attachments/2022/12/Activate-Screenshot.jpg)

SAP Roadmap Viewer Activate Screenshot

The overall purpose of the Discovery is to gain an understanding of the desired end state of an S/4HANA Cloud implementation by mapping the functionality of S/4HANA Cloud to the functional requirements of the business.  The assessment starts at the highest level, reviewing the company industry, countries of operation, number of legal entities per country, and estimated user counts.  From there, while not a detailed assessment, overall business requirements are reviewed to identify the S/4HANA Cloud scope items that address the various needs.  High-level gaps are identified where scope items are not available to address functionality.  Additional scrutiny must be placed on any financial and/or operational requirements that are industry specific, as scope items may be available but precisely how they work may not be sufficient.  Should any known extensions be required, they are noted and addressed at a high level.  Lastly, from a scope perspective, integrating systems are identified, along with the nature of the data and the data flows; this analysis will help determine if existing SAP Released APIs will likely support the integrations or if additional API development work is required.

Tangential to the functional analysis, but certainly as important is an assessment of what SAP calls, “Cloud Mindset.”  Part of the Solution Adoption workstream, this assessment will help determine user adoption risks and the propensity for the business users to accept SAP’s pre-configured “Best Practice” business processes, adapting the current business processes where required.  A Cloud Mindset requires the ability to rapidly adopt standard best practices and leverage cloud technology to engage in continuous innovation.

![](/legacyfs/online/storage/blog_attachments/2022/12/SAP-Cloud-Mindset.jpg)

SAP Cloud Mindset

Last but not least, while this work is going on, the business team can be getting more familiar with S/4HANA Cloud via a Cloud Trial system.  This “sandbox” experience will accomplish two key goals.  First, it will give the business users some relevant experience to help with the Cloud Mindset assessment.  Business users are better able to respond to questions about process change if they have at least some vision of what those changes would look like.  Second, this initial look at the system will help ready the business users for the more rigorous Fit-to-Standard sessions that lay ahead – again, giving them at least some idea of what the new system will look like so that they can focus on business requirements and not orienting to a new user experience.

![](/legacyfs/online/storage/blog_attachments/2022/12/SAP-S4HC-Trial.jpg)

SAP S/4HANA Cloud Public Edition 14 Day Trial

Clearly, the Discovery Phase can add a great deal of value to an implementation.  While not true design work, the Discovery scoping work is clearly necessary for effective project planning.  Similarly, the Cloud Mindset assessment and work with the Cloud Trial system will help ensure the business team is ready to move forward.  In addition, SAP has recently taken steps that add even more value to the Discovery Phase.

First, on October 4, 2022, SAP officially branded S/4HANA Cloud into a Public Edition and a Private Edition.  This clarity in the editions will promote Discovery phases that can be run prior to licensing, independent of the Public or Private Edition, allowing the actual business requirements to drive determination of the correct edition to license.

The second major change by SAP has to do with an SAP tool called the Digital Discovery Assessment tool.  This is a tool used by SAP and its implementation partners to document the Discovery findings and then assist in the determination of the correct edition.  The documentation acts as input into the more detailed Explore phase.  Now, however, SAP has ramped up the value of this tool even further in S/4HANA Cloud Public Edition implementations as the output, e.g. the selected scope items, can be exported and then imported into the SAP C-ALM and Central Business Configuration tools, eliminating double entry and jumpstarting the implementation.

![](/legacyfs/online/storage/blog_attachments/2022/12/DDA.jpg)

SAP Digital Discovery Assessment Tool

With the new capabilities of the Digital Discovery Assessment tool, and all of the other value derived from a strong Discovery phase, this often overlooked phase has now become a crucial first step in S/4HANA Cloud implementations.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fthe-importance-of-the-discovery-phase%2Fba-p%2F13567845%23comment-on-this)

Copy Link
![](https://commun...