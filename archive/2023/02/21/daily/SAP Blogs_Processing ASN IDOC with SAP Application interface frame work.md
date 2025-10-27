---
title: Processing ASN IDOC with SAP Application interface frame work
url: https://blogs.sap.com/2023/02/20/processing-asn-idoc-with-sap-application-interface-frame-work/
source: SAP Blogs
date: 2023-02-21
fetch_date: 2025-10-04T07:37:15.503029
---

# Processing ASN IDOC with SAP Application interface frame work

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Processing ASN IDOC with SAP Application interface...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160070&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Processing ASN IDOC with SAP Application interface frame work](/t5/technology-blog-posts-by-members/processing-asn-idoc-with-sap-application-interface-frame-work/ba-p/13550087)

![Riaz-Ahammed](https://avatars.profile.sap.com/a/c/idacb914bc2d2fc0d48bd5bfee02ff5fbc906002661716bf1952225ec0c12c1ff6_small.jpeg "Riaz-Ahammed")

[Riaz-Ahammed](https://community.sap.com/t5/user/viewprofilepage/user-id/124174)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160070)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160070)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550087)

‎2023 Feb 20
8:53 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160070/tab/all-users "Click here to see who gave kudos to this post.")

8,139

* SAP Managed Tags
* [SAP Application Interface Framework](https://community.sap.com/t5/c-khhcw49343/SAP%2520Application%2520Interface%2520Framework/pd-p/01200314690800001892)

* [SAP Application Interface Framework

  SAP Application Interface Framework](/t5/c-khhcw49343/SAP%2BApplication%2BInterface%2BFramework/pd-p/01200314690800001892)

View products (1)

I read many SDN blogs on SAP AIF interfaces and its concepts. Based on the knowledge acquired from multiple blogs, I am writing this article in step wise by simplifying, implementing many of AIF features in one valid business case and to allow readers to get quick idea of SAP AIF interface implementation. Thank you michal.krawczyk2 for all your effort and sharing knowledge through various blogs.

***Business case***: Supplier uses Advanced shipment notification (ASN) document to inform customer that he or she has sent the customer a delivery. Assuming this document sent in IDOC format to create inbound delivery in SAP. SAP application interface frame work to be used for processing these ASN inbound IDOC’s and monitoring its success and error IDOC postings by vendors, materials etc. Following is the step wise approach to process ASN IDOC within SAP AIF and how it allowed us, to use standard SAP AIF monitoring transaction **/AIF/ERR** for it.

1. Create namespace for grouping of interfaces and to control accessing it. Use transaction code /AIF/CUST for it.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-14.png)

Config path 1

e.g. Created ZP2P Namespace to group all interfaces relevant to P2P scenarios

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture7-12.png)

Namespace

2. For inbound ASN IDOC basic idoc type is DELVRY07 and valid message type is DESADV. Using Basic IDOC type and message type generate interface structure from transaction code /AIF/IDOC\_GEN. Here i took IDOC process scenario 2 for processing idoc’s within SAP AIF. Input selection field entries appear as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture8-11.png)

AIF Interface Generator

After successful execution, AIF IDOC interface structure ZP2P\_AIF\_ASN generated and assigned to our interface IN\_ASN.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture9-8.png)

AIF Interface structure

Assignment of ASN\_IN interface generated to the name space ZP2P.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture10-7.png)

AIF Interface Config path

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture11-10.png)

AIF Interface

Interface engine generated; Our ASN interface should be able to process IDOC within SAP AIF, update additional index tables for more specific selection of idoc segment fields and to provide log of it.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture12-10.png)

Interface engine - Config path

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture13-10.png)

Interface engine

3. Assign IDOC type DELVRY07 and Message type DESADV to the interface ASN\_IN; I used message function to process ASN IDOC’s always in SAP AIF.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture14-9.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Picture15-10.png)

4. Define action ZP2P\_ASN\_PROCESS and assignment to interface IN\_ASN; This allows interface to process ASN idoc

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture19-8.png)

Define Action

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture20-8.png)

Define Action

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture21-6.png)

Action - SAP Config path

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture22-5.png)

Action assignment

5. Function module ZP2P\_AC\_ID\_CREATE created and assigned to action ZP2P\_ASN\_PROCESS

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture23-4.png)

FM Assignment to Action

Create custom function group ZP2P\_AIF and function module ZP2P\_AC\_ID\_CREATE assign to action ZP2P\_ASN\_PROCESS.

Standard SAP uses FM /SPE/IDOC\_INPUT\_DESADV1 for ASN Idoc postings. Code implementation for our FM ZP2P\_AC\_ID\_CREATE as follows.

To call IDOC posting FM '/SPE/IDOC\_INPUT\_DESADV1'

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture24-4.png)

FM for Action

6. Use transaction WE57 to create entry for assignment of ASN inbound idoc messages to process within SAP AIF.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture25-7.png)

7. Create custom process code ZDLS from Transaction WE42

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture26-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture27-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture28-4.png)

8. Maintain partner profile from transaction code WE20

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture29-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture30-4.png)8. Creation of custom single index table ZP2P\_ID\_INX\_SGL with fields VBELN and LIFEX; This single-index table used for saving message processing information along with ASN document header level index fields in AIF.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture31-5.png)

9. Creation of custom multi-index table ZP2P\_ID\_INX\_MUL; This multi-index table used for saving message processing information along with ASN document item level index fields in AIF.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture32-2.png)

10. Create ZP2P\_AIF\_SEL\_SCREEN module pool program for custom selection subn monitoring and error handling.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture33-3.png)

11. Assign custom tables ZP2P\_ID\_INX\_SGL and ZP2P\_ID\_INX\_MUL and custom

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture34-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture35-2.png)

12. Selection screen inputs for search assignment to interface

![](/legacyfs/online/storage/blog_attachments/202...