---
title: SAP HANA Database Encryption
url: https://blogs.sap.com/2022/11/18/sap-hana-database-encryption/
source: SAP Blogs
date: 2022-11-19
fetch_date: 2025-10-03T23:13:03.578874
---

# SAP HANA Database Encryption

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP HANA Database Encryption

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160932&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP HANA Database Encryption](/t5/technology-blog-posts-by-members/sap-hana-database-encryption/ba-p/13555367)

![saroopreddy88](https://avatars.profile.sap.com/c/f/idcfdf1a63e02d8aba89b98079bf91d0c599253ff5ae92dcf505e74e92e459c7d3_small.jpeg "saroopreddy88")

[saroopreddy88](https://community.sap.com/t5/user/viewprofilepage/user-id/17026)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160932)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160932)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555367)

‎2022 Nov 18
8:26 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160932/tab/all-users "Click here to see who gave kudos to this post.")

59,908

* SAP Managed Tags
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)

* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)

View products (1)

**SAP HANA ENCRYPTION**

**INTRODUCTION**

SAP HANA provides full support for data-at-rest encryption to secure your data.

SAP HANA is an in-memory database, and most of the data is in the main memory for maximum performance. This helps in processing large data at a very high speed with less administrative effort. However, data is automatically saved from memory to disk at regularly to ensure that the database can be restored to its most recent committed state. Here, all data changes are also captured in redo log entries.

**DATA VOLUME ENCRYPTION**

Data volume encryption is available from SAP HANA 1.0 SP12.  This protects the data area on the disk, i.e., all the data that resides under /hana/data/<SID>

This encryption uses AES-256-CBC Algorithm and 256-bit page encryption keys to encrypt and decrypt the data.

As shown here, data is encrypted while it is being saved on to the disk, and it is decrypted when it is being loaded into the memory.

![](/legacyfs/online/storage/blog_attachments/2022/10/1-94.png)

**LOG VOLUME ENCRYPTION**

Redo log encryption protects the log area i.e., the logs that are created under /hana/log/SID.

This feature is available only from HANA 2.0 SP00.

Like data volume encryption, log volume encryption also uses AES-256-CBC Algorithm and 256-bit page encryption keys.

**BACKUP ENCRYPTION**

This feature is available from HANA 2.0 SP01. Backup encryption protects the contents of data backup, log backups and delta/ differential backups which includes snapshot backups as well. Backup encryption can be enabled for both backups written to the file system or backup written to the third-party backup tool through backint for SAP HANA interface.

A third-party backup tool can also be used, in this case, you have a choice between SAP HANA Encryption or tool-side backup encryption. If full protection in the persistence layer is required, SAP recommends that you use all the three backups.

**KEYS USED IN SAP HANA ENCRYPTION**

1. Instance SSFS Master Key

2. PKI SSFS Key.

3. Data Volume Root Key

4. Log Volume Root Key

5. Backup Volume Root Key

**HOW TO ENABLE AND DISABLE ENCRYPTION?**

There are two ways in which you can enable and disable encryption, one is through SAP HANA Studio by use of various SQL commands or statements. The other option is to do it through SAP HANA COCKPIT.

**Enable and Disable Encryption using SAP HANA Studio**

Stop your HANA DB.

SAP HANA provides two keys with installation which are

1. SSFS Keys à These keys reside in /hana/shared/<SID>/global/hdb/security/ssfs. These instance SSFS keys helps in protecting the root keys used for all data-at-rest encryption services and the internal application encryption service.

2. PKI SSFS à system PKI SSFS helps protect system-internal root certificates required for secure internal communication. These keys can be found under /usr/sap/<SID>/SYS/global/security/rsecssfs/.

If your HANA DB is pre-installed or delivered by any partner, then SAP recommends to change the master keys that are created during installation.

1. Encrypt SSFS Keys:

Take a backup of existing SSFS keys which will be at /hana/shared/<SID>/global/hdb/security![](/legacyfs/online/storage/blog_attachments/2022/10/2-50.png)

Switch to sidadm at OS level and execute below commands

*export RSEC\_SSFS\_DATAPATH=/usr/sap/SAR/SYS/global/hdb/security/ssfs*

*export RSEC\_SSFS\_KEYPATH=/usr/sap/SAR/SYS/global/hdb/security/ssfs*![](/legacyfs/online/storage/blog_attachments/2022/10/3-42.png)

*rsecssfx changekey $(rsecssfx generatekey -getPlainValueToConsole)*![](/legacyfs/online/storage/blog_attachments/2022/10/4-35.png)

Go to path /usr/sap/SAR/SYS/global/hdb/custom/config and add below lines in global.ini file.

*ssfs\_key\_file\_path = /usr/sap/SAR/SYS/global/hdb/security/ssfs*![](/legacyfs/online/storage/blog_attachments/2022/10/5-34.png)

Encrypt PKI SSFS Keys:

*export RSEC\_SSFS\_DATAPATH=/usr/sap/SAR/SYS/global/security/rsecssfs/data*

*export RSEC\_SSFS\_KEYPATH=/usr/sap/SAR/SYS/global/security/rsecssfs/key*

*rsecssfx changekey $(rsecssfx generatekey -getPlainValueToConsole)*

![](/legacyfs/online/storage/blog_attachments/2022/10/6-34.png)

Now start your HANA DB and give system privilege ENCRYPTION ROOT KEY ADMIN to user and run below SQL command.

Whenever HANA DB is installed or a tenant DB is created, unique keys will be created, and encryption will be disabled.

From HANA studio, To check Initial Keys ***select \* from ENCRYPTION\_ROOT\_KEYS;***

![](/legacyfs/online/storage/blog_attachments/2022/10/7-23.png)

To check encryption status ***select \* from SYS.M\_ENCRYPTION\_OVERVIEW***

![](/legacyfs/online/storage/blog_attachments/2022/10/8-18.png)

**How to enable Encryption on SYSTEM DB**

**Set the Root Key Backup Password**

This root key backup password is required to decrypt the root key backup file while any restore or recovery is being performed. This can be done via HANA Studio or Cockpit.

*ALTER SYSTEM SET ENCRYPTION ROOT KEYS BACKUP PASSWORD <PASSPHRASE>*

![](/legacyfs/online/storage/blog_attachments/2022/10/9-17.png)

Once the password is created, this will be stored in SSFS along with other keys.

To validate the password run below SQL statement.

*ALTER SYSTEM VALIDATE ENCRYPTION ROOT KEYS BACKUP PASSWORD "Welcome.1"*

If password is wrong output will be as below.

![](/legacyfs/online/storage/blog_attachments/2022/10/10-10.jpg)

Could not execute 'ALTER SYSTEM VALIDATE ENCRYPTION ROOT KEYS BACKUP PASSWORD "Welcome1"' in 7 ms 575 µs .

SAP DBTech JDBC: [703]: incorrect root keys backup password: Validation of the Root Keys Backup Password failed.

**Generate New Root Keys**

Below are the unique keys which are created during installation.

*select \* from ENCRYPTION\_ROOT\_KEYS;*

![](/legacyfs/online/storage/blog_attachments/2022/10/...