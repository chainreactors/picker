---
title: SAP Commissions(K8s) – OpenId Connect(OIDC) Setup – Part 1
url: https://blogs.sap.com/2023/02/25/sap-commissionsk8s-openid-connectoidc-setup-part-1/
source: SAP Blogs
date: 2023-02-26
fetch_date: 2025-10-04T08:08:29.894007
---

# SAP Commissions(K8s) – OpenId Connect(OIDC) Setup – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions(K8s) - 🔑OpenId Connect(OIDC) Setu...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5965&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions(K8s) - 🔑OpenId Connect(OIDC) Setup - Part 1](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-k8s-openid-connect-oidc-setup-part-1/ba-p/13557699)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5965)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5965)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557699)

‎2023 Feb 25
9:08 AM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5965/tab/all-users "Click here to see who gave kudos to this post.")

2,019

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (1)

In this blog, you will come to know how to configure OpenID Connect Configuration for your **SAP IAS (Identity Authentication Service)** tenant explained in step by step process. This process is mainly required for API Authentication to get some data out of SAP Commissions using Rest APIs.

|  |
| --- |
| New SAP Commissions is running on a microservice architecture - Kubernetes inside Google Cloud Platform (GCP).  This blog information content is applicable only for tenants starting with \*\*\*\*.app.commissions.cloud.sap |

![](/legacyfs/online/storage/blog_attachments/2023/02/cloudsecurity-WrightStudio-AdobeStock.png)

### Perform the following steps to create Application for OIDC

Go to IAS Administration → Applications and Create Commissions OIDC application.

To create Commissions OIDC applications, we use the following naming pattern: COMM\_{SUBDOMAIN}\_OIDC\_{TENANTURL}.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-25_09-15-57.png)Follow the steps as shown in highlighted numbers which is required information to be updated.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-25_09-31-52.png)Follow the steps as shown for OpenID Connect Configuration

|  |  |
| --- | --- |
| **Name** | <https://gxxx.app.commissions.cloud.sap> |
| Redirect URIs | <https://gxxx.app.commissions.cloud.sap/iamsvc/oidc/receive/login> |
| Post Logout Redirect URIs | <https://gxxx.app.commissions.cloud.sap/iamsvc/oidc/logout/receive> |

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-25_09-22-04.png)Open Client ID Authentication and you would see the below example![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-25_09-36-11.png)Provide the required details in the Add Secrets dialog and click Save.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-24_21-14-05.png)**Add a new secret and copy the clientId and the clientSecret from the result prompt
Save your client secret** and click OK.
![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-24_21-16-43.png)

---

**Watch out for next blog Part 2 - How to Authenticate APIs using OAuth token**

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [API](/t5/tag/API/tg-p/board-id/hcm-blog-sap)
* [Authentication](/t5/tag/Authentication/tg-p/board-id/hcm-blog-sap)
* [OpenIDConnect](/t5/tag/OpenIDConnect/tg-p/board-id/hcm-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fsap-commissions-k8s-openid-connect-oidc-setup-part-1%2Fba-p%2F13557699%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Deprecation of API Basic Authentication & Configuring Open ID Connect](/t5/human-capital-management-blog-posts-by-members/deprecation-of-api-basic-authentication-amp-configuring-open-id-connect/ba-p/14215998)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago
* [Enable Social Login & 2FA for External Candidates in SAP SuccessFactors via SAP Customer Data Cloud](/t5/human-capital-management-blog-posts-by-sap/enable-social-login-amp-2fa-for-external-candidates-in-sap-successfactors/ba-p/14081304)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  2025 Jun 25
* [SEN and S/4 sso issue X-Frame-Options](/t5/human-capital-management-q-a/sen-and-s-4-sso-issue-x-frame-options/qaq-p/14094217)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 May 06
* [Principles to Practice: Securing SAP Business AI](/t5/human-capital-management-blog-posts-by-sap/principles-to-practice-securing-sap-business-ai/ba-p/14090586)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  2025 Apr 30
* [Step-by-Step Guide to Use an Attribute Other Than LoginName for Seamless Authentication](/t5/human-capital-management-blog-posts-by-sap/step-by-step-guide-to-use-an-attribute-other-than-loginname-for-seamless/ba-p/13952563)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  2024 Dec 02

Top kudoed authors

| User | Count |
| --- | --- |
| [![ThomasBilbaugh](https://avatars.profile.sap.com/e/0/ide0070e22003039d74134e36021e60621f3d8092be5f11f8ea807d3b320997975_small.jpeg "ThomasBilbaugh")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") ThomasBilbaugh](/t5/user/viewprofilepage/user-id/18281) | 31 |
| [![jenny_geipel](https://avatars.profile.sap.com/2/b/id2bfd2cb1406b6274e78674658af9d916a0ca15fb66ab4e6793400a0a524f93e2_small.jpeg "jenny_geipel")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jenny\_geipel](/t5/user/viewprofilepage/user-id/17811) | 4 |
| [![safina](https://avatars.profile.sap.com/d/8/idd888a4b25efd80039c6b8e8e7a87dc02042f00bd3864ea...