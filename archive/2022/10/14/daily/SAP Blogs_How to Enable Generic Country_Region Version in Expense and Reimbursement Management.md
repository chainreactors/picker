---
title: How to Enable Generic Country/Region Version in Expense and Reimbursement Management
url: https://blogs.sap.com/2022/10/13/how-to-enable-generic-country-region-version-in-expense-and-reimbursement-management/
source: SAP Blogs
date: 2022-10-14
fetch_date: 2025-10-03T19:49:50.875156
---

# How to Enable Generic Country/Region Version in Expense and Reimbursement Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to Enable Generic Country/Region Version in Ex...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/48760&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Enable Generic Country/Region Version in Expense and Reimbursement Management](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-enable-generic-country-region-version-in-expense-and-reimbursement/ba-p/13538449)

![former_member39830](https://avatars.profile.sap.com/former_member_small.jpeg "former_member39830")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[former\_member39830](https://community.sap.com/t5/user/viewprofilepage/user-id/39830)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=48760)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/48760)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13538449)

‎2022 Oct 13
9:33 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/48760/tab/all-users "Click here to see who gave kudos to this post.")

1,333

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

This blog explains how to create a country/region version based on a generic template and then configure it to meet the country/region-specific requirements if you need a version that is not covered by the standard country/region scope of SAP Business ByDesign Expense and Reimbursement Management (ERM).

### **Prerequisites**

* You have already included *Travel & Expense Reimbursement* in your solution scope.

* To use generic country/region version features for ERM, you must hire an employee. In case employee is from non-localized country/region, check the blog on [Administering and Maintaining Employees in Non-Localized Countries/Regions](https://blogs.sap.com/2022/10/12/administering-and-maintaining-employees-in-non-localized-countries-regions/)

### **Steps**

Following are the steps to enable generic country/region Versions in Expense and Reimbursement Management:

1. Enable the generic country/region version for ERM

2. Configure expenses for the generic country/region version

3. Configure per diems for the generic country/region version

####

####

####

#### **Enable the generic country/region version for ERM**

1. In the *Business Configuration* work center, select Implementation Project. (You must have the relevant user rights to access the *Business Configuration* work center.)

2. Select your project and click *Edit Project Scope*.

3. Click *Next* until you get to the *Questions* step.

4. Select *Travel and Expense* - > *Expense and Reimbursement Management* - > *Expense Reporting*. On the right, you will see the question regarding the generic country/region version. Select the checkbox to enable generic country/region version solution.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-1-6.png)

5. Select *Next* until you reach the Confirmation step. To complete the scoping of generic country/region version, click *Finish*.

6. Select your project and click on *Open Activity* to proceed with the fine-tuning process.

7. In the Fine-Tune tab, make the following selections:

   * In the Show field, select *All Activities*

   * In the Search field, enter Create New Country/Region Version

   * Press Enter.

8. Select the *Create* *New Country/Region Version* activity that appears and add this activity to your project if it has not been already added.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-2-5.png)

9. Open the activity, and here you can define various parameters for the new *Country/Region Version* you want to create.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-3-6.png)

#### **Configure expenses for the generic country/region version**

1. Go to the Fine-Tune tab and make the following selections:

1. * In the Show field, select *All Activities*

   * In the Search field, enter Expense Reporting – Generic Country/Region Version

   * Press Enter

2. Select the *Expense Reporting – Generic Country/Region Version* activity and add this activity to your project if it has not already been added.![](/legacyfs/online/storage/blog_attachments/2022/10/newpic-scaled.jpg)

3. Open the activity, and here you will find various options to configure as shown below.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-5-5.png)

4. To define expenses for the new country/region version created above, select *Edit expense types*. You can define validity, reimbursement groups, account assignment, and so on.

#### **Configure per diems for the generic country/region version**

1. Go to the Fine-Tune tab and make the following selections:

   * In the Show field, select *All Activities*

   * In the Search field, enter Per Diem Rates for Meals - Generic Country/Region Version

   * Press Enter

2. Select the *Per Diem Rates for Meals – Generic Country/Region Version* activity as shown below and add this activity to your project, if it is not already added.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-6-6.png)

3. Open the activity, and here you will find various options to configure as shown below. You can define duration codes, account assignment, and company-specific and statutory rates for per diem rates for meals.![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-7-4.png)

4. Similar steps can be performed to configure per diems for lodging for the generic country/region version.

###

### **Summary**

When you deploy this solution, the generic country/region version related activities appear in the fine-tuning activity list in the Business Configuration. You can customise it as per your requirements and also create an expense report for an employee.

Please share your feedback or thoughts in comments.

Follow the below pages for more information:

[SAP Business ByDesign Localization](https://community.sap.com/topics/business-bydesign/localization)

[To post and answer questions on SAP Business ByDesign Localization](https://answers.sap.com/tags/190e64de-834f-49a0-bbba-822f4f809cb0)

[To read other blog posts on SAP Business ByDesign Localization](https://blogs.sap.com/tags/190e64de-834f-49a0-bbba-822f4f809cb0/)

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhow-to-enable-generic-country-region-version-in-expense-and-reimbursement%2Fba-p%2F13538449%23comment-on...