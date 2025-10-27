---
title: IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) – Part II
url: https://blogs.sap.com/2023/04/16/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems-version-750-740-part-ii/
source: SAP Blogs
date: 2023-04-17
fetch_date: 2025-10-04T11:31:53.510944
---

# IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) – Part II

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* IDOC error for same custom IDOC extension/segment ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160684&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) - Part II](/t5/technology-blog-posts-by-members/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems/ba-p/13553885)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160684)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160684)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553885)

‎2023 Apr 16
11:47 PM

0
Kudos

1,674

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Master Data Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Master%2520Data%2520Governance/pd-p/67837800100800004488)

* [SAP Master Data Governance

  SAP Master Data Governance](/t5/c-khhcw49343/SAP%2BMaster%2BData%2BGovernance/pd-p/67837800100800004488)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

**Introduction:** In my [previous blog](https://blogs.sap.com/2023/04/16/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems-version-750-740-part-i/), I explained a scenario in which we needed to add new fields in a custom segment of the IDOC in two SAP systems while both systems are on different releases. It is mention to worth it that there were no problems before the upgrade when both SAP systems were on the same release (740).

In this article, I'll cover how to add new segments in the same IDOC basic type and custom extensions in SAP MDG(750) and SAP ECC(740).

**Background:** To illustrate the issues and potential fix, I’ll use the MATMAS IDOC (Basic Type: MATMAS05) with extension (ZMATMAS05\_EXTN) and a single custom segment (Y1MARAM1) that was developed identically in both the SAP systems.

So let's get started.

While it is possible to add new segments to the ECC system (in the custom extension in the same release, let’s say 740), however, the same segments could not be added in MDG with the older extension version. According to the SAP release strategy, to add new segments to the IDOC extension from prior versions, a successor extension must be created.

SAP MDG system release – 750

![](/legacyfs/online/storage/blog_attachments/2023/04/unnamed2-1.png)

IDOC Extension release – 740

It is not advisable to cancel the release which is from the previous SAP release.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap410.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/snap415.png)

In this scenario, we need to create a new successor extension ( let's say ZMATMAS05\_EXTN\_750) of an existing extension(ZMATMAS05\_EXTN) in the MDG system, add a new segment (Y1MARAM1\_NEW ) and release the segment and the new extension.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap418.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/snap411-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/snap412-1.png)

Change ABAP code when passing CIMTYP (new extension ZMATMAS05\_EXTN\_750) for IDOC extension in the MDG system.

Next, we need to maintain Output types and IDOC type/extension in T-code WE82

![](/legacyfs/online/storage/blog_attachments/2023/04/snap413.png)

And in WE20 for the outbound partner profile - Add extension ZMATMAS05\_EXTN\_750

![](/legacyfs/online/storage/blog_attachments/2023/04/snap414.png)

Now we will log in to the ECC system and will create the same replica as the MDG ones. So we will create one successor extension and a new segment. We can release the segment but not the extension ZMATMAS05\_EXTN\_750 following the SAP basic release concept ( We can’t have two released extensions in the same release, here 740).

![](/legacyfs/online/storage/blog_attachments/2023/04/snap419.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/snap420.png)

In T-code **WE82**: Add Message type, Basic type, and new extension ZMATMAS05\_EXTN\_750, same as MDG.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap416.png)

In T-code **WE57**: Add an entry for FM (for Inbound IDOC processing) against message type, basic type, and new extension ZMATMAS05\_EXTN\_750.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap417.png)

This completes the configuration and now IDOC is ready to be sent over from MDG to ECC and will be posted successfully in ECC.

Now next step is not required but if we want to release new extension in ECC, then we need to change it in the SAP standard table EDCIM-related to the old extension (here ZMATMAS05\_EXTN) – in debug mode.  We can set **Application Release** ( for example 617) and it will allow releasing new extension( ZMATMAS05\_EXTN\_750 ) too.

I sincerely hope you enjoyed reading this article. Please continue reading. I value your opinions and recommendations at any moment. And, once again, thank you for your time.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fidoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems%2Fba-p%2F13553885%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP BusinessObjects Business Intelligence 2025](/t5/technology-q-a/sap-businessobjects-business-intelligence-2025/qaq-p/14234685)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  an hour ago
* [Problems to web build](/t5/technology-q-a/problems-to-web-build/qaq-p/14234583)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Deploy Your First SAPUI5 App : CF deployed mtar results in 500 Internal Server Error](/t5/technology-q-a/deploy-your-first-sapui5-app-cf-deployed-mtar-results-in-500-internal/qaq-p/14234214)
  i...