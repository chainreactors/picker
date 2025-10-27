---
title: Error trying to logon from external system using SNC
url: https://blogs.sap.com/2023/07/11/error-trying-to-logon-from-external-system-using-snc/
source: SAP Blogs
date: 2023-07-12
fetch_date: 2025-10-04T11:54:49.902921
---

# Error trying to logon from external system using SNC

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [DevOps and System Administration](/t5/devops-and-system-administration/gh-p/devops-sysadmin)
* [Blog Posts](/t5/devops-and-system-administration-blog-posts/bg-p/devops-sysadminblog-board)
* Error trying to logon from external system using S...

DevOps and System Administration Blog Posts

Explore DevOps and system administration blog posts. Stay current with best practices, tools, and insights into efficient IT management strategies.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/devops-sysadminblog-board/article-id/227&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Error trying to logon from external system using SNC](/t5/devops-and-system-administration-blog-posts/error-trying-to-logon-from-external-system-using-snc/ba-p/13556375)

![marcelom_bovo](https://avatars.profile.sap.com/c/3/idc30ab58d8de57da10cd1f05b66d56bd1438d3970b8b13ac072197b3f400aca0e_small.jpeg "marcelom_bovo")

[marcelom\_bovo](https://community.sap.com/t5/user/viewprofilepage/user-id/341453)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=devops-sysadminblog-board&message.id=227)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/devops-sysadminblog-board/article-id/227)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556375)

‎2023 Jul 11
9:25 PM

[1
Kudo](/t5/kudos/messagepage/board-id/devops-sysadminblog-board/message-id/227/tab/all-users "Click here to see who gave kudos to this post.")

1,530

* SAP Managed Tags
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (1)

Hi All,

Recently we were changing some external connections from user/pass logon to SNC logon without password and we had a problem which were really difficult to find out. So for future reference if anyone face the same problem this post might be helpful.

User on SAP

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-10_15-22-55.png)

Here you can see the user has password disable and can be accessed using SNC

But when we tried this connection we were getting the error: CALL\_FUNCTION\_SIGNON\_INCOMPL The logon data for user "" is incomplete

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-10_15-27-12.png)

And the external application were getting the error JCO\_ERROR\_LOGON\_FAILURE: Initialization of repository destination.....failed: Logon data incomplete.

To solve this we had to **delete the entry** related to the SNC name on the user on table **SNCSYSACL,**transaction **SNC0**

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-10_15-22-55-1.png)

After this, the connection were OK

* [SNC Connection](/t5/tag/SNC%20Connection/tg-p/board-id/devops-sysadminblog-board)
* [SNC0](/t5/tag/SNC0/tg-p/board-id/devops-sysadminblog-board)
* [SNCSYSACL Table](/t5/tag/SNCSYSACL%20Table/tg-p/board-id/devops-sysadminblog-board)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fdevops-and-system-administration-blog-posts%2Ferror-trying-to-logon-from-external-system-using-snc%2Fba-p%2F13556375%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin