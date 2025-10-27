---
title: Integrating SAP Commerce and SAP Emarsys using Cloud Integration
url: https://blogs.sap.com/2022/10/28/integrating-sap-commerce-and-sap-emarsys-using-cloud-integration/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:23.131118
---

# Integrating SAP Commerce and SAP Emarsys using Cloud Integration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Integrating SAP Commerce and SAP Emarsys using Clo...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/12963&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrating SAP Commerce and SAP Emarsys using Cloud Integration](/t5/crm-and-cx-blog-posts-by-sap/integrating-sap-commerce-and-sap-emarsys-using-cloud-integration/ba-p/13553952)

![D_Pietroniro](https://avatars.profile.sap.com/4/a/id4a778ea249d2aae0f568389e14f7ab3eef639167c19b16966ab4250babbd96eb_small.jpeg "D_Pietroniro")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[D\_Pietroniro](https://community.sap.com/t5/user/viewprofilepage/user-id/41820)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=12963)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/12963)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553952)

‎2022 Oct 28
7:05 PM

[7
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/12963/tab/all-users "Click here to see who gave kudos to this post.")

4,219

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Emarsys Commerce Cloud Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys%2520Commerce%2520Cloud%2520Integration/pd-p/eaaffcef-f085-4369-80ca-7016d6fd1c1a)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [Customer Experience](https://community.sap.com/t5/c-khhcw49343/Customer%2520Experience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)
* [SAP Emarsys](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys/pd-p/73554900100800003661)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Customer Experience

  Topic](/t5/c-khhcw49343/Customer%2BExperience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Emarsys Commerce Cloud Integration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BEmarsys%2BCommerce%2BCloud%2BIntegration/pd-p/eaaffcef-f085-4369-80ca-7016d6fd1c1a)
* [SAP Emarsys

  Software Product](/t5/c-khhcw49343/SAP%2BEmarsys/pd-p/73554900100800003661)

View products (5)

# Introduction

This blog post is part of a series of blogs demonstrating how to feed data on the SAP Emarsys from SAP Commerce.

In this part, I demonstrate the developments on the SAP CPI that receives the customer data from SAP Commerce, does the necessary transformations and enrichments, then send it to SAP Emarsys.

My colleague 555786 wrote a great blog showing how to [enable this integration on the SAP Commerce Cloud.](https://blogs.sap.com/2022/11/08/integration-between-sap-commerce-cloud-and-cpi-using-integration-object-one-case-with-emarsys/)

# TLDR

The SAP CPI package with all the artifacts can be downloaded on [GitHub](https://github.com/pietronirod/commerce_emarsys_contacts).

# Process Flow

This blog demonstrates the following process:

1. A customer is created on the SAP Commerce, triggering an event;

2. This event starts a job that sends the customer data to an iFlow on the SAP Cloud Integration through an HTTP post;

3. This first iFlow transforms the data to the SAP Emarsys expected format and stores it on a JMS queue, making this replication process asynchronous;

4. A second iFlow pools the JMS queue, fetch the data, and calls a third iFlow. This last iFlow is responsible for generating the HTTP Header WSSE necessary to authenticate in the SAP Emarsys tenant;

5. The data is sent to the SAP Emarsys tenant.

This diagram briefly shows the process described above.

# ![](/legacyfs/online/storage/blog_attachments/2022/10/Communication_flow.png)

# Preparation

## Import of Digital Certificates

The communication between the SAP Commerce, SAP CPI, and SAP Emarsys tenants use the HTTPS protocol.

The following steps are necessary to acquire and import the digital certificates on the SAP CPI tenant:

1. Go to the Connectivity Tests app on the Integrations Monitor.
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_001.png)

2. Enter **api.emarsys.net**on the host, uncheck the **Valid Server Certificate Required,**and click on Send button;
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_002.png)

3. Download the digital certificate chain locally;

4. Decompress the ZIP file locally;

5. On the SAP CPI, open the Keystore app;
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_004.jpg)

6. Click on Add, Certificate;
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_005-1-scaled.jpg)

7. In the popup, click on browse and select the file on the image. This file is the root certificate and the only one necessary to establish the HTTPS connection between SAP CPI and SAP Emarsys;
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_003-1.jpg)

8. Execute steps 1 and 2 again, but with the flag, Valid Server Certificate Required checked. You must see a successful response.![](/legacyfs/online/storage/blog_attachments/2022/10/Import_Digital_Certificates_006-1-scaled.jpg)

## Creation of Security Materials

As described in the [SAP Emarsys API documentation](https://dev.emarsys.com/docs/emarsys-api/ZG9jOjI0ODk5NzAx-authentication), their API requires a WSSE authentication. For this reason, I created the Emarsys security material with the user and password provided by the SAP Emarsys tenant administrator.

# Integration Flows

As mentioned in the Process Flow, I created three iFlows:

## 1. Receive Contacts from SAP Commerce

This iFlow receives the customer data from SAP Commerce, transforms this customer data to the SAP Emarsys contact data format, and stores the data on a JMS queue.

![](/legacyfs/online/storage/blog_attachments/2022/10/Receive_from_Commerce_001.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Receive_from_Commerce_004-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Receive_from_Commerce_005.png)

The iFlows proceed as follows:

1. SAP Commerce sends the customer data using the HTTPS protocol (method POST). Just for simplicity, I disabled the CSRF protection;
   ![](/legacyfs/online/storage/blog_attachments/2022/10/Receive_from_Commerce_002-1.png)

2. The Set Parameters step creates two parameters, SourceAgency and TargetAgency, in case of a value mapping usage;

3. The generic Mapper step is a script that converts the customer data to the contact data format. It uses the POGOs concept described in [Eng Swee Yeoh's blog](https://blogs.sap.com/2018/03/15/modularising-cpi-groovy-scripts-using-pogo/);

4. Then the data is sent to a JMS queue, making the replication process asynchronous, as explained on [Mandy Crimmel's bl...