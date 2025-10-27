---
title: First look into SAP Build & SAP Build Apps – QA
url: https://blogs.sap.com/2022/11/20/first-look-into-sap-build-sap-build-apps-qa/
source: SAP Blogs
date: 2022-11-21
fetch_date: 2025-10-03T23:19:15.847719
---

# First look into SAP Build & SAP Build Apps – QA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* First look into SAP Build & SAP Build Apps – QA

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160388&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [First look into SAP Build & SAP Build Apps – QA](/t5/technology-blog-posts-by-members/first-look-into-sap-build-sap-build-apps-qa/ba-p/13552093)

![AdrDen](https://avatars.profile.sap.com/8/2/id82022e4fc3c5f4d60fbf88946f30becef0ff133f962789641f23532e5c381db8_small.jpeg "AdrDen")

[AdrDen](https://community.sap.com/t5/user/viewprofilepage/user-id/362972)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160388)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160388)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552093)

‎2022 Nov 20
8:16 AM

[25
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160388/tab/all-users "Click here to see who gave kudos to this post.")

6,120

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Build Work Zone, standard edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520standard%2520edition/pd-p/73554900100800003081)
* [SAP Build Work Zone, advanced edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520advanced%2520edition/pd-p/73555000100800002781)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Build Work Zone, advanced edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Badvanced%2Bedition/pd-p/73555000100800002781)
* [SAP Build Work Zone, standard edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Bstandard%2Bedition/pd-p/73554900100800003081)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (6)

It might be a bit confusing for the developers to understand what **SAP Build** actually is, so I would like to bring some light to the topic, based on my experiences from sessions on SAP TechEd 2022.

In this blog I would like to answer basic technical questions related to SAP Build & SAP Build Apps.

#### ***Is SAP Build related to the old Build prototyping tool for Fiori?***

No, it's not. Former build.me (SAP Build Classic) is in sunset. See an update [here](https://blogs.sap.com/2021/02/18/sap-build-sunset-update-one-year-later/).

A preffered tool for SAP Fiori apps sketching is [Figma](https://experience.sap.com/fiori-design-web/design-stencils-for-figma/).

#### ***What SAP Build actually is?***

**SAP Build** is a set of tools combining:

* SAP Build Apps (formerly SAP AppGyver)

* SAP Build Process Automation (formerly SAP Process Automation)

* SAP Build Work Zone standard edition (formerly Launchpad Service)

* SAP Build Work Zone advanced edition (formerly WorkZone)

In general SAP Build is a low-code solution portfolio and re-branding around **AppGyver**, which seems to be heart of the concept. See a nice overview [here](https://github.com/SAP-samples/teched2022-AD280/blob/main/intro/overview.md).

**SAP Build Apps** is an evolution of AppGyver. SAP Build Apps adds additional application-building capabilities such as authentication, data integration, or lifecycle management.

#### ***Is SAP Build Apps (former AppGyver) available free-tier?***

Yes, it is. See the prerequisites and subscription guide [here](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/01225b6b951d425c97b58a834a1ff484.html).

#### ***Can I build UI5 prototypes with SAP Build Apps?***

No, it's not possible to create UI5 protoypes using this tool. It's a no-code tool enabling users to create business apps without requiring programming skills.

#### ***What I can build using SAP Build Apps?***

SAP Build Apps can be used to develop desktop, web-based, and mobile applications.

#### ***Can I use my old AppGyver projects in SAP Build Apps?***

Yes, it is possible to reach existing AppGyver projects in a new tool. The new backend functionality works together with what was formerly called SAP AppGyver.

#### ***Can we include SAP Build Apps apps in a Launchpad Service, so they can be accessed via browser or Mobile Start?***

Yes, it is possible.

#### ***Can I create my own themes for apps?***

Yes, you can create your own themes via Theme Variables, so it's ready to be consumed in the projects.

#### ***How can I consume data in my apps?***

You can use OData Services and BTP Destinations or create entities using Visual Cloud Functions. Visual Cloud Functions is a persistency layer for SAP Build Apps, so think it's a database (based on postgres db running on SAP BTP).

#### ***How can we compare SAP Build Apps with SAP Mobile Services Mobile Development Kit?***

MDK is a pro-code offering, while SAP Build Apps is a no-code citizen dev tool. Both can be used to develop mobile Android and iOS applications. MDK supports offline scenarios.

#### ***Can I use offline for my OData in SAP Build Apps?***

As of now offline is not supported with SAP Build Apps.

#### ***How can we distribute SAP Build Apps and handle different tenants (Development, Quality, Production)? Is there any app versioning?***

Once the apps design is completed, it is needed to build the project. If you build the project as MTAR type, you can use Transport Management Service to deploy the app to different subaccounts. There's also a history functionality available, that allows you to review previous states of the app. Release management is a built-in feature too.

#### ***Can we create roles for the apps and restrict access based on them?***

It's not yet supported. You can share your app with other stakeholders, who can work as admins, developers or viewers, but it's not possible to restrict the access wth so-called role concept.

#### ***Is there an option to create custom components for SAP Build Apps?***

Currently, you cannot create own components, but it's in the roadmap for 2023.

#### ***How can we collaborate on the projects?***

There's a project sharing feature in the lobby, enabling real-time collaboration on SAP Build Apps projects.

## References

[SAP Build: What’s Under the Hood?](https://news.sap.com/2022/11/sap-build-capabili...