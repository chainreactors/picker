---
title: From Rookie to Result: integrating S/4HANA Cloud Public Edition with ChatGPT using SAP BTP/CPI
url: https://blogs.sap.com/2023/08/19/from-rookie-to-result-integrating-s-4hana-cloud-public-edition-with-chatgpt-using-sap-btp-cpi/
source: SAP Blogs
date: 2023-08-20
fetch_date: 2025-10-04T11:59:16.622666
---

# From Rookie to Result: integrating S/4HANA Cloud Public Edition with ChatGPT using SAP BTP/CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* From Rookie to Result: integrating S/4HANA Cloud P...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54982&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [From Rookie to Result: integrating S/4HANA Cloud Public Edition with ChatGPT using SAP BTP/CPI](/t5/enterprise-resource-planning-blog-posts-by-sap/from-rookie-to-result-integrating-s-4hana-cloud-public-edition-with-chatgpt/ba-p/13580523)

![richardnagel](https://avatars.profile.sap.com/0/3/id03589e7cd3f0ff900cffa71acf896fca9732c2520f1eb320c49b7031c5ee751b_small.jpeg "richardnagel")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[richardnagel](https://community.sap.com/t5/user/viewprofilepage/user-id/183489)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54982)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54982)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580523)

‎2023 Aug 19
2:33 PM

[27
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54982/tab/all-users "Click here to see who gave kudos to this post.")

6,859

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (7)

Hello world ![:slightly_smiling_face:](/html/@AB1AFF728742E596A69993DB64EECECF/emoticons/1f642.png ":slightly_smiling_face:")

Recently I got inspired by some blogs explaining how to integrate SAP S/4HANA OnPrem with ChatGPT - using 3rd party tools such as MS-Azure.

Since more then a decade I have my focus on "pure Public Cloud ERP" and hence on SAP S/4HANA Cloud Public Edition. Also my focus is on midmarket and scaleup/hypergrowth companies who select the "GROW with SAP" bundle of SAP S/4HANA Cloud Public Edition and SAP BTP/CPI.

So in my opinion, it must be possible when buying nothing but this SAP bundle, you are capable to create E2E integration flows. No need to use other tools or brands.

I wanted to create an iFlow which executes the following: automating the reply to an incoming customer email query about the status of an order the customer placed earlier. The automation should parse the incoming query - for a valid SalesOrder number but also the "tone of voice". S4HC Public gives factual details about the SalesOrder, followed by ChatGPT which crafts a customer-specific email response. Final step is the e-mail reply to the customer.

The motivation for this process I got reading the excellent blog from Sudip Gosh ([ChatGPT Integration with S/4HANA](https://blogs.sap.com/2023/03/07/chatgpt-integration-with-sap-s-4hana/)).

So I set myself a challenge to integrate **S/4HANA Cloud Public Edition** with **ChatGPT** using nothing but **SAP BTP/CPI**.

Although I am experienced in S4HC Public, I had zero experience in creating iFlows in CPI, nor did I know how to do things like tracing and debugging errors, checking deployment status, creating groovy scripts, taking care of security features etc. So my other challenge was to self-learn how to do all these while "learning on the job" creating my storyline.

It was  nice challenge as I learned rapidly new things which I can apply in my daily job as blackbelt presales. "From Rookie to Result" took me a few evenings hobbying - and in this blog I am sharing my meandering experience in the format of a step-by-step explanation how the end-to-end flow works.

In another blog I will describe which skills and experiences it takes to go "From Rookie to Result" - but I am sure anyone is able to learn this too :-). Two very nice learnings here though: 1) my CPI trial account is deployed in the USA Eastcoast area and I am based in NL. Just like using S4HC Public from an SAP datacenter, the CPI performance is phenomanal. 2) Using **SAP Digital Assistance** during my challenge was a real asset - I was amazed how well it serves its purpose.

The iFlow I created is neither perfect nor ready for productive use - but it serves a purpose to show how to integrate pure public cloud applications into a working prototype. And for other rookies to help saving time, effort and energy searching for sources and examples - which was a big part of those evenings hobbying for me ![:winking_face:](/html/@BA8A4D6F163BA71843A4DFD85ADCAE67/emoticons/1f609.png ":winking_face:")

My iFlow does take care of security! Although I have chosen to use the simpler UserID/PWD in some steps, CPI provides the means to use the strictest of security if you want. In the next image the green stars indicate where security measurements are used (enforced - as without your iFlow simply won't work).

![](/legacyfs/online/storage/blog_attachments/2023/08/p22-1.png)

The following image shows the working end-to-end iFlow which integrates SAP S/4HANA Cloud Public Edition, ChatGPT and e-mail. The block numbers are used in the text following it.

![](/legacyfs/online/storage/blog_attachments/2023/08/p0.png)

Block 1. This is a Sender role - and in this iFlow version this is POSTMAN. In a new version of this iFlow the Sender must be reading from an Email system - where CPI offers possibilities to poll an inbox and extract emails from it on any desired frequency and interval.

Block 2. HTTPS Connector

It defines the unique URL used when the iFlow is deployed on BTP, in such a way that a Sender knows what to call:

![]...