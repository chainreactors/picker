---
title: ODATA Adapter – Delta Job are taking long time to complete
url: https://blogs.sap.com/2022/12/14/odata-adapter-delta-job-are-taking-long-time-to-complete/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:05.352177
---

# ODATA Adapter – Delta Job are taking long time to complete

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ODATA Adapter - Delta Job are taking long time to ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160042&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ODATA Adapter - Delta Job are taking long time to complete](/t5/technology-blog-posts-by-members/odata-adapter-delta-job-are-taking-long-time-to-complete/ba-p/13549955)

![arun231](https://avatars.profile.sap.com/2/1/id2138714a9405ea33250f5ec342fbdf761a19f998bda300c7bd9ed8661021382a_small.jpeg "arun231")

[arun231](https://community.sap.com/t5/user/viewprofilepage/user-id/403367)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160042)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160042)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549955)

‎2022 Dec 14
10:57 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160042/tab/all-users "Click here to see who gave kudos to this post.")

1,002

* SAP Managed Tags
* [SAP Data Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Services/pd-p/01200314690800000395)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)

* [SAP Data Services

  SAP Data Services](/t5/c-khhcw49343/SAP%2BData%2BServices/pd-p/01200314690800000395)
* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)

View products (2)

**Issue –** The BODS job it was taking only 30 mins to complete by the time when it was go- live, and it is daily job with delta load filter condition. Later on this jobs completion was increasing by 3 mins every day and it reached to 5hrs 33 mins. Basis team raised a concern that this job is occupying job server for 5hrs, and this might crash the job server.

**Analyzing issue and fix -**

Our BODS source connects to SAP Cloud Platform via ODATA Adapter datastore connection. So reached out to Source Team (ABAP Team) to check on the CDS view whether it is taking long time to extract the data at source end itself. But ABAP Team confirmed that it is direct view, but this table huge records, everyday data will be appended to this source table.

Then later we started looking on the BODS side, job delta extraction was not pushed down to DB level, and it is taking entire huge records from Source to BODS layer then applying the delta logic and also due to the increase in the source every day, there is increase in job execution.

Before Optimization -

![](/legacyfs/online/storage/blog_attachments/2022/12/Untitled.jpg)

Why was it not push down?

The ODATA Adapter use API Link to connect with SAP Cloud. The date format which is passed on to the delta filter condition is “YYYYMMDD”. The date format which is passed is not in the expected format of API, so BODS couldn’t push down to DB level.

Solution -

To Push down the delta extraction to DB level we need to change it to below “YYYY/MM/DDTHH:MI:SS”. After changing the date format job completion time has reduced to more than 100%. Now job completing less than 12 mins.

![](/legacyfs/online/storage/blog_attachments/2022/12/Untitled1.jpg)

*This is the working solution, Which I have implemented in my development. Thanks for reading my blog !!!*

*I will be covering more interesting topics, solution which have implemented and experienced in upcoming blogs. Please do provide your feedback which will help me in improving my inputs.*

*Do follow my blogs to know more on data migration and integration topics.*

**Thanks for your time!!!**

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fodata-adapter-delta-job-are-taking-long-time-to-complete%2Fba-p%2F13549955%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate SAP S/4HANA Guide: From Master Data to End-to-End Processes](/t5/technology-blog-posts-by-members/the-ultimate-sap-s-4hana-guide-from-master-data-to-end-to-end-processes/ba-p/14228226)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Event enabling SAP Data Replication Framework with Advanced Event Mesh & RAP Business Events](/t5/technology-blog-posts-by-sap/event-enabling-sap-data-replication-framework-with-advanced-event-mesh-amp/ba-p/14224298)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [A Comprehensive Guide to SAP S/4HANA Material Ledger & Integrated Logistics](/t5/technology-blog-posts-by-members/a-comprehensive-guide-to-sap-s-4hana-material-ledger-amp-integrated/ba-p/14224569)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Understanding the Distinct Scope of SAP Cloud ERP Private](/t5/technology-blog-posts-by-sap/understanding-the-distinct-scope-of-sap-cloud-erp-private/ba-p/14219721)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id575...