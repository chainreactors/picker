---
title: Abap2ui5 Project – Development of UI5 Selection Screens in pure ABAP (no app deployment or javascript needed)
url: https://blogs.sap.com/2023/01/22/abap2ui5-project-development-of-ui5-selection-screens-in-pure-abap-no-app-deployment-or-javascript-needed/
source: SAP Blogs
date: 2023-01-23
fetch_date: 2025-10-04T04:35:48.391547
---

# Abap2ui5 Project – Development of UI5 Selection Screens in pure ABAP (no app deployment or javascript needed)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* abap2UI5 - Development of UI5 Selection Screens in...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160574&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [abap2UI5 - Development of UI5 Selection Screens in Pure ABAP](/t5/technology-blog-posts-by-members/abap2ui5-development-of-ui5-selection-screens-in-pure-abap/ba-p/13553176)

![oblomov](https://avatars.profile.sap.com/9/7/id9724ed072fc9280b23442d4a0cc6c09ad8089500c097bb19af8ef03aa790ef85_small.jpeg "oblomov")

[oblomov](https://community.sap.com/t5/user/viewprofilepage/user-id/44240)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160574)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160574)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553176)

‎2023 Jan 22
10:25 AM

[61
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160574/tab/all-users "Click here to see who gave kudos to this post.")

18,279

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP R/3](https://community.sap.com/t5/c-khhcw49343/SAP%2520R%252F3/pd-p/01200245450800000002)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP R/3

  SAP R/3](/t5/c-khhcw49343/SAP%2BR%25252F3/pd-p/01200245450800000002)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (6)

|  |
| --- |
| **Update 23.02.2023** Thank you all for the great feedback and comments on this blog article. The approach is now extended, enabling the creation of views for a wide range of UI5 Controls. Check out the new blog post [here.](https://blogs.sap.com/2023/02/22/abap2ui5-development-of-ui5-apps-in-pure-abap-1-3/) |

### **Introduction**

In newer ABAP releases, SAP-GUI is no longer available. One feature that I miss a lot is the classic selection screen. With just a few lines of ABAP, an application with GUI and event handling was automatically generated. Unfortunately, if\_oo\_adt\_classrun cannot replace this functionality since it does not allow data transfer of inputs to the server, nor does it generate a browser-based app that can be used by end-users.

**So how can we adapt the Selection Screen approach to the new non-SAP-GUI and browser-based ABAP environment?**

As a solution, I have developed this open-source project called **[abap2UI5](https://github.com/abap2UI5/abap2ui5)**. With this project you can create standalone and ready-to-use UI5 applications in pure ABAP. No app deployment or JavaScript is needed. Data transfer and event handling in the backend is automatically integrated. It has the function scope of the former selection screen.

**Example:**
![](/legacyfs/online/storage/blog_attachments/2022/12/Bild-10.12.22-um-15.20-scaled.jpeg)

*UI5 App with Selection Screen Functionality Developed in Pure ABAP*

The entire functionality is based on a single HTTP handler. The frontend app is a generic one-page UI5 application, and the framework dynamically generates UI5-XML-Views and JSON-View-Models at runtime based on the ABAP implementation of the user.

Let's start with a basic example:

### **Getting Started & Example**

After installing the project with [**abapGit**](https://abapgit.org/) you will find the interface z2ui5\_if\_app in your system:

```
INTERFACE z2ui5_if_app PUBLIC.

  INTERFACES if_serializable_object.

  METHODS set_view
    IMPORTING
      view TYPE REF TO z2ui5_if_view.

  METHODS on_event
    IMPORTING
      client TYPE REF TO z2ui5_if_client.

ENDINTERFACE.
```

To develop a new abap2UI5 application, create a global ABAP class and implement the above interface. You can use the following code snippet as a template:

```
CLASS z2ui5_cl_app_demo_01 DEFINITION PUBLIC.

  PUBLIC SECTION.

    INTERFACES z2ui5_if_app.

    DATA product TYPE string.
    DATA quantity TYPE string.
    DATA check_initialized TYPE abap_bool.

ENDCLASS.

CLASS z2ui5_cl_app_demo_01 IMPLEMENTATION.

  METHOD z2ui5_if_app~on_event.

    "set initial values
    IF check_initialized = abap_false.
      check_initialized = abap_true.
      product = 'tomato'.
      quantity = '500'.
    ENDIF.

    "user event handling
    CASE client->event( )->get_id( ).
      WHEN 'BUTTON_POST'.
        "do something
        client->popup( )->message_toast( |{ product } { quantity } ST - GR successful| ).

    ENDCASE.
  ENDMETHOD.

  METHOD z2ui5_if_app~set_view.

    "define selection screen
    view->factory_selscreen_page( title = 'My ABAP Application - Z2UI5_CL_APP_DEMO_01'
        )->begin_of_block( 'Selection Screen Title'
            )->begin_of_group( 'Stock Information'
                )->label( 'Product'
                )->input( product
                )->label( 'Quantity'
                )->input( quantity
                )->button( text = 'Post Goods Receipt' on_press_id = 'BUTTON_POST' ).

  ENDMETHOD.
ENDCLASS.
```

There is nothing else left to do and your application is already ready to start now.

Simply call the HTTP interface z2ui5\_http\_cloud of the project in your browser. You can find the URL for this interface in the project's package:![](/legacyfs/online/storage/blog_attachments/2022/12/Bild-17.12.22-um-15.19-scaled.jpeg)

*HTTP Endpoint of abap2UI5*

Replace the 'app' parameter in the URL with the name of your new ABAP class. The updated URL looks like this:
<your\_system>:<port>/sap/bc/http/sap/z2ui5\_http\_cloud?app=<your\_abap\_class\_name>
Next call it in your browser and your new app will be displayed:![](/legacyfs/online/storage/blog_attachments/2022/12/Bildschirm­foto-2022-12-10-um-15.39.43.png)

*UI5 App sent from the Backend*

This is just a small example, but it can be seen as a starting point. Feel free to modify the view and add your own custom logic to the controller as needed.

### **Data Transfer & Event Handling**

We will now change the values on the frontend to "potato" and a quantity of 200:![](/legacyfs/online/storage/blog_attachments/2022/12/Bildschirm­foto-2022-12-10-um-15.43.29.png)

*Changing Values at the Frontend*

Then we set a breakpoint in Eclipse and take a look at the backend system:
![](...