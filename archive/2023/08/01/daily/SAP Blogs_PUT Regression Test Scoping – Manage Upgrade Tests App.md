---
title: PUT Regression Test Scoping – Manage Upgrade Tests App
url: https://blogs.sap.com/2023/07/31/put-regression-test-scoping-manage-upgrade-tests-app/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T16:59:53.041133
---

# PUT Regression Test Scoping – Manage Upgrade Tests App

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* PUT Regression Test Scoping – Manage Upgrade Tests...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53569&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [PUT Regression Test Scoping – Manage Upgrade Tests App](/t5/enterprise-resource-planning-blog-posts-by-sap/put-regression-test-scoping-manage-upgrade-tests-app/ba-p/13571884)

![Aparna_Vohra](https://avatars.profile.sap.com/4/0/id40ddb9efea8d8a2345734c03d1851c1641d39c92a898ce3436bb0cc87a45de11_small.jpeg "Aparna_Vohra")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Aparna\_Vohra](https://community.sap.com/t5/user/viewprofilepage/user-id/131756)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53569)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53569)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571884)

‎2023 Jul 31
10:23 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53569/tab/all-users "Click here to see who gave kudos to this post.")

2,609

* SAP Managed Tags
* [test automation tool for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/test%2520automation%2520tool%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [test automation tool for SAP S/4HANA Cloud

  Software Product Function](/t5/c-khhcw49343/test%2Bautomation%2Btool%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)

View products (2)

One of the most common questions which come from our customers is - Can we scope our custom automates in Post Upgrade Tests (PUT). The answer is Yes, the Manage Upgrade Tests App was a new addition to the SAP S/4HANA Cloud Test Automation Tool (TAT) suite which offers our customers the flexibility to customize the scope of their upgrade tests by adding custom automates

The MUT app serves as a preparatory step for the upgrade cycle where the scope is maintained and automatically triggered via the task list after every major upgrade. This makes PUT more customer driven and helps to identify defects earlier. Apart from enabling them to add custom scope, customers can trigger PUT from the Test Your Process (TYP) app at any point in the software lifecycle with a single click.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-43.png)

# Requirements which paved the way forward

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-33.png)

* Configure custom automates created using the Test automation Tool - Our customers may want to execute additional business processes which may not be part of the regular PUT scope.

* The upgrade test scope can be customized with a mix of SAP delivered PUT automates and customer specific custom automates.

* Focus on customer relevant scenarios as per the business model. Our customers may not want to execute the entire scope of PUT automates as some of them may not be relevant for them.

# Building your test suite using the Manage Upgrade Tests App

Using the MUT app, you can create multiple regression test scope with execution variants. Each execution variant contains a combination of standard and customized scope to be triggered during PUT.

* **Execution Variants**: You can view, update, copy and delete execution variants comprising of an execution list which contains PUT processes and customer test plans. The execution variants can have names and descriptions for easy distinction. One execution variant is marked as default at any point in time. It is easily possible to create new execution variants by navigating to the PUT Processes and/or Customer Test Plans tabs.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-30.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture4-26.png)

* **Execution List**: If a previously created execution scope exists, it will be displayed in this view-only tab. Otherwise, it will be empty. A set of PUT processes get populated as the default execution list once the system setup is complete.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-26.png)

* PUT Processes: All the PUT processes relevant to your scope and which pass the pre-check are listed in this tab. We can run a Pre-check by clicking on the Run Pre-check button to populate the PUT processes which are active for the given customer system.

* Customer Test Plans: All Customer Test Plans with the last execution status along with the data variant name used for the latest execution will be listed in this tab. This is where we can add the custom automates.

# Integration with Test Your Processes (TYP) App

Starting with the 2308 release, all the Execution Variants maintained in the MUT app will be available to for a PUT execution from the TYP application. Customers can select the ‘Execution Variant” from the dropdown and with one click trigger the PUT execution for the regression suite of their choice.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture6-24.png)

The Post-Upgrade Tests Execution History pop up displays the execution variant triggered and the scope of execution along with the status of the tests. The Track Post-Upgrade Tests option launches this pop up.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture7-17.png)

The source of the execution scope can take one of the following values-

* Executed with all relevant post-upgrade scope.

* Executed with Scope from Manage Upgrade Tests application along with the execution variant name.

# Viewing results in the Analyze Automated Test Results App

We can apply the Test Plan Type filter to view the execution results in the Analyze Automated Test Results application. The execution scope as well as the execution variant can be selected from the dropdown to filter the results accordingly.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture8-16.png)

# Further Helpful Links

[Manage Upgrade Tests](https://help.sap.com/docs/SAP_S4HANA_CLOUD/9f3351bbe2f04b42bb29f690886a6f54/dd1dc59e34364a26b1c6183a1369612b.html?state=DRAFT&q=manage%20upgrade%20tests)

[Viewing filtered results in AATR](https://help.sap.com/docs/SAP_S4HANA_CLOUD/7ce8f79186e1445ab82e37439eba795c/1641ad7da8ff42d195a8cdcfc541fa26.html?state=DRAFT&q=variant#loio205c00fb7da74f3880e9929f39f5e868)

[Blog Post on Test Data Container](https://blogs.sap.com/2021/09/01/centralized-test-data-management-with-test-data-container/)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [post upgrade test](/t5/tag/post%20upgrade%20test/tg-p...