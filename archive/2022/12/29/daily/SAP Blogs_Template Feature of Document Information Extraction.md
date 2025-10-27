---
title: Template Feature of Document Information Extraction
url: https://blogs.sap.com/2022/12/28/template-feature-of-document-information-extraction/
source: SAP Blogs
date: 2022-12-29
fetch_date: 2025-10-04T02:39:43.989328
---

# Template Feature of Document Information Extraction

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Template Feature of Document Information Extractio...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161091&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Template Feature of Document Information Extraction](/t5/technology-blog-posts-by-sap/template-feature-of-document-information-extraction/ba-p/13559721)

![Abeeha_Rizvi](https://avatars.profile.sap.com/c/1/idc127bb15b0ab99ae1bebd0f112ba4b41fee36689a772ec2496e109c75ee491ef_small.jpeg "Abeeha_Rizvi")

![Employee](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Employee")
[Abeeha\_Rizvi](https://community.sap.com/t5/user/viewprofilepage/user-id/44329)

Employee

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161091)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161091)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559721)

‎2022 Dec 28
11:19 AM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161091/tab/all-users "Click here to see who gave kudos to this post.")

3,381

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Services/pd-p/73555000100700001042)
* [SAP Document AI](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520AI/pd-p/73554900100800002861)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [SAP AI Services

  Software Product](/t5/c-khhcw49343/SAP%2BAI%2BServices/pd-p/73555000100700001042)
* [SAP Document AI

  SAP AI Services](/t5/c-khhcw49343/SAP%2BDocument%2BAI/pd-p/73554900100800002861)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

## Document Information Extraction

With the smart capabilities of Document Information Extraction (which is part of the SAP AI Business Services Portfolio), information can be easily extracted from business documents using the pre-trained AI models.

The pre-trained models can extract all the relevant information from [standard documents](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/9e6a56d37ad1463fb3b85eed5d962a3c.html)(such as invoices, purchase orders, payment advices and business cards). However, in our day to day use, we come across various types of business documents which might also have special formats and [custom fields](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/1589bb3ffb704340abe76f7224540904.html)(for example power of attorney). Such documents are sometimes unrecognizable for the pre-trained models.

In this blog we would like to share how you can add a customization touch to your information extraction process by using templates based on your specific business needs.

## Template Feature

We would like to highlight the template feature here, which is one of the [key features](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/f448937bcb3843648f8ab31c043ba679.html) of Document Information Extraction UI. It supports users to extract information very easily and flexibly from many different types of documents. With the template feature, users are able to create, reuse, edit, and delete templates, based on [schemas](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/3c7862e30fc2488ea95f58f1d77e424e.html) and sample document files.

*Note*: Schemas are a basis for creating templates. Users can select schemas and associated templates when adding documents.

As we already mentioned above, Document Information Extraction uses pre-trained models to extract information from your documents. Templates can be used to extend these existing pre-trained models to yield even greater benefit for you. This feature offers two scenarios for you:

•**Fine-tuning,**where you can use existing schemas (which are used for pre-trained models), for creating new templates and use them to extract information from [standard document types](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/4e135eced35a4fe988545372e6dc284b.html) more precisely and accurately

•**Full customization,** where you can create new schemas and new templates to extract information from [custom document types](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/e5795859a97742e89b7cc7444de55317.html)

We have prepared a short demo video to give you a first idea about how to create your own template using an existing schema. Let us know in the comments below if you would be interested to see more such demo videos, also for the schema creation.

Document Information Extraction offers the template feature in many different languages so that you can enjoy the customization of documents fully and more flexibly. Find here the [list of languages](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/c793a6a0065f4f90b4b96de810a6505a.html?q=business%20recognition) available.

Now you can use the template feature of Document Information Extraction to customize and enhance the information extraction process. Find more information on the SAP [Help Portal](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/1eeb08998f49409681c06a01febc3172.html?q=templating) page for Document Information Extraction.

Here are our recommendations for using templates: [Using Templates: General Recommendations](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/8363d9556130477899bfd9e14fee8c4e.html?state=DRAFT).

## What’s more?

Document Information Extraction also offers the template feature in free tier. Read more about it [here](https://blogs.sap.com/2022/11/21/templating-function-in-free-tier-of-document-information-extraction/?preview_id=1650881). Stay tuned for more updates on new features.

We recommend to also read our recent blogs about of Document Information Extraction:

* [OCR Only Schema](https://blogs.sap.com/2022/11/21/new-feature-release-ocr-only-schema/?preview_id=1649055)

* [Support for business cards](https://blogs.sap.com/2022/12/06/document-information-extraction-support-for-business-cards/)

* [Handwriting Recognition](https://blogs.sap.com/2022/12/06/handwriting-recognition-by-document-information-extraction/)

* [Internationalizatio...