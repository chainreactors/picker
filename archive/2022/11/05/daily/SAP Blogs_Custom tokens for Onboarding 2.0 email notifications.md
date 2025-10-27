---
title: Custom tokens for Onboarding 2.0 email notifications
url: https://blogs.sap.com/2022/11/04/custom-tokens-for-onboarding-2.0-email-notifications/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:44:47.119017
---

# Custom tokens for Onboarding 2.0 email notifications

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Custom tokens for Onboarding 2.0 email notificatio...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5045&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Custom tokens for Onboarding 2.0 email notifications](/t5/human-capital-management-blog-posts-by-members/custom-tokens-for-onboarding-2-0-email-notifications/ba-p/13560942)

![](/skins/images/E8A536C0D834652C9A43FCC2963C1D98/responsive_peak/images/icon_anonymous_profile.png)

Former Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5045)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5045)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560942)

‎2022 Nov 04
8:35 PM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5045/tab/all-users "Click here to see who gave kudos to this post.")

7,805

* SAP Managed Tags
* [SAP SuccessFactors Onboarding](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Onboarding/pd-p/67838200100800006242)

* [SAP SuccessFactors Onboarding

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BOnboarding/pd-p/67838200100800006242)

View products (1)

**New Release**

**Custom Tokens for Onboarding 2.0 Email Notifications**

This is long time requirement for most of the customers, as custom tokens in Onboarding 1.0 is feasible and it is expected to be available in Onboarding 2.0 also.

It’s a great start from SAP and in the 2H 2022 new release SAP has brought in the custom token’s functionality into availability with some limitations for now.

**Below are the steps/actions on how to configure custom tokens in Onboarding 2.0.**

**High level steps**

* Create the custom token template content using Document Generation- Manage Document Template.

* Map the custom tokens using Document Generation- Manage Document Template Mapping.

* Insert the custom tokens in the email template in Email Services.

**Configuration steps**

1. Access Document Generation- Manage Document Template from Admin centre

2. Search for Manage Document Template from create new

3. Name the template ID exactly as **EMAIL\_CUSTOM\_TOKEN\_MAPPING** (Note: Addition to the default one created, you need to create another with an extension of **EN\_US/EN\_GB** at the end Ex: **EMAIL\_CUSTOM\_TOKEN\_MAPPING\_EN\_US** depending on the additional locales you are configuring)

4. Enter the details in rest of the fields as needed

5. Create the tokens using place holders in Template Content as needed and save

6. Map the custom tokens from Document Generation- Manage Document Template Mapping

After mapping, you can now use the custom tokens and can insert the custom tokens in the email template in Email Services.

![](/legacyfs/online/storage/blog_attachments/2022/11/Image01-2.jpg)

Only the tokens that are mapped in Document Generation-Manage Document Template Mapping will appear in the email template token list

Note that, there are still some limitations.

* Fields from custom MDF objects cannot be mapped to custom tokens.

* Custom tokens are not supported in templates with trigger (ONB) Suite mapping error Trigger.

* Custom tokens are not supported in Nudge email notifications.

Expecting these limitations to be covered also in the upcoming releases which will best support Onboarding 2.0 module for extended/enhanced customer implementations.

To summarize: Provided information on the new functionality availability of **Custom Tokens for Onboarding 2.0 Email Notifications,**along with the high level and configuration steps to achieve and the current limitations.

Please feel free to add any additional information/feedback in the comments.

Thank you..

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fcustom-tokens-for-onboarding-2-0-email-notifications%2Fba-p%2F13560942%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [2H 2025 Onboarding (Preview): Employee‑Initiated Corrections to Form I‑9 Section 1](/t5/human-capital-management-blog-posts-by-sap/2h-2025-onboarding-preview-employee-initiated-corrections-to-form-i-9/ba-p/14209129)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a month ago
* [SAP BTP for HR at SAP Connect and Success Connect 2025 summary - bigger and better than ever](/t5/human-capital-management-blog-posts-by-sap/sap-btp-for-hr-at-sap-connect-and-success-connect-2025-summary-bigger-and/ba-p/14209124)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a month ago
* [Onboarding Email Notification with Candidate uploaded document as an attachment](/t5/human-capital-management-q-a/onboarding-email-notification-with-candidate-uploaded-document-as-an/qaq-p/14155551)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Jul 17
* [SuccessFactors Onboarding - Attach 1 specific signed custom document in Onboardee Notification](/t5/human-capital-management-q-a/successfactors-onboarding-attach-1-specific-signed-custom-document-in/qaq-p/14141085)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Jul 01
* [Onboarding P45 Notification](/t5/human-capital-management-q-a/onboarding-p45-notification/qaq-p/14139761)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Jun 29

Top kudoed authors

| User | Count |
| --- | --- |
| [![StephanieBM01](https://avatars.profile.sap.com/c/c/idccc84e6bff2c414fae1b3ec977ab5e84ee0ad729b03db91e7b5124b190a9fbcd_small.jpeg "StephanieBM01")  StephanieBM01](/t5/user/viewprofilepage/user-id/24844) | 4 |
| [![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad9733599afa7882bd07df433a59e25fac28240_small.jpeg "nageshpolu")  nageshpolu](/t5/user/viewprofilepage/user-id/751) | 3 |
| [![ShashankS](https://avatars.profile.sap.com/9/f/id9f3b39f55ea45eacc370db4afd8e7a3b01b65bc4d6fe9d68d9159059e1d0c4f7_small.jpeg "ShashankS")  ShashankS](/t5/user/viewprofilepage/user-id/1459014) | 1 |
| [![fim](https://avatars.profile.sap.com/3/e/id3e6d9c88f875a4197f372bafa845571ef1ae5005c564356d6bd46112dfe505e0_small.jpeg "fim")  fim](/t5/user/viewprofilepage/user-id/29289) | 1 |
| [![Angie_Pullano](https://avatars.profile.sap.com/b/f/idbf843fe38d889c13e75f2fce356883defe4c5cbdb7740d24f4fe65cc4eaada60_small.jpeg "Angie_Pullano")  Angie\_Pullano](/t5/user/viewprofilepage/user-id/96679) | 1 |
| [![sameergovekar](https://avatars.profile.sa...