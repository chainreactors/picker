---
title: Creating Compound Keys in Datasphere
url: https://blogs.sap.com/2023/06/08/creating-compound-keys-in-datasphere/
source: SAP Blogs
date: 2023-06-09
fetch_date: 2025-10-04T11:47:05.840161
---

# Creating Compound Keys in Datasphere

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Creating Compound Keys in Datasphere

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157253&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating Compound Keys in Datasphere](/t5/technology-blog-posts-by-sap/creating-compound-keys-in-datasphere/ba-p/13548925)

![vasilikb](https://avatars.profile.sap.com/2/3/id23f2669d9d045fc8af6ebed4a999d9c55c8dd6c7eca7316a4ce2cfc6681ce505_small.jpeg "vasilikb")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[vasilikb](https://community.sap.com/t5/user/viewprofilepage/user-id/141665)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157253)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157253)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548925)

‎2023 Jun 08
3:46 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157253/tab/all-users "Click here to see who gave kudos to this post.")

8,773

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

## Business value

When defining tables in Datasphere, sometimes, one key will not be refined enough to define the uniqueness of records.

The sample data below shows 2 columns that are keys

* Controlling area

* Cost Center

![](/legacyfs/online/storage/blog_attachments/2023/05/Sample.png)

Sample Dataset

## How to apply compound keys

Modelers will first need to create an entity of one of the below semantic usages selected:

* Dimension

* Text

* External Hierarchy

This can be defined at the local table level or a view level.

In addition, another view of transactional data will be required to complete the model.

This example highlights creation of a compound key for the below flow from the dimension to the Analytic Model preview.

![](/legacyfs/online/storage/blog_attachments/2023/05/Dataflow.png)

To implement the compound key, 4 steps are required.

* Step 1: Create a dimension and ensure it has key values

* Step 2: Define key order and representative key

* Step 3: Create a model and associate the dimension to the model

* Step 4: Build analytic model for consumption

### Step 1: Ensure the dimension has key values

In the local table, define the primary keys (this can also be done at a view level)

![](/legacyfs/online/storage/blog_attachments/2023/05/Cost-Center-Dimension-3.png)

### Step 2: Define key order and representative key

The compound key will be defined at this step. It is important to take two considerations while completing these steps

* Define a representative key that holds the most granular level of data

* Order the key columns in the appropriate manner if there is more than 2 keys

![](/legacyfs/online/storage/blog_attachments/2023/05/Key-and-Rep-2.png)

### Step 3: Create a model and associate the dimension to the model

Define an analytical dataset and create an association to the CostCenters dimension.

![](/legacyfs/online/storage/blog_attachments/2023/05/Analytical-Dataset.png)

### Step 4: Build analytic model for consumption

We can now create an analytic model by dragging in the analytical dataset with the associated dimension and view the result of the compound key in the result set.

![](/legacyfs/online/storage/blog_attachments/2023/05/Analytic-Model.png)

## Summary

Now should be able to view compound keys in our Analytic Models, SAC stories and SAC Add-in for Microsoft Office.

Please like, comment or post a question!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fcreating-compound-keys-in-datasphere%2Fba-p%2F13548925%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [How to create/export a CSV file from Datasphere?](/t5/technology-q-a/how-to-create-export-a-csv-file-from-datasphere/qaq-p/14230939)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday
* [NDC Converter 2.0: Automating Your Journey from BusinessObjects to Cloud Analytics](/t5/technology-q-a/ndc-converter-2-0-automating-your-journey-from-businessobjects-to-cloud/qaq-p/14226676)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  a week ago
* [SAP Datasphere Integration with SAP S/4HANA: SAP Cloud Connector Setup Guide](/t5/technology-blog-posts-by-sap/sap-datasphere-integration-with-sap-s-4hana-sap-cloud-connector-setup-guide/ba-p/14224459)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [SAP Business Data Cloud - From Provisioning to Intelligent Applications](/t5/technology-blog-posts-by-sap/sap-business-data-cloud-from-provisioning-to-intelligent-applications/ba-p/14224669)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457dbe84b4_small.jpeg "FranciscoHurtado")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") FranciscoHurtado](/t5/user/viewprofilepage/user-id/170459) | 10 |
| [![marc_steinert](https://avatars.profile.sap.com/e/8/ide87ef5876c7e6b7e3cd441b0a163b602ce92b8fde548577e3274e0845485f23b_small.jpeg "marc_steinert")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") marc\_steinert](/t5/user/viewprofilepage/user-id/892436) | ...