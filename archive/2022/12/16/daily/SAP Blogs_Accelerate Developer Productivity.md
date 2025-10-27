---
title: Accelerate Developer Productivity
url: https://blogs.sap.com/2022/12/15/accelerate-developer-productivity/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:00.312831
---

# Accelerate Developer Productivity

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [DevOps and System Administration](/t5/devops-and-system-administration/gh-p/devops-sysadmin)
* [Blog Posts](/t5/devops-and-system-administration-blog-posts/bg-p/devops-sysadminblog-board)
* Accelerate Developer Productivity

DevOps and System Administration Blog Posts

Explore DevOps and system administration blog posts. Stay current with best practices, tools, and insights into efficient IT management strategies.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/devops-sysadminblog-board/article-id/226&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Accelerate Developer Productivity](/t5/devops-and-system-administration-blog-posts/accelerate-developer-productivity/ba-p/13552686)

![nlara](https://avatars.profile.sap.com/9/b/id9b212e1208681c68c553ebafa5be340a770e083c196f27616f2cf6a9a96c29db_small.jpeg "nlara")

[nlara](https://community.sap.com/t5/user/viewprofilepage/user-id/4773)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=devops-sysadminblog-board&message.id=226)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/devops-sysadminblog-board/article-id/226)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552686)

‎2022 Dec 15
9:49 PM

[5
Kudos](/t5/kudos/messagepage/board-id/devops-sysadminblog-board/message-id/226/tab/all-users "Click here to see who gave kudos to this post.")

1,053

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [DevOps](https://community.sap.com/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [DevOps

  Programming Tool](/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)

View products (2)

I frequently come across SAP developers that are eager to innovate but face technology hurdles that limit them. This is particularly frustrating since technology should serve as an engine for growth. This is not just my opinion; it has been proven by all the world's largest companies. If you are not innovating, you risk being passed up by companies that are. So the question arises, how can organizations accelerate developer productivity in an environment where waiting months for a shared development system is the norm?

To answer this, first, we have to thoroughly understand the motivation.

## ![accelerate-developer-productivity](https://www.nuveplatform.com/_next/image?url=%2Fimages%2Fblog%2Faccelerate-developer-productivity.png&w=1080&q=75)

## Can Technology Drive Business Value?

Top-performing companies know that internal IT is as critical as customer-facing technology. However, metrics for internal IT are not as straightforward, leading most companies to only see it as a cost center. Too often, the inability to correctly measure ROI leads to missed opportunities.

IT becomes a value driver and innovation engine when the ROI is measured correctly and a framework to improve productivity is in place. Organizations that do not leverage IT as a value driver risk being surpassed by those that do. This blog explores how improving developer productivity is the catalyst for building and scaling high-performing technology and organizations.

## Measuring the Unmeasurable

How do you measure developer productivity? It is not as easy as it may seem. If developers are evaluated against the wrong metrics, they will learn to game the system.

For example, if you measure lines of code, it's easy to write overly complex code for simple things. This is not the right approach, as it will quickly lead to technical debt.

So then you might think, let's measure productivity based on the number of transports. That can lead to increased risk as developers may rush to create a high number of transports, increasing the likelihood of a failure in production. Not to mention, transport management also poses risks.

What if you instead focus on the number of features completed. This is not fair since not all features are equal; some are more important than others and vary in implementation difficulty.

An observant reader may note that the metrics above are sacrificing speed or stability. And, of course, we want it all!

## No Trade-offs Between Speed and Stability

Instead of measuring productivity via isolated metrics, consider adopting the framework based on Accelerate.

1. Delivery lead time - the time it takes for a feature to make it from the first line of code to production

2. Deployment frequency - the number of deploys to production

3. Time to restore service - the time it takes to correct an issue in production

4. Change rate fail - the percentage of deploys that cause production issues

When these metrics are optimized collectively, you notice that there isn't a sacrifice between speed and stability. Instead, you set the foundation for becoming a high-performing organization. Elite IT teams achieve the following results:

1. Delivery lead time - less than 1 day

2. Deployment frequency - on-demand

3. Time to restore service - less than 1 hour

4. Change rate fail - 0-15%

## Culture Guides Everything

Metrics, frameworks, and technology are valueless if you don't also establish a healthy organizational culture.

**Healthy Culture**
The right metrics are used for positive change

**Toxic Culture**
Metrics are used as tools for control and culpability

Culture and process go hand in hand; they can be mutually reinforcing or mutually destructive.

Consider the shared DEV and QAS systems we've grown used to in the SAP world. These shared systems are intrinsically risky. As developers, we have the potential to break them, which would negatively impact everyone else on the team. So to mitigate the risk, companies put in processes and procedures that adversely affect productivity. With containerized SAP systems, you can eliminate the risk of adversely affecting others, allowing for a culture where you are free to try anything in your container.

## The Modern Approach to SAP Development

You've likely heard it, "implement DevOps!"

DevOps is a broad term that is often overused or misused. Instead, you should focus on implementing CI/CD pipelines. Leveraging several established best practices that include:

* Isolated development (ideally using containerized SAP systems)

* Intuitive version control (GitHub, GitLab, etc.)

* Test automation (ABAP Unit, [abaplint](https://abaplint.org/))

* Test data management (refresh your containerized SAP systems)

* Git-based workflows ([abapGit](https://abapgit.org/), GitHub, etc.)

Implementing these best practices puts you in a promising position to increase productivity. Coupled with a healthy culture, your IT team can provide a competitive advantage and pass up competitors that do not value the performance of software delivery teams.

Credits:

> Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations by Nicole Forsgren Ph.D., Jez Humble, Gene Kim

> Photo by [Carl Heyerdahl](https://unsplash.com/photos/KE0nC8-58MQ) on [Unsplash](https://unsplash.com/)

* [CICDforSAP](/t5/tag/CICDforSAP/tg-p/board-id/devops-sysadminblog-board)
* [containers](/t5/ta...