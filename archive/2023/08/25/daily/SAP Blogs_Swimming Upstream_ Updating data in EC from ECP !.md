---
title: Swimming Upstream: Updating data in EC from ECP !
url: https://blogs.sap.com/2023/08/24/swimming-upstream-updating-data-in-ec-from-ecp/
source: SAP Blogs
date: 2023-08-25
fetch_date: 2025-10-04T12:01:15.313826
---

# Swimming Upstream: Updating data in EC from ECP !

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Swimming Upstream: Updating data in EC from ECP !

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6673&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Swimming Upstream: Updating data in EC from ECP !](/t5/human-capital-management-blog-posts-by-sap/swimming-upstream-updating-data-in-ec-from-ecp/ba-p/13580594)

![rakesh](https://avatars.profile.sap.com/5/d/id5dd279246ddf038a5e6a34fd6215f0f791d74edc64e1e9db920ed88e66fd76fc_small.jpeg "rakesh")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[rakesh](https://community.sap.com/t5/user/viewprofilepage/user-id/7228)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6673)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6673)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580594)

‎2023 Aug 24
8:58 PM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6673/tab/all-users "Click here to see who gave kudos to this post.")

2,499

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central Payroll](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll/pd-p/67837800100800006744)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Employee Central Payroll, third-party data integration tool](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll%252C%2520third-party%2520data%2520integration%2520tool/pd-p/67837800100800007325)

* [SAP SuccessFactors Employee Central Payroll

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll/pd-p/67837800100800006744)
* [SAP SuccessFactors Employee Central Payroll, third-party data integration tool

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll%25252C%2Bthird-party%2Bdata%2Bintegration%2Btool/pd-p/67837800100800007325)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (4)

Greetings Solution Architects and ABAP Developers!

When I presented the program described below to my manager – a program designed to transfer data from ECP to EC – her remark was, "You're swimming upstream." That comment struck a chord. Today, I invite you to embark on a technical journey that echoes that feeling. We'll explore the process of "[upserting](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/c1330c5b2034472b909509fafcfe1471.html?state=DRAFT&q=batch)" Non-Recurring Pay Components in EC. Even though the process is straightforward, it can often feel counterintuitive as we're moving data from our well-understood downstream systems to their upstream counterparts.

It's worth noting that while our focus is on a specific use case, the underlying logic can be adapted to update various EC Employee data points. Whether it's updating the Payroll ID in the EC Employee Profile Compensation Portlet, the PayScale structure in the Job information of EC, or the Work Schedule in the Job Information of EC, the methodology remains robust.

Lastly, while the journey ahead is charted in ABAP, the principles are transferrable. Whether you're operating in another programming language or using tools like Postman(shown below), the roadmap to successful upserting remains consistent. I am hoping that you are aware of what is OData API. If not, please read [SAP SF OData APIs(V2).](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/03e1fc3791684367a6a76a614a2916de.html?state=DRAFT)

![](/legacyfs/online/storage/blog_attachments/2023/08/postman_upsert_authorization.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/postman_upsert.png)

In this guide, we'll illustrate how to achieve our objectives using an ABAP Program. Note that this ABAP code is basically a part of larger program, so I am just presenting and sharing the upsert process. You can refine and enhance this program with proper error handling based on your specific needs. To provide a clearer understanding of our approach, here's an overview of our data flow:

The customer has a distinct compensation planning process that demands a robust program to determine employee bonuses. Given specific dependencies, ECP was selected as the platform for these calculations. The challenge we encountered was ensuring that EC received the latest bonus data, which would subsequently update ECP. This procedure is divided into three distinct steps:

Step 1: Our primary topic of discussion.
Step 2: A standard PTP replication between EC and ECP.
Step 3: The usual payroll run process.
For this discussion, we'll delve deeply into Step 1, but it's vital to see how it fits into the broader process.

![](/legacyfs/online/storage/blog_attachments/2023/08/bonus-flow.png)

#### **Data Declarations**:

A set of data variables and constants are defined for handling various parts of the request and response cycle, such as:

* gv\_uri: The URI for the OData request.

* gv\_payload: The payload for the HTTP request.

* Data and string types for dates and other values.

* JSON-related data types and references for handling JSON responses.

```
DATA: gv_uri             TYPE string,

      gv_payload         TYPE string,

      go_client          TYPE REF TO cl_http_client,

      ldate              TYPE d,

      sdate              TYPE d,

      edate              TYPE d,

      date_str           TYPE string,

      sdate_str          TYPE string,

      edate_str          TYPE string,

      sum_tabix          TYPE i,

      str_bonus          TYPE string VALUE '                    ', " Initialized to 20 spaces

      http_client_instance TYPE REF TO any, " Replace 'any' with the actual class type

      request_payload    TYPE string,

      response_data      TYPE string,

      json_data_root     TYPE REF TO /ui2/cl_json,

      json_data_node     TYPE REF TO any, " Replace 'any' with the appropriate class or data type

      lv_seqnr           TYPE zuspy_dg_sb_log-seqnr,

      field_ref          TYPE REF TO data,

      val_ref            TYPE REF TO data,

      lv_abap_date       TYPE d,

      lv_date_in_milliseconds TYPE n LENGTH 13,

      str_date           TYPE string,

      lv_result_string   TYPE string,

      lv_seconds_since_epoch TYPE p DECIMALS 0,

      c_e...