---
title: SAP Fiori Elements preview fails with underscore character in hostname
url: https://blogs.sap.com/2022/11/25/sap-fiori-elements-preview-fails-with-underscore-character-in-hostname/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:48:42.837624
---

# SAP Fiori Elements preview fails with underscore character in hostname

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori Elements preview fails with underscore c...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160911&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Elements preview fails with underscore character in hostname](/t5/technology-blog-posts-by-sap/sap-fiori-elements-preview-fails-with-underscore-character-in-hostname/ba-p/13559051)

![Andre_Fischer](https://avatars.profile.sap.com/a/6/ida655827d8a31777be0763b58b458b654e4e62b0aa9c88ee1658ce78b56fe5810_small.jpeg "Andre_Fischer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andre\_Fischer](https://community.sap.com/t5/user/viewprofilepage/user-id/55)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160911)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160911)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559051)

‎2022 Nov 25
7:24 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160911/tab/all-users "Click here to see who gave kudos to this post.")

1,602

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

## The problem:

When using the Fiori Elements preview for a RAP business object in an on-premise SAP S/4HANA test system I ran into the problem that the SAP Fiori Elements preview did not work.

Instead I got the following error message: “Host and port configuration information is missing”

![](/legacyfs/online/storage/blog_attachments/2022/11/Host-and-port-configuration-information-is-missing.png)

## The solution:

The root cause of this problem was that the hostname that was configured in table HTTPURLLOC in our SAP S/4HANA on premise demo system contained an underscore "\_".

The field for the host name with domain contained the value

2022\_SP00\_SANDBOX.S4HANA.ONLY.SAP

However, underscore characters are illegal in host names as I learned from our ADT development team, which is described here:

<https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames>

Though it works in tools such as Chrome / Firefox / ...(which do not follow the standard strictly), the URI parser in Java is very strict:

```
jshell> URI.create("https://2022_SECOND_SANDBOX.S4HANA.ONLY.COM:44301/sap/bc/adt").getHost()

$19 ==> null
```

and as a result the hostname is lost.

Using e.g. "-" instead of "\_" solves this:

```
jshell> URI.create("https://2022-SECOND-SANDBOX.S4HANA.ONLY.COM:44301/sap/bc/adt").getHost()

$20 ==> "2022-SECOND-SANDBOX.S4HANA.ONLY.COM"
```

When using a hostname that contains underscores will also cause that the URL that is generated when trying to share source code via a http link in ADT will generate a URL without a hostname nor a port information that will hence not work.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-fiori-elements-preview-fails-with-underscore-character-in-hostname%2Fba-p%2F13559051%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [IBM MQ JMS Adapter for SAP Integration Suite](/t5/technology-blog-posts-by-sap/ibm-mq-jms-adapter-for-sap-integration-suite/ba-p/14097082)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 May 09
* [Troubleshooting Access to a Specific Application Server in SAPGUI for Java](/t5/technology-blog-posts-by-sap/troubleshooting-access-to-a-specific-application-server-in-sapgui-for-java/ba-p/14075030)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Apr 14
* [SAP BI 2025: What’s New In Web Intelligence and Semantic Layer](/t5/technology-blog-posts-by-sap/sap-bi-2025-what-s-new-in-web-intelligence-and-semantic-layer/ba-p/14033408)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Mar 12
* [CDS Access Controls 7.5x Quick Reference](/t5/technology-blog-posts-by-members/cds-access-controls-7-5x-quick-reference/ba-p/13986001)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Jan 17
* [Enabling Access to On-Premise S/4HANA Applications in SAP Build Work Zone, Standard Edition](/t5/technology-blog-posts-by-members/enabling-access-to-on-premise-s-4hana-applications-in-sap-build-work-zone/ba-p/13935816)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2024 Nov 18

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457dbe84b4_small.jpeg "FranciscoHurtado")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") FranciscoHurtado](/t5/user/viewprofilepage/user-id/170459) | 10 |
| [![CarineTchoutouo](https://avatars.profile.sap.com/9/d/id9d3dd02b884098ed83600846c6bfd4f3b6aba5b4657b084d98aea0fc87214b66_small.jpeg "CarineTchoutouo")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_...