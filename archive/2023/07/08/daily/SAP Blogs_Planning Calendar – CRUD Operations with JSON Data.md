---
title: Planning Calendar – CRUD Operations with JSON Data
url: https://blogs.sap.com/2023/07/07/planning-calendar-crud-operations-with-json-data/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:45.849310
---

# Planning Calendar – CRUD Operations with JSON Data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Planning Calendar – Custom Views and CRUD Operatio...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160689&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Planning Calendar – Custom Views and CRUD Operations with JSON Data](/t5/technology-blog-posts-by-members/planning-calendar-custom-views-and-crud-operations-with-json-data/ba-p/13554001)

![Sathish-KILARI](https://avatars.profile.sap.com/1/3/id13b73e0e708abe1ffd0f850420003e2eee0c9894e07aaa4fe7b8ccb0e09e0287_small.jpeg "Sathish-KILARI")

[Sathish-KILARI](https://community.sap.com/t5/user/viewprofilepage/user-id/646708)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160689)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160689)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554001)

‎2023 Jul 07
5:28 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160689/tab/all-users "Click here to see who gave kudos to this post.")

2,768

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (3)

Hi Readers,

Good Day.
> In this blog post I am going to explain How to Create custom views and Create, Read, Update and Delete appointments using Planning Calendar with JSON Data in BAS (Business Application Studio).

**Steps includes:**

1. Create a JSON Data

2. Create a Planning Calendar and bind the JSON Data to the Planning Calendar.

3. Adding a custom Views to the Planning Calendar.

4. Performing CRUD Operations in Planning Calendar.

**Introduction:**

You can use the Planning Calendar to represent a calendar containing multiple rows with appointments, where each row represents a different person.

You can configure different time-interval views so that the user can switch between hours, days, week, and month. The available navigation allows the user to select a specific interval using a picker or move to the previous/next interval using arrows.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-8.png)

**Use Case:**

We can use the Planning Calendar to schedule meetings with our team on hourly, daily, weekly and monthly basis.

**Technical Specification**:

The application developer should add dependency to sap.ui.unified library on application level to ensure that the library is loaded before the module dependencies will be required. The Planning Calendar uses parts of the sap.ui.unified library. This library will be loaded after the Planning Calendar.

Displays rows with appointments for different entities (such as persons or teams) for the selected time interval.

The Planning Calendar has the following structure from top to bottom:

* A toolbar where you can add your own buttons or other controls using the toolbar Content aggregation.

* A header containing a drop-down menu for selecting the [PlanningCalendarViews](https://sapui5.hana.ondemand.com/api/sap.m.PlanningCalendarView), and navigation for moving through the intervals using arrows or selecting a specific interval with a picker. Custom views can be configured using the views aggregation. If not configured, the following set of default built-in views is available - Hours, Days, 1 Week, 1 Month, and Months. Setting a custom view(s) replaces the built-in ones.

* The rows of the Planning Calendar that contain the assigned appointments. They can be configured with the rows aggregation, which is of type [PlanningCalendarRow](https://sapui5.hana.ondemand.com/api/sap.m.PlanningCalendarRow).

Let me demonstrate how I achieved in developing Planning Calendar and perform the CRUD operations with JSON data step by step.

The default view of the planning calendar will be look like as below, where showing drop down values/options - Hours, days, Months, 1Week and 1Month.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-5.png)

**Step 1: Create a JSON Data**

Now I have created a JSON Data in controller file as below.

```
 onInit: function () {

                var that = this;

                var oViewModel = new JSONModel({

                    "titleVal": "",

                    "shortDateVal": "",

                    "endDateVal": "",

                    "InfoVal": ""

                });

                that.getView().setModel(oViewModel, "createModel");

                var employeeImage = "https://png.pngtree.com/png-vector/20190710/ourmid/pngtree-user-vector-avatar-png-image_1541962.jpg";

                var oModel = new JSONModel();

                oModel.setData({

                    startDate: new Date("2023", "0", "15", "8", "0"),

                    people: [{

                        pic: employeeImage,

                        name: "Team Member 1",

                        role: "Team Leader",

                        info: "Daily Status",

                        appointments: [

                            {

                                start: new Date("2023", "0", "8", "08", "30"),

                                end: new Date("2023", "01", "8", "09", "30"),

                                title: "Team Meeting",

                                type: "Type03",

                                info: "Discussion about daily Task",

                                tentative: false

                            },

                            {

                                start: new Date("2023", "0", "11", "10", "0"),

                                end: new Date("2023", "0", "11", "12", "0"),

                                title: "Team Outing",

                                info: "room 1",

                                type: "Type01",

                                pic: "sap-icon://company-view",

                                tentative: false

                            },

                            {

                                start: new Date("2023", "1", "12", "11", "30"),

                                end: new Date("2023", "1", "12", "13", "30"),

                                title: "Lunch",

                                info: "Canteen",

                                type: "Type04",

                                tentative: true

                            },

                            {

                                start: new Date("2023", "4", "15", "11", "30"),

                                end: new Date("2023", "4", "15", "13", "30"...