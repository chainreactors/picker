---
title: Stay current with the SAP SF Performance Management and Goal Management: 2H 2022 Release Highlights
url: https://blogs.sap.com/2022/10/22/stay-current-with-the-sap-sf-performance-management-and-goal-management-2h-2022-release-highlights/
source: SAP Blogs
date: 2022-10-23
fetch_date: 2025-10-03T20:41:17.468885
---

# Stay current with the SAP SF Performance Management and Goal Management: 2H 2022 Release Highlights

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Stay current with the SAP SF Performance Managemen...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4862&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Stay current with the SAP SF Performance Management and Goal Management: 2H 2022 Release Highlights](/t5/human-capital-management-blog-posts-by-members/stay-current-with-the-sap-sf-performance-management-and-goal-management-2h/ba-p/13552492)

![jahnavia](https://avatars.profile.sap.com/2/d/id2da8849bfc22ec01b78b7c885e68062008623f34c51442d33cfefbca7322faa2_small.jpeg "jahnavia")

[jahnavia](https://community.sap.com/t5/user/viewprofilepage/user-id/37065)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4862)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4862)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552492)

‎2022 Oct 22
1:39 PM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4862/tab/all-users "Click here to see who gave kudos to this post.")

3,817

* SAP Managed Tags
* [SAP SuccessFactors Performance & Goals](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Performance%2520%2526%2520Goals/pd-p/73555000100800000774)

* [SAP SuccessFactors Performance & Goals

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPerformance%2B%252526%2BGoals/pd-p/73555000100800000774)

View products (1)

This article highlights Key updates of **SuccessFactors PMGM 2H 2022  Release Innovations**.

There are 34 updates in total wherein 22 are universal and 12 are Admin opt-in changes.

There are a few Release Updates for **360 Reviews**. I have devoted a separate blog post to those.

[Click here to view the 360 Reviews Blog Post](https://blogs.sap.com/2022/10/25/sap-successfactors-360-reviews-2h-2022-release-highlights/)

Let's have a look at the Important PMGM announcements.

### New Confirmation Experience for Sending Forms

This new feature is taken from the  [Customer Community.](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Finfluence.sap.com%2Fsap%2Fino%2F%23%2Fidea%2F288246 "https://influence.sap.com/sap/ino/#/idea/288246") The user experience enhancement allows users to confirm the routing action without navigating them to a separate page.

SAP offers a new confirmation experience for sending Performance Management forms to the next or previous step. When users send a form, a message popup appears and allows them to confirm the action.

The new experience, if enabled, applies to the following actions:

* Send forms to the next step

* Send forms in an iterative or collaboration step

* Send forms to the previous step

* Sign forms

* Reject forms

* Send a copy of the completed forms

The highlighted button in the popup shows the default text or a customized one in a route map. If you've defined step exit text in the route map, it's shown in the popup. If you've configured the comment field, it's also shown in the popup.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog4.png)

Sending Form to Iterative Step

If an iterative step has no or several entry users, when sending a form to this step, the current step user selects a recipient from a dropdown in the popup.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog5.png)

### Managing General Audit

You can now enable auditing for page access, data export, and proxy sessions using the new tool Manage General Audit in Admin Center.

Enable general audit to expand auditing coverage and gain more insight into your system. Also, configure the retention period for the generated audit data to ensure compliance and improve storage efficiency.

* By default, auditing for data export and proxy sessions is enabled. Auditing for page access is by default disabled.

* You can turn off auditing for proxy sessions or turn on auditing for page access according to your business needs. You can't turn off auditing for data export.

* By default, audit data of data export is retained for 180 days and proxy sessions or page access is retained for 365 days. You can change the default retention period for all three types of auditing according to your business needs.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog1-4.png)

#### Prerequisites RBP

You have the Administrator  Admin Center Permissions  **Manage General Audit Configuration**. You need View permission to access Manage General Audit. You need Edit permission to change default configurations.

### New Bound Action: approveSession

You can now use the bound action, approveSession, under the CalSession.svc OData API V4 service, to finalize a calibration session that is in the In Progress or Approving status. The associated form will be automatically routed to the next step if the source of the Calibration data is Performance Management.

SAP provides this bound action to support more session operations from a third-party system.

### More Gender Values in Calibration Views

Gender indication in Calibration views has been redesigned. Previously, only Male and females were supported for visualization in Calibration Views. Now, SAP also supports the other three standard values: Unknown, Undeclared, and Others.

When the gender of an employee hasn't been specified in the system yet, it will be indicated as No Selection.

The gender icon is displayed next to the employee's name and the corresponding icons for each gender value are as follows:

![](/legacyfs/online/storage/blog_attachments/2022/10/blog2-3.png)

### Remove Subjects from Calibration Sessions

You can now remove subjects from all calibration sessions. Previously, you could only remove subjects from inactive sessions or those that were still in the setup status.

A new admin tool, Remove Subjects from Calibration Sessions, has been built, where you can search for the sessions where an employee has been included as a calibration subject.

When the employee is included in many sessions, you narrow down the search results by selecting a calibration template name. Then, only the sessions created with the specified template are listed.

SAP has built this feature to provide you more flexibility in handling data privacy, with which you can remove individual employees' calibration information by session. If a calibration session is created with People Profile as the data source, after you remove the subjects, their calibration information is removed from People Profile as well.

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog3-3.png)

### Enhancement to Guidelines Enforcement During Mass Finalization

SAP has  enhanced the enforcement of distribution guidelines so that more guidelines enforcement scenarios are supported when you finalize multiple sessions at one time.

It is now supported in three more guideline scenarios:

* More than one rating is included in a guideline, that is, the guideline is defined with a r...