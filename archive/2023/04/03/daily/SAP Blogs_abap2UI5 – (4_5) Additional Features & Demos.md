---
title: abap2UI5 – (4/5) Additional Features & Demos
url: https://blogs.sap.com/2023/04/02/abap2ui5-4-5-additional-features-demos/
source: SAP Blogs
date: 2023-04-03
fetch_date: 2025-10-04T11:30:12.587963
---

# abap2UI5 – (4/5) Additional Features & Demos

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* abap2UI5 - (4) Advanced Functionality & Demonstrat...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161881&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [abap2UI5 - (4) Advanced Functionality & Demonstrations](/t5/technology-blog-posts-by-members/abap2ui5-4-advanced-functionality-demonstrations/ba-p/13560294)

![oblomov](https://avatars.profile.sap.com/9/7/id9724ed072fc9280b23442d4a0cc6c09ad8089500c097bb19af8ef03aa790ef85_small.jpeg "oblomov")

[oblomov](https://community.sap.com/t5/user/viewprofilepage/user-id/44240)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161881)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161881)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560294)

‎2023 Apr 02
3:43 PM

[26
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161881/tab/all-users "Click here to see who gave kudos to this post.")

6,252

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP R/3](https://community.sap.com/t5/c-khhcw49343/SAP%2520R%252F3/pd-p/01200245450800000002)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP R/3

  SAP R/3](/t5/c-khhcw49343/SAP%2BR%25252F3/pd-p/01200245450800000002)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)

View products (6)

Welcome to part 4 of this blog series introducing **[abap2UI5](https://github.com/abap2UI5/abap2UI5)** — an open-source project for developing UI5 apps purely in ABAP.

**In this post, we will explore various demos, including File Editor, Table Maintenance, and Charts, among others. These demos aim to showcase the diverse use cases and features of abap2UI5.**

**Blog Series & More**

You can find all the information about this project on **[GitHub,](https://github.com/abap2UI5/abap2UI5)** stay up-to-date by following on **[Twitter](https://twitter.com/abap2UI5)** and be sure to explore the other articles of this blog series:

|
 **[(1) Introduction: Developing UI5 Apps Purely in ABAP](https://blogs.sap.com/2023/02/22/abap2ui5-development-of-ui5-apps-in-pure-abap-1-3/)** |

|
 **[(2) Displaying Selection Screens & Tables](https://blogs.sap.com/2023/02/22/abap2ui5-output-of-lists-and-tables-toolbar-and-editable-2-3/)** |

|
 **[(3) Popups, F4-Help, Messages & Controller Logic](https://blogs.sap.com/2023/03/30/abap2ui5-3-4-flow-logic-pop-ups-f4-help/)** |

|
 (4) Advanced Functionality & Demonstrations (this blog post) |

|
 **[(5) Creating UIs with XML Views, HTML, CSS & JavaScript](https://blogs.sap.com/2023/04/12/abap2ui5-5-6-extensions-with-xml-views-html-js-custom-controls/)** |

|
 **[(6) Installation, Configuration &](https://blogs.sap.com/2023/04/14/abap2ui5-6-7-installation-configuration-debugging/) [Troubleshooting](https://blogs.sap.com/2023/04/14/abap2ui5-6-7-installation-configuration-debugging/)** |

|
 [**(7) Technical Background: Under the Hood of abap2UI5**](https://blogs.sap.com/2023/04/26/abap2ui5-7-7-technical-background-under-the-hood-of-abap2ui5/) |

|
 [**(8) Repository Organization: Working with abapGit, abaplint & open-abap**](https://blogs.sap.com/2023/08/21/abap2ui5-a1-repository-setup-with-abapgit-abaplint-open-abap/) |

|
 **[(9) Update I: Community Feedback & New Features - Sep. 2023](https://blogs.sap.com/2023/09/11/abap2ui5-a2-community-feedback-new-features/)** |

|
 **[(10) Extensions I: Exploring External Libraries & Native Device Capabilities](https://blogs.sap.com/2023/12/04/abap2ui5-a3-extensions-i-exploring-external-libraries-native-device-capabilities/)** |

|
 **[(11) Extensions II: Guideline for Developing New Features in JavaScript](https://blogs.sap.com/2023/12/11/abap2ui5-a4-extensions-ii-guideline-for-developing-new-features-in-javascript/)** |

|
 **[(12) Update II: Community Feedback, New Features & Outlook - Jan. 2024](https://blogs.sap.com/2024/01/08/abap2ui5-12-update-ii-community-feedback-new-features-outlook-january-2024/)** |

**Content**

While we've already explored classic scenarios like selection screens and table outputs, the **[UI5 Library](https://sapui5.hana.ondemand.com/sdk/#/topic)** also enables the development of abap2UI5 applications for a broad range of additional use cases. This post covers the following areas:

1. File Editor

2. Table Maintenance

3. File Upload & Download

4. Visualization with Charts

5. Monitoring & Timer

6. Layouts

7. Side Effects

8. List Report

9. Conclusion

Let's begin with the file editor.

### **1. Demo - File Editor**

The File Editor uses the **[Code Editor Control](https://sapui5.hana.ondemand.com/sdk/#/entity/sap.ui.codeeditor.CodeEditor).** It displays text files and highlights the syntax for a lot of different code types (xml, json, js, abap, yaml...). This functionality is part of UI5 and works seamlessly, requiring no extra effort. We simply need to fill in the attributes of the editor control in the rendering method. For the editor content, we use two-way binding to retrieve the updated frontend values and we call function modules to read and update the MIME repository. Here's a preview of the demo app in action:

![](/legacyfs/online/storage/blog_attachments/2023/03/gif_mime-2.gif)

Demo File Editor

Check out the source code **[here.](https://github.com/abap2UI5/abap2UI5-tools/blob/main/src/z2ui5_cl_tool_app_01.clas.abap)**

The **[UI5 Library](https://sapui5.hana.ondemand.com/sdk/#/topic)** provides information about all controls, including their attributes and possible values:![](/legacyfs/online/storage/blog_attachments/2023/04/Bildschirm­foto-2023-04-01-um-11.06.07.png)

Available Code Types for Syntax Highlighting of the Editor Control

### **2. Demo - Table Maintenance**

Combining the [**Editor Control**](https://sapui5.hana.ondemand.com/sdk/#/entity/sap.ui.codeeditor.CodeEditor) with an editable [**Table Control,**](https://sapui5.hana.ondemand.com/sdk/#/entity/sap.m.Table) as explained in the second blog post, enables us to create an abap2UI5 table maintenance app. This app provides three input formats (XML, JSON, CSV) and converts the data into a...