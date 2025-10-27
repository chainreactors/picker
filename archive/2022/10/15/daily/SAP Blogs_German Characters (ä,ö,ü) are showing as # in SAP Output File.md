---
title: German Characters (ä,ö,ü) are showing as # in SAP Output File
url: https://blogs.sap.com/2022/10/14/german-characters-aou-are-showing-as-in-sap-output-file/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:21.586536
---

# German Characters (ä,ö,ü) are showing as # in SAP Output File

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* German Characters (ä,ö,ü) showing as # in SAP Outp...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66467&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [German Characters (ä,ö,ü) showing as # in SAP Output File](/t5/enterprise-resource-planning-blog-posts-by-members/german-characters-%C3%A4-%C3%B6-%C3%BC-showing-as-in-sap-output-file/ba-p/13543501)

![kiranchavan0912](https://avatars.profile.sap.com/2/1/id21e77e5d4804dd6e9f376c90fb45c5f77e8bf9c7f489f91e512219783cad0f1c_small.jpeg "kiranchavan0912")

[kiranchavan0912](https://community.sap.com/t5/user/viewprofilepage/user-id/808708)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66467)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66467)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543501)

‎2022 Oct 14
9:24 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66467/tab/all-users "Click here to see who gave kudos to this post.")

2,588

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

Hello Everyone,

Recently I came across the issue related to output device configuration in sap, hence thought of sharing the resolution with all of you.

**Scenario:**

We have an output device set for Printing Using E-Mail in our SAP system. This means, Basically you have to specify output device in the print window  i.e output device with Access Method - M and It creates an output that sends the print data as an attachment to an e-mail. The user requirement was to get that output attachment in .TXT file format and we had an output device setup with device type **ASCIIPRI,**which was fulfilling the requirement.

The twist here is, with current setup the German letters (ä,ö,ü) are showing as # in the text file.

**Solution:**

Here, the challenge was to find the device type which can export the output to email in .TXT file  format and which can support the German characters (ä,ö,ü) too.

After much research, We found SAP has Unicode-capable version of ASCIIPRI called UTF8PRI ![:victory_hand:](/html/@78457C1C3A3DCF6290E17D81D9DA6EFD/emoticons/270c.png ":victory_hand:"), Thankfully our system was in higher release i.e S4HANA 1909 SP05 (SAP\_BASIS release 754 ), UTF8PRI device type was already available.

We created new unicode output device with below configuration and this had solved our issue.

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog2-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog3-2.png)

If you are on lower SAP version **UTF8PRI** device type might not be available in your system, In such case kindly follow the steps mentioned in SAP note #1673313

**Reference:**

<https://launchpad.support.sap.com/#/notes/1673313>

Hope this blog will help you to solve your issue too![:grinning_face_with_sweat:](/html/@2EEAE894AF027E0461DA2E103D51DB18/emoticons/1f605.png ":grinning_face_with_sweat:")

***Requesting all readers to drop your feedback or thoughts in comments, also post your questions, if you have any, I will try to answer to the best of my knowledge and research.***

***Do follow my profile to see more useful contents related to SAP BASIS and HANA topics in near future.***

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fgerman-characters-%25C3%25A4-%25C3%25B6-%25C3%25BC-showing-as-in-sap-output-file%2Fba-p%2F13543501%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Packing List form issue in public cloud.](/t5/enterprise-resource-planning-q-a/packing-list-form-issue-in-public-cloud/qaq-p/14230590)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Monday
* [Extensibility Assistant for Key Users: The extensibility expert right next to you](/t5/enterprise-resource-planning-blog-posts-by-sap/extensibility-assistant-for-key-users-the-extensibility-expert-right-next/ba-p/14216097)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Mass Download Of Attachment In SAP Document / Invoice - SAP S4HANA / FICO](/t5/enterprise-resource-planning-blog-posts-by-members/mass-download-of-attachment-in-sap-document-invoice-sap-s4hana-fico/ba-p/14211434)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 weeks ago
* [SAP B1: Formatted Search auto-trigger on header UDF does not fire (manual run works)](/t5/enterprise-resource-planning-q-a/sap-b1-formatted-search-auto-trigger-on-header-udf-does-not-fire-manual-run/qaq-p/14211012)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  4 weeks ago
* [Purchasing Planning Monitor for Collective Evaluation of MRP Planning Results](/t5/enterprise-resource-planning-blog-posts-by-sap/purchasing-planning-monitor-for-collective-evaluation-of-mrp-planning/ba-p/14200697)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 02

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![former_member816598](https://avatars.profile.sap.com/former_member_small.jpeg "former_member816598")  former\_member816598](/t5/user/viewprofilepage/user-id/816598) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  arghadipkar3013](/t5/user/viewprofilepage/user-id/686417) | 2 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![vianshu](https://avatars.profile.sap.com/7/3/id73f851dd2d601f9bd347d78ecfa46602245b7e89d831c26845276966f760a654_small.jpeg "vianshu")  vianshu](/t5/user/viewprof...