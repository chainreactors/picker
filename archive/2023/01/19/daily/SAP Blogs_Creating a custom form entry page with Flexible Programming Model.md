---
title: Creating a custom form entry page with Flexible Programming Model
url: https://blogs.sap.com/2023/01/18/creating-a-custom-form-entry-page-with-flexible-programming-model/
source: SAP Blogs
date: 2023-01-19
fetch_date: 2025-10-04T04:16:42.607545
---

# Creating a custom form entry page with Flexible Programming Model

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creating a custom form entry page with Flexible Pr...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163326&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating a custom form entry page with Flexible Programming Model](/t5/technology-blog-posts-by-members/creating-a-custom-form-entry-page-with-flexible-programming-model/ba-p/13568879)

![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[MioYasutake](https://community.sap.com/t5/user/viewprofilepage/user-id/789)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163326)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163326)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568879)

‎2023 Jan 18
8:49 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163326/tab/all-users "Click here to see who gave kudos to this post.")

14,169

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

## Introduction

Flexible Programming Model enables you to extend Fiori elements applications based on OData V4, as well as create freestyle applications from scratch using [building blocks](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/buildingBlocks/buildingBlockOverview). An overview of Flexible Programming Model and what it provides is explained in the following blog post.
[Leverage the flexible programming model to extend your SAP Fiori elements apps for OData V4](https://blogs.sap.com/2021/08/19/leverage-the-flexible-programming-model-to-extend-your-sap-fiori-elements-apps-for-odata-v4/)

In this article, I am going to create a freestyle (custom page) application with create function. In  Business Application Studio there is  "**Form Entry Object Page**" template. This creates an application that directly opens an Object Page where you can create a new record. What I am going to do is to achieve a similar functionality with a freestyle application using **"Custom Page"** template.

The source code is available on GitHub in the [blog-custom-form](https://github.com/miyasuta/flex-orders/tree/blog-custom-form) branch.

![](/legacyfs/online/storage/blog_attachments/2023/01/templates2.png)

Templates

## Form entry object page

Before we start off, let's see how "Form Entry Object Page" looks like.

* When you start the application, an object page opens.![](/legacyfs/online/storage/blog_attachments/2023/01/object-page-1.png)

* When you press "Create", the screen turns to display mode and a message toast is shown.![](/legacyfs/online/storage/blog_attachments/2023/01/object-page-created.png)

* When you press "Discard Draft", draft data is discarded and the screen turns to display mode.

  ![](/legacyfs/online/storage/blog_attachments/2023/01/object-page-discard.png)

##

## Create a custom form entry page

### Prerequisites

To create an Fiori application using Flexible Programming Model, your OData service must fulfill the following requirements.

* OData V4

* Draft enabled (in case of create & edit scenarios)

### Steps

1. Create an app with "Custom Page" template

2. Create a form page

The base CAP project is on [GitHub](https://github.com/miyasuta/flex-orders).

## 1. Create an app with "Custom Page" template

### 1.1. Generate an app

Select "Custom Page" from the templates.

![](/legacyfs/online/storage/blog_attachments/2023/01/custom-page.png)

Template selection

Select local CAP project as a data source.

![](/legacyfs/online/storage/blog_attachments/2023/01/data-source.png)

Data source selection

An app with the following structure will be generated. Note that the main view and controller files are located in the "ext/main" folder.

![](/legacyfs/online/storage/blog_attachments/2023/01/app-structure-1.png)

Project structure

### 1.2. Trigger the creation of an entity

Add the following code to Main.contrller.js to trigger the creation of an entity.

```
sap.ui.define(

    [

        'sap/fe/core/PageController'

    ],

    function(PageController) {

        'use strict';

        return PageController.extend('flex.customformentry.ext.main.Main', {

            onInit: function() {

                PageController.prototype.onInit.apply(this);

                const router = this.getAppComponent().getRouter();

                router.getRoute("OrdersMain").attachPatternMatched(this._onObjectMatched, this);

            },

            _onObjectMatched: function() {

                if(this._createDone) {

                    if (sap.ushell && sap.ushell.Container && sap.ushell.Container.getService) {

                        var oCrossAppNav = sap.ushell.Container.getService("CrossApplicationNavigation");

                        oCrossAppNav.toExternal({

                            target: {

                                shellHash: "#"

                            }

                        });

                    }

                } else {

                    this._createDone = true;

                    const listBinding = this.getAppComponent().getModel().bindList("/Orders");

                    this.editFlow.createDocument(listBinding, {

                        creationMode: "NewPage"

                    });

                }

            }

        });

    }

);
```

[EditFlow](https://sapui5.hana.ondemand.com/#/api/sap.fe.core.controllerextensions.EditFlow%23methods/Summary) provides several methods to interact with a document. Inside a controller, you can access those methods simply by `this.editflow.<functionName>`.

[createDocument](https://sapui5.hana.ondemand.com/#/api/sap.fe.core.controllerextensions.EditFlow%23methods/createDocument) is used here to create a new entity. The parameter "creationMode" accepts one of the following values.

* NewPage: the created document is shown in a new page

* Inline: the creation is done inline in a table

* External: the creation is done in a different application specified via the parameter 'outbound'

In the case of "NewPage", the URL pattern changes to `/<EntityName>(<key>)` so a route matching this pattern has to exist (we will be creating this route in the next step).

**Important:**

* When you implement "onInit" method,...