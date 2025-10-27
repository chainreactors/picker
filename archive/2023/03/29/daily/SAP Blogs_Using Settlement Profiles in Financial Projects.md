---
title: Using Settlement Profiles in Financial Projects
url: https://blogs.sap.com/2023/03/28/using-settlement-profiles-in-financial-projects/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:00:46.687705
---

# Using Settlement Profiles in Financial Projects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Using Settlement Profiles in Financial Projects

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51705&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Settlement Profiles in Financial Projects](/t5/enterprise-resource-planning-blog-posts-by-sap/using-settlement-profiles-in-financial-projects/ba-p/13559079)

![helenakray](https://avatars.profile.sap.com/9/2/id92f1ce12ba88dff172b17022599be00677647040e69ccd78882cc15cb6ee4e53_small.jpeg "helenakray")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[helenakray](https://community.sap.com/t5/user/viewprofilepage/user-id/151256)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51705)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51705)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559079)

‎2023 Mar 29
12:04 AM

0
Kudos

2,498

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

View products (1)

If you ever wondered how we can use different Settlement Profiles in Financial Projects Context, you're in the right place. In this Blog, I'll explain step by step how to check the Settlement Profiles and attribute it to a Project / WBS Element.

The Settlement Profiles have many usages, for example, when you would like to close an Internal Project with balance greater than zero (with costs) without running settlement. In this case, you can use a settlement profile **YNS - No Settlement** in order to close this project without errors. Please check if this is allowed in your business context.

To check the existing profiles, you can go to your CBC System and search for Configuration Activity - **Create Settlement Profile**. If you are using "Manage Your Solution", you can search for SSCUI - 105768. Once you enter the configuration, you will be able to see the full list of Settlement Profiles:

![](/legacyfs/online/storage/blog_attachments/2023/03/Create-Settlement-Profile.png)

Figure 1: Create Settlement Profile

Now it's time to link a Settlement Profile to your Project! For that, you can access your Project via "Project Control - Enterprise Projects" and enter the Project / WBS Element. From there, you can click on **Settlement Rule** button:

![](/legacyfs/online/storage/blog_attachments/2023/03/Overhead-Project.png)

Figure 2: Overhead Project

Then, in the header, you can select the Menu -> Goto -> Settlement parameters:

![](/legacyfs/online/storage/blog_attachments/2023/03/Maintain-Settlement-Rules.png)

Figure 3: Maintain Settlement Rule

This is where you will be able to adjust the Settlement Profile, as long as the Allocation Structure and other configurations:

![](/legacyfs/online/storage/blog_attachments/2023/03/Parameters-1.png)

Figure 4: Parameters

The purpose of this blog post is to present you the possibility to adjust the Settlement Profile in accordance to your business requirement in Financial Projects context. In addition to that, you can find more information in SAP Help Portal page: [Settlement](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/d4bfba538c95b54ce10000000a174cb4.html?locale=en-US), you can also follow other contents for [SAP S/4HANA Cloud for Finance](https://answers.sap.com/tags/66233466-fcd6-45d2-a9ae-2cba38c72e19).

Please, feel free to leave your comments or questions. I'll also invite you to follow my profile, for similar content, and make suggestions if you want me to write about another topic related to Controlling for SAP S/4HANA Cloud.

Hope you find this article helpful!

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [settlement profile](/t5/tag/settlement%20profile/tg-p/board-id/erp-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fusing-settlement-profiles-in-financial-projects%2Fba-p%2F13559079%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Unlocking Efficiency: New SAP Signavio Content for Agricultural Origination & Trading](/t5/enterprise-resource-planning-blog-posts-by-sap/unlocking-efficiency-new-sap-signavio-content-for-agricultural-origination/ba-p/14233482)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [Retention Process in SAP Purchase Orders: A Practical Guide](/t5/enterprise-resource-planning-blog-posts-by-members/retention-process-in-sap-purchase-orders-a-practical-guide/ba-p/14212122)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 weeks ago
* [Service Entry Sheet Accruals - Posting and Configurations for SAP S/4HANA 2023](/t5/enterprise-resource-planning-blog-posts-by-members/service-entry-sheet-accruals-posting-and-configurations-for-sap-s-4hana/ba-p/14189510)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Sep 02
* [Public Sector highlights of the SAP Cloud ERP 2508 release](/t5/enterprise-resource-planning-blog-posts-by-sap/public-sector-highlights-of-the-sap-cloud-erp-2508-release/ba-p/14191660)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01
* [Professional Services in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/professional-services-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14202789)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford"...