---
title: Business Technology Platform solution diagrams and icons taken to the next level
url: https://blogs.sap.com/2022/11/26/business-technology-platform-solution-diagrams-and-icons-taken-to-the-next-level/
source: SAP Blogs
date: 2022-11-27
fetch_date: 2025-10-03T23:52:44.393119
---

# Business Technology Platform solution diagrams and icons taken to the next level

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Business Technology Platform solution diagrams and...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161686&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Business Technology Platform solution diagrams and icons taken to the next level](/t5/technology-blog-posts-by-members/business-technology-platform-solution-diagrams-and-icons-taken-to-the-next/ba-p/13559583)

![geert-janklaps](https://avatars.profile.sap.com/0/4/id04b00688b301802999785d929acf106d595b6d2ca9c484b5ade1444b1f2eb0d1_small.jpeg "geert-janklaps")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[geert-janklaps](https://community.sap.com/t5/user/viewprofilepage/user-id/868)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161686)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161686)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559583)

‎2022 Nov 26
9:38 PM

[48
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161686/tab/all-users "Click here to see who gave kudos to this post.")

26,816

* SAP Managed Tags
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (1)

A few years back the introduction of the SAP Icons & Samples for solution diagrams eased our lives as a BTP architects. It was / is great to have all icons available and a set of templates as a basis to start from (although PowerPoint is not the best solution in my personal opinion).

Announcement blog:

[Be Visual! Use Official Icons and Samples for SAP Business Technology Platform Solution Diagrams | S...](https://blogs.sap.com/2018/01/05/be-visual-use-official-icons-and-samples-for-sap-cloud-platform-solution-diagrams/)

In the meanwhile, the original Wiki page has already been removed and it's now only possible to download the templates & icons through direct links provided in the comments. Unfortunately, the last update of the SAP BTP Icons dates from somewhere around March 2021.

A few weeks ago, I saw a few new blogs, reusing the same outdated icons for draw.io. Which is an absolutely great alternative compared to the PowerPoint templates.

[Create SAP BTP solution diagrams with Draw.io (Diagrams.net) | SAP Blogs](https://blogs.sap.com/2022/11/07/create-sap-btp-solution-diagrams-with-draw.io-diagrams.net/) (by mauriciolauffer)

[Creating architecture diagrams with code | SAP Blogs](https://blogs.sap.com/2022/06/29/creating-architecture-diagrams-with-code/) (by ajmaradiaga)

***Edit: The original solution Mauricio mentioned in his blog, does contain updated icons, which I missed while I wrote this blog and created this solution. (See [Mauricio's comment](https://blogs.sap.com/2022/11/26/business-technology-platform-solution-diagrams-and-icons-taken-to-the-next-level/comment-page-1/#comment-649331) below)***

So, that got me thinking, how can I make sure I have all latest BTP icons available to use them in my solution / architecture diagrams? I came up with a few requirements I wanted to have available in my solution diagrams:

1. Latest version of BTP service icon as-is

2. Latest version of BTP service icon surrounded by a circle (as typically seen in the previous libraries)

3. Generic SAP Icons (as included in SAP Fiori)

### Introducing the BTP Diagram Icon generator

The BTP Diagram Icon Generator is a yeoman generator that:

* Downloads the latest BTP service icons from the SAP Discovery Center

* Generates a version of the service icon surrounded by a circle

* Uses the UI5 Web Components to extract the Fiori icons

Icons are generated in two formats, file-based in a folder structure so that they can be used in any diagram designing tool and as a draw.io / diagrams.net library which can easily be imported.

Icons can be organized by category as defined in the SAP Discovery Center or by type.

![](/legacyfs/online/storage/blog_attachments/2022/11/draw-io-library.png)

Generated draw.io / diagrams.net library

### Using the BTP Diagram Icon Generator

Generating your own BTP diagram icons is a matter of installing Nodejs, [yeoman generator](https://www.npmjs.com/package/yo) and the [BTP Diagram Icon Generator](https://www.npmjs.com/package/generator-btp-diagram-icons) itself.

First [download](https://nodejs.org/en/download/) and install Nodejs for your OS.

After installing Nodejs open a terminal / command-line and execute following command:

```
npm install -g yo generator-btp-diagram-icons
```

Now you're ready to run the generator! In the terminal / command-line, navigate to the folder where you want the icons to be generated and execute following command:

```
yo btp-diagram-icons
```

![](/legacyfs/online/storage/blog_attachments/2022/11/generator-1.png)

BTP Diagram Icons Generator

After the generator is finished, your folder will contain a set of folders containing the icons and libraries based on the choices made in the generator.

![](/legacyfs/online/storage/blog_attachments/2022/11/folder-structure.png)

BTP Diagram Icons Generator - Folder Structure

* btp: BTP service icon files (regular & circled)

* icons: SAP Fiori icon files

* libraries: draw.io / diagrams.net libraries

### Wrap-up

You now have the latest icons available for all your BTP solution diagrams! Whenever a new service is released, it's just a matter of running the generator again and the new service icon will be generated automatically!

Hope you enjoy this new open-source solution and happy diagramming!

* [Application Architecture](/t5/tag/Application%20Architecture/tg-p/board-id/technology-blog-members)
* [diagrams](/t5/tag/diagrams/tg-p/board-id/technology-blog-members)
* [drawio](/t5/tag/drawio/tg-p/board-id/technology-blog-members)
* [solution](/t5/tag/solution/tg-p/board-id/technology-blog-members)
* [yeoman](/t5/tag/yeoman/tg-p/board-id/technology-blog-members)
* [yeoman generators](/t5/tag/yeoman%20generators/tg-p/board-id/technology-blog-members)

20 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fbusiness-technology-platform-solution-diagrams-and-icons-taken-to-the-next%2Fba-p%2F13559583%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Secure Your Digital Journey with SAP CIAM](/t5/technology-blog-posts-by-sap/secure-your-digital-journey-with-sap-ciam/ba-p/14232983)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Tr...