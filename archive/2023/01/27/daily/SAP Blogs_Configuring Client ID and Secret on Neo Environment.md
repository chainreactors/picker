---
title: Configuring Client ID and Secret on Neo Environment
url: https://blogs.sap.com/2023/01/26/configuring-client-id-and-secret-on-neo-environment/
source: SAP Blogs
date: 2023-01-27
fetch_date: 2025-10-04T04:58:12.847278
---

# Configuring Client ID and Secret on Neo Environment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Configuring Client ID and Secret on Neo Environmen...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160807&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Configuring Client ID and Secret on Neo Environment](/t5/technology-blog-posts-by-members/configuring-client-id-and-secret-on-neo-environment/ba-p/13554635)

![kc_kristris](https://avatars.profile.sap.com/8/e/id8ef493802989819e8c13ab2d44b92a37b94b4a83d63345b20ba96d051b09f563_small.jpeg "kc_kristris")

[kc\_kristris](https://community.sap.com/t5/user/viewprofilepage/user-id/2139)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160807)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160807)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554635)

‎2023 Jan 26
5:34 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160807/tab/all-users "Click here to see who gave kudos to this post.")

6,213

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [development tools for SAP BTP, Neo environment](https://community.sap.com/t5/c-khhcw49343/development%2520tools%2520for%2520SAP%2520BTP%252C%2520Neo%2520environment/pd-p/67838200100800004383)

* [development tools for SAP BTP, Neo environment

  SAP Business Technology Platform](/t5/c-khhcw49343/development%2Btools%2Bfor%2BSAP%2BBTP%25252C%2BNeo%2Benvironment/pd-p/67838200100800004383)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (2)

**Environment Scope:** Neo

![](/legacyfs/online/storage/blog_attachments/2023/01/1-28.jpg)

**Technical Requirement –** Accessing Cloud Integration (CI) APIs through Client ID and Secret (in Neo). There is slight difference in the way we generate these keys in Cloud Foundry environment.

Following below steps we will see an end-to-end scenario.

* *What will we do here?*

  + *Adding new Client ID & Secret*

  + *Adding user*

  + *Creating dummy HTTPs i-flow in CI*

  + *Testing HTTPs endpoint through POSTMAN*

* **Adding new Client ID & Secret**

 -> Go to -> Security -> OAuth and register new client

![](/legacyfs/online/storage/blog_attachments/2023/01/2-23.jpg)

-> Give a name, select subscription from the dropdown, authorization grant type, set password and validity of token

![](/legacyfs/online/storage/blog_attachments/2023/01/3-20.jpg)

* **Adding user**

-> Follow the below naming convention to add user (client created in above step) and assign *"ESBMessaging"* service to send request

Naming convention to follow for user - oauth\_client\_<client\_name>

![](/legacyfs/online/storage/blog_attachments/2023/01/4-20.jpg)

-> Copy the Token Endpoint to fetch token (this will be used in below step while testing through POSTMAN)

![](/legacyfs/online/storage/blog_attachments/2023/01/4-19.jpg)

* **Create dummy HTTP i-flow in CI**

-> Design i-flow (sample flow to test the connection)

![](/legacyfs/online/storage/blog_attachments/2023/01/6-8.jpg)

-> Set HTTPs endpoint and Body

![](/legacyfs/online/storage/blog_attachments/2023/01/7-6.jpg)

* **Testing HTTPs endpoint through POSTMAN**

-> Fetch token  <https://oauthasservices-<Tenant>.hana.ondemand.com/oauth2/api/v1/token>**?grant\_type=client\_credentials**

-> Select BASIC as Authorization. Pass the secret key generated above.

![](/legacyfs/online/storage/blog_attachments/2023/01/8-7.jpg)

-> Send request to HTTPs endpoint configured above (i-flow).

-> Select Authorization as No Auth

-> Add Header as Authorization (with Value - Bearer <Token generated above>

![](/legacyfs/online/storage/blog_attachments/2023/01/9-10.jpg)

> *We have seen an end-to-end scenario, starting with configuring token (Client ID and Secret) and further, used the same to access CI HTTPs end point.*
>
> *Any question or feedback will be appreciated!*

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fconfiguring-client-id-and-secret-on-neo-environment%2Fba-p%2F13554635%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [From REST to Datasphere: A CAP-based Integration Approach](/t5/technology-blog-posts-by-members/from-rest-to-datasphere-a-cap-based-integration-approach/ba-p/14218922)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Build a Code-based Agent using SAP AI Core with Next.js and the Vercel AI SDK](/t5/technology-blog-posts-by-sap/build-a-code-based-agent-using-sap-ai-core-with-next-js-and-the-vercel-ai/ba-p/14230640)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [Vibe Coding with MCP Servers & SAP AI Core: Toward "Coding by Conversation"](/t5/technology-q-a/vibe-coding-with-mcp-servers-amp-sap-ai-core-toward-quot-coding-by/qaq-p/14230581)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate Guide to SAP S/4HANA Master Data - Part 5](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-part-5/ba-p/14229426)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Friday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db72...