---
title: How to set a Fiori Elements object page as a detail page of SAP My Inbox application
url: https://blogs.sap.com/2023/03/02/how-to-set-a-fiori-elements-object-page-as-a-detail-page-of-sap-my-inbox-application/
source: SAP Blogs
date: 2023-03-03
fetch_date: 2025-10-04T08:31:37.155621
---

# How to set a Fiori Elements object page as a detail page of SAP My Inbox application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to set a Fiori Elements object page as a detai...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161712&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to set a Fiori Elements object page as a detail page of SAP My Inbox application](/t5/technology-blog-posts-by-members/how-to-set-a-fiori-elements-object-page-as-a-detail-page-of-sap-my-inbox/ba-p/13559656)

![Dipankar](https://avatars.profile.sap.com/4/e/id4eb6437181ac523210bb1eaa6c8acc41fabbf0340e3846a91e5593e9bb49b8ca_small.jpeg "Dipankar")

[Dipankar](https://community.sap.com/t5/user/viewprofilepage/user-id/2779)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161712)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161712)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559656)

‎2023 Mar 02
11:47 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161712/tab/all-users "Click here to see who gave kudos to this post.")

3,943

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

**Introduction:**

This blog showcases the approach I took to achieve the requirement of Customizing SAP My Inbox App. Even though it comes many extension possibilities like extending detail page (regular extension approach) or add more attributes to the detail page. But achieving the requirement when your app is Fiori Elements was challenging.

**Requirement:**

As part of other requirements, we had developed a List Page ->Object Page application. For My Inbox app’s detail page, we wanted to reuse this previously developed object page. Instead of creating a new app for the detail page, we wanted to reuse to reduce development and maintenance efforts.

**Architecture:**

I created a new wrapper UI5 application, which consumed the FE as a Component. It had the logic to load the FE elements app and then navigate to the Object Page with the selected context. Below diagram explains it.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-119.png)

Architectural Diagram

**Let us see the details now.**

**First step was to create a new UI5 application as below.**

A Custom SAPUI5 App was created, and ***Component reuse concept*** was utilized.

Component Container –“usage=dashboard” is the name of the app given on the manifest

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-59.png)

Component Container -

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture3-51.png)

Manifest Changes

**Routes** –

A specific route is defined as mentioned in the above blog. And this route contains the ***path:”detail/{scenarioid}/{wfInstanceId}/{taskPath}**”* and the Dashboard App component as target. This is the same path that will be fired from the My Inbox when a task is selected.

“&/detail/LOCAL\_TGW/000001577878/TaskCollection(SAP\_\_Origin='LOCAL\_TGW',InstanceID='000001577878')”

Manifest – Routes ->

(Pls Note : prefix as child was used to know whether the Dashboard App is being run from My-Inbox, found this way cool to handle)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-44.png)

Route Definition

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture5-30.png)

Target Definition

Pls note – No Routingmacthed parameter isn’t required in our case as we are reusing the component and the Detail App is a Fiori Elements App.

Next parameter of the Route- “&/**Child**/zgc\_c\_requests(req\_uuid=guid'00505694-0AD9-1EED-A4CD-A9CC33EA8180',IsActiveEntity=true)”

So on Init of ListReportExt.controller , the hashkey parameter is checked for “Child” parameter and *nav.to* triggered.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-33.png)

Hashkey Parameter - `Child`

Now let us configure the newly created app.

New entry created for our task with “Intend-Based Navigation”. At least an entry for “SEMANTIC\_OBJECT” and “ACTION” is required which is then used in the Fiori Configuration.

Entry created using the **SWFVISU** transaction

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture7-30.png)

entry creation in SWFVISU Transaction

**Fiori Configuration – Target Mapping (Semantic Object, Action and the Parameter below)**

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture8-27.png)

Fiori Configuration

Let us try loading the app and clicking on an item. But the whole App is getting loaded instead of loading the detail page alone

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture-2.jpg)

Our App

After lot of analysis, nav.to was written above for the navigation and another check was written to enable the detail page Full Screen (*Please let me know if there is any better solution to it, looked apt to me for that time*)

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture10-20.png)

Code Snippet for Full Screen

**Issues after deployment-**

* ***Floating Toolbar of the detail page of the Child App is shown below*** ->  you can hide by getting the id of the toolbar and setting it visible(false)

* ***My-Inbox Footer bar and Header Layout Issue*** -> you can fix this layout issue by handling the height of the custom app to 85%.

### Conclusion:

In conclusion, this is how I was able to show the Customized User Task using an wrapper UI5 app.  Hope you find it useful and do share yours with me in comments.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-1.png)

Our App in My-Inbox User task

SAP Note - [2305401 - Integration of SAPUI5 Fiori Applications into My Inbox 2.0 - SAP ONE Support Launchpad](https://launchpad.support.sap.com/#/notes/2305401)

SDK - [Enabling Routing in Nested Components - Documentation - Demo Kit - SAPUI5 SDK (ondemand.com)](https://sapui5.hana.ondemand.com/#/topic/fb19f501b16e4e4991eb6a017770945b)

Keep learning & Keep Sharing!!

Special Thanks to @KrishnaKammaje

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-set-a-fio...