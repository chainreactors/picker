---
title: Migrating SAP UI5 Applications from SAP Web IDE to Visual Studio Code (VS Code) and Deploy the application to S/4HANA On-Premise ABAP Repository
url: https://blogs.sap.com/2023/03/14/migrating-sap-ui5-applications-from-sap-web-ide-to-visual-studio-code-vs-code-and-deploy-the-application-to-s-4hana-on-premise-abap-repository/
source: SAP Blogs
date: 2023-03-15
fetch_date: 2025-10-04T09:35:15.508031
---

# Migrating SAP UI5 Applications from SAP Web IDE to Visual Studio Code (VS Code) and Deploy the application to S/4HANA On-Premise ABAP Repository

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Migrating SAP UI5 Applications from SAP Web IDE to...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163232&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrating SAP UI5 Applications from SAP Web IDE to Visual Studio Code (VS Code) and Deploy the application to S/4HANA On-Premise ABAP Repository](/t5/technology-blog-posts-by-members/migrating-sap-ui5-applications-from-sap-web-ide-to-visual-studio-code-vs/ba-p/13568463)

![loganathanc](https://avatars.profile.sap.com/c/c/idcc6a75548e339ebc0cc40a898a9a3bfd2472c0d5665914dbc31a848e6fc99b6d_small.jpeg "loganathanc")

[loganathanc](https://community.sap.com/t5/user/viewprofilepage/user-id/127723)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163232)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163232)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568463)

‎2023 Mar 14
9:56 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163232/tab/all-users "Click here to see who gave kudos to this post.")

11,407

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (3)

In this blog post, I will guide you step by step process for Migration of SAP UI5 Application from SAP Web IDE to Visual Studio Code (VS Code). And deployment of the application to S/4 HANA On-Promise ABAP Repository from Visual Studio Code (VS Code).

#### **I have taken reference from**

[SAP Help Document](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/70d41f3ee29d453a90efab3ce025d450.html?locale=en-US)

#### **Follow the below link to set up Visual Studio Code for SAPUI5 development** @lenahammerer

[Getting Ready for UI5 Development with Visual Studio Code](https://blogs.sap.com/2021/10/15/getting-ready-for-ui5-development-with-visual-studio-code/)

### In this article will discuss

#### **Migration of SAP Web IDE Project into VS Code**

1. Download the BSP application from S/4 HANA On-Promise ABAP Repository using SAP Web IDE.

2. Create a workspace for Visual Studio Code UI5 Development and copy the source code to workspace.

3. Start the migration process using Visual Studio Code.

4. Modify the ui5.yaml file to connect S/4 HANA On-Promise system & Preview the application.

#### **UI5 Application deployment process for S/4HANA On-Promise System.**

1. Add the gateway system details in Visual Studio Code.

2. Add deployment configuration.

3. Deploy the application to S/4 HANA On-Promise system ABAP repository.

### Lets get started.

#### **Migration of SAP Web IDE Project into VS Code.**

Step 1: Download the BSP application from S/4 HANA On-Promise ABAP Repository using SAP Web IDE.

![](/legacyfs/online/storage/blog_attachments/2023/03/1-23.png)

BSP Application from ABAP Repository

Step 2: Create a workspace for Visual Studio Code UI5 Development and copy the source code to workspace.

![](/legacyfs/online/storage/blog_attachments/2023/03/2-12.png)

BSP Application copied in to Visual Studio Code workspace

Step 3: Start the migration process using Visual Studio Code.

* Ctrl + Shift + P (Show All Commands)

* Fiori: Migrate Project for use in Fiori Tools

![](/legacyfs/online/storage/blog_attachments/2023/03/2_1.png)

Migrate Fiori Project

![](/legacyfs/online/storage/blog_attachments/2023/03/2_2.png)

Start Migration

![](/legacyfs/online/storage/blog_attachments/2023/03/2_3.png)

After successful migration

Step 4: Modify the ui5.yaml file to connect S/4 HANA On-Promise system & Preview the application.

* Modifying ui5.yaml file

![](/legacyfs/online/storage/blog_attachments/2023/03/3_2.png)

ui5.yaml modification

* Preview application

![](/legacyfs/online/storage/blog_attachments/2023/03/3_3.png)

Preview Application

![](/legacyfs/online/storage/blog_attachments/2023/03/3_4.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/3_5.png)

npm run start

![](/legacyfs/online/storage/blog_attachments/2023/03/3_6.png)

Application loaded successfully in browser

#### **UI5 Application deployment process for S/4HANA On-Promise System.**

Step 1: Adding Gateway System in the Visual Studio Code

![](/legacyfs/online/storage/blog_attachments/2023/03/3_1-1.png)

Adding Gateway System in the Visual Studio Code

Step 2: Adding deployment configuration.

* Create ui5-deploy.yaml file for deployment configuration

*Note: Before deployment please create your package & Transport request. If your deploying into $TMP package then Transport Request is not required*

![](/legacyfs/online/storage/blog_attachments/2023/03/4_1.png)

ui5-deploy.yaml file

Step 3: Deploy the application to S/4 HANA On-Promise system ABAP repository.

* Add deploy scripts in package.json

```
"deploy": "npm run build && fiori deploy --config ui5-deploy.yaml && rimraf archive.zip",
```

![](/legacyfs/online/storage/blog_attachments/2023/03/4_2.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/4_3.png)

Successfully deployed the application

* Congratulations! You have successfully deployed and tested your SAPUI5 application.

![](/legacyfs/online/storage/blog_attachments/2023/03/5_1-1.png)

SICF

![](/legacyfs/online/storage/blog_attachments/2023/03/5_2-1.png)

Application running in development system.

#### Troubleshooting

#### **There are a variety of virus scan errors:**

* Virus scan server error

* No virus scan profile is selected as the default.

* Virus scan errors should not block the deployment process. The virus scan should be configured in such a way so as not to disturb the deployment process.

* Also, a default virus scan profile should be selected in the system or switched off entirely.

* See SAP Note: <https://launchpad.support.sap.com/#/notes/3052386>

### Conclusion

After going through this post, you should be able to migrate and deploy[SAPUI5](https://community.sap.com/topics/ui5) applications using Visual Studio Code. I hope this guide has been helpful in getting you migration of the SAPUI5 application to Visual Studio Code and deploying SAPUI5 applications. If you have any questions or comments, please feel free to leave them below.

* Please follow <https://community.sap.com/topics/ui5> for SAPUI5 Topic related updates.

* Post questions and answers on SAPUI5 [here](https://answers.sap.com/tags/500983881501772639608291559920477).

* Read other posts on SAPUI5 [here](https://blogs...