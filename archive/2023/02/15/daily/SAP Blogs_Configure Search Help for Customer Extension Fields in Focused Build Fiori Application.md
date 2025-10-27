---
title: Configure Search Help for Customer Extension Fields in Focused Build Fiori Application
url: https://blogs.sap.com/2023/02/14/configure-search-help-for-customer-extension-fields-in-focused-build-fiori-application/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:37:05.295398
---

# Configure Search Help for Customer Extension Fields in Focused Build Fiori Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Configure Search Help for Customer Extension Field...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/150011&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Configure Search Help for Customer Extension Fields in Focused Build Fiori Application](/t5/technology-blog-posts-by-sap/configure-search-help-for-customer-extension-fields-in-focused-build-fiori/ba-p/13527645)

![cgovind](https://avatars.profile.sap.com/0/6/id0665de18c66e74790f40f57e82234551f604a20c623781579e46202799f5ba78_small.jpeg "cgovind")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[cgovind](https://community.sap.com/t5/user/viewprofilepage/user-id/145886)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=150011)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/150011)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13527645)

‎2023 Feb 14
11:23 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/150011/tab/all-users "Click here to see who gave kudos to this post.")

5,223

* SAP Managed Tags
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (1)

This blog post in continuation to the earlier [blog post](https://blogs.sap.com/2022/02/17/search-and-maintain-customer-extension-fields-from-focused-build-fiori-application/?preview_id=1489424) where I explain, how the Customer Extension fields can be maintained in a Focused Build Application. In this blog post, I will walk through the steps required to enable the Value help for the Extension fields.

To follow this blog post, the user needs to have some knowledge in SAP CRM Application Enhancement Tool, Focused Build Requirement Fiori Application.

This blog post is relevant for Focused Build Solution Consultants, and Customers who would like to extend the Fiori Application with the SAP CRM Extension Fields.

The user should have some technical know-how in ABAP to build and configure the custom search help.

### **Scope of this Feature**

This extension feature is supported only from [Focused Build for Solution Manager SP09](https://support.sap.com/content/dam/support/en_us/library/ssp/alm/sap-solution-manager/focused-solutions/Focused_Build/sp09/FB_SP9_delta.pdf) Release.

In SP09 and SP10 releases, the extension field feature is only supported for the Requirement Management and My Requirements Fiori Application Application.

In addition to the above two applications, starting SP11 release, the Extension field feature is also supported in Mass Change Application for Requirements Process Type.

Starting SP13 release, the extension fields are now supported across all the Focused Build process types and related Fiori applications.

Kindly refer to the [blog post](https://blogs.sap.com/2023/02/06/focused-build-sp11-improvements-in-mass-change-operations-app-mca-for-requirements/) to know more about the extension field capabilities in Mass change application.

### **Limitations of the Search Help**

Collective Search Help is not currently supported.

Only Elementary ABAP Search Help is currently supported.

Elementary Search Help has to be mandatorily be provided to enable the Search Help although the field might have an underlying Value Table defined under its domain.

Earlier to SP13 release, extension fields with domain fixed values require search help to display the fixed values configured under the domain. Starting SP13 release, search help is not required to display the underlying domain with fixed values.

### **Configure the Search Help for the Extension Field**

I would provide few Search Help examples to explain the concept and the steps required to configure the Search Help for the Extension field.

Let us take the below example where we add a Business Partner Extension field to the Requirement Management Application. Let us assume the Customer needs a Business Partner Extension Field to capture the Product Lead details in the Requirement.

Kindly follow the below steps to add the Business Partner Extension field and check the earlier [blog post](https://blogs.sap.com/2022/02/17/search-and-maintain-customer-extension-fields-from-focused-build-fiori-application/?preview_id=1489424) if you happen to hit any road block while following the steps.

1. Open an existing Focused Build Requirement from the My Requirements Fiori Application.![](/legacyfs/online/storage/blog_attachments/2022/04/Screenshot-2022-04-17-at-9.27.36-PM.png)

2. Navigate to the CRM Web UI Application from the My Requirements Fiori Application by clicking on the Requirement Description. Choose the Architect Business Role or any suitable Business used to generate and add the Business Partner Extension field.![](/legacyfs/online/storage/blog_attachments/2022/04/Screenshot-2022-04-17-at-9.30.49-PM.png)

3. Add the Business Partner Extension field to the CUSTOMER\_H Business Object and assign the standard Search Help BUPAP. The extension field semantics are determined from the data element.![](/legacyfs/online/storage/blog_attachments/2022/04/Screenshot-2022-04-17-at-9.32.38-PM.png)

4. Save and Generate the Extension field.

5. Generate the Field Control Properties for the Product Lead if you have already performed this step using the report - "/SALM/GEN\_CUSTFLD\_UXFC\_APPEND". This step is not a pre-requisite to configure the value help.  However, it is required to maintain the extension field. Refer the previous [blog post](https://blogs.sap.com/2022/02/17/search-and-maintain-customer-extension-fields-from-focused-build-fiori-application/?preview_id=1489424) to know more about this step.![](/legacyfs/online/storage/blog_attachments/2022/04/Screenshot-2022-04-20-at-12.49.54-AM.png)

6. Configure the Extension Field using the transaction /SALM/CUSTFLD for the transaction type S1BR.

   * In this example, I am using the standard elementary search help BUPAP to configure the search help for the Product Lead field.

   * Maintain the Value Help BUPAP, the elementary search help for the Extension Field.

   * ![](/legacyfs/online/storage/blog_attachments/2023/02/Screenshot-2023-02-14-at-12.07.34-AM.png)

   * Maintain the field VH\_FLD\_MAPPING, as the field from the Elementary Search Help that would map to the Product Lead field on selecting a record from the Value Help. In this case on selecting a Business Partner from the Value Help, the Business Partner ID would be returned and mapped to the Product Lead Field.

   * Maintain the field VH\_FLD\_TEXTMAP, as the field that would serve as the Description for the Product Lead Field. We will cover the capabilities of this field in a separate blog post. This is an optional field an...