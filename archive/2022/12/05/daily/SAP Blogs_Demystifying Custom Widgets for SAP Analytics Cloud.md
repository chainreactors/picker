---
title: Demystifying Custom Widgets for SAP Analytics Cloud
url: https://blogs.sap.com/2022/12/04/demystifying-custom-widgets-for-sap-analytics-cloud/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:30:48.803044
---

# Demystifying Custom Widgets for SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Demystifying Custom Widgets for SAP Analytics Clou...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162843&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Demystifying Custom Widgets for SAP Analytics Cloud](/t5/technology-blog-posts-by-members/demystifying-custom-widgets-for-sap-analytics-cloud/ba-p/13566066)

![pranav_kandpal](https://avatars.profile.sap.com/4/7/id47f1055a2eb4281b1df632d8078d820cd1f662f35154bd8687c1de1f1705f796_small.jpeg "pranav_kandpal")

[pranav\_kandpal](https://community.sap.com/t5/user/viewprofilepage/user-id/223932)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162843)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162843)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566066)

‎2022 Dec 04
8:37 PM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162843/tab/all-users "Click here to see who gave kudos to this post.")

10,882

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)

View products (2)

## Introduction

While investigating on a custom solution for SAC widget , I realized there is still a lot of Mist around Custom Widget , primarily towards its hosting as well as creating a basic working version of a custom widget. The aim of this blog is to demystify the basics around custom widget and navigate through the custom widget world smoothly.

The blog will try to cover the below 2 aspects:

* Deployment of Custom Widget in GitHub.

* Creation of a simple custom widget which can be used as a 'Hello world' for navigating through the world of custom widgets.

### Brief Background

Custom widgets is the Robin to the Batman , of course SAC being the Batman here (a bit of goofing around for the DC fans :D). No doubt Custom widget is the sidekick which SAC needs for extensions and adding more powerful features which are not delivered out of the box by SAC. But the question still remain - How do custom widgets provide extensions to SAC apps?

As we all know , SAC is a web based analytical product from SAP (as the name suggests as well) which displays the dashboards in a Web Browser. Web browsers use a combination of HTML , CSS and JS (JavaScript) files to act as an interpreter.

So in short it reads the text from these files and displays the result (which is what we see in the web browser). When you run a SAC dashboard and inspect the page , it will show the list of various files which SAC uses for creating the powerful results of the Dashboards.

You must be wondering , Why am i even mentioning all this? Well the answer to this another question - how is custom widget the sidekick of SAC and how can it be used to add extensions. As I mentioned earlier , a web browser uses JS and CSS files for interpreting what needs to be displayed as an output of the Web Page. A custom widget is also interpreted by the JS and CSS files. Its logic is written in the JS file and its styling is present in the CSS file. All we need to do is to add these files to the Web Page and once added , it will be read by the interpreter of the web page and perform the magic :).

Since SAC now provides the feature of bring your own widget with the custom widget option , this means we can bring our own JS and CSS files (by the custom widget) and add more features to your existing applications. Once a custom widget is added to a SAP Analytical Application , this means when this page will run , it will add also the JS and CSS files of the custom widget for the interpreter of the Web Page :).

Now since this Web Page and the CSS needs to be added to the Web Page , it needs to exist somewhere. Of course we can create these files locally in our PC and host it locally but when this Page will be loaded globally (lets say by another user in a different location) , these files will not be present for the user and the custom widget will not be loaded.Therefore these files need to be present somewhere globally which can be called by anyone across the internet in this whole wide world.

This is where the deployment of the custom widget comes into picture. These JS and CSS files are hosted/deployed somewhere and using a custom JSON file the location information of these files  is added to SAC (and of course more info).

So in short the most important files for a custom widget are :

* JS Files - File holding the function relevant info

* CSS Files - File for styling

* JSON File - File which is loaded in SAC for providing the details about the custom widget.

## 'Hello World' of Custom Widget

Since we discussed some background around Custom Widget , now lets quickly dive into the most important part of this Blog. The deployment of a Custom widget in GitHub. However to deploy a custom widget , we need the files for custom widget. So lets begin with creating a very basic widget which I would refer to as the 'Hello World' for Custom widgets.

Lets make a simple widget which is a button and can be added to the SAC apps - I know there are buttons already present within SAC , but my aim is to showcase how :

* Custom DOMS / Elements can be added to the SAC app

* Event Listeners can be added for the Custom Widgets

* Styling could be added later if needed.

To showcase these features , the easiest option is button and this is why i call it our 'Hello World'.

Without further ado , lets jump over to our most import files for this solution.

### JSON File

Well the JSON file is basically a file which contains some basic information about the Custom widget which is added to SAC to inform SAC about the details about this Custom Widget.

[SAC Custom Widget Developer Guide](https://help.sap.com/doc/c813a28922b54e50bd2a307b099787dc/release/en-US/CustomWidgetDevGuide_en.pdf) provides more details about the custom widget and the section 6.1 within this guide gives more details about the JSON file , the object and properties. JSON file is basically it stores simple data structures and objects in JavaScript Object Notation (JSON) format.

The most important details relevant for us are below :

* Root Object - This is where the attributes of your Custom widget are defined like the Name , Version , description etc. This is elaborated more in the text that follows.

* Web Component Object : This contains information about the JS Files.

* Properties object : This is where the properties of the custom widget could be added. A property would have its own data type and can contain a value

* Method Object : Methods which can be used to perform some operations by the SAC app later or used internally for any specific logic.

*...