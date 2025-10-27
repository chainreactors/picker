---
title: Displaying the single/ multiple Customized Header Messages at HTTP Response under Success Status using OData service
url: https://blogs.sap.com/2022/10/20/displaying-the-single-multiple-customized-header-messages-at-http-response-under-success-status-using-odata-service/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:12.512343
---

# Displaying the single/ multiple Customized Header Messages at HTTP Response under Success Status using OData service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Displaying the single/ multiple Customized Header ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160222&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Displaying the single/ multiple Customized Header Messages at HTTP Response under Success Status using OData service](/t5/technology-blog-posts-by-members/displaying-the-single-multiple-customized-header-messages-at-http-response/ba-p/13551135)

![sreeramg](https://avatars.profile.sap.com/e/a/idea198a3e06b8dab3857a5073b6071e1537dbf390d191381f59e30f6b4595c90c_small.jpeg "sreeramg")

[sreeramg](https://community.sap.com/t5/user/viewprofilepage/user-id/391441)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160222)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160222)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551135)

‎2022 Oct 20
9:03 PM

0
Kudos

2,968

* SAP Managed Tags
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP Gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Gateway/pd-p/01200615320800003185)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)

* [SAP Gateway

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BGateway/pd-p/01200615320800003185)
* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)

View products (3)

Hi All,

Actually all of you knows the Error handling Messages in OData

But I am going to show you the **Header messages** at the success **Status-200**.

Some one knows this in other way but max number of developers don't know this scenario

I am going to tell you the simple way to display the Customized Header

messages at the **HTTP Response.**

Follow the below steps to create project as usual :

1. Go to T-code **SEGW**.

2. Create the **project** and give properties.

3. Create the get entity and **get entity set**.

4. Give the properties and **Generate** Service

5. **Redefine** the Get entity set method.

6. Write the **logic**.

![](/legacyfs/online/storage/blog_attachments/2022/10/HM3.png)

**Code:**

METHOD purchaseset\_get\_entityset.

\*\*\*Extracting the data

SELECT \* FROM ekko INTO TABLE et\_entityset  UP TO 1 ROWS.

IF et\_entity set IS NOT INITIAL.

\*\*Display the header message

DATA : ls\_message TYPE **ihttpnvp** ,

lt\_message TYPE TABLE OF **ihttpnvp** .

ls\_message-name = 'Message1'.

ls\_message-value = '**SUCCESSFULY UPDATED**'.

\*\* Moving to internal table

APPEND ls\_message TO lt\_message.

CLEAR ls\_message.

\*\* Moving to internal table

ls\_message-name = 'Message2'.

ls\_message-value = '**Sucessfully Updated**'.

APPEND ls\_message TO lt\_message.

\*\*For display header message

LOOP AT lt\_message INTO ls\_message.

**/iwbep/if\_mgw\_conv\_srv\_runtime~set\_header( ls\_message ).**

CLEAR ls\_message.

ENDLOOP.

ENDIF.

**OUT PUT :**

In this scenario I have given 2 messages with Capital and small letters and will be

displayed as Message1 and Message2.

After executing the scenario the messages will be displayed at the **Success header**

level **status 200** at the  **HTTP Response**.

![](/legacyfs/online/storage/blog_attachments/2022/10/Header_messages2.png)

Thank you.

Some Important Articles :

<https://blogs.sap.com/2021/06/10/calling-the-submit-report-program-through-the-odata-service/>

<https://blogs.sap.com/2019/05/17/display-the-bsp-application-without-asking-the-login-page/>

[https://blogs.sap.com/2017/12/06/display-countfilterorderbyinlinecounttop-and-skip-operations-using-...](https://blogs.sap.com/2017/12/06/display-countfilterorderbyinlinecounttop-and-skip-operations-using-odata-services/)

* [Header Messages](/t5/tag/Header%20Messages/tg-p/board-id/technology-blog-members)
* [Net weaver gateway](/t5/tag/Net%20weaver%20gateway/tg-p/board-id/technology-blog-members)
* [netweaver](/t5/tag/netweaver/tg-p/board-id/technology-blog-members)
* [OData](/t5/tag/OData/tg-p/board-id/technology-blog-members)
* [SAP](/t5/tag/SAP/tg-p/board-id/technology-blog-members)
* [sap erp human capital management](/t5/tag/sap%20erp%20human%20capital%20management/tg-p/board-id/technology-blog-members)
* [Success header message](/t5/tag/Success%20header%20message/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fdisplaying-the-single-multiple-customized-header-messages-at-http-response%2Fba-p%2F13551135%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Building Custom LLM Agent in Databricks: An Example Generating AI Responses from Customer Review](/t5/technology-blog-posts-by-members/building-custom-llm-agent-in-databricks-an-example-generating-ai-responses/ba-p/14223274)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [How to display custom MIGO fields in Stock – Multiple Materials app (S/4HANA Public Cloud)](/t5/technology-q-a/how-to-display-custom-migo-fields-in-stock-multiple-materials-app-s-4hana/qaq-p/14221952)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2 weeks ago
* [CDS Views: The Key to a "Clean Core" and a More Agile SAP](/t5/technology-blog-posts-by-sap/cds-views-the-key-to-a-quot-clean-core-quot-and-a-more-agile-sap/ba-p/14209118)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a month ago
* [SAP BTP ABAP Environment - Release 2508](/t5/technology-blog-posts-by-sap/sap-btp-abap-environment-release-2508/ba-p/14182635)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Aug 22

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap....