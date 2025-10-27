---
title: Walkthrough of S/4HANA Conversion Project Cycle
url: https://blogs.sap.com/2022/12/17/walkthrough-of-s-4hana-conversion-project-cycle/
source: SAP Blogs
date: 2022-12-18
fetch_date: 2025-10-04T01:51:38.158290
---

# Walkthrough of S/4HANA Conversion Project Cycle

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Walkthrough of S/4HANA Conversion Project Cycle

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67295&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Walkthrough of S/4HANA Conversion Project Cycle](/t5/enterprise-resource-planning-blog-posts-by-members/walkthrough-of-s-4hana-conversion-project-cycle/ba-p/13553799)

![rishi_singh3](https://avatars.profile.sap.com/9/e/id9ee56c2b1343505d8acbe51256c872d20208dacf00df68df2eae54c6f704d5d9_small.jpeg "rishi_singh3")

[rishi\_singh3](https://community.sap.com/t5/user/viewprofilepage/user-id/675993)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67295)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67295)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553799)

‎2022 Dec 17
7:15 PM

[22
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67295/tab/all-users "Click here to see who gave kudos to this post.")

14,041

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP NetWeaver](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver/pd-p/01200314690800000134)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP NetWeaver

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver/pd-p/01200314690800000134)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

View products (6)

Hello, How is everyone doing? I hope all are in good health and always driving towards leanings new things or expanding your horizons.

Today I will be discussing a walkthrough of the project cycle for the S/4HANA conversion project. Sometimes while working on a particular role we miss the bigger picture.

I will be explaining the same with the help of the below diagram which I created myself.

![](/legacyfs/online/storage/blog_attachments/2022/12/S4HANA-conversion-diagram-1-scaled.jpeg)

Let's try to write the project flow in bullet points. Yes, this is quite uncommon but it's good for a person who is trying to understand it.

1. Initially, a request is generated from the vendor that they want their system (ECC) to be converted to S/4HANA.

2. Next in most cases SI partners or SAP consulting firms asset the same and decide if the conversion of their system meets the prerequisites or if any further activities need to be performed before the system is ready.

3. Once the assessment is complete, based on the SAP modules the vendor is using, the team for the S/4HANA conversion project is formed. This will include functional, technical, and management teams.

4. The team is now finalized and the project is kicked off, after doing all the prerequisites.

5. Next BASIS Team implements the readiness check report which informs us on the readiness of the system that needs to move to S/4HANA.

6. Next functional team remediates the Simplification Items checklist. This makes the system ready to adapt S/4HANA changes to the impacted functional areas.

7. Next ABAP team identifies the custom codes which would require remediations once a system is converted, this is due to the changing version of the system itself. Moving from ECC to S/4HANA is not just an upgrade but brings in a new product altogether, that is the reason SAP calls this conversion.

8. Next BASIS team executes the SUM tool which technically converts the system to S/4HANA.

9. But still, finance conversion is not done and this is done post-technical conversion.

10. Once finance conversion is completed, the functional team does the SI validation and reconciliation of the reports that were generated in the pre-converted system.

11. In parallel to it if FIORI was not a part of your previous system, then it's activated and the custom FIORI APP is enabled.

12. ABAP team performs the custom code remediations of the Z and Y objects which they identified before conversion.

13. In parallel BASIS team also performs post-conversion tasks.

14. Finally, the converted S/4HANA system is released for testing.

**Conclusion**

I hope this will give your a high-level idea of the project cycle for S/4HANA conversion. I generally plan my blogs which let us understand the technology in the simplest of language and thoughts.

Happy Learning and please do share your feedback !!

* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-members)
* [s4hana conversion](/t5/tag/s4hana%20conversion/tg-p/board-id/erp-blog-members)
* [SAP S4HANA Conversion](/t5/tag/SAP%20S4HANA%20Conversion/tg-p/board-id/erp-blog-members)
* [SAP S4HANA RIG SAP Readiness Check 2.0 SAP S4HANA Conversion SAP S4HANA Readiness Check](/t5/tag/SAP%20S4HANA%20RIG%20SAP%20Readiness%20Check%202.0%20SAP%20S4HANA%20Conversion%20SAP%20S4HANA%20Readiness%20Check/tg-p/board-id/erp-blog-members)

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fwalkthrough-of-s-4hana-conversion-project-cycle%2Fba-p%2F13553799%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Finance Part2 & Reporting - Bulgaria EUR Transition for S/4HANA Cloud Public Cloud Live Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/finance-part2-amp-reporting-bulgaria-eur-transition-for-s-4hana-cloud/ba-p/14215210)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Selection of optimal scenario for Selective Data Transition to SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-sap/selection-of-optimal-scenario-for-selective-data-transition-to-sap-s-4hana/ba-p/14143325)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 02
* [How to Prepare for SAP S/4 HANA Private Edition Certification (wi...