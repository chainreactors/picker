---
title: Cloud Economics (aka FinOps) with SAP BTP
url: https://blogs.sap.com/2023/06/28/cloud-economics-aka-finops-with-sap-btp/
source: SAP Blogs
date: 2023-06-29
fetch_date: 2025-10-04T11:47:54.467189
---

# Cloud Economics (aka FinOps) with SAP BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cloud Economics (aka FinOps) with SAP BTP

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163563&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Economics (aka FinOps) with SAP BTP](/t5/technology-blog-posts-by-members/cloud-economics-aka-finops-with-sap-btp/ba-p/13570494)

![gsimeone](https://avatars.profile.sap.com/6/e/id6e63b8074215f9b21ef277d5c2402862dd7e36f8cc2a364fb87ba76c376c7412_small.jpeg "gsimeone")

[gsimeone](https://community.sap.com/t5/user/viewprofilepage/user-id/12834)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163563)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163563)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570494)

‎2023 Jun 28
3:46 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163563/tab/all-users "Click here to see who gave kudos to this post.")

6,249

* SAP Managed Tags
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (1)

Approaching business-critical applications and solutions on the cloud, primarily PaaS and SaaS, indicates cloud maturity and a cloud-centric mindset. Typically, it indicates that a PoC (Proof of Concept), or a Pilot has been validated and that the business case is sound; therefore, we can proceed to the next stage. Today, we are pushing the "Clean Core" methodology more and more on the SAP domain, and this is a valid driver for achieving the much-touted flexibility, innovation, and agility in the SAP context, where we are typically complex, waterfall, and monolithic.

Moving from a pilot to something more comprehensive and complex requires strong governance, a solid composable architecture, a new target operating model and a design authority approach. Working with Cloud Platforms, API, Microservices, and Containers, it is necessary to be agile or hybrid (or should be), approaching new methods and tools to achieve "Continuous-everything" for all technical layers, from infrastructure to applications end-to-end.

However, what about cost management? Cloud Providers typically cover cloud consumption costs during the pilot phase (credits, founding, sandbox, etc.). Bill-of-Materials (BoM) and related contracts, subscriptions, with Cloud Providers (one or more), consuming a different commercial model: pay-as-you-go, reserved, etc. Complex BoM, Accounts, and extended cloud landing zones necessitate daily based costs control to monitor, to alert, to adjust, to act, to scale-up & down, etc., while adhering to the budget and meeting the business's daily needs. All topics for which a suitable FinOps solution can provide accurate information and answers. FinOps is an operating model for cost management in the cloud: A combination of processes, tools, best practices, and organizational culture that enhances an organization's capacity to comprehend cloud costs and make tradeoffs. It enables the organization to anticipate, control, monitor, and optimize reactively and proactively the costs associated with a cloud-based solution.

This is something that is already in place with Hyperscalers (Microsoft, AWS, Azure, etc.), whereas the SAP BTP introduces something new. Yes, because there is currently nothing comparable on BTP that can complement what clients already know from hyperscalers. We must be Cloud-native, pushing Clean Core on BTP, Data, etc., and for this, a strong governance is required in accordance with the increasing complexity of the SAP BTP:

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-1.jpg)

Today user journey

The objective is to provide a new user-experience to the Personas depicted in the humorous cartoon, and for this we are working on solving Nina's paint-point, building the right solution for SAP BTP, powered by SAP BTP, and ultimately covering both hyperscalers and SAP BTP-related content in a single location:

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-2.jpg)

Golden thread

This is possible today thanks to the APIs provided by SAP BTP, implementing an architecture where a new SAP BTP App can show, on a daily basis, what's happening on the running cloud services in terms of consumptions, alerting in case of any actual vs. budget deviation and scaling in/out according to business requirements and plans:

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-3.jpg)

Controlling the transition from the SAP BTP subscription model to the SAP BTP CPEA, consumption-based model, is essential: transforming and migrating workloads to the public cloud results in a significant increase in recurring cloud spending. Numerous organizations are currently experiencing problems implementing cloud governance and cost management, resulting in uncontrolled growth of monthly SAP and Hyperscaler bills. SAP BTP FinOps enables the organization to proactively anticipate, control, monitor, and optimize the costs associated with cloud-based services. Daily reporting and dashboarding of SAP BTP Global Account, SAP BTP Directories, and SAP BTP Sub-Accounts operating costs. For the purposes of central analysis, reporting, and license auditing, data is retrieved from APIs provided by SAP for gathering, storing, and making usage information available for all services and applications in all regions of a cloud deployment:

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-4.jpg)

Working with our app you can overall navigate in analytics providing to you a daily-based reports on services consumptions, arranged by SubAccounts, Directory and other “tags” you can manage on SAP BTP. You can easly control deviations budget vs actuals and you can react in adjust what is wrong and what is not in line.

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-6.jpg)

FinOps is totally agnostic from the industry. It is relevant for all the Clients that are consuming SAP BTP services (with or without hyperscalers extensions) for any business needs in any domains, in pay-as-you-go commercial models:

* Opex approach with a pure consumption based on business need, avoiding additional costs, avoiding waste and unused resources.

* Budget and actuals daily checked avoiding end-months financial surprise, finetuning cloud services according to dynamic business needs.

* Business can ask for less/more; IT will prompt properly, setting the right size, controlling the related costs

Feel free to reach me in case you need more. Enjoy ![:winking_face:](/html/@9274F1BDD4BD1647F1AD237FE932AAD6/emoticons/1f609.png ":winking_face:")

* [clean core](/t5/tag/clean%20core/tg-p/board-id/technology-blog-members)
* [finops](/t5/tag/finops/tg-p/board-id/technology-blog-members)

15 Comments

You must be a registered user to add a comment. If you've already registered, s...