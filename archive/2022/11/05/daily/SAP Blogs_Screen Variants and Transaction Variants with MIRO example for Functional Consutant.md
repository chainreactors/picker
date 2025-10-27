---
title: Screen Variants and Transaction Variants with MIRO example for Functional Consutant
url: https://blogs.sap.com/2022/11/04/screen-variants-and-transaction-variants-with-miro-example-for-functional-consutant/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:44:49.311370
---

# Screen Variants and Transaction Variants with MIRO example for Functional Consutant

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Screen Variants and Transaction Variants with MIRO...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68106&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Screen Variants and Transaction Variants with MIRO example for Functional Consutant](/t5/enterprise-resource-planning-blog-posts-by-members/screen-variants-and-transaction-variants-with-miro-example-for-functional/ba-p/13563383)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68106)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68106)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563383)

‎2022 Nov 04
7:40 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68106/tab/all-users "Click here to see who gave kudos to this post.")

11,490

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)
* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)

View products (7)

# **Introduction**

This document will help functional consultant to create screen variant/transaction variant and achieve the business requirement without the support of technical team. This document aims to identify and describe all steps associated with the screen variant & transaction varaints. In addition, This document will help functional consultant who want to explore the possibility by screen variant functionality.

# **Purpose**

Usually we have many such business requirement in every project where business ask us to preform such validation during a business transaction. We can achieve below functionality without the help of technical team. We can use screen variant to achieve the desired result. Screen variants can be used to achieve the below business requirement –

* **Adopt field values - Saves the field values you have inserted on the current screen.**

* **Do not display screen - Hides screen**

* **With contents - Field contents are saved with it**

* **Output only - Field is no longer ready for input (display mode only)**

* **Invisible - Hides field**

* **Mandatory - Required field**

## **Scope**

Explaining the creation of screen variant and transaction variant with the help of business requirement.

## **Requirement**

There is a requirement to grey out (Display mode) below mentioned fields during the MIRO transaction and make the Inv. Ref. a mandatory field.

**Baseline date – Display Only**

**Payment terms - Display Only**

**Due on - Display Only**

**In. Ref. – Mandatory**

## **Configuration**

Step 1 – find the program and field name. T code MIRO and Keep the cursor on field baseline date and click on F1.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.43.43-AM.png)

Step2 – T code – OLMRLIST and enter the transaction MIRO

Click on Screen Variant and enter the program name and hit enter.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.44.10-AM.png)

Select the screen 020.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.44.24-AM.png)

Click on edit

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.44.41-AM.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.44.52-AM.png)

Select the output only checkbox for

**BaselineDt**

**Pyt Terms**

**Due On**

Select the Required checkbox for

**Inv. Ref.**

Save the screen variant.

Step 3 – T code – SHD0

Create a transaction variant and assigned the screen variant.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.45.13-AM.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.45.26-AM.png)

## **Authorization**

The specific group for which we have created this transaction variant XXXXXXX  will now be authorized by BASIS with proper roles and authorizations. We can assign the group name as below.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.45.43-AM.png)

Step 4- Check and test the variant.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.45.59-AM.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.47.22-AM.png)

Please do not forget to activate it.

## Result

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-05-at-12.49.06-AM.png)

 Mandatory checkbox will appear in field.

Please share your valuable feedback.

**Please follow my blog for FI cutover activities –**

<https://blogs.sap.com/2022/10/14/sap-fi-cutover-activity-plan-complete-activities/>

**Please follow my blog for validation and****substitution -**

<https://blogs.sap.com/2022/10/30/user-exit-in-validation-substitution-for-functional-consultant/>

Please follow the ...