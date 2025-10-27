---
title: Business case for candidate filter within job requisition for Mass Recruiting
url: https://blogs.sap.com/2022/12/15/business-case-for-candidate-filter-within-job-requisition-for-mass-recruiting/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:23.217923
---

# Business case for candidate filter within job requisition for Mass Recruiting

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Business case for candidate filter within job requ...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5763&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Business case for candidate filter within job requisition for Mass Recruiting](/t5/human-capital-management-blog-posts-by-sap/business-case-for-candidate-filter-within-job-requisition-for-mass/ba-p/13551904)

![thiagomata](https://avatars.profile.sap.com/7/b/id7bbabda7539335d7848b16bf52c6ec3a3e2f8d22a14a5e4b93f4e5eae138000e_small.jpeg "thiagomata")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[thiagomata](https://community.sap.com/t5/user/viewprofilepage/user-id/22622)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5763)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5763)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551904)

‎2022 Dec 15
6:15 PM

[3
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5763/tab/all-users "Click here to see who gave kudos to this post.")

870

* SAP Managed Tags
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)

View products (1)

Hi!

Would like to share an idea on how to utilize in full potential the combo Recruiting business rules, Pre-screening questions and quick Apply as a powerful tool to rate candidates in your job requisitions.

In order to do that I need you to understand three main features:

**1 - Pre-Screening Questions:**

Roughly speaking, “pre-screening” questions are questions that you can add in a job requisition that a candidate will answer when they apply to a job posting, If you want a deep dive, you can access this KBA [2204476 - How Pre-Screening Questions Feature Works in Recruiting Module - Recruiting Management - S...](https://launchpad.support.sap.com/#/notes/2204476)  that I´ve used as a reference for this post, but I want to call your attention specially to one concept: Rating.

**Rating:**

Rating is calculated as the percentage of correctly answered questions which are marked ‘Score’ out of total questions which are given weights irrespective of marked ‘Required’ or answered wrongly or correctly.

Rating is calculated on weight given to each question.

Rating is dependent on ‘Score’ but independent of ‘Required’.

**Required Score:**

Required Score is the amount of rating score that you need to achieve in order to not be disqualified.

We are going to use rating to filter the candidate on the pipeline.

2 – **Quick Apply:**

Quick Apply in a quick overview is a feature that allows you to merge the user creation page with the application form in just one place. This allows us to speed up the process and just focus on what matter the most for bulk selecting candidates.

As you can see on the images bellow, I´ve created three fields: “Years of Experience”, “Zone” and “Education Level”

![](/legacyfs/online/storage/blog_attachments/2022/12/2-9.jpg)

**3 – Rules in Recruiting:**

Rules in Recruiting module allow you to apply logic to the Job Requisition, Offer, Candidate and application as you can see in the images bellow.

![](/legacyfs/online/storage/blog_attachments/2022/12/3-7.jpg)

Now you can create a pipeline with statuses you want to filter candidates.

It’s important to know that rules will only apply if an internal operator (ex: recruiter) move the candidate from one status to another. To solve this problem after the default status. I suggest that you create a “Filter” step so the only thing that the operator needs to do is to select all the candidates on the default status and move them to “Filter” status all at once.

Ex:

1 - Zone X with rating >80%, Zone X with Rating between 50% and 80% and Zone x below 50%

2 - Zone X with rating >80% with degree Y and Z Years of experience, Zone Y with rating >80% with degree Y and Z Years of experience and so on….

Summary:

1 – Create Pre- Screening questions that are going to rate the candidates accordingly the desired range for each criteria.

2 – Configure and create fields for quick apply that are going to meet the desired criteria.

3 – Create the Pipeline steps to trigger and to separate the candidates as you want.

4 – Apply the recruiting rules to move the candidates accordingly,

![](/legacyfs/online/storage/blog_attachments/2022/12/1-12.jpg)

For more details:

Visit SAP SuccessFactors community in [Home – Welcome to the SAP SuccessFactors Community!](https://community.successfactors.com/)

And take a look in SAP HELP at [SAP SuccessFactors Learning | SAP Help Portal](https://help.sap.com/docs/SAP_SUCCESSFACTORS_LEARNING?version=2111)

Quick Apply: <https://launchpad.support.sap.com/#/notes/2859372>

Recruiting Rules: <https://launchpad.support.sap.com/#/notes/2515173>

Applicant status set: [https://help.sap.com/docs/SAP\_SUCCESSFACTORS\_RECRUITING/8477193265ea4172a1dda118505ca631/41bd985d23b...](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RECRUITING/8477193265ea4172a1dda118505ca631/41bd985d23bc4dee8368c0f6da456517.html?q=edit%20applicant%20status%20set)

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [filter](/t5/tag/filter/tg-p/board-id/hcm-blog-sap)
* [quick apply](/t5/tag/quick%20apply/tg-p/board-id/hcm-blog-sap)
* [RCM](/t5/tag/RCM/tg-p/board-id/hcm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fbusiness-case-for-candidate-filter-within-job-requisition-for-mass%2Fba-p%2F13551904%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HR Efficiency in Action: Automate and Streamline HR Processes](/t5/human-capital-management-blog-posts-by-sap/hr-efficiency-in-action-automate-and-streamline-hr-processes/ba-p/14233229)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  yesterday
* [Flagging a candidate that we do not wish to consider](/t5/human-capital-management-q-a/flagging-a-candidate-that-we-do-not-wish-to-consider/qaq-p/14231970)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  Tuesday
* [Best Practices for Pay Transparency in SuccessFactors Recruiting](/t5/human-capital-management-blog-posts-by-members/best-...