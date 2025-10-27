---
title: Deep dive into SAP Migration with Distribution Monitor
url: https://blogs.sap.com/2023/02/21/deep-dive-into-sap-migration-with-distribution-monitor/
source: SAP Blogs
date: 2023-02-22
fetch_date: 2025-10-04T07:42:40.952829
---

# Deep dive into SAP Migration with Distribution Monitor

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [DevOps and System Administration](/t5/devops-and-system-administration/gh-p/devops-sysadmin)
* [Blog Posts](/t5/devops-and-system-administration-blog-posts/bg-p/devops-sysadminblog-board)
* Deep dive into SAP Migration with Distribution Mon...

DevOps and System Administration Blog Posts

Explore DevOps and system administration blog posts. Stay current with best practices, tools, and insights into efficient IT management strategies.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/devops-sysadminblog-board/article-id/208&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Deep dive into SAP Migration with Distribution Monitor](/t5/devops-and-system-administration-blog-posts/deep-dive-into-sap-migration-with-distribution-monitor/ba-p/13540962)

![Sagar198416](https://avatars.profile.sap.com/1/8/id18d0977a10a10b93c42c2af2996e1d700746f3735963bfc32399b031dc5516a9_small.jpeg "Sagar198416")

[Sagar198416](https://community.sap.com/t5/user/viewprofilepage/user-id/15716)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=devops-sysadminblog-board&message.id=208)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/devops-sysadminblog-board/article-id/208)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13540962)

‎2023 Feb 21
9:34 PM

[1
Kudo](/t5/kudos/messagepage/board-id/devops-sysadminblog-board/message-id/208/tab/all-users "Click here to see who gave kudos to this post.")

1,983

* SAP Managed Tags
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (1)

The purpose of this document is to cover the detailed procedure around setting up and executing the migration of large sized database with considerably higher number of application servers using SAP Distribution Monitor.
The Source system run on an Oracle 10.2.0.4 but the Target RHEL based SAP systems will run on Oracle 11.2. The Oracle version will be integrated to the SAP migration using the R3load Export & Import procedure.
This document should not be used as a technical plan and should only be used as a reference for future dry-runs and the actual cut-over.

Setting up of distribution monitor has to be done per-dominantly in three phases

**Preparation phase**

In the pre-requiste phase,the control information is generated and migration structure is formulated.Setting up common directory is the key as all the activities takes place over there rather than distributed over all the application servers.

**Export phase**

In export phase ,source database is unloaded in the respective application server in the local export directories.Distmon has to be executed in each of the application servers in order to dump the database in the local export locations in parallel which invariably shortens the net export time by utilizing all available resources.

**Import phase**

Each machine imports the packages that were designated to it during setup (and have been stored in the local data directory of this machine during import). Similar to the export, each machine must run the Distribution Monitor.
The packages are divided among the machines. A given package's export and import processes always operate on the same system.
Using a shared directory that is accessible to all machines, the control information is distributed among them. The Communication Directory is the name of this directory (commDir). One of the servers involved in the situation may host the communication directory. On each of the servers concerned, the DM is set up.

Before the export and import phases can begin, the preparation phase must be completed.If both the source and the target databases are accessible at the same time, the export and import phases can proceed simultaneously. Before beginning the import step, SAPinst must build the target database. Only tables and indexes are created by the DM at the target database.
The data folders on each individual server are where the R3load data files are written to and read from.

During the export and import process ,it is possible to monitor the status of the packages.

Tools which are used
The application is in DISTMON.SAR. The SAR file comprises of the Migration Monitor, the Java Split Tool and the Time Analyzer.

Please refer to note 784118 for details about the Migration Monitor, the Java Split Tool and the Time Analyzer.

• The Migration Monitor's properties files (export monitor cmd.properties and import monitor cmd.properties) are created automatically by the Distribution Monitor. The Preparation Phase is when this is primarily done. Later on, during the export and import phase, some parameters are set. Typically, the created files don't need to be modified. After the Preparation Phase was finished, you might change them if necessary in the directory before beginning the Export and Import Phase.

• The properties files (package splitter cmd.properties and package splitter tables.txt) required to execute the Java Split Tool are provided as samples. Before beginning the Preparation Phase, you can use them as a starting point to construct them in your working directory. For instance, package splitter tables.txt contains tables that need to be treated differently. You could choose the 50 biggest tables from transaction DB02 to replace the default selection.

• The Time Analyzer frequency is set using the analyzerFrequency export and import option. No properties files are used.
Restrictions

• The DM does not support system copies of releases lower than SAP\_BASIS 6.20.

•It is strongly advised to only read/write R3load control files (.exportInstallDir,.importInstallDir) and data files (.dataDirs) on local file systems. On occasions, NFS-mounted file systems crash due to heavy parallel load.

• Only the net mode of the Migration Monitor is supported with the DM (ftp and socket mode are not supported).

• Oracle: tablespace changes need to be perfomed as pr SAP Note 425079 ,

• DM only supports only ABAP based systems. Dual stack system is not supported.

Distribution Monitor and PL/SQL Splitter: Product and Version Details
The latest version of the distribution monitor should be downloaded from the SAP Note 855772.

**Distribution Monitor and PL/SQL Splitter: Product and Version Details**

The latest version of the distribution monitor should be downloaded from the SAP Note 855772.

![](/legacyfs/online/storage/blog_attachments/2023/01/Distribution-Monitor-executable-details.png)

The DISTMON.SAR contains the following executables:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture2-19.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture3-14.png)

A PL/SQL Package "SPLITTER" (attached to this note) has been developed to make the calculation of the ranges more efficient using Oracle specific optimizations. Depending on the type of table (cluster/pool, transparent, partitioned) different methods of calculation for the ranges will be performed to optimize the R3load export phase of the table. The splitter\_hint.txt version must be used for Oracle 10.2.x databases. There is additionally the file presplitter.txt, this file assist...