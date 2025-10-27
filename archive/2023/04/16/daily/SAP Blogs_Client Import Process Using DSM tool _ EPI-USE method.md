---
title: Client Import Process Using DSM tool / EPI-USE method
url: https://blogs.sap.com/2023/04/15/client-import-process-using-dsm-tool-epi-use-method/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:17.439587
---

# Client Import Process Using DSM tool / EPI-USE method

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Client Import Process Using DSM tool / EPI-USE met...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67055&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Client Import Process Using DSM tool / EPI-USE method](/t5/enterprise-resource-planning-blog-posts-by-members/client-import-process-using-dsm-tool-epi-use-method/ba-p/13550418)

![ashwani1](https://avatars.profile.sap.com/4/e/id4ec9d4c3c6c39b6371890a09043121a2635ae2e0dcd53ecdd9adac30b49f9442_small.jpeg "ashwani1")

[ashwani1](https://community.sap.com/t5/user/viewprofilepage/user-id/219292)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67055)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67055)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550418)

‎2023 Apr 15
7:38 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67055/tab/all-users "Click here to see who gave kudos to this post.")

2,705

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)

View products (1)

**Introduction:**

As I've already covered the complete procedure for carrying out the following activities using EPI-USE approach on my previous blog post.

1. Client Copyback [<Process Overview of Client Refresh using EPI-USE method>](https://blogs.sap.com/2023/04/05/process-overview-of-client-refresh-using-epi-use-method/)

2. Client Export [<Client Export Process- Production Client Data using DSM tool / EPI-USE method>](https://blogs.sap.com/2023/04/12/client-export-process-production-client-data-using-dsm-tool-epi-use-method/)

3. Client Delete [<Client Delete Process Using DSM tool / EPI-USE method](https://blogs.sap.com/2023/04/15/client-delete-process-using-dsm-tool-epi-use-method/)>

Here, I'll discuss how to import production data into quality client. Just so you know that, we require downtime of the target system to accomplish these tasks.

**Execution Steps:** **Phase 6 - Client Import – TARGET (Quality Client) System**

**- Client sync media transfer if necessary**.

If source location is not same in target location, then we need to manually move the export data files into target location.

**- Check permissible directory.**

T-Code: /n/USE/CS

* Click on Environment Menu > Administration

* Click on Permissible Directories

* And then click on Check Permissible Directory

![](/legacyfs/online/storage/blog_attachments/2023/04/1a.jpg)

**- IMPORT client sync grouping file.,** To maintain the list of tables to be included and excluded from Client Sync with the Client Sync Groupings

T-Code: /n/USE/CS

* Click on Environment Menu > Administration

* Select Client Sync Grouping -> Import

* Select the grouping profile, it may be in txt or excel template, you need to select and import it

* After importing click on Save

![](/legacyfs/online/storage/blog_attachments/2023/04/2-10.jpg)

**- DSM Client Sync import of Production data into Quality client.**

T-Code: /n/USE/CS

* Click on Import Sync from File

![](/legacyfs/online/storage/blog_attachments/2023/04/3-11.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/04/4-9.jpg)![](/legacyfs/online/storage/blog_attachments/2023/04/5-12.jpg)

Keep selection check mark as per above screenshot, it may be default selected.

* Click on Execution Options.

* Click Parallel processing and increase some number if background work process is available and click set details.

* Click on Scheduling and click Immediate.

![](/legacyfs/online/storage/blog_attachments/2023/04/6-12.jpg)

* Click on Import Sync, and import process will be started as below

![](/legacyfs/online/storage/blog_attachments/2023/04/7-9.jpg)

Now proceed for next phase 7 as explained in the previous blog [<Process Overview of Client Refresh using EPI-USE method>](https://blogs.sap.com/2023/04/05/process-overview-of-client-refresh-using-epi-use-method/)

**Conclusion:**

Using the EPI-USE/DSM tool, I have discussed client import methods and execution procedures in this blog.

———————-

I hope this blog post is useful to you. Your thoughts and suggestions are welcome.

Thanks for reading this article !

* [CopyClient](/t5/tag/CopyClient/tg-p/board-id/erp-blog-members)
* [DSM Tool](/t5/tag/DSM%20Tool/tg-p/board-id/erp-blog-members)
* [epi-use](/t5/tag/epi-use/tg-p/board-id/erp-blog-members)
* [import](/t5/tag/import/tg-p/board-id/erp-blog-members)
* [Refresh](/t5/tag/Refresh/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fclient-import-process-using-dsm-tool-epi-use-method%2Fba-p%2F13550418%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Japan Bank Charges in Payment Run](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-run/ba-p/14231441)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Regarding the update of business roles](/t5/enterprise-resource-planning-q-a/regarding-the-update-of-business-roles/qaq-p/14231118)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Tuesday
* [Create Professional Service Projects via APIs](/t5/enterprise-resource-planning-blog-posts-by-sap/create-professional-service-projects-via-apis/ba-p/14212432)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Mass Download Of Attachment In SAP Document / Invoice - SAP S4HANA / FICO](/t5/enterprise-resource-planning-blog-posts-by-members/mass-download-of-attachment-in-sap-document-invoice-sap-s4hana-fico/ba-p/14211434)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  4 weeks ago
* [How to Add a Custom OData Field to a Smart Form in Fiori App F1511 using an Adaptation Project?](/t5/enterprise-resource-planning-q-a/how-to-add-a-custom-odata-field-to-a-smart-form-in-fiori-app-f1511-using-an/qaq-p/14207605)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a month ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180ce...