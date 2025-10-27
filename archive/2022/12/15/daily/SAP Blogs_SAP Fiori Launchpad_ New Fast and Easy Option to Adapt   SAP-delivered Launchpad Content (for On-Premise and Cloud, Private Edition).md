---
title: SAP Fiori Launchpad: New Fast and Easy Option to Adapt   SAP-delivered Launchpad Content (for On-Premise and Cloud, Private Edition)
url: https://blogs.sap.com/2022/12/14/sap-fiori-launchpad-new-fast-and-easy-option-to-adapt-sap-delivered-launchpad-content-for-on-premise-and-cloud-private-edition/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:12.226726
---

# SAP Fiori Launchpad: New Fast and Easy Option to Adapt   SAP-delivered Launchpad Content (for On-Premise and Cloud, Private Edition)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori Launchpad: New Fast and Easy Option to A...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157728&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Launchpad: New Fast and Easy Option to Adapt SAP-delivered Launchpad Content (for On-Premise and Cloud, Private Edition)](/t5/technology-blog-posts-by-sap/sap-fiori-launchpad-new-fast-and-easy-option-to-adapt-sap-delivered/ba-p/13550177)

![ruth_groene](https://avatars.profile.sap.com/4/5/id45ab1408efe7302e72cadd4a4507543f0e901d9a52305d7b75335730a6682aac_small.jpeg "ruth_groene")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ruth\_groene](https://community.sap.com/t5/user/viewprofilepage/user-id/365081)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157728)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157728)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550177)

‎2022 Dec 14
9:19 PM

[33
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157728/tab/all-users "Click here to see who gave kudos to this post.")

18,554

* SAP Managed Tags
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori tools](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520tools/pd-p/73555000100800002345)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP Fiori tools

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Btools/pd-p/73555000100800002345)

View products (3)

Have you ever wanted to use SAP-delivered launchpad content out-of-the-box, but tweak it just a little bit? Maybe change a tile title to make it more meaningful for your business users, like renaming a tile “*Count Physical Inventory*” to “*Do a Stocktake*”?

This post covers the new adaptation of SAP-delivered launchpad content:

* How to adapt (video with end-to-end demo)

* Context and technical background

* Which fields can be adapted?

* How to translate adapted texts

## **How to Adapt (Demo of End-to-end Process)**

##

## **Adapting SAP-delivered Technical Catalogs**

In **earlier releases**, changing just the tile title of an SAP-delivered app meant that you had to copy its launchpad app descriptor item into a custom technical catalog and adjust all business catalogs, pages, spaces, groups and roles containing this app. But not anymore.

With **SAP Front-end server for SAP S/4HANA 2022**, you can now use an SAP-delivered technical catalog and tweak it just a little bit, e.g.

* Adapt a tile title using the new adaptation mode in SAP Fiori Launchpad App Manager (see [end-to-end demo video](https://video.sap.com/media/t/1_skkh3tnw) and SAP Help [Adapting Launchpad App Descriptor Items](https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/aa7cd725603d47348b7c5447579dd65a.html?locale=en-US)). These adaptations are cross-client, just like the technical catalogs themselves.

* There’s no need to copy the launchpad app descriptor item, so you don’t need to create a custom technical catalog either.

This reduces the need for custom technical catalogs and is an advantage for future upgrades: SAP’s updates to the SAP technical catalog will automatically show up on the launchpad of your business users. Except for the fields that you have adapted, of course – after all, you would not want your adapted tile title to disappear after an upgrade.

## **Context and Technical Background**

### **Supported Scenarios for SAP Fiori Launchpad Content**

For your launchpad content, you can decide between the following scenarios:

1. Use SAP-delivered content out-of-the box, **exactly as delivered** ([Basic Scenario - Use SAP Content as Delivered](https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/92061996fa0d462fb64d38bd2b92654e.html?locale=en-US))

2. **Adapt** SAP-delivered content to your needs ([Advanced Scenario - Adapt SAP Template Content and Add Your Own Content)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/fa2c1f8654254cbf9f78fba8f8d31482.html)

3. Create your own launchpad content **from scratch**.

We recommend using SAP-delivered content wherever possible - and now its adaptation has become even easier: in many cases it’s not necessary anymore to copy SAP technical content into custom technical catalogs.

### **Technical Background: How is launchpad content structured?**

Behind the tile that you see on your launchpad page, there are technical entities including spaces, pages, groups, business catalogs, and technical catalogs.  What you see on a tile is controlled by the underlying launchpad app descriptor item in the technical catalog. For more information on launchpad content entities, see SAP Help [SAP Fiori Launchpad - About Launchpad Content](https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/c0cb377b1b694116bc469622b258d0f1.html?locale=en-US).

![](/legacyfs/online/storage/blog_attachments/2022/12/blogpic2_tech_entities.png)

Picture 1: Overview of launchpad content entities.

![](/legacyfs/online/storage/blog_attachments/2022/12/blogpic3_LADI.png)

Picture 2: The ‘Launchpad app descriptor item’ bundles the entities for one app: one target mapping and one or more tiles.

## **What exactly can you change, without copying the SAP-delivered content?**

You can currently adapt the following fields of the launchpad app descriptor items.

With S/4HANA 2022 FPS1 (SAP\_UI SP02), it is also possible to adapt the target mapping parameters of SAP-delivered content: create new target mapping parameters and assign default .

|
 **Group of Fields** |
 **Fields you can adapt** |

|
 Target Application Fields |
 * Target Application Title  * Target Mapping Information  * Device Type - Desktop, Tablet, Phone |

|
 Tile Fields |
 * Tile Title  * Tile Subtitle  * Tile Icon  * Tile Keywords  * Tile Information  * *for dynamic tiles:* Refresh Interval in Seconds |

**Outlook**

For future releases, we plan to continue to refine features and user experience – based on your feedback.

## **Yes, you can translate adapted tile texts**

The first question customers asked was: ‘Our business users will see the adapted texts on their Fiori launchpad – can we translate them?’

Yes, it’s possible to translate the following adapted texts:

* Tile title, tile subtitle, tile keywords, tile information

* Target application title

And what if there is no translation of an adapted text to a user’s logon language? Then this user will see the translated original text, i.e. the translation shipped by SAP.

### **How...