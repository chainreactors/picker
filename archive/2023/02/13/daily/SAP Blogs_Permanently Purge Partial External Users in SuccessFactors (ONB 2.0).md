---
title: Permanently Purge Partial External Users in SuccessFactors (ONB 2.0)
url: https://blogs.sap.com/2023/02/12/permanently-purge-partial-external-users-in-successfactors-onb-2.0/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:27:54.014151
---

# Permanently Purge Partial External Users in SuccessFactors (ONB 2.0)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Permanently Purge Partial External Users in Succes...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5207&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Permanently Purge Partial External Users in SuccessFactors (ONB 2.0)](/t5/human-capital-management-blog-posts-by-members/permanently-purge-partial-external-users-in-successfactors-onb-2-0/ba-p/13568449)

![josmerjoseph6](https://avatars.profile.sap.com/1/4/id14b397e88a7db0edb57d5f95e1985c6b6a485c0589c56344f045e7b54c327500_small.jpeg "josmerjoseph6")

[josmerjoseph6](https://community.sap.com/t5/user/viewprofilepage/user-id/37777)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5207)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5207)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568449)

‎2023 Feb 12
12:49 PM

[9
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5207/tab/all-users "Click here to see who gave kudos to this post.")

5,127

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Onboarding](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Onboarding/pd-p/67838200100800006242)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Onboarding

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BOnboarding/pd-p/67838200100800006242)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (3)

Hope you are doing great!

This blog post explains the process of purging the partially created External Users in Onboarding 2.0.

### Scenario

Some Organizations use external solutions for the recruitment process and choose to use SuccessFactors for Onboarding, HR Core (Employee Central) and so on.

In these cases an integration should be set up with multiple entities like External User, Biographical Information, Personal Information, Job Information etc. in a sequence to create candidates. The User ID gets generated the moment the External User entity is upserted. In case the data was insufficient in the source file for any other entities or missed data for mandatory fields, the partial External Users get created in SuccessFactors.

These partial records have to be purged permanently due to this.

### Solution

**Step 1: Make the status of the candidate/external users inactive**

ONB 2.0 doesn't allow to manually update/edit status of the candidate in the instance.

Here, an Integration Center Job can be created to upsert the status of the candidate. The status has to be defaulted to 'd' to make the candidate inactive in Onboarding.

Click [here](https://userapps.support.sap.com/sap/support/knowledge/en/3141240) (KBA/Note 3141240) for the detailed process of creating the IC Job.

Once the Job is created, filter with the User Id's as required and run the job when necessary instead of scheduling job on a recurring basis as this scenario comes less frequently.

**Step 2: Purge the Inactive User**

Navigate to **Data Retention Management** to do the purge process.

Create a new purge request and select the Purge Inactive User as the purge request type.

Make sure **There is data for this user in Employee Central (EC)** is unchecked.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-12_18-00-05.jpg)

Note: Common step which may be missed in the setup of purging a user in an instance with LMS enabled is mentioned [here](https://userapps.support.sap.com/sap/support/knowledge/en/2179378#:~:text=If%20you%20are%20experiencing%20the,access%20provisioning%20and%20disable%20it.) (KBA/Note 2179378). Make sure this is also setup before purging the inactive users.

Once the soft purge is completed, do the permanent purge using **System Identifier Purge** in the **Data Retention Management**.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-12_18-04-47.jpg)

Hope this blog post was useful.

Thank You!

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fpermanently-purge-partial-external-users-in-successfactors-onb-2-0%2Fba-p%2F13568449%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Alerts for Employee's Dependent Information](/t5/human-capital-management-blog-posts-by-members/alerts-for-employee-s-dependent-information/ba-p/14223125)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  a week ago
* [EU Pay Transparency in SAP SuccessFactors — A Suite-Level Compliance Playbook](/t5/human-capital-management-blog-posts-by-members/eu-pay-transparency-in-sap-successfactors-a-suite-level-compliance-playbook/ba-p/14223230)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago
* [Qualtrics survey responses to LMS](/t5/human-capital-management-q-a/qualtrics-survey-responses-to-lms/qaq-p/14217314)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  3 weeks ago
* [Implementing OIDC Authentication for SuccessFactors API Integration](/t5/human-capital-management-q-a/implementing-oidc-authentication-for-successfactors-api-integration/qaq-p/14215387)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  3 weeks ago
* [2H 2025 Onboarding (Preview): Employee‑Initiated Corrections to Form I‑9 Section 1](/t5/human-capital-management-blog-posts-by-sap/2h-2025-onboarding-preview-employee-initiated-corrections-to-form-i-9/ba-p/14209129)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a month ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![StephanieBM01](https://avatars.profile.sap.com/c/c/idccc84e6bff2c414fae1b3ec977ab5e84ee0ad729b03db91e7b5124b190a9fbcd_small.jpeg "StephanieBM01")  StephanieBM01](/t5/user/viewprofilepage/user-id/24844) | 4 |
| [![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad9733599afa7882bd07df433a59e25fac28240_small.jpeg "nageshpolu")  nageshpolu](/t5/user...