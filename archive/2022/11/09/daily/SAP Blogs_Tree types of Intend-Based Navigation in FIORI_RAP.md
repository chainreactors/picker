---
title: Tree types of Intend-Based Navigation in FIORI/RAP
url: https://blogs.sap.com/2022/11/08/tree-types-of-intend-based-navigation-in-fiori-rap/
source: SAP Blogs
date: 2022-11-09
fetch_date: 2025-10-03T22:05:23.399881
---

# Tree types of Intend-Based Navigation in FIORI/RAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Three types of Intent-Based Navigation in FIORI/RA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/152357&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Three types of Intent-Based Navigation in FIORI/RAP](/t5/technology-blog-posts-by-members/three-types-of-intent-based-navigation-in-fiori-rap/ba-p/13502715)

![Mikhail_Minakov](https://avatars.profile.sap.com/8/e/id8eab92b1b71c7bce380d0a8a8ab879a2729a155e5a77ece27d2e154c7ea6ac63_small.jpeg "Mikhail_Minakov")

[Mikhail\_Minakov](https://community.sap.com/t5/user/viewprofilepage/user-id/163112)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=152357)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/152357)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13502715)

‎2022 Nov 08
8:18 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/152357/tab/all-users "Click here to see who gave kudos to this post.")

27,396

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (4)

During my daily work I've got a task to implement a call of another Fiori App from my Fiori Elements App. In order to achieve that I have found three possible ways to implement it (but only one of them was working for me):

1. Intent-based Navigation as RAP CDS Association

2. Intent-based Navigation as ABAP Call from RAP Action

3. Intent-based Navigation as Fiori Extension

Let's discuss all of them in details ![:slightly_smiling_face:](/html/@CB193FD929C1B3F628B5259D5B23C3AB/emoticons/1f642.png ":slightly_smiling_face:")

### 1. Intent-Based Navigation as RAP CDS Association

According to documentation [https://help.sap.com/docs/BTP/923180ddb98240829d935862025004d6/25f37dc4567f4287b9bfbdd0040270f1.html...](https://help.sap.com/docs/BTP/923180ddb98240829d935862025004d6/25f37dc4567f4287b9bfbdd0040270f1.html?locale=en-US)

you can use @UI.lineItem annotation with type #FOR\_INTENT\_BASED\_NAVIGATION to configure intent-based Navigation to another Fiori App. I have used the following configuration in Metadata Extension view of my RAP Model:

```
  @UI: { lineItem: [ { position: 100 }

      , { type: #FOR_INTENT_BASED_NAVIGATION, label: 'Send request', semanticObject: 'my_semantic_object', semanticObjectAction: 'create', requiresContext: true }

      ]

      , identification: [ { position: 100 }

      , { type: #FOR_INTENT_BASED_NAVIGATION, label: 'Send request', semanticObject: 'my_semantic_object', semanticObjectAction: 'create'}

      ]

      , selectionField: [ { position: 40 }

      ]

     }

  status;
```

The button will be shown only on the List Report Page in spite of the fact, that I have configured it in identification section as well.

**Note**, that you can see the button only after deploying application to Fiori Launchpad, you cannot see the button in Eclipse or BAS Preview. This type of navigation will only work for Fiori Apps and not for SAP GUI for HTML even if you call this from Fiori Launchpad as target mapping.

### 2. Intent-Based Navigation as ABAP Call

You can use the class to trigger intent-based navigation to Fiori App from ABAP code like that:

```
     cl_lsapi_manager=>navigate_to_intent(

          object = 'your_semantic_object'

          action = 'your_action'

          parameters = lt_parameters

          navigation_mode = if_lsapi=>gc_s_navigation_mode-new_external_window ).
```

This is working nicely but only from the backend side. So you cannot use this code as behaviour implementation of custom action in RAP, it will not work.

More information here <https://blogs.sap.com/2016/05/13/cllsapimanager-environment-independent-navigation/>

### 3. Intent-Based Navigation as Fiori Extension

According to the documentation [https://help.sap.com/docs/SAP\_NETWEAVER\_AS\_ABAP\_752/a7b390faab1140c087b8926571e942b7/3a35ab684174415...](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/a7b390faab1140c087b8926571e942b7/3a35ab684174415899c98da4931bd6c1.html?locale=en-US&version=7.52.5)

The CrossApplicationNavigation service is used here to call an semantic object action.

I have generated the fiory elements extension using "Guided Development" function in BAS.

![](/legacyfs/online/storage/blog_attachments/2022/10/1-93.png)

Choosing "Add a custom action using extensions"

![](/legacyfs/online/storage/blog_attachments/2022/10/2-49.png)

After executing this wizard the manifest.json file will be updated with a new action snippet where you can setup the button label

```
                            "content": {

                                "header": {

                                    "actions": {

                                        "a_op_btnSendRequest": {

                                            "id": "a_op_btnSendRequestButton",

                                            "text": "CS-Auftrag Versenden",

                                            "press": "csorder.csorder.custom.ObjectPageExtController.f_op_SendRequest",

                                            "requiresSelection": false

                                        }

                                    }

                                }

                            }
```

and new ObjectPageExtController.js file will be created in webapps/custom section.

ObjectPageExtController.js contains a empty function where you have to implement your code for intent-based navigation.

![](/legacyfs/online/storage/blog_attachments/2022/10/3-41.png)

The implementation may look like following:

```
sap.ui.define([],

function (){

    "use strict";

    return {

        f_op_SendRequest: function(oEvent) {

            var oCrossAppNav = sap.ushell.Container.getService("CrossApplicationNavigation");

            // trigger navigation

            oCrossAppNav.toExternal({

                target : { semanticObject : "Name of your semantic object", action : "Your action" },

                params : { your_parameter : [ your_value ] }

            });

        }

    };

});
```

After this you will see the new button in Object Page, clicking on it wil...