---
title: Creation of bgRFC and calling in a program
url: https://blogs.sap.com/2023/03/15/creation-of-bgrfc-and-calling-in-a-program/
source: SAP Blogs
date: 2023-03-16
fetch_date: 2025-10-04T09:44:34.957565
---

# Creation of bgRFC and calling in a program

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creation of bgRFC and calling in a program

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163411&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creation of bgRFC and calling in a program](/t5/technology-blog-posts-by-members/creation-of-bgrfc-and-calling-in-a-program/ba-p/13569644)

![MOHANVADDE](https://avatars.profile.sap.com/3/a/id3a6d4fa3102ba66a47ae58604d5f45693dc2b599cbe4ad484f40a91b45977788_small.jpeg "MOHANVADDE")

[MOHANVADDE](https://community.sap.com/t5/user/viewprofilepage/user-id/796419)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163411)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163411)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569644)

‎2023 Mar 15
6:38 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163411/tab/all-users "Click here to see who gave kudos to this post.")

17,822

* SAP Managed Tags
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [NW ABAP Remote Function Call (RFC)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Remote%2520Function%2520Call%2520%28RFC%29/pd-p/100394580653750417561290171292438)

* [NW ABAP Remote Function Call (RFC)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BRemote%2BFunction%2BCall%2B%252528RFC%252529/pd-p/100394580653750417561290171292438)
* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

> ### Description:
>
>
>
>
> 1. #### What is bgRFC.
>
> 2. #### bgRFC configuration.
>
> 3. #### bgRFC programming.
>
> 4. #### bgRFC Monitoring.
>
>
>
>
>
> ### **1. What is bgRFC?**
>
>
> The bgRFC allows application to record data that is received later by a called
>
> application. When the data is received, we must ensure that the data was transferred to
>
> the receiver either once only in any order(transactional) or once only in the order of
>
> creation(queued).
>
>
>
> ### 2. bgRFC Configuration?
>
>
>
>
> * #### Creation of supervisor Destination.
>
>
>
> This is a mandatory step because the bgRFC can only function if a supervisor
>
> destination has been define for bgRFC processing. For creation of supervisor
>
> destination the t-code is ***SBGRFCCONF***.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_1.png)
>
>
>
> bgRFC\_Configuration\_1
>
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_2.png)
>
>
>
> bgRFC\_Configuration\_2
>
>
>
>
> ### Prerequisite:
>
>
> Need to verify the supervisor destination as an RFC destination using the transaction
>
>  ***SM59***. This destination must be defined as either an ABAP connection or a logical
>
> connection.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_3.png)
>
>
>
> bgRFC\_Configuration\_3
>
>
> A user, password, and client must be entered for both connection types. Please refer
>
> the attached screenshot.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_4.png)
>
>
>
> bgRFC\_Configuration\_4
>
>
>
>
> ### ABAP Connection :
>
>
> No load balancing can be defined.
>
> No system number can be entered.
>
> No server can be entered.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_5.png)
>
>
>
> bgRFC\_Configuration\_5
>
>
>
>
> ### **Creation of destination:**
>
>
> We have to create inbound/outbound destination name based on the requirement.
>
>
>
> **Creation of Inbound Destination:**
>
> On the define inbound Dest. Tab page in the transaction ***SBGRFCCONF***, we can
>
> maintain a separate inbound destination for each application. This is also mandatory
>
> step to create any inbound bgRFC.
>
>
>
> Logon/Server group can be defined using transaction ***RZ12***.
>
>
>
> All the settings and activities related to the transaction ***SBGRFCCONF*** is BASIS related
>
> activity so before creating/configuring any bgRFC please consult with BASIS team.
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_6.png)
>
>
>
> bgRFC\_Configuration\_6
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_7.png)
>
>
>
> bgRFC\_Configuration\_7
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_8.png)
>
>
>
> bgRFC\_Configuration\_8
>
>
>
>
> #### **Creation of outbound destination:**
>
>
> We can create outbound destination using transaction ***SM59***. Creation of outbound
>
> destination in ***SM59*** is normal like any of the destination creation. Please refer the
>
> below screenshot for reference.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_9.png)
>
>
>
> bgRFC\_Configuration\_9
>
>
>
>
> We have to created outbound destination under ABAP Connections. For this destination
>
> we have to maintain the necessary target destination IP, system no etc. Please refer all
>
> the below screenshots for detailed setting in each tab.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_10.png)
>
>
>
> bgRFC\_Configuration\_10
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_11.png)
>
>
>
> bgRFC\_Configuration\_11
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_12.png)
>
>
>
> bgRFC\_Configuration\_12
>
>
>
>
> After creation of the outbound destination in ***SM59*** we have to maintain this destination
>
> in ***SBGRFCCONF*** transaction. We have to maintain the destination in Scheduler
>
> Destination tab of transaction ***SBGRFCCONF***. Please refer the below screenshot.
>
>
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Configuration_13.png)
>
>
>
> bgRFC\_Configuration\_13
>
>
>
>
> ### 3. bgRFC Programming
>
>
> After the entire configuration now let’s talk about the programming.
>
>
>
>
> * #### Creation of unit:
>
>
>
> We have to create one bgRFC unit by taking the reference from the configured
>
> inbound/outbound destination name. Destination objects can be requested using the
>
> class methods from the class CL\_BGRFC\_DESTINATION\_OUTBIUND for the
>
> outbound and the class CL\_BGRFC\_DESTINATION\_INBOUND for the inbound. We
>
> have to use method create of the above mentioned class to create a destination object.
>
> Please see the below example of how to create an inbound destination object.
>
>
>
> Pass any of the configured inbound destination name in the below mentioned variable.
>
>
>
> Call the below mentioned method to create reference of inbound destination.
>
> ![](/legacyfs/online/storage/blog_attachments/2023/03/bgRFC_Programming_1.png)
>
>
>
> bgRFC\_Progr...