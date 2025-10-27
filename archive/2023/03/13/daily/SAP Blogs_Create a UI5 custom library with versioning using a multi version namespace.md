---
title: Create a UI5 custom library with versioning using a multi version namespace
url: https://blogs.sap.com/2023/03/12/create-a-ui5-custom-library-with-versioning-using-a-multi-version-namespace/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:09.714138
---

# Create a UI5 custom library with versioning using a multi version namespace

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Create a UI5 custom library with versioning using ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163033&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create a UI5 custom library with versioning using a multi version namespace](/t5/technology-blog-posts-by-members/create-a-ui5-custom-library-with-versioning-using-a-multi-version-namespace/ba-p/13567207)

![Marian_Zeis](https://avatars.profile.sap.com/e/7/ide74053729274e7e2ae557b9a21e023fbf6239bb72f86c971922f90bdca9bebc1_small.jpeg "Marian_Zeis")

[Marian\_Zeis](https://community.sap.com/t5/user/viewprofilepage/user-id/61)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163033)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163033)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567207)

‎2023 Mar 12
5:17 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163033/tab/all-users "Click here to see who gave kudos to this post.")

6,249

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

### More from the Series related to the UI5 Spreadsheet Upload Control

|
 [Simplifying Excel Upload in Fiori Elements: The Open Source and Easy-to-Use UI5 Custom Control](https://blogs.sap.com/2023/02/17/simplifying-excel-upload-in-fiori-elements-the-open-source-and-easy-to-use-ui5-custom-control/) |

|
 [Create a UI5 custom library with versioning using a multi version namespace](https://blogs.sap.com/2023/03/12/create-a-ui5-custom-library-with-versioning-using-a-multi-version-namespace/) |

|
 [How test multiple scenarios and UI5 Versions with wdi5 and GitHub Actions](https://blogs.sap.com/2023/04/05/automating-ui5-testing-with-github-actions-and-wdi5-in-multiple-scenarios/) |

|
 [Load Data from a Excel File in UI5 and display the data in a Table with this Open Source Component](https://blogs.sap.com/2023/04/13/load-data-from-a-excel-file-in-ui5-and-display-the-data-in-a-table-with-this-open-source-component/) |

## Motivation

For a good structuring in a development project it is a smart idea to encapsulate different components and make them available for reuse.
In the area of UI5 there is the option of a [library](https://help.sap.com/docs/SAP_Web_IDE/825270ffffe74d9f988a0f0066ad59f0/ec4fda32e66f49d880a8fc6ad54a993c.html?locale=en-US) or a [reuse component](https://sapui5.hana.ondemand.com/sdk/#/topic/6314fcd2510648fbaad3cee8a421030d.html).

A good overview of the options [is a 2018 article](https://www.nabisoft.com/tutorials/sapui5/implementing-re-use-components-in-sapui5-libraries-and-consuming-them-in-sapui5-apps) by Nabi that still discusses current issues:

These components can then be used by many apps without having to develop them over and over again.
**The big disadvantage is that changes to these components can have a significant impact on many apps.**

The problem is that the component is supposed to improve and speed up the work.
Instead, this causes that the components are no longer touched because the risk of breaking something is too great or the test effort is too extensive.

## Idea

The major problem is that only the version that is available on the system must be used. It is not possible to use different versions of a reuse component on the same system.
It works differently e.g. in the NPM JavaScript Ecosystem, where changes create a new version number which can then be used explicitly by an application.
Wouldn't it be great if we could use this system for libraries and reuse components?

## Concept

A component is organized in a unique namespace, the namespace of the component equals the component name.
We could use this to include the version of a component in the namespace, since a specific component is always called with the namespace in the manifest.
For versioning for the widely used [semantic versioning](https://semver.org/lang/de/) can be used

So instead of looking like this "ui.component.orderhandling" , **the namespace of a component could look like this "ui.component.orderhandling.v1\_2\_4"**.

This namespace variant is just a suggestion I use and since there is no universal solution for it yet, the versioning can be customized as it suits you better.
The version can also be separated with dots and look like this:
**"ui.component.orderhandling.v1.2.4".**However, since this suggests a partitioning, it is recommended to use underscores.

Also the versioning with major minor and patch can be adapted for the own use case and e.g. patch can be omitted completely.
Without patch e.g. a version "ui.component.orderhandling.v1\_2" can be overwritten with a fix without having to adapt the app manifest.
But this must be decided differently for each use case.

## Proof of concept

My current UI5 open source project is the [reuse component UI5 Spreadsheet Upload](https://docs.spreadsheet-importer.com/).
Here I wanted to implement the idea of a multi version namespace from the beginning.
peter.muessig and frank.weigel gave me the idea and helped me with the implementation of this proof of concept.

### Development

The code of the latest version consumed by an application is always available on [npmjs.com:](https://www.npmjs.com/package/ui5-cc-spreadsheetimporter?activeTab=explore)
The source code is available here: <https://github.com/marianfoo/ui5-cc-spreadsheetimporter>

You can see the namespace with the version in the code and of course also in the [ui5.yaml](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/main/packages/ui5-cc-spreadsheetimporter/ui5.yaml):

```
specVersion: '2.6'

type: module

metadata:

  name: ui5-cc-spreadsheetimporter

resources:

  configuration:

    paths:

      /thirdparty/customControl/spreadsheetImporter/v0_21_0/: ./dist/
```

Of course, it would be a pain to always change this namespace manually. So here we use a combination of [node script](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/main/dev/replace-string.js) and the "[ui5-tooling-stringreplace](https://www.npmjs.com/package/ui5-task-stringreplacer)" module.

As a basis for the version we always take the [versions attribute from the package.json](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/6cfc2c17c09bf3a09fb21d41e09778b4367ab1cf/package.json#L3).
The node script takes this version and replaces the version in the yaml files for the [component](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/main/packages/ui5-cc-spreadsheetimporter/ui5.yaml), for the [build](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/main/packages/ui5-cc-spreadsheetimporter/ui5-build.yaml) and for the [ABAP system deployment](https://github.com/marianfoo/ui5-cc-spreadsheetimporter/blob/main/packages/ui5-cc-spreadsheetimporter/ui5-deploy.yaml).

Since the current version is now in the yaml files, we can use them and ...