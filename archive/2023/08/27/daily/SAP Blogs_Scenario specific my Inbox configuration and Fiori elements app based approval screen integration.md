---
title: Scenario specific my Inbox configuration and Fiori elements app based approval screen integration
url: https://blogs.sap.com/2023/08/26/scenario-specific-my-inbox-configuration-and-fiori-elements-app-based-approval-screen-integration/
source: SAP Blogs
date: 2023-08-27
fetch_date: 2025-10-04T11:59:24.049876
---

# Scenario specific my Inbox configuration and Fiori elements app based approval screen integration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Scenario specific my Inbox configuration and Fiori...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163884&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Scenario specific my Inbox configuration and Fiori elements app based approval screen integration](/t5/technology-blog-posts-by-members/scenario-specific-my-inbox-configuration-and-fiori-elements-app-based/ba-p/13572424)

![junwu](https://avatars.profile.sap.com/e/0/ide0ed02274b8ec87d825e38a027bbe36ab0d065614a3458c5a5423bd1a505a5b6_small.jpeg "junwu")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[junwu](https://community.sap.com/t5/user/viewprofilepage/user-id/126031)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163884)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163884)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572424)

‎2023 Aug 26
4:06 AM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163884/tab/all-users "Click here to see who gave kudos to this post.")

10,786

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Business Workflow](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Workflow/pd-p/271076705480744283548543960420215)

* [SAP Business Workflow

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusiness%2BWorkflow/pd-p/271076705480744283548543960420215)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (2)

For last three weeks, I was struggling with my inbox related task, finally I get it done. I want to share the whole journey. Hopefully it can help you someday.

My system is S4 2022 FPS01, converted from ECC.

Standard configuration can be found here.

[https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/e33b9d6f3eba4869900...](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/e33b9d6f3eba4869900363fc7b340a2d.html?version=2022.001)

First let's talk about the scenario definition.

![](/legacyfs/online/storage/blog_attachments/2023/08/scenario-definition.png)

My system is converted from ECC, when I open the configuration screen, scenario id is already defined, so everything looks good. But when you test, the fiori tile shows count 0 and gives this error popup in the inbox app.

![](/legacyfs/online/storage/blog_attachments/2023/08/2023-08-21_18-54-04.png)

error about scenario definition

![](/legacyfs/online/storage/blog_attachments/2023/08/inbox-1.png)

inbox tile configuration

/sap/opu/odata/IWPGW/TASKPROCESSING;mo;v=2/ScenarioCollection?filter=key eq 'YOURSCENARIO'

When I debug, I can see the code is able to read the scenarioid from url and the spro configuration also has the scenario definition.

![](/legacyfs/online/storage/blog_attachments/2023/08/2023-08-21_18-52-13.png)

success handler for retrieving scenario related data

The odata call  gives nothing back, it triggers the error popup.

![](/legacyfs/online/storage/blog_attachments/2023/08/scenariofailed.png)

SAP's code is querying backend with default ConsumerType='TABLET',

![](/legacyfs/online/storage/blog_attachments/2023/08/tablet-1.png)

consumer TABLET is mandatory

When I check my scenario definition in spro, no consumer type is defined. I have to add the missing configuration

![](/legacyfs/online/storage/blog_attachments/2023/08/consumertype.png)

define consumer type

After that, the error popup is gone, but it still shows 0 in the tile. then I go back to old ecc inbox to debug the same code. luckily I find some difference. in the same method loadInitialAppData, ecc odata call gives much more data for the attribute ScenarioServiceURL, basically it contains all the task definition you included in your defined scenario.

![](/legacyfs/online/storage/blog_attachments/2023/08/scenario-data-1.png)

scenario data

For s4, same call, it gives only one task definition, which is created recently by me for testing. that one record difference gives me an idea that the system may have bug, as it was two systems(gateway&backend) setup for fiori before, in s4, two system merged to one.  so I deleted all the task definition that came from old legacy system and re-created them for the scenario definition.

![](/legacyfs/online/storage/blog_attachments/2023/08/image742533625-4728-d482d722b3ec7df9b812c9d752b97742@2x.jpg)

Tile count is starting working.

![](/legacyfs/online/storage/blog_attachments/2023/08/tile-count.png)

So far it took me a day.

The next part regarding integrating fiori elements app as approval screen is simple one, but it took most of the time, because I missed one parameter in the configuration. When search online, there is no success example, I thought maybe the scenario is not supported, then I was trying a bunch other way to implement it by myself

1. develop a fiori element app and do navigation automatically when it is opened in inbox app

2. develop free style app and wrap a FE app

3. develop FPM(flexible programming model) based app as it can have object page as first page

They all didn't work at the end.

Long story short, here is the answer:

This is the target mapping

**openMode=embedIntoDetailsNestedRouter**

![](/legacyfs/online/storage/blog_attachments/2023/08/target-mapping.png)

Choose Intent-Based Navigation for the task

![](/legacyfs/online/storage/blog_attachments/2023/08/swfvisu.png)

In the visualization parameter you will refer to the target mapping above.

For my case, that uuid parameter is hardcoded, your case maybe different, you may have to get it from the workflow dynamically, like other parameter

![](/legacyfs/online/storage/blog_attachments/2023/08/swfvisu1.png)

In the attachment  of sap note <https://me.sap.com/notes/2305401/E>, it says you have to put application specific parameter in the visualization parameter. you have to "figure out" what is application specific parameter. I put the key components there but missed IsActiveEntity=true. it costed me two weeks

![](/legacyfs/online/storage/blog_attachments/2023/08/cry-1.png)

When you navigate to object page of your fiori element app, you will  find this  in the url (I am using travel expense app as example)

TravelExpense(PersonnelNumber='2540606',TravelTripNumber='600697855',TravelReqUUID=guid'00000000-0000-0000-0000-000000000000',IsActiveEntity=true)

You have to put all the key there.

Let's use the final output to conclude this blog. Have a good weekend everyone.

![](/legacyfs/online/storage/blog_attachments/2023/08/final-1.png)

* [fiori myinbox](/t5/tag/fiori%20myinbox/tg-p/board-id/technology-blog-members)
* [scenario specific inbox](/t5/tag/scenario%20specific%20inbox/tg-p/board-id/technology-blog-members)

6 Comments

You must be a registered user to add a comment. If you've already r...