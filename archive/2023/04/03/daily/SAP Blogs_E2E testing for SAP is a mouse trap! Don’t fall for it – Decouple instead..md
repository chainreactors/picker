---
title: E2E testing for SAP is a mouse trap! Don’t fall for it – Decouple instead.
url: https://blogs.sap.com/2023/04/02/e2e-testing-for-sap-is-a-mouse-trap-dont-fall-for-it-decouple-instead./
source: SAP Blogs
date: 2023-04-03
fetch_date: 2025-10-04T11:30:19.787021
---

# E2E testing for SAP is a mouse trap! Don’t fall for it – Decouple instead.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Automated E2E testing for SAP is a mouse trap! Don...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68337&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automated E2E testing for SAP is a mouse trap! Don't fall for it - Decouple instead.](/t5/enterprise-resource-planning-blog-posts-by-members/automated-e2e-testing-for-sap-is-a-mouse-trap-don-t-fall-for-it-decouple/ba-p/13566805)

![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")

[MichalKrawczyk](https://community.sap.com/t5/user/viewprofilepage/user-id/45785)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68337)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68337)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566805)

‎2023 Apr 02
9:12 AM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68337/tab/all-users "Click here to see who gave kudos to this post.")

11,373

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Test Acceleration and Optimization](https://community.sap.com/t5/c-khhcw49343/SAP%2520Test%2520Acceleration%2520and%2520Optimization/pd-p/01200314690800000231)
* [SOLMAN Test Suite](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Test%2520Suite/pd-p/132949817163443344955330185779754)
* [test automation tool for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/test%2520automation%2520tool%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Private Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Private%2520Edition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Test Acceleration and Optimization

  SAP Test Acceleration and Optimization](/t5/c-khhcw49343/SAP%2BTest%2BAcceleration%2Band%2BOptimization/pd-p/01200314690800000231)
* [SOLMAN Test Suite

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BTest%2BSuite/pd-p/132949817163443344955330185779754)
* [test automation tool for SAP S/4HANA Cloud

  Software Product Function](/t5/c-khhcw49343/test%2Bautomation%2Btool%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Private Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPrivate%2BEdition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

View products (5)

## Why Automated E2E testing for SAP projects is a trap?

Automated E2E testing sounds like dream come true for SAP S/4HANA complex transformations (Selective Data Transitions/BlueField or Complex Brownfield projects) but in reality it's a hidden mouse trap.

![](/legacyfs/online/storage/blog_attachments/2023/04/Mouse_trap.png)

On one hand, thoroughly testing your system in a production-like test environments sounds like a great idea but in reality it's only doable for very simple systems. When we talk about SAP transformation projects like Selective Data Transitions/BlueField or Complex Brownfield projects where we have hundreds of 3rd party systems and even more EDI/B2B partners it start to resemble a Greek myth of Sisyphus (can never be achieved). It's brilliantly explained in this video from David Farley author of "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation".

## What makes E2E testing fail for SAP projects?

Imagine having to run a complex SAP transformation program with 30-100 SAP consultants and many more internal resources which need to work together. Now someone comes to you and says the best way to run this program is to enable E2E testing so whatever change the SAP team will do will be automatically validated. While it's a great idea in reality you don't add 5-10% of more work to the scope of the project as with 50-100 3rd party systems and 200-500 EDI partners you may actually be doubling or tripling the project scope - were you aware of that? Doesn't that remind  "spinning too many plates"? Are you such a good coordinator and is your SAP project budget owner are of the additional costs?

![](/legacyfs/online/storage/blog_attachments/2023/04/platespinning-770x360-1.jpeg)

Image source: <https://halfretire.com/why-selling-a-business-is-a-million-dollar-aspirin/>

It doesn't end here I'm afraid, E2E testing setup would be deployed by people who are not involved in the software development process and don't know the functionality of those 50-100 3rd party systems. Testing teams in such situations tend to be overly cautious and test everything due to concerns about potential issues. This approach can be slow, costly, and not very effective at ensuring high quality. Also the problem is that testing is happening too late in the process to catch and prevent quality issues from occurring in the first place.

## Solution - Simulate to Isolate and Decouple your SAP project

As Dave Farley mentions a good test is deterministic and atomic so the key to solve this puzzle is to use simulation to isolate and decouple SAP project from 3rd party systems and EDI/B2B partners as shown in Figure below.

![](/legacyfs/online/storage/blog_attachments/2023/04/decouple_isolate.png)

Figure - Simulate 3rd party systems and EDI/B2B partners for SAP projects.

It simplifies the following:

a) scope of the project - you're only testing the releasable unit of software - SAP system and not anything else

b) we can test every aspect of the releasable unit of software in a much better way instead of testing only vanilla flows with E2E testing

c) by simulating 3rd party systems and EDI/B2B partners we speed up the SAP project as we eliminate the need to coordinate the testing with multiple parties

d) our SAP project can be more sustainable - no need to create matching tiers of test environments of 3rd party systems and the existing ones don't even need to be online during the testing

This method is a much more organised and structured approach to conducting comprehensive and detailed testing of SAP transformation programs, and it is more efficient and quicker than the E2E alternative.

## Where I can learn more about this topic of Simulations/Service Virtualization for SAP transformation programs?

There’s a 3h course on openSAP just on this topic called “[Avoid SAP S/4HANA Project Delays with Third-Party Systems Service Virtualization](https://open.sap.com/courses/iftt1-2-pc)” – In this course we help you understand why SAP-tailored service virtualization is a hidden gem of SAP S/4HANA projects, who can use it and when to use it, and most importantly, how to benefit from it. In addition, you’ll learn how service virtualization can make your projects more sustainable by significantly minimizing their carbon footprint.

![](/legacyfs/online/storage/blog_at...