---
title: SAP BTP Integration Suite migration: don’t do lift&shift!
url: https://blogs.sap.com/2023/05/06/sap-btp-integration-suite-migration-dont-do-liftshift/
source: SAP Blogs
date: 2023-05-07
fetch_date: 2025-10-04T11:38:04.478526
---

# SAP BTP Integration Suite migration: don’t do lift&shift!

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP BTP Integration Suite migration: don't do lift...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159795&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP Integration Suite migration: don't do lift&shift!](/t5/technology-blog-posts-by-members/sap-btp-integration-suite-migration-don-t-do-lift-shift/ba-p/13548223)

![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")

[MichalKrawczyk](https://community.sap.com/t5/user/viewprofilepage/user-id/45785)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159795)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159795)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548223)

‎2023 May 06
9:34 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159795/tab/all-users "Click here to see who gave kudos to this post.")

14,216

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

## Don't do Lift and Shift for SAP BTP Integration Suite migrations!

In terms of integration platform migrations “Lift and shift”, also known as “rehosting,” is a process of migrating an exact copy of an integration platform from one integration platform to another. SAP has initiated one of the biggest moves in the integration platform migrations but sunsetting SAP Process Orchestration in 2027 but migration to SAP Integration Suite are not only happening from one direction - many SAP customers are also looking to leverage more SAP's cloud integration platform and they want to move from other integration platforms like WebMethods, Boomi, Mulesoft, Seeburger as well.

![](/legacyfs/online/storage/blog_attachments/2023/05/migr.png)

While the purpose/decision of the move process will not be discussed in this article, the method of the move will. I will try to prove that lift and shift method, while is might be fine in some exceptions, for most of SAP customers is the worst choice and should be avoided if possible.

## Why should lift and shift method be avoided?

As one of the analyst wrote: “**Lift-and-shift migrations**, or the use of automated migration tools, **fail to capitalize** on the rich functionalities and opportunities of a new integration platform”. Doing that is like taking your old TV set when moving to a new home...do you really want to do that? The world of integration platforms has changed since you bought you developed your first integration flow back in 1990 or early 2000... why would you ever want to move the old "garbage" and keep using your old TV set in a new flat?

![](/legacyfs/online/storage/blog_attachments/2023/05/tv.png)

Taking SAP Process Orchestration into SAP Integration Suite migrations do you really want move:

a) Message mappings with 20 User Defined functions - developed back in 2010 with zero information what do they do and everyone is afraid to touch this?

b) ccBPM or even BPMs - designed only because someone didn't know how to implement a specific functionality without them?

c) RFC, SOAP, JDBC lookups inside user defined functions?

d) monolith integrations into the world of SAP Integration Suite components (SAP API Management, SAP Cloud Integration, SAP Advanced Event Mesh, etc.)?

I hope it's just a rhetorical question - as you don't want to do that.

## What should I do then - my company does not have money for new reimplementation?

Did I say you need to reimplement something manually? Try using the Blue Lift & Shift approach! What does it mean? Blue Lift & Shift by Int4 approach (similar to SAP S/4HANA BlueField approach by SNP) means you do not continue with a simple Lift & Shift but try to use automated solutions like ChatGPT with [Generative TDD](https://blogs.sap.com/2023/03/15/automated-mapping-programs-generative-tdd-with-chatgpt/) to redesign the flows in order to simplify and clean them for business as usual (BAU) and make use of the new distributed architecture. Let's compare both approaches.

a) **Lift and Shift**:

* migrate existing message mappings into the SAP Integration Suite - remember those with over 10-20 user defined functions? Do you want to move this mess into a new landscape?

* migrate java mappings, ABAP mappings by reimplementing them in groovy (ChatGPT will work like magic here but there are two things: ChatGPT will not validate the migration - this you can fix with [Int4 Shield](https://blogs.sap.com/2023/01/20/automate-over-65-of-your-sap-integration-suite-migration-with-int4-shield-lite-for-free/) but it can still the same poorly written code - is that what you want?

b) **Blue Lift & Shift:**

* reimplement message mappings, java mappings, ABAP mappings and XSLT mappings in groovy from scratch & automatically - [Automated mapping programs – Generative TDD with ChatGPT](https://blogs.sap.com/2023/03/15/automated-mapping-programs-generative-tdd-with-chatgpt/) this way you will have fresh mappings in groovy (your SAP Integration Developers will love it and your BAU team will be ready to add new features on the next day after the migration if required) and they will be automatically validated as shown in the blog

* use prepackaged content when possible to eliminate custom integration flows (again with generative Test Driven Development approach)

* use the new frameworks to redesign the flows to use the rich capabilities of the SAP Integration Suite like MACH - [MACH Architecture with SAP BTP and Advanced Event Mesh](https://blogs.sap.com/2023/04/26/mach-architecture-with-sap-btp-and-advanced-event-mesh)

## What is the difference in business value of SAP Integration Suite between Lift & Shift and Blue Lift & Shift?

The main business value of using SAP Integration Suite stays in the same in both approaches: cloud infrastructure does not need to managed by your internal team and for new integration you can implement them much faster using the new features of SAP Integration Suite. **Blue Lift & Shift**however gives you tons of additional business value:

a) your old integration flows are easy to change (as they were rewritten automatically from scratch using the Generative TDD approach) so the BAU team is not afraid to touch them

b) the poorly written mappings (speed, etc.) are replaced = faster integration speed

c) monolith integration are broken down (like in MACH architecture) - your existing integrations are again faster, more reliable and easier to decouple

d) you can use prepackage content from SAP Integration Suite eve...