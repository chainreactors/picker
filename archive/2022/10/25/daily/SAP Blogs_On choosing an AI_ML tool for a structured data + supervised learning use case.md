---
title: On choosing an AI/ML tool for a structured data + supervised learning use case
url: https://blogs.sap.com/2022/10/24/on-choosing-an-ai-ml-tool-for-a-structured-data-supervised-learning-use-case/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:25.924519
---

# On choosing an AI/ML tool for a structured data + supervised learning use case

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* On choosing an AI/ML tool for a structured data + ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160500&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [On choosing an AI/ML tool for a structured data + supervised learning use case](/t5/technology-blog-posts-by-members/on-choosing-an-ai-ml-tool-for-a-structured-data-supervised-learning-use/ba-p/13552634)

![leojmfrancia60](https://avatars.profile.sap.com/5/7/id5718db71ef1a48c6bd7b78e9f4396e71c41e127a0197ae32522cfb69e243122e_small.jpeg "leojmfrancia60")

[leojmfrancia60](https://community.sap.com/t5/user/viewprofilepage/user-id/40845)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160500)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160500)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552634)

‎2022 Oct 24
10:34 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160500/tab/all-users "Click here to see who gave kudos to this post.")

1,153

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Services/pd-p/73555000100700001042)
* [SAP AI Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Core/pd-p/73554900100800003641)
* [SAP AI Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Launchpad/pd-p/73555000100800003283)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [SAP AI Services

  Software Product](/t5/c-khhcw49343/SAP%2BAI%2BServices/pd-p/73555000100700001042)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Core

  SAP Business AI](/t5/c-khhcw49343/SAP%2BAI%2BCore/pd-p/73554900100800003641)
* [SAP AI Launchpad

  SAP Business AI](/t5/c-khhcw49343/SAP%2BAI%2BLaunchpad/pd-p/73555000100800003283)

View products (6)

After [getting caught up on the available AI/ML tools](https://blogs.sap.com/2022/10/18/sap-ai-and-ml-tools-when-to-use-what-insights-2022-edition/) within the SAP ecosystem and finding yourself ready to progress on the journey, you might ask - what's next?

If you are like me and have been curious about how SAP's AI/ML offerings can be evaluated in your landscape and are looking for some practical first steps, this may be a great place to start. We observed the points below in selecting the appropriate SAP AI/ML tool to productionize our models - it would be great if you can share your experience and findings in the comments as well.

This blog might be useful to you if:

1. Your organization has started its AI/ML journey, having **at least** (1) awareness and (2) vision to use AI/ML - both are early steps for a data-driven business transformation (source: [Gartner](https://www.gartner.com/en/documents/3991368), subscription required)

2. You have identified a few tools within the SAP ecosystem that apply to your AI/ML use case, do have a look at [my previous blog post](https://blogs.sap.com/2022/10/18/sap-ai-and-ml-tools-when-to-use-what-insights-2022-edition/) on said tools for more details

3. You have reviewed articles on how to compare tools/models but want to start with something more basic

The scenario used as a reference for pointers discussed in this blog post:

1. Uses [structured](https://machine-learning.paperspace.com/wiki/structured-vs-unstructured-data) and labeled training data set **outside** S/4HANA for [supervised learning](https://towardsdatascience.com/supervised-vs-unsupervised-learning-14f68e32ea8d) specific to a real business case (~100,000 observations) which cannot be shared here; i.e. not taken from open datasets such as [Kaggle](https://www.kaggle.com/datasets)

2. Has access to SAP and non-SAP AI/ML tools, primarily through trial versions

3. Uses [AutoML](https://en.wikipedia.org/wiki/Automated_machine_learning) feature in the tools being evaluated, keeping the same parameters (e.g. training time, class balancing, etc.) across all tools

The idea: Standardizing the data, approach, and parameters across the different tools for evaluation will provide a data-driven basis for identifying which tool is best for my use case.

The caveats:

1. You do not have to compare the tools every time you have a use case. If your organization has some use cases in mind that you want to pilot but have not decided on a tool yet, this might be a worthwhile exercise

2. As mentioned above, the hints here are based on an AI/ML use case that has [structured](https://machine-learning.paperspace.com/wiki/structured-vs-unstructured-data) and labeled training data in a [supervised learning](https://towardsdatascience.com/supervised-vs-unsupervised-learning-14f68e32ea8d) use case

Now, for the pointers.

### 1. Start small and think big

According to [Gartner's Roadmap for Data Literacy and Data-Driven Business Transformation](https://www.gartner.com/en/documents/3991368) (subscription required), the next steps after (1) selling the value and (2) building the vision are (3) assessments and (4) education before (5) embedding AI/ML into the business. While the broader organization may be looking at roadmap steps (3) and (4), it would be beneficial to run pilots that have a high probability of contributing measurable success to the business. An example of a pilot area would be the automated classification of data entries, which can be addressed by SAP Business Services Data Attribute Recommendation (DAR). You can make use of [CRISP-DM](https://blogs.sap.com/2018/08/28/sap-machine-learning-approaching-your-project/) as your framework in deploying your use case.

The pilot areas explored should align with the broader vision: to ensure the success of the organization.

### 2. Review architectural fit

Assess how the tools directly address your use case.

*Do you require online inference using data within and outside S/4HANA?* SAP AI Core or Data Intelligence may be suitable but do make use of the provided capacity unit calculator (see next point).

*Are you looking at batch reporting of AI/ML predictions for a fixed number of stakeholders?* SAP Analytics Cloud may be suitable.

*Do you have a use case specific to S/4HANA?* Then it may be worthwhile looking at ISLM.

*Does your team have data scientists who prefer to work on hyperscaler ML platforms?* You can consider SAP FedML to avoid replicating training data from your business systems to the hyperscaler platforms.

### 3. Analyze tool pricin...