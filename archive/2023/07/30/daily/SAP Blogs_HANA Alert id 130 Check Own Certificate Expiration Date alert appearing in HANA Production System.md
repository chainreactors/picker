---
title: HANA Alert id 130 Check Own Certificate Expiration Date alert appearing in HANA Production System
url: https://blogs.sap.com/2023/07/29/hana-alert-id-130-check-own-certificate-expiration-date-alert-appearing-in-hana-production-system/
source: SAP Blogs
date: 2023-07-30
fetch_date: 2025-10-04T11:52:40.621844
---

# HANA Alert id 130 Check Own Certificate Expiration Date alert appearing in HANA Production System

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* HANA Alert id 130 Check Own Certificate Expiration...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163799&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HANA Alert id 130 Check Own Certificate Expiration Date alert appearing in HANA Production System](/t5/technology-blog-posts-by-members/hana-alert-id-130-check-own-certificate-expiration-date-alert-appearing-in/ba-p/13572115)

![aprao](https://avatars.profile.sap.com/1/d/id1dfd26151ea643961fb2ee8035c2b00e3d17720953e491da3095c658cfaf6311_small.jpeg "aprao")

[aprao](https://community.sap.com/t5/user/viewprofilepage/user-id/139458)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163799)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163799)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572115)

‎2023 Jul 29
1:45 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163799/tab/all-users "Click here to see who gave kudos to this post.")

9,658

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520studio/pd-p/67838200100800004076)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA studio

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bstudio/pd-p/67838200100800004076)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (5)

**HANA Alert id 130 Check Own Certificate Expiration Date alert appearing in HANA Production System**

**Overview**

During system installation, a specific dedicated PKI for external communication is automatically built and enabled. This PKI is integrated with each host on which a database server is  running, as well as with each tenant database in the system.

The tenant-specific certificate authorities (CAs), host-specific X.509 certificates signed by these CAs, private keys, and other components that make up the client PKI are all kept in database collections called certificate collections.

All certificates employ SHA-256 with RSA and a 4096-bit key length as its robust encryption and signature techniques.

As shown below, Click Alerts tab in the HANA Studio, alert message appeared "1 own or chain certificate will expire soon."

![](/legacyfs/online/storage/blog_attachments/2023/07/a1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/a2.jpg)

**Investigation and Finding:**

Login to Tenant Database in Hana studio with  hana DB user SYSTEM or equivalent hana DB user with sufficient privilege.

Execute SQL statement  to check the date of expiration and which certificate as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/07/a3.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/a4.jpg)

As shown above, certificate name is \_SYS\_CLIENTPKI\_HOST\_CERT and the expiration date is 25th Aug 2023.

**Host Certificates**

Host certificates are used to validate  the server's authenticity. The host certificates include all known host names of the SAP HANA servers in the subject alternative names (SAN) field.

A database's host certificates (\_SYS\_CLIENTPKI\_HOST\_CERT) are kept in the database certificate store and given to the \_SYS\_CLIENTPKI certificate collection for SSL purposes.

Host certificates only last 180 days. They are automatically renewed 32 days before expiry, after a restart, and after a host has been added or removed.

The SQL command can also be used to create or generate new host certificates using the statement

*ALTER SYSTEM CLIENTPKI UPDATE CERTIFICATES*.

Check the Hana Parameter [communication] sslclientpki in the global.ini configuration file to ON  before  the update as well as after update to ensure that client PKI is enabled after an update  or trigger the creation of the associated certificates, private keys and certificate collections

![](/legacyfs/online/storage/blog_attachments/2023/07/a5.jpg)

**Procedure**

Execute Update certificates sql statement as follows

![](/legacyfs/online/storage/blog_attachments/2023/07/a6.jpg)

Execute  the SQL command to check the expiration date as shown below

![](/legacyfs/online/storage/blog_attachments/2023/07/a7.jpg)

Check the Hana Parameter [communication] sslclientpki in the global.ini configuration file to ON  after update to ensure that client PKI is enabled after an update  or trigger the creation of the associated certificates, private keys and certificate collections

![](/legacyfs/online/storage/blog_attachments/2023/07/a8.jpg)

Repeat the procedure for SYSTEMDB as shown below.

Before updating certificates execute SQL statements

select \* from CERTIFICATES;

select \* from PSE\_CERTIFICATES;

![](/legacyfs/online/storage/blog_attachments/2023/07/s1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/s2.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/s3.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/s4.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/s5.jpg)

**Conclusion:**

Host certificates automatically renewed 32 days before expiry, after a restart, and after a host has been added or removed.

However, in order to restart HANA instances on the Hana Production Host, we must wait for a customer's clearance.

Therefore, if the customer does not consent to restart the instance, it would be preferable to run Update certificate SQL statement.

Reference:

[3287000 - How to handle HANA Alert 130: 'Check own certificate expiration date' - SAP for Me](https://me.sap.com/notes/0003287000)

Thanks for reading!

Follow for more such posts by clicking on FOLLOW => aprao

Please share your thoughts and feedback on this blog in a comment.

* [1 own or chain certificate will expire soon](/t5/tag/1%20own%20or%20chain%20certificate%20will%20expire%20soon/tg-p/board-id/technology-blog-members)
* [Check Own Certificate Expiration Date](/t5/tag/Check%20Own%20Certificate%20Expiration%20Date/tg-p/board-id/technology-blog-members)
* [HANA Alert id 130](/t5/tag/HANA%20Alert%20id%20130/tg-p/board-id/technology-blog-members)
* [PSE\_CERTIFICATES](/t5/tag/PSE_CERTIFICATES/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/...