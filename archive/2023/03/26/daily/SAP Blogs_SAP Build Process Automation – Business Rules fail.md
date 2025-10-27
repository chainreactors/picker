---
title: SAP Build Process Automation – Business Rules fail
url: https://blogs.sap.com/2023/03/25/sap-build-process-automation-business-rules-fail/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:56.696143
---

# SAP Build Process Automation – Business Rules fail

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Build Process Automation - Business Rules fail

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161627&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build Process Automation - Business Rules fail](/t5/technology-blog-posts-by-members/sap-build-process-automation-business-rules-fail/ba-p/13559233)

![pjcools](https://avatars.profile.sap.com/f/f/idffbfb807853b3c0f20f768e6ebeac8a1da7b33dcfd45ecc56d3d8586e330746d_small.jpeg "pjcools")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[pjcools](https://community.sap.com/t5/user/viewprofilepage/user-id/944)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161627)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161627)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559233)

‎2023 Mar 25
1:48 AM

[23
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161627/tab/all-users "Click here to see who gave kudos to this post.")

6,538

* SAP Managed Tags
* [SAP Workflow Management, business rules capability](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management%252C%2520business%2520rules%2520capability/pd-p/73554900100800000842)
* [SAP Business Rules Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Rules%2520Management/pd-p/10027901995226543076552839495060)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Rules Management

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusiness%2BRules%2BManagement/pd-p/10027901995226543076552839495060)
* [SAP Workflow Management, business rules capability

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement%25252C%2Bbusiness%2Brules%2Bcapability/pd-p/73554900100800000842)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (4)

Those that know me well, know that I love the Business Rules service that is part of the SAP Business Technology Platform (SAP BTP). Over the years this has morphed a few times from what was originally offered. For background, Business Rules was an individual service offering on Neo and enabled businesses to provide much needed flexibility and decision logic to applications built and hosted on SAP BTP. With this service, REST API's were available to easily read back the rules. Overall, applications were enhanced due to this service as it enabled the ultimate flexibility and avoided hard wiring in the code base of applications and saved unnecessary data from being kept in Core systems such as S/4 or SAP ERP.

![](/legacyfs/online/storage/blog_attachments/2023/03/Business-rules-on-Neo.png)

Business Rules service offering on Neo

Since then I feel like it has bounced around with SAP Product Managers maybe not knowing the full extent of how this service can be utilised. The first change was that it was bundled in SAP Workflow Management. Now while, Business Rules are more than likely required when building Workflows I never understood why it was still not an individual service - especially when workflows could just as easily call the REST API's to retrieve them? Why did it need to be bundled? Why couldn't this be offered as it's own outright service? Additionally, there was a time where developers had to use Business Application Studio to create the app launcher for Business Rules. This was very cumbersome and made zero sense. Talk about making it hard for customers and partners to easily activate and use it. This was a really poor UX for development teams. Luckily, this was fixed in the future by Boosters which was a great idea.

Regardless of the above changes, I have continued to use them in solution architectures I provide to customers. In some cases, the projects that I have been part of used only the Business Rules element of SAP Workflow Management - at that particular time there was actually no need for any workflow management and as such the service was only activated for Business Rules. Every single project over the last how many years has used Business Rules as part of the full solution and the applications we have built have been better for it. Customers also are happy with the fact they can maintain some of these rules and change settings when business requirements change slightly. This means there were no code changes required by a Developer - instead small changes to Business rules allowed customers to meet changing business requirements over time. The same REST API's (v2) could be used to retrieve Business rules as well so from a solution perspective not much changed when it was part of the SAP WM service.

OK - so now SAP Workflow Management has been deprecated(!) and now we have SAP Build Process Automation (SAP BPA). Customers that already have workflow management enabled can still continue to use Business rules (as they were) so this is OK. However, I found out this week that while Business Rules is part of the entire SAP BPA suite it does **not**allow customers to create their own rules! What??? In fact, the + button has been deactivated. When consuming presentations on these new tools like SAP BPA there is a big push for using predefined Live content. OK - this is fine and I am ok with this however why on earth would SAP turn off the ability for customers to create their own Business Rules if in fact they want to?? Makes absolutely no sense at all.

![](/legacyfs/online/storage/blog_attachments/2023/03/BR-BPA.png)

Add (+) button deactivated

You can see that only the Import icon is active. The + button has been deactivated.

![](/legacyfs/online/storage/blog_attachments/2023/03/BR.png)

So what this effectively means is that customers can only use this service if in fact they use predefined Live content and within an Automation scenario???? Seriously.

I have been in the SAP ecosystem for over 25 years and have loved the flexibility available across the SAP ERP, SAP CRM and of course SAP BTP so turning off this function I am really at a loss to explain. Customers are paying for this service but now they cannot even use this service outside of Automations that they need to be build? And wait - they can only import business rules packages based on predefined content.

![](/legacyfs/online/storage/blog_attachments/2023/03/BR-can-no-longer-be-used.png)

SAP Help explaining removal of the + Button

The only possible reason for this is that the SAP Product Managers in this area have limited understanding of how customers and partners have used the Business Rules se...