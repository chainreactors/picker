---
title: Monthly ABAP to EXCEL Blog – February 2023
url: https://blogs.sap.com/2023/02/11/monthly-abap-to-excel-blog-february-2023/
source: SAP Blogs
date: 2023-02-12
fetch_date: 2025-10-04T06:25:53.106200
---

# Monthly ABAP to EXCEL Blog – February 2023

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Monthly ABAP to EXCEL Blog – February 2023

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47420&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Monthly ABAP to EXCEL Blog – February 2023](/t5/application-development-and-automation-blog-posts/monthly-abap-to-excel-blog-february-2023/ba-p/13568128)

![hardyp180](https://avatars.profile.sap.com/7/0/id70fe549259937f2b1b98e44da0f7bd9453cb5df35004602e05d40b6523508cb7_small.jpeg "hardyp180")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[hardyp180](https://community.sap.com/t5/user/viewprofilepage/user-id/13778)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47420)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47420)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568128)

‎2023 Feb 11
8:37 AM

[23
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47420/tab/all-users "Click here to see who gave kudos to this post.")

10,753

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

**Monthly ABAP to EXCEL Blog – February 2023**

For over ten years now every month on the SAP Community Site someone publishes a blog about how to upload/download data from EXCEL to ABAP. So, I am going to start doing this as well - only I will always be talking about ABAP2XLSX as the preferred mechanism to do this.

![](/legacyfs/online/storage/blog_attachments/2023/02/Excel-01.jpg)

Excel Blogs

The 120 blogs posted over the last ten years usually never mention ABAP2XLSX at all. They either talk about the archaic OLE technology that can be used to communicate with Microsoft products or re-invent the ABAP2XLSX concept.

Then myself and about three or four other people (the “usual suspects” as I call them) will post in the comments section talking about ABAP2XLSX and the original poster will either admit they had never heard of ABAP2XLSX or sometimes get all offended and say of course they had heard of it, just forgot to mention in their blog.

The most wonderful thing that happened this week was that as an experiment someone got CHAT GPT to write a blog on how to download from ABAP to Excel. It did a better job than some of the hundreds I have read.

Anyway, to fight back I am going to try an explain ABAP2XLSX as best I can and why it is a Good Thing.

The last blog in this new series I posted can be found at: -

<https://blogs.sap.com/2023/01/12/monthly-abap-to-excel-blog-january-2023/>

**Footfall**

Now in some ways I am going to start off by shooting myself in the foot. As well as putting example code I am going to also create a public GitHub repository so people can download the examples via abapGit.

This immediately begs the question – if the reason assorted people do not want to use ABAP2XLSX is because of a hatred/fear of anything remotely open-source plus a fictitious “no open-source” policy then why in the world would they go anywhere near GitHub in a billion years? The answer is of course they will not, but as it turns out the no open-source brigade have no problem at all copying code off an SCN blog into their development systems – after all if they had a problem with that concept then why in the world would they post their own code on SCN every month and expect other people to download that code to their development systems?

**Monsieur Example-Mousse**

A lot of examples on the internet – and indeed the standard ABAP2XLSX demo programs – are divorced from any actual use cases and consist of an executable program which does whatever is being demonstrated in as few lines as possible so as not to distract from the point being made.

That makes sense does it not? But I cannot do it. I cannot write a program, even as an example, which just has everything after START-OF-SELECTION in a big, coagulated mass without even any FORM routines, let alone methods.

So, I am going to shoot myself in the foot again and have an example OO program with methods. The reason that is such a bad decision of my part is that many of the opponents of ABAP2XLSX dislike it *because* it is all classes and methods and new-fangled nonsense like that.

However, if after 23 years every new ABAP code example on the internet is still made up of all FORM routines, then new people will still think FORM routines are the go.

The B-side is that for incredibly simple example OO programs take one billion times more code than the procedural code – leading the observation that whilst reading a blog about transforming a procedural program to the OO equivalent someone said “the <better> the code gets the longer and more complicated it is”. Meaning it is not better at all.

I would of course disagree on the grounds that in the real-world simple programs never stay simple – they expand at a geometric rate and once a program reaches a certain (quite small really) size then it is easier to maintain it going forward if it is written in an OO manner.

I will however make a slight compromise and use – for the example data - SFLIGHT as opposed to Monsters.

**Use Casey Jones, Working on the Railroad**

So as a starting point we are going to be displaying the good old SFLIGHT table in class CL\_SALV\_TABLE (which is not editable by the way, did I ever mention that?)

Much as the IT world hates it the truth is that 99.99% of data generated out of SAP reports ends up getting downloaded to Excel and then having all sorts of further processing done on that data at the Excel level. This is so called “Spreadsheet Hell” – so called by software vendors who are trying to convince you to stop using Excel altogether and buy their alternative instead.

As another alternative perhaps another way forward is to stop trying to be King Canute and ordering the tide to go back out but instead working with reality and improving the bi-directional integration between SAP and Excel.

With ABAP2XLSX you have three options once you have turned your ALV grid into a spreadsheet: -

* Show that spreadsheet “in place” embedded inside the SAP GUI

* Download the spreadsheet to your local PC

* Email the spreadsheet to yourself or someone else (who will then open the XLSX attachment and then download it to their local PC if they feel like it)

The st...