---
title: SAP Fiori Elements: Breakout with sap.fe.macros
url: https://blogs.sap.com/2022/10/24/sap-fiori-elements-breakout-with-sap.fe.macros/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:46.893942
---

# SAP Fiori Elements: Breakout with sap.fe.macros

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori Elements: Breakout with sap.fe.macros

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/154026&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Elements: Breakout with sap.fe.macros](/t5/technology-blog-posts-by-sap/sap-fiori-elements-breakout-with-sap-fe-macros/ba-p/13539564)

![former_member10326](https://avatars.profile.sap.com/former_member_small.jpeg "former_member10326")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[former\_member10326](https://community.sap.com/t5/user/viewprofilepage/user-id/10326)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=154026)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/154026)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13539564)

‎2022 Oct 24
7:19 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/154026/tab/all-users "Click here to see who gave kudos to this post.")

8,151

* SAP Managed Tags
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (1)

ABAP RESTful Application Programming Model (RAP) based SAP Fiori Elements app, gives developer the opportunity to create UI5 apps with minimum (or most of the times with none) front-end code. This includes the benefits of out-of-the box UI5 application features (like value help, filter bar, object page etc.) and standard layout across other apps in FLP.

As a developer, this takes us away from the front end coding or more into back-end programming using CDS and annotations. However, there are rare occurrences when its required to implement features which could be as simple as a piece of cake in a custom UI5 app (true for a pro UI5 app developer) and could be a equally hard task via SAP Fiori Elements.

Then come to our rescue the **Flexible Programming Model** for SAP Fiori Elements app. There is a detailed help documentation available on possible Extension points, building blocks and controller extension with some executable examples and code snippets. This also documents some added features which can be used to enhance the app.

However, enhancing the app with breakouts comes with additional coding required to keep the custom part of the app in sync with the standard auto generated sections,mostly in terms of User Experience. Just for an example, to achieve same kind of value help features in the breakout code as compared to the SAP Fiori Elements generated standard value help, will require a heavy set of front-end code as well as high maintenance to keep up with the evolving features of the SAP Fiori Elements.

What if there was a way to create custom sections comprising all the SAP Fiori Elements delivered features. This can be made possible using [sap.fe.macros](https://sapui5.hana.ondemand.com/sdk/#/api/sap.fe.macros).

Using sap.fe.macros instead of custom UI5 element will help reuse the SAP Fiori Elements features. For e.g., if the entity property is linked to a value help(via CDS annotation), the UI will render the value help with no additional coding.

## Implementation

Say in the SAP Fiori Elements app there is a requirement to develop a custom fragment which contains some input fields.

These input fields can be directly associated to the field(property) of the OData entity using sap.fe.macros.Field instead of using **sap.m.input** custom control.

### UI Rendering

* Define the xml UI

  + the Fragment should look something like this

    ```
      <core:FragmentDefinition

            ......

            xmlns:macros="sap.fe.macros">

            ......

            <macros:Field

                    id="myMacroField"

                    metaPath="<nameOfTheEntityProperty>"

                    readOnly="false"

                    change="onChangeMyMacroField"

             </macros:Field>

      </core:FragmentDefinition>​
    ```

    where,

* + - **id**(string) : is the identifier of the Field control

    - **metaPath**(string) : is the relative path of the property in the metamodel, based on the current contextPath

    - **readOnly**(boolean) : allows us to control the read-only state of the field

    - **change** : an event containing details is triggered when the value of the field is changed

* In the controller, at fragment loading,

  + create a temporary context binding for the entity (same entity whose property was specified in the sap.fe.macros.Field property metadata)

    ```
    var oBinding = this.base.getExtensionAPI()

                                     .getModel()

                                     .bindList("/<ContextPathOfTheEntity>",

                                               null,

                                               [],

                                               [],

                                               {

                                                 $$updateGroupId: "noSubmit",

                                                 $$groupId: "noSubmit"

                                               }

                                              );​
    ```

    arguments for *bindList,*

    - **sPath**(string) : path pointing to the entity that should be bound

    - **oContext**([sap.ui.model.Context](https://ui5.sap.com/api/sap.ui.model.Context)) : context object for this databinding

    - **aSorters**([sap.ui.model.Sorter](https://ui5.sap.com/api/sap.ui.model.Sorter) | sap.ui.model.Sorter[ ]) : Initial sort order

    - **aFilters**([sap.ui.model.Filter](https://ui5.sap.com/api/sap.ui.model.Filter) | sap.ui.model.Filter[ ] ) : Predefined filter/s

    - **mParameters**(object) : additional batch call related parameters

* + Next, bind the above created binding to the macro element control

    ```
     oMacroElement.setBindingContext(oBinding.create({}));​
    ```

* That's it, the UI will render the sap.fe.macros.Field as an input list , or as a value list or as a checkbox field, as defined in the CDS entity

### Reading the value from UI

* The control for the sap.fe.macros.Field is bound to the the entity instance and from here the property can be read

  ```
  var oEntity = oMacroElement.getBindingContext().getObject();​
  ```

  In the above example the value can be read from *oEntity.<nameOfTheEntityProperty>*

### Error Handling

* To add a custom errors (for any front-end validations) , can be achieved using *addMessage* method of the sap.fe.macros control

  ```
   oCreateJobDefinitionAPJ.addMessage({

                                      description: "Some description",

                                      message: "Some Error",

                                      persistent: fal...