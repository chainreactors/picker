---
title: Top 5 Reasons to Migrate SAP IQ Systems to SAP HANA Cloud, Data Lake
url: https://blogs.sap.com/2022/11/22/top-5-reasons-to-migrate-sap-iq-systems-to-sap-hana-cloud-data-lake/
source: SAP Blogs
date: 2022-11-23
fetch_date: 2025-10-03T23:29:14.341680
---

# Top 5 Reasons to Migrate SAP IQ Systems to SAP HANA Cloud, Data Lake

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Top 5 Reasons to Migrate SAP IQ Systems to SAP HAN...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160071&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Top 5 Reasons to Migrate SAP IQ Systems to SAP HANA Cloud, Data Lake](/t5/technology-blog-posts-by-sap/top-5-reasons-to-migrate-sap-iq-systems-to-sap-hana-cloud-data-lake/ba-p/13556447)

![RobertWaywell](https://avatars.profile.sap.com/c/5/idc58d100aa7257aec8039ea32c926ea250f55f2fcb11b8c8aa240b8da6823d03a_small.jpeg "RobertWaywell")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[RobertWaywell](https://community.sap.com/t5/user/viewprofilepage/user-id/160099)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160071)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160071)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556447)

‎2022 Nov 22
8:13 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160071/tab/all-users "Click here to see who gave kudos to this post.")

3,957

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP IQ](https://community.sap.com/t5/c-khhcw49343/SAP%2520IQ/pd-p/01200314690800002024)
* [SAP HANA Cloud, data lake](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520data%2520lake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP IQ

  SAP IQ](/t5/c-khhcw49343/SAP%2BIQ/pd-p/01200314690800002024)
* [SAP HANA Cloud, data lake

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2Bdata%2Blake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

View products (3)

It’s pretty well known that SAP HANA Cloud, data lake is built on the foundation of on-premise SAP IQ which makes it the perfect choice if you’re thinking about migrating your existing SAP IQ systems to the cloud. You don’t have to move, on-premise SAP IQ continues to be fully supported with SAP having committed to keeping version 16.1 in mainstream maintenance through at least 2027-12-31. However, it takes a lot of effort to maintain an on-premise database system and migrating to a cloud deployment provides the opportunity to offload a lot of critical but time consuming administration and maintenance tasks to the cloud service, which then frees up your database team to focus more time on higher value database development activities.

If you are thinking about migrating your on-premise SAP IQ system to the cloud, here are my picks for the top 5 benefits of moving to SAP HANA Cloud, data lake.

## Ease of provisioning

Provisioning a new database in an on-premise environment is never a simple task. Even if you have software licenses already available you still have to go through the hardware procurement process, getting multiple quotes from vendors, waiting for delivery once a purchase order is submitted, and waiting for the hardware to be set up. The overall process usually takes a few months and depending on your hardware refresh cycle, it has to be repeated every 3-5 years.

With SAP HANA Cloud, data lake it takes just a few minutes from clicking Create Instance to having a running database, and perhaps best of all – you NEVER have to upgrade the hardware.

![](/legacyfs/online/storage/blog_attachments/2022/11/Create-Standalone-HDL-Workflow.png)

## Near Zero Downtime Upgrades (NZDU)

Speaking of upgrades, hardware isn’t the only thing that needs to be upgraded when running your on-premise system. The database software has to be upgraded too, and that certainly happens more frequently than the hardware upgrades.

One of the bigger pain points in the execution of software upgrades of mission critical systems is scheduling and managing the system downtime, often having to align with very tight maintenance windows.

This is an area where SAP HANA Cloud, data lake provides real innovation leveraging control of the cloud infrastructure along with the fact that every SAP HANA Cloud, data lake instance is a multi-node scale out or multiplex system to execute a rolling NZDU that maintains read access to the system throughout the process.

![](/legacyfs/online/storage/blog_attachments/2022/11/NZDU-Screenshot.png)

## Flexible scaling of compute

Coming back to the topic of provisioning, one of the challenging aspects of any on premise system is sizing. Hardware purchases, for both the server hardware and the storage hardware, are pretty inflexible. Sure, you can use virtualization software to deploy multiple smaller systems on a single server, but when you are deploying a database system that could scale to 10’s or 100’s of TB, or even PBs then sharing servers really isn’t an option.

If you are working with a mature on-premise database, then you likely have a good idea of how the data volume will grow over the next 3-5 year hardware cycle. However, if you’re standing up a new system your data volume and workload estimates might be solid for the first year but get less and less reliable the further out you look.

With an on-premise system you usually end up buying and provisioning a system that is over sized for the first year, that you hope the business will grow into over the hardware lifecycle, but which could end up being undersized before the end of the cycle.

Migrating your SAP IQ system to an SAP HANA Cloud, data lake system provides the ability to scale your compute resources – vCPU and memory – up or down as needed. Scaling can be done vertically or horizontally, either increasing the size of worker nodes or adding more worker nodes to the system.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-HDLRE-Compute.png)

## Automatic storage resizing

One of the characteristics of SAP IQ that has felt outdated to me for a long time is the need to pre-allocate storage space in the form of dbspaces made up of multiple dbfiles. Monitoring the available space, and adding dbfiles as needed to grow the storage volume isn’t a difficult task but it is “one more thing” you have to do when administering an on-premise SAP IQ system.

That task goes away when you migrate to SAP HANA Cloud, data lake with the required storage volume being automatically allocated as you add data to the database. This also benefits your cost of ownership compared to an on-premise SAP IQ system because with SAP HANA Cloud, data lake you are only charged for the storage volume that you are currently using.

**<Sorry, no picture for this one because you don’t**

**have to manage your storage volume.** **![:smiling_face_with_smiling_eyes:](/html/@F1E2370483376CBD357141A1D520B3FD/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")>**

Another cost benefit of migrating your on-premise SAP IQ system to SAP HANA Cloud, data lake Relational Engine is reducing the per unit cost of the storage volume. The pe...