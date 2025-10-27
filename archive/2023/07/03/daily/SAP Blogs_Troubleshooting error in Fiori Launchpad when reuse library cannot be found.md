---
title: Troubleshooting error in Fiori Launchpad when reuse library cannot be found
url: https://blogs.sap.com/2023/07/02/troubleshooting-error-in-fiori-launchpad-when-reuse-library-cannot-be-found/
source: SAP Blogs
date: 2023-07-03
fetch_date: 2025-10-04T11:52:38.446647
---

# Troubleshooting error in Fiori Launchpad when reuse library cannot be found

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Troubleshooting error in Fiori Launchpad when reus...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160176&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Troubleshooting error in Fiori Launchpad when reuse library cannot be found](/t5/technology-blog-posts-by-members/troubleshooting-error-in-fiori-launchpad-when-reuse-library-cannot-be-found/ba-p/13550750)

![alexandr_razinkin](https://avatars.profile.sap.com/1/b/id1bd327d48d4c43cd05a8f37b3985f4e94b32a962a399d1546e045869916679b4_small.jpeg "alexandr_razinkin")

[alexandr\_razinkin](https://community.sap.com/t5/user/viewprofilepage/user-id/756342)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160176)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160176)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550750)

‎2023 Jul 02
7:10 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160176/tab/all-users "Click here to see who gave kudos to this post.")

5,643

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

# Introduction

Reuse Libraries are certainly a significant advantage in the process of developing complicated software. Copy-paste is a kind of antipattern and we should always try to reuse a code.

Fortunately, SAP Fiori allows the creation and usage of reuse libraries.

However, this topic is not covered by detailed documentation and developers sometimes need to struggle with different problems to make it work.

Many people face problems when an application cannot find a library. There can be errors that the library is being searched under the path */sap/bc/ui5\_ui5/ui2/ushell/resources* where it normally cannot be.

There is a lot of advice over the internet to use the registerModulePath function to get it working. This solution can help but it’s a kind of a workaround. If we launch our application through the Fiori launchpad (and we always should do so) then it’s possible to avoid such a direct call by informing SAPUI5 where to find the library in the manifest.json file.

As soon as UI5 can be hosted on different kinds of platforms I would like to note that this article covers the case when UI5 is hosted on ABAP Netweaver on-premise instance.

When I faced that problem on the customer side I needed to investigate some errors and debug some code to find a solution.

Now I would like to share the knowledge that I achieved during the solving of that problem.

I’ll share some technical details about standard SAP mechanisms that are working during the usage of standard and customer libraries. I hope that looking under the hood can help one better understand how it works on the ABAP on-premise instance and troubleshoot possible problems more effectively.

# Error description

For example, you have a Fiori application that depends on a library.

Sometimes you can get an error when the application cannot be opened. In the browser console, you can see that library is searched on the wrong path under /sap/bc/ui5\_ui5/ui2/ushell/resources/…

For example, the error in the browser console can look like this:

![](/legacyfs/online/storage/blog_attachments/2023/07/screenshot_error_ui2_resources.png)

The cause of this error is that the shell does not know the location of the library and searches for it in a standard SAP location.

A cause of this error can be a missing link to the library in manifest.json of the calling application in section sap.ui5 -> dependencies -> libs, for example:

![](/legacyfs/online/storage/blog_attachments/2023/07/screenshot_manifest_lib_reference.png)

The library name in the ‘dependencies’ section of the application’s manifest file must match the ‘id’ of the library which is contained in the library’s manifest file.

Below you can see an example of the ‘id’ parameter in the manifest.json file of a library:

![](/legacyfs/online/storage/blog_attachments/2023/07/screenshot_manifest_lib_id.png)

In the next section, we will look under the hood to see how exactly the shell finds the path of a library given its id.

# How the Fiori application finds the Fiori library

## On the front-end

When the application is started then all dependent library paths are retrieved from the back end.

There exists the following web service in SICF:

/default\_host/sap/bc/ui2/start\_up

This service is called each time before the Fiori application is started from Fiori Launchpad.

In my version of SAP Netweaver, the call is sent from the following piece of code:

/sap/ushell\_abap/bootstrap/abap-dbg.js

function requestFullTM

Note: You must open the Fiori Launchpad with the option sap-ui-debug=true to see debug versions of UI5 javascript sources. For example, the URL can look like this:

<https://<myserver>:<myport>/sap/bc/ui2/flp?sap-ui-debug=true#Shell-home>

After the service is called the response comes as JSON. The response contains a lot of information including the section ‘Dependencies’ with a list of all dependent libraries. If everything was set up and deployed correctly then your custom library should be among these dependencies and its path must also be present.

After that, the shell calls jQuery.sap.registerModulePath from the file /sap/fiori/core-min-0-dbg.js to map the library name with its path.

If something goes wrong then the call to registerModulePath can be missing and the error can occur.

In this case, an explicit calling of this module can help. However, it is always better to find a root cause and make the shell do the call automatically.

## On the backend

When an application or a library is deployed to SAP Netweaver then its manifest is parsed in ABAP and all reference information is put into tables /UIF/LREPDEREFCD and /UIF/LREPDCONTCD. It is more convenient to explore these tables with the help of database view /UIF/LREPVEREFCD.

After that, all dependencies of an application can be retrieved from this view. Also, additional information can also be got including a path of a library.

It is possible to force the recalculation of data in these tables by running program /UI5/APP\_INDEX\_CALCULATE.

All dependencies of an application can be found by the following query to the view /UIF/LREPVEREFCD:

REF\_TYPE = ‘UI5DEP’

REF\_SUBTYPE = ‘LIBRARY’

NAMESPACE contains the id of your application from manifest.json.

For example, let the app id be as in the screenshot below:

![](/legacyfs/online/storage/blog_attachments/2023/07/manifest_of_application_id.png)

Then we can find its dependencies by the following query from se16:

![](/legacyfs/online/storage/blog_attachments/2023/07/query_for_dependencies.png)

Reference to the custom library should be i...