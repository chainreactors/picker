---
title: SAP Commissions – Design & Extract Sales Incentive Compensation Plan
url: https://blogs.sap.com/2023/02/26/sap-commissions-design-extract-sales-incentive-compensation-plan/
source: SAP Blogs
date: 2023-02-27
fetch_date: 2025-10-04T08:10:47.795769
---

# SAP Commissions – Design & Extract Sales Incentive Compensation Plan

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions - Design & Extract Sales Incentive...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5974&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions - Design & Extract Sales Incentive Compensation Plan](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-design-amp-extract-sales-incentive-compensation-plan/ba-p/13558328)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5974)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5974)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558328)

‎2023 Feb 26
8:33 PM

[7
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5974/tab/all-users "Click here to see who gave kudos to this post.")

1,424

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (1)

Dear All,

This blog is mainly for SAP Commissions Compensation Admin on how to extract the Compensation Plan Design from your tenant to BTP Portal in one single view.

### Background :

### Sales Incentive Compensation Plan setting by an Organization from Global Sales Leaders or Program Managers takes place in every company.

The goal of setting up a sales rep compensation plan is to motivate sales reps to reach their targets and maximize their Incentive/Commissions. It is important to have a plan that is well-structured and tailored to each individual rep’s strengths and weaknesses.  Also, its been considered on top of geography of the sales area or Market.

The first step to setting up a plan is to create a design document that outlines the objectives of the plan for a **Yearly, Quarterly, Monthly or fortnightly**![](/legacyfs/online/storage/blog_attachments/2023/02/FNFA57_UYAgg9yO.png)
Once finalized, plan document should include the amount of pay each rep will receive, any bonuses or incentives they can earn, and any other perks they can expect to receive. It is important to consider each rep’s individual strengths and weaknesses when creating the design document.

Once the design document is finalized, Comp Admins will design the rule in SAP Commissions according to the finalized document shared by Sales Program Manager or Global Sales Leaders...

This means that you must break down the plan into its individual components and then assign each component a monetary value. This ensures that each rep is compensated appropriately for their efforts.

so the next step is to extract the plan from the document.

The **advantages** of setting up a sales rep compensation plan include giving reps a clear understanding of the goals they are expected to reach and the rewards they can expect to receive if they are successful. This can help to increase morale and motivation, leading to better sales performance. Additionally, it can help to create a more positive work environment as reps know they will be rewarded for their achievement as a payout.

Refer this link for SAP Commissions Dashboard view shows Achievement & Payout Details : [Sales rep Dashboard view](https://blogs.sap.com/2022/03/19/sap-commissions-single-sign-on-authentication-in-ms-teams-tabs/)

---

### Let's Get Started

Once Comp Admins have designed the Compensation Plan which would be seen like as shown in Screenshot.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-26_20-59-18.png)

While this type of request is frequently handled with the Internal Services team, SAP Commissions does not give any out-of-the-box Compensation Plan Summary Detail as an output in a single view.

Hence, in the next section, I will give as little of my development as possible for this request so that you may build in your own way with alternative Ideas with dynamic extraction.

Kindly reach out to SAP Account Executive or CSP or your SAP Implementation Services team for any of your extraction request for Comp Plan Summary.

---

### Extract Plan Design Document through API

```
Request URL: https://tenantid.callidusondemand.com/TrueComp-SaaS/services/rest/exportToXML/getPrepareXML

Request Method: POST

{"beanName":"com.callidus.plan.Plan","shouldExportCurrentEffectiveVersion":false,
"shouldExportVersionInRange":false,"shouldExportAllVersions":true,
"startDate":1641024000000,"endDate":1643702400000,
"beans":["6473924464350791"],"shouldExportRelatedData":true,
"shouldExportVariableAssignments":true,"shouldExportInternalObjects":true,
"shouldExportQuotaCells":true,"locale":"en-US"}
```

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-26_20-32-59.png)
Now, since we got the API endpoint to extract the XML for a Plan which includes all the versions contains the rule and rule elements.

Once XML is generated, you need to convert XML to XSLT and XSLT to HTML or there is also another way XML to JSON and JSON to HTML (whichever is easy for you to do conversion)

Example : <http://makble.com/convert-xml-to-html-with-lxml-xslt-in-python>

<https://www.oxygenxml.com/xml_editor/xml_json_converter.html>

once your code is ready and you can push the code to **SAP BTP Cloud foundry** for getting to Online in One Single page.. so you can circulate the portal to your Global Sales Leaders or Sales Program Managers for usage.

```
cf push spm-plan-extract
```

This is how it looks once pushed to SAP BTP with having all the information about Sales Incentive Plan been designed by Comp Admins.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-26_20-19-55.png)

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [compensationplan](/t5/tag/compensationplan/tg-p/board-id/hcm-blog-sap)
* [payout](/t5/tag/payout/tg-p/board-id/hcm-blog-sap)
* [plans](/t5/tag/plans/tg-p/board-id/hcm-blog-sap)
* [plansummary](/t5/tag/plansummary/tg-p/board-id/hcm-blog-sap)
* [sapcommissions](/t5/tag/sapcommissions/tg-p/board-id/hcm-blog-sap)
* [SPM](/t5/tag/SPM/tg-p/board-id/hcm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fsap-commi...