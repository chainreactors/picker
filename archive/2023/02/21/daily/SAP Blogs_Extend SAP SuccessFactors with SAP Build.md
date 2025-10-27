---
title: Extend SAP SuccessFactors with SAP Build
url: https://blogs.sap.com/2023/02/20/extend-sap-successfactors-with-sap-build/
source: SAP Blogs
date: 2023-02-21
fetch_date: 2025-10-04T07:36:57.849097
---

# Extend SAP SuccessFactors with SAP Build

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Extend SAP SuccessFactors with SAP Build

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158317&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extend SAP SuccessFactors with SAP Build](/t5/technology-blog-posts-by-sap/extend-sap-successfactors-with-sap-build/ba-p/13551611)

![Alejandro1](https://avatars.profile.sap.com/a/f/idafced0cba95f8154496cc5adf8081a717b74429d46df9af2648acc6ebf290ae6_small.jpeg "Alejandro1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Alejandro1](https://community.sap.com/t5/user/viewprofilepage/user-id/18957)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158317)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158317)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551611)

‎2023 Feb 20
11:53 PM

[35
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158317/tab/all-users "Click here to see who gave kudos to this post.")

9,807

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (5)

Are you looking for a way to extend and customize your HR processes to meet your organization's requirements?

As organizations seek to optimize their HR processes, there is an increasing need for customized workflows that can handle complex logic and provide a higher level of UI customization. While SAP SuccessFactors provides a range of out-of-the-box workflow capabilities, sometimes you might need more flexibility. That's where SAP Build comes in, SAP Build can be used to create custom workflows and applications that are tailored to your organization's unique requirements.

In this blog post, I'll walk you through an example of a custom application built with SAP Build Apps that pulls employee data from SAP SuccessFactors, and on submit it triggers a workflow on SAP Build Process Automation. The goal is to help you gain a better understanding of the integration and extension capabilities of [SAP BTP](https://community.sap.com/topics/business-technology-platform) and SAP SuccessFactors, and provide you with actionable insights for your own projects.

![](/legacyfs/online/storage/blog_attachments/2023/02/Extend-SAP-SuccessFactors-with-SAP-Build-Architecture-3.png)

Architecture

In the upcoming demo video, you'll see a custom HR application built with SAP Build Apps and SAP Build Process Automation, integrated with SAP SuccessFactors. The application pulls employee data from SuccessFactors (the API is filter to only show the employees located in Madrid), triggers a workflow using Build Process Automation, resulting in an email notification.

While this use case is just an example, it demonstrates the integration and extensibility capabilities of SAP SuccessFactors & SAP Build. I hope it has shown you how SAP Business Technology Platform (SAP BTP) and SAP SuccessFactors can be used together to extend and enhance your HR processes. If you're looking for a powerful, scalable solution for custom HR applications that integrate seamlessly with SAP SuccessFactors, I encourage you to explore the many features and capabilities of [SAP BTP](https://blogs.sap.com/tags/8077228b-f0b1-4176-ad1b-61a78d61a847/).

Ready to start building your own custom HR applications and workflows with SAP Build? To get started with SAP Build, visit the [SAP Blog: SAP Build is now available in SAP BTP – Free-Tier](https://blogs.sap.com/2022/11/16/sap-build-is-now-available-in-sap-btp-free-tier/) and sign up for a free tier.

If you are interested to understand how to build this application with SAP Build App, check my Blog: [SAP Build Apps consuming employee data from SAP SuccessFactors](https://blogs.sap.com/2023/02/23/sap-build-apps-consuming-employee-data-from-successfactors/). I'll dive into the technical details of how to use SAP Build Apps to create such an application.

If you have any questions, doubts, or concerns, don't hesitate to post them in the comments or [reach out to the community](https://answers.sap.com/tags/8077228b-f0b1-4176-ad1b-61a78d61a847). We're always here to help you make the most of SAP BTP!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

14 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fextend-sap-successfactors-with-sap-build%2Fba-p%2F13551611%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/142...