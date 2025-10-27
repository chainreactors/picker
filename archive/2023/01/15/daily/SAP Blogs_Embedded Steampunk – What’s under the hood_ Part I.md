---
title: Embedded Steampunk – What’s under the hood? Part I
url: https://blogs.sap.com/2023/01/14/embedded-steampunk-whats-under-the-hood-part-i/
source: SAP Blogs
date: 2023-01-15
fetch_date: 2025-10-04T03:56:38.755078
---

# Embedded Steampunk – What’s under the hood? Part I

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Embedded Steampunk - What's under the hood? Part I

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163077&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Embedded Steampunk - What's under the hood? Part I](/t5/technology-blog-posts-by-members/embedded-steampunk-what-s-under-the-hood-part-i/ba-p/13567515)

![amangarg1](https://avatars.profile.sap.com/8/f/id8f6af096c82ae9d45cd6649babc0a7426fef5f4175b47a3bcae1ed9b04aac701_small.jpeg "amangarg1")

[amangarg1](https://community.sap.com/t5/user/viewprofilepage/user-id/14709)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163077)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163077)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567515)

‎2023 Jan 14
9:41 PM

[21
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163077/tab/all-users "Click here to see who gave kudos to this post.")

12,269

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (5)

> Steampunk is now officially ABAP Cloud, as announced in SAP TechEd 2022.

Does this mean Embedded Steampunk is now Embedded ABAP Cloud? Not sure? Me too ![:grinning_face_with_smiling_eyes:](/html/@CB5FC51E90068B5623B30B421915E8BD/emoticons/1f604.png ":grinning_face_with_smiling_eyes:") so let's call it Embedded Steampunk for now.

***Update: The term Embedded Steampunk is now replaced with "The SAP S/4HANA Cloud ABAP Environment", as suggested in this [blog](https://blogs.sap.com/2022/09/01/evolution-of-abap/)***

I was lucky to get an opportunity to try my hands on SAP S/4 HANA 2022 on premise system recently. I tried out different new features in the new system, but what I focused on most was Embedded Steampunk.

Welcome to this series of blog posts, where I will try to share the learnings and findings from my hands on experience with Embedded Steampunk (hyperlinks to topics #3,4 will be updated here once they are published):

1. [How to use Embedded Steampunk in S/4 HANA 2022 on premise system](https://blogs.sap.com/2023/01/14/embedded-steampu%E2%80%A6-the-hood-part-i/)(current topic),

2. [RAP as the programming model of choice in Embedded Steampunk](https://blogs.sap.com/2023/01/21/embedded-steampunk-whats-under-the-hood-part-ii/),

3. [Restricted ABAP in Embedded Steampunk with tried out examples](https://blogs.sap.com/2023/02/11/embedded-steampunk-whats-under-the-hood-part-iii/),

4. ADT tips which might be useful.

For the people who are alien to the term Embedded Steampunk (just like I was few months back ![:grinning_face_with_smiling_eyes:](/html/@CB5FC51E90068B5623B30B421915E8BD/emoticons/1f604.png ":grinning_face_with_smiling_eyes:") ), I would recommend to go through below blogs, which are very helpful in understanding what exactly Embedded Steampunk is. Since there are already detailed blog explaining what Embedded steampunk is, I will keep this blog series focused on findings

[Embedded Steampunk - Some more details for ABAP developers](https://blogs.sap.com/2022/09/05/embedded-steampunk-some-more-details-for-abap-developers/)

[Steampunk is going all-in](https://blogs.sap.com/2021/09/30/steampunk-is-going-all-in/)

### **How to use Embedded Steampunk in SAP S/4 HANA 2022 on premise system**

**Step 1:**

Open/create an object in ADT which you want to build on Embedded Steampunk. Let's consider a simple CDS in our example.

**Step 2:**

Click Properties icon in ADT to open properties of the selected object

![](/legacyfs/online/storage/blog_attachments/2023/01/1-22.png)

Object Properties in ADT

**Step 3:**

Go to General tab in the properties to see the ABAP language version

![](/legacyfs/online/storage/blog_attachments/2023/01/2-13.png)

ABAP Language version

**Step 4:**

Click Browse, and select ABAP Language version as ABAP for Cloud Development.

*Note: The language version ABAP for Cloud Development was called with different names in past, however, this is the latest name as of now.*

![](/legacyfs/online/storage/blog_attachments/2023/01/3-8.png)

ABAP for Cloud development

That's it. The object is now enabled for ABAP for Cloud Development

**What does this mean?**

This means:

1. Strict syntax and runtime checks for this object,

2. You won't be allowed to use tables directly in this object,

3. You won't be allowed to use non-released APIs in this object,

A list of all the released APIs can be found at below link:

[Released APIs](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/index.htm?file=abenreleased_apis.htm)

Unreleased and Released objects within same software components(set of packages) can be used.

For ex: Under a Cloud enabled package P1, you have 2 unreleased CDS C1, C2. You can still associate C1 in C2 or use C1 as data source in C2 etc, since they are in same package,

4. If this is an oData exposure, then RAP should be your programming model of choice,

5. ABAP Development Tools(ADT) to be used for ABAP Cloud developments,

6. Not all repository objects can be used in ABAP for Cloud Development. A list of all the repository objects allowed in restricted language version can be found at below link:

[Allowed Repository Objects in Restricted ABAP](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/index.htm?file=abenreleased_apis.htm)

7. Not all ABAP language elements are supported in ABAP for Cloud development. A list of all the supported language elements can be found at below link:

[Language Elements in ABAP Versions](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/index.htm?file=abenrestricted_abap_elements.h...