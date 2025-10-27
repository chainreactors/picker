---
title: Transporting only changed/modified/created holidays and holiday calendars from development to quality and production system.
url: https://blogs.sap.com/2022/12/21/transporting-only-changed-modified-created-holidays-and-holiday-calendars-from-development-to-quality-and-production-system./
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:05.311371
---

# Transporting only changed/modified/created holidays and holiday calendars from development to quality and production system.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Transporting only changed/modified/created holiday...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67245&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Transporting only changed/modified/created holidays and holiday calendars from development to quality and production system.](/t5/enterprise-resource-planning-blog-posts-by-members/transporting-only-changed-modified-created-holidays-and-holiday-calendars/ba-p/13552943)

![javed_shaikh2](https://avatars.profile.sap.com/9/e/id9e5b3346a6faa85c2a3a710b16eea31511b37b38523ba4802d8edcb3518be532_small.jpeg "javed_shaikh2")

[javed\_shaikh2](https://community.sap.com/t5/user/viewprofilepage/user-id/497166)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67245)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67245)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552943)

‎2022 Dec 21
7:01 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67245/tab/all-users "Click here to see who gave kudos to this post.")

8,015

* SAP Managed Tags
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)
* [HCM Time Management](https://community.sap.com/t5/c-khhcw49343/HCM%2520Time%2520Management/pd-p/666118459887932219928019980895838)

* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [HCM Time Management

  Software Product Function](/t5/c-khhcw49343/HCM%2BTime%2BManagement/pd-p/666118459887932219928019980895838)

View products (2)

**Transporting only changed / modified / created holidays and holiday calendars from development to quality and production system.**

Transporting holiday and holiday calendar changes are not like transporting any other SAP HR configurations.

Reason: SAP have not provided any option to transport only holidays or holiday calendars you have created / changed / modified. If you try to transport it, all the holidays and holiday calendars available in the system gets included in transport request and gets transported to quality and production system and this is very risky.

Your system might have thousands of holidays and hundreds of holiday calendars in your system over the years. E.g. your system might have 1000 holidays and 50 holiday calendars. Even if you create / change a single holiday, all 1000 holidays and 50 holiday calendars will get included in transport request and gets transported to quality and production systems.

If your development and production systems are not in synch, then incorrect entries of development system will get transported to quality and production system and this will create huge problems in time management such as missing holidays or extra holidays and hence in time evaluation.

Even if your development and production systems are in synch, transporting all the holidays and holiday calendars each time will take a lot of time and will result in system performance issue.

To avoid these issues most of the customers do not transport the holidays and holiday calendars changes from development to quality and production systems, instead they configure the requirements directly in each system independently. Of course, it doesn’t matter whether you are making the changes first in development or quality or production system.  This is the easiest way to achieve the goal.

But this is the most insecure way of doing the holiday and holiday calendar changes, as for this approach, quality and production client should be opened for configuration directly, which is not suggested. By this approach there is a high risk of holiday and holiday calendars of all the systems to be out of synch with each other. This will result in issues while performing any unit testing and user acceptance testing in development and quality server for any future requirements.

To avoid all the above issues there is one work around by which you can transport only the holiday and holiday calendars which you have created / changed / modified from development to quality and production systems.

With this work around all the holiday and holiday calendars does not get moved to quality and production systems. Also, you don’t need to open the quality and production client for configurations.

The approach is as follows:

Create, change, or modify any holiday or holiday calendar using tcode SCAL in development system.

Remember if you save any changes in SCAL tcode system does not prompt for any transport request.

Go to SCAL tcode main screen as follows and click on transport Icon

![](/legacyfs/online/storage/blog_attachments/2022/12/2-47.png)

System will give you warning message as below. Click on OK.

![](/legacyfs/online/storage/blog_attachments/2022/12/3-44.png)

Now system will prompt you for transport request. Click on create request to create a new transport request

![](/legacyfs/online/storage/blog_attachments/2022/12/4-33.png)

Give short Description and click on save.

![](/legacyfs/online/storage/blog_attachments/2022/12/5-30.png)

System will create the workbench transport request and not the customizing transport request which generally gets created for configurations.

Note: By doing this, you have included all the holiday and holidays calendars in this transport request.

TR looks like below:

![](/legacyfs/online/storage/blog_attachments/2022/12/6-25.png)

Now most important point here is to ***NOT*** to release this transport request. Even if you release the transport request by mistake then there is no option to stop transporting everything to quality and production system.

We need to modify this transport request manually. In the above TR the tables which are related to holidays and holiday calendar are: THOC, THOCD, THOCS, THOCT, THOCI, THOLT, THOLU, THOL so delete the other tables from TR, i.e., tables to be deleted are TCALS, TFACD, TFACS, TFAIN, TFACT, TFAIT.

For deleting the tables from TR click on display < - > change icon, by doing this, TR will get opened in change mode, select the table rows to be deleted and click on delete row, then save the TR.

![](/legacyfs/online/storage/blog_attachments/2022/12/ch-2.png)

Only below tables rows should remain in TR:

![](/legacyfs/online/storage/blog_attachments/2022/12/7-19.png)

Now if we move this TR, still all the holiday and holiday calendars will get moved.

So now in this TR we should include only those holidays and calendars which we have modified.

For this you should know the holiday and holiday calendar codes. You will get the holiday calendar codes directly from SCAL tcode as per below:

![](/legacyfs/online/storage/blog_attachments/2022/12/ch1-1.png)

But for holiday codes you need to refer 2 tables in SE16, THOCD and THOL.

![](/legacyfs/online/storage/blog_attachments/2022/12/ch3.png)

Once you get the holidays and holi...