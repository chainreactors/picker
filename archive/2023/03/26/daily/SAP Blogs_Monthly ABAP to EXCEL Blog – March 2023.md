---
title: Monthly ABAP to EXCEL Blog – March 2023
url: https://blogs.sap.com/2023/03/25/monthly-abap-to-excel-blog-march-2023/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:51.773621
---

# Monthly ABAP to EXCEL Blog – March 2023

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Monthly ABAP to EXCEL Blog – March 2023

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46974&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Monthly ABAP to EXCEL Blog – March 2023](/t5/application-development-and-automation-blog-posts/monthly-abap-to-excel-blog-march-2023/ba-p/13559368)

![hardyp180](https://avatars.profile.sap.com/7/0/id70fe549259937f2b1b98e44da0f7bd9453cb5df35004602e05d40b6523508cb7_small.jpeg "hardyp180")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[hardyp180](https://community.sap.com/t5/user/viewprofilepage/user-id/13778)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46974)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46974)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559368)

‎2023 Mar 25
5:45 AM

[24
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46974/tab/all-users "Click here to see who gave kudos to this post.")

13,113

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

For over ten years now every month on the SAP Community Site someone publishes a blog about how to upload/download data from EXCEL to ABAP. So, I am going to start doing this as well - only I will always be talking about ABAP2XLSX as the preferred mechanism to do this.

![](/legacyfs/online/storage/blog_attachments/2023/03/Excel-01.jpg)

Hundreds of ABAP to Excel Blogs

The 120 blogs posted over the last ten years usually never mention ABAP2XLSX at all. They either talk about the archaic OLE technology that can be used to communicate with Microsoft products or re-invent the ABAP2XLSX concept.

Then myself and about three or four other people (the “usual suspects” as I call them) will post in the comments section talking about ABAP2XLSX and the original poster will either admit they had never heard of ABAP2XLSX or sometimes get all offended and say of course they had heard of it, just forgot to mention in their blog.

Anyway, to fight back I am going to try an explain ABAP2XLSX as best I can and why it is a Good Thing.

First off ABAP2XLSX is an open-source project which can be found on the GitHub repository mentioned below.

[abap2xlsx/abap2xlsx: Generate your professional Excel spreadsheet from ABAP (github.com)](https://github.com/abap2xlsx/abap2xlsx)

Its purpose is to move data between Excel and ABAP. Any classes you see in my demo program with “EXCEL” in their name come from the ABAP2XLSX repository.

The last blogs in this new series I posted can be found at: -

<https://blogs.sap.com/2023/01/12/monthly-abap-to-excel-blog-january-2023/>

<https://blogs.sap.com/2023/02/11/monthly-abap-to-excel-blog-february-2023/>

The GitHub repository for my evolving demonstration program is

[hardyp/ABAP2XLSX\_EXAMPLES: ABAP2XLSX Examples (github.com)](https://github.com/hardyp/ABAP2XLSX_EXAMPLES)

using local package $ABAP2XLSX\_PDH\_DEMO. There will be several versions of the same program (Z\_ABAP2XLSX\_PDH\_DEMO) one per blog, and you can download them to your development system using abapGit. The version I talk about in this blog is Z\_ABAP2XLSX\_PDH\_DEMO\_V02.

**Halley’s Comment**

The good thing about posting blogs on SCN is the comments you get. Some suggest positive improvements to the demo code, and even the negative comments can be valuable if they are written in a constructive manner rather than just “you are an idiot”. I already knew that last fact.

* Some people got confused that I did not really explain what ABAP2XLSX was and just started using classes like ZCL\_EXCEL out of the blue. So, I have updated the blurb at the start of these blogs.

* It was pointed out I had used Hungarian Notation in the example program (e.g., LD\_TITLE instead of just TITLE). That is a Bad Thing and so in the second version of the demo program the prefixes have vanished from the local variables. I keep them for member variables and parameters – in this case the prefix does not denote the variable *type* because a good name can denote that, but rather the *scope*. I suppose in theory a name could also denote the scope, but I cannot think of a good way to do this. Any suggestions welcome.

* I was submitting the SOST program for no good reason in the example. The suggested improvement was to set the “send immediately” flag which is now done in the second version.

**What’s New Pussycat?**

With each blog now, we will pretend one or more new business requirements have come in. In each case the business will say to you “This ABAP2XLSX thing is no good, because after the spreadsheet has been emailed to me, I have to manually do XYZ in Excel”.

The point is that anything you can do manually in Excel you can do programmatically via ABAP2XLSX

**Why is that then?**

Some of us older types remember when the suffix for an Excel file was just XLS as opposed to XLSX. That was when dinosaurs walked the Earth, and everything was made of wood. The added “X” at the end is to indicate that “under the hood” as it were an Excel spreadsheet is really an XML document. Same with Word documents, same with PowerPoint and so on.

So, what Ivan Femia thought to himself was thus – since you can generate XML documents programmatically from ABAP, and a spreadsheet is an XML document, therefore you can generate spreadsheets from ABAP.

The reverse is of course true, ABAP can read the contents of an XML document, and can therefore read the contents of a spreadsheet right down to the font and colour and so forth of each cell as well as the contents. In a subsequent blog you will see why that is important as when you send someone a spreadsheet to fill out for later upload into SAP they will “improve” that spreadsheet by re-arranging all the columns and adding ten blank rows at the top and so on and so forth, and then expecting the new layout to upload just fine. With ABAP2XLSX you can say “Ha! Ha! Do your worst! I will be able to upload it anyway!”

**Ready Playback One**

You may recall the days before SAP created BAPIs and other APIs for all common business objects. You had to use a BDC to record the manual steps needed for a transaction, use the recording to generate a skeleton program, and then change that program to provide dynamic...