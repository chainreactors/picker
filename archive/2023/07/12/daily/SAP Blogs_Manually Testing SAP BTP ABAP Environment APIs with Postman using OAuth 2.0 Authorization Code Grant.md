---
title: Manually Testing SAP BTP ABAP Environment APIs with Postman using OAuth 2.0 Authorization Code Grant
url: https://blogs.sap.com/2023/07/11/manually-testing-sap-btp-abap-environment-apis-with-postman-using-oauth-2.0-authorization-code-grant/
source: SAP Blogs
date: 2023-07-12
fetch_date: 2025-10-04T11:54:55.641640
---

# Manually Testing SAP BTP ABAP Environment APIs with Postman using OAuth 2.0 Authorization Code Grant

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Manually Testing SAP BTP ABAP Environment APIs wit...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160069&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Manually Testing SAP BTP ABAP Environment APIs with Postman using OAuth 2.0 Authorization Code Grant](/t5/technology-blog-posts-by-sap/manually-testing-sap-btp-abap-environment-apis-with-postman-using-oauth-2-0/ba-p/13556445)

![former_member239751](https://avatars.profile.sap.com/former_member_small.jpeg "former_member239751")

[former\_member239751](https://community.sap.com/t5/user/viewprofilepage/user-id/239751)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160069)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160069)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556445)

‎2023 Jul 11
9:23 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160069/tab/all-users "Click here to see who gave kudos to this post.")

7,689

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

View products (2)

There are already some blogs out there outlining ways to test your APIs developed on SAP BTP ABAP Environment e.g. using cookies from ABAP Development Tools (see [here](https://blogs.sap.com/2021/07/27/manual-testing-of-apis-in-sap-btp-abap-environment-using-postman/)) or other SAP BTP APIs using the OAuth 2.0 password grant (see [here](https://blogs.sap.com/2020/03/02/using-postman-for-api-testing-with-xsuaa/)).

With this blog I want to add another option that Postman offers and that is possible to be used with SAP BTP ABAP Environment: The OAuth 2.0 Authorization Code Grant

What you need:

* Postman

* Service key of your SAP BTP ABAP Environment service instance

* An API you want to test and have access to with your Business User

What you get:

* Quick way to test your ABAP APIs without including them in communication scenarios of IAM Apps / business catalogs (provided you do this in your development system)

* Access to the API with your own user without the need for a technical user

* Support for most authentication flows that your Identity Provider might require (e.g. 2-Factor)

# Get the Service Key

In the SAP BTP Cockpit navigate to your BTP ABAP Environment service instance and create a service key for it, which contains the required OAuth 2.0 credentials for the Authorization Code grant.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.29.35.png)

SAP BTP ABAP Environment Service Key

# Prepare Postman

1. In Postman start off with an empty request and navigate to the *Authorization*pane

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.32.00.png)

Postman Authorization pane

2. Choose **OAuth 2.0** as Authorization *Type,* select *Add authorization data to* **Request Headers** and scroll down to *Configure a New Token*

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.34.13.png)

Configure New Token

3. Provide a *Token Name*, select **Authorization Code** as *Grant Type* and enter **[http://localhost:8080](http://localhost:8080 )**as Callback URL (port doesn't really matter, but needs to be filled)

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.36.00.png)

Initial Configuration

4. Now fetch the *url, clientid* and *clientsecret*values from the *uaa* section of your SAP BTP ABAP Environment service key

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.37.32.png)

UAA Service Key Section

5. Use the URL from the service key and append **/oauth/authorize** for the *Auth URL* and **/oauth/token** for the *Access Token URL*

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.41.17.png)

Auth URL

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.41.46.png)

Access Token URL

6. Finally use the *clientid*and *clientsecret*values for the *Client ID*and *Client Secret*fields respectively

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.44.22.png)

Client ID / Secret

7. Use the *Get New Access Token*button at the bottom to start the authentication flow, which depends on your concrete trust configuration

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.46.45.png)

Get New Access Token

8. Once authenticated you can *Use the Token*for your Postman request

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.48.29.png)

Use Token

# Test your API

Use the URL of the SAP BTP ABAP Environment instance from your service key (not the one from the uaa section) to call any API your user has authorizations for

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-10-at-16.52.08.png)

Execute ABAP API

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [OAuth](/t5/tag/OAuth/tg-p/board-id/technology-blog-sap)
* [postman](/t5/tag/postman/tg-p/board-id/technology-blog-sap)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fmanually-testing-sap-btp-abap-environment-apis-with-postman-using-oauth-2-0%2Fba-p%2F13556445%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Creating a Hybrid CAP (Node.js) Profile with PostgreSQL on BTP from Business Application Studio](/t5/technology-blog-posts-by-members/creating-a-hybrid-cap-node-js-profile-with-postgresql-on-btp-from-business/ba-p/14233631)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [Login Failure to SAP BTP - ABAP Environment](/t5/technology-q-a/login-failure-to-sap-btp-abap-environment/qaq-p/14231845)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday
* [From REST to Datasphere: A C...