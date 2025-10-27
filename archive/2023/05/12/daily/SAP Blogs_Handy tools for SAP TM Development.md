---
title: Handy tools for SAP TM Development
url: https://blogs.sap.com/2023/05/11/handy-tools-for-sap-tm-development/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:37.275603
---

# Handy tools for SAP TM Development

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Handy tools for SAP TM Development

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5145&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Handy tools for SAP TM Development](/t5/supply-chain-management-blog-posts-by-sap/handy-tools-for-sap-tm-development/ba-p/13569917)

![bence_toth](https://avatars.profile.sap.com/d/e/iddea327eced8a08dc309a92818d1d9ecc58788e8847cac3348276819bc8328c6e_small.jpeg "bence_toth")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[bence\_toth](https://community.sap.com/t5/user/viewprofilepage/user-id/214846)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5145)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5145)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569917)

‎2023 May 11
7:25 PM

[28
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5145/tab/all-users "Click here to see who gave kudos to this post.")

8,375

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

## Intended Audience

You are

* an SAP TM Developer or Consultant.

* familiar with the ABAP programming language, BOPF framework.

You have already

* faced the difficulties of GUIDs, determination/validation cycles.

* debugged TM ABAP code.

* got lost in the call stack / complexity of a debugger session.

You would like to understand

* which BOPF action is responsible for setting a certain field?

* how does the TM application work within the BOPF framework?

* what is the actual execution sequence of actions and determinations?

## Introduction

In this blog post I would like to show you how I use the following tools in SAP TM maintenance:

* Notepad++:                     to deal with GUIDs.

* Change Documents:      to investigate the crime scene.

* TM BOPF Navigator:     for free style search, navigation, and where-used-list of BOPF objects.

* Debugger script /SCMTMS/DS\_TRACE: to quickly identify, which code is responsible for certain changes, and to visualize the program flow.

Disclaimer:

Debugger script /SCMTMS/DS\_TRACE was written as an internal support tool. Though officially not supported, any feedback is highly appreciated and will be considered. Please be aware that certain gaps, features, fixes to bugs – that would absolutely make sense – may never be implemented.

##

## Notepad++

As a complementary tool, I use application Notepad++ from <https://notepad-plus-plus.org/> to find identical GUIDs with a double click:

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture16-8.png)

Figure 1: Notepad++ \* Click to enlarge \*

In this screenshot, you can see the data I have copied from database tables and double clicked on one of the ROOT GUID. When working in a debugger session, I regularly copy the content of internal tables into Notepad++ and use this feature to quickly identify TOR documents with PARENT\_KEY or item hierarchy with ITEM\_PARENT\_KEY, for example

## Change Documents

Whenever someone asks: “This field value was changed, why?”, your first task is to identify when it has happened. So that we could identify the exact process as a first step to provide a step-by-step reproduction.

This can be identified from the “Change Documents” tab, Transaction Code:

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture17-4.png)

Figure 2: Change Documents \* Click to enlarge \*

As column “Transaction Code” is hidden by default, you will need to add it to the displayed columns. In this screenshot, I have also replaced the description columns with “Node” and “Field Name”, as for me, the technical names are more informative.

Now, what corrections are needed and how can the values under “Transaction Code” be interpreted?
Consulting note #[2951038 -How to use Change Documents, field Transaction Code](https://launchpad.support.sap.com/#/notes/2951038/E)
describes possible values and the existing correction notes.

On the screenshot under column Transaction Code, value /SCMTMS/FRE\_ORDER means, that the change was done on the Freight Order maintenance WebDynpro application. Value /SCMTMS/FWD\_ORDER means the Forwarding Order maintenance WebDynpro application.

Sometimes it is not that easy to identify the origin of a Transaction Code even with the help of consulting note #2951038. Maybe a prefix character could be added to quickly identify the source, in this example “Web Dynpro Application”. What do you think? Can you use “Transaction Code” on the “Change Documents” tab “as is” or would you welcome a prefix character? Please share your opinion in the comment section of this blog!

##

## TM BOPF Navigator

Start TM BOPF Navigator with transaction code /SCMTMS/BONAV.
This is what I would call a fine tool, as it does not need any documentation.
Enter any search term and explore the functionality yourself!

I frequently use it to

* navigate with a double click into ABAP source code directly after vaguely remembering an action name.

* discover the usage of actions via “Where-Used” List

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture18-7.png)

Figure 3: TM BOPF Navigator \* Click to enlarge \*

Please share your improvement ideas for this tool in the comment section, let’s make this even better together!

The latest correction was delivered in the following correction note:
#[3234950 - Technical correction, TM BOBF Navigator 3](https://launchpad.support.sap.com/#/notes/3234950/E).

## Debugger Script /SCMTMS/DS\_TRACE

Some thoughts on debugger scripts if you have not used them before. It can be used to automate what you can also do manually in a debugger session. Here is a blog post how it works: <https://blogs.sap.com/2010/12/14/abap-debugger-scripting-basics/>

You do need a debugger session to be able to execute a debugger script. It means, that you cannot use it to investigate a “not reproducible issue”. It can also not be used for example to trace all users in the background.

It can be used in the following situations/cases:

* A reproducible example is available.

* It is known at which interaction step the issue occurs.

* It can be used to trace a single interaction step.

Selecting “Start New Trace” in transaction /SCMTMS/DS\_TRACE creates a breakpoint in the WebDynpro framework. When you execute the step that you would like to trace in the TM application, the breakpoint will start a debugger session. Then you can load and start the debugger script to trace the execution of ...