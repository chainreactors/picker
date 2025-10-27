---
title: Hacks for Innovation 2022: Experience using SAP Build apps
url: https://blogs.sap.com/2022/12/17/hacks-for-innovation-2022-experience-using-sap-build-apps/
source: SAP Blogs
date: 2022-12-18
fetch_date: 2025-10-04T01:51:40.760212
---

# Hacks for Innovation 2022: Experience using SAP Build apps

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Hacks for Innovation 2022: Experience using SAP Bu...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50813&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Hacks for Innovation 2022: Experience using SAP Build apps](/t5/enterprise-resource-planning-blog-posts-by-sap/hacks-for-innovation-2022-experience-using-sap-build-apps/ba-p/13553282)

![Navin_Krishnan](https://avatars.profile.sap.com/3/3/id333861be0026d19f52ab214bb6005fd5f5530c17acf0d311354726664cddc512_small.jpeg "Navin_Krishnan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Navin\_Krishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/44464)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50813)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50813)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553282)

‎2022 Dec 17
12:26 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50813/tab/all-users "Click here to see who gave kudos to this post.")

1,056

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (4)

I recently had the opportunity to participate in the event **Hacks for Innovation 2022** organised by SAP HIVE, India where our team  built an application using SAP Build apps for the theme **Operational Excellence**. The experience was really rewarding, and I want to share some of the key takeaways from the event.

Hacks for Innovation 2022 is the No-code hackathon using **SAP Build apps**, spanning around the themes of Sustainability, Operational Excellence, and Business User Experience.

Our team chose the theme Operational excellence, where we attempted to improve the experience of using [Maintenance Notification](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/78c09d53839cca11e10000000a44176d.html) (part of Plant Maintenance module) in SAP S/4HANA system with SAP Build apps.

In todays business, Operational excellence helps to improve the quality of products and services, which can lead to increased customer satisfaction. This can help to build customer loyalty and drive business growth.

The use case we attempted to solve has 2 personas:

**Persona 1: Customer,** who would like to have an application to inspect and report the product complaints by scanning the QR code of the product to capture the product details like Product ID, serial number, location etc.. that has issue and create the complaint in the SAP S/4HANA on-premise system.

Customer would then use the application to track the real time status of his complaint.

**Persona 2: Facility Manager,** who would like to use the facility admin application to track all the complaints, update an assignee and modify the status of the complaint which is reflected in real time in SAP S/4HANA on-premise system.

As first step, we explored the APIs relevant to Maintenance Notification in the [API Business Hub](https://api.sap.com/api/API_MAINTNOTIFICATION/resource) and activated the respective oData service in the SAP S/4HANA system.

We have also setup the [SAP Cloud connector](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e6c7616abb5710148cfcf3e75d96d596.html) which serves as a link between the on-premise system and SAP BTP applications. SAP Cloud connector runs as on-premise agent in a secured network and acts as a reverse invoke proxy between the on-premise network and SAP BTP.

Finally, build the application using [SAP Build apps](https://www.sap.com/products/technology-platform/no-code-app-builder.html).

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-17-at-12.08.41-PM.png)

Fresh response - SAP Build apps

One of the things that I appreciated most about SAP Build apps was how user-friendly it is.

Even though its my first time experience with SAP Build apps, I was able to quickly get up to speed with the platform and start building my application. The drag-and-drop interface made it easy to customize the pre-built templates and modules, and I was able to create a functional application in a fraction of the time it would have taken me to code it from scratch.

Another thing that really impressed me about SAP Build apps was the quality of the end result. My application looked professional and worked flawlessly, and I received a lot of positive feedback.

It was clear that SAP Build apps is a powerful and reliable platform that can be used to create high-quality applications.

Our final end to end solution looks like below

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-17-at-12.26.04-PM.png)

Solution Diagram - End to End

Overall, I had an amazing experience using SAP Build apps and I would highly recommend it to anyone (be a professional or a Citizen developer) looking to create a functional application without needing to write code. It's user-friendly, efficient, and produces great results – what more could you ask for?

Our [5min pitch video](https://video.sap.com/media/t/1_zdc2wxnk) explaining the use case and demo.

**Bonus:**

If you are interested in learning more about no-code platforms and their potential in building side-by-side extensions for SAP systems, I recommend checking out this [discovery center mission](https://discovery-center.cloud.sap/missiondetail/4024/4228/)

*Happy Learning and have a great year 2023 !*

Labels

* [Business Trends](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/business%20trends)

* [hackathon](/t5/tag/hackathon/tg-p/board-id/erp-blog-sap)
* [No-Code](/t5/tag/No-Code/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhacks-for-innovation-2022-experience-using-sap-build-apps%2Fba...