---
title: Secure your APIs using JSON Web Token (JWT)
url: https://blogs.sap.com/2023/02/05/secure-your-apis-using-json-web-token-jwt/
source: SAP Blogs
date: 2023-02-06
fetch_date: 2025-10-04T05:47:27.281687
---

# Secure your APIs using JSON Web Token (JWT)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Secure your APIs using JSON Web Token (JWT)

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162762&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Secure your APIs using JSON Web Token (JWT)](/t5/technology-blog-posts-by-sap/secure-your-apis-using-json-web-token-jwt/ba-p/13564819)

![mangeshpise](https://avatars.profile.sap.com/3/c/id3cb00775f418fcc9e7a52a6b3ed81fe1dff09089a9df8d25937baeb7b95559e1_small.jpeg "mangeshpise")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mangeshpise](https://community.sap.com/t5/user/viewprofilepage/user-id/3250)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162762)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162762)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564819)

‎2023 Feb 05
12:32 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162762/tab/all-users "Click here to see who gave kudos to this post.")

18,106

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

The phrase, "Data is the new oil," quickly resonated with the masses when British mathematician Clive Humbly first coined it in 2006. Michael Palmer described the similarities between oil and data. Michael indicated that just like crude oil, data has no intrinsic value early on until it gets cleaned and refined, which makes it ready for consumption (Palmer, 2006). Consumption-ready data is valuable and can be shared in exchange for value. For example, coded medical records are of immense value to hospitals as it helps them identify effective clinical pathways to treat their patients. Point-of-Sales (POS) datasets from retail stores and e-commerce platforms are utilized to identify upsell opportunities. Rich enterprise datasets can also be used to create headless content management systems (CMS), which enable a rich user experience. For example, targeted product details, pricing, customer reviews, etc., can be seamlessly provided to prospective customers via multiple interfaces such as mobile notifications, web pages, mobile apps, intelligent assistants, etc.

The most common approach to sharing such data is via APIs. Frontend applications or backend services can request real-time data via APIs and either presents them on a user interface or process them via backend services to support a business process. For instance, by leveraging APIs from your choice of a payment processor, a developer can easily enable PCI-compliant online payment capability on its app or website.

However, such APIs must be restricted to authorized users or members, typically external consumers. And that's where API security comes into play. This blog post will focus on using the upcoming JSON Web Tokens (JWT) standard ([RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) to protect your APIs. Although the concepts can be applied to both internal-facing and external-facing APIs, the perspective maintained in this blog post is the latter, just to help you maintain a consistent frame of mind. Do note that it takes much more than just a token to secure the APIs completely. However, to prevent getting lost in all the moving parts around securing APIs and web applications, this blog post strictly explains how tokens can be used for authenticating API calls.

The most common approach that might come to one's mind would be to have the actual API / Web Service perform authentication based on some information passed during the API call. Two such implementations are Basic Authentication and API-Key based authentication. Both these are discussed below, but it is essential to understand the impact of this approach on the overall scalability aspect of the architecture. And that is another purpose of this blog post I'd like to clarify, which has to do more with the impact of JWT-based security on the overall scalability aspect of the architecture versus discussing comparisons between multiple authentication methods.

## Scaling issue with API Authentication

Because REST APIs are stateless, there is no way for the service to know about your previous calls, nor can you have it remember you for subsequent calls. Each call is independent. If the caller must be authenticated repeatedly with every API call, the authentication server, responsible for the actual username and password authentication, is hit every time the API is called. Please look at Fig. 1(A) below, which shows a generic API request/response flow that includes an authentication step.

There are two scenarios in which scaling can become a major concern. Each of these are described below.

**Scaling Scenario 1:** Imagine one customer that calls your API setup using Basic authentication at least 100 times everyday. The total number of calls to the authentication server will also be at least 100 per day since each stateless API call needs to be authenticated individually.

![](/legacyfs/online/storage/blog_attachments/2023/01/auth-flow-Page-1.drawio.png)

Fig. 1(A): Single API request-response with authentication

If we scale our customers by double (i.e., 2 customers), the number of API calls will now be 200 per day, meaning the calls to the authentication server will also double, becoming 200 calls per day. So, if you need to increase the capacity in your API infrastructure, even the authentication server capacity needs to be upscaled.

**Scaling Scenario 2:** Imagine you have two externally exposed APIs secured via Basic authentication against a single authentication server. Let's also assume that our single customer calls each of the APIs 100 times per day. Under these situations, the calls to the authentication servers will be a summation of authentications between both APIs, i.e., 200 authentications per day.

![](/legacyfs/online/storage/blog_attachments/2023/01/auth-flow-Page-2.drawio-1.png)

Fig. 1(B): Multiple APIs request-response with authentication

Just like in scenario 1, if our customer base doubles to 2 customers, who also call both the APIs 100 times a day, the total API calls would be somewhere to the order of -

2 customers x (100 calls x 2 APIs) = 400 calls per day. Effectively meaning that the calls to the authentication server will also be 400 calls per day.

In conclusion, although each of the API services can be scaled individually based on the volume of calls, the authentication server must be scaled considering the total API call volume. It also quickly becomes the sing...