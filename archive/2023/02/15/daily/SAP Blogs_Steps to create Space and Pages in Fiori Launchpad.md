---
title: Steps to create Space and Pages in Fiori Launchpad
url: https://blogs.sap.com/2023/02/14/steps-to-create-space-and-pages-in-fiori-launchpad/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:37:02.636375
---

# Steps to create Space and Pages in Fiori Launchpad

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Steps to create Space and Pages in Fiori Launchpad

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163341&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Steps to create Space and Pages in Fiori Launchpad](/t5/technology-blog-posts-by-members/steps-to-create-space-and-pages-in-fiori-launchpad/ba-p/13568966)

![kuldeep2813](https://avatars.profile.sap.com/c/a/idca77fa5420586fe40f1c0f7dd255dd4f632b872a329f361d868cd04405ed4796_small.jpeg "kuldeep2813")

[kuldeep2813](https://community.sap.com/t5/user/viewprofilepage/user-id/736775)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163341)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163341)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568966)

‎2023 Feb 14
11:43 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163341/tab/all-users "Click here to see who gave kudos to this post.")

70,323

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [field masking for SAPUI5 and SAP Fiori](https://community.sap.com/t5/c-khhcw49343/field%2520masking%2520for%2520SAPUI5%2520and%2520SAP%2520Fiori/pd-p/73554900100800000794)
* [SAP Fiori tools](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520tools/pd-p/73555000100800002345)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)
* [field masking for SAPUI5 and SAP Fiori

  field masking](/t5/c-khhcw49343/field%2Bmasking%2Bfor%2BSAPUI5%2Band%2BSAP%2BFiori/pd-p/73554900100800000794)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Fiori tools

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Btools/pd-p/73555000100800002345)

View products (7)

Hello,

In this blog post we will learn how to create [space and pages on Fiori Launchpad](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e55f5cc8ccec490f83a00284659bce9f.html).

## What is Space and Pages

Provides structured way to display the apps in [Fiori launchpad](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e55f5cc8ccec490f83a00284659bce9f.html) and ease to end user for accessing the apps, which is available from S4 HANA 2020 and onward ON-PREMISE environment.

### Prerequisite for Space and Pages

User must have access of below:

1. PFCG - TCode

2. /n/ui2/FLP - TCode

3. Fiori app - Manage Launchpad Space (F4834)

4. Fiori app - Manage Launchpad Page (F4512)

### **There are 4 main parts for space and pages**

1. **Space** - Space has navigation items, a space holds the multiple pages.

2. **Pages** - Pages has the single or multiple sections.

3. **Sections** - Section is the Subareas in the Pages, Section has single or multiple Tiles.

4. **Tiles** - A tile represents that an app on the SAP Fiori launchpad.

The following diagram shows this with an example for the space “Accounts Payable”.

![](/legacyfs/online/storage/blog_attachments/2023/02/Space_Overview.png)

Space and Pages Overview

## Activate the Space and Pages in Fiori Launchpad

1. Go to **User's** Icon and Click on **Setting** Button.

![](/legacyfs/online/storage/blog_attachments/2023/02/User_Icon.png)

2.Click on **Space and Pages** --> check both checkbox (**Use Spaces, Show My Home**) -->**Save**.

![](/legacyfs/online/storage/blog_attachments/2023/02/Space_Pages_Setting.png)

Now we can see the Space and Pages in Fiori Launchpad:

![](/legacyfs/online/storage/blog_attachments/2023/02/Space.png)

## Steps to Create Space and Pages

### Step 1: Go to SAP Logon and enter the TCode - /n/ui2/FLP (Fiori Launchpad) and Press Enter

![](/legacyfs/online/storage/blog_attachments/2023/02/SAP-Logon.png)

Now It will navigate to the Fiori Launchpad.

![](/legacyfs/online/storage/blog_attachments/2023/02/Space-1.png)

### Step 2: Launch the Fiori app - 'Manage Launchpad Spaces'.

![](/legacyfs/online/storage/blog_attachments/2023/02/Launchpad_Space.png)

Click on the **Create** Button.

![](/legacyfs/online/storage/blog_attachments/2023/02/Create.png)

### Step 3: Fill the required details in Popup and Select Also Create a Page Option  and click on Create Button. This will create a New Page in this space.

**Note**: If page is already created, not need to select the **Also Create a Page** option.

Please follow the standard naming convention for Space and page name,

i.e. Space Name: <Z/Y + Functional Area +SP+ Text>

Page Name: <Z/Y + Functional Area + PG + TEXT>.

![](/legacyfs/online/storage/blog_attachments/2023/02/Popup.png)

Navigate to the the Page.

If Page visibility is **Hidden**, select the row and click on the **Set Visible**.

![](/legacyfs/online/storage/blog_attachments/2023/02/Page-Visibility.png)

Now the **Page Visibility** status will be Visible.

![](/legacyfs/online/storage/blog_attachments/2023/02/Visible.png)

### Step 4: Click on Page and select the Page (Row)

![](/legacyfs/online/storage/blog_attachments/2023/02/Page1.png)

Click on **Edit** Button

![](/legacyfs/online/storage/blog_attachments/2023/02/Page2.png)

Give the Section Name in **Section Title,** If  you want to add more section then click on the **Add Section.**

![](/legacyfs/online/storage/blog_attachments/2023/02/Section2.png)

### Step 5: Add catalogs from which app needs to be assigned, search the catalog and select.

![](/legacyfs/online/storage/blog_attachments/2023/02/Catalog1.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Catalog2.png)

### Step 6: Assign the app to the section and Page.

![](/legacyfs/online/storage/blog_attachments/2023/02/Apps.png)

Click on **Save** Button and Save the changes.

![](/legacyfs/online/storage/blog_attachments/2023/02/Save.png)

### Step 7: If space exist, and need to create new page, we can use the fiori app - Manage Launchpad Pages

### ![](/legacyfs/online/storage/blog_attachments/2023/02/Page3.png)

Click on Create Button

### ![](/legacyfs/online/storage/blog_attachments/2023/02/Page-4.png)

Fill the required details and create. Follow step 5 and 6.

![](/legacyfs/online/storage/blog_attachments/2023/02/Ne...