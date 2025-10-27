---
title: Consume SNI based APIs via SAP PO 7.5
url: https://blogs.sap.com/2023/07/31/consume-sni-based-apis-via-sap-po-7.5/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T17:00:08.843376
---

# Consume SNI based APIs via SAP PO 7.5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Consume SNI based APIs via SAP PO 7.5

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164025&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Consume SNI based APIs via SAP PO 7.5](/t5/technology-blog-posts-by-members/consume-sni-based-apis-via-sap-po-7-5/ba-p/13573028)

![phanikumar_akella](https://avatars.profile.sap.com/a/d/idad69fc1e304a63c38a3f8301ca0f46ce71bda9c468b0ca71288301adcf7b753d_small.jpeg "phanikumar_akella")

[phanikumar\_akella](https://community.sap.com/t5/user/viewprofilepage/user-id/187382)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164025)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164025)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13573028)

‎2023 Jul 31
7:49 PM

0
Kudos

1,628

* SAP Managed Tags
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (1)

We have been trying to integrate SAP ECC with one of the third parties REST API via SAP PO 7.5 (dual usage type). It’s Proxy to REST (Synch) scenario. API endpoint and Security key updated in the receiver SAP PO REST Communication channel. All the certificates (chain) deployed in SAP PO NWA Key Storage.

Integration flow:

![](/legacyfs/online/storage/blog_attachments/2023/07/Capture1-2.png)

While testing, we have encountered SSL based issues -  “SSLException while handshaking: Peer sent alert: Alert Fatal: unrecognized name”.

SAP PO Logs

![](/legacyfs/online/storage/blog_attachments/2023/07/Capture-35.png)

We have used XPI Inspector to analyse the SSL errors and identified below issues:
> Using Transport Protocol: HTTPS
> Handshake Timeout: 0
> Keep alive: false
> TCP No Delay: false
> Exception Occured: Peer sent alert: Alert Fatal: unrecognized name
>
> Begin IAIK Debug:
> ssl\_debug(49386): Starting handshake (iSaSiLk 5.2)...
> ssl\_debug(49386): Sending v3 client\_hello message to api.qua.txxxs.com:8xx3, requesting version 3.3...
> ssl\_debug(49386): Sending extensions: renegotiation\_info (65281), signature\_algorithms (13)
> ssl\_debug(49386): Received alert message: Alert Fatal: unrecognized name
> ssl\_debug(49386): SSLException while handshaking: Peer sent alert: Alert Fatal: unrecognized name
> ssl\_debug(49386): Shutting down SSL layer...
> ssl\_debug(49386): Closing transport...
>
> End IAIK Debug.

We have used Qualy's SSL Labs free online service (<https://www.ssllabs.com/ssltest/analyze.html?d=api.txxxs.com>) to performs a deep analysis of the configuration of api.txxxs.com SSL web server on the public Internet. As per the report, we have identified api.txxxs.com API requires SNI (Server Name Indication) support from any HTTP clients connecting to it.

By default, SNI extension is disabled in SAP PO. Connectivity issue between SAP PO and SNI based third party API got resolved post applying below OSS notes recommended by SAP:

2492386 - SSLException: Peer sent alert: Alert Fatal: unrecognized name

2604240 - TLS handshake failure due to missing SNI extension

<https://me.sap.com/notes/0002604240>

2569156 - How to create, modify and validate SSLContext.properties file

<https://me.sap.com/notes/0002569156>

<https://ga.support.sap.com/dtp/viewer/index.html#/tree/1809/actions/23446>

Learn more about SNI:

<https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/>

* [restapi](/t5/tag/restapi/tg-p/board-id/technology-blog-members)
* [sap po](/t5/tag/sap%20po/tg-p/board-id/technology-blog-members)
* [sni](/t5/tag/sni/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fconsume-sni-based-apis-via-sap-po-7-5%2Fba-p%2F13573028%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Custom Agentic Chatbot with SAP AI Core and Joule Studio — Part 1](/t5/technology-blog-posts-by-sap/custom-agentic-chatbot-with-sap-ai-core-and-joule-studio-part-1/ba-p/14232347)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  7 hours ago
* [SAP GUI Automation within SAP BPA Workflow Process](/t5/technology-q-a/sap-gui-automation-within-sap-bpa-workflow-process/qaq-p/14234302)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Friday
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ramjee_korada](https://avatars.profile.sap.com/a/6/ida68feb06dad0280b54c7e92a0996c1389c5cbe26af62aeffa035d47c94865194_small.jpeg "Ramjee_korada")  Ramjee\_korada](/t5/user/viewprofilepage/user-id/10276) | 8 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 7 |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 5 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d5907...