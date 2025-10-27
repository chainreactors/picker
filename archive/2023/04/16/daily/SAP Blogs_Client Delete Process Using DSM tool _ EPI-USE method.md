---
title: Client Delete Process Using DSM tool / EPI-USE method
url: https://blogs.sap.com/2023/04/15/client-delete-process-using-dsm-tool-epi-use-method/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:20.165935
---

# Client Delete Process Using DSM tool / EPI-USE method

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Client Delete Process Using DSM tool / EPI-USE met...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67040&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Client Delete Process Using DSM tool / EPI-USE method](/t5/enterprise-resource-planning-blog-posts-by-members/client-delete-process-using-dsm-tool-epi-use-method/ba-p/13550292)

![ashwani1](https://avatars.profile.sap.com/4/e/id4ec9d4c3c6c39b6371890a09043121a2635ae2e0dcd53ecdd9adac30b49f9442_small.jpeg "ashwani1")

[ashwani1](https://community.sap.com/t5/user/viewprofilepage/user-id/219292)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67040)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67040)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550292)

‎2023 Apr 15
7:21 PM

0
Kudos

1,256

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)

View products (1)

**Introduction:**

As explained the complete process involved in the client copy back [<Process Overview of Client Refresh using EPI-USE method>](https://blogs.sap.com/2023/04/05/process-overview-of-client-refresh-using-epi-use-method/)  and client export [<Client Export Process- Production Client Data using DSM tool / EPI-USE method>](https://blogs.sap.com/2023/04/12/client-export-process-production-client-data-using-dsm-tool-epi-use-method/) using EPI-USE method in my previous blog post. I’ll now go over **Phase 5** of my earlier blog post, which describes how to delete the target client data using the DSM tool. Just so you know, the target system must be offline for the user access for the duration of these entire processes.

The benefit of deleting a client using the EPI-USE approach is that only the client's data will be removed and not client itself. Furthermore, it will be quicker than standard client deletes using tcode SCC5.

**Execution Steps:** **Phase 5 - Client Delete - TARGET (Quality Client) System**

**- Check profile parameter for SAP\* login and change in the value as 0 (zero) if not set.**

T-Code: RZ11

* Check the profile parameter login/no\_automatic\_user\_sapstar = 0

![](/legacyfs/online/storage/blog_attachments/2023/04/1-19.jpg)

Value should be 0 zero, if not set change and activate the parameter.

* Change and activate.

![](/legacyfs/online/storage/blog_attachments/2023/04/2-9.jpg)

**- Take SAP System shutdown/start to activate the profile parameter if you changed.**

After restarting SAP application, the check profile parameter value using TCode: RZ11

![](/legacyfs/online/storage/blog_attachments/2023/04/3-10.jpg)

**- Delete SAP\* user from the client, which you want to delete the client, if required delete from DB level.**

![](/legacyfs/online/storage/blog_attachments/2023/04/4-8.jpg)

**- Now you can perform client delete using EPI-USE method.**

**Caution: Make sure you logged into target client only or else another client will be deleted.**

T-Code: /n/USE/CS

* Click on Client Delete

![](/legacyfs/online/storage/blog_attachments/2023/04/5-11.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/04/6-11.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/04/7-8.jpg)

Here after clicking on Execution. It will popup for client number confirmation, if okay Click on Yes.

![](/legacyfs/online/storage/blog_attachments/2023/04/8-10.jpg)

**Conclusion:**

Using the EPI-USE/DSM tool, I have discussed client data delete methods and execution procedures in this blog.

———————-

I hope this blog post is useful to you. Your thoughts and suggestions are welcome.

Thanks for reading this article !

* [client delete](/t5/tag/client%20delete/tg-p/board-id/erp-blog-members)
* [DSM Tool](/t5/tag/DSM%20Tool/tg-p/board-id/erp-blog-members)
* [epi-use](/t5/tag/epi-use/tg-p/board-id/erp-blog-members)
* [Refresh](/t5/tag/Refresh/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fclient-delete-process-using-dsm-tool-epi-use-method%2Fba-p%2F13550292%23comment-on-this)

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
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  argha...