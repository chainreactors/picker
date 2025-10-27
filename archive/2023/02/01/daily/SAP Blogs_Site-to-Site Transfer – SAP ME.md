---
title: Site-to-Site Transfer – SAP ME
url: https://blogs.sap.com/2023/01/31/site-to-site-transfer-sap-me/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:19:57.132929
---

# Site-to-Site Transfer – SAP ME

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* Site-to-Site Transfer - SAP ME

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1455&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Site-to-Site Transfer - SAP ME](/t5/product-lifecycle-management-blog-posts-by-members/site-to-site-transfer-sap-me/ba-p/13556101)

![sathya77](https://avatars.profile.sap.com/2/0/id209d7543f2eb048192d287f7b093f313b127f87850ee6d20e33334a8a6aab9e0_small.jpeg "sathya77")

[sathya77](https://community.sap.com/t5/user/viewprofilepage/user-id/121142)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1455)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1455)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556101)

‎2023 Jan 31
5:30 PM

[11
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1455/tab/all-users "Click here to see who gave kudos to this post.")

2,488

* SAP Managed Tags
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)

View products (1)

Hello Everyone,

Here in this article, I'd like to walk you through the process of implementing a site-to-site transfer in SAP ME, specifically how data collection results are shared/transferred. And also the SFC numbers and product-related data can be transferred from one site to another. For transferring the SFC details the databases for the source and destination sites can be the same or different.

## **Implementation Considerations**

When you transfer SFC numbers, you must decide:

* Which sites you will transfer SFC numbers from and which sites will receive those SFC numbers.

* At what level the transfer will be defined.

* Whether the SFC numbers you transfer will be ready for consumption or will need further processing (span production).

* Whether the transferred SFC numbers are received automatically or manually at the destination site.

## **Pre-requisites:**

* The following Master Data should exist in both Source and Destination System

  + Material

  + BOM

  + Operations

  + Routings

* Shop Order

**High-Level Overview****:**

**Step 1:** Collaboration Link Maintenance

**Step 2:** System Rule Maintenance

**Step 3:** Site Maintenance

**Step 4:** Shop Order Maintenance

**Step 5:** Export Template Maintenance

**Step 6:** POD

**Step 7:** SFC Receipt

**Detailed Steps:**

**Step 1: Collaboration Link Maintenance**

In *Collaboration Link Maintenance*, you have to map the *COLLABORATION\_SFC\_TRANSFER*  trigger action to the *SITE2SITE* directive.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-1-3.png)

                                                                              *Fig-1*

**Step 2:** **System Rule Maintenance**

In *System Rule Maintenance*, under System Setup, you set the rules Enable SFC Data Transfer and Enable Collaboration Action Messages to “*Yes.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-2.png)*

*Fig-2*

**Step 3:** **Site Maintenance**

SFC numbers to a remote site, you must create the site type as “*Production”* in *Site Maintenance.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-3-1.png)*

*Fig-3*

**Step 4:** **Shop Order Maintenance**

In *Shop Order Maintenance*, on the *Transfer* tab page of the maintenance activity screen where you define SFC number transfer, proceed as follows:

* In the *Transfer Type* field, choose SFC\_CONSUME or SFC\_SPAN to transfer finished SFC numbers for consumption or plan production accordingly.

* Select the *Receive* checkbox if you want to receive the transferred SFC numbers using the *SFC Receipt*activity at the destination site.

* In the *Destination Site* field, enter the destination site.

* In the *Export Template* field, enter the name of the export template.

* In the *Transfer Type*, enter the name of the event that will occur at the destination site after the SFC number has been transferred.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-4.png)

*Fig-4*

**Step 5:** **Export Template Maintenance**

In *Export Template Maintenance* you can either use one of the default export templates or select your own to define what SFC number data should be transferred to the destination site.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-5.png)

*Fig-5*

**Step 6: POD**

On the Active Work List POD, enter the SFC numbers you want to transfer and “Start” the operation and do the “Data Collection”.  Once we complete the SFC, the SFC with the Data Collection will get transferred to the Destination Site.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-6.png)

*Fig-6*

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-8.png)

*Fig-7*

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-8-1.png)

*Fig-8*

![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-9-1.png)

*Fig-9*

**Destination System**

**Step 7: SFC Receipt**

In *SFC Receipt*, enter the SFC number that has been transferred, and click on the retrieve.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-10-1.png)

*Fig-10*

Select the SFC and click on the “Receive” button.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-11.png)

*Fig-11*

In the SFC Report, check whether the SFC is received.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-12.png)

*Fig-12*

In “Data Collection Result Report” enter the SFC and search for the DC Results, the collected DC for the SFC in the source system will be transferred to the Destination System.![](/legacyfs/online/storage/blog_attachments/2023/01/Blog-13.png)

*Fig-13*

**Conclusion:**

The above summarizes the understanding of Site-to-Site Transfer, and I hope that you all understand it.

Thank you for reading the blog post, and stay tuned! to learn more about [SAP Manufacturing and Execution.](https://www.sap.com/products/scm/execution-mes.html)

For further questions related to the blog, please check the [Q&A area](https://answers.sap.com/questions/ask.html), and feel free to post your questions and feedback.

* [sap me](/t5/tag/sap%20me/tg-p/board-id/plm-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fproduct-lifecycle-management-blog-posts-by-members%2Fsite-to-site-transfer-sap-me%2Fba-p%2F13556101%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Why is BOM Header Not Transferred to Project in Auto BOM Transfer (VC / PS Integration)?](/t5/product-lifecycle-management-q-a/why-is-bom-header-not-transferred-to-project-in-aut...