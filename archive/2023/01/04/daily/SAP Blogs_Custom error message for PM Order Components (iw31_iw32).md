---
title: Custom error message for PM Order Components (iw31/iw32)
url: https://blogs.sap.com/2023/01/03/custom-error-message-for-pm-order-components-iw31-iw32/
source: SAP Blogs
date: 2023-01-04
fetch_date: 2025-10-04T02:59:23.421135
---

# Custom error message for PM Order Components (iw31/iw32)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Custom error message for PM Order Components (iw31...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67919&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Custom error message for PM Order Components (iw31/iw32)](/t5/enterprise-resource-planning-blog-posts-by-members/custom-error-message-for-pm-order-components-iw31-iw32/ba-p/13560579)

![fyagubova](https://avatars.profile.sap.com/d/5/idd5a63ec075d53768574c6d6cfdcaf5c8a755029dd1fd9fde6f671de952a02f8d_small.jpeg "fyagubova")

[fyagubova](https://community.sap.com/t5/user/viewprofilepage/user-id/46311)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67919)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67919)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560579)

‎2023 Jan 03
7:21 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67919/tab/all-users "Click here to see who gave kudos to this post.")

5,718

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

### **Searching User Exits and BADI**

In this blog, we will look at another way to debug and find a place to enhance custom error message. Also, I am going to explain the problem we faced and the solution to it.

P.S You can read my [previous blog](https://blogs.sap.com/2022/12/19/enhancement-for-fiori-finding-the-places-for-enhancement-getting-custom-error-message-abap/) about the enhancement for Fiori.

Problem: The customer wants to get the error message when the user tries to modify any components of the order.

Clarifying the problem: in SAP GUI run t-code **IW32** -> enter test order -> and click on **Components**

![](/legacyfs/online/storage/blog_attachments/2022/12/image8-10.png)

So, if the user is not in set **ZUSERS** and the order type is **‘PM01’**, in this case, the user shouldn’t modify the components and get the error message with the text *“You are not authorized to change order components! For further information contact authorized staff.”*

For solving this problem, first, we are going to find an enhancement point for this screen. We start with searching **BADI**s.

Method for finding BADI:

Run t-code SE24 and display class **CL\_EXITHANDLER** -> set a breakpoint on method **get\_class\_name\_by\_interface** in class-method **GET\_INSTANCE** – because of this breakpoint, we’ll be redirected to the debugger screen when we click/run any button/t-code. Just press F8 to continue.

![](/legacyfs/online/storage/blog_attachments/2022/12/image3-9.png)

-> Go back and run t-code IW32 -> Enter test order and open Components -> On item line add a new component -> In debug screen open ***exit\_name*** value – this is a BADI for Components screen. (**IWO1\_ORDER\_BADI**) If we continue with F8 exit\_name will be changed to **W\_RETAILSYSTEM\_IDENT**. It means we can implement both of these BADIs for controlling components.

![](/legacyfs/online/storage/blog_attachments/2022/12/image9-8.png)

To make sure that one of these BADIs is relevant to our problem we have to look through the methods of BADI and the import/export parameters of the methods.

![](/legacyfs/online/storage/blog_attachments/2022/12/image2-9.png)

For instance, in this BADI (IWO1\_ORDER\_BADI) there is **AUTHORITY\_CHECK\_AUART\_ACTIVIT** which looks relevant according to its **import/export parameters**. But when we implement this BADI, the result of this implementation is if the user is not in ZUSERS, then the user won’t be able to even open the order. So that’s why our implementation won’t be successful. And we have the same situation in W\_RETAILSYSTEM\_IDENT BADI. That’s why we cannot write the error message in this BADI too.

Another method to find BADI is searching BADI using **CALL BADI** statement in debugger. After setting a breakpoint at statement ‘CALL BADI’ we reach the other two BADIs but according to their parameters we cannot implement these BADIs for our problem.

Because of unsuccessful implementation in BADI, we are going to search for **User Exits** to enhance for Components screen.

One of the ways for finding user exits is by searching exits according to their package. First, find the package of Components screen: in Components screen click on **System** -> **Status** -> double click **on Program (Subdynpro)** name - you can find the package name from program **Attributes**.

![](/legacyfs/online/storage/blog_attachments/2022/12/image5-11.png)

Go to **SE84** and open: *Enhancement* -> *Customer Exits* -> *Enhancement* – execute package of Components screen. The list of user exits and their description will be displayed.

![](/legacyfs/online/storage/blog_attachments/2022/12/image6-7.png)

Through the package, we reach limited user exits and none of them is relevant to our problem. That’s why we explain below another method for finding user exits.

In Components screen turn on the debugger with /h and add any component. In debugger screen set a breakpoint at statement **CALL CUSTOMER-FUNCTION**.

![](/legacyfs/online/storage/blog_attachments/2022/12/image11-6.png)

Then continue with F8 and you will see the codes below:

![](/legacyfs/online/storage/blog_attachments/2022/12/image13-5.png)

While you continue with F8 you will see a function module with different *parameters and id*. For choosing the right user exit for our solution, again, we have to focus on the user *exit’s parameters*. For example, this exit which is shown above picture doesn’t have parameters for the error message or exception. So, we continue with F8 until we find the exit with relevant parameters.

During debugging I found these two user exits (mentioned below pictures) which look relevant according to their parameters. After finding the user exit place, our next step will be finding their name and project.

Tips: while debugging for user exits, if we click F5 to see what code is inside the user exit. If it is redirecting to include of exit it means this exit **has already been implemented** and has been assigned to any project, and if it’s not redirecting to the include it means **it’s not implemented**.

![](/legacyfs/online/storage/blog_attachments/2022/12/image14-1-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/image15-1-1.png)

In our system, none of these user exits has been implemented and we are going to find exit name for assigning it to the project.

In t-code **SE80** open include shown picture and search for user exit id (011 or 014). We will continue with user exit with id 011. Enter to function module with id ‘011’ to see the code inside.

![](...