---
title: Support Spotlight: Quick Handbook for SAP HANA Database 2.0 administration using SAP HANA Studio
url: https://blogs.sap.com/2023/03/16/support-spotlight-quick-handbook-for-sap-hana-database-2.0-administration-using-sap-hana-studio/
source: SAP Blogs
date: 2023-03-17
fetch_date: 2025-10-04T09:50:42.548270
---

# Support Spotlight: Quick Handbook for SAP HANA Database 2.0 administration using SAP HANA Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Support Spotlight: Quick Handbook for SAP HANA Dat...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50458&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Support Spotlight: Quick Handbook for SAP HANA Database 2.0 administration using SAP HANA Studio](/t5/enterprise-resource-planning-blog-posts-by-sap/support-spotlight-quick-handbook-for-sap-hana-database-2-0-administration/ba-p/13550554)

![haow](https://avatars.profile.sap.com/e/e/idee09ee5a9e5a4fbd88153ad8bb9bdf881ffdd0171a362c0ecb93804b04b5011b_small.jpeg "haow")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[haow](https://community.sap.com/t5/user/viewprofilepage/user-id/174897)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50458)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50458)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550554)

‎2023 Mar 16
9:47 PM

[16
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50458/tab/all-users "Click here to see who gave kudos to this post.")

2,078

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)

View products (2)

With the release of SAP Business One 10.0, version for SAP HANA, the SAP HANA Database 2.0 with SAP HANA Multitenant Database Containers (MDC), has become the only and default database system mode.

In this blog post we will look at various aspects of this new environment - Adding system and tenant database, License installation, Import of schema, Backup, some housekeeping tips and finally how to recover to a point in time.

**Adding System and Tenant Database using SAP HANA MDC**

When installing SAP HANA Database 2.0 MDC for SAP Business One, it will contain a system database which is used for central system administration and a tenant database which holds catalogs for company schemas.

For operational tasks related to database administration, monitoring and maintenance, a database administrator can use SAP HANA Studio to add the database systems with MDC mode. This is possible for both the system and tenant database as per the screenshot below.

![](/legacyfs/online/storage/blog_attachments/2023/03/SS1-1.png)

Screenshot 1-1 Adding system and tenant database to the HANA Studio

**License installation**

After successfully adding both system and tenant to SAP HANA Studio, the database administrator should request and install a permanent license key, this is to avoid a standstill as the temporary license used during installation expires after 90 days.

With SAP HANA Database 2.0 you can install separate licenses for the system and tenant systems. Installing the license on the system database will automatically install it on the tenant database. However, a license installed on the tenant database will only govern the tenant. The recommendation is to install the license on the system database.

The license information for the system database can be found by right clicking on the system database and then selecting *Properties → License* as per the screenshot.

![](/legacyfs/online/storage/blog_attachments/2023/03/SS2-1.png)

Screenshot 2-1 Install license for system database

SAP Knowledge Base Article (KBA) [*3230586*](https://launchpad.support.sap.com/#/notes/3230586) [*- How to Correctly Perform License Installation for SAP HANA Database in SAP HANA*](https://i7p.wdf.sap.corp/sap/support/notes/3230586) *2.0,* provides additional information on how to perform a license reinstallation if the license was installed incorrectly or a license reinstallation is needed for other reasons.

**Import a database schema**

Now the new SAP HANA database is ready for importing database schemas! The process can be done either via the tenant database catalog import wizard in SAP HANA Studio, or via the tenant database catalog import SQL query provided via SAP Note [*2134959 - Schema Export and Import Guide for SAP Business One, version for SAP HANA*](https://launchpad.support.sap.com/#/notes/2134959).

![](/legacyfs/online/storage/blog_attachments/2023/03/SS3-1.png)

Screenshot 3-1 Importing a database schema in SAP HANA Studio

Once a database schema is imported, it can be found under the tenant database catalog.

**Database backup**

SAP HANA database provides multiple functionalities for database backup and recovery. A healthy, recently completed database backup is crucial to ensure the database can be recovered with maximum business continuity.

To manually make a database backup using SAP HANA Studio, right click on *Backup* under the system database, and then select *Backup Up System Database* or *Back up Tenant Database*.

![](/legacyfs/online/storage/blog_attachments/2023/03/SS4-1.png)

Screenshot 4-1 Making new backup for system and tenant database via SAP HANA Studio

It is recommended to back up system and tenant databases as they both contain business critical information.

**Housekeeping**

If there is a schedule set up either manually or automatically to create backups for the onsite SAP HANA Database, it is also recommended to regularly check the disk usage and whether old backups need to be deleted to maintain sufficient disk space on the server.

To remove old backups which are no longer needed, the database administrator can right-click on an existing backup from the *Backup Console* list and select *Delete Older Backups*. To open the *Backup Console* click on *Backup* under *System* in the screenshot below. Then, check *Catalog and Backup Location* and *File System* to clean the old backups and related files physically from the backup location on the server.

![](/legacyfs/online/storage/blog_attachments/2023/03/SS5-1.png)

Screenshot 5-1 Backup list showing in Backup Catalog in Backup Console

![](/legacyfs/online/storage/blog_attachments/2023/03/SS5-2.png)

Screenshot 5-2 Delete old backups and related files from the backup location physically

**Recover database to a point in time**

If some unexpected issue occurs to the SAP HANA Database system in the environment, and the database is unavailable the database administrator can validate the server status and decide if a database recovery is needed. If so, the most common and easiest way is to recover the database to a specific point in time.

For a point in time database recovery, the database administrator will need to ensure that the following are available:

* At least one full backup (complete data backup or da...