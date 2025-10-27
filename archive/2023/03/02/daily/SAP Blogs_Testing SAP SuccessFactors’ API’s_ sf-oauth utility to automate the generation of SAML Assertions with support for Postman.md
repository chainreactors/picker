---
title: Testing SAP SuccessFactors’ API’s: sf-oauth utility to automate the generation of SAML Assertions with support for Postman
url: https://blogs.sap.com/2023/03/01/testing-sap-successfactors-apis-sf-oauth-utility-to-automate-the-generation-of-saml-assertions-with-support-for-postman/
source: SAP Blogs
date: 2023-03-02
fetch_date: 2025-10-04T08:26:41.053671
---

# Testing SAP SuccessFactors’ API’s: sf-oauth utility to automate the generation of SAML Assertions with support for Postman

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Testing SAP SuccessFactors’ API’s: sf-oauth utilit...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5047&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Testing SAP SuccessFactors’ API’s: sf-oauth utility to automate the generation of SAML Assertions with support for Postman](/t5/human-capital-management-blog-posts-by-members/testing-sap-successfactors-api-s-sf-oauth-utility-to-automate-the/ba-p/13561000)

![pieterjanssens](https://avatars.profile.sap.com/e/f/idef494442263c5d86971e028495804440bfe1baef44537b88b8075e473ab84bea_small.jpeg "pieterjanssens")

[pieterjanssens](https://community.sap.com/t5/user/viewprofilepage/user-id/68447)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5047)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5047)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561000)

‎2023 Mar 01
9:15 PM

[6
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5047/tab/all-users "Click here to see who gave kudos to this post.")

2,396

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

SuccessFactors consultants and developers are often using the /oauth/idp endpoint the generate the assertion and consequently use the assertion in an additional request to obtain an access token.

This endpoint is [now deprecated and will be removed in the near future](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/db7ccbbbc7a54e929a305ff92d12241c.html). It's good to point out that although Postman supports many flavours of OAuth, it does not support the OAuth 2.0 SAML bearer assertion flow that is used by SAP SuccessFactors HXM Suite.

Let's look at some alternatives:

* Use [basic authentication](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/fcc05a902b4140e585d968c2fe4a96bc.html)

  + should not even be considered as an option

* Use [an offline assertion generator](https://launchpad.support.sap.com/#/notes/3031657)

  + cumbersome to switch between instances/identities

* Swap out Postman for to a different API testing tool, like [Insomnia](https://insomnia.rest/) for which [there exists a plugin](https://blogs.sap.com/2023/02/02/testing-successfactors-apis-how-to-use-insomnia-to-automate-the-generation-of-saml-assertions/) developed by edersouza38

  + might a big ask to step away from a tool that is already familiar for many

I decided to find and eventually develop a solution that could work for Postman and in general help me to manage the required SAML assertion keys.

## Let me introduce you to '**sf-oauth**' 🪄

It's a cross-platform cli utility featuring:

* Generate a new key pair

* Check certificate validity

* **Generate assertion (and validate)**

* **Run a local web service to generate an assertion and provide access tokens**

* **Integrate with a Postman OAuth flow to obtain an access token**

  + Indirect: Automatically opening your browser to enter a user ID and returning to Postman

  + Direct: when a userId is provided in the request to the local web service, a valid access token is immediately returned to Postman

To get going, please take a look at the documentation on the homepage: [sf-oauth (npmjs.com)](https://www.npmjs.com/package/sf-oauth)

Here is a sneak peak on how effortless your API testing will become in Postman using this utility:

* [oauth2](/t5/tag/oauth2/tg-p/board-id/hcm-blog-members)
* [oauth2samlbearerassertion](/t5/tag/oauth2samlbearerassertion/tg-p/board-id/hcm-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Ftesting-sap-successfactors-api-s-sf-oauth-utility-to-automate-the%2Fba-p%2F13561000%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HR Efficiency in Action: Automate and Streamline HR Processes](/t5/human-capital-management-blog-posts-by-sap/hr-efficiency-in-action-automate-and-streamline-hr-processes/ba-p/14233229)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  Thursday
* [Implementing OIDC Authentication for SuccessFactors API Integration](/t5/human-capital-management-q-a/implementing-oidc-authentication-for-successfactors-api-integration/qaq-p/14215387)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  3 weeks ago
* [Unlocking MDF Power: A Practical User Case in SAP SuccessFactors](/t5/human-capital-management-blog-posts-by-members/unlocking-mdf-power-a-practical-user-case-in-sap-successfactors/ba-p/14201953)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2025 Aug 31
* [SAP SuccessFactors Employee Central - Business Rule Function Doesnot Work as Expected](/t5/human-capital-management-blog-posts-by-members/sap-successfactors-employee-central-business-rule-function-doesnot-work-as/ba-p/14170341)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2025 Aug 11
* [Leveraging SAP Joule for Performance & Goals Management: Exact Prompts for Maximum Productivity](/t5/human-capital-management-blog-posts-by-members/leveraging-sap-joule-for-performance-amp-goals-management-exact-prompts-for/ba-p/14170375)
  in [Human Capital Management Blog Posts by Members](/t5/hum...