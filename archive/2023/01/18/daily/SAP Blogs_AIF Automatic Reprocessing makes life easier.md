---
title: AIF Automatic Reprocessing makes life easier
url: https://blogs.sap.com/2023/01/17/aif-automatic-reprocessing-makes-life-easier/
source: SAP Blogs
date: 2023-01-18
fetch_date: 2025-10-04T04:08:33.118304
---

# AIF Automatic Reprocessing makes life easier

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* AIF Automatic Reprocessing makes life easier

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163196&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [AIF Automatic Reprocessing makes life easier](/t5/technology-blog-posts-by-members/aif-automatic-reprocessing-makes-life-easier/ba-p/13568122)

![akmal1216](https://avatars.profile.sap.com/9/4/id948e11a366cf66936cc8d044c4d79229fea8866f9f5ad56309440d7a51b2e37e_small.jpeg "akmal1216")

![Employee](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Employee")
[akmal1216](https://community.sap.com/t5/user/viewprofilepage/user-id/120805)

Employee

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163196)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163196)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568122)

‎2023 Jan 17
11:12 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163196/tab/all-users "Click here to see who gave kudos to this post.")

15,123

* SAP Managed Tags
* [SAP Application Interface Framework](https://community.sap.com/t5/c-khhcw49343/SAP%2520Application%2520Interface%2520Framework/pd-p/01200314690800001892)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP Application Interface Framework

  SAP Application Interface Framework](/t5/c-khhcw49343/SAP%2BApplication%2BInterface%2BFramework/pd-p/01200314690800001892)

View products (2)

Dear All,

I would like to share one interesting case related to AIF Automatic Reprocessing in this blog. It made my life easier, so I decided to share it with you ![:smiling_face_with_smiling_eyes:](/html/@61796F7B1C73E81D1D9470FE142AD91D/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

### **Requirement**

Recently I had requirement to make some enhancements in Sales Order change VA02 Tcode. So, to be more exact, in case of adding new item positions the same item position should be created in respective outbound delivery. It could be specific requirement regarding the customer, but customer is always right ![:smiling_face_with_smiling_eyes:](/html/@61796F7B1C73E81D1D9470FE142AD91D/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

### **Problem area:**

So, nothing is special here to do the above requirement. You can easily find include to do the enhancements in **VA02** and use standard BAPI or BDC to insert the new item position to the respective outbound delivery. Some selects and mapping data to BAPI structures. Voila... it is done.

But in the real life not everything is as easy as it sounds. During process I came across with error **VL045 - The sales order &1 is currently being processed by user &2.**

**So, it showed the current sales order is locked by my own user while doing changes in VL02N.**

![](/legacyfs/online/storage/blog_attachments/2023/01/what.jpg)

Yes, that’s correct since both processes are interconnected, inserting the new item position to outbound delivery checks if Sales Order transaction is locked or not.

### **Solution area:**

Then I understood that I need a tool which can save the current payload and re-process it after some time. Besides, user can do some extra changes in VA02, in that case my solution should be triggered until I don't get error message **VL045 - The sales order &1 is currently being processed by user &2.**

So, tool should include number of counters to set how many times my logic should be triggered and amount of time ( minutes/seconds ) to set time interval to the logic triggering.

Additionally, logic should be triggered only and only having VL045 error message.

![](/legacyfs/online/storage/blog_attachments/2023/01/solution.jpg)

And… I found out AIF automatic reprocessing is the best fit here.

So, what’s AIF automatic reprocessing and how to use it in my case. According to the official documentation:

*In the SAP Application Interface Framework, a reprocessing action is the technical representation of a function module that is called by a batch job. A reprocessing action contains the appropriate AIF runtime configuration group and the function module that is called by the reprocessing job.*

*The AIF runtime schedules a reprocessing action for registered error messages according to your settings in the following configuration tables:*

* ***AIF Automatic Reprocessing: Define Reprocessing Action****(transaction code /AIF/REP\_AC\_DEF )*

* ***AIF Automatic Reprocessing: Assign Reprocessing Action****(transaction code /AIF/REP\_AC\_ASGN)*

Firstly, execute **/AIF/CUST** transaction to create namespace via **Define Namespace** and assign the interface to your namespace via **Define Interfaces**. So, here is the result in my case:

![](/legacyfs/online/storage/blog_attachments/2023/01/interface.jpg)

Don’t forget to check the **Move Corresponding Structures**.

As for the **SAP Data Structure** and **Raw Data Structure**, they should have the structure which keeps payload, and it will be used later in FM. In my case, I have created structure which includes three main fields to insert new position to the existing outbound delivery:

![](/legacyfs/online/storage/blog_attachments/2023/01/structure.jpg)

As the next step, expand **Additional Interface Properties** in **/AIF/CUST** and execute **Specify Interface Engines** and set **Structured Persistence** to the following three fields:

![](/legacyfs/online/storage/blog_attachments/2023/01/assign-structure.jpg)

Now we need to create action and FM by executing **Define Actions**. As for the FM

![](/legacyfs/online/storage/blog_attachments/2023/01/define-action.jpg)

As for the FM, choose **Define functions** and insert FM name, by clicking SAVE or ENTER, pop-up asks you copy FM from AIF template. Just click COPY and that’s it.

![](/legacyfs/online/storage/blog_attachments/2023/01/define-fm.jpg)

So far so good. We have already created some basic AIF staff like namespace, interface, persistence structure and action. It is time to do structure and action mapping. To do this, execute **Define Structure Mappings** insert your namespace, interface, and version number. Then in the source structure set your structure which you created in previous steps and do the same with **Assign Actions.**

![](/legacyfs/online/storage/blog_attachments/2023/01/define-mapping.jpg)

Hugh, finally it is time to create the main objects to implement automatic re-processing. First step here is to create runtime group configuration via Tcode  **/AIF/PERS\_CGR**

![](/legacyfs/online/storage/blog_attachments/2023/01/runtime.jpg)

Attention !!! Don’t forget to check **Runtime Cfg Active** and **Run Scheduled** checkboxes.

Now let’s define reprocessing action, using Tcode **/AIF/REP\_AC\_DEF**

![](/legacyfs/online/storage/blog_attachments/2023/01/action-assign.jpg)

Pay attention that **/AIF/RESTART\_MSG** is set.

*The SAP Application Interface Framework delivers the /AIF/RE...