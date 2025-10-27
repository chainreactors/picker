---
title: Cloud Integration with Slack
url: https://blogs.sap.com/2022/12/31/cloud-integration-with-slack/
source: SAP Blogs
date: 2023-01-01
fetch_date: 2025-10-04T02:50:49.766460
---

# Cloud Integration with Slack

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cloud Integration with Slack

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161961&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Integration with Slack](/t5/technology-blog-posts-by-members/cloud-integration-with-slack/ba-p/13560690)

![PriyankaChak](https://avatars.profile.sap.com/1/7/id17786275abb24ff991937bf35e88f628fdbbf731c31446e00f4dc916962a59c5_small.jpeg "PriyankaChak")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[PriyankaChak](https://community.sap.com/t5/user/viewprofilepage/user-id/3763)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161961)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161961)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560690)

‎2022 Dec 31
3:56 AM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161961/tab/all-users "Click here to see who gave kudos to this post.")

6,803

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

# **Introduction:**

This blog post shows the set up configurations of Slack adapter in Cloud Integration.

# **Implementation Guide:**

## Configuration at Slack:

1. Create an app at <https://api.slack.com>

2. In 'Permissions', add 'Bot Token Scope' as 'chat:write'.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-10.58.00-AM.png)

3. Click on 'Install to Workspace' and then allow. This will generate 'Bot User OAuth Token'.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-10.59.55-AM-1.png)

4. Add the app into the slack channel.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-2.35.16-PM.png)

## Configuration at CPI:

### Step 1:

Go to CPI tenant -> Manage Security Material -> Create -> Secure Parameter. ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-11.16.00-AM.png)

### Step 2:

Design I-Flow as below.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.15.23-PM.png)

1. Use Content modifier to set template for message.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.26.09-PM.png)

2. Use Content modifier to create a property with value as message body.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.27.55-PM.png)

3. Configure slack receiver adapter as below.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.30.50-PM.png)![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.32.04-PM.png)

## Try Out:

As per the above configuration, the iflow will end with error event and that will be handled in exception subprocess. The slack notification will contain the alert message with MPL ID and error reason, as shown below.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-30-at-3.34.30-PM.png)

# Reference Links:

1. [SAP Help Portal](https://help.sap.com/docs/CLOUD_INTEGRATION/987273656c2f47d2aca4e0bfce26c594/7c2ea64f931640afb01c6a9d82abdfa1.html?locale=en-US)

2. [Slack API Method](https://api.slack.com/methods/chat.postMessage)

Thank you for reading this blog post. Please feel free to share your feedback or thoughts in the comments section or ask any questions in the Q&A tag below.

[QA link](https://answers.sap.com/tags/67837800100800006801)

Regards,

Priyanka Chakraborti

* [priyanka chakraborti](/t5/tag/priyanka%20chakraborti/tg-p/board-id/technology-blog-members)
* [slack](/t5/tag/slack/tg-p/board-id/technology-blog-members)
* [Slack Integration](/t5/tag/Slack%20Integration/tg-p/board-id/technology-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcloud-integration-with-slack%2Fba-p%2F13560690%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Resource Injection Failed: Error while pushing files. Cause: Request not supported. CPI error.](/t5/technology-q-a/resource-injection-failed-error-while-pushing-files-cause-request-not/qaq-p/14234547)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  29m ago
* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  46m ago
* [SAP BTP CI CD service for on premise S4 HANA systems RICEFW applications](/t5/technology-q-a/sap-btp-ci-cd-service-for-on-premise-s4-hana-systems-ricefw-applications/qaq-p/14234519)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  an hour ago
* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  3 hours ago
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  6 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/me...