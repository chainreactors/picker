---
title: How to setup Time Evaluation in Time Tracking
url: https://blogs.sap.com/2022/10/20/how-to-setup-time-evaluation-in-time-tracking/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:26.792242
---

# How to setup Time Evaluation in Time Tracking

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* How to setup Time Evaluation in Time Tracking

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5507&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to setup Time Evaluation in Time Tracking](/t5/human-capital-management-blog-posts-by-sap/how-to-setup-time-evaluation-in-time-tracking/ba-p/13545654)

![TB](https://avatars.profile.sap.com/f/8/idf8a8c2d104bd9e7cabdb621d0ea7f18451ce35a279f5360c1b6a5c58e24d53f1_small.jpeg "TB")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[TB](https://community.sap.com/t5/user/viewprofilepage/user-id/20637)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5507)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5507)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545654)

‎2022 Oct 20
6:36 PM

[66
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5507/tab/all-users "Click here to see who gave kudos to this post.")

46,081

* SAP Managed Tags
* [SAP SuccessFactors Employee Central Payroll](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll/pd-p/67837800100800006744)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Time Tracking](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Time%2520Tracking/pd-p/73555000100800002827)
* [SAP Timesheet](https://community.sap.com/t5/c-khhcw49343/SAP%2520Timesheet/pd-p/01200615320800003662)
* [HCM Time Management](https://community.sap.com/t5/c-khhcw49343/HCM%2520Time%2520Management/pd-p/666118459887932219928019980895838)

* [SAP SuccessFactors Employee Central Payroll

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll/pd-p/67837800100800006744)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Time Tracking

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BTime%2BTracking/pd-p/73555000100800002827)
* [SAP Timesheet

  SAP Timesheet](/t5/c-khhcw49343/SAP%2BTimesheet/pd-p/01200615320800003662)
* [HCM Time Management

  Software Product Function](/t5/c-khhcw49343/HCM%2BTime%2BManagement/pd-p/666118459887932219928019980895838)

View products (5)

# Why should I read this blog post?

Time Evaluation is needed to process recorded times in a way to calculate overtime premiums, shift premiums, working time account or overtime account balances, to create alerts and warnings if employees have times outside their planned hours, outside the flextime bandwidth, if they record more than 10hours per day and many more reasons. Successfactors Time Evaluation provides you a very flexible way to create time valuation rules to accommodate your company agreements, trade union contracts or even processes that are derived from laws and regulations like the European Directive on working time.

Time Evaluation might be easy – but can also be complex. This depends on the business processes you want to cover. This blog describes the mechanism of the Successfactors Time Evaluation and each time valuation type in more detail in order to give some hints and help you to decide which valuation type to be used in what constellation.

Target readers are time management consultants who want to learn more on the configuration of Successfactors Time Evaluation.

# Discover the Latest Updates from September 3, 2025

We're excited to share a new blog post that dives deeper into the process of time valuation! If you're looking to understand how to come from a requirement to a solution, check out our latest blog post: ["From Requirement to Configuration: Your Guide to Time Valuation in SAP SuccessFactors Time Tracking...](https://community.sap.com/t5/human-capital-management-blog-posts-by-sap/from-requirement-to-configuration-your-guide-to-time-valuation-in-sap/ba-p/14196781) It's packed with practical tips and insights to help you navigate this crucial aspect of implementing our Time Valuation.

# Discover the Latest Updates from October 18, 2024: Introducing Time Containers and new Valuation Types

In the latest update of this blog post, we have made some small corrections and added the description of time containers and new valuation types that will greatly enhance your possibilities. Check it out now!

# **Time Evaluation**

## **Definitions**

Time Evaluation is a valuation of attendance, break, oncall and absence times by comparing the recorded hours against the company-internal, contractual, and collective agreement provisions.
Time Evaluation runs periodically to calculate overtime, calculate time off in lieu postings and working time accounts (flextime), validate attendance recordings, and calculate wage types (for example, bonuses) for payroll.

+ Time Evaluation is the process of calculating valuation results from a set of input time records to generate an output time record.

+ An output time record can be an interim calculation result or an time valuation result

+ Input time records, output time records and the valuation results are represented by time type groups.

+ The complete Time Evaluation contains several small calculation steps with time type groups as input and output. These steps are called time valuations and are combined in a time recording profile.

## **D****efinition** **by** **Example**

![Time Valuation - Definition by Example](/t5/image/serverpage/image-id/182700i9A1288A412D556D9/image-size/large?v=v2&px=999 "01 definition by example.jpg")Time Valuation - Definition by Example

# Basics

## **Time Type Groups – General** **and** **Usage**

+ General
  - Time type groups are containers for interim calculation results and final time pay types.
  - Output of time valuations that can be displayed on the Time Sheet UI.UI Component

+ Time Pay Type
  - The calculated time valuation results are stored on the database and available either for payroll processing or conversion to time off in lieu or working time account.
+ Time Collector
  - Calculated time valuation result which is aggregated daily, weekly, or monthly and stored on the database.
+ Time Container
  - ![:warning:](/html/@FEA4F6128ED5C2F6F3ED3ECB50778D1E/emoticons/26a0.png ":warning:")Time Tracking subscription necessary
  - Calculated time valuation result which is aggregated daily or for a period and stored on the database. Daily Time Container, e.g. created by an Aggregation time valuation, can be read from database by a Time Type Group of Time Category “Time Container”. They can be used for periodically calculations and result in periodical Time Containers. These periodically calculations are processed asynchronously.

## **Usage and Stor...