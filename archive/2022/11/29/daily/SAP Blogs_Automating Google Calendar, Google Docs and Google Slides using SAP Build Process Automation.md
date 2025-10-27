---
title: Automating Google Calendar, Google Docs and Google Slides using SAP Build Process Automation
url: https://blogs.sap.com/2022/11/28/automating-google-calendar-google-docs-and-google-slides-using-sap-build-process-automation/
source: SAP Blogs
date: 2022-11-29
fetch_date: 2025-10-03T23:58:53.796217
---

# Automating Google Calendar, Google Docs and Google Slides using SAP Build Process Automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Automating Google Calendar, Google Docs and Google...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160138&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automating Google Calendar, Google Docs and Google Slides using SAP Build Process Automation](/t5/technology-blog-posts-by-sap/automating-google-calendar-google-docs-and-google-slides-using-sap-build/ba-p/13556743)

![former_member829026](https://avatars.profile.sap.com/former_member_small.jpeg "former_member829026")

[former\_member829026](https://community.sap.com/t5/user/viewprofilepage/user-id/829026)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160138)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160138)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556743)

‎2022 Nov 28
7:17 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160138/tab/all-users "Click here to see who gave kudos to this post.")

1,348

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (2)

SAP Build Process Automation provides Google Workspace SDK which can be used to automate Google Workspace products like Gmail, Sheets, Drive, Calendar, Docs and Slides. The activities provided by the SDK are grouped into different modules each for automating a Google Workspace product.

In this blog post I would like to introduce modules to automate Google Calendar, Google docs and Google Slides. This blog will be helpful for those who use Google Workspace products as office suite and are looking to automate it. The activities to automate these are available in Google Workspace SDK and requires an authorization with the help of activities in Google Authorization SDK. For more information on authorization required for Google Workspace SDK, please refer [Authorizing SAP Build Process Automation to automate Google Applications](https://blogs.sap.com/2022/11/14/authorizing-sap-process-automation-to-automate-google-applications/)

Once authorized then Google workspace SDK lets you to automate Google Workspace products. On the SAP Build Process Automation side, we need to create an automation and add the Google Authorization SDK and Google Workspace SDK along with Core SDK.

    ![](/legacyfs/online/storage/blog_attachments/2022/11/CaptureBlog.jpg)

**Google Calendar:**

Managing meetings can be automated using Google Calendar activities.

Activities like Fetch Busy Information or List Events  can be used to check calendar details and when participants of a meeting would be available between certain time intervals. Let’s look at the Fetch Busy Information activity and  its parameters,

***Fetch Busy Information :*** This activity gets meeting schedules information of a user.

*Input Parameters:*

***calendarBusyInfoParameters*** *Data type to define the identifier of the calendar and the interval when a specific user is busy. Which accepts from and to time, values as shown below*

***from****: 2022-08-21T10:00:00+05:30*

***to****: 2022-08-21T10:00:00+05:30*

***CalendarIds*** *: Semilcolon separated google calendarIds e.g.* *xyzcal@googleworkspace.com*

*Output Parameters:*

***calendarBusyInfo*** *Busy Info for the specified Calendar*

*It contains* ***calendarId*** *and* ***busyInfo*** *i.e Start and End time of the event*

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture2b.png)

calendarsbusyInfo[0].busyInfo.length === 0 would indicate that user with calendarId *xyzcal@googleworkspace.com* is free and meeting request can be sent.

Once you want to send the meeting request, there is a **Create Event** activity to help you create the meeting request. It is possible update or delete events using Update Event and Delete Event activities.

To Get an event details like evenetType, description or location etc., we can use Get Event Activity

***Get Event***

*Input parameters:*

***eventId****: Unique Identifier for the event*

***calendarId:*** *Unique Identifier for the calendar. If you want to access the primary calendar then use the keyword primary*

*Output parameters:*

***event:*** *Google Event*

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture3b.png)

Note:  Calendar activities need <https://www.googleapis.com/auth/calendar> scope. This has to be provided in the authorization activity.

**Google Docs:**

You may need to create a document and would like to do an update to it. SDK has activities to help automate creation of document and update it.

Create Doc activity will create a document in “my drive”. This activity takes an optional parameter for title of document. If not specified untitled document would be created.

***Create Document:*** This activity creates a new document

*Input Parameters:*

***Title****: Name of the new document*

*Output Parameters:*

***createdDocument*** *New Google Document created in my drive.*

***documentId****: Unique Identifier for the document.*

***title****: Title of the document, it is name given to the document.*

***revisionId****: revisionId of the document, each time google document is updated it returns the revisionId.*

     ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture4b.png)

Google Documents can be updated with other activities using the document Id. If you need to fetch document Id for an existing document, we can get that by opening the document in the browser, url will have the document Id.

Content in the document can be updated using Insert Text activity. Currently there is no support for styles in Google docs automation activities and this has to be done manually. Let’s look at the Replace Text activity from Google Docs module

***Replace Text:*** Replaces the matching texts in a Google Document with new value

*Input parameters:*

***documentId****: Unique Identifier for the document*

***textToBeReplaced:*** *Text which should be replaced*

***replaceText****: Text to replace*

***matchCase:*** *Whether the search of text is case-sensitive*

*Output parameters:*

***ocuurencesChanged:*** *Number of occurrences changed for the specified text*

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture5b.png)

Note: Docs activities need <https://www.googleapis.com/auth/drive> scope. This has to be provided in the authorization activity.

**Google Slides:**

It is possible to automate Google Slides using Google Workspace SDK. You can create a new presentation using Create Presentation activity. This activity takes an optional p...