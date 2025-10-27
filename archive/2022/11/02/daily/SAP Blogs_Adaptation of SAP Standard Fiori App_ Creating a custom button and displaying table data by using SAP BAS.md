---
title: Adaptation of SAP Standard Fiori App: Creating a custom button and displaying table data by using SAP BAS
url: https://blogs.sap.com/2022/11/01/adaptation-of-sap-standard-fiori-app-creating-a-custom-button-and-displaying-table-data-by-using-sap-bas/
source: SAP Blogs
date: 2022-11-02
fetch_date: 2025-10-03T21:31:55.741805
---

# Adaptation of SAP Standard Fiori App: Creating a custom button and displaying table data by using SAP BAS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Adaptation of SAP Standard Fiori App: Creating a c...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/156314&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adaptation of SAP Standard Fiori App: Creating a custom button and displaying table data by using SAP BAS](/t5/technology-blog-posts-by-members/adaptation-of-sap-standard-fiori-app-creating-a-custom-button-and/ba-p/13526261)

![former_member679920](https://avatars.profile.sap.com/former_member_small.jpeg "former_member679920")

[former\_member679920](https://community.sap.com/t5/user/viewprofilepage/user-id/679920)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=156314)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/156314)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13526261)

‎2022 Nov 01
5:58 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/156314/tab/all-users "Click here to see who gave kudos to this post.")

21,028

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

Hi All,

Great Day,

Hope everyone are doing good!!!

**Problem Statement:**

In order to enhance the initial screen by adding custom button with popup table in the fragment here I am using request maintenance F1511(Standard App).

**Adaptation Project:**

Adaptation is a feature of SAPUI5 flexibility that allows to make UI changes for all users. By using SAP BAS, you are leveraging features of UI5 Flexibility and able to adapt and extend UI5 applications without changing the base app, which allows seamless upgrades and lifecycle stability.

it will an Adaptation Project for an On-Premise System we will be connecting to the on-premise system in our case and will be extending request maintenance application in this blog

**Steps for  Adaptation Project in BAS:**

In the development environment prerequisite will be having access to  the BAS development  environment and in which it is connected to the required destination maintained and connection established. And also development and deployment access int he abap system connected to.

Let’s go over a series of steps below for the  Adaption Project.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture1-44.png)

creating new project

1. Select the Adoption project and Click on Start

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture2-34.png)

2. Select the Target Environment from the template creation

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture3-35.png)

Traget enviroment selection

3. Here, we have ABAP environment for me so I selected ABAP from the drop-down then click on Next button.it means BAS is connected to On-Premise SAP system connected using cloud connector.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture4-29.png)

ABAP System environment Selection

4.In the next section about adaption project, basic information needed. Enter the project name as you like but you must fallow some naming convention to fill project name and name space will auto populate based on project name. Click Next.

custom.<project name> will be created by default as we are creating a custom adaptation for the stander application.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture5-21.png)

5. In the configuration part we must have select the System for that you have to add the destinations in the BTP cockpit destination section.

there destinations will help to connect with the targeted system and establish the communication with the system

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture6-20qq.png)

6. After System selection, it will auto populate the Selection of Application that you need to Adapt/Extend the Fiori application. In the drop-down section you can search with the name or Application ID and select the application which you need to extend.

We will be checking for the Application which be extended and also the application ID in the system.
we can search the same by application name as mentioned in the above point or get the same details from the Fiori App library . we can get the required details from the app library in this case its  F1511 search for application and in the configuration section we can find the details.

Here I am selecting Standard App app Id-  F1511(Request maintenance App).

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture7-20.png)

7.Select the version as per configuration and then click on Finish. In the below screen safe mode determines the developer flexibility, in safe mode developer will have less freestyle capabilities and it will allow the application to be compatible with the future upgrades for the targeted application releasing

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture8-21.png)

8. The adapted application will be automatically open in the new workspace please find the attached screenshot

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture9-16.png)

**App Extension process:**

In the web App section, you can find the **manifest.appdescr.varient** file and right click on it and there you can find the **Open SAPUI5 visual editor**. Please find the attached screen shot for reference.

**manifest.appdescr.varient** is the manifest file we will be using for this variant of the application.
we would be having the specific actions available to be performed recommended to us as a options when we open the application in the editor.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture10-17.png)

Preview an Fiori Application from BAS

As per the current scenario we are looking to add a button with a fragment and in the related controller we will be specifying the logic and model related bindings for the application  . We are creating a fragment shown as below.

Click on Edit Mode, to add the custom button footer section right click on the footer section and then select the  **Add : Fragment** option.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture11-12.png)

Once you click on it you can see  the below details and by creating button create new Fragment, the target aggregation which you can able to add the controls in it.

Along with the add fragment we have the options to add content and Extend with controller.

![](/legacyfs/online/storage/blog_attachments/2022/09/Picture12-10.png)

* Give the Fragmen...