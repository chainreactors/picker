---
title: PS Easy Cost Planning Integration with S/4HANA Financial Planning
url: https://blogs.sap.com/2022/12/17/ps-easy-cost-planning-integration-with-s-4hana-financial-planning/
source: SAP Blogs
date: 2022-12-18
fetch_date: 2025-10-04T01:51:43.524348
---

# PS Easy Cost Planning Integration with S/4HANA Financial Planning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* PS Easy Cost Planning Integration with S/4HANA Fin...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67290&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [PS Easy Cost Planning Integration with S/4HANA Financial Planning](/t5/enterprise-resource-planning-blog-posts-by-members/ps-easy-cost-planning-integration-with-s-4hana-financial-planning/ba-p/13553744)

![akashkhandelwal368](https://avatars.profile.sap.com/6/2/id62ba5f5c757adeffc1aa9535f6a85cf7d62eba62cb44e14d2cd21607a8fdf330_small.jpeg "akashkhandelwal368")

[akashkhandelwal368](https://community.sap.com/t5/user/viewprofilepage/user-id/403989)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67290)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67290)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553744)

‎2022 Dec 17
11:29 AM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67290/tab/all-users "Click here to see who gave kudos to this post.")

6,438

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [PLM Project System (PS)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Project%2520System%2520%28PS%29/pd-p/653310048283475313268757797580946)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [PLM Project System (PS)

  Software Product Function](/t5/c-khhcw49343/PLM%2BProject%2BSystem%2B%252528PS%252529/pd-p/653310048283475313268757797580946)

View products (2)

Dear Readers,

This Blog will cover End-End cycle including Important Configurations and Demo for PS Easy Cost Planning ( ECP ) Integration with S/4HANA Financial Planning

* As of Version 2022 FPS 00, SAP has provided out-of-box Integration of Project based cost planning integration with Financial Planning for Easy Cost Planning and Network Costing

* Before above mentioned version, we need to use Program (R\_FINS\_PLAN\_TRANS\_CO\_ERP\_2\_S4H) to Transfer the value from Classical CO Table to ACDOCP Table

* With this new version, this manual step is reduced for Easy Cost Planning and Network Costing and now Data will be stored in ACDOCP Table along with Classical CO Table

* With This new feature, couple of Standard Fiori Apps of PS (Project Cost Report - Line Items, Project Cost Report - Overview) can be directly used as far as plan data is concerned.

* This New Feature is part of The Modernized Easy Cost Planning for projects and shall be available as part of S/4HANA perpetual scope

* In this Blog I will be explaining the Easy Cost Planning Integration with Financial Integration

* I assume Readers are aware of Function/Feature of Easy Cost Planning Method and S/4HANA Financial Planning , hence I will be focusing on subject itself.

***Prerequisites :***

1. Necessary Configuration for Easy Cost Planning

2. Maintain Category for Planning

3. Assign Plan Category to CO Version for Easy Cost Planning for Project

Below are couple of important configuration screenshot.

* Maintain Category for Planning

  + System Uses planning category to differentiate sets of plan data

  + Usage 1 is defined for Easy cost planning for Project

![](/legacyfs/online/storage/blog_attachments/2022/12/1-82.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/2-55.png)

* Assign Plan Category to CO Version for Easy Cost Planning for Project

  + To Write Plan Data from ECP to Financial Integration ( CO Table to ACDOCP Table ) this is the new customization introduced

  + This customization is based on CO Area and ECP CO Version

  + Please, note that Once plan category is in use , you can not edit or delete it

![](/legacyfs/online/storage/blog_attachments/2022/12/3-54.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/4-43.png)

***Demo :***

* Perform Easy Cost Planning for Project

![](/legacyfs/online/storage/blog_attachments/2022/12/5-40.png)

* Check Values in CO Table

![](/legacyfs/online/storage/blog_attachments/2022/12/6-34.png)

* Check Values in ACDOCP Table

![](/legacyfs/online/storage/blog_attachments/2022/12/7-28.png)

***Summary***

By using New Standard Configuration of S/4HANA 2022 FPS 00, we are able to Transfer Plan Cost from ECP to ACDOCP Financial Table along with Classical CO Table.

———————————————————————————————————————————-

Please, let me know if anyone have doubt or I missed something.

Your suggestions are most welcome.

Cheers for EPPM Community…!!!

Thanks,

Akash Khandelwal

9 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fps-easy-cost-planning-integration-with-s-4hana-financial-planning%2Fba-p%2F13553744%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [VIM Foundation & Invoice Solution Configuration Overview](/t5/enterprise-resource-planning-blog-posts-by-sap/vim-foundation-amp-invoice-solution-configuration-overview/ba-p/14229743)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Sunday
* [My Learning Journal on BTP (5) - Build A Small Finance Agent: CAP + Generative AI Hub + LangChain](/t5/enterprise-resource-planning-blog-posts-by-sap/my-learning-journal-on-btp-5-build-a-small-finance-agent-cap-generative-ai/ba-p/14222295)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [How to set up Withholding Tax in Treasury Using Extended Withholding Tax](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-set-up-withholding-tax-in-treasury-using-extended-withholding-tax/ba-p/14214462)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Localization in SAP S/4HANA: Strategic Enabler or Deployment Bottleneck?](/t5/enterprise-resource-planning-blog-posts-by-sap/localization-in-sap-s-4hana-strategic-enabler-or-deployment-bottleneck/ba-p/14218573)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://ava...