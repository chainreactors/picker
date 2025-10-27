---
title: SAP Supports customers in becoming Intelligent Sustainable Enterprises (IES)
url: https://blogs.sap.com/2022/12/06/sap-supports-customers-in-becoming-intelligent-sustainable-enterprises-ies/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:14.715908
---

# SAP Supports customers in becoming Intelligent Sustainable Enterprises (IES)

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* SAP’s powering technology enabling customers in be...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47340&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [SAP’s powering technology enabling customers in becoming Intelligent Sustainable Enterprises (IES)](/t5/application-development-and-automation-blog-posts/sap-s-powering-technology-enabling-customers-in-becoming-intelligent/ba-p/13566967)

![former_member721319](https://avatars.profile.sap.com/former_member_small.jpeg "former_member721319")

[former\_member721319](https://community.sap.com/t5/user/viewprofilepage/user-id/721319)

Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47340)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47340)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566967)

‎2022 Dec 06
10:27 PM

[5
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47340/tab/all-users "Click here to see who gave kudos to this post.")

942

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)

* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

View products (2)

SAP offers RISE with SAP to enable customers in becoming Intelligent and Sustainable Enterprises (IES). RISE with SAP offers customers a flexible solution combining Cloud ERP, Industry best practices, Analytics and more, under a single contract.

Behind the scenes, SAP’s powering technology is responsible for making this happen. In this blog, I would like to share about the technology responsible for gluing together the different SAP solutions into a whole being greater than the sum of its parts.

You might have heard about Desired state repository, it is a method of using API calls in a unified and centric way, it simplifies the activation of Micro-Services which are designed to serve different requests from different users. One of the important principles of this concept is a declarative programming paradigm, in which the user declares what the desired state is for him and the various services work to achieve it. This concept is well known in Kubernetes and other cloud providers.

Why is using a desired state repository worthwhile? Traditionally app developers need access to every API to make changes and consume services. Using APIs requires time to learn, understand, and plan since every API is different and might behave differently. For instance, input from a user can be processed instantly or be save for later. If services require a similar input, the user will have to provide it again and separately for every service provider. In addition, if a service would like to access data of a different service it would require integration to extract the data and copy it to a different location.

The current approach requires to deal with the working with different APIs- connecting, securing and saving data, transferring data between APIs and more. This is the reason a different approach is required, offering a simple integration process between two services. Providing a holistic solution for integrating solutions can significantly improve the ability to interact with new solutions, expand existing solutions and thus save valuable development time and resources.

How can it be done differently? First of all, by centralizing and unifying the APIs. This means all requests can be received in a centralized and common way (uniform API contract) and not in the way that each Service defines its API.

The second step is a paradigm shift - moving from consuming services to working with a declarative programming paradigm. The declarative paradigm is very important because it can simplify the development process. With this method, the developer is not required to know and program all the actions that need to be performed to reach a certain desired state (in the past this required familiarization and usage of many APIs), but he/she is only required to describe the desired state and hence the system works to provide it in the best possible way.

For example, a developer wants to develop a service that would be able to make the following steps:

1. Create a new account.

2. Create a primary user for the account.

3. Provide service ‘A’ to the account.

4. Provide service ‘B’ to the account.

5. Update the account with the services provided.

Imperative paradigm example:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-05-at-13.51.10-1.png)

Imperative paradigm

Declarative paradigm example:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-05-at-13.49.18-1.png)

Declarative paradigm

We built a desired state repository using declarative programming tailored for our needs to centralize and unify the APIs. The goal was to build a control plane that can address common challenges: large scale of operation, lifecycle and version management and robust privilege management. The solution was inspired by Kubernetes API server and we implemented on top a hierarchical structure of folders and additional capabilities that were required.

To conclude, the solution we built simplifies and reduces the time it takes developers to implement internal integrations and to extend existing services. The advantages provided by this solution can enable us in the future to extend the use of this solution for others.

* [IntelligentSustainableEnterprises](/t5/tag/IntelligentSustainableEnterprises/tg-p/board-id/application-developmentblog-board)
* [onesap](/t5/tag/onesap/tg-p/board-id/application-developmentblog-board)
* [SAP](/t5/tag/SAP/tg-p/board-id/application-developmentblog-board)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin