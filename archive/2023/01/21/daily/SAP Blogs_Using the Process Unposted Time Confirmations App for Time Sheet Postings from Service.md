---
title: Using the Process Unposted Time Confirmations App for Time Sheet Postings from Service
url: https://blogs.sap.com/2023/01/20/using-the-process-unposted-time-confirmations-app-for-time-sheet-postings-from-service/
source: SAP Blogs
date: 2023-01-21
fetch_date: 2025-10-04T04:28:33.552280
---

# Using the Process Unposted Time Confirmations App for Time Sheet Postings from Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Using the Process Unposted Time Confirmations App ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50237&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using the Process Unposted Time Confirmations App for Time Sheet Postings from Service](/t5/enterprise-resource-planning-blog-posts-by-sap/using-the-process-unposted-time-confirmations-app-for-time-sheet-postings/ba-p/13549448)

![Stephanie_Beuch](https://avatars.profile.sap.com/6/4/id64e3aca001b270ccec18dd5ffa41c93f15e6290a288dc808184bee4ff00c35fb_small.jpeg "Stephanie_Beuch")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Stephanie\_Beuch](https://community.sap.com/t5/user/viewprofilepage/user-id/131456)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50237)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50237)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549448)

‎2023 Jan 20
9:59 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50237/tab/all-users "Click here to see who gave kudos to this post.")

2,157

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Service](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Service/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)

* [SAP S/4HANA Cloud Public Edition Service

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BService/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)

View products (1)

When you record the consumption of time  during service execution, the system automatically creates cross-application time sheet (CATS) in SAP S/4HANA Cloud. After the completion of a service confirmation, the recorded time is copied to this time sheet. You can check whether the time sheet is created successfully or not in the transaction history of the service confirmation. (See screenshot in Figure 1.)

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog_Process_Unposted_Time_Confirmations_Figure_1-1.jpg)

Figure 1: Transaction History of Service Confirmations (screenshot from SAP S/4HANA Cloud 2208).

The time sheet will be approved automatically. And then the approved time sheet records are posted to accounting.

From the following screenshot in Figure 2, you can see an example of how internal costs are posted from time sheets in the **Service** **Actuals** app. In this example, the time sheet that posts costs is created for service confirmation item 10. The service confirmation item is the follow-up transaction of the service order item, which is the item-based accounting object.

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog_Process_Unposted_Time_Confirmations_Figure_2.jpg)

Figure 2: Service Actuals for service order (screenshot from SAP S/4HANA Cloud 2208).

Remark: If a service confirmation is canceled, the previous recorded time will be canceled. The canceled time sheet record will be posted to accounting as well.

In this blog I am going to explain how you can check if time sheet records are posted to accounting successfully.

# **Background information**

The time you record after the completion of a service confirmation is reflected in the cross-application time sheet (CATS). The creation of CATS then triggers a posting to accounting so that the internal costs are booked in accounting.

# **Time Sheet Postings**

Due to technical reasons, you cannot know whether the postings of time sheet records to accounting are successful or not when you complete service confirmations.

It can happen that the system can’t automatically post the time sheet records to accounting. The reason can be, for example, the financial period during which the labor was provided has already been closed. In this case, you must post the data manually using the **Process Unposted Time Confirmations** app (with the business role SAP\_BR\_OVERHEAD\_ACCOUNTANT).

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog_Process_Unposted_Time_Confirmations_Figure_3.jpg)

Figure 3: Process Unposted Time Confirmations app (screenshot from SAP S/4HANA Cloud 2208).

You can enter the provided selection parameters such as to determine the data you want to post to accounting.

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog_Process_Unposted_Time_Confirmations_Figure_4.jpg)

Figure 4: Screenshot of CATS: Transfer to Controlling (screenshot from SAP S/4HANA Cloud 2208).

## **Notes**

You can use the function of application log in the **Process Unposted Time Confirmations** app.

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog_Process_Unposted_Time_Confirmations_Figure_5.jpg)

Figure 5: Checkbox for Application Log (screenshot from SAP S/4HANA Cloud 2208).

In the log you can see which time sheet records were posted. If errors occurred and no postings were done, you can check the error messages and take appropriate actions according to the error messages. After fixing the error, you can execute the report again. If you want to check whether the error is successfully fixed or not beforehand, you can also do a test run by choosing the **Test Run** checkbox.

Hopefully after reading this blog post, you will have more in-depth knowledge about the process of postings of time sheet records to accounting after completing service confirmations.

Please don’t hesitate to raise your questions in Q&A forum of SAP Community or leave your comments below!

For more details, please visit the full product assistance documentation in the SAP Help Portal:

* [Service Confirmations | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/adbae5bcd5994f159bf2847a11397b61/f51f9127ec904db69be5bfc40cfcaeb4.html?version=latest)

* [Process Unposted Time Confirmations | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/2e9798b14cb6454ab600d6fbb1dfee00.html?state=DRAFT)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [cats](/t5/tag/cats/tg-p/board-id/erp-blog-sap)
* [service confirmation](/t5/tag/service%20confirmation/tg-p/board-id/erp-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fusing-the-process-unposted-time-confirmations-app-for-time-sheet-postings%2Fba-p%2F13549448%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite — your SAP Joule testbed and skills builder](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-your-sap-joule-testbed-and-skills-builder/ba-p/14...