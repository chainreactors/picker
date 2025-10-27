---
title: Enhancement for Fiori — finding the places for enhancement — getting custom error message (ABAP)
url: https://blogs.sap.com/2022/12/19/enhancement-for-fiori-finding-the-places-for-enhancement-getting-custom-error-message-abap/
source: SAP Blogs
date: 2022-12-20
fetch_date: 2025-10-04T01:58:38.219684
---

# Enhancement for Fiori — finding the places for enhancement — getting custom error message (ABAP)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Enhancement for Fiori — finding the places for enh...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160420&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enhancement for Fiori — finding the places for enhancement — getting custom error message (ABAP)](/t5/technology-blog-posts-by-members/enhancement-for-fiori-finding-the-places-for-enhancement-getting-custom/ba-p/13552199)

![fyagubova](https://avatars.profile.sap.com/d/5/idd5a63ec075d53768574c6d6cfdcaf5c8a755029dd1fd9fde6f671de952a02f8d_small.jpeg "fyagubova")

[fyagubova](https://community.sap.com/t5/user/viewprofilepage/user-id/46311)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160420)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160420)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552199)

‎2022 Dec 19
10:14 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160420/tab/all-users "Click here to see who gave kudos to this post.")

4,996

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

*Please note that this post was first published at [https://medium.com/@yagubovafatima/enhancement-for-fiori-finding-the-places-for-enhancement-getting-...](https://medium.com/%40yagubovafatima/enhancement-for-fiori-finding-the-places-for-enhancement-getting-custom-error-message-4a6272fb7daa).*

I am working as a SAP ABAP Developer in a Consulting company and during the worktime we face different kind of problems especially in adding custom functionalties to SAP standards. In this blog, I am going to explain one these problems and its solution.

The problem: The customer wants to get an error message in Fiori if the document is once canceled you cannot cancel again the same document after reversing.

The purpose of this blog, finding points for enhancement and a solution for getting an error message in Fiori. (database: s4hana)

Launch Fiori from SAP GUI using **/N/UI2/FLP** t-code. Search for the application**Material Documents Overview** and click it. Then write the material document number and click to Go. We will see the screen below. In **Posting date** box write the earlier date and choose the item and finally click **OK**.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_K9OAptYH1iQx9Ap7-1.png)

1.

We will get the error message:

![](/legacyfs/online/storage/blog_attachments/2022/12/0_njmHsUIRDGU0Hl3W.png)

2.

Clarifying the problem: the customer wants in this page the error message with the text **‘You cannot cancel the document canceled before!’** before getting the error shown in the picture.

So, how to do it?

We understand that we have to enhance for getting custom error in Fiori application. And where to enhance and how to find the places for enhancement — these are our next questions.

Firstly, we have to find where all data is collected (selected). For finding it we have to know its **OData Service**. There are 2 ways:

1. <https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/> — go to the link, click:

All apps -> Search application name (in our example: Material Documents Overview) -> click the application name -> Implementation information -> Configuration — on this page, we can find OData Service name.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_uBtLhlIyEnae7dMg.png)

3.

2. In Fiori open the application, Press F12 (opening the inspection of the website). Open Network tab and try to reverse the document. And click OK for reversing the document. In Network tab find the row with the name ‘batch’. In this file, we’ll find OData service name.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_KSVeOpXOrElstqtf.png)

4.

Okay, we found the OData service name. The next step is explained below.

In SAP GUI, open t-code /n/iwfnd/maint\_service. Here we’ll see the services list. Click find icon and paste the web service name. Find and click on the web service name and right below click Service Implementation button.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_Ic4lbOdTvLcNmpk5.png)

5.

This screen will appear:

![](/legacyfs/online/storage/blog_attachments/2022/12/0_qc4W1cK6Ww_qz574.png)

6.

Then double-click on **Data Provider class** and it redirects us Class Builder page. On this page, we’ll see the methods of a class. Some of these methods are blue and some of them are black. If we set a breakpoint for each of them (of course external breakpoint) and launch the application to reverse the document we’ll see that the application redirects us to methods colored black. So, it means we can enhance into these methods. While debugging the methods we see the method with the name \*cancellation\*.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_7d0MwJqbu23ZJvEU.png)

7.

Double-click on the name of the method. And there we are! Here we’re going to enhance.

According to our experience with an error message in this method which has type ‘**E**’, this error message breaks the connection and directly closes the Fiori application. So that’s why we cannot write the error message in this method. But we have to keep in mind that we can only access this section of code when we run the application from Fiori. If we run migo it won’t be redirected to this section. So where do we have to write this error message then? For finding it we continue debugging.

There is an idea that we can write this error message where the Posting date error is written.

Run the migo -> Enter the document number -> Click to Item OK -> Check — we’ll get the same error message about the posting date that we’d got in Fiori application. Click the long text of the error message and copy message no.

Then return to the method for cancellation and set the external breakpoint. Open Fiori application and try to reverse it. It will redirect us to SAP GUI debug screen.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_NSiuxUbCZCscyboI.png)

8.

Set the breakpoint at the message. Enter the message details:

![](/legacyfs/online/storage/blog_attachments/2022/12/0_wy6ZKJ7Rh-gBwcA9.png)

9.

And we continue debugging.

![](/legacyfs/online/storage/blog_attachments/2022/12/0_-Y0Ae83YaOFIEhnJ.png)

10.

Here, we found that error message. It means we can implement the error message here (in this form). Take the program name, form name, and find it in se80.

![](/legacyfs/online/storage/blog_attachments/2022/12/...