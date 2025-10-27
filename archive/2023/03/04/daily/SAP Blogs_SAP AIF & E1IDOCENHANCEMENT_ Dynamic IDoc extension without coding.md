---
title: SAP AIF & E1IDOCENHANCEMENT: Dynamic IDoc extension without coding
url: https://blogs.sap.com/2023/03/03/sap-aif-e1idocenhancement-dynamic-idoc-extension-without-coding/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:41.073180
---

# SAP AIF & E1IDOCENHANCEMENT: Dynamic IDoc extension without coding

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP AIF & E1IDOCENHANCEMENT: Dynamic IDoc extensio...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162259&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP AIF & E1IDOCENHANCEMENT: Dynamic IDoc extension without coding](/t5/technology-blog-posts-by-members/sap-aif-e1idocenhancement-dynamic-idoc-extension-without-coding/ba-p/13562435)

![bogar_benedikt](https://avatars.profile.sap.com/9/9/id9976c5de0c9c541f24b7479d0f2f2c7b27c1249fe3875f636814a7025dcc24cd_small.jpeg "bogar_benedikt")

[bogar\_benedikt](https://community.sap.com/t5/user/viewprofilepage/user-id/605053)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162259)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162259)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562435)

‎2023 Mar 03
8:51 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162259/tab/all-users "Click here to see who gave kudos to this post.")

5,532

* SAP Managed Tags
* [SAP Application Interface Framework](https://community.sap.com/t5/c-khhcw49343/SAP%2520Application%2520Interface%2520Framework/pd-p/01200314690800001892)

* [SAP Application Interface Framework

  SAP Application Interface Framework](/t5/c-khhcw49343/SAP%2BApplication%2BInterface%2BFramework/pd-p/01200314690800001892)

View products (1)

## Baseline

Within the SAP Application Interface Framework (AIF), dynamic enhancements of IDocs can be used, which allows especially powerful & generic additions to standard logic without the need to adjust the IDoc types.

Note 2457381 introduces a generic enhancement to any IDoc type by adding segment E1IDOCENHANCEMENT dynamically.

This allows you to add additional data to an SAP standard IDoc type without a custom extension.

### The result compared to the standard way:

* Time saving

* Less custom extension

* No additional ALE settings, like WE30, WE31, WE20

* No need to reupload the IDoc definitions

* Reduction of error sources

### Use cases:

* Various types of IDoc extensions

* Additional global informations of the IDoc

* Especially powerful in combination with reusable  AIF functions to build generic solutions like:

  + Reference Document numbers or Duplicate check

## Prerequisites

Your system must support the dynamic enhancements. Therefore, two SAP notes must be applied:

<https://launchpad.support.sap.com/#/notes/2457381>

<https://launchpad.support.sap.com/#/notes/2833608>

The E1IDOCENHANCEMENT is a table, which consists of an 30 char "IDENTIFIER" fieldand the corresponding payload in the field "DATA". Since it offers 970 chars for the payload in each line there are plenty of use cases.

There are some additions needed in the system to use this in SAP AIF:

1. The SAP AIF Raw structure should include the component E1IDOCENHANCEMENT.

* This can be done in advance, by the check box "Add segment E1IDOCENHANCEMENT to the generated structure" in the AIF IDoc Structure Generator.

![](/legacyfs/online/storage/blog_attachments/2023/03/STRU_GEN.png)

The resulting AIF structure includes now the table with corresponding SAP standard type:

![](/legacyfs/online/storage/blog_attachments/2023/03/AIF_e1IDOC_1-1.png)

1. 2. Apply in the port settings to send dynamic enhancements. (Transaction WE21, Port Options, Send Dynamic Enhancement Segments)

![](/legacyfs/online/storage/blog_attachments/2023/03/Port_enh.png)

* Otherwise, the segment will be filtered out before the IDoc is sent

* **Best practice:** create 2nd Port for all scenarios which are using the enhancement

## Implementation

For the implementation you are as flexible as the enhancement itself and can implement various use cases via the AIF structure mapping.

let's just assume you want to add the username of the processor to the outbound IDoc to confirm the Flightbooking.

After the structure is enhanced as described above you can simply add this in AIF structure mapping. In this example the root structure is used to insert a new line in the E1IDOCENHANCEMENT.

![](/legacyfs/online/storage/blog_attachments/2023/03/AIF_Root_mapping.png)

During the AIF transformation a new segment will be added.

Next step is to define the identifier and the value.

In this case we map the identifier field to the value ‘USERNAME’ and the corresponding data should be mapped with the current user. Therefore we can use the standard functions of SAP AIF fieldmappings.

![](/legacyfs/online/storage/blog_attachments/2023/03/AIF_FMAP.png)

 Now we could use the AIF transformation to test this:

![](/legacyfs/online/storage/blog_attachments/2023/03/AIF_transform.png)

During the transformation the IDoc is enriched with the additional data

![](/legacyfs/online/storage/blog_attachments/2023/03/2023_03_03_10_54_38_S4X_2_100_SAP.png)

Resulting XML

Analogous to this example, we can use all standard AIF functions to enrich the IDoc with data without development. For example, we can use a value mapping to select and add data from tables like SFLIGHT.

#### The one Hook:

The dynamic enhancement must always be located at the end of the IDoc

## Conclusion

The E1IDOCENHANCEMENT in SAP AIF can be used to extend IDocs quickly and easily. Especially when creating the IDoc structures via the AIF structure generator, the checkbox for adding dynamic enhancements should always be ticked in order to be able to use the segment at any time.

Since the segment can be used in every IDoc, especially generic IDoc extensions can be implemented effectively, since each IDoc uses the same structure for this.

Particularly in ALE, this results in a great time saving, as otherwise the extensions would always have to be set in the same way in both systems.

The only disadvantage to note is that the dynamic enhancement must always be the last segment of the IDoc. This means that it is particularly suitable for global extensions or extensions that are detached from the structure. If you want to extend sub-segments, you must find a way to determine the correct structure again via the identifier field. Here classical enhancements are more powerful in most cases.

* [aif](/t5/tag/aif/tg-p/board-id/technology-blog-members)
* [ale idoc](/t5/tag/ale%20idoc/tg-p/board-id/technology-blog-members)
* [idoc](/t5/tag/idoc/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-aif-e1idocenhancement-dynamic-idoc-extension-without-coding%2Fba-p%2F13562435%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibil...