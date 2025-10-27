---
title: Enterprise Planning with AWS data on SAP Data Warehouse Cloud and SAP Analytics Cloud
url: https://blogs.sap.com/2022/11/14/enterprise-planning-with-aws-data-using-with-sap-data-warehouse-cloud-and-sap-analytics-cloud/
source: SAP Blogs
date: 2022-11-15
fetch_date: 2025-10-03T22:45:21.204778
---

# Enterprise Planning with AWS data on SAP Data Warehouse Cloud and SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Enterprise Planning with AWS data on SAP Dataspher...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164362&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enterprise Planning with AWS data on SAP Datasphere and SAP Analytics Cloud](/t5/technology-blog-posts-by-sap/enterprise-planning-with-aws-data-on-sap-datasphere-and-sap-analytics-cloud/ba-p/13569916)

![Sangeetha_K1](https://avatars.profile.sap.com/6/f/id6f85dd6cd7b2ff123451b75b0eb77274da82eb211806e94d4840542964b6c31e_small.jpeg "Sangeetha_K1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Sangeetha\_K1](https://community.sap.com/t5/user/viewprofilepage/user-id/86176)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164362)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164362)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569916)

‎2022 Nov 14
9:13 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164362/tab/all-users "Click here to see who gave kudos to this post.")

6,036

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (2)

This blog is part of technical resource for SAP TechEd session [DT-200 : Amplify the Value of SAP Investments with Joint Reference Architectures](https://go3.events.sap.com/sapteched/hybrid/2022/reg/flow/sap/saptech2022/sapteched2022catalog/page/catalog/session/1662568100211001geGh)

As an operational or financial planner, you want to have access to your distributed data so you can analyse, plan and forecast better. This data might reside in SAP (applications like Analytics cloud and Data warehouse cloud) or non-SAP applications, stored in data lakes such as Amazon S3.

Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. For more details refer to <https://aws.amazon.com/s3/>

Now we will be looking at the architectural pattern(which is part of the SAP and AWS Joint Reference Architectures), that will allow you to have a consolidated view of the distributed data and extend it into SAP Analytics Cloud (SAC) to allow effective enterprise planning.

We will see how to connect and acquire the data from Amazon S3 (shown by arrow 3 in below diagram) and create models in SAP Datasphere. We will use OData APIs to import and create the Planning models in SAC that will be used for the Planning (shown by arrow 4).

![](/legacyfs/online/storage/blog_attachments/2022/11/AWSBlog2_1.jpg)

## **Steps**

1. Create connection in SAP Datawarehouse cloud to Amazon S3 bucket that holds the planning data

2. Create target table in SAP Datawarehouse cloud that will be used to acquire data from Amazon S3

3. Create dataflows to bring the data from Amazon S3 to SAP Datasphere target models

4. Identify the SAP Analytics Cloud tenant that will be used for Planning. Find the redirect URL that will be used for OData API client configuration in SAP Datasphere

5. Create and configure the OData API Client in SAP Datasphere for the SAP Analytics Cloud tenant identified in earlier step

6. In SAP Analytics Cloud, Create OData connection pointing it to the SAP Datasphere model which holds data acquired from Amazon S3

7. Create a Planning model in SAP Analytics Cloud

8. Import data into it using OData API connection created earlier

9. Map and validate the data.

10. Create Planning Story and create planning widgets using the model created

**Step1-3 :** Upload Sales data sample to Amazon S3  bucket and create connection in SAP Datawarehouse cloud to S3 bucket.

[https://blogs.sap.com/2021/02/02/data-integration-between-sap-data-warehouse-cloud-and-amazon-s3-to-...](https://blogs.sap.com/2021/02/02/data-integration-between-sap-data-warehouse-cloud-and-amazon-s3-to-blend-business-data-with-external-data/)

Sample Sales Data that will be stored in Amazon S3  to be used as input for Enterprise Planning.

![](/legacyfs/online/storage/blog_attachments/2022/11/AWSBlog2_2.jpg)

**Step 4-6:**Create OData Client in SAP Datasphere and configure connectivity inSAP Analytics Cloud to read data from the OData API end point.

<https://blogs.sap.com/2022/06/17/using-the-data-warehouse-cloud-odata-api-with-sap-analytics-cloud/>

**Steps 7 – 10 :** Create planning model in SAP Analytics Cloud and import data from SAP Datasphere Odata API.

Now that the connection is successfully established, there are multiple options for acquiring the data into SAP Analytics Cloud:

* Option1: Load data into an existing Planning model

* Option 2: Create a model from scratch via the OData Service connection

[https://blogs.sap.com/2022/06/21/introducing-the-bi-directional-integration-of-sap-data-warehouse-cl...](https://blogs.sap.com/2022/06/21/introducing-the-bi-directional-integration-of-sap-data-warehouse-cloud-and-sap-analytics-cloud-for-planning/)

**SAP Analytics Cloud Planning model:**

![](/legacyfs/online/storage/blog_attachments/2022/11/AWSBlog2_3.jpg)

**SAP Analytics Cloud Planning dashboard:**

![](/legacyfs/online/storage/blog_attachments/2022/11/AWSBlog2_4.jpg)

## **Conclusion**

Through the SAP Datasphere's rich data flows and integration to external data stores such as Amazon S3, , this architectural pattern allows for end to end unified and consolidated view of all your data (no matter where they originate from - SAP or non-SAP applications),  to be used as inputs for the planning models in SAP Analytics cloud. This allows for an effective enterprise planning.

For more information about this topic or to ask a question, please contact us at paa@sap.com

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [data warehouse cloud](/t5/tag/data%20warehouse%20cloud/tg-p/board-id/technology-blog-sap)
* [EnterprisePlanning](/t5/tag/EnterprisePlanning/tg-p/board-id/technology-blog-sap)
* [SAP Analytics Cloud](/t5/tag/SAP%20Analytics%20Cloud/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fenterprise-planning-with-aws-data-on-sap-datasphere-and-sap-analytics-cloud%2Fba-p%2F13569916%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)...