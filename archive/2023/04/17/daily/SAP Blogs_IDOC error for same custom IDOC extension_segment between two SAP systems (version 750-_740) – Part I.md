---
title: IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) – Part I
url: https://blogs.sap.com/2023/04/16/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems-version-750-740-part-i/
source: SAP Blogs
date: 2023-04-17
fetch_date: 2025-10-04T11:31:56.067987
---

# IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) – Part I

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* IDOC error for same custom IDOC extension/segment ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160674&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [IDOC error for same custom IDOC extension/segment between two SAP systems (version 750->740) - Part I](/t5/technology-blog-posts-by-members/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems/ba-p/13553722)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160674)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160674)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553722)

‎2023 Apr 16
9:45 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160674/tab/all-users "Click here to see who gave kudos to this post.")

2,587

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Master Data Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Master%2520Data%2520Governance/pd-p/67837800100800004488)

* [SAP Master Data Governance

  SAP Master Data Governance](/t5/c-khhcw49343/SAP%2BMaster%2BData%2BGovernance/pd-p/67837800100800004488)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

**Introduction:** I recently experienced a scenario in which we wanted to send data from the SAP MDG (release 750) system to the SAP ECC (release 740) system following an upgrade of the MDG system. There were no problems prior to the upgrade when both SAP systems were on the same release (740).

**Background:** To illustrate the issues and potential fix, I'll use the MATMAS IDOC (Basic Type: MATMAS05) with extension (ZMATMAS05\_EXTENSION) and a single custom segment (Y1MARAM1) that was developed identically in both the SAP systems.

*Scenario 1:* Add new custom fields in the existing custom segments in both the SAP systems, which I'll cover in this blog.

*Scenario 2:* Add new custom segments in the existing IDOC extension in both the SAP systems, which I'll explain in [my next blog](https://blogs.sap.com/2023/04/16/idoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems-version-750-740-part-ii/)(Part II) in detail.

**Scenario 1:** While it is possible to add new fields to the ECC system (in the custom segment in the same release, let's say 740), however, the same fields could not be added in MDG with the older segment version. According to the SAP release strategy, to add new fields to the segments from prior versions, a new version must be created.

SAP MDG system release - 750

![](/legacyfs/online/storage/blog_attachments/2023/04/unnamed2.png)

IDOC Segment release - 740

Additionally, because the system is running on a higher release of 750, we were unable to cancel the release to add new fields.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap397.png)

As a following step, we must add a new version of the same segment (Menu **Segment->Add Version**), then add new fields and release the new version of the segment.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap399-1.png)

In ECC, we had similar IDOC extension and custom segments created in the latest release 740.

So, we added all new fields in custom segment and set the segment as released.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap400.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/snap401.png)

Next, we triggered an IDOC from MDG to ECC which resulted in a syntax error in inbound IDOC and subsequently a posting failure in ECC too though outbound IDOC from MDG was successful.

Outbound IDOC in the MDG system

![](/legacyfs/online/storage/blog_attachments/2023/04/snap402-1.png)

Inbound IDOC in ECC: Error message - EA258: External segment name cannot be interpreted.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap404.png)

While the identical IDOC extension and segments are transferred between two separate SAP systems, the segment definition is taken into account while mapping each field. In this case, the segment definition in MDG is Y1MARAM1001, whereas the segment definition in ECC is Y1MARAM1000. The syntax issue is caused by inbound IDOC's inability to locate segment definition Y1MARAM1001.

To resolve this error, we need to create a new version of the same segment in SAP ECC too like we did in MDG.

However, when we attempt to do so, it issues a warning, stating that we already have a segment definition available in the current release and that we are aware of this. right? Press ENTER once again to create a new version that is identical to MDG.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap406.png)

Only the difference is that we wouldn't be able to release a new version created in the same release. The reason is in one SAP release, we can have only one version released for any segment( custom/standard).

![](/legacyfs/online/storage/blog_attachments/2023/04/snap407.png)

Let's trigger, IDOC from SAP MDG to SAP ECC. Boom!!. IDOC posted successfully in ECC as well!

![](/legacyfs/online/storage/blog_attachments/2023/04/snap408.png)

Now next step is not required but if we want to release new segment definition in ECC, then we need to change it in the SAP standard table EDISDEF-related to the old segment definition (here Y1MARAM1000) - in debug mode.  We can set **Application Release** ( for example 617) and it will allow releasing new segment definition too.

![](/legacyfs/online/storage/blog_attachments/2023/04/snap409.png)

Please keep reading along and leave us any suggestions or comments.

Thanks again for reading the document. I really appreciate your valuable time.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fidoc-error-for-same-custom-idoc-extension-segment-between-two-sap-systems%2Fba-p%2F13553722%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP BusinessObjects Business Intelligence 2025](/t5/technology-q-a/sap-businessobjects-business-intelligence-2025/qaq-p/14234685)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  an hour ago
* [Problems to web build](/t5/technology-q-a/problems-to-web-build/qaq-p/14234583)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-m...