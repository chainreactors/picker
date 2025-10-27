---
title: 0.1 + 0.2 does not equal 0.3
url: https://blogs.sap.com/2023/01/02/0.1-0.2-does-not-equal-0.3/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:54:45.628896
---

# 0.1 + 0.2 does not equal 0.3

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* 0.1 + 0.2 does not equal 0.3

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47072&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [0.1 + 0.2 does not equal 0.3](/t5/application-development-and-automation-blog-posts/0-1-0-2-does-not-equal-0-3/ba-p/13561667)

![matt](https://avatars.profile.sap.com/1/c/id1cae56a3d0a04deff9c8d10f54c3f562a6106c370cfae33f5fcd6d3888172910_small.jpeg "matt")

[matt](https://community.sap.com/t5/user/viewprofilepage/user-id/310)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47072)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47072)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561667)

‎2023 Jan 02
6:52 PM

[11
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47072/tab/all-users "Click here to see who gave kudos to this post.")

1,219

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Here's a little bit of code:

```
REPORT.

DATA a TYPE f.

DATA b TYPE f.

a = '0.1'.

b = '0.2'.

DATA c TYPE f.

c = a + b.

WRITE / c.
```

Output is... 3,0000000000000004E-01 (i.e. 0.300 000 000 000 000 04)

Add a couple more WRITE statements and you might begin to see what's going on.

1.0000000000000001E-01
2.0000000000000001E-01
3.0000000000000004E-01

For a full explanation (and what put me onto this) see [here](https://qntm.org/notpointthree). It's kind of obvious, once you think about, but it never really occured to me!

* [binary](/t5/tag/binary/tg-p/board-id/application-developmentblog-board)
* [computer science](/t5/tag/computer%20science/tg-p/board-id/application-developmentblog-board)

5 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin