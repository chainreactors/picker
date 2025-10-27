---
title: Technical Note 2022.003: Updating Fields and Validation Rules for NF-e Model 55
url: https://blogs.sap.com/2023/03/03/technical-note-2022.003-updating-fields-and-validation-rules-for-nf-e-model-55/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:34.541961
---

# Technical Note 2022.003: Updating Fields and Validation Rules for NF-e Model 55

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Technical Note 2022.003: Updating Fields and Valid...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52043&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Technical Note 2022.003: Updating Fields and Validation Rules for NF-e Model 55](/t5/enterprise-resource-planning-blog-posts-by-sap/technical-note-2022-003-updating-fields-and-validation-rules-for-nf-e-model/ba-p/13561923)

![Luize_Boyen](https://avatars.profile.sap.com/3/5/id353948d94af654a2f8134e5dd3f8520e38aa358136ef23a0de8ad99a84bcbbe8_small.jpeg "Luize_Boyen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Luize\_Boyen](https://community.sap.com/t5/user/viewprofilepage/user-id/39112)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52043)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52043)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561923)

‎2023 Mar 03
9:45 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52043/tab/all-users "Click here to see who gave kudos to this post.")

2,494

* SAP Managed Tags
* [SAP S/4HANA Logistics for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Logistics%2520for%2520Brazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization](https://community.sap.com/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

* [SAP S/4HANA Logistics for Brazil

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BLogistics%2Bfor%2BBrazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization

  Topic](/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/03/Technical-Note-EN.png)

Hello everyone,

The Brazilian government has published the technical note 2022.003, which provides new validation rules, as well as changes in the referenced tax document group.

The NF-e technical note includes a new field and validation rules applicable to this field. In this blog post, we will cover updates regarding these changes and SAP Notes relevant to this legal requirement available for SAP S/4HANA and SAP ERP. Click [here](https://blogs.sap.com/2023/03/03/nota-tecnica-2022.003-atualizacao-de-campos-e-regras-de-validacao-da-nf-e-modelo-55/) for the Portuguese version.

## **Changed Fields and Validation Rules**

The new **refNFeSig** field enables the taxpayer to reference the NF-e by informing the access key with a zeroed numeric code (random number). This implies restricting access to information in the nota fiscal, ensuring data secrecy. There are new validation rules that ensure the referenced access key consistency with zeroed numeric code and prevent this referencing from happening on an NF-e with a purpose other than normal (finNFe=1).

The reference by the full access key is still mandatory in cases of return NF-e, complementary NF-e and when required by legal regulations.

One of the changes is related to the number of occurrences of the group of referenced tax documents that previously had a maximum of 500 occurrences and now can have 999 occurrences. This change addresses situations in which more than 500 documents are referenced in the same nota fiscal.

## **New table for Document References**

The **Nota Fiscal Document Reference** (J\_1BNF\_DOCREF) table is available in your system, delivered according to the specifications of the technical note.

You can find the table in the following objects in your system:

* **Nota Fiscal Writer** (J1B\*N) transactions, **External NFe References** table under the **Additional Information** tab of the document

* **Additional Data for Nota Fiscal** (J\_1BNF\_ADD\_DATA) BAdI

* **Nota Fiscal System – Create Object from data** (BAPI\_J\_1B\_NF\_CREATEFROMDATA) BAPI

* **Nota Fiscal: List details of a Nota Fiscal** (BAPI\_J\_1B\_NF\_READDATA) BAPI

The **Document Reference Type** (DOCREF\_TYPE) field defines the confidentiality of the referenced document. You can choose between the values *Standard* or *Confidential* and the **44-Digit Access Key** (ACCESS\_KEY) field stores the access key of the referenced tax document.

The new table allows the reference for external tax documents (notas fiscais that don’t exist in your system). In the case of internal reference (when tax documents are stored in your system), nothing changes as it continues to be as it is today.

Choosing the *Standard* value, inform the complete NF-e access key. By choosing the *Confidential* value, you may inform the NF-e access key with zeroed numeric code (random number) to ensure confidentiality.

When entering a reference as *Confidential*, it goes to the **refNFeSig** field of the XML, but when you enter a reference as *Standard*, it goes to the **refNFe** field.

## **Relevant SAP Notes for this legal requirement**

* SAP Note [3295909](https://launchpad.support.sap.com/#/notes/3295909) – NT 2022.003: Confidential Nota Fiscal References

* SAP Note [3288601](https://launchpad.support.sap.com/#/notes/3288601) – Prerequisite Objects for NT 2022.003: Confidential Nota Fiscal References

SAP Notes for NF-e are planned for March 08.

**Update – March 10, 2023**

ERP NF-e:

* SAP Note [3308184](https://launchpad.support.sap.com/#/notes/3308184) - Outbound NF-e: Technical Note 2022.003

* SAP Note [3309134](https://launchpad.support.sap.com/#/notes/3309134) - Outbound NF-e: Prerequisite objects for SAP Note 3308184

Inbound GRC:

* SAP Note [3309145](https://launchpad.support.sap.com/#/notes/3309145) -  Inbound NF-e: Technical Note 2022.003

Inbound eDocuments:

* SAP Note [3309706](https://launchpad.support.sap.com/#/notes/3309706) - eDocument Brazil Inbound NF-e: Technical Note 2022.003

* SAP Note [3309710](https://launchpad.support.sap.com/#/notes/3309710) - eDocument Brazil Inbound NF-e: Prerequisite objects for SAP Note 3309706

GRC NF-e:

* SAP Note [3290276](https://launchpad.support.sap.com/#/notes/3290276) - NF-e NT2022.003

**Update – March 22, 2023**

* SAP Note [3310241](https://launchpad.support.sap.com/#/notes/3310241) - Prerequisite Objects for NT 2022.003: Confidential Nota Fiscal References BAPI

* SAP Note [3310242](https://launchpad.support.sap.com/#/notes/3310242) - NT 2022.003: Confidential Nota Fiscal References BAPI

Did you like this post? Give it a *Like* and share the content with your colleagues. Feel free to leave feedback, comment, or question in the space below.  And don’t forget to follow [*SAP S/4HANA Logistics for Brazil*](https://blogs.sap.com/tags/ad2381ac-617c-4639-ad63-251765718582/)in the SAP Community to stay tuned for the latest news.

Regards,

Luize Boyen

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [Legal Change](/t5/tag/Legal%20Change/tg-p/board-id/erp-blog-sap)
* [legal change BR](/t5/tag/legal%20change%20BR/tg-p/board-id/erp-blog...