---
title: SAP Archiving Basic Guide for Beginner’s
url: https://blogs.sap.com/2022/11/21/sap-archiving-basic-guide-for-beginners/
source: SAP Blogs
date: 2022-11-22
fetch_date: 2025-10-03T23:23:16.569124
---

# SAP Archiving Basic Guide for Beginner’s

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Data Archiving Basic Guide for Beginner's

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160341&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Data Archiving Basic Guide for Beginner's](/t5/technology-blog-posts-by-members/sap-data-archiving-basic-guide-for-beginner-s/ba-p/13551746)

![P2004515579](https://avatars.profile.sap.com/8/6/id860aab797c4af453254693fda74bbb042890afb8d95e9ba9a3786c85e1bacab4_small.jpeg "P2004515579")

[P2004515579](https://community.sap.com/t5/user/viewprofilepage/user-id/43027)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160341)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160341)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551746)

‎2022 Nov 21
10:45 PM

[25
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160341/tab/all-users "Click here to see who gave kudos to this post.")

69,809

* SAP Managed Tags
* [NW ABAP Data Archiving](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Data%2520Archiving/pd-p/777340172955087410686548844218124)

* [NW ABAP Data Archiving

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BData%2BArchiving/pd-p/777340172955087410686548844218124)

View products (1)

## **Topics to be covered**

* Introduction

* Benefits

* Programs

* Archiving object

* T-Codes Explain

* Archiving Development Kit

* Access to archived data

* Data Archiving Roadmap

* Storage system

* Conclusion

## **Introduction**

Recently, I completed SAP Data Archiving Basic Training. Everyone has heard about archiving once in a lifetime. Let’s understand the basics of SAP data archiving in detail.

‘**Archiving**’ means the process associated with copying data and supporting documents from an active system to an external source for the purpose of deletion or storage for later retrieval.

In SAP, ‘**Data archiving’** means selecting the huge volume of data that is no longer required in the database and that has not been used for a long time. Sap recommends this process of data archiving to clean up the SAP standard tables and improve the system's performance and usability.

![](/legacyfs/online/storage/blog_attachments/2022/11/IMG_20221120_132704.jpg)

Fig.1 A data archiving decision tree (Source: SAP)

## **Benefits of data archiving**

* Reduce the cost of memory, disk, and administration costs.

* Improved system performance and response time.

* Reduce the cost of maintenance and run of growing application infrastructure.

Let’s understand the programs used in the data archiving process,

1. Write :-

This program creates a new archive file and writes the data in it. At this point, no data has been deleted from the database. The write program can be executed in two processing models. (To create archive files)

* Test mode

* Production mode

In the test mode, no archive files will be created, whereas in the production mode, archive files will be created.

![](/legacyfs/online/storage/blog_attachments/2022/11/wd.png)

Fig.2 Write Program

Write session: -

* SARA - > Give archiving object name.

* Click on write button

* Now provide variant name and click on maintain button to create the variant for write session.

* Determine the user under which the session needs to be started.

* Specify the date and time.

* Define the spool parameter.

* Execute

2. Delete: -

This program reads the data from the archived files and deletes the data from the database. The delete program can be executed in different processing modes.

* Test mode

* Production mode

In the test mode, the log after the execution shows the entries of the data to be deleted from the database, whereas in the production mode it shows the statistics of the deleted data from the database.

Delete session:-

* SARA- > Give archiving name.

* Click on delete action button

* Determine the user under which the archive files need to be deleted

* Select the archive files to be deleted

* Specify the start date and time.

* Define the spool parameter

* Execute

3. Reload: -

This program is used to reload the archived data from the external storage system back into the respective SAP database tables. It is not available for all the archiving objects. (If need be, the archived objects can be restored.)

4. Pre-processing: -

Before the write phase, some archiving objects undergo optional phase named pre-processing.

In pre-processing, the data for archiving is marked by the creation of a deletion flag, but the data is not deleted from the database.

On completion of pre-processing, the data marked for deletion will be archived by write program.

![](/legacyfs/online/storage/blog_attachments/2022/11/man.png)

Fig.3 Preprocessing

5. Post processing:-

It also operates on the database and does not require any archive files. This is the final program and can be executed asynchronously with the delete program.

If the data from the database is not deleted by the delete programs, it can be deleted by the post processing program.

6. Index program:-

The program builds or deletes an index that allows individuals access. Infostructure created for archive objects acts as an index to the archived data.

### **Archiving session’s status:-**

* Complete status:- Data archived and deleted.(Green)

* Incomplete status:- Data was only archived.(Yellow)

* Error status:- Error occurred while write program.(Red)

![](/legacyfs/online/storage/blog_attachments/2022/11/varaiant.png)

Fig.4 Status

## **Archiving object:-**

* Archiving objects describe the structure and context of the data to be archived.

* An archiving object combines all the functions necessary to archive data that is linked through business process (Such as Orders, invoices etc.) and object linked to this data.

* Archiving objects are defined by the transaction AOBJ.

![](/legacyfs/online/storage/blog_attachments/2022/11/Ar.Project1.png)

Fig.5 Archiving Object

### **Archive Administration**:

The Archive administration enables you to all your archiving programs (read, write, delete, and restore) and also generates background jobs for them.

Residence period:

Amount of data that will be available online before it meets the achievability criteria.

Retention period: -

It is the entire time that the data spends in archive format before it gets deleted from the actual database.

## **T-Codes  explain****:-**

SARA:-

* Central transaction for performing data archiving.

* From SARA, we can branch to other transactions in data archiving environment.

* SARA is an archive administration tool that is used to write, delete and manage all data archive in SAP system.

![](/legacyfs/online/storage/blog_attachments/2022/11/Sara1.png)

Fig.6 SARA

AOBJ:-

* Contains the programs offered by archiving object.

* Contains the tables from which the data is archived for a particular object, customizing settings for the object etc.

* AOBJ can be used to define custom archiving objects for the customer specific tables.

DB02:-

* A datab...