---
title: New Feature in Integration Advisor: Reordering of Source Structure
url: https://blogs.sap.com/2022/11/28/new-feature-in-integration-advisor-reordering-of-source-structure/
source: SAP Blogs
date: 2022-11-29
fetch_date: 2025-10-03T23:58:44.398470
---

# New Feature in Integration Advisor: Reordering of Source Structure

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* New Feature in Integration Advisor: Reordering of ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162232&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [New Feature in Integration Advisor: Reordering of Source Structure](/t5/technology-blog-posts-by-sap/new-feature-in-integration-advisor-reordering-of-source-structure/ba-p/13563089)

![dirk_ostertag](https://avatars.profile.sap.com/d/c/iddc7cb43f875ce6d54482048be49e435b2040bd632343bbd6c7a759ae2e40a05b_small.jpeg "dirk_ostertag")

![Employee](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Employee")
[dirk\_ostertag](https://community.sap.com/t5/user/viewprofilepage/user-id/827372)

Employee

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162232)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162232)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563089)

‎2022 Nov 28
7:34 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162232/tab/all-users "Click here to see who gave kudos to this post.")

2,147

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

## Introduction

If you are familiar with doing complex mappings in SAP Integration Suite, it might be of interest for you, that Integration Advisor Capability of SAP Integration Suite now introduces a new powerful feature called pre-transformation of source Message Implementation Guide structure. With this new feature Integration Advisor now supports the reordering of source structure before the actual mapping is taking place.

In certain integration scenarios it is inevitable to apply specific structural changes to the incoming data structure. This is usually the case if the source and target side structures differ that much, that a simple 1:1 mapping between hierarchy levels on both sides is not possible.To cope with such situations, Integration Advisor now allows to apply structure modifying operation prior to the actual mapping is taking place. This new and optional transformation is called **Pre-transformation** because at runtime it is applied to the message payload *before* the actual transformation is applied and it is applied to the Message Implementation Guide at design time also *before* the mapping utilizes the transformed source structure.

By adding a Pre-transformation to the Mapping Guideline it is now possible to tailor the incoming data structure to fit the structural requirements of the outgoing data structure in integration scenarios where this is required. The result of the Pre-transformation then is used in the Mapping Guideline as the source side Message Implementation Guide while the original source side MIG becomes the input for the Pre-transformation. The entire functionality, that is required to develop and simulate Mapping Guidelines with Pre-transformation is encapsulated in the new version of the Mapping Guideline Editor in Integration Advisor.

The export of runtime artifacts for SAP Cloud Integration automatically contain all relevant entities for executing the Pre-transformation along with the main mapping. Hence, it is completely transparent to the executing integration flow whether an IA mapping contains a Pre-transformation or not. No changes or extensions to any integration flow are required for the Pre-transformation to be executed along with the main transformation. This way, Pre-transformation integrates perfectly with all existing integration flow, that might already be in use for running Integration Advisor mappings.

## The first two operations

The first version of Pre-transformation in Integration Advisor comes with two operations. The aim of the provided Pre-transformation operations is to encapsulate complex structural changes into one single step whenever possible.

Further operations are already on the roadmap.

### Copy Referenced Node

This operation allows to create a copy of a group node into a different group node, that is not the parent of this original group node. The copy operation itself is controlled by a reference between the copied node and the receiving group node. The user is free to choose that reference nodes. As a result, only such group nodes are copied into such receiving group nodes, where the two reference nodes contain the same value. Reference nodes always must be descendants of the involved group nodes (the copied node called "referenced node" and the "receiving node").

For instance, a source structure contains Items and corresponding Handling Units as sibling. Though the target structure requires the Items to be children of the corresponding Handling Units. Whenever it is possible in the source structure to derive a reference between the *corresponding* instances of Items and Handlings Units for example because both contain an ID, that allows to link them together, the operation **Copy Referenced Node** can be used to copy the items into the correct Handling Units.

### Group by Key

The purpose of this operation is to allow grouping of group nodes according to properties of these pre-existing group nodes. This property must be an {descendant} {{leaf}} node of the group that shall be grouped and is called the "group key node". For all instances of a group with the identical value in group key node, a new supergroup node will be created carrying a distinct group key. This new group collects all instances of the original group with one specific value in group key node. As the result of this operation, the structure will contain one instance of the newly created supergroup for each distinct value of group key node. All instances of the original group node will be moved into the super group with the value of group key corresponding to the value of the group key node of this original group.

Assuming a source structure contains an arbitrary number of handling units of different types as sibling nodes on the same hierarchy level. Further on these units can appear in arbitrary order while the target structure required such units to be in order corresponding to their type. In this case the handling unit itself would be the group to be grouped into newly to be created instances of the super group. The type of the unit would become the Id to be used for grouping. The result of the operation is one instance of the supergroup for each distinct type of ...