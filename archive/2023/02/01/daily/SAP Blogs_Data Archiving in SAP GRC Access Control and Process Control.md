---
title: Data Archiving in SAP GRC Access Control and Process Control
url: https://blogs.sap.com/2023/01/31/data-archiving-in-sap-grc-access-control-and-process-control/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:20:02.591299
---

# Data Archiving in SAP GRC Access Control and Process Control

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Data Archiving in SAP GRC Access Control and Proce...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5358&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data Archiving in SAP GRC Access Control and Process Control](/t5/financial-management-blog-posts-by-members/data-archiving-in-sap-grc-access-control-and-process-control/ba-p/13556279)

![debashish-sarma](https://avatars.profile.sap.com/8/2/id8201317f3f28f1aeaaeab275ce12d31aec878d6c935754f5fbf6d5e9e834c3ba_small.jpeg "debashish-sarma")

[debashish-sarma](https://community.sap.com/t5/user/viewprofilepage/user-id/592607)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5358)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5358)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556279)

‎2023 Jan 31
5:16 PM

[5
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5358/tab/all-users "Click here to see who gave kudos to this post.")

5,616

* SAP Managed Tags
* [SAP Access Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Access%2520Control/pd-p/01200615320800000796)
* [SAP Process Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Control/pd-p/01200314690800000209)

* [SAP Access Control

  SAP Access Control](/t5/c-khhcw49343/SAP%2BAccess%2BControl/pd-p/01200615320800000796)
* [SAP Process Control

  SAP Process Control](/t5/c-khhcw49343/SAP%2BProcess%2BControl/pd-p/01200314690800000209)

View products (2)

**Introduction:** We might come across data in Access Control and Process Control applications which are relatively old or obsolete in nature and need to be archived to avoid system performance issues when the data volume rises.

The archiving function provides the choice to store away unneeded historical data so that the different features/applications will be able to function more quickly with a reduced dataset. This information is kept in the system, but it can be brought up again by restoring it if required. In this blog, we will keep our focus in archiving data related to Access Requests.

**Step-by-step Procedure:**

Prior to archiving data, we must first identify or create the archiving object. Go to transaction AOBJ and under the node **Archiving Object,** filter for **GR\*** and **SPM\*** using the Position button to find standard archiving objects available for GRC applications.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-46.png)

In this case (GRFND\_A/V8100/SP09), the following archiving objects are available. Since the aim is to archive data related to access requests, **GRFNMSMP** is the object used for this purpose.

**![](/legacyfs/online/storage/blog_attachments/2023/01/Picture2-31.png)**

**![](/legacyfs/online/storage/blog_attachments/2023/01/Picture17-9.png)**

When there is a requirement to archive a specific set of data, just for instance, not all tables configured under the archiving object **GRFNMSMP** are required to be archived, the following sequence of steps can be followed:

Execute transaction AOBJ and create a new object by clicking on New Entries. Enter information like the object name, text, application component information along with the programs for Write, Delete, Reload and/or Read functionalities.

Then go to the Structure Definition sub-dialog and define the structure (tables) that need to be archived. For example:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture3-22.png)

Go to the Customizing Settings sub-dialog and define the archive file ARCHIVE\_DATA\_FILE

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture4-25.png)

Optionally, you can assign a read program to the archive object in the Read Program sub-dialog, if you want to read the archived data. For example:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture5-24.png)

Now, since we have already identified the archiving object GRFNMSMP, double click on the object to validate if the programs for Write, Delete and Reload are already tagged to the object.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture6-17.png)

Providing additional context, Write, Delete, Reload, Read are the steps involved in an archiving process. First, data is written with respect to an archiving object which is then stored based on the parameters defined in the logical filename under Customizing Settings in transaction AOBJ.

Second step is deletion, where the data is deleted from the respective tables included in the archiving object definition.

Reloading is the third step, for reloading the deleted data. However, it is not generally recommended as it might lead to inconsistencies in the system. Alternatively, the archived data can still be read using the program tagged to the object under **Read Programs** in transaction AOBJ as mentioned above, without the need to reload the deleted data.

*Note: Write, Delete, Reload and/or Read activities can also be performed using the Archive Administration tool (transaction **SARA**) provided the archiving object is known already.*

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture8-14.png)

**Write Data of Old Access Requests for Archiving:** Go to transaction SA38 and enter the program GRFNMW\_ARCHIVE\_WRITE as shown above. Run the program in Test mode first to see the expected results. This step will however not result in data deletion and the archived data will still be visible in SAP tables and NWBC screens.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture9-15.png)

Output:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture10-17.png)

**Delete Data of Old Access Requests for Archiving:**

Go to transaction SA38 and enter the program GRFNMW\_ARCHIVE\_DELETE as shown above. Run the program in Test mode first to see the expected results. After executing this step, the archived data will no longer be visible in NWBC screens.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture11-12.png)

Select the sessions to be deleted:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture12-11.png)

Output:

**![](/legacyfs/online/storage/blog_attachments/2023/01/Picture13-11.png)**

**Reload Data of Old Access Requests for Archiving:**

Go to transaction SA38 and enter the program GRFNMW\_ARCHIVE\_RELOAD as shown above. Run the program in Test mode first to see the expected results.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture14-11.png)

Select the archived session to be reloaded and click on Continue:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture15-14.png)

Output:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture16-11.png)

**Conclusion:** Archiving can be an effective way to keep records securely maintained and accessible, with improved storage efficiency, improved security, and easier access to read-on-demand feature. However, to ensure data in...