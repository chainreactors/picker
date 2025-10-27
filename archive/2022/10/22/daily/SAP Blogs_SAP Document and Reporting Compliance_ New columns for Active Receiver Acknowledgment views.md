---
title: SAP Document and Reporting Compliance: New columns for Active Receiver Acknowledgment views
url: https://blogs.sap.com/2022/10/21/sap-document-and-reporting-compliance-new-columns-for-active-receiver-acknowledgment-views/
source: SAP Blogs
date: 2022-10-22
fetch_date: 2025-10-03T20:35:36.997163
---

# SAP Document and Reporting Compliance: New columns for Active Receiver Acknowledgment views

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAP Document and Reporting Compliance: New columns...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7780&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Document and Reporting Compliance: New columns for Active Receiver Acknowledgment views](/t5/financial-management-blog-posts-by-sap/sap-document-and-reporting-compliance-new-columns-for-active-receiver/ba-p/13548489)

![BrunoEltz](https://avatars.profile.sap.com/e/c/ideccd6960c67bf5098793434eb575794574737134a3c1f15f72cd75a1154022eb_small.jpeg "BrunoEltz")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[BrunoEltz](https://community.sap.com/t5/user/viewprofilepage/user-id/609531)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7780)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7780)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548489)

‎2022 Oct 21
7:59 PM

[6
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7780/tab/all-users "Click here to see who gave kudos to this post.")

1,282

* SAP Managed Tags
* [SAP S/4HANA Logistics for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Logistics%2520for%2520Brazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [SAP Electronic Invoicing for Brazil (SAP Nota Fiscal Eletronica)](https://community.sap.com/t5/c-khhcw49343/SAP%2520Electronic%2520Invoicing%2520for%2520Brazil%2520%28SAP%2520Nota%2520Fiscal%2520Eletronica%29/pd-p/01200615320800000708)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP Electronic Invoicing for Brazil (SAP Nota Fiscal Eletronica)

  SAP Electronic Invoicing for Brazil](/t5/c-khhcw49343/SAP%2BElectronic%2BInvoicing%2Bfor%2BBrazil%2B%252528SAP%2BNota%2BFiscal%2BEletronica%252529/pd-p/01200615320800000708)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Logistics for Brazil

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BLogistics%2Bfor%2BBrazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)

View products (5)

Hi everyone,

Currently, the SAP Document and Reporting Compliance, inbound invoicing option for Brazil provides a configuration view for activating Receiver Acknowledgment solution (Manifestação do Destinatário) as a business' requirement. Nevertheless, in case of issues in the documents receiving, customers don't know the quantity of XML pending download and the reason for that.

To address this issue, the new Log and Total Documents columns were included in the **NF-e: Active Receiver Acknowledgment** and **CT-e: Active Documents** views.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-67-1.png)

The new columns provide details about the latest XML files downloaded from SEFAZ:

* The 'Total docs' column presents the number of documents pending download;

* The 'Log' column allows customers to access the available logs for the given CNPJ. A pop-up dialog is opened and informs the action required by the customer to continue downloading XML files.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-48-1.png)

You can check the new solution for Receiver Acknowledgment SAP Notes for further details:

* [3254999](https://i7p.wdf.sap.corp/sap/support/notes/3254999) - eDocument Brazil Inbound NF-e: Prerequisite objects for SAP Note 3255000.

* [3255000](https://i7p.wdf.sap.corp/sap/support/notes/3255000) - eDocument Brazil Inbound NF-e: Manifesto Resilience.

Don’t hesitate to check out this new feature and enhance your distribution control!

Like that post? Give it a Like and share the content with your colleagues.

Follow my profile for similar content. Please share your feedback, thoughts, or questions in the space below.

Don’t forget to follow the SAP Electronic Invoicing for Brazil (SAP Nota Fiscal Eletronica <https://blogs.sap.com/tags/01200615320800000708/> ) tag in the SAP Community to stay tuned in the latest news about NF-e.

Best regards,

Bruno Eltz

Labels

* [Product Updates](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap/label-name/product%20updates)

* [Cloud NF-e](/t5/tag/Cloud%20NF-e/tg-p/board-id/financial-management-blog-sap)
* [nfe](/t5/tag/nfe/tg-p/board-id/financial-management-blog-sap)
* [nota fiscal eletronica](/t5/tag/nota%20fiscal%20eletronica/tg-p/board-id/financial-management-blog-sap)
* [SAP Document and Reporting Compliance](/t5/tag/SAP%20Document%20and%20Reporting%20Compliance/tg-p/board-id/financial-management-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-sap%2Fsap-document-and-reporting-compliance-new-columns-for-active-receiver%2Fba-p%2F13548489%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Introducing Carbon Accounting for Sustainability with SAP](/t5/financial-management-blog-posts-by-sap/introducing-carbon-accounting-for-sustainability-with-sap/ba-p/14231500)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  Tuesday
* [ACR – Business Partner Email Recipient Not Pulled in Statutory Report Distribution](/t5/financial-management-q-a/acr-business-partner-email-recipient-not-pulled-in-statutory-report/qaq-p/14229778)
  in [Financial Management Q&A](/t5/financial-management-q-a/qa-p/financial-management-questions)  Sunday
* [Do We Need a Separate Company Code for Hungarian Subsidiary?](/t5/financial-management-q-a/do-we-need-a-separate-company-code-for-hungarian-subsidiary/qaq-p/14223947)
  in [Financial Management Q&A](/t5/financial-management-q-a/qa-p/financial-management-questions)  2 weeks ago
* [Implementation of a taxable entity across system boundaries (public cloud ↔ private cloud) using DRC](/t5/financial-management-q-a/implementation-of-a-taxable-entity-across-system-boundaries-public-cloud/qaq-p/14222602)
  in [Financial Management Q&A](/t5/financial-management-q-a/qa-p/financial-management-questions)  ...