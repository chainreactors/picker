---
title: When Do Situations Occur and How to Handle and Automate it.
url: https://blogs.sap.com/2023/06/25/when-do-situations-occur-and-how-to-handle-and-automate-it./
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:19.035170
---

# When Do Situations Occur and How to Handle and Automate it.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* When Do Situations Occur and How to Handle and Aut...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52095&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [When Do Situations Occur and How to Handle and Automate it.](/t5/enterprise-resource-planning-blog-posts-by-sap/when-do-situations-occur-and-how-to-handle-and-automate-it/ba-p/13562116)

![former_member828158](https://avatars.profile.sap.com/former_member_small.jpeg "former_member828158")

[former\_member828158](https://community.sap.com/t5/user/viewprofilepage/user-id/828158)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52095)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52095)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562116)

‎2023 Jun 25
11:37 AM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52095/tab/all-users "Click here to see who gave kudos to this post.")

2,188

* SAP Managed Tags
* [Situation Handling](https://community.sap.com/t5/c-khhcw49343/Situation%2520Handling/pd-p/db4786c7-74ce-4e4a-91f2-027a57fa3921)

* [Situation Handling

  Additional Software Product](/t5/c-khhcw49343/Situation%2BHandling/pd-p/db4786c7-74ce-4e4a-91f2-027a57fa3921)

View products (1)

Situation Handling is SAP S/4HANA functionality provided to bring certain settings (situations) to the attention of a relevant group of business users. This allows for proactive notification to the needed users for a situation that has occurred. Situations may be seen as problems or chances.

Business users are given the notification of a situation, together with the notification status (Open, Resolved, Obsolete, Invalid), contextual information relating to the object pertaining to the situation and lastly, any actions deemed necessary to address the situation. Situation Handling conveys the crucial and appropriate information to the attention of the business users.

![](/legacyfs/online/storage/blog_attachments/2023/06/Image1-5.png)

Figure 1: Process Flow of the Situation Scenario

With SAP S/4HANA Cloud 2202 you can create your own situation use cases with the extended framework for Situation Handling.  The extended framework offers three new configuration apps: The extended framework also contains an enhanced end-user app, My Situation- Extended, and the Situation Handing Demo app. You use the demo app to manage the flights of a fictional booking portal and to trigger situations based on pre-delivered configuration samples.

**Manage Situation Object:**

In this application, we can model business objects that enable Situation Handling. A situation object connects existing application artefacts such as CDS views, events, and actions that form the foundation to set up situation use cases. Model business objects that enable Situation Handling, including the events that trigger a situation.

**Manage Situation Scenario:**

In this app, you can model your own situation scenarios for extended object-based situations. That is, situations that occur for a specific business object, such as a contract. A situation scenario is the technical description of a business scenario and provides the foundation for defining multiple use cases in the form of situation templates, which serve as blueprints for situation types. The business object affected by a situation is defined as the anchor object. In the app, you define the anchor object and add all objects that could trigger situations for the anchor object. For the trigger objects, you define the trigger events and the actions that help the users resolve the situations. And you define which information is displayed in the My Situation - Extended app to the users responsible for solving situations based on this scenario.

**Manage Situation Extended:**

In this application, you can create situation templates as blueprints for business cases. It can also create situation types for productive use. You could manage instances here and collect the message-based situation which is supposed to be triggered.

**Situation Handling Demo:**

This app contains test data you can use to explore the extended framework of Situation Handling. This is a simplified version of a booking portal focusing on actions for flights and bookings. After defining and enabling a situation type, you can use the app's actions to trigger situations.

**My Situations – Extended:**

With this app, you can display all situations in your area of responsibility, based on the extended framework of Situation Handling. From the overview table, you can go to the situation page where context information and related actions help you solve the situation.

In this blog, you will learn how to use the extended framework for Situation Handling based on demo cases. Business Scenario for the Demo Case of a Fictional Flight Booking Scenario. As in any business, trust, reliability, and a smooth process is to be looked upon. The sales and profit of the flights are considered. Other issues like Cancellation, Overbooking, rebooking, missing, or flight delays must be captured thoroughly. To get a better grip on the processes the right user groups should get informed if such issues are likely to happen. These heads-ups allow us to react to the situations in time and decrease negative effects to a minimum.

The Situation Handling app supports these cases. You can manipulate the flight data, for instance by assigning a smaller plane to overbook the economy class.

![](/legacyfs/online/storage/blog_attachments/2023/06/Image2-5.png)

Figure 2: Flight details showcased by Situation Handling Application

The end user gets a notification on the SAP Fiori launchpad.

![](/legacyfs/online/storage/blog_attachments/2023/06/MicrosoftTeams-image-159-1.png)

Figure 3: Notification Preview

The situation is also displayed in the list view of the My situation-extended app. The details about the situations are shown on the situation page in the My situation-extended app. Situation Configuration with Templates, Scenarios, and Objects. The extended framework for Situation Handling introduces the new concepts situation scenario and situation object in addition to the existing situation template. This three-layer approach lets you configure your own situations in a generic yet controlled way. As you know from the standard framework of Situation Handling, situation templates are used as blueprints for use cases. The pain points identified in the fictional booking portal translate well into templates which are configured in the Manage Situation -Extended app. For the overbooking case, the values of seat occupancy and flight date are of interest. Situations can be detected by a regular check of the flight data or by events such as new bookings, cancelled bookings, or upgrades. Taking the details of the templates into account, we can see a similar pattern. All templates refer to a flight. The flight data can be observed with a batch job. Alternatively, situations can be triggered by a flight event or a booking e...