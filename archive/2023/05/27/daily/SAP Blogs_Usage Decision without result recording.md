---
title: Usage Decision without result recording
url: https://blogs.sap.com/2023/05/26/usage-decision-without-result-recording/
source: SAP Blogs
date: 2023-05-27
fetch_date: 2025-10-04T11:39:46.501647
---

# Usage Decision without result recording

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Usage Decision without result recording

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68259&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Usage Decision without result recording](/t5/enterprise-resource-planning-blog-posts-by-members/usage-decision-without-result-recording/ba-p/13565474)

![SAPFaizan](https://avatars.profile.sap.com/d/9/idd9996722899bead71211066923a1a52cc9aa46da3e258f5bb60dd92271f0d425_small.jpeg "SAPFaizan")

[SAPFaizan](https://community.sap.com/t5/user/viewprofilepage/user-id/160329)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68259)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68259)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565474)

‎2023 May 26
7:58 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68259/tab/all-users "Click here to see who gave kudos to this post.")

5,811

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [PLM Quality Management (QM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Quality%2520Management%2520%28QM%29/pd-p/484135010855456218597016630642366)
* [SAP Quality Issue Resolution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Quality%2520Issue%2520Resolution/pd-p/73555000100700001661)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [PLM Quality Management (QM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BQuality%2BManagement%2B%252528QM%252529/pd-p/484135010855456218597016630642366)
* [SAP Quality Issue Resolution

  Software Product](/t5/c-khhcw49343/SAP%2BQuality%2BIssue%2BResolution/pd-p/73555000100700001661)

View products (3)

In SAP QM, the Usage Decision is a crucial step that determines the fate of inspected materials or products. It involves evaluating the inspection results against predefined acceptance criteria and deciding whether the material meets the required quality standards. Result Recording, on the other hand, involves capturing and documenting individual inspection results for various characteristics or parameters.

UD without Result Recording enables real-time decision-making, allowing organizations to respond promptly to quality issues. Instead of waiting for the completion of result recording, materials can be immediately released for further processing or flagged for corrective actions, reducing delays in production or delivery timelines. This agile decision-making process enhances overall operations.

Follow the below steps:

1. First, we need to remove the QM control key from the material master QM view.

2. Add inspection type **01** in the inspection setup with "**Post to insp stock**" check.

3. Uncheck "**Automatic assignment**" and "**Inspect charcs**".

4. ![](/legacyfs/online/storage/blog_attachments/2023/05/QM-View.jpg)

5. Create PO with this material with stock type Quality inspection.

6. Stock type is also Quality Inspection while doing GR of PO.

7. Check MMBE for verification of stock you will found stock in QI (Quality inspection).

8. Run TCODE **QA32** find inspection lot with status of **REL.**

9. Stock post and take UD without result recording when needed.

Conclusion:

Stock holding or quarantine stock are integral components of quality inspections, playing a vital role in effective quality management. By embracing stock holding and quarantine stock as valuable tools. To save time you can by pass only result recording by above setting in **QM**

Please share your feed back or ask Question to give you more solutions to this and other SAP issues.

Follow me for more SAP related articles

* [sap hana](/t5/tag/sap%20hana/tg-p/board-id/erp-blog-members)
* [sap qm](/t5/tag/sap%20qm/tg-p/board-id/erp-blog-members)
* [sap qm master data](/t5/tag/sap%20qm%20master%20data/tg-p/board-id/erp-blog-members)
* [usage decision](/t5/tag/usage%20decision/tg-p/board-id/erp-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fusage-decision-without-result-recording%2Fba-p%2F13565474%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Unlocking Efficiency: New SAP Signavio Content for Agricultural Origination & Trading](/t5/enterprise-resource-planning-blog-posts-by-sap/unlocking-efficiency-new-sap-signavio-content-for-agricultural-origination/ba-p/14233482)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [Wear Monitoring Measurement Maintenance Plans/Counters](/t5/enterprise-resource-planning-q-a/wear-monitoring-measurement-maintenance-plans-counters/qaq-p/14233085)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Thursday
* [Can you link/join a MATDOC record to the corresponding idoc record](/t5/enterprise-resource-planning-q-a/can-you-link-join-a-matdoc-record-to-the-corresponding-idoc-record/qaq-p/14233006)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [Upgrade Tools & Resources - New Enterprise Support Advisory Council Pilot for Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/upgrade-tools-amp-resources-new-enterprise-support-advisory-council-pilot/ba-p/14221435)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![arghadipkar3013](https://av...