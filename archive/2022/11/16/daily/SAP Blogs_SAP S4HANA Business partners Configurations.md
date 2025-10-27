---
title: SAP S4HANA Business partners Configurations
url: https://blogs.sap.com/2022/11/15/sap-s4hana-business-partners-configurations/
source: SAP Blogs
date: 2022-11-16
fetch_date: 2025-10-03T22:52:39.020426
---

# SAP S4HANA Business partners Configurations

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP S4HANA Business partners Configurations

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68310&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S4HANA Business partners Configurations](/t5/enterprise-resource-planning-blog-posts-by-members/sap-s4hana-business-partners-configurations/ba-p/13566281)

![carunkumar](https://avatars.profile.sap.com/c/4/idc4c1396b296e26cf575b153ad752d3c9095d69ba6a30a3058a5511802b96e6b0_small.jpeg "carunkumar")

[carunkumar](https://community.sap.com/t5/user/viewprofilepage/user-id/40206)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68310)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68310)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566281)

‎2022 Nov 15
9:43 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68310/tab/all-users "Click here to see who gave kudos to this post.")

30,602

* SAP Managed Tags
* [SAP S/4HANA business partner](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520business%2520partner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)

* [SAP S/4HANA business partner

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bbusiness%2Bpartner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)

View products (1)

**Objective:** The Main aim of this post is giving the brief idea about the SAP S4hana business partners and configuration settings for the business partners to customer integration.

SAP Business partner is a person, Organization, or group of organizations. It is a single point of entry to maintain company code, vendor and customer data. BP is an integrated with SRM and CRM modules into core module.

For creation of Vendor and customer to a business partner we need the inputs of General data, company code data, Purchase organization data and Sales organization data.

In sap S4HANA system we have multiple options to create the business partners. Those are

* Business partner as a customer

* Business partner as a Vendor

* Business partner as a customer and vendor

Based on the business requirement we need to configure the required business partners.

Here I will present you the customer with business partner integration process.

**Prerequisites to create Business partners to customer:**

1.Define Number ranges for the BP

2.Define groupings and assign number ranges to BP

3.Define Business partners roles and grouping

4.Create customer account group

5.Create the Customer number ranges and account groups

6.Number assignment for direction BP to customer & BP to Vendor

7.Creation of business partners

For proceeding the above steps, we need to configure the S4Hana system by following configurations.

**1.Define Number ranges for the BP:**

For configuring the BP number ranges and group we need to procced the following path

**Path: SPRO->Cross application components->SAP Business partners->SAP Business partners****->Basic Settings ->**

![](/legacyfs/online/storage/blog_attachments/2022/11/1-51.png)

Here we need to define the number ranges for the business partners

![](/legacyfs/online/storage/blog_attachments/2022/11/2-32.png)

For the Customer vendor integration to business partners we must select the business partners number range is internal.

**2.Define groupings and assign number ranges to BP:**

![](/legacyfs/online/storage/blog_attachments/2022/11/3-22.png)

**3.Define Business partners roles and grouping:**

Path: **SPRO->Cross application components->SAP Business partners->SAP Business partners****->Basic Settings ->**

![](/legacyfs/online/storage/blog_attachments/2022/11/4-20.png)

Here we need define the BP roles and assign those to particular BP role grouping.

Normally SAP standard BP roles are

* 00000-BP General data

* FLVN00- FI vendor data (company code data)

* FLVN01- Purchase org data

* FLCU00- Customer company code data

* FLCU01- Customer sales org data

Define Roles:

![](/legacyfs/online/storage/blog_attachments/2022/11/5-16.png)

Define roles grouping:

![](/legacyfs/online/storage/blog_attachments/2022/11/6-13.png)

Here we need to give the relevant roles for BP grouping. Suppose for BP to customer  we required BP roles 00000,FLCU00 and FLCU01.

**4.Create customer account groups:**

![](/legacyfs/online/storage/blog_attachments/2022/11/7-20.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/8-17.png)

Here we need to create the customer account group based on the requirement.

**5.Create the Customer number ranges and account groups:**

Path: SPRO->Financial Accounting ->Accounts receivable and Accounts payable-> Customer accounts->Master data-> Preparations for creating customer master data

![](/legacyfs/online/storage/blog_attachments/2022/11/9-31.png)

Here we need to configure the Customer accounts number ranges

![](/legacyfs/online/storage/blog_attachments/2022/11/10-8.png)

Assign number ranges to the relevant customer account groups

![](/legacyfs/online/storage/blog_attachments/2022/11/11-10.png)

**6.Number assignment for direction BP to customer & BP to Vendor:**

Path: Cross Application Components –> Master Data synchronization –> Customer/Vendor Integration –> Business Partner Settings –> Setting for Customer Integration –> Filed Assignment for customer Integration –> Assign Keys –> Define Number ranges for Direction BP to Customer

![](/legacyfs/online/storage/blog_attachments/2022/11/12-10.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/13-9.png)

Here we need to maintain the same number range for the BP to customer.

**7.Creation of business partners:**

Create Business partners using BP Transection code.

![](/legacyfs/online/storage/blog_attachments/2022/11/14-9.png)

Where we need to give the input fields in the tabs General data, company code data and sales and distribution data.

For Existing business partners data, we can check in the below tables.

BUT000- BP general data

BUT001- BP roles

CVI\_VEND\_LINK-Assignment Between Vendor and Business Partner

CVI\_CUST\_LINK-Assignment Between Customer and Business Partner

I Hope this information get the clear idea about the SAP S4hana business partners configuration.

Thanking you.

Need your  valuable suggestions and comments about this content.

Best Regards,
Arun Kumar C

* [business partner](/t5/tag/business%20partner/tg-p/board-id/erp-blog-members)
* [SAP Business Partner Master Data](/t5/tag/SAP%20Business%20Partner%20Master%20Data/tg-p/board-id/erp-blog-members)
* [sap business partner screening](/t5/tag/sap%20business%20partner%20screening/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fsap-s4hana-business-partners-con...