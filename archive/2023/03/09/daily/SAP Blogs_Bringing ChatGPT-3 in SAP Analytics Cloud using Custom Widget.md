---
title: Bringing ChatGPT-3 in SAP Analytics Cloud using Custom Widget
url: https://blogs.sap.com/2023/03/08/integrating-chatgpt-3-in-sap-analytics-cloud-using-custom-widget/
source: SAP Blogs
date: 2023-03-09
fetch_date: 2025-10-04T09:01:18.272995
---

# Bringing ChatGPT-3 in SAP Analytics Cloud using Custom Widget

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Bringing ChatGPT in SAP Analytics Cloud using Cust...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163102&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Bringing ChatGPT in SAP Analytics Cloud using Custom Widget](/t5/technology-blog-posts-by-members/bringing-chatgpt-in-sap-analytics-cloud-using-custom-widget/ba-p/13567616)

![danishmeraj](https://avatars.profile.sap.com/d/b/iddb2cfdeb96c693738e11426808246b9f36b70fae67976670055df13ff4605896_small.jpeg "danishmeraj")

[danishmeraj](https://community.sap.com/t5/user/viewprofilepage/user-id/810158)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163102)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163102)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567616)

‎2023 Mar 08
10:27 PM

[26
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163102/tab/all-users "Click here to see who gave kudos to this post.")

14,034

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [SAP Analytics Cloud, connectivity](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520connectivity/pd-p/0db4caf8-3039-4a93-9d11-543de33255a4)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP Analytics Cloud, connectivity

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bconnectivity/pd-p/0db4caf8-3039-4a93-9d11-543de33255a4)

View products (6)

Part - 1: Bringing ChatGPT in SAP Analytics Cloud using Custom Widget

Part - 2: [Data Discovery using ChatGPT in SAP Analytics Cloud](https://blogs.sap.com/2023/09/04/data-discovery-using-chatgpt-in-sap-analytics-cloud/)

"Integrating ChatGPT-3 in SAP Analytics Cloud using the custom widget". Sounds complex? Believe me! It is not. You can do it in less than 30 mins, even if you are an absolute beginner.

This blog post will explain how to create an analytic application in the SAP Analytics Cloud that can take user queries and return responses. It will involve creating a custom widget in the SAP Analytics Cloud to integrate with ChatGPT-3 using the OpenAI API. We will achieve this goal in **7 easy steps**. All the relevant files can also be found on my GitHub repository [here](https://github.com/dmeraj/integrating-chatGPT3-in-SAC).

**Step 1: Prerequisites:**

Before we proceed with the creation of a custom widget and its integration in SAC, it is important that you fulfill the following requirements.

* **Create an account on the OpenAI platform:**Create an account on the OpenAI platform by visiting this URL [here](https://chat.openai.com/auth/login).

* **Getting the API key:**Create a secret key in the "Build your application" section of the page by visiting this URL [here.](https://platform.openai.com/docs/quickstart/build-your-application)

![](/legacyfs/online/storage/blog_attachments/2023/03/create-APIKey-1.png)

*Figure 1: The figure shows creation of secret key.*

**Note:** Please ensure that you copy and securely save the secret key. This key will be required to make an API call in the future step.

**Step 2: Creating custom widget:**

The custom widget created in this blog will help us integrate SAP Analytics cloud with OpenAI API. Custom widget is created with different web components and a JSON file. These web components files differ according to the custom widget use case. In this case, we need two files, i.e., "customWidget.json" and "main.js".

*I will not cover the basics of custom widget but If you would like to understand custom widgets in detail, then I recommend reading this nice blog [Demystifying Custom Widgets for SAP Analytics Cloud](https://blogs.sap.com/2022/12/04/demystifying-custom-widgets-for-sap-analytics-cloud/) by Pranav Kandpal.*

Please select one method from Method 1 and Method 2. Note that **Method 1 is recommended** for quick creation of the custom widget.

**Method 1: Plug and Play**

Copy the below code and save it as a .json file to your local system with the name "customWidget" and proceed to **Step 3**.

```
{

  "eula": "",

  "vendor": "Danish",

  "license": "",

  "id": "com.danish.sap.sac.chatgpt",

  "version": "1.0.0",

  "name": "chatGPT SAC",

  "newInstancePrefix": "chatGPTInSAC",

  "description": "A custom widget to integrate chatGPT3 in SAC Analytic application",

  "webcomponents": [

    {

      "kind": "main",

      "tag": "custom-widget",

      "url": "https://dmeraj.github.io/integrating-chatGPT3-in-SAC/main.js",

      "integrity": "",

      "ignoreIntegrity": true

    }

  ],

  "properties": {

		"width": {

			"type": "integer",

			"default": 1

		},

		"height": {

			"type": "integer",

			"default": 1

		}

  },

  "methods": {

		"post": {

			"description": "Wrapper for jQuery post",

			"parameters": [

				{

					"name": "APIKey",

					"type": "string",

					"description": ""

				},

				{

					"name": "endPoint",

					"type": "string",

					"description": ""

				},

				{

					"name": "prompt",

					"type": "string",

					"description": ""

				}

			],

			"returnType": "string"

		}

  },

  "events": {

  }

}
```

**Method 2:**

* Copy the code below and Save it as .js file to your github. Ensure that the code is hosted and can be accessed from the URL.

  ```
  var ajaxCall = (key, url, prompt) => {

    return new Promise((resolve, reject) => {

      $.ajax({

        url: url,

        type: "POST",

        dataType: "json",

        data: JSON.stringify({

          model: "text-davinci-002",

          prompt: prompt,

          max_tokens: 1024,

          n: 1,

          temperature: 0.5,

        }),

        headers: {

          "Content-Type": "application/json",

          Authorization: `Bearer ${...