---
title: Building GenAI powered Data-Driven Applications on SAP HANA Cloud/SAP Datasphere- E2E Scenario
url: https://blogs.sap.com/2023/06/25/building-genai-powered-data-driven-applications-on-sap-hana-cloud-sap-datasphere-e2e-scenario/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:04.307184
---

# Building GenAI powered Data-Driven Applications on SAP HANA Cloud/SAP Datasphere- E2E Scenario

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Building GenAI powered Data-Driven Applications on...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164065&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Building GenAI powered Data-Driven Applications on SAP HANA Cloud/SAP Datasphere- E2E Scenario](/t5/technology-blog-posts-by-sap/building-genai-powered-data-driven-applications-on-sap-hana-cloud-sap/ba-p/13568872)

![Vivek-RR](https://avatars.profile.sap.com/f/0/idf06d469c228dd1e12f497082c75b83bda8ccf0e7238fa2b83aec83a9f6adb183_small.jpeg "Vivek-RR")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Vivek-RR](https://community.sap.com/t5/user/viewprofilepage/user-id/143545)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164065)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164065)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568872)

‎2023 Jun 25
7:46 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164065/tab/all-users "Click here to see who gave kudos to this post.")

14,821

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP HANA multi-model processing](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520multi-model%2520processing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP HANA multi-model processing

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2Bmulti-model%2Bprocessing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (7)

# Why GenAI Now?

The recent announcements about [SAP partnering with Microsoft](https://news.sap.com/2023/05/sap-microsoft-joint-generative-ai-offerings-talent-gap/) to build enterprise-ready innovative solutions excited us about the future of SAP solutions. And the integration with Microsoft Azure Open AI to access language models securely got us to think about productive use cases that might fit SAP HANA Cloud/SAP Datasphere scenarios. Again, **the use case we are discussing is our perspective and nothing related to any official roadmap/messaging**. And the objective is that going through use cases as such will help you map similar ideas in your respective areas. Or you could learn the technical deployments that might help you. The use case was also presented at SAPPHIRE/ASUG 2019, consuming AI Business services. Still, we could do it differently based on Generative AI (AI) since we can access powerful language models (Open AI) through Microsoft Azure Cognitive Services. So here we go ![:smiling_face_with_smiling_eyes:](/html/@F1E2370483376CBD357141A1D520B3FD/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

## **What’s the Use-case?**

The objective was to extract budget intelligence from reports published as pdf or Word documents from the contractor sites. And the reports were updated weekly/monthly. Certain assets maintained in their SAP system were of interest and required additional information, such as program elements and the associated budget information. In the past, analysts scanned the documents manually, captured the relevant information, and matched the relevant data with SAP assets. The information would be available as reports for key business users to make appropriate decisions.  Another ask was to extract asset-related details from press releases updated on the same contractor sites to understand the market trends. Now, these were registered users, and they were allowed the extract the information as it is done in compliance with applicable regulations.  The solution was tested in 2018, and the data was captured, as you see in the data flow.

![](/legacyfs/online/storage/blog_attachments/2023/06/A1-1.png)

The whole flow involves analysts, data quality teams, and finally, the business users who review both the assets and the information processed from documents related to assets. The solution works, but there are many repetitive tasks here, and Business users need to explore the documents, like executing self-service reports on the documents directly. This also aligns with what SAP is trying to convey in this [article](https://news.sap.com/2023/05/sap-microsoft-joint-generative-ai-offerings-talent-gap/) on Joint Generative AI(GenAI) offerings that help avoid repetitive work and provide more freedom to business users to explore the documents without needing data pipelines to extract content from unstructured documents.

## **How would you do it now?**

How about executing the query on the documents or online resources directly without data pipelines?

Let me explain the same scenario with an architecture involving SAP Datasphere/SAP HANA Cloud, Cloud Storage, Azure Cognitive services (Azure Open AI), and Azure app service. The base logic is built as Python script and extended as a [Django](https://www.djangoproject.com/) app, a high-level Python web-based framework. And the app is deployed on Azure app services using private git repositories. We could have deployed the app on SAP BTP, Kyma runtime too.  But hey, let’s learn something new.

The app consumes the Azure Open AI deployment models based on the Django framework. The user sends the prompt from the front end, such as getting the summary of the press release statements or looking for specific keywords and retrieving a summary. The user would also mention the SAP HANA Cloud /Datasphere table the app needs to refer to for the source URLs or document path.  We will extract the text from the document using relevant libraries and split the extracted text into segments. The segments are sent to the Azure AI deployment model (the base model being text-davinci-003 an...