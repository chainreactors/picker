---
title: Alignment of SAP Focused Build with SAP S/4HANA Projects
url: https://blogs.sap.com/2023/01/29/alignment-of-sap-focused-build-with-sap-s-4hana-projects/
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:03.865337
---

# Alignment of SAP Focused Build with SAP S/4HANA Projects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Alignment of SAP Focused Build with SAP S/4HANA Pr...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161121&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Alignment of SAP Focused Build with SAP S/4HANA Projects](/t5/technology-blog-posts-by-members/alignment-of-sap-focused-build-with-sap-s-4hana-projects/ba-p/13556580)

![Daniel_Enderli](https://avatars.profile.sap.com/f/e/idfebfba3ea1ceebf41ddea8cc08c626c2b7468602b70bd873fbaed2d689a7e574_small.jpeg "Daniel_Enderli")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Daniel\_Enderli](https://community.sap.com/t5/user/viewprofilepage/user-id/2995)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161121)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161121)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556580)

‎2023 Jan 29
10:38 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161121/tab/all-users "Click here to see who gave kudos to this post.")

2,821

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SOLMAN Project Management](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Project%2520Management/pd-p/859834545111167391953063734572784)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Project Management

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BProject%2BManagement/pd-p/859834545111167391953063734572784)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (6)

# Introduction

Based on the experiences from several SAP S/4HANA projects, I can definitely say that adapting SAP Focused Build to the SAP S/4HANA project methodology is an essential key to success.

Regardless of whether the approach is greenfield, brownfield or selective data transition, with all these approaches it is nevertheless important to synchronize the topic of SAP ALM with the project right from the start and thus at an early stage.

***«Involve the people who are responsible in the project and make them participants.»***

Depending on which ALM functionalities and how deep and integrated you want to use them in the project, you can choose either the SAP Solution Manager with Focused Build or SAP Cloud ALM. Of course, there are often many other supporting tools that can be used and integrated for planning and controlling a project. However, in this blog post I focus on the SAP-centric ALM tools. I show how these can be optimally coordinated with the project.

## Adaptation of SAP Focused Build on SAP S/4HANA projects

As a first step, it is important that the program/project planning is aligned with, in this specific example, SAP Focused Build. At Swisscom, we have defined five steps to answer the essential questions for an effective alignment. The goal of these five steps is to ensure that the Focused Build Requirements to Deploy process is properly dovetailed with project planning and project control.

![](/legacyfs/online/storage/blog_attachments/2023/01/alignment_02-scaled.jpg)

Source: Swisscom, Alignment of SAP Focused Build with SAP S/4HANA Projects

## Defining the project procedure model and using accelerators

At the beginning of a project, it must also be determined according to which project procedure model the SAP S/4HANA project is to be processed. Traditionally based on waterfall, agile process methodology or a mixture of waterfall and agile and thus a hybrid model.

SAP already has various best practice approaches for this, which can be adapted to your own project with manageable effort.

![](/legacyfs/online/storage/blog_attachments/2023/01/agile-build.jpg)

Source: SAP, Project procedure and accelerators

## Project Setup in Focused Build

Based on the previous clarifications and their results, the appropriate structures for project, releases, cycles, waves and sprints can then be mapped in Focused Build.

Here it is important that the plan data of the project plan is kept in sync with the plan data in Focused Build.

I would also like to emphasize once again that Focused Build can be used both for a waterfall method (see variant 1 in the picture) and for an agile method (see variants 2 and 3 in the picture).

![](/legacyfs/online/storage/blog_attachments/2023/01/fb-projects-scaled.jpg)

Source: SAP, Focused Build project variants

## Alignment of roles, tasks and responsibilities

Next, the roles, tasks, and responsibilities must be aligned. In SAP Focused Build there are predefined roles for which many helpful SAP Fiori apps are available. This involves comparing the roles defined in the project with the SAP Focused Build roles. Each role has interfaces to other roles. It is therefore very important to clearly describe the transfer of the individual deliverables to a subsequent role.

![](/legacyfs/online/storage/blog_attachments/2023/01/roles.jpg)

Source: Swisscom, Alignment of roles, tasks and responsibilities

## Focus on the 10 SAP Quality Principles

It is always helpful to regularly recall the 10 SAP Quality Principles. Ask yourself how you would like to implement this operationally. Also ask yourself who is responsible for these Principles and how they can be continuously monitored.

The following illustration shows very nicely which SAP Focused Build tools cover which quality principles. Here, too, an alignment of Quality Principle with Focused Build functionality is required at a deeper level.

![](/legacyfs/online/storage/blog_attachments/2023/01/quality-principles.jpg)

Source: SAP, SAP Quality Principles supported by Focused Build

## Further success factors

To conclude, I would like to list a few other success factors that also contribute significantly to the successful use of Focused Build in a SAP S/4HANA project.

![](/legacyfs/online/storage/blog_attachments/2023/01/further-sf-scaled.jpg)

Source: Swisscom, Further succe...