---
title: Generative AI for SAP using AWS Part II. Model Customizing with RAG
url: https://blogs.sap.com/2023/08/20/generative-ai-for-sap-using-aws-part-ii.-model-customizing-with-rag/
source: SAP Blogs
date: 2023-08-21
fetch_date: 2025-10-04T11:59:55.136205
---

# Generative AI for SAP using AWS Part II. Model Customizing with RAG

* [SAP Community](/)
* [Developers](/t5/developers/ct-p/developers)
* [Artificial Intelligence](/t5/artificial-intelligence/gh-p/ai)
* [Blogs Posts](/t5/artificial-intelligence-blogs-posts/bg-p/aiblog-board)
* Generative AI for SAP using AWS Part II. Model Cus...

Artificial Intelligence Blogs Posts

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/aiblog-board/article-id/373&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Generative AI for SAP using AWS Part II. Model Customizing (with RAG)](/t5/artificial-intelligence-blogs-posts/generative-ai-for-sap-using-aws-part-ii-model-customizing-with-rag/ba-p/13580643)

![MarioDeFelipe](https://avatars.profile.sap.com/d/5/idd54a66537cf10dee8ff1d1db09cfb0088e9ae1b985efdfc003fb1217b9d6b46a_small.jpeg "MarioDeFelipe")

[MarioDeFelipe](https://community.sap.com/t5/user/viewprofilepage/user-id/13491)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=aiblog-board&message.id=373)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/aiblog-board/article-id/373)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580643)

‎2023 Aug 20
9:01 AM

[5
Kudos](/t5/kudos/messagepage/board-id/aiblog-board/message-id/373/tab/all-users "Click here to see who gave kudos to this post.")

2,972

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

View products (1)

This is a series of blogs I am writing for SAP Tech leaders who want to understand how to use Generative AI from an SAP and Enterprise perspective using the AWS platform.

I know this is an immature technology, and this series of blogs will age really bad, but I decided to try it to share my personal impressions and best practices I see while I am in the process of personal and professional POCs.

In my [first blog](https://blogs.sap.com/2023/08/13/generative-ai-for-sap-using-aws.-private-domains-and-foundation-models/), I discussed what foundation models are available and how they can be deployed in a custom VPC in a custom Domain.

In this second blog, I address a fundamental question, how we can customize models, focusing on Data Privacy. The way I see it, AI has been there for many years; what has changed in the last months and has caused market disruption is the, allow me to use this phrase, give "power to the people", more technically, the creation of pre-trained foundation models ready to be consumed, like GPT from OpenAI. There is massive information on the web about this right now, Bard here, LLAMA there, but we operate at the enterprise level, and for the Enterprise, the rules are very different to us as individuals; as individuals, we can ask ChatGPT a generalistic question about our next visit to Rome, but as Enterprise, the data must be relevant, secured and up to date. No data from public datasets might be appropriate, and of course, we need to feed our models with the most up-to-date elements.

OpenAI is fantastic, but in the enterprise, we see Data vendors like Snowflake, Databricks, or Datarobot (which integrates well with SAP DataSphere) continue to carve out policies that allow customers an *alternative to using* **OpenAI** path by quickly allowing its customers to develop machine-learning models from scratch, or use open-source models, rather than being dependent on proprietary ones like OpenAI’s GPT-4, which for the end-user is not relevant but for the Enterprise it matters significantly.

This wide-scale adoption of ML Models makes the concerns and challenges around privacy and data security paramount and ones that each organization needs to address. In this blog post, we will explore some potential approaches organizations can take to ensure robust data privacy while harnessing the power of these Models and feeding these models with SAP data.

![](/legacyfs/online/storage/blog_attachments/2016/02/sapnwabline_885687.png)

# Intro

Models like LLMs are typically trained on vast amounts of data to develop a statistical understanding of human language patterns. The extensive datasets used in training can often contain sensitive information, leading to privacy concerns. Additionally, the traditional approach of relying on cloud-based services to deploy and conduct inference with these models requires organizations to transfer their data to third-party centralized model providers, which can lead to data exposure, data breaches, and unauthorized access. This is why large corporations have limited employees' use of LLMs with enterprise data.

Instead of throwing a plethora of technical jargon into this blog, I will describe the art of the possibility for SAP customers' interest to leverage Model customizing, why that should happen, and how it can be done in the easiest way possible, using the AWS platform.

I use the AWS platform as an example for several reasons;

* I am totally biased in favor of the platform because 99% of the customers I serve on my business unit have their data on the AWS platform, and here is where my interest and expertise rely, but most of what I say is also possible in other platforms.

* I see AWS as an exciting approach, where the company sets itself in a clear Platform Strategy compared to Microsoft or Google, which are positioning their platforms toward their own Models or 3rd party models (like OpenAI), probably leaving less space for an open platform.

* I particularly like Amazon SageMaker and its capabilities; it's a complex but mature tool. SageMaker has been with us for years for AI, but AWS is about to release a specific service for Generative AI, Bedrock, which is still in preview as of August 2023. Bedrock will dramatically simplify and enhance the Generative AI capabilities of AWS, but until its GA, we can achieve must on the AWS platform with current software.

* Bedrock lets developers select from a range of Models from co:here, Anthropic, AI21Labs, and Stability AI. Using these models, the AWS platform allows an easy build using existing Generative AI products, easing the development of applications like chatbots, which run on AWS’ infrastructure without worrying about the underlying infrastructure.

We are still unsure if there's a lot of investment in Enterprise Models, but at least there is a lot of focus. If we focus on co:here (LLM), they are planning to integrate lots of Generative AI capabilities in Oracle Fusion Cloud and Netsuite as well as Oracle industry-specific apps, and so they are planning to do this with SAP. So the Holy Grail of the previous blog discussing private Foundation Models vs. Public Foundation Models will continue during this blog; private data sets/ public data sets are what the Software vendors Oracle and SAP are planning to use co:here Foundation Model enables companies to train on smaller data sets to generate higher confidence results, and customers and users get key benefits from all that enterprise data into their apps. All with Privacy and Confidence we need to provide to our customers.

So, we see the list of initiatives that prominent Software vendors are doing, well summarized in [this blog post](https://www.cio.com/article/649334/what-enterprise-software-vendors-are-doing-with-generative...