---
title: Upgrading SAP HANA, express edition from SPS05 to SPS06 (solution for failed HRTT service deployment)
url: https://blogs.sap.com/2022/11/18/upgrading-sap-hana-express-edition-from-sps05-to-sps06-solution-for-failed-hrtt-service-deployment/
source: SAP Blogs
date: 2022-11-19
fetch_date: 2025-10-03T23:13:18.939370
---

# Upgrading SAP HANA, express edition from SPS05 to SPS06 (solution for failed HRTT service deployment)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Upgrading SAP HANA, express edition from SPS05 to ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163595&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Upgrading SAP HANA, express edition from SPS05 to SPS06 (solution for failed HRTT service deployment)](/t5/technology-blog-posts-by-sap/upgrading-sap-hana-express-edition-from-sps05-to-sps06-solution-for-failed/ba-p/13567376)

![Laszlo_Thoma](https://avatars.profile.sap.com/9/0/id90e702a1d83a67b7a2fde409bf21a6d43811f8e390c7650756fae929ea4a3e5d_small.jpeg "Laszlo_Thoma")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Laszlo\_Thoma](https://community.sap.com/t5/user/viewprofilepage/user-id/170406)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163595)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163595)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567376)

‎2022 Nov 18
3:44 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163595/tab/all-users "Click here to see who gave kudos to this post.")

3,147

* SAP Managed Tags
* [SAP HANA, express edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520express%2520edition/pd-p/73555000100800000651)

* [SAP HANA, express edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bexpress%2Bedition/pd-p/73555000100800000651)

View products (1)

**![banner.png](/t5/image/serverpage/image-id/53575iC0ECBC3D91E9BC8A/image-size/large?v=v2&px=999 "banner.png")**

**Task**
Upgrading SAP HANA, express edition SPS05 (db version: 2.00.057) to SPS06 (db version: 2.00.061).

**Reason of the Article**
I encountered issues during the upgrade. The aim of this article is to document these upgrade issues, and demonstrate how I resolved them.

**Architecture**
In my scenario I am using Windows 11 operating system on my laptop. I am running SAP HANA, express edition (preconfigured) Server + applications virtual machine on VMware Workstation.

