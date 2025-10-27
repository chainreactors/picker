---
title: Alerts for Payment Information: Full step-by-step guide
url: https://blogs.sap.com/2023/03/31/alerts-for-payment-information-full-step-by-step-guide/
source: SAP Blogs
date: 2023-04-01
fetch_date: 2025-10-04T11:20:54.712471
---

# Alerts for Payment Information: Full step-by-step guide

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Alerts for Payment Information: Full step-by-step ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5059&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Alerts for Payment Information: Full step-by-step guide](/t5/human-capital-management-blog-posts-by-members/alerts-for-payment-information-full-step-by-step-guide/ba-p/13561894)

![Narendra_Prasath_Parthiban](https://avatars.profile.sap.com/5/c/id5c298864d0072dd281ff3ceb213878b5d438f4445f6465ecee152535df6c793a_small.jpeg "Narendra_Prasath_Parthiban")

[Narendra\_Prasath\_Parthiban](https://community.sap.com/t5/user/viewprofilepage/user-id/127521)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5059)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5059)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561894)

‎2023 Mar 31
9:37 PM

[10
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5059/tab/all-users "Click here to see who gave kudos to this post.")

6,552

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)

View products (3)

### **Introduction**

In this blog, I would like to introduce the automatic alerts for payment information when employee fails to provide the payment details. In this process, we will not change the existing configuration such as rules, field details and permissions in the Payment information and details object.

The following steps has been taken in order to achieve this configuration

+ Custom MDF objects (Lookup table)

+ Business rules

+ Integration Center - Job

### **Custom MDF Objects (Lookup table)**

Create a custom MDF object > Configure Object definition > Create New

***Basic Configurations in Object Definition***

|  |  |
| --- | --- |
| **Code** | PaymentInformationCheck |
| **Effective dating** | None |
| **API Visibility** | Editable |
| **Label** | Payment Information Check |

You can use the default settings for the rest of the configuration.

![](/legacyfs/online/storage/blog_attachments/2023/03/A01.jpg)

Object Definition

***Field details***

|  |  |  |  |
| --- | --- | --- | --- |
| **ID** | **Date type** | **Visibility** | **Label** |
| externalCode | User | Read only | Employee |
| externalName | Boolean | Read only | Is Payment Information exits? |

![](/legacyfs/online/storage/blog_attachments/2023/03/A2.jpg)

Field details

***Security***

The object will not be shown in employee profile, so we are not securing it.

![](/legacyfs/online/storage/blog_attachments/2023/03/A3.jpg)

Security

### **Business rules**

Create the business rules: Configure Business Rules > Create New Rule > Rules for MDF Based Objects >

***Rule 01***

|  |  |
| --- | --- |
| **Base Object** | Payment Information Check |
| **Purpose** | Evaluate |

The below rule pulls employee payment information and brings it to the custom MDF (Payment Information Check)

![](/legacyfs/online/storage/blog_attachments/2023/03/B1.jpg)

This rule which fetch the Payment information exist data.

***Rule 02***

|  |  |
| --- | --- |
| **Base Object** | Payment Information Check |
| **Purpose** | Alert |

In this rule, the alerts will be triggered for employees without payment information.

+ Alert Message

![](/legacyfs/online/storage/blog_attachments/2023/03/B2.jpg)

Manage data - Create New - Alert Message

+ Workflow

![](/legacyfs/online/storage/blog_attachments/2023/03/B3.jpg)

Manage Organisation, Pay and Job Structure - Create New - Workflow

+ Rule

![](/legacyfs/online/storage/blog_attachments/2023/03/B5.jpg)

The rule triggers alerts when an employee does not maintain payment information

Attach both the rules on the Payment Information Check object.

![](/legacyfs/online/storage/blog_attachments/2023/03/B6.jpg)

Attach these two rules on the Payment Information Check (Onsave)

### Integration Center - Job

Create a Integration Center - Job using below steps:

Go to Integration Center ==> My Integrations ==> Create ==> More Integration Types

![](/legacyfs/online/storage/blog_attachments/2023/03/I1.jpg)

Step: 1 - Go to Integration Center

![](/legacyfs/online/storage/blog_attachments/2023/03/I2.jpg)

Step:2 Choose Integration Types

![](/legacyfs/online/storage/blog_attachments/2023/03/I3.jpg)

Step:3 Select the Source Object

![](/legacyfs/online/storage/blog_attachments/2023/03/I4.jpg)

Step:4 Options

![](/legacyfs/online/storage/blog_attachments/2023/03/I5.jpg)

Step:5 Configure Fields

![](/legacyfs/online/storage/blog_attachments/2023/03/I6.jpg)

Step:6 Destination Object

![](/legacyfs/online/storage/blog_attachments/2023/03/i7-1.jpg)

Step:7 Adding the Destination Object

![](/legacyfs/online/storage/blog_attachments/2023/03/I9.jpg)

Step: 8, 9 Mapping the Source and Destination Object

![](/legacyfs/online/storage/blog_attachments/2023/03/I10.jpg)

Step:10 Scheduling

![](/legacyfs/online/storage/blog_attachments/2023/03/I11.jpg)

Step: 11 Save and Exit

### **Outcome**

There will be alerts and notifications sent to the Employee after the successful completion of the Integration job run.

+ You can check the payment information exist data in the "Manage Data > Payment Information Check".

![](/legacyfs/online/storage/blog_attachments/2023/03/D1.jpg)

Manage Data - Payment Information Check

+ Employees will be notified through the To-do Alerts on the Home Page.

![](/legacyfs/online/storage/blog_attachments/2023/03/D2.jpg)

Home Page - To-do Alerts

+ Employees will be notified via Mail notification.

![](/legacyfs/online/storage/blog_attachments/2023/03/D3.jpg)

Email Notifications

### **Conclusion**

As a result of reading this blog, you will be able to create the non-effective dated MDF object and Integration Center job. You will be able to gain a better understanding of how to extract data from one MDF and post it to another MDF using the Integration Center job.

Using the same logic, you can also trigger alerts and notifications for portlets such as National ID information.

> *Read other SAP SuccessFactors Employee Central blog posts and follow**[SAP SuccessFactors Employee Central](https://blogs.sap.com/tags/73555000100800000773...