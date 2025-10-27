---
title: Cloud Integration in GO (CIG) Desktop version – transports management
url: https://blogs.sap.com/2023/03/27/cloud-integration-in-go-cig-desktop-version-transports-management/
source: SAP Blogs
date: 2023-03-28
fetch_date: 2025-10-04T10:51:19.895808
---

# Cloud Integration in GO (CIG) Desktop version – transports management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cloud Integration in GO (CIG) Desktop version - tr...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161985&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Integration in GO (CIG) Desktop version - transports management](/t5/technology-blog-posts-by-members/cloud-integration-in-go-cig-desktop-version-transports-management/ba-p/13560896)

![tobiasz_h](https://avatars.profile.sap.com/c/d/idcdb5db2c7542783d6b4ac79922b1cd34910c0d8ca1c427050c545bc0dfbe9b3f_small.jpeg "tobiasz_h")

[tobiasz\_h](https://community.sap.com/t5/user/viewprofilepage/user-id/12314)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161985)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161985)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560896)

‎2023 Mar 27
4:25 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161985/tab/all-users "Click here to see who gave kudos to this post.")

1,031

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (1)

A few months ago, I published a post related to the CLI tool for Cloud Integration.
Here is a link to that post: <https://blogs.sap.com/2022/08/26/cloud-integration-cli-in-golang-cig/>

Now the time has come for a desktop version for this tool - I have named it cigDesktop.

The application can be run on Windows, macOS and linux systems. I have put the executable files for windows/amd64 on Github.
At the moment, this application solves the problem of transferring/transporting integration flows between different tenants. The application can also be used to move iflow in the same tenant.

The main advantages of using the app:

* When you do the iflow transport the first time - the configuration parameters are taken from source system

* When you do the iflow transport next time - there is no need to create the configuration parameters from scratch.

* The transported iflow is transferred as a new version to the target system. You have access to earlier versions.

* It is possible to change the Id and Name of the iflow during transport.

* intuitive interface

The project repository is available at:
<https://github.com/tobiaszgithub/cigDesktop>

Executable files for the windows operating system are available at:
<https://github.com/tobiaszgithub/cigDesktop/releases>

Some screenshots of the app:
![](/legacyfs/online/storage/blog_attachments/2023/03/ice_screenshot_20230327-152629-1.png)

Integration flows View

![](/legacyfs/online/storage/blog_attachments/2023/03/ice_screenshot_20230327-152712.png)

Transport View

![](/legacyfs/online/storage/blog_attachments/2023/03/ice_screenshot_20230327-152737.png)

Settings View

This is the first version of the app, I have some ideas on what to improve and what can be added.

* [CPI](/t5/tag/CPI/tg-p/board-id/technology-blog-members)
* [GoLangauge](/t5/tag/GoLangauge/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcloud-integration-in-go-cig-desktop-version-transports-management%2Fba-p%2F13560896%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") smarchesini](/t5/user/viewprofilepage/user-id/125739) | 3 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewprofilepage/user-id/197587) | 3 |
| [![Sharathmg](https://avatars.profile.sap.c...