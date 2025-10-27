---
title: SAP Note 3251797 – Only Destinations with one of the following proxy types are currently supported: Internet – S/4 HANA On Premise
url: https://blogs.sap.com/2022/12/30/sap-note-3251797-only-destinations-with-one-of-the-following-proxy-types-are-currently-supported-internet-s-4-hana-on-premise/
source: SAP Blogs
date: 2022-12-31
fetch_date: 2025-10-04T02:47:41.124994
---

# SAP Note 3251797 – Only Destinations with one of the following proxy types are currently supported: Internet – S/4 HANA On Premise

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Note 3251797 - Only Destinations with one of t...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161435&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Note 3251797 - Only Destinations with one of the following proxy types are currently supported: Internet - S/4 HANA On Premise](/t5/technology-blog-posts-by-members/sap-note-3251797-only-destinations-with-one-of-the-following-proxy-types/ba-p/13558396)

![former_member637499](https://avatars.profile.sap.com/former_member_small.jpeg "former_member637499")

[former\_member637499](https://community.sap.com/t5/user/viewprofilepage/user-id/637499)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161435)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161435)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558396)

‎2022 Dec 30
12:45 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161435/tab/all-users "Click here to see who gave kudos to this post.")

4,445

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (3)

**Introduction**

In case of S/4 HANA On premise where connection is secured using VPN, this error generally occurs while running the bot.

As per the SAP Note 3251797 - **Internet Proxy Type does not automatically mean that the invocation goes through the public internet before reaching its target**

\***\*All the images are captured from SAP Trail Account for BTP Cockpit and SAP Process Automation\*\***

**Resolution**

Follow the below steps.

* Make sure your backend S/4 HANA On Premise is configured in Cloud Connector using internal host and is reachable.

* Set the proxy type as Internet in BTP Destination, don't worry if Check Connection is not working.

![](/legacyfs/online/storage/blog_attachments/2022/12/BTP-Destination-4.png)

* Set the Technical User and Password which can access backend S/4 HANA On Premise system in the BTP Destination.

* Maintain the Relevant proxy settings or VPN connectivity under the operating environment of Agent. Enter the same Technical User and Password used in BTP Destination under Configure proxy authentication(advanced).

* Finally restart your agent.

![](/legacyfs/online/storage/blog_attachments/2022/12/Proxy-1.png)

Please share and provide your feedback in the comments.

* [intelligent robotic process automation](/t5/tag/intelligent%20robotic%20process%20automation/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-note-3251797-only-destinations-with-one-of-the-following-proxy-types%2Fba-p%2F13558396%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Resource Injection Failed: Error while pushing files. Cause: Request not supported. CPI error.](/t5/technology-q-a/resource-injection-failed-error-while-pushing-files-cause-request-not/qaq-p/14234547)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  26m ago
* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  43m ago
* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  3 hours ago
* [Deploy Your First SAPUI5 App : CF deployed mtar results in 500 Internal Server Error](/t5/technology-q-a/deploy-your-first-sapui5-app-cf-deployed-mtar-results-in-500-internal/qaq-p/14234214)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  8 hours ago
* [Handling of IT 0004 in PTP Employee Replication](/t5/technology-blog-posts-by-members/handling-of-it-0004-in-ptp-employee-replication/ba-p/14233987)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  11 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") MioYasutake](/t5/user/viewprofilepage/user-id/789) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39...