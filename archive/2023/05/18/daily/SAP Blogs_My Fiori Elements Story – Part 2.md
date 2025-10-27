---
title: My Fiori Elements Story – Part 2
url: https://blogs.sap.com/2023/05/17/my-fiori-elements-story-part-2/
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:48.848386
---

# My Fiori Elements Story – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* My Fiori Elements Story – Part 2

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160683&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [My Fiori Elements Story – Part 2](/t5/technology-blog-posts-by-members/my-fiori-elements-story-part-2/ba-p/13553884)

![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")

[Sharathmg](https://community.sap.com/t5/user/viewprofilepage/user-id/174516)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160683)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160683)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553884)

‎2023 May 17
10:44 PM

0
Kudos

1,594

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

**My Fiori Elements Story – Part 2**

This blog series on Fiori Elements is my experiences with Fiori Elements – development and customizations. The part 1 of the blog is available in the link: [My Fiori Elements Story - Part 1](https://blogs.sap.com/2023/04/04/my-fiori-elements-story-part-1/).

The list of topics covered over the two blogs are below:

1. Provide additional filters

   1. One filter is a property from the existing entity set

   2. Override Annotations

2. Provide Custom buttons in the toolbar

   1. UX feature – provide icons to the buttons

3. Invoke a custom OData service on the click of the buttons

   1. Usage of JS promise in service calls

4. Remove the navigation from List Report to Object Page

5. « Manifest.json » configurations on the table

   1. Multi selection of elements in the table

   2. Provide excel export feature on the table

6. Provide a popup on click of the custom button

   1. Integrate the help into the popup fields

7. UX feature – provide an Info toolbar to the table on selection of entries

8. Adaptation Project of the Duplicate App

   1. One filter was a new custom property with predefined values

9. Enable features – Enable Excel export, Growing threshold

10. Change files in the changes folder

11. Launchpad configuration of the adaptation project

Point 1 to 5 are covered in the Part 1 of the blog. In this blog, we will look into the points 6 to 11.

6. Provide a popup on click of the custom button

To add a custom button to the table, we discussed the steps in the part 1 of the blog, by using the extension wizard on the project. In the process of creating the custom button, a controller is created by the wizard. We will be using the same controller throughout the project to implement our customizations to the Fiori elements – List report app.

The generated custom controller is defined using sap.ui.controller. In continuing the same definition, to define the modules I made the use of jquery.sap.require.

In my project, have synchronously loaded the modules “ExtensionAPI” and “ushell”.

```
jQuery.sap.require("sap.suite.ui.generic.template.ListReport.extensionAPI.ExtensionAPI");

jQuery.sap.require("sap.ushell.library");
```

***Detour:*** The extensionAPI is used to refresh the list report table. It can used especially when the there is a need to update table records and ensure that changed data is immediately visible to users.

Once we have the custom button, the relevant event method is also available in the controller.

Prior to invoking a popup, we need to create fragments for the same. In my project, I maintained fragments in a separate folder under ext folder.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic1.png)

App Folder Structure

Now that the fragment is created we shall invoke the fragment in the event – method handler using the fragment load method.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic2.png)

Controller code to open popup

Now, on click of the button the popup opens up.

1. Integrate the help into the popup fields

Additional to the popup, I made use of the ValueHelpDialog control inside the help fragment, to provide the standard help framework. So, on the separate fragments for value help, valuehelpdialog control is included with method handlers for “ok”, “cancel”, “afterClose”. The parameters are passed using the parameters “key” and “descriptionKey”.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic3.png)

ValueHelpDialog control

7. UX feature – provide an Info toolbar to the table on selection of entries

The info toolbar was not requested by the client. However, the intention was to display to users the number of entries selected for the operation.

The approach to include an information toolbar on the table was as follows:

i. Get the handler to the table

The static id of the list report table can be pulled up from the Elements tab of the browser in which app is tested.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic4.png)

ii. Prepare the object of type sap.m.ToolBar

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic5.png)

iii. Include content for the info tool bar

The object infoToolbar’s method insertContent shall be used to include the text to be shown to the users.

iv. Insert the info tool bar to the table

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic6.png)

        v. Additionally, I made the info tool bar as sticky to ensure that message is displayed , when user scrolls the entries in the table.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic7.png)

         vi. In order to show the exact number of entries selected by user, I had to somehow trigger the event handler for the table on Select all. Now, the challenge with Fiori Elements List report was that I did not find a way to find event handler for the event “onSelectionChange” declaratively. So, I did the event binding using the “attachSelectionChange” method.

![](/legacyfs/online/storage/blog_attachments/2023/05/My-Fiori-Elements-Story_2_Pic8.png)

8. Adaptation Project of the Duplicate App

Now, we have the copy of standard app with customizations ready for use. However, for further personalization, I chose to adapt the project. Hence, I created an Adaptation project using the Web IDE.

In the Adaptation wizar...