---
title: HTTP Strict Transport Security (HSTS) With SAP BusinessObjects BI Web Applications
url: https://blogs.sap.com/2022/12/06/http-strict-transport-security-hsts-with-sap-businessobjects-bi-web-applications/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:05.771122
---

# HTTP Strict Transport Security (HSTS) With SAP BusinessObjects BI Web Applications

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* HTTP Strict Transport Security (HSTS) With SAP Bus...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162750&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HTTP Strict Transport Security (HSTS) With SAP BusinessObjects BI Web Applications](/t5/technology-blog-posts-by-sap/http-strict-transport-security-hsts-with-sap-businessobjects-bi-web/ba-p/13564798)

![HariPrasadChennamadhavuni](https://avatars.profile.sap.com/a/d/idadd3e94ca4924ee91338f3f1fb5f0751d69297ef441ab29e2600557ee86bec01_small.jpeg "HariPrasadChennamadhavuni")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[HariPrasadChennamadhavuni](https://community.sap.com/t5/user/viewprofilepage/user-id/274475)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162750)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162750)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564798)

‎2022 Dec 06
11:05 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162750/tab/all-users "Click here to see who gave kudos to this post.")

4,948

* SAP Managed Tags
* [SAP BusinessObjects Business Intelligence platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520Business%2520Intelligence%2520platform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Platform Administration](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Platform%2520Administration/pd-p/493706448058243238508632186627562)
* [SAP BusinessObjects - Platform Infrastructure](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Platform%2520Infrastructure/pd-p/908268185089197093202840551891078)

* [SAP BusinessObjects Business Intelligence platform

  SAP BusinessObjects Business Intelligence](/t5/c-khhcw49343/SAP%2BBusinessObjects%2BBusiness%2BIntelligence%2Bplatform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Platform Administration

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BPlatform%2BAdministration/pd-p/493706448058243238508632186627562)
* [SAP BusinessObjects - Platform Infrastructure

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BPlatform%2BInfrastructure/pd-p/908268185089197093202840551891078)

View products (3)

This blog is about another important security enhancement delivered in **SAP BusinessObjects 4.3 SP03 release**, which is support for the **HTTP Strict Transport Security(HSTS)** policy mechanism. As we know, HSTS is the web security policy mechanism; with the support of this policy in the BI Platform, now the BI end-users and BI Administrators will be able to access BI Launchpad, OpenDocument, and Central Management Console more secure way. For more information about HSTS and a better understanding of the policy, refer to the following [blog](https://blogs.sap.com/2014/04/26/http-strict-transport-security-hsts/).

**Note:**

The Strict-Transport-Security header is ignored by the browser when your site has only been accessed using HTTP. Once your site is accessed over HTTPS with no certificate errors, the browser knows your site is HTTPS capable and will honour the Strict-Transport-Security header. This means until the BI end user accesses the HTTPS URL first time, the browser will not auto-convert any HTTP URL to the HTTPS URL in that end-user system, even though the Server can do HTTPS communication and enable HSTS policy.

**How to Implement HSTS in your BI Landscape’s Web deployment system :**

As obvious, the first thing is configuring the Web Tier server (The application server on which the SAP BusinessObjects Web Applications are deployed) should be configured with HTTPS (that is, SSL/TLS) to enable the HSTS. Once SSL is enabled, please follow the below steps.

1. 1. Navigate to <BO\_Install\_Dir>\SAP BusinessObjects Enterprise XI 4.0\warfiles\webapps\BOE\WEB-INF\config\custom

   2. Create a PROPERTIES file with the name “global.properties”

   3. Open in any text editor and enter the following text

      ```
      hsts.enabled=true

      hsts.Include.SubDomains=true

      hsts.MaxAge.Seconds=31536000​
      ```

   4. Save the file.

   5. Re-deploy the BOE.war file; refer to the following note [2723514](https://launchpad.support.sap.com/#/notes/0002723514).

**Verification:**

How to find that the BI system is added to the Browser domain?

1. Open Google Chrome

2. Search for **chrome://net-internals/#hsts**in the address bar

3. In the **Query HSTS/PKP domain**field, type in the domain name for which you want to fetch the HSTS settings. This should return some values.

4. you can find HSTS domain details

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [BI4.3SP03](/t5/tag/BI4.3SP03/tg-p/board-id/technology-blog-sap)
* [bobi](/t5/tag/bobi/tg-p/board-id/technology-blog-sap)
* [bobj](/t5/tag/bobj/tg-p/board-id/technology-blog-sap)
* [boe](/t5/tag/boe/tg-p/board-id/technology-blog-sap)
* [BOE.WAR](/t5/tag/BOE.WAR/tg-p/board-id/technology-blog-sap)
* [hsts](/t5/tag/hsts/tg-p/board-id/technology-blog-sap)
* [HTTP Strict Transport Security](/t5/tag/HTTP%20Strict%20Transport%20Security/tg-p/board-id/technology-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fhttp-strict-transport-security-hsts-with-sap-businessobjects-bi-web%2Fba-p%2F13564798%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Top 10 SAP Cloud ALM News September 2025](/t5/technology-blog-posts-by-sap/top-10-sap-cloud-alm-news-september-2025/ba-p/14230396)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate Guide to SAP S/4HANA Master Data Management](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-management/ba-p/14229434)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Friday
* [What’s New in SAP HANA Cloud – September 2025](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-hana-cloud-septembe...