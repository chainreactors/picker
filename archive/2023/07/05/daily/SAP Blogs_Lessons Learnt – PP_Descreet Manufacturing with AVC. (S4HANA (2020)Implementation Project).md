---
title: Lessons Learnt – PP_Descreet Manufacturing with AVC. (S4HANA (2020)Implementation Project)
url: https://blogs.sap.com/2023/07/04/lessons-learnt-pp_descreet-manufacturing-with-avc.-s4hana-2020implementation-project/
source: SAP Blogs
date: 2023-07-05
fetch_date: 2025-10-04T11:53:25.915296
---

# Lessons Learnt – PP_Descreet Manufacturing with AVC. (S4HANA (2020)Implementation Project)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Lessons Learnt - PP\_Discrete Manufacturing with AV...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68005&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Lessons Learnt - PP\_Discrete Manufacturing with AVC. (S4HANA (2020)Implementation Project)](/t5/enterprise-resource-planning-blog-posts-by-members/lessons-learnt-pp-discrete-manufacturing-with-avc-s4hana-2020/ba-p/13562295)

![manishaparulekar3](https://avatars.profile.sap.com/b/d/idbda411315c4346379943709740375dad09dc02794f1a1bc48ff470e096e65f52_small.jpeg "manishaparulekar3")

[manishaparulekar3](https://community.sap.com/t5/user/viewprofilepage/user-id/618966)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68005)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68005)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562295)

‎2023 Jul 04
8:56 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68005/tab/all-users "Click here to see who gave kudos to this post.")

3,128

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [PLM Variant Configuration](https://community.sap.com/t5/c-khhcw49343/PLM%2520Variant%2520Configuration/pd-p/411295671235448601330173655419575)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [PLM Variant Configuration

  Software Product Function](/t5/c-khhcw49343/PLM%2BVariant%2BConfiguration/pd-p/411295671235448601330173655419575)

View products (2)

**PURPOSE:** The idea behind this blog is to highlight some of the issues faced in SAP S4HANA PP module implementation for Discrete Manufacturing Scenario with Variant Configuration.

**SCENARIO****:** DTB Business Mapping in **brief**

Business/Client have Materials either MTS or MTO, not a combination i.e., same material cannot be MTS as well as MTO.

Standard SAP strategies as below were used for mapping MTS /MTO(VC)/MTO (Non-VC)

MTS-40(Planning with Final Assy) /

MTO(VC)-56(Characteristics Based Planning) /

MTO(Non-VC)-50(Planning without Final Assy).

95% of demand is from Sales forecast ​/Sales Forecasting is carried out in SAP Analytics Cloud which is then uploaded as PIRs

5% of SO have MTS items.

Then the Fast Track Order Requirement where once SO is entered system must automatically and immediately create Production Order.

For lower-Level assemblies and Components system will generate requirements post MRP run batch job every 5 min for ZFAS SO type.

Three Production Order types created

1. ZMTS (Strategy 40)

2. ZMTO (Strategy 50 and 56/SO type ZMTO (normal SO) /ZPM (Project SO) / ZPD (Internal Order related SO))

3. ZFAS (Strategy 50 and 56/SO type ZFAS (Fast Track SO))

# ***ISSUES & SOLUTIONS***

### ***Master Data Issues:***

**1.** For Variant Configuration (KMAT)Materials for Usage Probability, In Std SAP the Usage Probability is entered manually in MD61.It can be random number entered in MD61 Configuration Supporting points pop-up screen for VC materials.

We had requirement for automatic population of this Usage Probability or Planning Percentage.

### ***SOLUTION***

For this Business case - we captured these usage probability values/Planning % values in Characteristics - CT04 using classify value function using classification type 044.

Hence, we created Class/Characteristics and assigned the value to the individual Materials which had Planning % value in EBS system.

Usage Probability/Planning Percent can be entered even in BOM Alternate item group functionality. But the Requirement was that the Usage probability must not be taken into consideration for SO requirement of dependent components/ Assemblies with planning % and only must be calculated for the Forecast requirements i.e., PIRs hence had to look out for other options to hold this value.Hence in the Z Program for Forecast upload from SAC we have implemented the logic for populating this field automatically in ZMD61(CUSTOM FIORI \_\_ZDTB\_PIR upload).

For Detailed Solution of Usage Probability/Planning Percentage please refer to blog:

[https://blogs.sap.com/2023/06/16/variant-configuration\_s4-hana-custom-fiori-for-pir-upload-and-usage...](https://blogs.sap.com/2023/06/16/variant-configuration_s4-hana-custom-fiori-for-pir-upload-and-usage-probability-calculation/)

**2**. LTMC cannot be created for Upload of Planning Profile (Transaction MDP6 and MDPH).

Also, creation of LSMW is not possible to upload this data. The PRel(Planning Relevancy) Indicator has to be manually ticked for Multiple BOM Low level materials.

![](/legacyfs/online/storage/blog_attachments/2023/06/Planning-Profile.png)

MDP6-Planning Profile

### ***SOLUTION***

Created a Z Program to combine both MDP6 and MDPH transactions using Function module.BDC Recording was not used to build this program. Function Modules “REQUIREMENTS\_CHAR\_RELEVANZ” and “M60V\_PROFIL\_FOR\_PLAN” used to build this program. This standalone program Creates & Updates Planning profile.

**3**.  A configurable material can have multiple configuration profiles (as maintained with CU42). If there is only one configuration profile with Processing mode **Advanced Variant Configuration or AVC Profile**, everything works fine when configuring the material either in Solution Quotation or Sales Order.
If another configuration profile is added, with Processing mode **Classic**, and with lower priority than the previous AVC-mode profile, the Solution Quotation doesn't recognize the priority sequence, but claims that the product with Classic-mode cannot be processed there.

The same issue and error message remains even if the second profile(Classic Profile) is set to Locked status.

Sales Order (VA01/2) configuration works fine in this scenario using the highest priority profile, i.e. the AVC-flagged. So, it seemed that Solution Quotation has an error detecting both the Priority and the status Locked.

AVC profile is not supported for Usage Probability or Planning Percentage Calculation.

Due to this reason, we had 2 profiles AVC profile as Priority 01 and Classic Profile with Priority 02.

With Sales Order creation we had no issues, but with Solution Quotation, the System gives error in the creation of Solution Quotation as shown in below snapshot.

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-06-21-183906.png)

Error Message

### ***SOLUTION***

SAP Note 3053798 was implemented.

Also, the conclusion was that when we have Solution Quotation and AVC we need to have both the Classic as well as the AVC Profile.

The Classic Profile is required for the Usage Probability Calculation and for dependencies in BOM to work.

Whereas the AVC profile is required for the Solution Quotation to work.

### ***MRP LIVE ISSUES:***

1. MRP Live (MD01N) was used for VC (KMAT)Materi...