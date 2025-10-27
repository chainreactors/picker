---
title: Variant Configuration_S4 HANA Custom FIORI for PIR Upload and Usage Probability Calculation
url: https://blogs.sap.com/2023/06/16/variant-configuration_s4-hana-custom-fiori-for-pir-upload-and-usage-probability-calculation/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:46:58.126525
---

# Variant Configuration_S4 HANA Custom FIORI for PIR Upload and Usage Probability Calculation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Variant Configuration\_S4 HANA Custom FIORI for PIR...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67073&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Variant Configuration\_S4 HANA Custom FIORI for PIR Upload and Usage Probability Calculation](/t5/enterprise-resource-planning-blog-posts-by-members/variant-configuration-s4-hana-custom-fiori-for-pir-upload-and-usage/ba-p/13550777)

![manishaparulekar3](https://avatars.profile.sap.com/b/d/idbda411315c4346379943709740375dad09dc02794f1a1bc48ff470e096e65f52_small.jpeg "manishaparulekar3")

[manishaparulekar3](https://community.sap.com/t5/user/viewprofilepage/user-id/618966)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67073)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67073)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550777)

‎2023 Jun 16
3:02 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67073/tab/all-users "Click here to see who gave kudos to this post.")

3,140

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [PLM Variant Configuration](https://community.sap.com/t5/c-khhcw49343/PLM%2520Variant%2520Configuration/pd-p/411295671235448601330173655419575)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [PLM Variant Configuration

  Software Product Function](/t5/c-khhcw49343/PLM%2BVariant%2BConfiguration/pd-p/411295671235448601330173655419575)

View products (2)

In this blog, I would like to explain how we built a custom FIORI to capture the Usage Probability values automatically in MD61(FIORI- Create PIR) and its advantages over the standard SAP FIORI-MAINTAIN PIRs.

The BOM's with huge number of components which have a Usage Probability value, it becomes difficult for the planners to enter these values manually in MD61 transaction. Hence it would reduce the laborious task for planners to enter these values manually whilst creating the PIRs.

To begin with, let me give an example of the Usage Probability or Planning Percentage value, the low-level components for a given sub-assembly (KMAT Material) can have varying demands, and the business meets these requirements by entering the Usage probabilities (Planning Percentages) in Create PIR or Tcode MD61. MRP plans the low level components with Usage Probability value as shown in below diagram.

A demand for the low level buy/make components must generate the Purchase Requisitions/Planned Orders as per the Usage Probability/Planning Percentage value post MRP run.

![](/legacyfs/online/storage/blog_attachments/2023/05/Screenshot-2023-05-13-190736.png)

Usage Probability/Planning Percentage Business concept

Below diagram explains the 2 parts in the Custom FIORI\_ZDTB\_PIR\_Upload

![](/legacyfs/online/storage/blog_attachments/2023/05/Flow-of-_PIR-upload_FIORI.png)

**Part1** *Upload the Excel file for the PIRs*

These values maybe download from SAC as shown or any other Interface or may be built in Excel itself. Program designed for upload of 36 months data.

The Forecast file (Excel file) will be uploaded with Custom FIORI\_ZDTB\_PIR\_UPLOAD. The Splitting of the Requirements from monthly to daily is carried out by the program, this can be changed to weekly/quarterly as per requirement.

**Part 2** *Capturing the Usage Probability/Planning Percentage Value*. The logic in the Z-Program will help to capture the Usage Probability value stored in Characteristic field in the classification tab of Material Master. The Requirement type will be automatically captured in the program. If the material is not a KMAT material type, there will be no pop-up for Usage probability.

The Advantages of the Custom FIORI "Upload Planned Independent Requirement" over the Standard SAP FIORI "Maintain PIR" are as shown in below diagram.

![](/legacyfs/online/storage/blog_attachments/2023/05/Comparison-of-Std-SAP-to-Custom-FIORI-2.png)

Maintain PIR v/s ZDTB Upload PIR

**Prerequisite & Process Flow**

1. Classic Mode Configuration Profile

2. Planning Percentage Master data                                                                                               MDP1 - Create Planning Table                                                                                                MDP4 - Maintain Combinations                                                                                           MDP6 - Create Planning Profile                                                                                                    CT04 - Maintaining Planning Percentage Value in Characteristics using Classify Value Function

3. Demand / Forecast Upload using Transaction – ZDTB\_PIR\_UPLOAD or FIORI “**Upload Planned Independent Requirement.**”

4. Evaluate Planning % Value on Dependent requirement demand.

**1. Classic Mode Configuration Profile – FIORI – “Display Configuration Profile” (CU43)**

The classic Mode Configuration Profile is a mandatory Master data for Usage Probability/Planning Percentage functionality.

If Advanced Variant Configuration  has been activated, then both Configuration profiles need to be created.

The Classic configuration profile for Usage Probability/Planning Percentage solution to work.

And the Advanced Variant Configuration profile for normal Made To Order (MTO) scenarios.

Hence 2 profiles as shown below![](/legacyfs/online/storage/blog_attachments/2023/05/Cofiguration-Profile.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/config-profile-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/config-profile-3.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/config-profile-4.png)

Similarly create AVC profile for the material as below![](/legacyfs/online/storage/blog_attachments/2023/05/AVC-profile.png)

**2.Planning Percentage Master data**

**1.MDP1-Create Planning Table/** **FIORI** -**Create/Change/Display Combination structure**              ID – **MDP1, MDP2, MDP3**

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP1_1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP1_2-1.png)

**2.MDP4 - Maintain Combinations /** **FIORI – Maintain Combination Structure**

**ID – MDP4**

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP4_1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP4_2.png)

**3. MDP6 – Create Planning Profile**

**FIORI – Modeling , Planning Profile**

**ID – MDP6, MDPH**

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP6_1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/MDP6_2.png)

**Step by Step procedure to capture Planning % in SAP using SAP Feature “Classify Value”.**

Below steps are one time process as Master data load.

**Step 1: -**

Create Class with Type -044,

Then, Assign Characteristic created to Class Type -044

Go to Transaction **CL01**,

Input “**PLANNING\_PERCENTAG**” Class with Class Type - **044** and pres...