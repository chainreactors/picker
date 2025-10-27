---
title: How to audit SAP S/4HANA Cloud
url: https://blogs.sap.com/2022/10/25/how-to-audit-sap-s-4hana-cloud-2/
source: SAP Blogs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:22.324198
---

# How to audit SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to audit SAP S/4HANA Cloud (Part 1.1)

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67099&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to audit SAP S/4HANA Cloud (Part 1.1)](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-audit-sap-s-4hana-cloud-part-1-1/ba-p/13551251)

![christinadeloitte](https://avatars.profile.sap.com/b/3/idb3ef4ca4a9ad6998b0420a97356b51d5a2294b6b34839db388b308e8860a8f3b_small.jpeg "christinadeloitte")

[christinadeloitte](https://community.sap.com/t5/user/viewprofilepage/user-id/784762)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67099)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67099)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551251)

‎2022 Oct 26
12:07 AM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67099/tab/all-users "Click here to see who gave kudos to this post.")

3,664

* SAP Managed Tags
* [Governance, Risk, Compliance (GRC) and Cybersecurity](https://community.sap.com/t5/c-khhcw49343/Governance%252C%2520Risk%252C%2520Compliance%2520%28GRC%29%2520and%2520Cybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

* [Governance, Risk, Compliance (GRC) and Cybersecurity

  Product Category](/t5/c-khhcw49343/Governance%25252C%2BRisk%25252C%2BCompliance%2B%252528GRC%252529%2Band%2BCybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

View products (3)

[*Two-thirds of the Earth’s surface is covered with water. The other third is covered with auditors fr...*](https://www.azquotes.com/quote/984927?ref=auditors)*”*
– [Norman Ralph Augustine](https://www.azquotes.com/author/662-Norman_Ralph_Augustine) –

1. **Introduction**

**1.1. Legal and Regulatory Requirements – Local GAAP**

The IT-Audit procedures described in this blog posts are intended as a guidance for an IT-Auditor familiar with both, SAP ERP systems and with knowledge of the legal requirements for IT-Audits as part of the annual year-end audit. This is a prerequisite to understand the blog posts.

The blog posts are neither legally binding nor a mandatory guideline or standard and solely serve as an orientational guidance. Any responsibility for the type, scope, and results of external and internal audits remains with the auditor. It is also the auditor's responsibility to define the selected key audit areas in accordance with relevant regulations and standards.

Generally, when conducting IT-Audits as part of the annual year-end audit, certain provisions and guidelines apply. As an example, here are some applicable German guidelines:
Statutory commercial and tax law provisions (§§ 238 et seq. German Commercial Code (Handelsgesetzbuch, "HGB") and §§ 140 - 148 German Fiscal Code (Abgabenordnung, "AO"));

+ Generally accepted accounting principles (Grundsätze ordnungsmäßiger Buchführung, "GoB");

+ The Letter of the Federal Minister of Finance dated 28. November 2019 „Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff“ (GoBD), broadly translated as “Principles of proper electronic bookkeeping and storage of financial statements as well as commercial documents and of their retrieval”;

+ Accounting publication by the Select Committee for Information Technology (Fachausschuss für Informationstechnologie, "FAIT") of the German Institute of Auditors (Institut der Wirtschaftsprüfer in Deutschland e.V., "IDW") entitled "Principles of proper accounting in connection with the use of information technology" (Grundsätze ordnungsmäßiger Buchführung bei Einsatz von Informationstechnologie, "IDW RS FAIT 1");

+ Principles of proper accounting in connection with the use of electronic archiving systems (Grundsätze ordnungsmäßiger Buchführung beim Einsatz von Archivierungssystemen, “IDW RS FAIT 3”);

+ IDW auditing standard „Project related audit using information technology" (Projektbegleitende Prüfung bei Einsatz von Informationstechnologie IDW PS 850).

+ Processes and Functions, including Cloud Computing“ (IDW RS FAIT 5)

Similar guidelines and standards are in place for most countries. In addition to the general audit guidelines, specific requirements for software operated in the cloud apply. Furthermore, multiple frameworks try to address cloud risks, among them are, as an example, CSA Cloud Controls Matrix, ISO 27001, COBIT 5, Consensus Assessments Initiative Questionnaire (CAIQ), Payment Card Industry Data Security Standard (PCI-DSS), National Institute of Standards in Technology (NIST) 800-53 and – as mentioned above - IDW RS FAIT 5. The following figure illustrates how IDW RS FAIT 5 accounts for different complexity levels of IT outsourcing:

![](/legacyfs/online/storage/blog_attachments/2022/10/Cloud-Computing.png)

Besides the type of outsourcing, IDW RS FAIT 5 also classifies outsourcing projects by the underlying provider model:

+ Public Cloud: All outsourcing companies have access to services.

+ Private Cloud: Only one particular outsourcing company (group) has access to the services.

+ Hybrid Cloud: Hybrid form consisting of a combination of the above mentioned models.

Furthermore, IDW RS FAIT 5 defines four phases of an outsourcing projects and the corresponding requirements for each phase. Lifecycle according to IDW RS FAIT 5:

![](/legacyfs/online/storage/blog_attachments/2022/10/Lifecycle-according-to-IDW-RS-FAIT-5.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Lifecycle-according-to-IDW-RS-FAIT-5-c_2.png)

**Engage with us**

To read all upcoming posts in this series, please follow the [S4HANACloud audit](https://community.sap.com/t5/tag/S4HANACloud%20audit/tg-p/board-id/erp-blog-sap) tag we’ve created for this purpose.

Or contact us on LinkedIn.

**Your feedback**

Feel free to share your feedback and thoughts in the comment section below.

### **Who we are**

This blog is written by:

|  |  |
| --- | --- |
| ![](/legacyfs/online/storage/blog_attachments/2022/10/MEms_BusinessPortrait_Small.jpg) | **Matthias Ems (SAP) –***Business Information Security Officer SAP S/4HANA and Chief Security Product Owner S/4HANA*  With more than 20 years of experience in SAP Security, Auditing and Compliance, Matthias leads a team of Security Experts, responsible for Cloud Operations Security, Secure Development, Data Protection & Privacy and Security Attestation & Certification. |
| ![](/legacyfs/online/storage/blog_attachments/2022/10/Florian_Portrait-scaled.jpg) | **Florian Eller (SAP) –***Product Management SAP S/4HANA Security*  Florian has more than 15 years of expe...