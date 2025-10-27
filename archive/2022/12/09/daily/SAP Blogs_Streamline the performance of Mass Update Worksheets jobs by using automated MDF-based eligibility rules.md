---
title: Streamline the performance of Mass Update Worksheets jobs by using automated MDF-based eligibility rules
url: https://blogs.sap.com/2022/12/08/streamline-the-performance-of-mass-update-worksheets-jobs-by-using-automated-mdf-based-eligibility-rules/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:56.080195
---

# Streamline the performance of Mass Update Worksheets jobs by using automated MDF-based eligibility rules

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Streamline the performance of Mass Update Workshee...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6399&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Streamline the performance of Mass Update Worksheets jobs by using automated MDF-based eligibility rules](/t5/human-capital-management-blog-posts-by-sap/streamline-the-performance-of-mass-update-worksheets-jobs-by-using/ba-p/13571404)

![xavierlegarrec](https://avatars.profile.sap.com/e/1/ide191ffbd1506acbea27fa713f7d40cc166155c1a67fd472acb8c46fa0863e44a_small.jpeg "xavierlegarrec")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[xavierlegarrec](https://community.sap.com/t5/user/viewprofilepage/user-id/20879)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6399)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6399)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571404)

‎2022 Dec 08
7:05 PM

[22
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6399/tab/all-users "Click here to see who gave kudos to this post.")

2,298

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (2)

**Introduction**

A few customers with large numbers of employees in compensation worksheets (15k+) have reached out to SAP Professional Services recently to try to find a solution to a persistent issue impacting their review cycle : when first applying their eligibility rules or when running the daily "Mass Update Worksheets" job it takes 10+ hours for the job to finish running (*please note that since this blog was written in December 2022 the product team enhanced the performance of these jobs in 2H 2023 - see [recording #3 of this blog](https://blogs.sap.com/2023/10/21/2h-2023-for-compensation-must-know-new-features/) - however we still think there are many cases in which they would take many hours to run despite these enhancements and that the content below is still valid).*

Beyond making sure that the rules built under Plan Setup > Plan Details > Eligibility are streamlined (as few rules as possible is recommended because every new rule will increase job processing times by 1.5 / also the use of [Variables](https://blogs.sap.com/2020/09/02/compensation-eligibility-rules-lesser-known-rule-conditions-and-overall-limitations/) is recommended), there is a way to automate eligibility rules through MDF objects that is incredibly efficient and can bring down job run times from 14 hours to less than 4 hours.

It was the case for a customer I worked with recently that has 300,000 active users and 700,000 inactive users in their production environment : these statistics matter as much as the number of employees on worksheets (35,000 for this customer) or the number of worksheets (9,000 for this customer) because when regular compensation eligibility rules run they always run on the whole UDF including inactive users - even if "Include inactive users" is unchecked in Plan Setup > Define planners).

**Eligibility rules based on automated MDF objects**

Discover in the recording below how to set up not only the custom MDF object but also all business rules and integration center jobs that will enable us to fully replace the regular compensation eligibility rules with a custom MDF Object without any loss of functionality and without having to do any CSV upload.

Credits go to [Phil MacGovern](https://blogs.sap.com/2022/07/06/using-standard-eligibility-flags-in-an-ec-integrated-compensation-template/) for paving the way for this design.

* The first 5-6 minutes are dedicated to building the starting situation and expectations.

* The new MDF eligibility design demo starts at 6'50.

* The first demo of how the custom object for eligibility gets populated "On Save" by the business rules tied to it starts at 21'23.

<https://youtu.be/On0NABPNnpw>

**Notes about this MDF based eligibility design and the recording**

In the recording contrarily to what I mention I only take care of greying out the Merit column with the new MDF based design for employee Alexander Ruuid. To also grey out the Promotion and the Adjustment columns with that same design I would have needed to create two more fields in the custom MDF object (promotionEligible and extraEligible) as well as 2 more "set" conditions in my existing business rule (no need for a new one in this case since the criteria for ineligibility is the same than for Merit).

The only drawback of this MDF design for eligibility rules vs existing Eligibility rules has to do with the Integration Center which is usually only accessible to full System Admins and not just to Comp Admins. So just like for Executive Review access changes (RBP) Comp Admins would need to reach out to System Admin in case they need to trigger the integration center job manually (in case they cannot wait for the daily or semi-daily job to run). Please note however that we could have the job scheduled every 2 or 3 hours as a workaround (or simply run an UDF export or Adhoc report providing all UserIDs then mass reimport all these UserIDs into the MDF through "Import and Export data"). Usually integration center jobs are very fast (10 minutes max for 200,000 active employees in an environment in my experience).

**Conclusion**

I personally love this design not only because it allows customers to improve performance but also because it allows us to breakdown the complexity of the rules : we could for example build the MDF in a way that a user is marked as compensationEligible=TRUE only if MDF field A (Eligibility based on Country)=YES + MDF field B (Eligibility based on Pay Grade) =YES + C=YES+ D=YES, ... which makes it incredibly easy to troubleshoot eligibility issues. See the discussion [here](https://blogs.sap.com/2023/10/16/preparing-ec-for-compensation-implementation-success/#comment-697304) for a recent business case for this (Comp eligibility reports that need to be used by GenAI and Chatbots for interaction with planners). I've attached a screenshot of one of the MDF eligibility reports [here](https://drive.google.com/file/d/1xBWj-xveH7Cnrx48elr4dDtRTtIjeqGC/view?usp=sharing). Please see this document for [Pros and Cons](https://drive.google.com/file/d/1K3R3BEKdQeFO-yrD-jneJI_LZpPWNOL6/view?usp=sharing) of using MDF objects vs Compensation ...