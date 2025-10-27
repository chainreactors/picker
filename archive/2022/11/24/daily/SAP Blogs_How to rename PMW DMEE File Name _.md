---
title: How to rename PMW DMEE File Name ?
url: https://blogs.sap.com/2022/11/23/how-to-rename-pmw-dmee-file-name/
source: SAP Blogs
date: 2022-11-24
fetch_date: 2025-10-03T23:39:01.042702
---

# How to rename PMW DMEE File Name ?

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* How to rename PMW DMEE File Name ?

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46772&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [How to rename PMW DMEE File Name ?](/t5/application-development-and-automation-blog-posts/how-to-rename-pmw-dmee-file-name/ba-p/13554453)

![former_member793781](https://avatars.profile.sap.com/former_member_small.jpeg "former_member793781")

[former\_member793781](https://community.sap.com/t5/user/viewprofilepage/user-id/793781)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46772)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46772)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554453)

‎2022 Nov 23
5:06 PM

[1
Kudo](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46772/tab/all-users "Click here to see who gave kudos to this post.")

7,108

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

## **Introduction:**

In this blog I am going to explain how to modify the payment method workbench (PMW) File name.

Usually, In the standard program the filename will be generated as like the below format,

![](/legacyfs/online/storage/blog_attachments/2022/11/stnd_fmt-1.jpg)

Sometimes, we may need to add **DATE** and **TIMESTAMP** Values for the filename. Let's see how we can achieve that using simple steps.

**Disclaimer**: The Program name and other details I am using in this blog is from demo system only and this is only for learning purpose.

## **Steps to follow:**

I’ve come up with a solution that we are going to use Standard **FM FI\_PAYMEDIUM\_SAMPLE\_20**to modify the file name.

#### **Step 1:**

Goto **SE****37 to** take copy of standard FM FI\_PAYMEDIUM\_SAMPLE\_20 as **ZFI\_PAYMEDIUM\_SAMPLE\_****20.**

![](/legacyfs/online/storage/blog_attachments/2022/11/FM.jpg)

#### **Step 2:**

Using changing parameter C\_FILENAME, Modify the file name as per your requirement.

To trigger the debugger. Add the below mentioned infinite endless loop code, and check in SM50.

```
data: a, b.

a = 'X'.

do.

   if a = b.

     exit.

   endif.

enddo.
```

**Step****3:**

Goto **OBPM3** T-Code select the **Payment Medium** format and click **Event Modules,**

Enter the **Event as 21,** add your own custom Function Module Name

![](/legacyfs/online/storage/blog_attachments/2022/11/ombt3.png)

**Sample****Output:**

Check in AL11.

![](/legacyfs/online/storage/blog_attachments/2022/11/result-1-1.png)

## **Summary:**

In this blog, I have explained how to modify standard Payment Medium Workbench DMEE File Name.

Sincerely appreciate any feedback/comments/questions.

**Thanks & Regards,**

**M.Purushothaman**

* [FI\_PAYMEDIUM\_SAMPLE\_20](/t5/tag/FI_PAYMEDIUM_SAMPLE_20/tg-p/board-id/application-developmentblog-board)
* [obpm3](/t5/tag/obpm3/tg-p/board-id/application-developmentblog-board)
* [pmw](/t5/tag/pmw/tg-p/board-id/application-developmentblog-board)

1 Comment

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin