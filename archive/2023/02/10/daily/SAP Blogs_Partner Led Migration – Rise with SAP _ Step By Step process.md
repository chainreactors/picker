---
title: Partner Led Migration – Rise with SAP : Step By Step process
url: https://blogs.sap.com/2023/02/09/partner-led-migration-rise-with-sap-step-by-step-process/
source: SAP Blogs
date: 2023-02-10
fetch_date: 2025-10-04T06:13:59.994837
---

# Partner Led Migration – Rise with SAP : Step By Step process

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Additional Blog Posts by Members](/t5/additional-blog-posts-by-members/bg-p/additional-blog-members)
* Partner Led Migration – Rise with SAP : Step By St...

Additional Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/additional-blog-members/article-id/63337&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Partner Led Migration – Rise with SAP : Step By Step process](/t5/additional-blog-posts-by-members/partner-led-migration-rise-with-sap-step-by-step-process/ba-p/13562147)

![rkumar_47](https://avatars.profile.sap.com/4/8/id48f35610756242275cbe07d9579b7fa7ad8ab6dcc993547d859a3cfcd8cb0549_small.jpeg "rkumar_47")

[rkumar\_47](https://community.sap.com/t5/user/viewprofilepage/user-id/44541)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=additional-blog-members&message.id=63337)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/additional-blog-members/article-id/63337)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562147)

‎2023 Feb 09
10:25 PM

[15
Kudos](/t5/kudos/messagepage/board-id/additional-blog-members/message-id/63337/tab/all-users "Click here to see who gave kudos to this post.")

22,242

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

View products (1)

Lot of SAP users are planning to move their SAP instances into Rise with SAP offering. The client who want to move there existing S/4HANA system under Rise my blog will help them to plan their activity in more organized way.

As you all know, RISE with SAP is offers One SAP contract covering all components, in addition to secondary contracts with Partners for services or add-on packages if applicable.

RISE with SAP is not a product. RISE with SAP offering is centred around SAP S/4HANA and this package aims to accelerate, streamline, and motivate organisations with their journey to a cloud centric intelligent enterprise.

Following figure describes how S/4HANA services are managed:

**SAP S/4HANA : On-Premise vs Rise with SAP**

![](/legacyfs/online/storage/blog_attachments/2023/02/Partner-led-Migration-1.jpg)

If the client wants to move it existing S/4HANA system (as-is) into Rise with SAP environment, SAP has given a five step Brownfield approach which uses the System copy – Backup/Restore method using the migration server. Following are the steps

Step 1: Take the backup of existing S/4HANA system.

Step 2: Move the backup to Object Storage provided by SAP

Step 3: SAP team will move the backup from Object Storage to Storage attached to the HANA Database of the S/4HANA server.

Step 4: Run the SWPM on Migration Server.

Step 5: Restore the backup on the S/4HANA system hosted into Rise with SAP environment.

Since **SAP has regulations in place and they do not provide OS/root access on SAP Cloud deployed application and database servers.**

Instead of, SAP provided additional VM with full OS/root access and they call it as Migration server. The VM have 128GB RAM, 32vCPUs and 100GB storage which /sapmnt of 20GB and /usr/sap of 80GB.

Steps to provision copy of client system into Rise which is also called as Partner Led Migration

![](/legacyfs/online/storage/blog_attachments/2023/02/Partner-led-Migration-3.jpg)

Following details are require from client to start the migration:

* Hostname of the migration server, database server

* DB ports to be opened so that it can be accessed from migration server

* Location of Backup files and backup prefix

* SID and instance number of the database

* Passwords for SYSTEMDB/SYSTEM user, sidadm, Tenant DB/SYSTEM user

* S-user ID for software download on migration server

Once the migration is complete, partner will shutdown the application running on the migration server and will provide password of DDIC in 000, 100, 200, 300, TenantDB / SYSTEM, Schema user password which came with the backup.

Kindly provide feedback about my blog and also if I have missed any thing do let me know.

* [@S4HANA](/t5/tag/%40S4HANA/tg-p/board-id/additional-blog-members)
* [Brownfield Migration](/t5/tag/Brownfield%20Migration/tg-p/board-id/additional-blog-members)

3 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  7 hours ago
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  9 hours ago
* [Supplier Return process not working](/t5/technology-q-a/supplier-return-process-not-working/qaq-p/14234317)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  9 hours ago
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9 hours ago
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  10 hours ago