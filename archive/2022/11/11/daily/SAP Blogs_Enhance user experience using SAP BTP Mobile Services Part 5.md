---
title: Enhance user experience using SAP BTP Mobile Services Part 5
url: https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-5/
source: SAP Blogs
date: 2022-11-11
fetch_date: 2025-10-03T22:22:48.291546
---

# Enhance user experience using SAP BTP Mobile Services Part 5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Enhance user experience using SAP BTP Mobile Servi...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163934&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enhance user experience using SAP BTP Mobile Services Part 5](/t5/technology-blog-posts-by-sap/enhance-user-experience-using-sap-btp-mobile-services-part-5/ba-p/13568483)

![nhatdoan](https://avatars.profile.sap.com/a/5/ida5490a07f5959f18b25154fff95782c659e3e1e1aab073083346d715149a0f6b_small.jpeg "nhatdoan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[nhatdoan](https://community.sap.com/t5/user/viewprofilepage/user-id/39493)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163934)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163934)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568483)

‎2022 Nov 10
7:52 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163934/tab/all-users "Click here to see who gave kudos to this post.")

893

* SAP Managed Tags
* [SAP Mobile Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Services/pd-p/668874921104038800958643358380369)

* [SAP Mobile Services

  Software Product Function](/t5/c-khhcw49343/SAP%2BMobile%2BServices/pd-p/668874921104038800958643358380369)

View products (1)

My name is Nhat Doan. I am currently in SAP Student Training and Rotation (STAR) Program. In my first rotation, I have a chance to join CoE Mobile & UX team. I have learned a lot of things especially about current developments in mobile technology. Today, smartphones become essential for daily life. Businesses are using mobile applications to serve their clients and they will see many benefits such as brand building, customer connection, and profit boosts. I would like to share some topics concerning mobile development.

1. [Build ProductCatalog application with AppGyver and Northwind OData service.](https://blogs.sap.com/2022/11/02/enhance-user-experience-using-sap-btp-mobile-services/)

2. [Build ProductCatalog application with SAP MDK and Northwind OData service.](https://blogs.sap.com/2022/11/07/enhance-user-experience-using-sap-btp-mobile-services-2/)

3. [How to style the MDK application.](https://blogs.sap.com/2022/11/08/enhance-user-experience-using-sap-btp-mobile-services-part-3/)

4. [How to run MDK application on virtual device and override resources.](https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-4/)

5. [How to reads log, traces issue, and measures performance for MDK application.](https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-5/)

**How to reads log, traces issue, and measures performance for MDK application**

For this blog, I would like to share how I use Android Studio to read logs, traces issue, and measure the performance for MDK application.

**Read log**

Set up to run the application on virtual device.  Open Android Studio, select Logcat tab at the bottom of the application. Select the package (AppId) that we want to see the log.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_1.png)

*Figure 1: Use Logcat to see the log of MDK application*

**Trace issue**

Here is an example of updating a record unsuccessful. The application shows the error.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_2.png)

*Figure 2: The application show error when updating a record*

Go to Logcat and check the log. We can see the error log in the Logcat.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_3.png)

*Figure 3: The error log in Logcat*

Based on the log error, the issue is we update the record using PATH method (The **UpdateValue** in action file is **Merge**). However, the oData service does not support PATCH. We need to change the **UpdateMode** value  from **Merge** to **Replace**.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_4.png)

*Figure 4: Change UpdateMode to Replace*

Now the application can update the records successfully.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_5.png)

*Figure 5: The application run normally after fixing the bug*

**Performance measure**

This example shows how to measure the time the application performs an action to update a record and the actual time of oData service takes to update the record. It will be very useful for analyzing performance issue of MDK application.

We can use the rule file to log the time of an action. The code below is the content of ExecuteUpdateCartItem.js

```
export default async function ExecuteUpdateCartItem(context) {

    try {

        console.log('ExecuteUpdateCartItem start')

        console.time('ExecuteUpdateCartItem')

        return await context.executeAction({

            'Name': '/ProductCatalog2/Actions/Cart/UpdateCartItem.action'

        })

    } catch (e) {

        console.error(e);

    } finally {

        console.timeEnd('ExecuteUpdateCartItem')

        console.log('ExecuteUpdateCartItem end')

    }

}
```

This rule file will be called when we update a record instead of using UpdateCartItem.action directly.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_6.png)

*Figure 6: Use rule file to have the log*

Run the application and check the log. Now we have the time for performing UpdateCartItem.action in the log.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_7.png)

*Figure 7: The time of executing UpdateCartItem.action*

We can use **App Inspection** in **Android Studio** to measure the time of calling oData service to update a record. Click on **App Inspection** at the bottom of **Android Studio**. Select the package that we want to inspect (AppId). And select **Network Inspector** tab. Select the timeline that we want to inspect.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_5_8.png)

*Figure 8: The time of sending and receiving data*

We can use the time from the log file and from **App Inspection** for analyzing the performance of MDK application.

**Conclusion**

We have just finished reading logs, analyzing issues, and tracing performance for MDK application. It will be useful in the future for fixing bug, or analyzing the performance issue.

Please let me know your feedback, questions in the comments. I would be happy to get back to you.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fenhance-user-experience-using-sap-btp-mobile-services-part-5%2Fba-p%2F13568483%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCE...