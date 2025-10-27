---
title: Getting BTP user information in AppGyver
url: https://blogs.sap.com/2022/10/24/getting-btp-user-information-in-appgyver/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:39.229236
---

# Getting BTP user information in AppGyver

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Getting BTP user information in AppGyver

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158704&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Getting BTP user information in AppGyver](/t5/technology-blog-posts-by-sap/getting-btp-user-information-in-appgyver/ba-p/13552700)

![MarcHuber](https://avatars.profile.sap.com/b/f/idbf68913d04e2bd22420dcb52e4327b500252006467dd795a8b0c429a1cd35e6d_small.jpeg "MarcHuber")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MarcHuber](https://community.sap.com/t5/user/viewprofilepage/user-id/13080)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158704)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158704)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552700)

‎2022 Oct 24
7:50 PM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158704/tab/all-users "Click here to see who gave kudos to this post.")

5,278

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (2)

**Introduction**

Are you using the BTP Authentication feature in your AppGyver app and you want to know who is using the application?

In this guide I will explain quickly how to get the logged-in user information as email, first name or last name.

**Steps**

1. Create a REST API data source

2. Define a data variable

3. Display user data

1. **Create a REST API data source**

Go to the DATA tab and create an AppGyver classic data entity ->  REST API direct integration.

Call the data source **userApi**

![](/legacyfs/online/storage/blog_attachments/2022/10/logged1-1.png)

AppGyver classic data entity - REST API

Set the settings to:

Resource ID: userAPI

Resource URL: user-api/currentUser

![](/legacyfs/online/storage/blog_attachments/2022/10/userAPI.png)

BASE userApi

Define the GET RECORD (GET) without an URL Placeholder and remove the /{id} from the Relative path.

![](/legacyfs/online/storage/blog_attachments/2022/10/logged3.png)

get Record (GET)

Go to the SCHEMA Tab and create the following schema by clicking ADD Property.

You need displayName, email, firstname, lastname, name all type of text. Additionally you need scopes as list of texts.![](/legacyfs/online/storage/blog_attachments/2022/10/logged4.png)

Add schema properties

**2. Define a data variable**

Add a new data variable for the userAPI as data variable type “Single data record” and modify the logic that it just get the records and set the data variable. Remove the delay part.

![](/legacyfs/online/storage/blog_attachments/2022/10/logged5.png)

data variable userApi

**3. Display the user information**

Now you can use the data variable userApi to display the logged-in user information.

![](/legacyfs/online/storage/blog_attachments/2022/10/logged6.png)

Bind text field to data variable

**Final result**

![](/legacyfs/online/storage/blog_attachments/2022/10/logged7.png)

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

20 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fgetting-btp-user-information-in-appgyver%2Fba-p%2F13552700%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9m ago
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  45m ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  53m ago
* [Replicating IT0006 to SAP ECP with a fixed address value, excluding address information in SF EC](/t5/technology-blog-posts-by-members/replicating-it0006-to-sap-ecp-with-a-fixed-address-value-excluding-address/ba-p/14234216)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 hours ago
* [Is there a way to dynamically change the names and legends of measure items in SAC?](/t5/technology-q-a/is-there-a-way-to-dynamically-change-the-names-and-legends-of-measure-items/qaq-p/14234032)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  5 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457dbe84b4_small.jpeg "FranciscoHurtado")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") FranciscoHurtado](/t5/user/viewprofilepage/user-id/170459) | 10 |
| [![CarineTchoutouo](https://avatars.profile.sap.com/9/d/id9d3dd02b884098ed83600846c6bfd4f3b6aba5b4657b084d98aea0fc87214b66_small.jpeg "CarineTchoutouo")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") CarineTchoutouo](/t5/user/viewprofilepage/user-id/1462) | 8 |
| [![marc_steinert](https://avatars.profile.sap.com/e/8/ide87ef5876c7e6b7e3cd441b...