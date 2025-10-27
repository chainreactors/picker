---
title: Quick Guide to SAP BW/4HANA Migration
url: https://blogs.sap.com/2023/06/18/quick-guide-to-sap-bw-4hana-migration/
source: SAP Blogs
date: 2023-06-19
fetch_date: 2025-10-04T11:45:47.942434
---

# Quick Guide to SAP BW/4HANA Migration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Quick Guide to SAP BW/4HANA Migration

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162320&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Quick Guide to SAP BW/4HANA Migration](/t5/technology-blog-posts-by-members/quick-guide-to-sap-bw-4hana-migration/ba-p/13562964)

![prem_shanker](https://avatars.profile.sap.com/2/d/id2dee7548c0513f10ba088d98dffca78f1df082a7c171c47230013be7eadc164f_small.jpeg "prem_shanker")

[prem\_shanker](https://community.sap.com/t5/user/viewprofilepage/user-id/652189)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162320)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162320)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562964)

‎2023 Jun 18
1:02 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162320/tab/all-users "Click here to see who gave kudos to this post.")

32,142

* SAP Managed Tags
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)

* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)

View products (1)

**SAP BW/4HANA** is SAP’s next generation data warehouse solution. It is entirely built on **SAP HANA** database. When customer wants to install SAP BW/4HANA, the question arises of which method is most appropriate. Generally, the “greenfield approach” (new installation of the system) or the System Migration approach come into question. System Migration which are “in-place conversion”, “remote conversion” and “shell conversion”.

In this blog we will be discussing how to Migrate current BW system to SAP BW/4HANA system.

**Strategy 1:** Same BW box we are upgrading to BW/4HANA system. This is called **In-Place Migration** i.e., we don’t have a separate server, the same BW Prod box will be upgraded to             BW/4HANA system. SID (System ID) will remain the same.

* Redesign your current applications. [i.e., current DSO to ADSO, current MP to CP etc.]

* Clean up and delete obsolete objects.

* Significant downtime for Production.

**Strategy 2**: Create a new SAP BW/4HANA system. (New SID) i.e., Install a fresh new system which is already on BW/4HANA.

* Carve out existing future-proof BW applications or build them from scratch again.

* Phase out existing BW system and roll out new BW/4HANA system.

* Almost zero down time for production.

**Shell Conversion:**

* Accelerated Greenfield Conversion.

* Transfer of selected data model without data transfer.

**Remote Conversion:**

* Brownfield Conversion

* Transfer of selected data model with data transfer

![](/legacyfs/online/storage/blog_attachments/2023/06/Types-of-Migration-1.png)

Different Paths for SAP BW/4HANA Migration

**In-Place Conversion:**

* Target group: customer who wants to change their current SAP BW system into BW/4HANA system and who are already on an up-to-date release (preferably 7.5 powered by HANA).

* This means that the customer gets to keep the existing BW system and transfer it so BW/4HANA system (keeping the SID).

* Approach without re-implementation, no disruption for existing business processes.

* SAP provides all the tools that is required to complete the migration process (BW/4HANA Transfer cockpit).

* Release requirements: SAP BW 7.5 SP05 powered by HANA, but recommended is the recent SP level.

**Shell Conversion:**

* Target group: SAP BW customer

* For customer who wants a fresh SAP offers an option to transport certain objects from the old BW to newly installed BW/4HANA. These objects will be transported into BW/4HANA supported objects during import into BW/4HANA system (ex:- Infocube à ADSO).

* New System ID(SID).

* No Data transfer will happen from old BW system (neither Master data nor Transactional data) Data has to be re-loaded from original source system.

* Release requirements: SAP BW 7.x(regardless of database).

**Remote Conversion:**

* Target group: Customer who wants to change their current SAP BW system into SAP BW/4HANA system and who are in older release and not on SAP HANA.

* Remote conversion means that customer builds up a new BW/4HANA system (new SID) and transfer BW objects (metadata) and data (master and transactional data) from original SAP BW system.

* Convert BW objects in newly installed SAP BW/4HANA system. Multiple persistent objects (Infocube, DSO etc) will be replaced by ADSO.

* No database migration or BW application upgrade required.

* Release requirements: SAP BW 7.3(regardless of database).

![](/legacyfs/online/storage/blog_attachments/2023/06/right-path-for-migration.png)

Right Path for Migration

**Pre-Migration checks: -**

SAP Note - 2383530: Conversion from SAP BW to SAP BW/4HANA

This is the central note for the people who are planning to move to SAP BW/4HANA.

This note delivers the tool for Migration “Transfer cockpit” [T-Code: RSB4HCONV].

SAP Note - 2575059: SAP Readiness check for SAP BW/4HANA.

Initial Step: Readiness check [Tool will check the details of what we are missing].

* This provides add-on compatibility and do compatibility checks.

* BW/4HANA Sizing

* Simplification Items (like IPAK’s are simplified as DTP’s, PSA’s are simplified as ADSO’s)

**Transfer Cockpit [T-Code: RSB4HCONV].**

**Preparation phase: -** Pre-Checks - Sizing reports, clean up reports, Scan codes (if any manual modification is required).

* This is independent of migration/conversion approach.

* The Pre-checks provides the list of all non-compatible objects on the line item level (with technical names).

* It also provides the information on which line item will be deleted by default, or need to be deleted manually or taken care by the transfer tool itself etc.

![](/legacyfs/online/storage/blog_attachments/2023/06/BW4HANA-Transfer-cockpit-Prepare-a-conversion.png)

SAP BW/4HANA Transfer Cockpit

**Realization Phase: -** Which objects we need to migrate (scope Transfer), actual migration.

* This is different for each migration/conversion approach.

* This is actual migration step, and the conversion happens here.

* Deleting Technical content(ex:- 0TCT objects).

**Steps for Migration**

**In-Place Conversion:** When customer is already at BW on HANA latest version, one should be recommended to use In-Place Conversion. Prerequisite for In-Place Conversion is the Started Add on

**SAP BW/4HANA Started Add on: -**

* Pre-condition for BW/4HANA In-place migration.

* Added into the BW system which needs to be converted.

* Provide access to conversion tools and manage the conversion process.

* Technical Name of this component is BW4HANA.

* Basis person needs the authorization object **S\_RS\_B4H** to do the migration activity.

  + *SAP Notes 2246699: SAP BW/4HANA started add on Pre-Requisite and Installations.*

  + *SAP Notes 2189708 Installable Adds-Ons for SAP BW/4HANA Started Add-on.*

**System Modes provided by BW/4HANA Starter Add-on**

![](/legacyfs/online/storage/blog_attachments/2023/06/System-Modes.png)
...