---
title: Simplifying Destination Configuration with Resource Path in Action Editor
url: https://blogs.sap.com/2023/03/26/simplifying-destination-configuration-with-resource-path-in-action-editor/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:46:14.540696
---

# Simplifying Destination Configuration with Resource Path in Action Editor

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Simplifying Destination Configuration with Resourc...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158817&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Simplifying Destination Configuration with Resource Path in Action Editor](/t5/technology-blog-posts-by-sap/simplifying-destination-configuration-with-resource-path-in-action-editor/ba-p/13552911)

![nipun_madan](https://avatars.profile.sap.com/7/d/id7deaea93c0211138d1e14a64bc8b4a0e290bd5586436a60220d60eaff45d1e51_small.jpeg "nipun_madan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[nipun\_madan](https://community.sap.com/t5/user/viewprofilepage/user-id/269490)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158817)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158817)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552911)

‎2023 Mar 26
11:24 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158817/tab/all-users "Click here to see who gave kudos to this post.")

1,733

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

## **Introduction:**

As an IT admin, managing multiple destinations for different resources can be time-consuming and complex. However, with the new feature of creating a single destination with a global setting in the Actions Editor, managing resources has become easier. In this blog post, we will discuss this new feature and how it can be utilized for different projects.

**Note: All the existing Action Projects that are consuming the existing API-specific destinations can still continue to work as is or use a central system-specific destination as explained below using the Resource Path feature.**

## **Before Resource Path Feature:**

+ IT admins had to create separate destinations for each resource when testing actions with destinations

+ Example: creating separate destinations for Business Partner and Sales Order resources

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-at-5.43.55-PM-1.png)

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-at-9.58.32-AM.png)

## **After Resource Path feature:**

+ IT admins can create only one destination with URL: **<s4system>**

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-at-9.59.05-AM.png)

+ Use Global setting in the action editor to set the resource path

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-19-at-5.31.10-PM.png)

## Example

### **Project One example:**

+ Created using business partner OAS

+ Set the resource path as **/sap/opu/odata/sap/API\_BUSINESS\_PARTNER\_SRV**

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-19-at-5.27.53-PM.png)

+ Use the above-created root destination to call the API

  * ![Screenshot 2024-03-21 at 12.55.01 PM.png](/t5/image/serverpage/image-id/84189i1BB69401FB545ABB/image-size/large?v=v2&px=999 "Screenshot 2024-03-21 at 12.55.01 PM.png")

## **Project Two example:**

+ Created using sales order OAS

+ Set the resource path as **/sap/opu/odata/sap/API\_SALES\_ORDER\_SRV**

  * ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-at-10.07.41-AM.png)

+ Use the above-created root destination to call the API

  - ![Screenshot 2024-03-21 at 12.57.02 PM.png](/t5/image/serverpage/image-id/84190iE764C3DC045A7E3A/image-size/large?v=v2&px=999 "Screenshot 2024-03-21 at 12.57.02 PM.png")

## **Conclusion:**

In conclusion, this new feature of creating a single destination with a global setting in the Actions Editor is a game-changer for IT admins. It simplifies the process of managing multiple resources and saves time. With the ability to set the resource path globally, IT admins can use the same root destination for different projects, which makes the entire process much more efficient.

## **Call to Action:**

We hope you found this blog post informative and useful. Please feel free to share your feedback or thoughts in the comments section below.

## **References**

1. Help portal documentation on the topic Actions Editor can be found [here](https://help.sap.com/docs/PROCESS_AUTOMATION/a331c4ef0a9d48a89c779fd449c022e7/609538e04bc843d887011765c14ecdda.html?version=Cloud&locale=en-US).

1. More help regarding this feature can be found [here](https://help.sap.com/docs/PROCESS_AUTOMATION/a331c4ef0a9d48a89c779fd449c022e7/f0669e115acf41bab0f7dce854bda437.html).

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [ActionEditor](/t5/tag/ActionEditor/tg-p/board-id/technology-blog-sap)
* [ActionProject](/t5/tag/ActionProject/tg-p/board-id/technology-blog-sap)
* [Prefix URL](/t5/tag/Prefix%20URL/tg-p/board-id/technology-blog-sap)
* [resource path](/t5/tag/resource%20path/tg-p/board-id/technology-blog-sap)
* [SAP BTP CoreServices](/t5/tag/SAP%20BTP%20CoreServices/tg-p/board-id/technology-blog-sap)
* [URL Prefix](/t5/tag/URL%20Prefix/tg-p/board-id/technology-blog-sap)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsimplifying-destination-configuration-with-resource-path-in-action-editor%2Fba-p%2F13552911%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Basic Configurations for SAP EWM Material Flow System: Part-1](/t5/technology-blog-posts-by-members/basic-configurations-for-sap-ewm-material-flow-system-part-1/ba-p/14233314)
  in [Technol...