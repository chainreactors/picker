---
title: How To Create Fiori Pages, Spaces and link with authorization role
url: https://blogs.sap.com/2023/07/09/how-to-create-fiori-pages-spaces-and-link-with-authorization-role/
source: SAP Blogs
date: 2023-07-10
fetch_date: 2025-10-04T11:52:24.486572
---

# How To Create Fiori Pages, Spaces and link with authorization role

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How To Create Fiori Pages, Spaces and link with au...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67780&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How To Create Fiori Pages, Spaces and link with authorization role](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-create-fiori-pages-spaces-and-link-with-authorization-role/ba-p/13559494)

![ahmedrashed33](https://avatars.profile.sap.com/8/e/id8ed26df30e519344cb0d79f396b23b00264d26180c86611db5c6e15ae3a3491d_small.jpeg "ahmedrashed33")

[ahmedrashed33](https://community.sap.com/t5/user/viewprofilepage/user-id/141739)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67780)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67780)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559494)

‎2023 Jul 09
2:56 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67780/tab/all-users "Click here to see who gave kudos to this post.")

10,629

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)

View products (7)

**Introduction**

Starting from SAP S/4HANA 2021, Fiori groups mode are officially deprecated, it means soon will be obsolete.

in this blog post we will discover how to use the new Fiori mode “pages and spaces”

Note: This blog post having simple steps for a functional consultant to deal with pages and spaces

**Blog content**

1. Prerequisites to activate Fiori pages and spaces.

2. check the standard Spaces

3. create new page

4. Create new space and assign it to Page

5. Assign Tiles to pages

6. Assign space to authorization roles

**Prerequisites to activate Fiori pages and spaces.**

To be able to manage pages and space, you will need an authorization role : **SAP\_FLP\_ADMIN**

* once you have an access to this role, you will be able to see the below apps to manage pages and spaces

![](/legacyfs/online/storage/blog_attachments/2023/06/1-45.png)

* you will need to change the mode in user setting to Pages mode

![](/legacyfs/online/storage/blog_attachments/2023/06/1-46.png)

**Check the standard Spaces**

There are standard pages and spaces delivered by sap you can check it throw fiori library as below

![](/legacyfs/online/storage/blog_attachments/2023/06/1-47.png)

also you can check all delivered pages and spaces using their apps

![](/legacyfs/online/storage/blog_attachments/2023/06/1-45.png)

you can search for using the search for the standard spaces using search bar

![](/legacyfs/online/storage/blog_attachments/2023/06/1-48.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/1-49.png)

**Create new page**

Using the manage launchpad pages app you can create a new page to personalize it as you want

![](/legacyfs/online/storage/blog_attachments/2023/06/1-51.png)

after that you can click on create bottom

![](/legacyfs/online/storage/blog_attachments/2023/07/1-36.png)

enter the page ID, Description, and transport request

then click on create

![](/legacyfs/online/storage/blog_attachments/2023/07/1-38.png)

i have added also new three sections by just added the section title

Note : an empty section will not appear in the pages, it means if you have created a section you need to add a tile to that section to be able to see it in the page

![](/legacyfs/online/storage/blog_attachments/2023/07/1-39.png)

we can create space then assign it to the page, by click on manage launchpad spaces

![](/legacyfs/online/storage/blog_attachments/2023/07/1-40.png)

**Create new space and assign it to Page**

now we will start create the space and assign it to the page that we have created

spaces are like group of pages, you can group many pages under one space

Go to manage launchpad space app

![](/legacyfs/online/storage/blog_attachments/2023/07/1-42.png)

then click on create bottom

![](/legacyfs/online/storage/blog_attachments/2023/07/1-43.png)

you have to enter the ID and description for the Space

![](/legacyfs/online/storage/blog_attachments/2023/07/1-45.png)

from the right side you need to select the page that you need to assign this space to

![](/legacyfs/online/storage/blog_attachments/2023/07/1-46.png)

we will choose our page that we created earlier and click on add

![](/legacyfs/online/storage/blog_attachments/2023/07/1-47.png)

once the page added, you can Save the space

![](/legacyfs/online/storage/blog_attachments/2023/07/1-48.png)

Note : we can add mangy pages to the same space

**Assign Tiles to pages**

After creating the space, we need to assign the tiles ( Fiori applications ) to the pages and sections that we have created earlier

we need to open the page in Edit mode

![](/legacyfs/online/storage/blog_attachments/2023/07/1-49.png)

then we will see the pages and the section that we have created

![](/legacyfs/online/storage/blog_attachments/2023/07/1-50.png)

Now we have two ways to get the tiles

we can get the tiles from assigned role or we can get it manually by selecting the catalog

we will see how to get the tiles from the catalog

click on catalog bottom

![](/legacyfs/online/storage/blog_attachments/2023/07/1-51.png)

search for the required cat...