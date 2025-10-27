---
title: Configuration for Named vs Anonymous visibility of Rater’s name on 360 Fiori Form template
url: https://blogs.sap.com/2023/01/23/configuration-for-named-vs-anonymous-visibility-of-raters-name-on-360-fiori-form-template/
source: SAP Blogs
date: 2023-01-24
fetch_date: 2025-10-04T04:38:45.343446
---

# Configuration for Named vs Anonymous visibility of Rater’s name on 360 Fiori Form template

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Configuration for Named vs Anonymous visibility of...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4843&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Configuration for Named vs Anonymous visibility of Rater's name on 360 Fiori Form template](/t5/human-capital-management-blog-posts-by-members/configuration-for-named-vs-anonymous-visibility-of-rater-s-name-on-360/ba-p/13548750)

![Haridha_Ponnusamy](https://avatars.profile.sap.com/4/7/id47d2662c0ea52124500baac0bee1936f19966c6c3aa97a99a1269e038f04157d_small.jpeg "Haridha_Ponnusamy")

[Haridha\_Ponnusamy](https://community.sap.com/t5/user/viewprofilepage/user-id/118171)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4843)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4843)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548750)

‎2023 Jan 23
11:45 PM

[11
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4843/tab/all-users "Click here to see who gave kudos to this post.")

2,872

* SAP Managed Tags
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Performance & Goals](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Performance%2520%2526%2520Goals/pd-p/73555000100800000774)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Performance & Goals

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPerformance%2B%252526%2BGoals/pd-p/73555000100800000774)

View products (3)

## Introduction

Configuring a 360 form to have different levels of anonymity based on steps available in Route map and relation to an employee.

For example:
1. Configuring the form with permission where the manager can see the raters list in 360 forms as named, but the employee can only see the rater list anonymous.
2. Configuring the form with permission where the employee can see responses from employee's manager or peers as named, but the response from direct reports is anonymous.

## Configuring 360 template with Anonymous Rater's

In Provisioning, access your 360-form template and select the option **Anonymous 360.**

*Note - To complete tasks in Provisioning, contact your implementation partner. If you're no longer working with an implementation partner, contact SAP Cloud Support.*

In Anonymous 360 Process, users will not be able to see the names of the participants in the form. The Username will show as "Anonymous" in all route map stages.

![](/legacyfs/online/storage/blog_attachments/2023/01/anonymous-360-fiori.jpg)

## Configuring 360 template with Rater's name

In Provisioning, access your 360-form template and select the option **Participant names on 360.**

*Note - To complete tasks in Provisioning, contact your implementation partner. If you're no longer working with an implementation partner, contact SAP Cloud Support.*

In Named 360 Process, the participant names are visible in the Evaluation Summary of your 360 forms. However, it is possible to make a 360 anonymous for someone and named for others in Named 360 process.

### Configuration of rater-id-permission

This element (**<rater-id-permission>**) defines who can see the rater identities in which routing step. This only makes sense in an Open or Named 360 in which you can choose to hide rater identities in certain 360 routing steps, including 360 Evaluation Stage and Completed Stage.
For 360 evaluation stage, use this special stepid: "**360EvaluationStage**".
For Completed Stage, use this special stepid: "**CompletedStage**".
This is configured in the meta-section of the form template xml.

After enabling **Participant names on 360**, add the following XML example in the meta section after:

*<meta-cat hidden-threshold="0" min-count="0" max-count="2147483647" ><![CDATA[Self]]></meta-cat>*

Here are example codes for rater-id-permission:

#### Example 1:

The following XML permission added in the meta-section hides all rater identities for all users & every rater will be displayed as Anonymous in all stages available. In effect, it turns a Named 360 form to an Anonymous 360 form even though participants name on 360 form is enabled.

*<rater-id-permission type="none">*
*<rater-category>\*</rater-category>*
*<role-name>\*</role-name>*
*<route-step stepid="\*"/>*
*</rater-id-permission>*

OR

*<rater-id-permission type="none">*
*<role-name>\*</role-name>*
*<route-step stepid="\*"/>*
*</rater-id-permission>*

**![](/legacyfs/online/storage/blog_attachments/2023/01/None-permission-1.png)**

Employee View-"Anonymous username" though "Participants name on form" option is enabled.

![](/legacyfs/online/storage/blog_attachments/2023/01/Manager-view-None-permission-1.png)

Manager View-Anonymous username though "Participants name on form" option is enabled.

#### Example 2:

The following XML permission added in the meta-section hides all rater identities for all users in 360 Evaluation Stage alone & the raters name will be displayed on the form in completion step.

*<rater-id-permission type="none">*
*<rater-category>\*</rater-category>*
*<role-name>\*</role-name>*
*<route-step stepid="360EvaluationStage"/>*
*</rater-id-permission>*

OR

*<rater-id-permission type="none">*
*<role-name>\*</role-name>*
*<route-step stepid="360EvaluationStage"/>*
*</rater-id-permission>*

![](/legacyfs/online/storage/blog_attachments/2023/01/Manager-view-Evalution-step-1-1.png)

Manager view-Evaluation step with Anonymous raters

![](/legacyfs/online/storage/blog_attachments/2023/01/Employee-view-Evalution-step-.png)

Employee View-Evaluation step with Anonymous raters

![](/legacyfs/online/storage/blog_attachments/2023/01/Employee-view-Completion-step-1-1.png)

Employee view-Completion step with rater's name

![](/legacyfs/online/storage/blog_attachments/2023/01/Manager-view-Completion-step-.png)

Manager view-Completion step with rater's name

#### Example 3:

The following XML permission added in the meta-section hides all rater identities for All users in 360 Evaluation and Completion Stage EXCEPT for the Manager.

*<rater-id-permission type="none">*
*<rater-category>\*</rater-category>*
*<role-name>\*</role-name>*
*<route-step stepid="\*"/>*
*</rater-id-permission>*
*<rater-id-permission type="enabled">*
*<rater-category>\*</rater-category>*
*<role-name>EM</role-name>*
*<route-step stepid="360EvaluationStage"/>*
*<route-step stepid="CompletedStage"/>*
*</rater-id-permission>*

![](/legacyfs/onlin...