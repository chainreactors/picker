---
title: SAP Fiori Catalog, Business Group & Role Creation
url: https://blogs.sap.com/2023/02/26/sap-fiori-catalog-business-group-role-creation-2/
source: SAP Blogs
date: 2023-02-27
fetch_date: 2025-10-04T08:10:54.966090
---

# SAP Fiori Catalog, Business Group & Role Creation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Fiori Catalog, Business Group & Role Creation

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160847&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Catalog, Business Group & Role Creation](/t5/technology-blog-posts-by-members/sap-fiori-catalog-business-group-role-creation/ba-p/13554886)

![abhishekchoukse](https://avatars.profile.sap.com/d/1/idd1b2c46373ad8b77359dda8576a24db73f2e0585158d94c6fb5c34dc075e0765_small.jpeg "abhishekchoukse")

[abhishekchoukse](https://community.sap.com/t5/user/viewprofilepage/user-id/124515)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160847)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160847)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554886)

‎2023 Feb 26
11:43 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160847/tab/all-users "Click here to see who gave kudos to this post.")

11,210

* SAP Managed Tags
* [SAP GRC Role Expert for SAP NetWeaver](https://community.sap.com/t5/c-khhcw49343/SAP%2520GRC%2520Role%2520Expert%2520for%2520SAP%2520NetWeaver/pd-p/01200314690800000196)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAP GRC Role Expert for SAP NetWeaver

  SAP Access Control](/t5/c-khhcw49343/SAP%2BGRC%2BRole%2BExpert%2Bfor%2BSAP%2BNetWeaver/pd-p/01200314690800000196)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)

View products (3)

## Will see how to Create a Catalog and Business Group in Fiori Launchpad Designer

## **What is Fiori Catalog?**

A catalog is a set of Tiles / Applications you want to make available for one role. Depending on the role and the catalogs assigned to the role, users can browse through the catalogs and choose the Tiles / Applications that they want to display on the entry page of the SAP Fiori launchpad.

## **What is Business Group?**

A group is a subset of Applications from one or more catalogs. Which tiles are displayed on a user’s Home page depends on the groups assigned to the user’s role. In addition, the user can personalize the entry Fiori Page by adding or removing Applications to pre-delivered groups or self-defined groups.

## Why to Create a Custome Role?

If we use SAP Standard Role End User / Business User will be getting lots of other Application which are not required actually and His / Her Home page will end up messy with lots of business groups and Applications

#### Please Follow Below Steps to Create a Successful Role instead of using SAP Standard Role for Fiori Role.

## Fiori Catalog & Business Group Creation

1. Enter T.code :- **/n/ui2/flpd\_cust**

**Need to Create Catalog & Business Group**
![](/legacyfs/online/storage/blog_attachments/2019/03/1-16.png)

2. Click on Add / Create button
![](/legacyfs/online/storage/blog_attachments/2019/03/2-18.png)

3. Give Title & Role (its Description)

4. Click Save
![](/legacyfs/online/storage/blog_attachments/2019/03/3-18.png)

5. We can use Standard SAP Catalogs which is will full fill our requirement, once you select catalog its tiles / Applications will be displayed on right side
![](/legacyfs/online/storage/blog_attachments/2019/03/4-19.png)

6. Select the required Tile which you need to add to your catalog and drag once its dragged as shown above 2 options will be enabled Create Reference and delete

***Note:- Don’t Delete Role By Mistikely also once it deleted its deleted it can’t be undo.***

![](/legacyfs/online/storage/blog_attachments/2019/03/5-14.png)

7. Once you drop in Create reference popup will be enabled to select under which need to add

8. Select catalog which you created earlier

![](/legacyfs/online/storage/blog_attachments/2019/03/6-8.jpg)

9. Click on Target Mapping

10. Select the required segment and Action and click on create reference.

![](/legacyfs/online/storage/blog_attachments/2019/03/7-10.png)

11. Select the Catalog under which you need to copy Mapping . like this you can add multiple Applications/tiles and Target Mapping as per the Applications you wanted to Add

with this, we Completed Creation of catalog

## **Creation of Business Group.**

![](/legacyfs/online/storage/blog_attachments/2019/03/8-12.png)

1. Now click on Group and click Create
   ![](/legacyfs/online/storage/blog_attachments/2019/03/9-11.png)

2. Give Title & ID and click on save
   ![](/legacyfs/online/storage/blog_attachments/2019/03/10-10.png)

3. Click on add
   ![](/legacyfs/online/storage/blog_attachments/2019/03/11-12.png)

4. Once you click on add will get a list of tiles / Apps which we added in Catalog

5. Click on Add button which is bottom of the tile
   ![](/legacyfs/online/storage/blog_attachments/2019/03/12-11.png)

6. Once its added will get a successful message as shown above.

7. We can also add other Apps/tiles from other Catalogs by searching in the search bar.
   ![](/legacyfs/online/storage/blog_attachments/2019/03/13-12.png)
   ![](/legacyfs/online/storage/blog_attachments/2019/03/14-9.png)

8. I have selected BOM Catalog and under BOM Catalog selected 3 Apps which are required

9. Click back button and come to the main page
   ![](/legacyfs/online/storage/blog_attachments/2019/03/15-8.png)

We can see under the Business Group which we created now we have 4 apps once from catalog which we created and other 3 are from different / SAP standard Catalogs.

With this we completed Creation of Catalog & business group, now need to create Role and assign created Catalog and Business Group “RUTHVIK” to a role.

## Creation of Role using Catalog and Business Group

1. In SAP Open PFCG Transaction.

![](/legacyfs/online/storage/blog_attachments/2019/03/16-9.png)

2. Give the role name and click on the single role
![](/legacyfs/online/storage/blog_attachments/2019/03/17-8.png)

3. Give the description and long text

4. Save
![](/legacyfs/online/storage/blog_attachments/2019/03/18-8.png)

5. Select Menu Tab and select Transaction Drop down to select SAP Fiori Tile Catalog.

![](/legacyfs/online/storage/blog_attachments/2019/03/19-7.png)

6. Once you select Fiori Catalog “Assign Catalog” Popup will be opened in catalog ID select from search and select Catalog which we created

7. Clicks continue.

![](/legacyfs/online/storage/blog_attachments/2019/03/20-10.png)

8. Repeat same to select Business Group

![](/legacyfs/online/storage/blog_attachments/2019/03/21-6.png)

9. Select Business Group we created

10.Click Continue

![](/legacyfs/online/storage/blog_attachments/2019/03/22-8.png)

11. Go to User Tab and assign User ID to whom these new roles need to be assigned.

12. Click Save

We Have successf...