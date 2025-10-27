---
title: What is a composable enterprise? And who is the composer?
url: https://blogs.sap.com/2022/12/22/what-is-a-composable-enterprise-and-who-is-the-composer/
source: SAP Blogs
date: 2022-12-23
fetch_date: 2025-10-04T02:19:32.529036
---

# What is a composable enterprise? And who is the composer?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Additional Blog Posts by SAP](/t5/additional-blog-posts-by-sap/bg-p/additional-blog-sap)
* What is a composable enterprise? And who is the co...

Additional Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/additional-blog-sap/article-id/52744&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What is a composable enterprise? And who is the composer?](/t5/additional-blog-posts-by-sap/what-is-a-composable-enterprise-and-who-is-the-composer/ba-p/13557568)

![mariafay](https://avatars.profile.sap.com/e/e/idee7bb943c71cfa8535fe332d0dcf997a57d6847e988158f5f914b2c5142abb27_small.jpeg "mariafay")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mariafay](https://community.sap.com/t5/user/viewprofilepage/user-id/12587)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=additional-blog-sap&message.id=52744)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/additional-blog-sap/article-id/52744)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557568)

‎2022 Dec 22
5:48 PM

[15
Kudos](/t5/kudos/messagepage/board-id/additional-blog-sap/message-id/52744/tab/all-users "Click here to see who gave kudos to this post.")

10,225

* SAP Managed Tags
* [Digital Technologies](https://community.sap.com/t5/c-khhcw49343/Digital%2520Technologies/pd-p/33d804ef-26b2-4f01-b858-ddef6871cb3b)

* [Digital Technologies

  Topic](/t5/c-khhcw49343/Digital%2BTechnologies/pd-p/33d804ef-26b2-4f01-b858-ddef6871cb3b)

View products (1)

This post reflects a view from the field on how composable enterprise is seen by analysts and companies, as well as a consultant’s perspective on various aspects of implementing composable enterprise in an organization.

First of all: You do not have to be Mozart or Beethoven to compose an enterprise, and it does not have to do with music at all, besides the creative elements.

So let us define what a composable enterprise is. SAP’s Board Member Jürgen Müller [has emphasized](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6978750379677126657/) composable business as being “agile and open to change and disruption.” Gartner, among the first to coin the term, has described it in the following way:

***“Composability in a business context [means] architecting your business for real-time adaptability and resilience in the face of uncertainty.”*** [Gartner Keynote](https://www.gartner.com/smarterwithgartner/gartner-keynote-the-future-of-business-is-composable), 2020

It seems that agility and resilience are the key characteristics of composability, with various technologies that can now be placed behind it. This is also why some bring together the concept of composability with MACH architecture (***M***icroservices, ***A***PI-first, ***C***loud-native and ***H***eadless).

Let’s take an easy analogy: When you think of your company as a pasta dish (yes, we all like some good Italian food!), what is the first thing that comes into your mind? A multilayer lasagna? Some ravioli? Or maybe slightly disorganized but tasty spaghetti? A short survey of some friends (no scientific basis involved) showed that very few of them think of modular raviolis, rather going for more hierarchical or chaotic comparisons.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture-1-1.jpg)*Figure 1. What does pasta have to do with composability?*

What is behind the big buzz of composability? On the one hand, current system landscapes are too complex, causing slow response to change (which is needed as much as ever in such turbulent times), partially redundant solutions, and vendor dependency. On the other hand, there is a need to be more flexible, to freely choose from millions of solutions and platforms out there, and to focus on outcomes.

Should enterprises become composable if they want to be agile? Is life different in the composable world? For this, let us first understand what being composable ***means***.

## **Defining composability**

There are three key building blocks of composability ([as defined by Gartner](https://www.gartner.com/smarterwithgartner/gartner-keynote-the-future-of-business-is-composable)![:disappointed_face:](/html/@59FA2E79CF9A18D1BFE50058D3E31BAD/emoticons/1f61e.png ":disappointed_face:")

* ### **composable thinking,**

focusing on a different (adaptive) approach towards strategy, more flexible organizational structures, and different planning cycles.

* ### **composable business architecture,**

featuring a value-based approach towards processes, working with business capabilities, and promoting distributed accountability.

* ### **composable technologies,**

characterized by agile development methodologies, modular architecture, and distributed data processing.

Those building blocks are somewhat similar to existing and well-established methodologies, although now in a composable context. As an example, TOGAF (The Open Group Architecture Framework) highlights the importance of business architecture and technology architecture and the [SAP Enterprise Architecture Framework](https://groups.community.sap.com/t5/enterprise-architecture-blog/sap-enterprise-architecture-framework/ba-p/124037) (Figure 2) deals with capability, process, data, and organizational views.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture-2-4.png)

Figure 2. SAP Enterprise Architecture Framework

As a recent methodology, [Scaled Agile Framework®](https://scaledagile.com/what-is-safe/) (SAFe®) introduces organizational and workflow patterns for implementing agile practices in an enterprise. Does it ‘support’ the principles of composability? Indeed – however, it takes more than a methodology to achieve the desired agility and composability in a company and its enterprise architecture.

## **So how do those three aspects come together in a composable enterprise?**

The key principles of composable business are: modularity, discovery, autonomy, and orchestration (see Figure 3).

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture-3-2.png)

Figure 3 Composable Architecture

Let us take the example of a pricing engine, providing price recommendations for various product lines.

In a composable world, **Modularity** would mean that there is a packaged business capability behind it that would encapsulate this one process (product pricing), have a certain purpose (such as optimizing pricing and maximizing income), and lead to an outcome (price recommendations).

**Discovery** would mean that the capability relies on a certain information architecture for certain objects (such as products) and is searchable / can be identified by the business and (re)used for certain business purposes (calculating price for a new product line).

**Autonomy** means that this capability can run independently (from architecture- and deployment perspectives) from other capabilities, have a certain governance process (product owner, lead architect, lead developer), have a certain life cycle (with releases, deployments, updates), and be scalable (cloud-native architecture is key in that case).

Finally, **Orchestration** focuses on security components, API support, workflow orchestration, and similar topics.

Following these...