* [Frequently Asked Questions About SAP HANA®, Express Edition](https://www.sapstore.com/medias/HANA-express-edition-FAQ?context=bWFzdGVyfHJlc291cmNlc3wxMzcwNzY0fGFwcGxpY2F0aW9uL3BkZnxyZXNvdXJjZXMvaDY0L2hkNS8xMzI2NjIwMzE4MTA4Ni5wZGZ8YjI5ZTkwOWZhZTEzNDllZmY0OTgyNjM1ZmZkNzU1NzBkYTUyMDIwNWJkYTY1ODEyNzk1ZjdmNDZlMTcyZGMyNw)
* [Server + Applications: SAP HANA, express edition and XSA – by the SAP HANA Academy](https://blogs.sap.com/2017/09/19/plus-apps.-sap-hana-express-edition-and-xsa-by-the-sap-hana-academy/)
* SAP Help Portal – [SAP HANA, express edition](https://help.sap.com/docs/SAP_HANA_EXPRESS_EDITION)
* SAP Help Portal – [Getting Started with SAP HANA 2.0, express edition (Virtual Machine Method)](https://help.sap.com/docs/SAP_HANA_EXPRESS_EDITION/8c3bbc4a904d42efac77c09da0bccf64/d151ab61e77047d487b45649f5a6d383.html)
* SAP Help Portal – [Getting Started with SAP HANA 2.0, express edition (Virtual Machine Method) – PDF](https://help.sap.com/doc/41294350f4c149418887c3c019a61354/2.0.050/en-US/Getting_Started_HANAexpress_VM.pdf)

**Prerequisites**

* Hypervisor (VMware Workstation Player 16)
* SAP HANA, express edition (db version: 2.00.057)
  [Install SAP HANA 2.0, express edition on a Preconfigured Virtual Machine (with SAP HANA XS Advanced)](https://developers.sap.com/group.hxe-install-vm-xsa.html)
* SAP HANA Studio (version: 2.3.63)

**Background**
I have performed SAP HANA express edition upgrades before, and the procedure went well without any issues. My previous SAP HANA, Express Edition upgrade from (db version: 2.00.054) to (db version: 2.00.057) was performed using the following articles as resources:

* [Upgrading SAP HANA, express edition to SPS04](https://blogs.sap.com/2019/08/08/upgrading-sap-hana-express-edition-to-sps04/)
* [Upgrade to SAP HANA Express 2.0 SPS03](https://answers.sap.com/questions/498086/upgrade-to-sap-hana-express-20-sps03.html)
* [Upgrade SAP HANA, express edition](https://developers.sap.com/group.hxe-upgrading.html)

**Configuration**

* Memory: Laptop has 32 GB physical memory. Virtual Machine has 16 GB memory in general. During the upgrade it can be setup up to 24 GB memory (in my case).
* Disk: Virtual Machine has 150 GB disk. Total Disk Usage is around 80 GB. This includes the backup files from the SYSTEMDB and the two Tenant DB also. The disk had been resized one time based on the following information: [SAP HANA Express, resize partition](https://answers.sap.com/questions/12965015/sap-hana-express-resize-partition.html)

**Before upgrade**

* [SAP HANA, express edition uninstall SHINE before upgrade to HANA 2.0 SPS06](https://blogs.sap.com/2022/11/07/sap-hana-express-edition-uninstall-shine-before-upgrade-to-hana-2.0-sps06/)

**Upgrade failed (issue with hrtt-service)**
I tried the same upgrade steps that I used in previous upgrades. However, this time the upgrade to SPS06 failed with the following error message on the console.

* *Installation of the component XSAC\_HRTT (sap.com) 2.14.220902 failed during deployment.*
* *Update of SAP HANA Express Edition components failed.*

**!!! IMPORTANT !!!**
**I tried the upgrade several times (I did the upgrade from VM backup multiple times)
and the same issue occurred again and again. That is, the issues were reproducible.**

```
...

Note: Resume SAP HANA System update at step 'Start instances'

Updating components...

Starting instances...

Updating Component List...

Installing XS Advanced Components...

  Installing SAP HANA tools for accessing catalog content, data preview, SQL console, etc....

    Deploying in org "HANAExpress" and space "SAP"

    Updating application "hrtt-service"...

    Uploading application "hrtt-service"...

    Stopping application "hrtt-service"...

    Starting application "hrtt-service"...

    Installation of the component XSAC_HRTT (sap.com) 2.14.220902 failed during deployment.

    Installation of archive file(s) '/usr/sap/HXE/home/Downloads/HANA_EXPRESS_20/DATA_UNITS/XSAC_HRTT_20/XSACHRTT14_220902.zip' failed.

    Installation of the component XSAC_HRTT (sap.com) 2.14.220902 failed during deployment.

  Installation of SAP HANA tools for accessing catalog content, data preview, SQL console, etc. failed

Update of SAP HANA Express Edition components failed.

  Installation of XS Advanced components failed

    Installation of SAP HANA tools for accessing catalog content, data preview, SQL console, etc. failed

Log file written to '/var/tmp/hdb_HXE_hdblcm_update_2022-10-08_17.18.45/hdblcm.log' on host 'hxehost'.

Upgrade failed.
```

I checked the following log files below. During the upgrade the XSAC\_HRTT component tried to update itself (first log file), but it failed. After that the XSAC\_HRTT component tried to update itself one more time (second log file), but it failed again, because of this the whole update process failed.

**/var/tmp/hdb\_HXE\_hdblcm\_update\_2022-10-08\_16.16.52/hdblcm.log**

```
16:41:05.898 - INFO:   -----------------------------------------...