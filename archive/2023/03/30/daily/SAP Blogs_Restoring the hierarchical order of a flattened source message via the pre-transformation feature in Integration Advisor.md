---
title: Restoring the hierarchical order of a flattened source message via the pre-transformation feature in Integration Advisor
url: https://blogs.sap.com/2023/03/29/restoring-the-hierarchical-order-of-a-flattened-source-message-via-the-pre-transformation-feature-in-integration-advisor/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:35.973949
---

# Restoring the hierarchical order of a flattened source message via the pre-transformation feature in Integration Advisor

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Restoring the hierarchical order of a flattened so...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159094&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Restoring the hierarchical order of a flattened source message via the pre-transformation feature in Integration Advisor](/t5/technology-blog-posts-by-sap/restoring-the-hierarchical-order-of-a-flattened-source-message-via-the-pre/ba-p/13553678)

![stefan_boller](https://avatars.profile.sap.com/7/2/id72b9a2eb76edfbbeeb8c8a15265ed3a1a3c595fbbfa044a078149eca498f6089_small.jpeg "stefan_boller")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[stefan\_boller](https://community.sap.com/t5/user/viewprofilepage/user-id/196798)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159094)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159094)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553678)

‎2023 Mar 30
12:30 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159094/tab/all-users "Click here to see who gave kudos to this post.")

1,713

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

Recently we have introduced a new feature in Integration Advisor called "[pre-transformations](https://blogs.sap.com/2022/11/28/new-feature-in-integration-advisor-reordering-of-source-structure/)". This feature allows the reordering of the source MIG structure of a mapping guideline before the actual mapping so that the mapping later is simpler and focuses only on mapping of content between source and target fields.

Currently, two operations are supported "Copy Referenced Node" and "Group by Key" (see [online docu](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/b287e5eae6e54359bd0103d0f148befb.html?locale=en-US)). These two operations however can be used to model even more complex uses cases. One example of such a more complex use case is to restore the hierarchical structure of a flattened structure what shall be explained in this blog article.

## Scenario

As an example we use the following scenario: Assume you have a source MIG based on X12 856 message (Ship Notice/Manifest) which shall be mapped to a cXML ShipNoticeRequest based target MIG. The source X12 message has a flat structure. Here we used the qualification feature to model the different instances of the HL nodes which corresponds to Shipment, Order, Pack, and Item:

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreeSource.png)

Structure of source MIG (X12 856)

That means that Shipment, Order, Pack, and Item are siblings in the source structure. The target message, however, has a hierarchical structure, where ShipNoticePortion (corresponds to Order) is the parent of ShipNoticeItem (corresponds to Item), which again is the parent of Packaging (corresponds to Pack):

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreeTarget.png)

Structure of target MIG

If we naively did the following mappings

* HL [Order] -> ShipNoticePortion,

* HL [Pack] -> Packaging, and

* HL [item] -> ShipNoticeItem,

we would get in each Packaging instance a merge of all HL [Pack] instances instead of only the HL [Pack] instance which corresponds to the parent ShipNoticeItem and similar each item is added to each ShipNoticePortion instead of only the the corresponding ones:

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreeNaiveMapping.png)

Mapping without pre-transformation

Therefore we need to transform the structure of the source message first so that it reflects the hierarchy which is encoded in the HL segments of the X12 message. For that we want to use the pre-transformation feature.

## Preparation

For creating the pre-transformation you first need to build two MIGs: One based on X12 message 856 (Ship Notice/Manifest), which will be the source message, and another based on cXML ShipNoticeRequest. For the former one we use the qualification feature to create 4 sibling qualified nodes for the HL loop:

1. 735 = S with cardinality 1..1

2. 735 = O with cardinality 1..\*

3. 735 = P with cardinality 1..\*

4. 735 = I with cardinality 1..\*

Please, note that this qualification is not yet proposed by the MIG editor. You first have to create a corresponding qualifier marker (see [online docu](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/0101869f1b1d4118bd76a48feb9ba6e8.html)).

Add the following segments to the respective nodes:

1. N1

2. PRF

3. PO4 (select some child elements) and MAN

4. LIN and SN1

Then your MIG shall look similar to

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreeSource2.png)

Source MIG

For cXML ShipNoticeRequest add the following group nodes:

1. ItemID

2. Packaging

Now your MIG shall look similar to

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreeTarget2.png)

Target MIG

As last step of the preparation create a MAG with your two MIGs, navigate to "Overview", and add a pre-transformation via the + button.

## Build the pre-transformation

Now we can build our pre-transformation. Add a new transformation step with operation "Copy referenced node". Assign the following nodes as operation parameters:

* Receiving node: G\_HL\_gq\_P

* Node with reference ID: D\_628 (child node of G\_HL\_gq\_P)

* Referenced Node: G\_HL\_gq\_I

* Referenced ID Node: D\_734 (child node of G\_HL\_gq\_I)

and execute the pretransformation.

Then add a second transformation step of type "Copy referenced node" and assign the following nodes:

* Receiving node: G\_HL\_gq\_O

* Node with reference ID: D\_628 (child node of G\_HL\_gq\_O)

* Referenced Node: G\_HL\_gq\_P

* Referenced ID Node: D\_734 (child node of G\_HL\_gq\_P)

and execute the pretransformation again. Now the pre-transformed MIG shall look like

![](/legacyfs/online/storage/blog_attachments/2023/03/RestoreTreePretransformedSource.png)

Result of pretransformation

## Create the Mapping

The next step is the creation of the main transformation. For that press the "Main Transformation" button and connect the following nodes (here only the mapping elements are listed which are necessary for the demonstration of the restoration of the tree s...