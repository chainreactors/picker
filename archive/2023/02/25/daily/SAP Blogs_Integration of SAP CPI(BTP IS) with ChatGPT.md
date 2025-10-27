---
title: Integration of SAP CPI(BTP IS) with ChatGPT
url: https://blogs.sap.com/2023/02/24/integration-of-sap-cpibtp-is-with-chatgpt/
source: SAP Blogs
date: 2023-02-25
fetch_date: 2025-10-04T08:03:54.271555
---

# Integration of SAP CPI(BTP IS) with ChatGPT

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integration of SAP CPI(BTP IS) with ChatGPT

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160997&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integration of SAP CPI(BTP IS) with ChatGPT](/t5/technology-blog-posts-by-members/integration-of-sap-cpi-btp-is-with-chatgpt/ba-p/13555849)

![FarooqAhmed](https://avatars.profile.sap.com/d/f/iddfb1152714bf31c10e4eedd929f76c497b72c4da0f55c0c827cc47ee85146d3a_small.jpeg "FarooqAhmed")

[FarooqAhmed](https://community.sap.com/t5/user/viewprofilepage/user-id/146868)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160997)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160997)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555849)

‎2023 Feb 24
6:02 PM

[23
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160997/tab/all-users "Click here to see who gave kudos to this post.")

18,239

* SAP Managed Tags
* [SAP Conversational AI](https://community.sap.com/t5/c-khhcw49343/SAP%2520Conversational%2520AI/pd-p/73555000100800001301)
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)
* [SAP Conversational AI

  SAP Business AI](/t5/c-khhcw49343/SAP%2BConversational%2BAI/pd-p/73555000100800001301)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (4)

**Integration of SAP CPI(BTP IS) with ChatGPT**

**Introduction**

**What is ChatGPT?**

ChatGPT is a language model developed by OpenAI. It is designed to understand natural language, generate human-like responses to a wide range of questions, and carry out various language-related tasks. It has been trained on a large corpus of text data and can understand a broad range of topics. Its purpose is to assist users in their quest for knowledge and provide them with informative and useful responses.

**What is CPI(BTP-IS)?**

CPI(BTP-IS) is a set of services and tools provided by SAP on its cloud-based Business Technology Platform (BTP) to enable integration between different systems, applications, and data sources. The key benefit of CPI(BTP IS) is that it enables organizations to quickly and easily integrate their systems, data, and applications without the need for extensive coding or custom development. This helps to streamline business processes, reduce costs, and improve operational efficiency.

**How ChatGPT can be integrated?**

ChatGPT can be integrated using APIs (Application Programming Interfaces) provided by OpenAI. The API can be used to send text inputs to ChatGPT and receive responses in real-time. Chatbot Platform Integration and Custom Integration using libraries and SDK also possible.

**How CPI integrates with ChatGPT?**

CPI interacts ChatGPT through HTTP requests using API Keys for authentication. ChatGPT has multiple APIs depending on the usage or self learning basis like Models, Completions, Edits, Images, Create Image Variations, Embeddings, Files, Fine-tunes and Moderations APIs

*Note: All the available ChatGPT APIs can be integrated with SAP CPI but for demonstration will use the Completion API.*

**Integration of SAP CPI(BTP IS) with ChatGPT**

**Prerequisites:**

1. SAP BTP IS Tenant Access

2. ChatGPT openai platform Access

3. Postman Tool for testing

**Step-1: Create a new secret key on ChatGPT**

After login to the account on <https://platform.openai.com/account/api-keys> goto API Keys and click on Create new secret key.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-112.png)

Image source from my account on platform.openai.com

**Step-2: Download the security certificate from respective ChatGPT API**

For demo we will use the API “ [https://api.openai.com/v1/completions”](https://api.openai.com/v1/completions%E2%80%9D) from other available APIs of ChatGPT.

Open the API url in any browser and click on the lock(HTTPS) icon from the address bar and select show certificate.

Export the root certificate and save to your local desktop.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-51.png)

Image source from my account on platform.openai.com

**Step-3: Upload the root security certificate in the SAP BTP IS(CPI)=>KeyStore**

Login to BTP account and redirect to your Integration Suite home page. From the left side pane select the monitor artifacts options and open the Keystore page.

Click on Add dropdown option from right side top pane and select the Certificate option and upload the already downloaded security certificate from Step-1.

**![](/legacyfs/online/storage/blog_attachments/2023/02/Picture3-43.png)**

Image source from my trail account on SAP BTP IS

**Step-4: Create a new Integration Flow under the desired package with appropriate naming convention.**

From the left side pane design artifacts option select or create a package and create a new IFLOW.

We need to create a scenario of HTTPS sender adapter to HTTP receiver adapter with intermediate call on chatGPT API .

**Step-5: Configure a sender HTTPS adapter as we will test it from Postman tool.**

As per the requirement we can have any sender adapter which can able to provide the expected input text.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-39.png)

Image source from my trail account on SAP BTP IS

Provide the desired Address path which will be added to the deployed tenant URL.

**Step-6:  Configure the JSON to XML converter as the input text from Postman will be provided as JSON.**

As per the requirement we can have any format input can be sent from sender system which can be modified accordingly.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture5-24.png)

Image source from my trail account on SAP BTP IS

Remove the Namespace Mapping if selected.

In our case JSON to XML only is used as input from POSTMAN will be JSON and for further processing of exchange properties we will use XML .

**Step-7: Configure the Content Modifier to set the Message Header, Exchange Property and Message Body.**

The ChatGPT HTTP API will be called with Authorization and ContentType values in the Message Header

So accordingly provide the Header constant in the Content Modifier with Content-Type as application/json

And Authorization will be the Bearer (space) API key generated in the step-1

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-29.png)

Image source from my trail account on SA...