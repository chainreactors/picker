---
title: Automate the Creation of Products in Central Governance by Implementing Derivation Scenarios for Products
url: https://blogs.sap.com/2023/04/21/automate-the-creation-of-products-in-central-governance-by-implementing-derivation-scenarios-for-products/
source: SAP Blogs
date: 2023-04-22
fetch_date: 2025-10-04T11:33:21.995507
---

# Automate the Creation of Products in Central Governance by Implementing Derivation Scenarios for Products

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Automate the Creation of Products in Central Gover...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160346&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automate the Creation of Products in Central Governance by Implementing Derivation Scenarios for Products](/t5/technology-blog-posts-by-sap/automate-the-creation-of-products-in-central-governance-by-implementing/ba-p/13557332)

![Madlin_Gruen](https://avatars.profile.sap.com/2/2/id22c2e20aae62a42e4b5798f778bfc7021071b727ff3588e3f68f3b1520b34e11_small.jpeg "Madlin_Gruen")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[Madlin\_Gruen](https://community.sap.com/t5/user/viewprofilepage/user-id/138013)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160346)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160346)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557332)

‎2023 Apr 21
10:27 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160346/tab/all-users "Click here to see who gave kudos to this post.")

1,904

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Master Data Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Master%2520Data%2520Governance/pd-p/67837800100800004488)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Master Data Governance

  SAP Master Data Governance](/t5/c-khhcw49343/SAP%2BMaster%2BData%2BGovernance/pd-p/67837800100800004488)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

Automation in governing master data is crucial for all master data domains. One such automation technique is the use of derivation rules that you define in a derivation scenario. A derivation scenario is used to deduce master data based on rules and a defined scope to ensure data quality. With derivation rules, you can derive values of single or multiple fields automatically. Instead of manually entering values for each field, the system can automatically populate these fields based on a predefined rule. This will free up time and resources to focus on higher-value tasks.

Did you know that you can define derivation scenarios not only for business partners, but also for products? We’ve recently published a [video](https://sapvideoa35699dc5.hana.ondemand.com/?entry_id=1_tc0rsjzl) showcasing an example in which we use a derivation scenario to derive values in a change request when creating a new material. This approach allows you to fill fields automatically that depend on an entered material group.

![](/legacyfs/online/storage/blog_attachments/2023/04/Define_Derivation_Scenario.png)

In the Condition section of the Define Derivation Scenario for Products app you determine on which field or fields the data to be derived depends, in this case the material group. In the Result Fields table, you can see the fields for which we derive the values. Go to the Implementation section and click the decision table link to add or change rules.

![](/legacyfs/online/storage/blog_attachments/2023/04/New_Material.png)

In the video example, we created a new material in the Manage Material Governance app using the derivation scenario shown in figure 1. Depending on the material group (24111502 paper bags) we’ve entered, related fields were filled in automatically.

Defining Derivation Scenarios for Products could be an important tool for companies looking to automate and improve their efficiency. By using derivation rules, you can save time, reduce risk of errors and improve productivity, helping your company to stay ahead of competition.

Stay up-to-date by following the [SAP Community Topic Page for SAP Master Data Governance](https://community.sap.com/topics/master-data-governance) and joining the [Questions & Answers forum and Blog space](https://community.sap.com/topics/master-data-governance?lng=en&tab=content).

**Learn more about derivation rules:**

* Guide: [Set up Central Governance to Use Derivation Scenarios](https://www.sap.com/documents/2022/11/643c8f3a-4e7e-0010-bca6-c68f7e60039b.html)

* Video: [Change Request Using Derivation Scenario](https://sapvideoa35699dc5.hana.ondemand.com/?entry_id=1_tc0rsjzl)

* Blog Post: [Automate Your Master Data Process With Derivation Scenarios in SAP Master Data Governance on SAP S/4...](https://blogs.sap.com/2022/05/19/automate-your-master-data-process-with-derivation-scenarios-in-sap-master-data-governance-on-sap-s-4hana/)

* Blog Post: [Added Automation in Central Governance](https://blogs.sap.com/2022/11/11/added-automation-in-central-governance/)

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [MDGupdates](/t5/tag/MDGupdates/tg-p/board-id/technology-blog-sap)
* [MDGupdates2023](/t5/tag/MDGupdates2023/tg-p/board-id/technology-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fautomate-the-creation-of-products-in-central-governance-by-implementing%2Fba-p%2F13557332%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Vibe Coding with MCP Servers & SAP AI Core: Toward "Coding by Conversation"](/t5/technology-q-a/vibe-coding-with-mcp-servers-amp-sap-ai-core-toward-quot-coding-by/qaq-p/14230581)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [SAP BTP Guidance Framework: Center of Expertise (CoE), Administration and DevOps](/t5/technology-blog-posts-by-sap/sap-btp-guidance-framework-center-of-expertise-coe-administration-and/ba-p/14224065)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 weeks ago
* [Blueprints for Success: Landscape setup recommendations for SAP Integ...