---
title: Different Permissions Pre & Post Saving of Portlets
url: https://blogs.sap.com/2023/04/16/different-permissions-pre-post-saving-of-portlets/
source: SAP Blogs
date: 2023-04-17
fetch_date: 2025-10-04T11:32:05.879139
---

# Different Permissions Pre & Post Saving of Portlets

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* How to Avoid Editing of MDF Portlets without RBP

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4904&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Avoid Editing of MDF Portlets without RBP](/t5/human-capital-management-blog-posts-by-members/how-to-avoid-editing-of-mdf-portlets-without-rbp/ba-p/13553546)

![Venkatesh_M](https://avatars.profile.sap.com/3/5/id35b0127b0929631ab3b5072196696f9ba842fbb5072c4c0288669ba556193e5d_small.jpeg "Venkatesh_M")

[Venkatesh\_M](https://community.sap.com/t5/user/viewprofilepage/user-id/116410)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4904)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4904)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553546)

‎2023 Apr 16
8:11 AM

[3
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4904/tab/all-users "Click here to see who gave kudos to this post.")

1,631

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (4)

In this blog post, we will delve into a specific scenario that highlights the challenge of granting users access to create records while simultaneously preventing them from editing those records. In this particular situation traditional role-based permissions (RBP) fall short in addressing this need.

Typically, when users are granted permission to create records, it inherently includes the ability to edit them as well. However, there are cases where organizations require a more granular level of control over record modifications, especially when the data serves as a crucial source for external systems.

To meet this need, a more controlled solution is necessary to avoid users with the creation privileges altering the data. This level of control is crucial to maintain the integrity and reliability of the data used across the system landscape.

**Boolean Field in MDF Object:**

Create a field with data type Boolean in the concerned MDF object which will be used to know if the record is already created or not. its default value is "No".

![](/legacyfs/online/storage/blog_attachments/2023/04/Blog-5.png)

**Business Rule to Update Boolean Field:**

Create a rule to set the Boolean field value to “Yes” when a record gets saved.  Assign this to the concerned object in Save Rules.

![](/legacyfs/online/storage/blog_attachments/2023/04/blog-5.1-1.png)

#### ![](/legacyfs/online/storage/blog_attachments/2023/04/Blog-5.2-2.png)

####

**Business Rule to Avoid Editing:**

This rule checks the Boolean field value and triggers an error while editing the fields. This rule should be assigned as on change type to the concerned fields of the object

![](/legacyfs/online/storage/blog_attachments/2023/04/Blog-5.3-1.png)
![](/legacyfs/online/storage/blog_attachments/2023/04/Blog-5.4.png)

System would throw the following error when the concerned user tries to edit the data

![](/legacyfs/online/storage/blog_attachments/2023/04/Blog-5.5.png)

Overall, it's a simple and effective solution when you need more controlled permissions than being offered by RBP. Thanks for reading until the end; please don't hesitate to share your opinions and thoughts.

You can subscribe this [newsletter](https://techandthoughts.beehiiv.com/) to join a strong community along with being updated on SAP and beyond

* [business rule on MDF object](/t5/tag/business%20rule%20on%20MDF%20object/tg-p/board-id/hcm-blog-members)
* [custom mdf](/t5/tag/custom%20mdf/tg-p/board-id/hcm-blog-members)
* [role based permissions](/t5/tag/role%20based%20permissions/tg-p/board-id/hcm-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fhow-to-avoid-editing-of-mdf-portlets-without-rbp%2Fba-p%2F13553546%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Cannot edit Bookpage](/t5/human-capital-management-q-a/cannot-edit-bookpage/qaq-p/14233605)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  Thursday
* [RCM Field permission blocks are getting added randomly](/t5/human-capital-management-blog-posts-by-members/rcm-field-permission-blocks-are-getting-added-randomly/ba-p/14233364)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  Thursday
* [Best Practices for Pay Transparency in SuccessFactors Recruiting](/t5/human-capital-management-blog-posts-by-members/best-practices-for-pay-transparency-in-successfactors-recruiting/ba-p/14228328)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  a week ago
* [List of Employee Central & Employee Central Payroll Guide Updates for the 2H 2025 Release](/t5/human-capital-management-blog-posts-by-sap/list-of-employee-central-amp-employee-central-payroll-guide-updates-for-the/ba-p/14228406)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a week ago
* [Custom field of Custom portlet to be pre-populated with Employees Date of Birth](/t5/human-capital-management-q-a/custom-field-of-custom-portlet-to-be-pre-populated-with-employees-date-of/qaq-p/14218556)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![StephanieBM01](https://avatars.profile.sap.com/c/c/...