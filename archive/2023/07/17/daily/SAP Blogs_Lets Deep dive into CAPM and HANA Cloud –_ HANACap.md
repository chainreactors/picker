---
title: Lets Deep dive into CAPM and HANA Cloud –> HANACap
url: https://blogs.sap.com/2023/07/16/lets-deep-dive-into-capm-and-hana-cloud-hanacap/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:29.166180
---

# Lets Deep dive into CAPM and HANA Cloud –> HANACap

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Lets Deep dive into CAPM and HANA Cloud --> HANACa...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161857&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Lets Deep dive into CAPM and HANA Cloud --> HANACap](/t5/technology-blog-posts-by-members/lets-deep-dive-into-capm-and-hana-cloud-gt-hanacap/ba-p/13560227)

![shivamshukla12](https://avatars.profile.sap.com/e/b/idebda0bbe9c5285574cf95111f2903eaf30d77594d0cfdf3e3d6bcb3be77f2e14_small.jpeg "shivamshukla12")

[shivamshukla12](https://community.sap.com/t5/user/viewprofilepage/user-id/16613)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161857)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161857)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560227)

‎2023 Jul 16
9:03 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161857/tab/all-users "Click here to see who gave kudos to this post.")

2,096

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (6)

Hello everyone!

I hope you're coding and having a great time!!!

Currently, I am engaged in working on various BTP (Business Technology Platform) services, and designing and development constitute my everyday tasks. As expected, we encounter some challenges along the way, which is quite normal ![:slightly_smiling_face:](/html/@CB4E4CB9DC3C08A3AD56D3C681CE34D1/emoticons/1f642.png ":slightly_smiling_face:") Therefore, I've decided to document these challenges along with their corresponding solutions in my GitHub repository. This compilation is expected to grow into a substantial list over time, but for now, I have already included two challenges and their respective solutions.

## **Pre-requisite:**

* Get your BTP Trial Account setup before you jump into Coding ![:slightly_smiling_face:](/html/@CB4E4CB9DC3C08A3AD56D3C681CE34D1/emoticons/1f642.png ":slightly_smiling_face:") + VSCode or BAS

### **Here you go GitHub Repo - <https://github.com/shivamshukla12/SAP-CAP/tree/main>**

* #### Write your first CAP Application -  Its a simple one Hello World

* #### Create one entity in your CAP App and Insert  / Retrieve some Hard coded Values

* #### Add some CSV Data in your CAP Application

* #### Run and retrieve your CSV Data

* #### Connect your CAP Application to BTP Space

* #### Provision Services for your CAP Application

* #### Enable HANA Cloud Instance and Add HDI Containers

* #### Build and Deploy your CAP Application on CF ( Cloud Foundry )

* #### Run and Debug your CAP Application

### **Tutorial Highlights:**

![](/legacyfs/online/storage/blog_attachments/2023/07/15-6.png)

Say Hello to SAP CAP

![](/legacyfs/online/storage/blog_attachments/2023/07/16-5.png)

Supplier Entity for Projection

![](/legacyfs/online/storage/blog_attachments/2023/07/17-5.png)

Supplier JS File For logic and data export

###

### GET Request :

Using CDS in CAP -  you can simply write select statement and Wrap it in NodeJS and run the query to get data back from the database

**POST Request :**

Using CDS in CAP - you can make POST Calls directly on Entity exposed which will Create New entry in Database

**Delete Request :**

Using CDS in CAP - You can use custom handler function to delete records from the database - A Custom logic or i would say simply wrap your delete statement in Nodejs and run it on CDS.

###

# Highlights

![](/legacyfs/online/storage/blog_attachments/2023/07/18-6.png)

CRUD Operations in CAP Entity

###

###

## **Coming up Next...**

* ```
   How SQL is giving the real value to your cloud Application Programming -- SQL is the magic
  ```

* ```
   Working with multiple entities and Association
  ```

* ```
   Projection , Aggregate functions and Joins
  ```

* ```
   Function Import in CAP
  ```

Keep Learning and Keep Sharing ![:slightly_smiling_face:](/html/@CB4E4CB9DC3C08A3AD56D3C681CE34D1/emoticons/1f642.png ":slightly_smiling_face:")

PS: I will Keep posting Updates in my this blog and Updating  the repo for promised exercises

Thanks Shivam

* [build your first application on sap hana cloud platform](/t5/tag/build%20your%20first%20application%20on%20sap%20hana%20cloud%20platform/tg-p/board-id/technology-blog-members)
* [CAP](/t5/tag/CAP/tg-p/board-id/technology-blog-members)
* [capm](/t5/tag/capm/tg-p/board-id/technology-blog-members)
* [CAPProgramming](/t5/tag/CAPProgramming/tg-p/board-id/technology-blog-members)
* [Node.js](/t5/tag/Node.js/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Flets-deep-dive-into-capm-and-hana-cloud-gt-hanacap%2Fba-p%2F13560227%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP BTP CI CD service for on premise S4 HANA systems RICEFW applications](/t5/technology-q-a/sap-btp-ci-cd-service-for-on-premise-s4-hana-systems-ricefw-applications/qaq-p/14234519)
  in [Technology Q&A](/t5/tech...