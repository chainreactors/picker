---
title: Migrating SAP Neon/Sap web Ide to BAS and Deployment to BTP and Creating Roles, catalog and Group on Launchpad
url: https://blogs.sap.com/2022/10/29/migrating-sap-neon-sap-web-ide-to-bas-and-deployment-to-btp-and-creating-roles-catalog-and-group-on-launchpad/
source: SAP Blogs
date: 2022-10-30
fetch_date: 2025-10-03T21:19:07.013635
---

# Migrating SAP Neon/Sap web Ide to BAS and Deployment to BTP and Creating Roles, catalog and Group on Launchpad

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Migrate an SAP Neon/Sap web Ide Application to BA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160874&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrate an SAP Neon/Sap web Ide Application to BAS and Deployment to BTP and Creating Roles, catalog and Group on Launchpad](/t5/technology-blog-posts-by-members/migrate-an-sap-neon-sap-web-ide-application-to-bas-and-deployment-to-btp/ba-p/13555052)

![rajesh_salapu](https://avatars.profile.sap.com/7/b/id7bcb4054ee6c7dcd06df3e347c0129a67d4959e2c0c1ada464dc1d7337b9d570_small.jpeg "rajesh_salapu")

[rajesh\_salapu](https://community.sap.com/t5/user/viewprofilepage/user-id/773332)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160874)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160874)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555052)

‎2022 Oct 29
1:51 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160874/tab/all-users "Click here to see who gave kudos to this post.")

1,475

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)

View products (2)

Hi Readers!!

Hope Everyone are doing Good and safe.

In this blog post I am going to demonstrate how you can Migrate an webide /neon application to BAS and deployed to BTP cloud foundry  and also Create roles, catalogs and Groups on launchpad.

**Steps Include**:

1.Export Application from sap webide/ neon.

2.import that file to Bas

1.After Uploading click on Start migrating and Select the Application and select latest Version and click on start migration.

* run “npm install” on Terminal.

* change code in manifest.json [adding cross navigation in sap.app library]

* Refresh on Application Status.

* Click on add Deploy Config.

2.Right Click on MTA.yaml File and Select Build MTA Project.

* Expand the MTA\_archives and right click on file and Select Deploy MTA Archive.

3.After Deployment Go to Html5 to check our deployed application.

4.Click on go to application on launchpad Service

* update the site Manager

* create Catalogs, groups and roles as per requirement

* adding roles in BTP

5.Update the site Manager

Click on Import.

![](/legacyfs/online/storage/blog_attachments/2022/10/impott-click.png)

Click on Start Migration

![](/legacyfs/online/storage/blog_attachments/2022/10/start-migration.png)

Select latest Version and if need Give Hostname, client and Destination as per requirement.

![](/legacyfs/online/storage/blog_attachments/2022/10/latest-version-.png)

Click on the run npm link

![](/legacyfs/online/storage/blog_attachments/2022/10/click-on-npm-install.png)

Refresh the Application information by click on icon.

![](/legacyfs/online/storage/blog_attachments/2022/10/refresh-application-status.png)

Add cross navigation properties in manifest to create sematic object and action in sap.app library

![](/legacyfs/online/storage/blog_attachments/2022/10/manifest-change.png)

Click on Add Deploy Config.

![](/legacyfs/online/storage/blog_attachments/2022/10/add-deployment.png)

Select Details using navigation keys in terminal.

![](/legacyfs/online/storage/blog_attachments/2022/10/w8-1.png)

after this mta.yaml file created in application . then right click on mta.yaml and Click on BUILT MTA project.

![](/legacyfs/online/storage/blog_attachments/2022/10/btp_8.png)

Right click on Mta\_archives expanded file and select Deploy MTA Archive

![](/legacyfs/online/storage/blog_attachments/2022/10/w10.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/w11.png)

Open BTP and Click on HTML Application then it shows our Deployed Application.

![](/legacyfs/online/storage/blog_attachments/2022/10/w12.png)

Select Go to Application to Create catalog, groups and roles in launchpad.

![](/legacyfs/online/storage/blog_attachments/2022/10/w13.png)

Select Channel Manager and click on Update button as below:

![](/legacyfs/online/storage/blog_attachments/2022/10/channel-refresh.png)

Select Site manager and choose Content Explorer and select HTML5 Apps to add our applications to my content.

![](/legacyfs/online/storage/blog_attachments/2022/10/content-Exporer.png)

Select our Application and click on Add to Content. Then the selected application added to My Content.

![](/legacyfs/online/storage/blog_attachments/2022/10/add-content.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/w17.png)

For to Create Catalog, Group and Role click on New as below. First Create catalog So that click on catalog option from dropdown.

![](/legacyfs/online/storage/blog_attachments/2022/10/w18.png)

Enter Title and Description and click on Assign Items then all items will be displayed and select ‘+’ of required item and click on save then Catalog Created.

![](/legacyfs/online/storage/blog_attachments/2022/10/catalog_01.png)

Same We need to Create Group also.

For to Display Our Application to every USER in our BTP account, Click on Every one row and then it navigates to the below Screen and select the required app to display every user in your BTP.

![](/legacyfs/online/storage/blog_attachments/2022/10/c32.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/everyone-role.png)

Finally Click on Site Directory and Select the below icon to navigate respected Launchpad.

![](/legacyfs/online/storage/blog_attachments/2022/10/site-directory.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/output_123.png)

How to add Users in BTP:

Select Users from Security then add Users as shown in below.

![](/legacyfs/online/storage/blog_attachments/2022/10/users-adding.png)

Suppose you want to display your Launchpad application to Selected users then we need to Create Role as mentioned Previously.

![](/legacyfs/online/storage/blog_attachments/2022/10/role-creation.png)

After that Select Role Collections in Security. Then search the role as you Created Earlier. Then click on that so that it navigates to the below Screen.

![](/legacyfs/online/storage/blog_attachments/2022/10/role-collection-tab.png)

Finally Update the site Manager.

![](/legacyfs/online/storage/blog_attachments/2022/10/channel-refresh-1.png)

**Conclusion**: Hope this blog post will give better understanding on migrate an application to BTP from webide/neon platform and also Creating roles , catalogs and Groups to that application on launchpad.

It would be a pleasure for me to see your feedbacks or thoughts in comments. I look forward to hearing from you.

Best R...