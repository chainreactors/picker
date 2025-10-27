---
title: Old Snapshot deletion to reduce doubled/Larged hana/data volume size
url: https://blogs.sap.com/2023/03/04/old-snapshot-deletion-to-reduce-doubled-larged-hana-data-volume-size/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:33.658314
---

# Old Snapshot deletion to reduce doubled/Larged hana/data volume size

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Old Snapshot deletion to reduce doubled/Larged /ha...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68063&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Old Snapshot deletion to reduce doubled/Larged /hana/data volume size](/t5/enterprise-resource-planning-blog-posts-by-members/old-snapshot-deletion-to-reduce-doubled-larged-hana-data-volume-size/ba-p/13562999)

![kiranchavan0912](https://avatars.profile.sap.com/2/1/id21e77e5d4804dd6e9f376c90fb45c5f77e8bf9c7f489f91e512219783cad0f1c_small.jpeg "kiranchavan0912")

[kiranchavan0912](https://community.sap.com/t5/user/viewprofilepage/user-id/808708)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68063)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68063)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562999)

‎2023 Mar 04
7:50 PM

0
Kudos

4,227

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (2)

Hello Everyone,

Recently I came across the situation where the HANA Data Volume Used Size is Doubled or Much Larger than Before and even HANA reclaim could not free up data volume used size.

This was for non-production HANA system where we had recently done the system refresh from production system which has HA (HIGH Availability) Setup. Usually this problem happens post system refresh as replication snapshots from production gets copied.

Below are the symptoms for this issue.

* Data volume used size is doubled or much larger than before

* Huge Difference between Backup size and /hana/data disk size

* There are old snapshots shown in result of "select \* from m\_snapshots" query in HANA tenant

* There is no large tabled imported or index created

* "ALTER SYSTEM RECLAIM DATAVOLUME" could not reclaim data volume used size

**Steps to identify the snapshots which can be deleted in HANA.**

**1**. Run sql query **"select \* from m\_snapshots"** in HANA tenant of affected system. Check for **FOR\_BACKUP**column, if value is **FALSE** and snapshot is old then it is eligible to get deleted from system to achieve free space in data disk.

![](/legacyfs/online/storage/blog_attachments/2023/03/PIC-1-1-1.jpg)

**2.** Now you can check the current replication status using ***SQL:** "**HANA\_Replication\_SystemReplication\_Status"*** (SAP Note [1969700](https://me.sap.com/notes/1969700)). If the STATUS\_DETAILS are empty for the services, you can proceed.

**3.** In Above Screenshot, Notedown the PORT Value, Which will help you to identify the service related to it. As per screenshot 1, the snapshots exists for PORTS 30003,30011, 30007,30040. To identify HANA service related to it navigate to **Landscape -> Services Tab** in HANA Studio.

![](/legacyfs/online/storage/blog_attachments/2023/03/pic2-1.jpg)

|
 **PORT** |
 **HANA Service** |

|
 30003 |
 Indexserver |

|
 30011 |
 dpserver |

|
 30007 |
 exengine |

|
 30040 |
 docstore |

**4.** In case only a single service with the name exists, you can use "-e" to identify it, otherwise you  need to use "-p":

```
hdbcons -e hdb<service_name> 'snapshot l'

hdbcons -p <os_pid> 'snapshot l'
```

*e.g hdbcons -e hdbindexserver 'snapshot l'   or  hdbcons -p 31655 'snapshot l'*

Note: Refer Screenshot 2 **Process ID** Column to get <os\_pid>

hdbcons -e hdbindexserver 'snapshot l'  command will give the snapshot ID. kindly make a note of it and cross check the same with ID column in screenshot 1.

**5.** To check the size cosumed by snapshot use below command.

```
hdbcons -e hdb<service_name> 'snapshot a <snapshot_id>'

hdbcons -p <os_pid> 'snapshot a <snapshot_id>'
```

*e.g hdbcons -e hdbindexserver 'snapshot a 423984'  or  hdbcons -p 31655 'snapshot a 423984'*

**6.** If you have confirmed that the database snapshot is no longer required, the snapshot ID can be dropped with the following hdbcons command:

```
hdbcons -e hdb<service_name> 'snapshot d <snapshot_id>'

hdbcons -p <os_pid> 'snapshot d <snapshot_id>'
```

 *e.g hdbcons -e hdbindexserver 'snapshot d 423984' or hdbcons -p 31655 'snapshot d 423984'*

**7.** Run sql query **"select \* from m\_snapshots"** which will result blank screen this means all snapshots has been deleted in the system.

8. Now you can check the Fragmentation status using ***SQL: "HANA\_DISK\_OVERVIEW"***(SAP Note [1969700](https://me.sap.com/notes/1969700)). If **FRAG\_PCT** ( Fragmentation % ) is more than 20% then we are good to run the reclaim in HANA. using sql **"ALTER SYSTEM RECLAIM DATAVOLUME 120 DEFRAGMENT;"**.

9. By this method you will be successfully able to achieve good amount of disk space in hana/data which was unnecessarily consumed by old replication snapshots.

**Reference:**

1. <https://me.sap.com/notes/0002562939>

2. <https://me.sap.com/notes/1999880>

* [HANA snapshot](/t5/tag/HANA%20snapshot/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fold-snapshot-deletion-to-reduce-doubled-larged-hana-data-volume-size%2Fba-p%2F13562999%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Error in archiving for HRCUSTAX object](/t5/enterprise-resource-planning-q-a/error-in-archiving-for-hrcustax-object/qaq-p/14234432)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Need Help: Deleting Multiple Schedule Lines in ME38](/t5/enterprise-resource-planning-q-a/need-help-deleting-multiple-schedule-lines-in-me38/qaq-p/14230968)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Monday
* [Unable to remove serial number profile from material](/t5/enterprise-resource-planning-q-a/unable-to-remove-serial-number-profile-from-material/qaq-p/14221595)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [How I can delete a sap business one company database properly?](/t5/enterprise-resource-planning-q-a/how-i-can-delete-a-sap-business-one-company-database-properly/qaq-p/14220491)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Data Migration Cockpit reporting data already migrated](/t5/enterprise-resource-planning-q-a/data-migration-cockpit-reporti...