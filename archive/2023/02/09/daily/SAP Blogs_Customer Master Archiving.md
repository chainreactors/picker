---
title: Customer Master Archiving
url: https://blogs.sap.com/2023/02/08/customer-master-archiving/
source: SAP Blogs
date: 2023-02-09
fetch_date: 2025-10-04T06:07:20.781868
---

# Customer Master Archiving

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Customer Master Archiving

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162520&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer Master Archiving](/t5/technology-blog-posts-by-members/customer-master-archiving/ba-p/13564130)

![former_member839951](https://avatars.profile.sap.com/former_member_small.jpeg "former_member839951")

[former\_member839951](https://community.sap.com/t5/user/viewprofilepage/user-id/839951)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162520)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162520)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564130)

‎2023 Feb 08
7:13 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162520/tab/all-users "Click here to see who gave kudos to this post.")

8,380

* SAP Managed Tags
* [SAP NetWeaver Master Data Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Master%2520Data%2520Management/pd-p/01200615320800000588)

* [SAP NetWeaver Master Data Management

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BMaster%2BData%2BManagement/pd-p/01200615320800000588)

View products (1)

The functionality for customer master archiving is used by business/client when the data is no longer used or not in operation. Sometimes archiving is used during de-commissioning of the company code/sales organization or system.

The customer master archiving can be leveraged using standard ECC functionality. It can be leveraged thru standard archiving objects present in the system. No enhancement is required.

**Context:**

Customer master data is stored and archived in three different areas:

* General data

* FI data (for a specific company code)

* SD data (for a specific sales organization)

The term customer master data is used in both the FI and SD components.

To archive master data, you must set the deletion flag in the master record. You can set this flag for a complete customer or for individual company codes and sales organizations.

Archiving object FI\_ACCRECV is used to archive data from different tables. The following table shows the reports available:

|
 **Function** |
 **Report** |

|
 Write |
 FI\_ACCRECV\_WRI |

|
 Delete |
 FI\_ACCRECV\_DEL |

**Settings:**

1. **Below are the steps involved in Write Function for Archiving Customer Master.**

a. Go to T-code SARA![](/legacyfs/online/storage/blog_attachments/2023/02/Image-1-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Image2-1.png)

b. Click on the Write Button and give the Variant name and Select Maintain Button

![](/legacyfs/online/storage/blog_attachments/2023/02/Image3.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Image4-1.png)

c. Give the Customer number and sales org that needs to be deleted. Click on Attributes. Give description and save.

![](/legacyfs/online/storage/blog_attachments/2023/02/Image5.png)

d. Save the Variant and come back to the initial screen. Maintain the Start Date and Spool Parameters. Now Press the execute button and it displays a status message at the bottom “New Archiving Job was Scheduled

![](/legacyfs/online/storage/blog_attachments/2023/02/Image6.png)

**2. Below is the step involves in Delete function for Customer Master Archive**

a. Delete

![](/legacyfs/online/storage/blog_attachments/2023/02/Image7.png)

b. Now press the Delete button. Once you click on it you will be redirected to screen shown below Press the archive selection button and you will get a Pop-up display which shows you the completed write Session. Select the check boxes and click on OK button. Maintain start date and Spool parameters which is the same as the one you maintained for the Write Step

![](/legacyfs/online/storage/blog_attachments/2023/02/Image8.png)

**FAQ**

Can we use same functionality for Archiving Vendor Master data?

The functionality is similar to both customer and Vendor master data archiving. We can use same steps to archive Vendor master but the only difference is report which is used for write and delete function

**Summary**

The concepts described above on Archiving customer master data will help OTC consultants and master data consultant to acquaint themselves with this functionality & build a good foundation.

Do share your thoughts and feedback on the blog.

Please go through the below links for more contents on Master Data:

<https://blogs.sap.com/tags/01200615320800000588/>

<https://answers.sap.com/tags/01200615320800000588>

* [Customer Master Archiving](/t5/tag/Customer%20Master%20Archiving/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcustomer-master-archiving%2Fba-p%2F13564130%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Supplier Return process not working](/t5/technology-q-a/supplier-return-process-not-working/qaq-p/14234317)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  9 hours ago
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9 hours ago
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  10 hours ago
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee...