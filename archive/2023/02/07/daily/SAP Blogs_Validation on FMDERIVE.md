---
title: Validation on FMDERIVE
url: https://blogs.sap.com/2023/02/06/validation-on-fmderive/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:14.815315
---

# Validation on FMDERIVE

* [SAP Community](/)
* [Archived Community Content](/t5/archived-content/ct-p/Archive)
* [Archived Groups](/t5/archived-groups/ct-p/archivedgroups)
* [Industry Groups](/t5/industry-groups/ct-p/IndustryGroups)
* [SAP for Public Sector](/t5/sap-for-public-sector/gh-p/public-sector)
* [Blogs](/t5/sap-for-public-sector-blogs/bg-p/public-sectorblog-board)
* Validation on FMDERIVE

SAP for Public Sector Blogs

Read and write blog posts showcasing creative initiatives, technology advancements, and success stories in public sector transformation powered by SAP.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/public-sectorblog-board/article-id/631&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

The SAP for Public Sector group was sunset as of July 2025, and has therefore been set to read-only.

Read only

## [Validation on FMDERIVE](/t5/sap-for-public-sector-blogs/validation-on-fmderive/ba-p/13562332)

![anss_shahid](https://avatars.profile.sap.com/3/a/id3af9c1bd9027ec5c878cf1eeaa0d004d29f08b955b19d1b493a285d1f7d7e362_small.jpeg "anss_shahid")

[anss\_shahid](https://community.sap.com/t5/user/viewprofilepage/user-id/203467)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=public-sectorblog-board&message.id=631)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/public-sectorblog-board/article-id/631)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562332)

‎2023 Feb 06
7:51 PM

[6
Kudos](/t5/kudos/messagepage/board-id/public-sectorblog-board/message-id/631/tab/all-users "Click here to see who gave kudos to this post.")

5,254

* SAP Managed Tags
* [Public Sector](https://community.sap.com/t5/c-khhcw49343/Public%2520Sector/pd-p/130110653021563432906662)

* [Public Sector

  Industry](/t5/c-khhcw49343/Public%2BSector/pd-p/130110653021563432906662)

View products (1)

**Introduction:**

I received a question from one of my professional colleagues for any possibilities of implementing Validations on FMDERIVER. He asked if we could generate a customized error message if the user enters an invalid combination of Commitment Item and Functional Area.

**Solution:**

We can implement the required validations using “BADI\_FMDERIVE” and method "CHECK\_DRULE\_BEFORE\_SAVE".

**Identify the Table of the Derivation Step:**

To identify the table of the derivation step where the validation is to be implemented, you can perform the steps below:

1. In my test environment, I am selecting the Step No. 18 of the FMDERIVE Derivation Rule with the Functional Area as the Source Field and Commitment Item as Target Field.

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-0.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-1-1.jpg)

2. Next Go to T-Code: SE16n and Enter the Table "TABADRS". Enter the values in the field as below:

* Application Class will always be "FM"

* Subclass will always be "01"

* Strategy ID will always be "FMOA"

* Environment strat represents the "FM Area" of the implementation

* Seq. number represents the "Step No".

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-3.jpg)

* After executing, the table will be found in the Parameter (PARAM\_1)

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-4-1.jpg)

In this case, we have identified that the table name is "FMFMOADEV8000055".

**Implement BADI\_FMDERIVE:**

You can implement the BADI via SE18 with the help of the ABAP Consultant. For validation of values, select the method "CHECK\_DRULE\_BEFORE\_SAVE".

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-5.jpg)

Within this method, you can write up the logic that needs to be implemented for the validation checks. For the purpose of this blog only, I implemented the below logic where the system will check the combination of new entries within the derivations rules and validate it if incorrect combination is maintained.

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-6-1.jpg)

* Please note that the Parameter "I\_TAB\_NEW\_ENTRIES" contains 2 important components "S-1-Val" which represents the source value and "T-1-Val" which represents the target value.

**Maintain FMDERIVER:**

Now when you maintain the values in FMDERIVER Derivation step, it will generate error message as if the Incorrect Combination is met.

![](/legacyfs/online/storage/blog_attachments/2023/02/Pic-7.jpg)

**Opportunity for Improvements:**

Instead of hardcoding the values, you can discuss with your ABAP consultants of configuring the combination variables in transparent tables which can be maintained using SM30. Now this depends on your experience and the complexity of the business requirements.

**Conclusion:**

Every business have different and unique requirements and have many variations. The above scenario is only for the purpose of sharing the knowledge with the SAP FM Consultants all over the world who may benefit from this tool. You can take this blog as a bench mark to have an initial idea and then modify it according to your requirements.

Best Regards,

Anss Shahid

* [BADI\_FMDERIVE](/t5/tag/BADI_FMDERIVE/tg-p/board-id/public-sectorblog-board)
* [Derivation Rules](/t5/tag/Derivation%20Rules/tg-p/board-id/public-sectorblog-board)
* [fmderive](/t5/tag/fmderive/tg-p/board-id/public-sectorblog-board)
* [fmderiver](/t5/tag/fmderiver/tg-p/board-id/public-sectorblog-board)
* [sap fm](/t5/tag/sap%20fm/tg-p/board-id/public-sectorblog-board)
* [Validations Rules](/t5/tag/Validations%20Rules/tg-p/board-id/public-sectorblog-board)

2 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin