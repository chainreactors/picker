---
title: Never again create a mapping manually!
url: https://blogs.sap.com/2023/02/23/never-again-create-a-mapping-manually/
source: SAP Blogs
date: 2023-02-24
fetch_date: 2025-10-04T07:58:00.302251
---

# Never again create a mapping manually!

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Never again create a mapping manually!

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161161&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Never again create a mapping manually!](/t5/technology-blog-posts-by-members/never-again-create-a-mapping-manually/ba-p/13556678)

![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")

[MichalKrawczyk](https://community.sap.com/t5/user/viewprofilepage/user-id/45785)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161161)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161161)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556678)

‎2023 Feb 23
9:46 PM

[33
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161161/tab/all-users "Click here to see who gave kudos to this post.")

9,260

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

## Can I generate a mapping which can be used in SAP Integration Suite/SAP Process Orchestration automatically?

It's not only possible but it actually takes seconds to do that. If you have an source message and an example of a target message you can easily do that with chatGPT in seconds as shown in the following screenshots:

![](/legacyfs/online/storage/blog_attachments/2023/02/input.png)

Figure 1 - source and target messages

After a few seconds you will get a desired result as shown in Figure 2:

![](/legacyfs/online/storage/blog_attachments/2023/02/XSLT.png)

Figure 2 - automatically generated XSLT mapping

You can generate the mapping in any language (XSLT, Groovy for SAP Integration Suite, Liquid for Azure LogicApps, etc.). The question which might be on your head right now might be: ok I can generate something but how good is the mapping? It depends on two factors:

a) the query you will make into the chatGPT or any other generative pre-trained transformer (you can ask for value mappings, etc.)

b) the quality of your representative example - if you take a message with a few fields only and one line item it will not be a good case... you need to get something better.

From our experience the mappings generated using this approach should give a good coverage of around 60-80% of the requirements. This is amazing already but can we get much more (closer to 100% using a similar approach)? Yes, please keep on reading.

## What is a generative Test Driven Development (generative TDD) and why is that a breakthrough in SAP integration platform development, delivery and maintenance ?

Let's start with TDD - Test-driven development is a process where you start development by creating a set of test cases first and only then do the actual development. Now compare those two:

a) **typical SAP Integration Development** - Integration Team together with SAP functional team prepares a mapping specification in excel...- full of conditions, very complex to understand and implement. Once the development is ready and is being tested with real examples - the process of fixing starts and all of a sudden the mappings needs to changed, enhanced, fixed completely.

b) **generative TDD SAP Integration Development** - Integration Team together with SAP functional team try to gather as many source and corresponding target messages as they can. Once they have a full bunch of them they just ask any generative pre-trained transformer (like chatGPT) to create a mapping and use the interface. Once we start testing everything is working as we were using tons of real messages to generate the mapping so there is not need to fix anything.

Which approach do you want to take in your next project?

## What are the use cases to generate the mappings automatically?

Let's move into the future for a while now. It's 2027... and SAP Process Orchestration is being sunset. One of the biggest winners for automated mapping generation will be SAP Process Orchestration migrations. Why is that you might say? I can reuse some mappings from SAP Process Orchestration in SAP Integration Suite? Let's see if this is what you can/want to do:

a) **ABAP mappings** - those cannot be migrated to SAP Integration Suite

b) **java mappings** - do you have a code for the java mapping and do you want to maintain it on your new integration platform (SAP Integration Suite or any other)?

c) **message mappings** - do you honestly want to migrate this amazing message mapping which is using 15 different UDFs into SAP Integration Suite?

d) **B2B/EDI mappings** - maybe you were using some external software to do this mapping, why not enable it now in SAP Integration Suite easily?

e) **what if you cannot migrate the mappings** - for example you migrate to Azure LogicApps or any other integration platform?

Of course you're free to do whatever you want but do you really want to shift and lift if it's possible to clean the code and make it much simpler while at the same time you can make sure nothing breaks?

## 60-80% is not enough - I need more - can I improve this method somehow?

We've found out an amazing way to improve the quality of the generated mapping and put it to a completely new level (our patent pending application). With integration platform migration projects we don't need to use single messages for mapping program generation - we can actually use thousands of historical messages and generate a mapping program on the basis that.

![](/legacyfs/online/storage/blog_attachments/2023/02/patent.png)

Figure 3 - how to improve the quality of a mapping program generation dramatically.

Our software (Int4 Suite) can connect to any production environment of an integration platform (SAP Process Orchestration, SAP Integration Suite, Webmethods, Boomi, etc.) and fetch thousands of historical messages for a single interface for the purpose of new mapping program generation in any language.

![](/legacyfs/online/storage/blog_attachments/2023/02/language.png)

With this approach we can produce a mapping program which will provide a much better mapping coverage compared to the one generated from a single source-target message pair.

## What is next?

Try chatGPT yourself! You will be amazed and hopefully you will embrace the generative TDD in your next SAP integration project!

As for the SAP Process Orchestration Customers moving to SAP Integration Suite due to the partnership that was announced bu Jurgen Mueller during the 2022 Teched in Las Vegas, all SAP customers can use our product - Int4 Shield Lite for free fo...