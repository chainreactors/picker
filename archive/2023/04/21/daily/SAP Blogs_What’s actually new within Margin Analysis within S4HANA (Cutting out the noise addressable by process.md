---
title: What’s actually new within Margin Analysis within S4HANA (Cutting out the noise addressable by process
url: https://blogs.sap.com/2023/04/20/whats-actually-new-within-margin-analysis-within-s4hana-cutting-out-the-noise-addressable-by-process/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:34.799990
---

# What’s actually new within Margin Analysis within S4HANA (Cutting out the noise addressable by process

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* What’s actually new within Margin Analysis within ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66854&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What’s actually new within Margin Analysis within S4HANA (Cutting out the noise addressable by process](/t5/enterprise-resource-planning-blog-posts-by-members/what-s-actually-new-within-margin-analysis-within-s4hana-cutting-out-the/ba-p/13548072)

![hakim_soni](https://avatars.profile.sap.com/a/9/ida9b71f926dc1f067b73278e6e3f29d19ac8a8eafd5ebf3f71b93ac2142bbec81_small.jpeg "hakim_soni")

[hakim\_soni](https://community.sap.com/t5/user/viewprofilepage/user-id/758354)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66854)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66854)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548072)

‎2023 Apr 20
10:29 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66854/tab/all-users "Click here to see who gave kudos to this post.")

2,643

* SAP Managed Tags
* [FIN Profitability Analysis](https://community.sap.com/t5/c-khhcw49343/FIN%2520Profitability%2520Analysis/pd-p/368252775582391257383490099411464)

* [FIN Profitability Analysis

  Software Product Function](/t5/c-khhcw49343/FIN%2BProfitability%2BAnalysis/pd-p/368252775582391257383490099411464)

View products (1)

**What’s actually new within Margin Analysis within S4HANA (Cutting out the noise addressable by process** **![:winking_face:](/html/@9274F1BDD4BD1647F1AD237FE932AAD6/emoticons/1f609.png ":winking_face:")****:**

Split Profile for cost of goods manufactured / assembled (Goods issues):

* You can have a split profile for the products which you have manufactured or assembled and when those items are issued on sales order it automatically splits the cost based on the relative weight of the cost component structure maintained. This split can only be achieved at the time of billing within cost-based COPA and causing recon issues when the billing happens in a different period to that of good issues.

Deriving characteristic for cost items based on the proportion of revenue (Top-Down Distribution):

* It can assign the characteristic usually onto the relevant cost line automatically in proportion to the revenue, probably this could be done based on the cost line items which are linked to the revenue product on which detailed cost posting has not been maintained

Real time Margin analysis (No need to wait for MEC settlements)

* Settlement rules on WBS and cost centre or internal order can be immediately available for reporting in ACDOCA table at the time of posting itself and do not need to wait for the MEC COPA settlements. However, the characteristic of those COPA dimensions would not available within KE24. They will appear in KE24 only once the MEC COPA settlement has been performed on those objects.

Transfer statistical conditions from SAP SD:

* The statistical pricing condition such as cash discount are taken into Margin analysis. However, this is posted onto a separate ledger for this and not onto the main reporting ledger. Technically you can still achieve this within cost-based COPA.

**Conclusion:**

Agreeing of the functionalities as highlighted above are unique to Margin analysis which is not provided by the cost-based COPA design, and for these specific requirements it might makes sense to make the switch on Margin.

The use case of assignment of characteristic on cost line with top-down distribution can be useful for some business with limitation they have embedded within their processes to gain the split within the cost postings. Real time analysis out from the controlling objects such as WBS, internal orders and cost centres can become useful for analysis and give management the much-needed control and view in real time for appropriate pro-active measures. Given that WBS are very much used as cost buckets on which COPA are being assigned this can be very useful for management. Cost based COPA gives you the split of COGS, but as mentioned above there are recon issues in terms of when it recognises those cost.

Given that Margin analysis is a way forward on product roadmap for SAP, corresponding improvements that will happen on it and cost-based COPA will be phased out of support eventually it makes sense to go with Margin and prepare and plan accordingly surrounding it if you are implementing the module of profitability analysis.

* [Account based COPA vs Costing Based COPA](/t5/tag/Account%20based%20COPA%20vs%20Costing%20Based%20COPA/tg-p/board-id/erp-blog-members)
* [costing based copa](/t5/tag/costing%20based%20copa/tg-p/board-id/erp-blog-members)
* [margin analysis](/t5/tag/margin%20analysis/tg-p/board-id/erp-blog-members)
* [SAP S4 HANA Margin Analysis](/t5/tag/SAP%20S4%20HANA%20Margin%20Analysis/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fwhat-s-actually-new-within-margin-analysis-within-s4hana-cutting-out-the%2Fba-p%2F13548072%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Unlocking Efficiency: New SAP Signavio Content for Agricultural Origination & Trading](/t5/enterprise-resource-planning-blog-posts-by-sap/unlocking-efficiency-new-sap-signavio-content-for-agricultural-origination/ba-p/14233482)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP MDG-M Custom UI Configuration Performance Comparison and Gains](/t5/enterprise-resource-planning-blog-posts-by-members/sap-mdg-m-custom-ui-configuration-performance-comparison-and-gains/ba-p/14209898)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Monday
* [BCWP & BCWS not properly calculated](/t5/enterprise-resource-planning-q-a/bcwp-amp-bcws-not-properly-calculated/qaq-p/14225901)
  in [Enterprise Re...