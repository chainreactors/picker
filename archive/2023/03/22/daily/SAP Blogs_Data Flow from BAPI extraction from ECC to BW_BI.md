---
title: Data Flow from BAPI extraction from ECC to BW/BI
url: https://blogs.sap.com/2023/03/21/data-flow-from-bapi-extraction-from-ecc-to-bw-bi/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:14:55.048058
---

# Data Flow from BAPI extraction from ECC to BW/BI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Data Flow from BAPI extraction from ECC to BW/BI

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160716&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data Flow from BAPI extraction from ECC to BW/BI](/t5/technology-blog-posts-by-members/data-flow-from-bapi-extraction-from-ecc-to-bw-bi/ba-p/13554098)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160716)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160716)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554098)

‎2023 Mar 21
10:17 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160716/tab/all-users "Click here to see who gave kudos to this post.")

2,121

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)

View products (2)

Today I will discuss about a scenario where I try to extract data from a **BAPI** extractor named **BAPI\_IM\_HERE** from **ECC**.

if you put the **BAPI** FM as a source of a generic data extractor you will get the error of **E\_T\_DATA** table mentioned below -

![](/legacyfs/online/storage/blog_attachments/2023/03/BAPI-Error.png)

**Solution :** You can not take data directly from **BAPI**. write  a functional module and put the BAPI extracted data into a temp table and them create a generic datasource from there. Consume the  datasource in SAP BW and continue BW modeling.

**Steps :**

1.Create a functional module from **SE37** in **ECC** where the **BAPI** exists and put the **BAPI** extracted **DATA** into a temporary table. If you want to do it from scratch it will take time. Better you copy a pre existing method  **RSAX\_BIW\_GET\_DATA** and customized according to you need.

You can give the new function name as **ZFM\_BAPI\_DATA** and also select  a functional Group **ZFM\_BPI** which is available in your landscape.

![](/legacyfs/online/storage/blog_attachments/2023/03/BAPI-COPY.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/COpy.png)

2. after that open the FM and delete all the code and customized your code. But to extract the FM as a genetic data source the table as a E\_T\_DATA   is required. Go to the Table tab and add this two table.

![](/legacyfs/online/storage/blog_attachments/2023/03/TABLEFM-1.png)

**Note :** The association type for **E\_T\_DATA** will be the same structure that return by the **BAPI** **BAPI\_IM\_HERE** when invoking the BAPI from our systems.

**3.** Now in the code section delete all the prepopulated code and start from the beginning.

* Call the BAPI function.

* Loop on the return structure from **BAPI BAPI\_IM\_HERE**.

* append it to **E\_T\_DATA.**

Like the below code you can customize.

```
** Extract BAPI data by invocking it **************************

    CALL FUNCTION 'BAPI_IM_HERE'

      EXPORTING

        system_id     = lf_lsys_id

        posting_date   = lf_postng_dt

      TABLES

          output_data  = lt_data.

** End of BAPI Extraction *************************************
```

```
** Start loop the extrated structure from BAPI****************

LOOP AT lt_data ASSIGNING FIELD-SYMBOL(<fs_data>).

      ls_data-sales_order      = <fs_data>-sales_order.

      ls_data-sales_order     = <fs_data>-order_date.

      ls_data-sales_order      = <fs_data>-quantity.

      APPEND ls_data TO e_t_data.

    ENDLOOP.

*************** End loop *************************************
```

4. use RSO2 and create a data generic source from FM.

![](/legacyfs/online/storage/blog_attachments/2023/03/GDC.png)

Now you do not get any error while activating the data source.

5. After activating go to RSA3 and check the data.

6. Finally replicate the data in SAP BW sid using RSDS.

Hope this will help.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fdata-flow-from-bapi-extraction-from-ecc-to-bw-bi%2Fba-p%2F13554098%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Error while extracting data: DataSource 0CO\_PC\_ACT\_02, package 000000 Message no. RODPS\_SAPI009](/t5/technology-q-a/error-while-extracting-data-datasource-0co-pc-act-02-package-000000-message/qaq-p/14234415)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/sap-iq-to-sap-hana-cloud-data-lake-migration-overview/ba-p/14228663)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [1,500× Faster: ABAP Cloud API with “Just” Gzip](/t5/technology-blog-posts-by-members/1-500-faster-abap-cloud-api-with-just-gzip/ba-p/14229207)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofi...