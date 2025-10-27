---
title: Integrating Artificial Intelligence with SAP ABAP using Microsoft AI SDK
url: https://blogs.sap.com/2023/08/18/integrating-artificial-intelligence-with-sap-abap-using-microsoft-ai-sdk/
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T11:59:47.927154
---

# Integrating Artificial Intelligence with SAP ABAP using Microsoft AI SDK

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Integrating Artificial Intelligence with SAP ABAP ...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47861&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Integrating Artificial Intelligence with SAP ABAP using Microsoft AI SDK](/t5/application-development-and-automation-blog-posts/integrating-artificial-intelligence-with-sap-abap-using-microsoft-ai-sdk/ba-p/13576757)

![adapatejanavya](https://avatars.profile.sap.com/2/9/id29cb07aad236e60e6eb0716ae721a5f18405a10020eb21c56a17049baf6a92b2_small.jpeg "adapatejanavya")

[adapatejanavya](https://community.sap.com/t5/user/viewprofilepage/user-id/155949)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47861)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47861)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13576757)

‎2023 Aug 18
10:07 PM

[11
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47861/tab/all-users "Click here to see who gave kudos to this post.")

12,871

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

View products (2)

Hi Abapers,

We all know that the use of AI has been rapidly increasing in all fields now a days. With the help of  AI one can easily automate tasks, reduce their work process and produce more efficient solutions.

So, to achieve such results in ABAP, Microsoft has introduced AI SDK for SAP ABAP.

Now let's dive into it.

**INTRODUCTION**

Microsoft AI SDK is user-friendly and have an innate interface. This helps the developers to easily integrate the AI capabilities into ABAP. The current version of AI SDK provides the ability to integrate OpenAI and Azure OpenAI capabilities.

We can incorporate AI capabilities such as Machine learning, Natural language processing and so on into ABAP applications to improve customer experience, automate tasks and make efficient business decisions.

So, to achieve this all we have to do is to install AI SDK for SAP ABAP to our systems and create either an Azure OpenAI or OpenAI account.

You can follow this [Blog](https://www.linkedin.com/pulse/ai-sdk-sap-abap-learning-series-part-1-initial-setup-gopal-nair?trk=article-ssr-frontend-pulse_more-articles_related-content-card) from LinkedIn by Gopal Nair to setup your system with AI SDK.

Now lets see an example on how we can use this.

We can deploy a GPT model into ABAP and chat with it. Lets say we asked AI to get you back with a test program for our query.

![](/legacyfs/online/storage/blog_attachments/2023/08/7-8.png)

So when we execute it, we will receive an output something like this.

![](/legacyfs/online/storage/blog_attachments/2023/08/9-6.png)

We can also develop this, so that we can use it as a chatbot not only for developers but also for customers to improve user experience.

Consider that you have a requirement and need to produce new report for it. What if we have a way to get the report for it automatically. You just need to provide it with the query and name of the report.

![](/legacyfs/online/storage/blog_attachments/2023/08/16-6.png)

Now it creates a program and updates it in the given report.
Like this,

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-62.png)

This helps in saving a lot of time for the ABAP developers.

AI models can be trained here for specific tasks. This can be achieved by using fine-tunes program to train the AI models.

So, once we get to understand it we can accomplish many more things such as,

* We can use AI SDK to create chatbot like solution that can interpret user’s request for a particular task.

* Developers may enter syntax as comments in the ABAP editor, pass it along to Open AI, and receive recommendations from the same editor in return.

* Developer can automate few manual tasks.

* We can input our data to prompt and get back an analysis from it.

Even though there are good advantages by using AI SDK, we also face some limitations. Such as,

1. AI models expect rich data quality. If the data used to train them is not good enough, the outputs can be unpredictable.

2. They need access to private data which causes security risk.

3. AI models can be hard to understand. So it takes some time for developers to get a hang of it. But once you get to understand how to utilize one AI model, you can easily grasp different AI models.

The fact that AI may be used in ABAP does not imply that ABAP developers' careers are in danger. To make our work easier, it requires developers like us to train and implement it.

Microsoft is making a lot of effort to improve the AI SDK. Therefore, the AI SDK will likely release a lot of new upgrades and experiences in the following days.

**REFERENCES**

You can follow up with these links to learn more about using the AI SDK.

* <https://microsoft.github.io/aisdkforsapabap/>

* [**Announcing – Microsoft AI SDK for SAP | SAP Blogs**](https://blogs.sap.com/2023/05/12/announcing-microsoft-ai-sdk-for-sap/)

* [**OpenAI**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169) [**#**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169)[**AISDKforSAPABAP**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169) [**#**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169)[**SAPonAzure**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169) [**#**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-announcing/ba-p/3818169)[**MicrosoftAISDK**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/propelling-the-aerodynamics-of-enterprise-innovation-an...