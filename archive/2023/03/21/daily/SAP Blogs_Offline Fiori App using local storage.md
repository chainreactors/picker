---
title: Offline Fiori App using local storage
url: https://blogs.sap.com/2023/03/20/offline-fiori-app-using-local-storage/
source: SAP Blogs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:22.493866
---

# Offline Fiori App using local storage

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Offline Fiori App using local storage

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160179&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Offline Fiori App using local storage](/t5/technology-blog-posts-by-members/offline-fiori-app-using-local-storage/ba-p/13550791)

![KarthikaMohan](https://avatars.profile.sap.com/5/5/id551ba19478fd348faa769bf317a9a9d484fc03356168bce15b110768ee77b7cb_small.jpeg "KarthikaMohan")

[KarthikaMohan](https://community.sap.com/t5/user/viewprofilepage/user-id/127152)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160179)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160179)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550791)

‎2023 Mar 20
10:08 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160179/tab/all-users "Click here to see who gave kudos to this post.")

3,931

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

Hello SAP Community members,

This is my first blog post in the SAP Community and I am a bit anxious already ![:slightly_smiling_face:](/html/@5D2D4274E851E17FD6B6AA8F470AA6B3/emoticons/1f642.png ":slightly_smiling_face:") I started my career at SAP Labs 12 years ago in the development support of Materials Management domain (a mix of technical and functional knowledge) and found my passion for pure technology. After leaving SAP Labs, I focused as an SAP Development Consultant and since then, it has been an even more exciting journey learning and working on different SAP Technologies – Fiori Apps, Cloud Application Programming, SAP BTP etc.

In my quest for learning new exciting SAP tech, I have spent a lot of time browsing through and learning immensely from the SAP Blogs and thought-provoking discussions in this community. So with a grateful feeling in my mind, here it goes… my first blog!

Recently I worked on the development of an S/4 Fiori On-Premise app which involved ordering of products for a Retail chain in Europe – wherein the product list proposal populated by automatic replenishment runs in SAP F&R (Forecasting and Replenishment) can be adjusted by the Store employee when needed. A special feature needed was that, the employee should be able to operate the app when online and offline (say, when the employee is adjusting a product count when inside a walk-in freezer). Since the automatic replenishment run from F&R runs daily, the product list sent is valid only for a day.

![](/legacyfs/online/storage/blog_attachments/2023/03/Fiori-On-Premise-architecture.png)

Fiori architecture

![](/legacyfs/online/storage/blog_attachments/2023/03/App1.png)
*App when Online*

![](/legacyfs/online/storage/blog_attachments/2023/03/App2.png)

App when Offline

Because the data necessary to be available offline is not a huge set of data (each store has its own order list), the decision was made to use :

* Local Storage – data is stored in local storage – data is retained when you close the browser (**sap.storage.Type.local**)

Below are the various scenarios with the app usage and how the goal was achieved in Fiori :

* The check on online/offline status happens with the *onLine* function.

* When the app gets launched and the user is :

  + *Online* – product list data is retrieved from the backend, displayed and saved in local storage with a store-specific storage key (a combination of the store number and today’s date)![](/legacyfs/online/storage/blog_attachments/2023/03/1-39.png)

  + *Offline* – product list data is retrieved from the local storage with the store-specific storage key![](/legacyfs/online/storage/blog_attachments/2023/03/2-23.png)

* When the user updates the order quantity of a product and the user is :

  + *Online* – the updated order quantity is directly sent to the backend via a call to the OData service.

  + *Offline* – the new order quantity is updated in the local storage![](/legacyfs/online/storage/blog_attachments/2023/03/3-26.png)

* The items changed offline will be stored in the local storage until the user goes online again. Hence an explicit ‘*Order*’ button was introduced to send these changed items to the backend system.

  + This button is enabled when the user is online again and there are items which were changed offline.

  + An auto-sync feature was also introduced in the *“init”* method of the controller to check every 10 seconds - if the user is online. If so, an auto-update of the changed items to the backend is triggered.![](/legacyfs/online/storage/blog_attachments/2023/03/4-18.png)

* The browser local storage for all the previous dates - except the offline storage dated today – is removed.

![](/legacyfs/online/storage/blog_attachments/2023/03/5-19.png)

* An additional feature was to have the ‘Order’ button in green color when the user is online & disabled when the user is offline. This informs a busy store employee if his PDA is online or not.

Even though a local storage is pretty commonly used in Fiori apps, it was an interesting experience for me to use local storage to store the whole product list, discuss more on different store employee scenarios and influence the user experience towards a quite seamless transition between online and offline modes.

### Conclusion

After going through this post, you should be able to use the local storage to develop Fiori applications which can switch seamlessly between online and offline modes without losing data. If you have any feedback or comments, please feel free to leave them below.

* Please follow the [SAP Fiori](https://community.sap.com/topics/fiori) topic page for related updates.

* Post questions and answers on SAP Fiori [here](https://answers.sap.com/tags/73554900100700000977).

* Read other SAP Fiori blog posts [here](https://blogs.sap.com/tags/73554900100700000977/).

* Please follow my profile karthika\_mohan13 for future posts.

Thank you! ![:slightly_smiling_face:](/html/@5D2D4274E851E17FD6B6AA8F470AA6B3/emoticons/1f642.png ":slightly_smiling_face:")

* [offlineapps](/t5/tag/offlineapps/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Foffline-fiori-app-using-local-storage%2Fba-p%2F13550791%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP IQ...