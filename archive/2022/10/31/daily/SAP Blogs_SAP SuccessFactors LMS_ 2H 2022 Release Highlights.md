---
title: SAP SuccessFactors LMS: 2H 2022 Release Highlights
url: https://blogs.sap.com/2022/10/30/sap-successfactors-lms-2h-2022-release-highlights/
source: SAP Blogs
date: 2022-10-31
fetch_date: 2025-10-03T21:20:58.584953
---

# SAP SuccessFactors LMS: 2H 2022 Release Highlights

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* SAP SuccessFactors LMS: 2H 2022 Release Highlights

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4992&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP SuccessFactors LMS: 2H 2022 Release Highlights](/t5/human-capital-management-blog-posts-by-members/sap-successfactors-lms-2h-2022-release-highlights/ba-p/13558681)

![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad9733599afa7882bd07df433a59e25fac28240_small.jpeg "nageshpolu")

[nageshpolu](https://community.sap.com/t5/user/viewprofilepage/user-id/751)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4992)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4992)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558681)

‎2022 Oct 30
1:44 PM

[10
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4992/tab/all-users "Click here to see who gave kudos to this post.")

4,556

* SAP Managed Tags
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Learning](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Learning/pd-p/67837800100800006334)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Learning

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BLearning/pd-p/67837800100800006334)

View products (2)

Hi there,

Second half 2022 release is here!

This blog highlights key enhancements to SuccessFactors Learning (LMS). As mentioned in my previous [blog](https://blogs.sap.com/2022/10/29/sap-successfactors-employee-central-2h-2022-release-highlights/), the 2H release is more customer centric, lot of enhancements coming from customer community ideas or customer feedback. Thank you, SAP!!

Let’s look at some of the most interesting features and changes introduced since last time.

1. **Task Checklist Preview:** Task Checklist Preview enables users see the Task Checklist tab when viewing an item with a classification of Other. This tab allows the user to preview the tasks they have to complete.

SAP once again proved that they are customer centric, this one has been the most requested in past years.

* Configuration Type: Universal

* ***Early Adoption***

**Note:** Course Home is a prerequisite, if you haven’t enabled the new Course Home experience, then the Task Checklist tab doesn't display to users, regardless of selection for this setting

![](/legacyfs/online/storage/blog_attachments/2022/10/Task-Checklist.png)

2. **Enhanced Course Home:** The new Course Home experience now supports items with a classification of Other, such as task checklists. In addition, the following features are supported for all applicable item classifications:

* Jam integration

* Selection of missing approvers when registering

SAP continuing to add functionality to the new Course Home experience because globally most of the customers have been asking for an updated user experience and SAP delivered in no time.

* Configuration Type: Admin Opt-in

Note: You will also notice few updates on previously released item classifications. For instructor-led training, the class details now display the timezone. For online courses that are launched in a new window, the Refresh after done button no longer displays.

![](/legacyfs/online/storage/blog_attachments/2022/10/CourseHome.png)

3. **Learning Assessments for Content Packages**: You can now select an assessment in the Exam field on the Content Tab Edit page. This enhancement allows you to use assessments in content packages. This replaces the legacy exam functionality for content packages that was previously removed.

* Configuration Type: Universal

![](/legacyfs/online/storage/blog_attachments/2022/10/Content-Package.png)

4. **Automatic Updates for Learning Assignments and Approvals on the Latest Home Page:** Thanks to SAP! Going forward, whenever you change the successFactorsLearningEnabled, baseURL, or successFactorsCompanyID settings in the BizX Configuration file, a background job will run automatically to display learning assignments and learning approvals on the latest home page. Previously, we had to manually run a job for learning assignments and learning approvals to be displayed on the latest home page.

* Configuration Type: Universal

5. **Global User ID**: Global User ID is now displayed on the User Details page. This has been added to enable admins to verify if a user is created in SuccessFactors platform at the same time they are created in Learning.

* Configuration Type: Universal

![](/legacyfs/online/storage/blog_attachments/2022/10/Global-User-ID.png)

6. **Microsoft Teams VLS Attendance**: Microsoft updated their attendance API for Microsoft Teams virtual learning sessions. Remember, this update requires an additional permission in Microsoft Azure. This permission is required by Microsoft to support their Microsoft Teams attendance API upgrade. In addition to this, SAP also configured the custom fields in user profiles to recognize an alternate Microsoft Azure email address. This enhancement ensures attendance is properly processed for virtual time slots where Microsoft Teams is the vendor. You need to specify which custom field contains the alternate email address in the VLS configuration for Microsoft Teams.

* Configuration Type: Admin Opt-in

7. **Qualtrics Feedback Opportunity for Learning Assignment Completion:** Addition to the User ID field (which contains the student ID of the learner), the Learning integration now sends more data to Qualtrics. These fields are automatically transmitted in the integration. Learning administrators have no new settings to configure or change. Till now, the only data that was transmitted to Qualtrics when employees completed a Learning assignment, was their User ID.

* Configuration Type: Admin Opt-in

![](/legacyfs/online/storage/blog_attachments/2022/10/Qualtrics.png)

Again, this is just a list of my favorites from the latest release. For detailed list of innovations, please check out the "[What's New Viewer](https://help.sap.com/doc/62fddbd651204629b46bbccbabf886ba/cloud/en-US/159bda31b711402c884ae5686446840d.html)". The What’s New View will provide the detailed release summary across application.

See you soon with a new blog! Happy Sunday!!

* [LMS](/t5/tag/LMS/tg-p/board-id/hcm-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fsap-successfactors-lms-2h-2022-release-high...