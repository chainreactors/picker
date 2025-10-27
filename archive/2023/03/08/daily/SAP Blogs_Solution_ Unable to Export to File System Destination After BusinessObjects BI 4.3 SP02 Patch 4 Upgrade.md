---
title: Solution: Unable to Export to File System Destination After BusinessObjects BI 4.3 SP02 Patch 4 Upgrade
url: https://blogs.sap.com/2023/03/07/solution-unable-to-export-to-file-system-destination-after-businessobjects-bi-4.3-sp02-patch-4-upgrade/
source: SAP Blogs
date: 2023-03-08
fetch_date: 2025-10-04T08:54:53.598124
---

# Solution: Unable to Export to File System Destination After BusinessObjects BI 4.3 SP02 Patch 4 Upgrade

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Solution: Unable to Export to File System Destinat...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162888&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Solution: Unable to Export to File System Destination After BusinessObjects BI 4.3 SP02 Patch 4 Upgrade](/t5/technology-blog-posts-by-members/solution-unable-to-export-to-file-system-destination-after-businessobjects/ba-p/13566341)

![nscheaffer](https://avatars.profile.sap.com/f/3/idf3119ffa8989320a4d37800115970326838e841af49d6f6e04634d4bf1e2e4f9_small.jpeg "nscheaffer")

[nscheaffer](https://community.sap.com/t5/user/viewprofilepage/user-id/8619)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162888)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162888)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566341)

‎2023 Mar 07
8:57 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162888/tab/all-users "Click here to see who gave kudos to this post.")

9,384

* SAP Managed Tags
* [SAP BusinessObjects Business Intelligence platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520Business%2520Intelligence%2520platform/pd-p/01200314690800000337)

* [SAP BusinessObjects Business Intelligence platform

  SAP BusinessObjects Business Intelligence](/t5/c-khhcw49343/SAP%2BBusinessObjects%2BBusiness%2BIntelligence%2Bplatform/pd-p/01200314690800000337)

View products (1)

**Update**: Based on the comment from ayman.salem the better solution is to create a  Destination\_AllowList.txt file as described in KBA [2477817](https://launchpad.support.sap.com/#/notes/2477817).

---

We are on BusinessObjects BI 4.2 SP09 Patch 4 and are in the final stages of preparing to upgrade to BI 4.3 SP02 Patch 8. I realized I had not yet tested saving to the File System as a delivery destination in our test environment so I give it a try. It did not work. I kept getting this error...
> destination file error. [CrystalEnterprise.DiskUnmanaged]: [{1}]

I checked the properties of the File System destination within the properties of my AdaptiveJobServer. Everything looked as it should...

![](/legacyfs/online/storage/blog_attachments/2023/03/AdaptiveJobServer-Settings.jpg)

Unfortunately, I had not tested this immediately prior to the upgrade in our test environment so I was not sure that it was working before. I could create a file in my the desired network location from the BOBJ server as the same user I was putting in the File System destination settings which was also the same user running the SIA (Server Intelligence Agent). I could send my scheduled report results to the Email or BI Inbox destinations, but not the File System destination. I spent about an hour trying different things, but still no success.

So yesterday I reached out to our SAP Support Provider and I got on the phone with a representative for about a hour checking and trying a bunch of different things with no success. We connected again today and after about 30 minutes of poking around he suggested we replace the DLL corresponding to the File System destination with a copy from another environment. The file in question is **dest\_CrystalEnterprise\_DiskUnmanaged.dll** in the **<InstallDirectory>\SAP BusinessObjects Enterprise XI 4.0\win64\_x64 directory**.

I renamed that file in our test system, located it in our production system, and copied it to our test system. Keep in mind our production system is BI 4.2 SP09 Patch 4. Next I restarted the test system  AdaptiveJobServer. It worked!

As an aside, I learned if you have your User Name and Password defined in the File System destination settings of your AdaptiveJobServer you can omit them in your schedule as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/03/File-System-Destination.jpg)

* [BOBJScheduling](/t5/tag/BOBJScheduling/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsolution-unable-to-export-to-file-system-destination-after-businessobjects%2Fba-p%2F13566341%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [ABAP's Parallel Processing Frameworks: Practical Guide to Performance Tuning of Mass Data Processing](/t5/technology-blog-posts-by-sap/abap-s-parallel-processing-frameworks-practical-guide-to-performance-tuning/ba-p/14224397)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [SAP Build Work Zone Meets Multi-Tenancy](/t5/technology-blog-posts-by-sap/sap-build-work-zone-meets-multi-tenancy/ba-p/14228480)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [A New Home for SAP Enterprise Support Value Maps on SAP Community](/t5/technology-blog-posts-by-sap/a-new-home-for-sap-enterprise-support-value-maps-on-sap-community/ba-p/14222693)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [NDC Converter 2.0: Automating Your Journey from BusinessObjects to Cloud Analytics](/t5/technology-q-a/ndc-converter-2-0-automating-your-journey-from-businessobjects-to-cloud/qaq-p/14226676)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec9...