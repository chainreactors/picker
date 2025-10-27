---
title: ROUTING AND NAVIGATION IN SAP UI5
url: https://blogs.sap.com/2023/08/07/routing-and-navigation-in-sap-ui5/
source: SAP Blogs
date: 2023-08-08
fetch_date: 2025-10-04T12:01:31.612406
---

# ROUTING AND NAVIGATION IN SAP UI5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ROUTING AND NAVIGATION IN SAP UI5

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164395&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ROUTING AND NAVIGATION IN SAP UI5](/t5/technology-blog-posts-by-members/routing-and-navigation-in-sap-ui5/ba-p/13575024)

![Rahul_Kanti](https://avatars.profile.sap.com/9/3/id9326666b76ff0d84bd458c9800552a97dffcd480c496d793c0b04721e0d35cad_small.jpeg "Rahul_Kanti")

[Rahul\_Kanti](https://community.sap.com/t5/user/viewprofilepage/user-id/155536)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164395)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164395)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575024)

‎2023 Aug 07
6:54 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164395/tab/all-users "Click here to see who gave kudos to this post.")

23,810

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

## **INTRODUCTION**

Modern web applications must have routing and navigation capabilities. User navigation between various pages and views is made possible by them. SAP UI5 provides us with these features.

The method of routing involves determining which views or pages should be displayed in response to a specific URL or hash fragment request. On the other hand, the process of moving from one perspective to another while following established paths is known as navigation.

In SAPUI5, the Router class is used to control routing and navigation. The responsibility of the Router class is to parse the URL, match it to a route, load the corresponding view, and then show it.

## **DEFINING ROUTES**

In the **manifest.json** file, we can define the routes by specifying the pattern, name, and target view for each route. Below is the example for the complete configuration of **manifest.json** file

![](/legacyfs/online/storage/blog_attachments/2023/08/Routes.png)
***IMAGE 1***

In the above image 1

* “routes” is the array that contains the individual routes.

* The "pattern" property defines the URL hash fragment pattern. In the first case, an empty string refers to the default route, which will match when the URL has no hash fragment, whereas in the second case route will match when the URL has a hash fragment of "#View1."

* The "name" property is the name given to a route, in the first case, it's named "home", whereas in the second case it’s named “View1”.

* The target represents the name of the target view that will be displayed when this route is matched. In the first case, it refers to the "home" view, whereas in the second case it refers to the “View1” view.

## DEFINING TARGETS

Once we are done with configuring the “routes” array, then we need to specify the respective targets for each routes/view. Below is the example for the same.

![](/legacyfs/online/storage/blog_attachments/2023/08/Targets.png)

***IMAGE 2***

In the above image 2

* “targets” is the array that contains the individual targets.

* **"**home**"** and **"**View1**"** are the names of the targets, which are referenced by their respective routes

* “viewType” specifies the type of view is “XML”

* "transition" specifies the type of transitional effect that will be used during navigation in this case its slide.

* The "clearControlAggregation" property determines whether the target's container control should be cleared before adding the new view.

* “viewId” it indicates unique Id for respective views

* “viewName” refers to the name of the view file.

## **HANDLING NAVIGATION**

After doing all the routes and targets configurations in the **manifest.json** file we can utilize the **navTo()** method of the Router class. The **navTo()** method takes a route as its argument,

Considering the home.view.xml file as follows:

![](/legacyfs/online/storage/blog_attachments/2023/08/Navigate-view.png)***IMAGE 3***

Having the controller file as:

![](/legacyfs/online/storage/blog_attachments/2023/08/Navigate-Controller.png)

***IMAGE 4***

Here in the above image 4, home.view.xml file has a button which is attached to a method named “onButtonClick” once this method is triggered from the view, we call oRouter.navTo("View1") to navigate to the "View1" route, which is defined in the "routes" section of the routing configuration.

The "View1" route's pattern will be compared by the router when the navTo method is called, and if a match is found, the "View1" view linked to the "View1" target will be loaded and shown. The target configuration will be followed when applying the "slide" navigation transition effect.

## **PASSING DATA DURING NAVIGATION**

We can pass data between views during navigation using parameters. Considering the example below:

![](/legacyfs/online/storage/blog_attachments/2023/08/onshowEmpDetails.png)

***IMAGE 5***

In the above image 5 we are navigating to “EmployeeDetails” view and passing the id parameter with the value of the variable employeeID.

![](/legacyfs/online/storage/blog_attachments/2023/08/onshowEmpDetails1.png)

***IMAGE 6***

By handling the route matched event and using the passed parameter ‘employeeID’, we can fetch the relevant data and update the view dynamically.

Here in the above image 6, we are using ‘employeeID’ retrieved from the URL parameter to fetch the employee details from the backend using oData model, after successful retrieval of the employee details a new JSON model is created ‘oEmployeeDetailsModel’ and is set with the retrieved data in the “EmployeeDetails” view. This allows us to bind controls in the view to display the Employee details. At last, the title of the view is updated with the employee name for better understanding.

Thanks, and Regards

Rahul Bhisham Kanti

* [Basic Navigation](/t5/tag/Basic%20Navigation/tg-p/board-id/technology-blog-members)
* [routing](/t5/tag/routing/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Frouting-and-navigation-in-sap-ui5%2Fba-p%2F13575024%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Full-Page Fit vs. Scrollable Dashboards in SAC which one is better?](/t5/technology-blog-posts-by-members/full-page-fit-vs-scrollable-dashboards-in-sac-wh...