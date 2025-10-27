---
title: Expose Calculation view as a service via OData in HANA XSA using Web IDE
url: https://blogs.sap.com/2023/01/02/expose-calculation-view-as-a-service-via-odata-in-hana-xsa-using-web-ide/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:55:03.556517
---

# Expose Calculation view as a service via OData in HANA XSA using Web IDE

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Expose Calculation view as a service via OData in ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162009&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Expose Calculation view as a service via OData in HANA XSA using Web IDE](/t5/technology-blog-posts-by-members/expose-calculation-view-as-a-service-via-odata-in-hana-xsa-using-web-ide/ba-p/13560972)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162009)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162009)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560972)

‎2023 Jan 02
3:59 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162009/tab/all-users "Click here to see who gave kudos to this post.")

1,396

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

In this blog I am going to discuss how we can  expose Calculation view as a service via OData in **HANA XSA using Web IDE**. Then  either you can consume it in SAPUI5 or other front end interface applications.

Before that we need to understand the architecture of **HANA XSA**  which is given below -

![](/legacyfs/online/storage/blog_attachments/2023/01/Architecture.png)

When HDI service deployed creates HDI Container . We will create tables and on top of it Calculation view which will be exposed as a consumer to Node.js.

**Lets go through the steps by step  :**

1. Create a MTA Project. Here PLB\_PROJECT.

2. Create a HDB database module.

![](/legacyfs/online/storage/blog_attachments/2023/01/CV0.png)

3. Upload a CSV file to the SRC folder of the HDB module (example: db\_plb)  creating a .hdbtabledata DB artifacts. you can create a separate folder. the file formats are given below -

A. Table format example inside /src/ EMPLOYEE.hdbtable :

```
COLUMN TABLE "PLB_PPROJECT.DB_PLB::EMPLOYEE" (

   "EMP_ID" INTEGER                COMMENT 'Employee ID',

   "EMP_NAME" NVARCHAR(256)        COMMENT 'Employee Name',

   "EMAIL_ID" NVARCHAR(256)        COMMENT 'Employee Email id',

   "ADDRESS" NVARCHAR(200)         COMMENT 'Employee Address',

   PRIMARY KEY ("EMP_ID")

)
```

B. CSV file Example :

![](/legacyfs/online/storage/blog_attachments/2023/01/EMPLOYEE12.png)

C. **.hdbtabledata** file table example -

```
{

  "format_version": 1,

  "imports": [{

		"target_table" : "PLB_PPROJECT.DB_PLB::EMPLOYEE",

		"source_data": {

       				"data_type" : "CSV",

       				"file_name" : ""PLB_PPROJECT.DB_PLB::EMPLOYEE.CSV",

       				"has_header" : true,

       				"no_data_import": false,

       				"delete_existing_foreign_data": false,

       				"dialect"   : "HANA",

       				"type_config" : {

          					"delimiter" : ","

        					}

      				},

		"import_settings" : {

				        "import_columns" : [

           				"EMP_ID",

           				"EMP_NAME",

           				"EMAIL_ID",

           				"ADDRESS",

        				],

       					 "include_filter" : [          ]

         			    } ,

    		"column_mappings" : {

        				"EMP_ID" : 1, "EMP_NAME" : 1, "EMAIL_ID" : 1, "ADDRESS" : 1

				    }

	     }]

}
```

C. Build the HDB module. Data will be loaded to the table EMPLOYEE.

D. Create a calculation view on the table Employee. Named as CV\_EMPLOYEE

![](/legacyfs/online/storage/blog_attachments/2023/01/joinpane-1.png)

4. Create a Node.js module.

5. In MTA.YML file add the DB module db\_plb as the Node.js dependency (using key and service you defined in DB module.

![](/legacyfs/online/storage/blog_attachments/2023/01/db_plb.png)

6. Create a **project.xsodata** file project. OData and consume the calculation view CV\_EMPLOYEE as service. The example code is given below -

```
Service{

"PLB_PROJECT.DB_PLB::CV_EMPLOYEE " AS "EMPLOYEE" Key ("EMP_ID")

}
```

7. Build the MTA project.

8.  Run plbnode as a Node.js Application.

9. Do copy the URL of the node.js service  which will appear below portion of the deployment.

10. Open a Browser and paste the URL from the ODATA file build (or click on the link ). Add you you Jason file at  the URL end -

<http://hcpur10.hcs.cloud.sap:8000/xsodata/project.xsodata/employee?$format=json>.

11. To see the metadata execute <http://hcpur10.hcs.cloud.sap:8000/> /xsodata/project.xsodata/employee/$metadata.

Note : No security is implemented .

12. The employee data will be available as JSON data with nodes.

Hope this will help.

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fexpose-calculation-view-as-a-service-via-odata-in-hana-xsa-using-web-ide%2Fba-p%2F13560972%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  6 hours ago
* [RAP Using Custom Entity with load multiple data using Pagination and Preview using UI annotations](/t5/technology-q-a/rap-using-custom-entity-with-load-multiple-data-using-pagination-and/qaq-p/14233901)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  15 hours ago
* [Q3 2025 Quarterly Release Highlights: SAP BTP Security and Identity & Access Management](/t5/technology-blog-posts-by-sap/q3-2025-quarterly-release-highlights-sap-btp-security-and-identity-amp/ba-p/14231563)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [From REST to Datasphere: A CAP-based Integration Approach](/t5/technology-blog-posts-by-members/from-rest-to-datasphere-a-cap-based-integration-approach/ba-p/14218922)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Vibe Coding with MCP Servers & SAP AI Core: Toward "Coding by Conversation"](/t5/technology-q-a/vibe-coding-with-mcp-servers-amp-sap-ai-core-toward-quot-coding-by/qaq-p/14230581)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47D...