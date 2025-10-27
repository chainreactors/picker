---
title: How to filter on several Line Manager or HR Manager teams in Compensation Executive Review
url: https://blogs.sap.com/2023/02/21/how-to-filter-on-several-line-managers-or-hr-managers-teams-in-compensation-executive-review/
source: SAP Blogs
date: 2023-02-22
fetch_date: 2025-10-04T07:42:27.101214
---

# How to filter on several Line Manager or HR Manager teams in Compensation Executive Review

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* How to filter on several Line Manager or HR Manage...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5898&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to filter on several Line Manager or HR Manager names in Compensation Executive Review](/t5/human-capital-management-blog-posts-by-sap/how-to-filter-on-several-line-manager-or-hr-manager-names-in-compensation/ba-p/13554804)

![xavierlegarrec](https://avatars.profile.sap.com/e/1/ide191ffbd1506acbea27fa713f7d40cc166155c1a67fd472acb8c46fa0863e44a_small.jpeg "xavierlegarrec")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[xavierlegarrec](https://community.sap.com/t5/user/viewprofilepage/user-id/20879)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5898)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5898)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554804)

‎2023 Feb 21
11:45 PM

[8
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5898/tab/all-users "Click here to see who gave kudos to this post.")

2,174

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)

* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)

View products (1)

**Introduction**

It may seem like something easy to do but depending on the configuration of an environment it can be difficult to build a filter in Compensation Executive review that allows us to filter on several manager **names** (not ID) that are not connected through a reporting line, for the following reasons :

* The Executive Review doesn't offer anything in standard to do this : we can only filter on one manager name or HR manager name at the time and then decide which levels below them in the reporting line we want to show.

* Username columns that show the name of a manager on the worksheet when mapped to EC Category = Job Info > Supervisor or EC Category = Job Info > HR manager job relationship are not yet supported in Executive Review and will not show in filter selection.

* We can try mapping a custom column of type "string" to EC Category = Employee Profile > Manager and another column to EC Category = Employee Profile > HR manager but we found after testing that it doesn't return the name of the manager in all environments (sometimes it returns the ID and we are still trying to troubleshoot what is causing this). We recommend trying this solution (which is by far the easiest - when it's working) and if it returns the ID of the manager and not the name then please follow guidance below.

**Solution that always works**

In this 20 minutes recording we show how to build a custom MDF object that allows planners and administrators to filter in Compensation Executive Review on several Line Managers or HR Managers (and by using their name vs userID) that are not in the same reporting line, which is not possible yet using standard tools.

The recording covers the following steps :

1. The creation of a custom MDF object (with externalCode=User so it can be used in Compensation) that will store the managers' names.

2. The creation of a business rule that populates the managers' names on save.

3. The creation of an integration center job that automatically captures changes on a daily basis thanks to a scheduled job.

4. How to link the MDF values to compensation template columns.

5. How to filter once the workaround is in place.

<https://youtu.be/T1prZbvs4s0>

**Conclusion**

Not only does this solution always work but it also allows us to create deep job relationship filters, for example if we want to see on the worksheet who is a person's "Level 3 manager" or "Level 4 manager" we can do so by creating the appropriate new field in the custom MDF object and then by nesting the mapping in the On Save business rule of the MDF object (Example for level 3 : Job Info > Supervisor > Job Info > Supervisor > Job Info > Supervisor.name).

--

All the best

Xavier

*(If you found this blog useful please consider giving it a Like)*

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [business rule on MDF object](/t5/tag/business%20rule%20on%20MDF%20object/tg-p/board-id/hcm-blog-sap)
* [Compensation Executive Review](/t5/tag/Compensation%20Executive%20Review/tg-p/board-id/hcm-blog-sap)
* [custom MDF object](/t5/tag/custom%20MDF%20object/tg-p/board-id/hcm-blog-sap)
* [executive review enhanced filters](/t5/tag/executive%20review%20enhanced%20filters/tg-p/board-id/hcm-blog-sap)
* [filter on several HR managers](/t5/tag/filter%20on%20several%20HR%20managers/tg-p/board-id/hcm-blog-sap)
* [filter on several managers](/t5/tag/filter%20on%20several%20managers/tg-p/board-id/hcm-blog-sap)
* [Integration Center](/t5/tag/Integration%20Center/tg-p/board-id/hcm-blog-sap)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fhow-to-filter-on-several-line-manager-or-hr-manager-names-in-compensation%2Fba-p%2F13554804%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enhancement Request: Duplicate Workflow Approvers](/t5/human-capital-management-q-a/enhancement-request-duplicate-workflow-approvers/qaq-p/14224097)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2 weeks ago
* [EU Pay Transparency in SAP SuccessFactors — A Suite-Level Compliance Playbook](/t5/human-capital-management-blog-posts-by-members/eu-pay-transparency-in-sap-successfactors-a-suite-level-compliance-playbook/ba-p/14223230)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago
* [2H 2025 SuccessFactors Release Schedule](/t5/human-capital-management-q-a/2h-2025-successfactors-release-schedule/qaq-p/14222284)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2 weeks ago
* [Adjustment field view access for managers & for HR edit access in Compensation worksheet](/t5/human-capital-management-q-a/adjustment-field-view-access-for-managers-amp-for-hr-edit-access-in/qaq-p/14214935)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  3 weeks ago
* [Complete Guide to Setting Up Story Reports in SAP Succ...