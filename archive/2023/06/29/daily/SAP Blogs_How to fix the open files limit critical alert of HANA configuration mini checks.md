---
title: How to fix the open files limit critical alert of HANA configuration mini checks
url: https://blogs.sap.com/2023/06/28/how-to-fix-the-open-limits-critical-alert-of-hana-configuration-mini-checks/
source: SAP Blogs
date: 2023-06-29
fetch_date: 2025-10-04T11:47:51.326426
---

# How to fix the open files limit critical alert of HANA configuration mini checks

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to fix the open files limit critical alert of ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163533&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to fix the open files limit critical alert of HANA configuration mini checks](/t5/technology-blog-posts-by-members/how-to-fix-the-open-files-limit-critical-alert-of-hana-configuration-mini/ba-p/13570290)

![Aniket-Nagarkar](https://avatars.profile.sap.com/0/9/id090e25e2164f41d0fae9aefb6eac604a1bbe6b0c2ec62e72dec4b7e5a5b895dc_small.jpeg "Aniket-Nagarkar")

[Aniket-Nagarkar](https://community.sap.com/t5/user/viewprofilepage/user-id/688195)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163533)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163533)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570290)

‎2023 Jun 28
5:34 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163533/tab/all-users "Click here to see who gave kudos to this post.")

2,916

* SAP Managed Tags
* [SUSE Linux Enterprise Server](https://community.sap.com/t5/c-khhcw49343/SUSE%2520Linux%2520Enterprise%2520Server/pd-p/68020287236497694019600446793069)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP NetWeaver](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver/pd-p/01200314690800000134)
* [SAP NetWeaver Application Server for ABAP](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server%2520for%2520ABAP/pd-p/01200314690800000234)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SUSE Linux Enterprise Server

  Operating System](/t5/c-khhcw49343/SUSE%2BLinux%2BEnterprise%2BServer/pd-p/68020287236497694019600446793069)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP NetWeaver

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver/pd-p/01200314690800000134)
* [SAP NetWeaver Application Server for ABAP

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer%2Bfor%2BABAP/pd-p/01200314690800000234)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (6)

Purpose of the blog

To help fixing the open files limit critical alert which comes in the HANA configuration mini checks. I have performed it for the HANA 2.0 SP05 Rev 59 on SLES 15 SP4 and SLES 12 SP4. This alert normally comes when we build the new HANA system or after any OS upgrade. It could lead to VM hung, SAP slowness as the open limits reach to the maximum capacity and can hamper the productivity of your SAP system.

This blog provides step by step procedure on how to resolve and fix the open files limit critical alert.

**Note: Always verify the help.sap.com and your OS vendor support to get the latest updates**

Steps to resolve are as per below

1. Execute the relevant HANA configuration mini checks as per your HANA DB version (download the latest SQL zip file from the SAP note [1969700](https://me.sap.com/notes/1969700), you can mark this SAP note as favourite to see the latest updates always). Once the HANA configuration mini checks are executed, check the results for the critical alerts by applying the filter of X (meaning critical) in the column named C. For e.g. Here CHID M0260 alert is of open files limit critical alert along with few other critical alert.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-8.jpg)

Fig 1. Output of HANA configuration mini checks

2. If there is no critical alert observed for open files limit in the HANA configuration mini checks, then please ignore this blog. But you can still read my blog.

3. If yes, please perform the following steps.

4. According to [https://help.sap.com/docs/SAP\_HANA\_PLATFORM/2c1988d620e04368aa4103bf26f17727/82e4575eec664846a9918e9...](https://help.sap.com/docs/SAP_HANA_PLATFORM/2c1988d620e04368aa4103bf26f17727/82e4575eec664846a9918e9ed1d90d41.html?locale=en-US)

Edit the /etc/security/limits.conf and append the file with the below line:

**sidadm -             nofile   1048576**

The value above is suggested in the HANA mini checks

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-8.jpg)

Fig 2. Configuring /etc/security/limits.conf

5. Login to the OS level of SAP HANA DB and execute the below command using the sidadm user

**bash -c "ulimit -a"**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-5.jpg)

*Fig 3. Check the open files parameter in the output, currently we see it is 1024 which is default*

6. As per the requirement we need to set the open files limit parameters to 1048576.

7. To do so, login using the root user in application host via putty session, go to the path

cd /etc/pam.d/ and create a backup copy of common-session-pc

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-6.jpg)

*Fig 4. Create backup copy of the common-session-pc via root user*

8. Edit the common-session-pc file using vi editor,

Add the below line on top of the file common-session-pc.

Please make sure you don’t make any typo here. As the server can go in inconsistent state and we can’t take the putty session (do ssh to server). To resolve this inconsistent state we require a Linux expert. So please be careful while adding the below line. Double-triple check is recommended.

**session required        pam\_limits.so**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-6.jpg)

*Fig 5. Edit the common-session-pc via root user*

9. Then execute the below command via the root user

**ulimit -n 1048576**

Then switch to sidadm user in the duplicate session and verify the below command

**bash -c "ulimit -a"**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-2.jpg)

*Fig 6. Validate the open files limit*

10. Don’t close the existing session and open the duplicate session and check if the open files limit value is in effect using sidadm

It is not yet over.

Finally take the clean restart of SAP application and HANA DB. Make sure you stop the sapstartsrv service for both SAP application and DB.

After starting the SAP, run the hana mini checks again and see if the open files limit alert.

Now the open files limit alert is no more critical.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture7-2.jpg)

*Fig 7. Executing the SQL query HANA configuration mini check post the configuration and restart of SAP*

This is it, now you are done!

References:

* [https://help.sap.com/docs/SAP\_HANA\_PLATFORM/2c1988d620e04368aa4103bf26f17727/82e4575eec664846a9918e9...](https://help.sap.com/docs/SAP_HANA_PLATFORM/2c1988d620e04368aa4103bf26f17727/82e4575eec664846a9918e9ed1d90d41.html?version=...