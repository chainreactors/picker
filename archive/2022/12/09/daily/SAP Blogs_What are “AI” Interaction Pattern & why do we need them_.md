---
title: What are “AI” Interaction Pattern & why do we need them?
url: https://blogs.sap.com/2022/12/08/what-are-ai-interaction-pattern-why-do-we-need-them/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:43.937829
---

# What are “AI” Interaction Pattern & why do we need them?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* What are AI interaction patterns & why do we need ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161821&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What are AI interaction patterns & why do we need them?](/t5/technology-blog-posts-by-sap/what-are-ai-interaction-patterns-why-do-we-need-them/ba-p/13561752)

![schale29](https://avatars.profile.sap.com/a/1/ida1108399369ba9c6690445af8f166e44da4027a2c6f6434fb35c4c7241012ce0_small.jpeg "schale29")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[schale29](https://community.sap.com/t5/user/viewprofilepage/user-id/274734)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161821)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161821)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561752)

‎2022 Dec 08
8:57 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161821/tab/all-users "Click here to see who gave kudos to this post.")

3,343

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [Design Thinking](https://community.sap.com/t5/c-khhcw49343/Design%2520Thinking/pd-p/617904475839583685536714765406723)
* [User Experience](https://community.sap.com/t5/c-khhcw49343/User%2520Experience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)
* [User Experience

  Topic](/t5/c-khhcw49343/User%2BExperience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)
* [Design Thinking

  Topic](/t5/c-khhcw49343/Design%2BThinking/pd-p/617904475839583685536714765406723)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

View products (5)

**Communication target:***The topic* *of this article concerns the set-up of a continuous series of small articles for* <https://community.sap.com>*.* For more details on my motives and profile please also read my first article posting about [approaching 'intelligence' as a designer](https://blogs.sap.com/2021/02/16/approaching-intelligence-from-a-design-standpoint/).

# Does SAP think about repeatable solutions to AI interaction problems?

SAP's AI Design Practice team has investigated various AI products and examined different interaction patterns for human-AI-interaction in the past. Our hypothesis was that, even though the individual objective of applications might vary a lot, how their solutions surface on the UI will eventually consolidate within a recognizable pattern. Most commonly we can view such a pattern emergence in the quite popular introduction of recommendation systems in many of today’s products in the consumer, as well as B2B, markets.

## What is an interaction pattern in UX?

**'[Patterns](https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/interaction-design-patterns?gclid=Cj0KCQiAmaibBhCAARIsAKUlaKQDo6FT0DkBngj7G7J_oD3Bi9NHivXv0qvmp-k914q6c5XRGpk6_TMaAoe-EALw_wcB "https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/interaction-design-patterns?gclid=cj0kcqiamaibbhcaarisakulakqdo6ft0dkbngj7g7j_od3bi9nhivxv0qvmp-k914q6c5xrgpk6_tmaaoe-ealw_wcb")'** are a common theme in UX / interaction design. Without them, designers would need to figure out each time anew how UI elements can be manipulated and interacted with to achieve various user objectives. *([Find an in depth definition for 'interaction pattern' here linked from IxDF.org](https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/interaction-design-patterns?gclid=Cj0KCQiAmaibBhCAARIsAKUlaKQDo6FT0DkBngj7G7J_oD3Bi9NHivXv0qvmp-k914q6c5XRGpk6_TMaAoe-EALw_wcB))*

If you are already familiar with the concept of UX pattern, you might want to skip to the next passage.

Thanks to all the prior work of the designers and UX researchers that came before us, many patterns in **Human Computer Interaction** **(HCI)** have been discovered and documented in detail already, so we are now able to choose from a rich set of options. For example, if we want to give the user the ability to revert wrong entries, we can make use of the "undo / redo" pattern. If we would like to guide our user in navigating our content, we use "progressive disclosure" to reveal information bit by bit. And if you would like to allow your user to change the order or location of items intuitively, the pattern of "drag & drop" provides a readymade solution.

**Are UI and UX patterns the same?**The two terms are mostly used interchangeably, or confused with other things like style guides or component libraries. In short, a UX pattern is defined by the user’s interaction along their journey through the product and therefore includes the individual steps the user needs to take in order to reach their objective / execute a certain operation. UX also includes the UI elements through which a user executes those steps and how the system returns feedback to them about the success of their actions.

**Drag-&-Drop example**The user would like to change the position or location of a given item. There are multiple patterns offered to achieve this. The user might choose this in a classical way by selecting the item and then using a dedicated action to move it. However, a drag-&-drop feature provides an intuitive way to grab the item and just drag it to its new location, which requires less steps to be performed. In order to enable this feature, multiple UI components must work together. For example, once the item has been grabbed out of its position, the item list must reflect that the item has been removed. The mouse cursor has to visualize that its actually holding onto the item while the user keeps the left mouse button pressed / their  finger down on the touchscreen. As a consequence / What ultimately constitutes the pattern is not a single UI element but the reciprocal interaction between a multitude of them. You probably get the point.

In summary, interaction patterns are a means to provide designers with systematic, standardized, and well-tried solutions. A UX-pattern is like a recipe that, when followed strictly, will give your users recognizable and reproducible experience. In contrast to that, 'UI-patterns' are constrained to the ability and behavior of a single UI element (e.g. a radio-button).

*If you would like to further follow up on the differentiation of concepts in interface design, I s...