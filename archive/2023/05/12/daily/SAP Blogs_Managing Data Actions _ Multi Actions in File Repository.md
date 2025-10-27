---
title: Managing Data Actions / Multi Actions in File Repository
url: https://blogs.sap.com/2023/05/11/managing-data-actions-multi-actions-in-file-repository/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:41.755013
---

# Managing Data Actions / Multi Actions in File Repository

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Managing Data Actions / Multi Actions in File Repo...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161988&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Managing Data Actions / Multi Actions in File Repository](/t5/technology-blog-posts-by-members/managing-data-actions-multi-actions-in-file-repository/ba-p/13560903)

![rtsaravi](https://avatars.profile.sap.com/a/5/ida5d37536967afa8a4cd0c0682512c343e8fef9072f86e5c01a77503b25b5925d_small.jpeg "rtsaravi")

[rtsaravi](https://community.sap.com/t5/user/viewprofilepage/user-id/128364)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161988)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161988)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560903)

‎2023 May 11
7:11 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161988/tab/all-users "Click here to see who gave kudos to this post.")

2,379

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [User Experience](https://community.sap.com/t5/c-khhcw49343/User%2520Experience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)
* [User Experience

  Topic](/t5/c-khhcw49343/User%2BExperience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

View products (3)

Here is the new and most awaited feature in SAP Analytics Cloud - Data Actions part has been released and with no doubt it's really useful on Security part of SAC, whereas now the Data Actions and Multi Actions can be restricted on Folder / File repository level.

Let's get into the blog for more details on how to restrict / move data actions and multi actions on file repository.

We can now able to manage Data Actions / Multi Actions by saving them into a file structure (under "My Files") in SAP Analytics Cloud from the release 2023.6.

**Before Release 2023.6 :**

Currently all Data Actions and Multi Actions are stored centrally as a list under respective toolbars.

![](/legacyfs/online/storage/blog_attachments/2023/05/1-41.png)

Centrally Stored Data Actions

![](/legacyfs/online/storage/blog_attachments/2023/05/2-19.png)

Centrally Stored Multi Actions

**After Release 2023.6 :**

From the new update we can able to see that under Data Actions and Multi Actions no list will be shown instead only the **Recent Files** will be visible. This means that only recently opened Data Actions and Multi Actions can be viewed by the user.

![](/legacyfs/online/storage/blog_attachments/2023/05/3-21.png)

Recently opened Data Actions from File Repository

**How to View/Open existing Data Actions & Multi Actions:**

All existing data actions and multi actions can be accessed under **"Files / My Files / Public / Data Actions" &  "Files / My Files / Public / Multi Actions"**

![](/legacyfs/online/storage/blog_attachments/2023/05/4-14.png)

Data Action File Repository Folder Path

![](/legacyfs/online/storage/blog_attachments/2023/05/5-12.png)

Multi Action File Repository Folder Path

**How to Restrict Data Action / Multi Action (DTA / MTA) Permission:**

In order to restrict DTA / MTA on a file repository folder, we can specify two different roles for DTA & MTA which should be assigned by system admin on the **"Roles"** page. Even there are many combinations of Role Based permissions are possible, here we are taking the below two types as example.

![](/legacyfs/online/storage/blog_attachments/2023/05/6-11.png)

Navigation to Roles

**Role Based Restriction**

* Data Action Designer

User with Full Permission (Create, Read, Update, Delete, Execute) which is assigned by the system admin is called as Data Action Designer

![](/legacyfs/online/storage/blog_attachments/2023/05/7-10.png)

Roles selected for Data Action Designer

* Data Action User

User without Permission to Create is considered as Data Action User, who have access to (Read, Update, Delete, Execute)

![](/legacyfs/online/storage/blog_attachments/2023/05/8-12.png)

Roles selected for Data Action User

Note: If a user doesn't have required role-based permissions for data actions, then permissions on file repository level will be restricted.

**File Repository Based Restriction:**

Asusual the file/folder based restrictions remains the same that we can restrict by sharing the file/folder with (**View, Edit, Full Control or Custom**) access.

![](/legacyfs/online/storage/blog_attachments/2023/05/9-11.png)

Custom Access setting from File Repository

From the file repository we can able to use toolbar to perform Copy, Move or Delete data actions & multi actions.

For more details refer - [help.sap.com](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/2023.8/en-US/2850221adef14958a4554ad2860ff412.html)

Hope this blog might be useful for everyone who actively works on data actions part, kindly share your thoughts and reviews in comments. For more blogs related to SAP Analytics Cloud don't forget to follow our community - [SAP Analytics Cloud Community](https://community.sap.com/topics/cloud-analytics)

* [@SAP Analytics Cloud](/t5/tag/%40SAP%20Analytics%20Cloud/tg-p/board-id/technology-blog-members)
* [sac data action](/t5/tag/sac%20data%20action/tg-p/board-id/technology-blog-members)
* [sac multi action](/t5/tag/sac%20multi%20action/tg-p/board-id/technology-blog-members)
* [SAP Analytics Cloud](/t5/tag/SAP%20Analytics%20Cloud/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmanaging-data-actions-multi-actions-in-file-repository%2Fba-p%2F13560903%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [How to use Version Management with Github Repository](/t5/technology-blog-posts-by-sap/how-to-use-version-management-with-github-repository/ba-p/13811133)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Artificial Intelligence and SAP Master Data Govern...