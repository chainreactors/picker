---
title: Searching Development Objects with the ABAP Object Search
url: https://blogs.sap.com/2022/12/15/searching-development-objects-with-the-abap-object-search/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:27.147809
---

# Searching Development Objects with the ABAP Object Search

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Searching Development Objects with the ABAP Object...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46530&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Searching Development Objects with the ABAP Object Search](/t5/application-development-and-automation-blog-posts/searching-development-objects-with-the-abap-object-search/ba-p/13548451)

![arminfarmani](https://avatars.profile.sap.com/a/d/idad94a4d40e45d99c77a884d4d007644c4df19d19aaa0029b1325e51357ca9417_small.jpeg "arminfarmani")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[arminfarmani](https://community.sap.com/t5/user/viewprofilepage/user-id/44875)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46530)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46530)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548451)

‎2022 Dec 15
5:54 PM

[21
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46530/tab/all-users "Click here to see who gave kudos to this post.")

6,647

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Hi everyone,

As most of you probably already know, there is the famous Ctrl+Shift+A search in ABAP Development Tools (ADT) to search for development objects in an ABAP system. So, you might wonder, why am I writing about the topic of searching for development objects if there’s a perfectly functioning solution already available? I’m glad you asked! Let me introduce you to the new **ABAP object search** in ADT and let me explain why its features make it a powerful tool for your everyday search. I will also show you why and when exactly you are going to need it by providing an example.

### **Why use the new ABAP Object Search?**

While the Ctrl+Shift+A search is very handy for quickly searching and opening development objects, the new ABAP object search does come with lots of more nuanced features and benefits. I will briefly mention some major advantages of the ABAP object search before showing a real-world example to you:

* You can execute different actions on multiple development objects from your search result by selecting them and then using the context menu. Some prominent actions are running ATC checks or unit tests for one or more objects.

* It’s also possible to delete development objects by using the context menu on the entries of your search result list.

* You can group and manually configure the columns of your results to order the result list in whatever way benefits you the most.

* The ABAP object search allows you to use the element info on your search results so that you can simply press F2 to get quick information on any given object.

* The search results are kept for the current ADT session whereas it vanishes in case of the Ctrl+Shift+A search once you decided to open a development object.

### **How to Open the ABAP Object Search in ADT:**

To open the ABAP object search in ADT, you can choose **Search->Search…** or alternatively use the shortcut Ctrl+H. Then the following **Search** dialog is opened:

![](/legacyfs/online/storage/blog_attachments/2022/12/ABAP_Object_Search_Dialog-2.png)

ABAP Object Search

In case you initially don’t see the tab **ABAP Object Search**, choose the **Customize…** button and select the checkbox for **ABAP Object Search**, as can be seen in the following screenshot:

![](/legacyfs/online/storage/blog_attachments/2022/12/Customize_ABAP_Object_Search-1.png)

Customize Your Search

### **Example: Finding Released APIs in an ABAP System**

Now, we will go through an example use case to better understand how to use the ABAP object search. Let’s say that we are interested in finding all those released APIs that start with the string “/DMO” in an ABAP system. How do we find them?

As you can see in the dialog, there are two fields right after our chosen **Project**. Those fields are the **Object Name Pattern** and the **Property Filter**. By using the right combination, we’re able to find all the objects that we are interested in.

To find all the released APIs, we just have to do the following:

1. Use content assist with Ctrl+Space in the **Property Filter** field (see also the following screenshot).

2. Choose **api**.

3. After choosing the property **api**, the content assist offers us in the next step multiple values. We choose **RELEASED**.

![](/legacyfs/online/storage/blog_attachments/2022/12/Content_Assist-2.png)

Use the Content Assist

If we would now select **Search**, we would find all the released APIs for the project **DEMO**. But to show how the object name pattern works, we additionally write **/DMO** in the field **Object Name Pattern** and after that we finally select **Search**. You will now see all those released APIs that start with “/DMO” in their name. In the system that I am using, 28 objects were found that match the object name pattern and property filter, and it looks like this:

![](/legacyfs/online/storage/blog_attachments/2022/12/Search_Result_View-2.png)

### **Conclusion and Further Remarks**

You’ve made it all the way to the end, congratulations! For those of you who still haven’t had enough, I would like to show you one more feature of the ABAP object search that is pretty cool. If you look at my result list from the last screenshot, you might think, the objects are not ordered in a way that is appealing. Therefore, we open the dropdown menu of the **Group Objects by** icon in the toolbar and then choose **Object Type**. Now, as you can see in my next screenshot, the development objects are nicely ordered by their type.

![](/legacyfs/online/storage/blog_attachments/2022/12/grouped_by_type-1.png)

I hope you will find the ABAP object search as useful as I do, and I would be happy to get your feedback. Please feel free to share your thoughts in a comment. You can also follow my profile to keep getting updated about future developments.

### Learning Materials

Here are some extra links and resources that you may find helpful:

* [ABAP object search Documentation](https://help.sap.com/docs/BTP/5371047f1273405bb46725a417f95433/46b80f0b01f84f429df5459bdf4fbf85.html?version=Cloud&locale=en-US)

* [Resources r...