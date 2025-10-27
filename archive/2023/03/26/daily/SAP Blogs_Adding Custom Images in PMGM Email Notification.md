---
title: Adding Custom Images in PMGM Email Notification
url: https://blogs.sap.com/2023/03/25/adding-custom-images-in-pmgm-email-notification/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:46.529224
---

# Adding Custom Images in PMGM Email Notification

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Adding Custom Images in PMGM Email Notification

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5008&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adding Custom Images in PMGM Email Notification](/t5/human-capital-management-blog-posts-by-members/adding-custom-images-in-pmgm-email-notification/ba-p/13559510)

![MridulSharmaSF](https://avatars.profile.sap.com/8/4/id844c2e9f835a1212be3f79e151eb074c2a2c9e633640e7cf958b1c69188c249b_small.jpeg "MridulSharmaSF")

[MridulSharmaSF](https://community.sap.com/t5/user/viewprofilepage/user-id/18397)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5008)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5008)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559510)

‎2023 Mar 25
9:36 AM

[14
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5008/tab/all-users "Click here to see who gave kudos to this post.")

5,335

* SAP Managed Tags
* [SAP SuccessFactors Performance & Goals](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Performance%2520%2526%2520Goals/pd-p/73555000100800000774)

* [SAP SuccessFactors Performance & Goals

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPerformance%2B%252526%2BGoals/pd-p/73555000100800000774)

View products (1)

**Adding Custom Images in PMGM Email Notification :**

This Blog post will help SF PMGM consultants in customizing email notifications of PMGM by adding images to make it more informative and attractive.

**Note :**

* **Data in the screenshot is not real data ,it is taken from Sales demo instance.**

Scenario : To add an image of Deadline(Hurry Up) in Document creation Notification.

**Prerequisite :**

Go to below path and Enable the required setting

1.Admin tools > Company System and Logo Settings
2.Enable HTML email notification.

**Steps to Configure :**

1.Right click on the Image which you want to add in your Notification and click on Copy image address .In my scenario image address is

<img align = "right" src="[https://previews.123rf.com/images/viktorijareut/viktorijareut1505/viktorijareut150501136/40221694-st...](https://previews.123rf.com/images/viktorijareut/viktorijareut1505/viktorijareut150501136/40221694-stopwatch-stopwatch-vector-deadline-hurry-up-stopwatch-icon-alert-icon.jpg)".

![](/legacyfs/online/storage/blog_attachments/2023/03/5-26.png)

2.Navigate to Email Notification Templates Settings under search bar and open the **Document Creation Notification Template**

![](/legacyfs/online/storage/blog_attachments/2023/03/1-60.png)

3.Navigate to Email Body of above Notification and enter the code as below.

Under src copy the image address which was captured in step 1.

You can align Left or Right as per your requirement.

Note : The max size of the logo for email footer is 470x68; this can be adjusted by adding the width and height as below

<img align = "right" src="URL of image you want to add in Notification" width="470" height="68">

4.Enter the code in Notification Template and save changes

![](/legacyfs/online/storage/blog_attachments/2023/03/7-19.png)

5.Navigate to your email inbox to see the outcome

![](/legacyfs/online/storage/blog_attachments/2023/03/8-15.png)

We can see our Highlighted image is displayed with alignment as Right which we mentioned in code.

Summary:

This Blog post is to configure our SF PMGM Notification by adding an Image inside the Email Body.

Kindly let me know if you have any questions on the same.

For other Performance Management related topic kindly visit : "<https://blogs.sap.com/tags/73555000100800000774/>"

For Questions and Answers on the Performance Management kindly visit "<https://answers.sap.com/tags/73555000100800000774>"

At last thanks for motivating me for writing Blog post and kindly follow me for more upcoming valuable Blog Posts

Thanks

Mridul Sharma

SF PMGM/SPCDP/COMP Consultant

22 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fadding-custom-images-in-pmgm-email-notification%2Fba-p%2F13559510%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [OFB - Trigger Email Notification to respective Responsible Group for document sign completion](/t5/human-capital-management-q-a/ofb-trigger-email-notification-to-respective-responsible-group-for-document/qaq-p/14202756)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Sep 01
* [How to configure Reason for late coming or leave early in SuccessFactors TimeSheet/TimeTracking?](/t5/human-capital-management-q-a/how-to-configure-reason-for-late-coming-or-leave-early-in-successfactors/qaq-p/14192557)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Aug 26
* [How to Trigger notification to HR team after all Onb tasks are completed (not just compliance)](/t5/human-capital-management-q-a/how-to-trigger-notification-to-hr-team-after-all-onb-tasks-are-completed/qaq-p/14190496)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Aug 25
* [Integrating Cluster TY Data (PCL1) with Infotype 3671 (A1 Notification) in a Custom Fiori App](/t5/human-capital-management-q-a/integrating-cluster-ty-data-pcl1-with-infotype-3671-a1-notification-in-a/qaq-p/14185039)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Aug 20
* [New ILX Blues](/t5/human-capital-management-q-a/new-ilx-blues/qaq-p/14173853)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Aug 06

Top kudoed authors

| User | Count |
| --- | --- |
| [![StephanieBM01](https://avatars.profile.sap.com/c/c/idccc84e6bff2c414fae1b3ec977ab5e84ee0ad729b03db91e7b5124b190a9fbcd_small.jpeg "StephanieBM01")  StephanieBM01](/t5/user/viewprofilepage/user-id/24844) | 4 |
| [![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad9733599afa7882bd07df433a59e25fac28240_small.jpeg "nageshpolu")  nageshpolu](/t5/user/viewprofilepage/user-id/751) | 3 |
| [![fim](https://avatars.profile.sap.com/3/e/id3e6d9c88f875a4197f372bafa845571ef1ae5005c564356d6bd46112dfe505e0_small.jpeg "fim")  fim](/t5/user/viewprofilepage/user-id/29289) | 1 |
| [![Angie_Pullano](https://avatars.profile.sap.com/b/f/idbf843fe38d889c13e75f2fce356883defe4c5cbdb7740d24f4fe65cc4eaada60_small.jpeg "Angie_Pullano")  Angie\_Pullano](/t5/user/viewprofilepage/user-id/96679) | 1 |
| [![sameergovekar](https://avatars.profile.sap.com/1/e/id1e0...