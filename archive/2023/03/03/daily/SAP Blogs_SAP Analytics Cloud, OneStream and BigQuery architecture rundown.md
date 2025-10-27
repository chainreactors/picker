---
title: SAP Analytics Cloud, OneStream and BigQuery architecture rundown
url: https://blogs.sap.com/2023/03/02/sap-analytics-cloud-onestream-and-bigquery-architecture-rundown/
source: SAP Blogs
date: 2023-03-03
fetch_date: 2025-10-04T08:31:55.126172
---

# SAP Analytics Cloud, OneStream and BigQuery architecture rundown

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Analytics Cloud, OneStream and BigQuery archit...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161753&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Analytics Cloud, OneStream and BigQuery architecture rundown](/t5/technology-blog-posts-by-members/sap-analytics-cloud-onestream-and-bigquery-architecture-rundown/ba-p/13559804)

![Filippo_Naggi](https://avatars.profile.sap.com/d/e/idde2985b6cc6d6f74c391d1d9f425fd2f82ac557149927601ea79bca45698466b_small.jpeg "Filippo_Naggi")

[Filippo\_Naggi](https://community.sap.com/t5/user/viewprofilepage/user-id/159164)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161753)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161753)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559804)

‎2023 Mar 02
10:43 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161753/tab/all-users "Click here to see who gave kudos to this post.")

2,247

* SAP Managed Tags
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Cloud, data modeling](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520data%2520modeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)
* [SAP S/4HANA Embedded Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Embedded%2520Analytics/pd-p/8492b555-b489-4972-8e37-83f2f27ae399)

* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)
* [SAP S/4HANA Embedded Analytics

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BEmbedded%2BAnalytics/pd-p/8492b555-b489-4972-8e37-83f2f27ae399)
* [SAP Analytics Cloud, data modeling

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bdata%2Bmodeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

View products (3)

Hello SAC, OneStream, and Google BigQuery curious,

in this blog we are going to run down the architecture of today's big planning and analytics market players: SAP Analytics Cloud, OneStream, and Google BigQuery.

This is Filippo, I am working for more than 15 years in the Financial Planning and Analytics universe, both with Functional-Business, Developer, and Application hats.

I would like to share with you the main architecture design for SAP Analytics Cloud, OneStream, and Google BigQuery.

Let's start with **SAP Analytics Cloud**:

SAC is running as an application on HANA 2.0.x tenants, on hyper scalers.

It can be either deployed as public  (sharing underlying HANA tenant) or private: in this last case, SAC will have a whole HANA system for itself.

![](/legacyfs/online/storage/blog_attachments/2023/03/loio91240423526740ed8ba0e2be67f4505e_LowRes.png)

Fig 1. From [help.sap.com](https://help.sap.com/docs/SAP_HANA_PLATFORM/78209c1d3a9b41cd8624338e42a12bf6/b9489b57634f41afbea1a81c9316ef11.html), link in Bibliography

HANA lives on VMs on any chosen hyper-scaler, SAC lives on HANA

SAC doesn’t call any hyper-scaler services as it resides on a HANA tenant.

Now let's look into the **OneStream** architecture:

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture.jpg)

Fig 2. From <https://femsadev.onestreamcloud.com/>, link in Bibliography

this is a classic architecture, with OneStream XF Framework helping the Application Server to fulfill all the requests.

Going to the application level details, we can see:

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture-1.jpg)

Fig 3. From <https://femsadev.onestreamcloud.com/>, link in Bibliography

Here, the Web Server Set calls different General Access and Queue Requests.

At the far end of the stack, SQL server instances are used both for Framework and Application.

Finally, this is the **Google BigQuery** Architecture:

![https://storage.googleapis.com/gweb-cloudblog-publish/images/BQ_Explained_2.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/BQ_Explained_2.max-900x900.jpg)

Fig 4. From <https://cloud.google.com>, link in Bibliography

BigQuery is leveraging BORG (the Google Orchestrator):

![https://storage.googleapis.com/gweb-cloudblog-publish/images/BQ_Explained_3.max-500x500.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/BQ_Explained_3.max-500x500.jpg)

Fig 5. From <https://cloud.google.com>, link in Bibliography

This is a Cloud Native Architecture, with Storage and Compute functions decoupled from servers.

Hope this architecture rundown has been useful for your business.

If you liked the article, please like and share it, and do not forget to add me to your LinkedIn profile.

<https://www.linkedin.com/in/filippo-naggi/>

See you soon on blog.sap.com

Filippo

## **Bibliography**

**SAP Analytics Cloud**

[https://help.sap.com/docs/SAP\_HANA\_PLATFORM/78209c1d3a9b41cd8624338e42a12bf6/b9489b57634f41afbea1a81...](https://help.sap.com/docs/SAP_HANA_PLATFORM/78209c1d3a9b41cd8624338e42a12bf6/b9489b57634f41afbea1a81c9316ef11.html)

**One Stream**

[https://femsadev.onestreamcloud.com/OneStreamWeb/Help/Content/PDFs/System%20Requirements%20and%20Arc...](https://femsadev.onestreamcloud.com/OneStreamWeb/Help/Content/PDFs/System%20Requirements%20and%20Architecture%20Guide.pdf)

**BigQuery**

<https://cloud.google.com/blog/products/data-analytics/new-blog-series-bigquery-explained-overview>

* [Architecture](/t5/tag/Architecture/tg-p/board-id/technology-blog-members)
* [Cloud](/t5/tag/Cloud/tg-p/board-id/technology-blog-members)
* [google bigquery](/t5/tag/google%20bigquery/tg-p/board-id/technology-blog-members)
* [onestream](/t5/tag/onestream/tg-p/board-id/technology-blog-members)
* [Planning](/t5/tag/Planning/tg-p/board-id/technology-blog-members)
* [SAP](/t5/tag/SAP/tg-p/board-id/technology-blog-members)
* [SQL](/t5/tag/SQL/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-analytics-cloud-onestream-and-bigquery-architecture-rundown%2Fba-p%2F13559804%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Driving AI Adoption with BTP: Highlights](/t5/technology-blog-posts-by-sap/driving-ai-adoption-with-btp-highlights/ba-p/14233554)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/techn...