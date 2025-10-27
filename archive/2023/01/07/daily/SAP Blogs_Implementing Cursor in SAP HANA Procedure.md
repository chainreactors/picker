---
title: Implementing Cursor in SAP HANA Procedure
url: https://blogs.sap.com/2023/01/06/implementing-cursor-in-sap-hana-procedure/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:14:58.135137
---

# Implementing Cursor in SAP HANA Procedure

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Implementing Cursor in SAP HANA Procedure

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159474&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implementing Cursor in SAP HANA Procedure](/t5/technology-blog-posts-by-members/implementing-cursor-in-sap-hana-procedure/ba-p/13546408)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159474)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159474)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13546408)

‎2023 Jan 06
10:41 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159474/tab/all-users "Click here to see who gave kudos to this post.")

11,756

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

In some business scenario need to parse the data and need to implement the loop and using calculation view it is not possible. The Cursor in SAP HANA procedure can be used for other purpose also.

Let's implement one scenario by creating a procedure using cursor -

Cursor Syntax -

```
DO

BEGIN

	DECLARE CURSOR DEMO_CUR1 for

		SELECT EMAIL ID FROM "PLB_MTA.DB_PLB"::"EMPLOYEE";

	FOR CURSORROW AS DEMO_CUR1

	DO

	/* YOUR CODE/*

	END FOR;

END
```

Scenario -

EMPLOYEE table Structure -

![](/legacyfs/online/storage/blog_attachments/2023/01/11.png)

Now we want to update salary of those employee under salary 30000 to input target salary using cursor.

```
CREATE PROCEDURE "PLB_MTRA.DB_PLB"::"DEMO_CURSOR" (

        IN TRGT_SALARY DECIMAL(10,2),

        OUT EMP "PLB_MTRA.DB_PLB"::"EMPLOYEE")

    LANGUAGE SQLSCRIPT

    SQL SECURITY INVOKER

    AS

BEGIN

DECLARE NEW_SALARY DECIMAL(10,2);

DECLARE CURSOR DEMO_CUR1 for

	SELECT EMP_ID,SALARY from FROM "PLB_MTA.DB_PLB"::"EMPLOYEE";

FOR CURSORROW AS DEMO_CUR1

DO

 NEW_SALARY := CURSORROW.SALARY;

 IF (:NEW_SALARY < 31000) then

   NEW_SALARY := TRGT_SALARY;

   UPDATE "PLB_MTRA.DB_PLB"::"EMPLOYEE"

   SET SALARY = NEW_SALARY where EMP_ID = CURSORROW.EMP_ID;

  END IF;

 EMP = select EMP_ID, EMP_NAME, EMAIL_ID, SALARY FROM "PLB_MTA.DB_PLB"::"EMPLOYEE";

 RETURN EMP;

END FOR;

END;
```

Call the Procedure  . You will get the updated data.

```
 CALL "PLB_MTRA.DB_PLB"::"DEMO_CURSOR" (60000,?);
```

You will get the below -

![](/legacyfs/online/storage/blog_attachments/2023/01/updated.png)

Hope it will help in your project for other scenario to write cursor in HANA procedure.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fimplementing-cursor-in-sap-hana-procedure%2Fba-p%2F13546408%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [The Ultimate SAP S/4HANA Master Data Guide & Test Plan](/t5/technology-blog-posts-by-members/the-ultimate-sap-s-4hana-master-data-guide-amp-test-plan/ba-p/14228211)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Enabling AD -based Kerberos for Windows, MacBook, and Desktop Linux](/t5/technology-blog-posts-by-members/enabling-ad-based-kerberos-for-windows-macbook-and-desktop-linux/ba-p/14228175)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [AI Assisted Data Quality Screening in SAP Business Data Cloud](/t5/technology-blog-posts-by-members/ai-assisted-data-quality-screening-in-sap-business-data-cloud/ba-p/14218695)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Demystifying the OAuth2 SAML Bearer Assertion usage in SAP Integration Suite](/t5/technology-blog-posts-by-sap/demystifying-the-oauth2-saml-bearer-assertion-usage-in-sap-integration/ba-p/14177915)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 weeks ago
* [A simple example of a SAP RAP Application based on Legacy API without UUID keys](/t5/technology-blog-posts-by-members/a-simple-example-of-a-sap-rap-application-based-on-legacy-api-without-uuid/ba-p/14184282)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") MioYasutake](/t5/user/viewprofilepage/user-id/789) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")  Sharathmg](/t5/user/viewprofilepage/user-id/174516) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewprofilepage/user-id/197587) | 3 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natana...