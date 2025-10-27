---
title: Comparing MD07 – MD04 Vs Monitor material coverage app – 1/2
url: https://blogs.sap.com/2022/12/27/comparing-md07-md04-vs-monitor-material-coverage-app-1-2/
source: SAP Blogs
date: 2022-12-28
fetch_date: 2025-10-04T02:35:58.850250
---

# Comparing MD07 – MD04 Vs Monitor material coverage app – 1/2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Comparing MD07 - MD04 Vs Monitor material coverage...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67680&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Comparing MD07 - MD04 Vs Monitor material coverage app - 1/2](/t5/enterprise-resource-planning-blog-posts-by-members/comparing-md07-md04-vs-monitor-material-coverage-app-1-2/ba-p/13558889)

![Narasimha](https://avatars.profile.sap.com/8/6/id86eeea52b1a32d196fa1a2cdbe4dac2d17041e9b1591b363f2d72303b40bd863_small.jpeg "Narasimha")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Narasimha](https://community.sap.com/t5/user/viewprofilepage/user-id/14917)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67680)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67680)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558889)

‎2022 Dec 27
4:20 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67680/tab/all-users "Click here to see who gave kudos to this post.")

8,310

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [MM Purchasing](https://community.sap.com/t5/c-khhcw49343/MM%2520Purchasing/pd-p/507573428100543543566493124410813)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [MM Purchasing

  Software Product Function](/t5/c-khhcw49343/MM%2BPurchasing/pd-p/507573428100543543566493124410813)

View products (2)

The blog post aims to evaluate the Monitor material coverage app features WRT  classical tools MD04 and MD07 with use cases.

**Use Case 1**: Material type - Raw material, Initial stock -0, No demand or supply elements.

![](/legacyfs/online/storage/blog_attachments/2022/12/2611_01.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2612_02.jpg)

You can select days of supply in the layout, the stock availability graph is shown as above when 0 stock is available in the stock.

**Use Case 2**: Material type - Raw material, Initial stock -0, No supply elements , Demand (safety stock maintained).

![](/legacyfs/online/storage/blog_attachments/2022/12/2612_03.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2612_04.jpg)

Observe Days of supply - This is not matching with MD07. Other data do match. One more observation in the app, if you don't filter the list by the material and go through all the output, you can see that data for the material (days of supply, correctly matches with Md07). Please let me know if you see the same issue on your screens. Apart from this minor issue, the Monitor material coverage app looks visually more appealing and is recommended over MD07 for the following reasons.

1- Create your own layout (Raw material MRP controller, SFG/FG MRP controllers can have their own layout

2- Graphical visibility of shortage (Which can be configured -Like from 21 days to 35 days)

3- Filtering by MRP standard vs filtering by Days of supply (Very useful feature to focus on shortages first), Time till shortage (Comparable to traffic light feature in MD07)

4- You have related actions in the same screen like - Manage material and start a quick MRP run

**Conclusion**: The monitor material coverage app is more visually appealing than MD07. However, some filter options of MD07 are still very useful, and we don't see them in the Monitor material coverage app; hence both need to be used for the time being until we see all the features in the Material coverage app.

Some MD07 features which are still to be seen in Fiori app are

1- Already accessed indicator.

2- Way to manage MRP issues along with the material situation in MD07 (In the material coverage app, we don't have the feature to manage MRP exceptions)

3- MD07 filters (Find materials by various filters, range of coverage, Find exceptions etc.) still need to be fully covered in the Fiori app.

The end users are now finding it useful to browse the app first and then to switch to MD07 and MD04 for detailed analysis.

The next blog will compare these objects when we see some future demand.

* [@Fiori](/t5/tag/%40Fiori/tg-p/board-id/erp-blog-members)
* [Monitor material coverage app](/t5/tag/Monitor%20material%20coverage%20app/tg-p/board-id/erp-blog-members)

32 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fcomparing-md07-md04-vs-monitor-material-coverage-app-1-2%2Fba-p%2F13558889%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Oman localization in SAP S/4HANA Cloud: what matters for Implementation and beyond](/t5/enterprise-resource-planning-blog-posts-by-sap/oman-localization-in-sap-s-4hana-cloud-what-matters-for-implementation-and/ba-p/14215901)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [F0251 / F2101A doesn't display the material's MRP Element](/t5/enterprise-resource-planning-q-a/f0251-f2101a-doesn-t-display-the-material-s-mrp-element/qaq-p/14208591)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a month ago
* [Purchasing Planning Monitor for Collective Evaluation of MRP Planning Results](/t5/enterprise-resource-planning-blog-posts-by-sap/purchasing-planning-monitor-for-collective-evaluation-of-mrp-planning/ba-p/14200697)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 02
* [Dynamic safety stock](/t5/enterprise-resource-planning-blog-posts-by-members/dynamic-safety-stock/ba-p/14186114)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Aug 21
* [Advanced Intercompany Stock Transfer (5HP) in SAP S4HANA Cloud Public Edition](/t5/enterprise-resource-planning-blog-posts-by-sap/advanced-intercompany-stock-transfer-5hp-in-sap-s4hana-cloud-public-edition/ba-p/14178380)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Aug 12

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sa...