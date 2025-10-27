---
title: SAP Datasphere Naming Convention in Action
url: https://blogs.sap.com/2023/03/14/sap-datasphere-naming-convention-in-action/
source: SAP Blogs
date: 2023-03-15
fetch_date: 2025-10-04T09:35:24.012751
---

# SAP Datasphere Naming Convention in Action

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere Naming Convention in Action

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163579&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere Naming Convention in Action](/t5/technology-blog-posts-by-sap/sap-datasphere-naming-convention-in-action/ba-p/13567336)

![GregoryRohloff](https://avatars.profile.sap.com/c/2/idc27f5dce7e90e2243fc0ae53584dfee3451435e79d38a6227b9de21a3bf72c4d_small.jpeg "GregoryRohloff")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[GregoryRohloff](https://community.sap.com/t5/user/viewprofilepage/user-id/127767)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163579)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163579)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567336)

‎2023 Mar 14
8:55 PM

[24
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163579/tab/all-users "Click here to see who gave kudos to this post.")

18,536

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2023/03/Image-scaled.jpg)

1: SAP Datasphere Naming Convention in Action (Source: SAP)

![](/legacyfs/online/storage/blog_attachments/2023/03/Yellow-Line.png)

## Introduction

Naming conventions help to establish a cross-functional structure and to maintain an overview in data warehouse projects. Since it is not always possible to predict how an existing project will develop, it is advisable to adhere to naming conventions consistently right from the start. In this blog post, suggestions are made for adhering to a consistent naming convention based on the example of the SAP Datasphere Data Challenge. These suggestions are meant as recommendations and can of course be customized along individual requirements. The focus of this blog post is on Modeling Objects and provides the reader with a quick overview of the topic - further resources are referenced.

## Content

* [Layer architecture for data warehouses](#LayerArchitectureForDatawarehouses)

* [Recommended approach and considerations](#RecommendedApproachAndConsiderations)

* [Examples](#Examples)

* [Abbreviations](#Abbreviations)

* [Procedure during the SAP Datasphere Data Challenge](#ProcedureDuringTheSAPDatasphereDataChallenge)

* [Conclusion](#Conclusion)

## Layer architecture for data warehouses

Modeling concepts for data warehouses are usually based on a layer architecture. Layers are logical groups of different entities (e.g. tables, views, data access controls, etc.). The following Figure shows a structure of such a layer architecture that has proven itself in practice.

![](/legacyfs/online/storage/blog_attachments/2023/03/LayerArchitecture.png)

Layered modeling approach (Source: SAP Datasphere First Guidance)

It is introduced within the [new first guidance document development guidelines and naming conventions](https://blogs.sap.com/2021/09/03/new-first-guidance-document-development-guidelines-and-naming-conventions/) document which goes into further detail about each layer.

## Recommended approach and considerations

The following considerations should be taken into account during the implementation of the Naming Convention. Depending on individual needs, this approach can be implemented for an entire SAP Datasphere Tenant or individual Spaces.

### Preparation

Before the artifacts of a project are created in the SAP Datasphere, essential contents of the project such as required subject areas should be roughly outlined. This is particularly important because the **technical name of an object cannot be changed after it has been saved**. Artifacts that have already been created would have to be replaced.

### Setting the structure

In the next step, a uniform structure of the Naming Convention (for the **technical names**) should be defined and adhered to. The following structure serves as an example and can be used as a template:

![](/legacyfs/online/storage/blog_attachments/2023/03/NCStructure.png)

Naming Convention Structure (Source: SAP Datasphere First Guidance)

#### 1. Layers and variants

A common modeling approach is to use stacked models with different layers. Therefore, it is useful to recognize already in the name of the object to which layer it is assigned. This also applies to the object type and different variants of tables or views. Either numbers or letters are suitable for this purpose (e.g. "A" = Analytical; "R" = Reporting; "H" = Harmonization; "P" = Propagation).

#### 2. Topic Area

In some cases several Topic Areas are stored in one Space (e.g. cost center as one area in a financial Space). Here it can be helpful to include the topic area in the name.

#### 3. Object Name

The object name should describe the object itself. If necessary, more than six letters or characters can be chosen for the object name.

#### 4. Number

Finally, it may be useful to append a two-digit number. This is especially relevant when multiple versions of similar artifacts are used for different purposes.

## Examples

From these considerations, the above structure can be applied to two specific examples from the SAP Datasphere Data Challenge as follows:

1TR\_EXC0\_KBAQ01\_01 - for a **r**elational **t**able for german car registrations in Q1 (Inbound Layer (1st))

4VA\_EXC1\_NCDEQ2\_02 - for an **a**nalytical **v**iew for new registered cars in germany in Q2 (Reporting Layer (4th))

## Abbreviations

The following figure gives an overview of how the object types and variants can be abbreviated within a SAP Datasphere project.

![](/legacyfs/online/storage/blog_attachments/2023/03/Table-1.png)

Abbreviation Table (Source: Own Image)

## Procedure during the SAP Datasphere Data Challenge

Figure 4 shows an example of a concrete use case of the naming convention and how it was implemented within the SAP Datasphere Data Challenge. In the following, the selected naming convention is explained using this example across the different layers.

### Inbound Layer

Relational tables from the SAP Datasphere Data Marketplace are used as the data source within the inbound layer. Since this is the first layer, a "1" was used as a prefix. Since these are relational tables, "TR" was chosen for the naming of the object-variant combination in each case (see Figure 3). The Topic Area concerns tasks 1 and 2 of the SAP Datasphere Data Challenge, "EXC0" and "EXC1". The Object Name was chosen individually, but should be as meaningful as possible despite the limitation of the number of characters.

### Harmonization Layer

In our example, the relational tables of the inbound layer were further processed in the harmonization layer using filters and saved in a relational view. Analogous to the procedure within the inbound layer, ...