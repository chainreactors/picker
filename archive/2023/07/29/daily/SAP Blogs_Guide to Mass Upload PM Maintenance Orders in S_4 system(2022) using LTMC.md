---
title: Guide to Mass Upload PM Maintenance Orders in S/4 system(2022) using LTMC
url: https://blogs.sap.com/2023/07/28/guide-to-mass-upload-pm-maintenance-orders-in-s-4-system2022-using-ltmc/
source: SAP Blogs
date: 2023-07-29
fetch_date: 2025-10-04T11:53:11.296416
---

# Guide to Mass Upload PM Maintenance Orders in S/4 system(2022) using LTMC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Guide to Mass Upload PM Maintenance Orders in S/4 ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68411&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Guide to Mass Upload PM Maintenance Orders in S/4 system(2022) using LTMC](/t5/enterprise-resource-planning-blog-posts-by-members/guide-to-mass-upload-pm-maintenance-orders-in-s-4-system-2022-using-ltmc/ba-p/13568107)

![vrishtijain](https://avatars.profile.sap.com/6/c/id6cc96a5e13dd7f47c265849c324cbc84ae7772efcd0f9cd4c17129de9166d7f7_small.jpeg "vrishtijain")

[vrishtijain](https://community.sap.com/t5/user/viewprofilepage/user-id/421557)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68411)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68411)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568107)

‎2023 Jul 28
6:42 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68411/tab/all-users "Click here to see who gave kudos to this post.")

4,459

* SAP Managed Tags
* [SAP Fiori Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Cloud/pd-p/73554900100800000375)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori Cloud

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BCloud/pd-p/73554900100800000375)

View products (2)

**Problem Statement** : We want to upload bulk PM: Maintenance order/ work order (IW31) to S4 HANA system from another legacy system along with long text info. Although there are many options available  like BDC, LSMW but with Maintenance work order these options does not have long text options. This LTMC approach has all the features including long text, operations, etc.

**Solution** : Benefits of using this LTMC approach.

• There are predefined templates (XML/.CSV) files for each object.
• There are multiple migration objects available which we can use as per requirement.
• The migration programs are created automatically, no developer required by customer.

In this article, we will see step by step guide to upload PM maintenance order (Iw31) in latest 2022 S/4 Version.

Step 1: Open Fiori Launchpad. Click on below tile "Migrate your Data"

![](/legacyfs/online/storage/blog_attachments/2023/07/Tile-1.png)

Step 2: Click on "Create" button and choose "Migrate using staging table"

![](/legacyfs/online/storage/blog_attachments/2023/07/Migrate.png)

Step 3: Now give name to project starting with Z\_ and then select database schema as per requirement. We are selecting "Local SAP S/4 HANA database schema". And Click on step 2.

![](/legacyfs/online/storage/blog_attachments/2023/07/Step-1-3.png)

Step 4: Select local package or provide your custom package and click on STEP 3 button.

![](/legacyfs/online/storage/blog_attachments/2023/07/Step-2.png)

Step 5: Search PM maintenance order in left side panel. Select it and transfer to right using arrows. And then click on "Review" button.

![](/legacyfs/online/storage/blog_attachments/2023/07/step-3.png)

Step 6: Then review your entries and click on "Create Project" button. And your project will be created.

The documentation button showing can be used to help in filling the template for data upload.

![](/legacyfs/online/storage/blog_attachments/2023/07/review.png)

 Please wait for few minutes , then your project status will be in progress.

Important info: If you feel your project creation is taking too long then click on "Monitoring button" It will show the status of background process . Also check the missing authorization using SU53 transaction,

Step 7: Once your project is read, you will have an option to  "Download template". Click on the button and save files in .CSV format.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-1.png)

Step 8: You can fill the data in the downloaded files and then upload the same using "Upload File" option. You can see which file is mandatory and which file you needed. You can also refer the documentation provided by SAP on portal / or the link I highlighted in above screenshots.

Step 9: Once the files are uploaded click on "Validate data " button.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-2.png)

Important tip: You can go to Monitoring button whenever you perform any activity to see if that is failed or successful, it will show you all the logs and error messages.

Step 10: Once the data validated successfully. Click on "Transfer Data to staging tables" button.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-3.png)

Step 11: After data successfully transfer to tables. Go back to main project screen and there you can see "Prepare" option.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-4.png)

Step 12: After Prepare "Mapping Tasks " option comes up. Click on it and then You can see the data and confirm the same at that steps.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-5.png)

Step 13: After this "Stimulate" option comes up, After you successfully stimulate it, finally "Migrate" Option comes up.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-6.png)

Once you click on Migrate your data will be migrated and new work order get created in the system. You can check the logs in Monitoring screen.

Similarly you can use LTMC for other data load into the S4 system. SAP has make the process very simple and efficient.

Always check for authorizations if any task/process failed during this. Monitoring screens helps to get the error messages or successful logs during this whole process.

Thanks for reading the post. Happy Learning.

* [long text](/t5/tag/long%20text/tg-p/board-id/erp-blog-members)
* [ltmc](/t5/tag/ltmc/tg-p/board-id/erp-blog-members)
* [mass upload](/t5/tag/mass%20upload/tg-p/board-id/erp-blog-members)
* [PM maintenance order](/t5/tag/PM%20maintenance%20order/tg-p/board-id/erp-blog-members)
* [SAP S4HANA 2022](/t5/tag/SAP%20S4HANA%202022/tg-p/board-id/erp-blog-members)
* [Work Order](/t5/tag/Work%20Order/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fguide-to-mass-upload-pm-maintenance-orders-in-s-4-system-2022-using-ltmc%2Fba-p%2F13568107%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enabling 'Compliance' tab in Purchase order header & Line item in SAP Public cloud](/t5/enterprise-resource-planning-q-a/enabling-compliance-tab-in-purchase-order-header-amp-line-item-in-sap/qaq-p/14234218)
  in [Ente...