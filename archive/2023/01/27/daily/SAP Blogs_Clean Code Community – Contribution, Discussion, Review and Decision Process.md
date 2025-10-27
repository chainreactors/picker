---
title: Clean Code Community – Contribution, Discussion, Review and Decision Process
url: https://blogs.sap.com/2023/01/26/clean-code-community-contribution-discussion-review-and-decision-process/
source: SAP Blogs
date: 2023-01-27
fetch_date: 2025-10-04T04:58:15.362184
---

# Clean Code Community – Contribution, Discussion, Review and Decision Process

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Clean Code - Contribution, Discussion, Review and ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159393&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Clean Code - Contribution, Discussion, Review and Decision Process](/t5/technology-blog-posts-by-sap/clean-code-contribution-discussion-review-and-decision-process/ba-p/13554739)

![haeuptle](https://avatars.profile.sap.com/d/0/idd099b643170a795cffeb57f54e74f97436f5a5f26bb8d41fc62037e69aae99a0_small.jpeg "haeuptle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[haeuptle](https://community.sap.com/t5/user/viewprofilepage/user-id/40145)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159393)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159393)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554739)

‎2023 Jan 26
4:24 PM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159393/tab/all-users "Click here to see who gave kudos to this post.")

3,893

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Community](https://community.sap.com/t5/c-khhcw49343/SAP%2520Community/pd-p/486157991894093153608181816584982)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Community

  Topic](/t5/c-khhcw49343/SAP%2BCommunity/pd-p/486157991894093153608181816584982)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (7)

# Clean Code - From Contribution to Decision

[Clean code](https://blogs.sap.com/2022/12/21/clean-code-writing-maintainable-readable-and-testable-code/) is a term used to describe software that is easy to read, understand, maintain and test. With the adoption of the clean code style guide by thousands of teams, changes to the style guide can have a large potential impact on developers (e.g. through new static code checks for new rules). While there is usually huge agreement for most of the style guide, there can also be very controversial conversations regarding some rules.

To improve the quality of the decision, the involvement of the interested engineers and be able to make decisions and keep pace with recent language developments, we need to improve the process for collaboration, moderation and decision making. In this blog I want to explain the current draft process for contribution, discussion, review and decision making. This process became necessary to deal with the increasing amount of feedback and change proposals. Probably we will make the process also part of the [style guide](https://github.com/SAP/styleguides) repository later this year.

If you do not miss an update on clean code, test automation, communities of practice, decision making, testability and other engineering / craftsmanship / architecture topics, [subscribe to the brand new newsletter](https://ecosystem4engineering.substack.com/p/collaboration-on-improving).

# Clean Code - Contribution, Discussion, Review and Decision Process

With the success of Clean ABAP and Clean SAPUI5 there comes the need for a more formal process when it comes to reviewing issues and improvement proposals. Clarity on how those should be opened, are processed and the typical timeframe. Besides, especially for changes with a larger impact (e.g. incompatible changes) we need a formal process for decision making.

## Principles for Decision Making

The style guides are based on some universal principles. So when we make the decision between different alternatives we keep those principles in mind:

* Testability: Every piece of code needs to be testable in an efficient, fast and robust way

* Readability and Maintainability is important and determines developer productivity

  + [Studies](https://www.researchgate.net/publication/359129462_Code_Red_The_Business_Impact_of_Code_Quality_--_A_Quantitative_Study_of_39_Proprietary_Production_Codebases) found that developers spend about 60% of their development time on program comprehension activities and at least 10 times the amount of time is used for reading compared to writing the same piece of code.

* Readability and Modularity over premature performance optimization, but performance is important (e.g. mass read over single read)

* Tradeoffs: If we cannot come up with a consensus, we list the tradeoffs and explain the consequences of the alternatives.

* Same terminology and principles across programming languages (e.g. [testing terminology](https://blogs.sap.com/2021/12/06/shared-language-for-talking-about-test-strategy/) is the same for JavaScript and ABAP)

## Review and Discussion

Compared to an open source software project, the rate of change for a style guide should be much slower. Due to the adoption by many projects and usage by S4HANA as official programming guideline changes can have an impact on many projects and can result in an adjustment of code check profiles. Therefore, we want to give the readers and contributors enough time to have a conversation on the issues and pull requests.

When moderating the discussion and more clarity is needed for the discussed topic you should consider the following. Discussions are unlikely to give a clear picture of the community as a whole for several reasons. They favor people who like to argue, those who are more articulate or have more experience in English (or whatever language the discussion is in), and those who feel like they're in the "in" crowd and will have a popular opinion. Finally, they hide how many people are in agreement with someone who speaks up. With this in mind, use the discussion to explore different sides of the issue. Raise awareness of the discussion by announcing in the respective channels (if appropriate) to make sure that the entire community is able to weigh in.

## Labeling

For deciding how to proceed with a pull request, we want to classify the different issues ...