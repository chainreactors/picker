---
title: Integration between SAP Commerce Cloud and CPI using Integration Object – one case with Emarsys
url: https://blogs.sap.com/2022/11/08/integration-between-sap-commerce-cloud-and-cpi-using-integration-object-one-case-with-emarsys/
source: SAP Blogs
date: 2022-11-09
fetch_date: 2025-10-03T22:05:11.735947
---

# Integration between SAP Commerce Cloud and CPI using Integration Object – one case with Emarsys

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Integration between SAP Commerce Cloud and CPI usi...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13150&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integration between SAP Commerce Cloud and CPI using Integration Object - one case with Emarsys](/t5/crm-and-cx-blog-posts-by-sap/integration-between-sap-commerce-cloud-and-cpi-using-integration-object-one/ba-p/13562405)

![rodrigocardoso](https://avatars.profile.sap.com/1/6/id160ce4ea088a7162377691cd311ebf4b43dcdf8404c25e2028c7e3c9a88220de_small.jpeg "rodrigocardoso")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[rodrigocardoso](https://community.sap.com/t5/user/viewprofilepage/user-id/13378)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13150)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13150)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562405)

‎2022 Nov 08
8:42 PM

[5
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13150/tab/all-users "Click here to see who gave kudos to this post.")

6,098

* SAP Managed Tags
* [SAP Emarsys Commerce Cloud Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys%2520Commerce%2520Cloud%2520Integration/pd-p/eaaffcef-f085-4369-80ca-7016d6fd1c1a)

* [SAP Emarsys Commerce Cloud Integration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BEmarsys%2BCommerce%2BCloud%2BIntegration/pd-p/eaaffcef-f085-4369-80ca-7016d6fd1c1a)

View products (1)

## Overview

---

This article will explain how you can integrate SAP Commerce and Emarsys through CPI.

This post can be helpful for things like Customer Register or any [Item Type](https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/8c755da8866910149c27ec908fc577ef.html) of SAP Commerce.**We will show an approach with the out-of-the-box (OOTB) features.**

This blog was built in 3 parts:

1. Requirement - SAP Commerce set up with information from CPI;

2. Integration Object setup;

3. Test.

The proposal is through the store ([Spartacus](https://sap.github.io/spartacus-docs/)) to make a register of customers, capture the event with Integration Object and send it to CPI.

In CPI, we will set up the Emarsys authentication (WSSE) and create a map of fields after sending it to Emarsys.

|
 **To CPI setups and Emarsys information, access the post** [Integrating SAP Commerce and SAP Emarsys using Cloud Integration](https://blogs.sap.com/2022/10/28/integrating-sap-commerce-and-sap-emarsys-using-cloud-integration/) post by d.pietroniro. |

In Emarsys, we are going to check the information sent from CPI.

![](/legacyfs/online/storage/blog_attachments/2022/11/Blog-Process.png)

Data Flow

## 1 Requirement

---

1.1 Firstly, we need CPI credentials and the URL of the public endpoint. In our sample, we used Basic Credentials.

1.2 Go to SAP Commerce Backoffice of SAP Commerce

1.3 Going to the vertical menu, select Basic Credentials and add a new Basic Credential.

![](/legacyfs/online/storage/blog_attachments/2022/11/1-Credencial.png)

1.4 Put the credential generated in CPI

![](/legacyfs/online/storage/blog_attachments/2022/11/2-Credencial-Register.png)

OK. We have the CPI credentials saved in our SAP Commerce.

We are going to save the public endpoint shared by CPI.

1.5 Again, in the vertical Backoffice menu, click on Consumed Destinations

![](/legacyfs/online/storage/blog_attachments/2022/11/3-Menu-Consumed-Destinations.png)

1.6 Add the public endpoint according to the following image

![](/legacyfs/online/storage/blog_attachments/2022/11/4-endpoint-consumed.png)

1.7 Select the credential created before

![](/legacyfs/online/storage/blog_attachments/2022/11/5-selection-credencial.png)

1.8 Test the endpoint from CPI and check if the green message is shown.

![](/legacyfs/online/storage/blog_attachments/2022/11/6-green-message.png)

With that steps, you have a connection with CPI.

## 2 Integration Object (IO) Setup

---

2.1 At the top of Commerce, select **Integration UI Tool**.

|
 **To see the full extensions list necessary for this resource**, click here[Integration Object - Extensions](https://help.sap.com/docs/SAP_COMMERCE/50c996852b32456c96d3161a95544cdb/9af51e8010034ac7bda41a3486196894.html). |

![](/legacyfs/online/storage/blog_attachments/2022/11/7-menu-integration-1.png)

2.2 Click on 'Create Integration Object' button

![](/legacyfs/online/storage/blog_attachments/2022/11/8-create-IO.png)

2.3 Define the name according to the context; in our case, Customer, I give the name 'ioCustomer' (i= Integration o= Object)

2.4 Select which Item Type of Commerce you need to capture the information; in our case, the Customer

![](/legacyfs/online/storage/blog_attachments/2022/11/9-registerIO.png)

2.5 After creating the ioCustomer, you can select the created IO.

2.6 Will be available many attributes; in our case, we selected the first level (Customer) and two attributes: 'contactEmail' and 'customerID.'

2.7 Choose also the attribute that will have a unique value.

![](/legacyfs/online/storage/blog_attachments/2022/11/10-selectFieldIO.png)

2.8 Now, you will create the Webhook; this functionality *"allows SAP Commerce to send notifications to a configured destination URL when an item is saved (created or updated) or deleted*."

|
 **To see more information about Webhook**, click here [Webhook](https://help.sap.com/docs/SAP_COMMERCE/50c996852b32456c96d3161a95544cdb/461d8cfe95f5442880491e2cad0a4831.html?q=webhook) |

2.9 In the vertical menu, select Webhook, following click on the plus button (CreateWebhookConfiguration)

![](/legacyfs/online/storage/blog_attachments/2022/11/11-create-Webhook.png)

2.10 In droplists, select the 'ioCustomer,' previously created; select 'sendCustomer2CPI', previously created in 1.6 item; select Event Type, in our case, 'Item Saved.'

|
 **'Item Saved' events will trigger all time that object Customer went changed**. |

![](/legacyfs/online/storage/blog_attachments/2022/11/12-SaveWebhook.png)

## 3 Testing

---

3.1 In our post, we are using Spartacus. "*Spartacus is a lean, Angular-based JavaScript storefront for SAP Commerce Cloud. Spartacus talks to SAP Commerce Cloud exclusively through the Commerce REST API."*

3.2 We choose the electronics store

|
 **It is not necessary to use Spartacus because what triggers the event is the Commerce platform.** |

3.3 Click on 'Sign/ Register'

![](/legacyfs/online/storage/blog_attachments/2022/11/13-Home-Store.png)

3.4 Considering that you are a new user, select 'Register'.

![](/legacyfs/online/storage/blog_attachments/2022/11/14-Register-Button.png)

3.5 Fill in all required fields and click on 'Register'

![](/legacyfs/online/storage/blog_attachments/2022/11/15-Fill-Fiesld.png)

3.6 Return to SAP Commerce, select the perspective 'Integration UI Tool again.'

3.7 In the vertical menu, click on 'Monitoring → Outbound.'

![](/legacyfs/online/storage/blog_attachments/2022/11/16-Monitoring.png)

3.8 The submission record must be available with a...