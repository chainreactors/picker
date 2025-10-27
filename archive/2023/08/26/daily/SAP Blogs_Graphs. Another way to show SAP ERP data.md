---
title: Graphs. Another way to show SAP ERP data
url: https://blogs.sap.com/2023/08/25/graphs.-another-way-to-show-sap-erp-data/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T12:00:13.697468
---

# Graphs. Another way to show SAP ERP data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Graphs. Another way to show SAP ERP data

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165489&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Graphs. Another way to show SAP ERP data](/t5/technology-blog-posts-by-members/graphs-another-way-to-show-sap-erp-data/ba-p/13580803)

![aamelin1](https://avatars.profile.sap.com/8/e/id8eacda0d2305d74a12c601ec075433bbe922d1383cf670a775c5368c0ec2b14e_small.jpeg "aamelin1")

[aamelin1](https://community.sap.com/t5/user/viewprofilepage/user-id/157733)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165489)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165489)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580803)

‎2023 Aug 25
8:58 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/165489/tab/all-users "Click here to see who gave kudos to this post.")

3,315

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [UI SAP GUI for Java](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520GUI%2520for%2520Java/pd-p/365168143769967368427513862901274)
* [UI SAP GUI for Windows](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520GUI%2520for%2520Windows/pd-p/345385326078662132058122667685214)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [UI SAP GUI for Java

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BGUI%2Bfor%2BJava/pd-p/365168143769967368427513862901274)
* [UI SAP GUI for Windows

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BGUI%2Bfor%2BWindows/pd-p/345385326078662132058122667685214)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (4)

# Existing visualisation tools at SAP

How typical SAP report looks like? Like a table with a lot of data or list of entries. Usually, table-like visualisation functionality using to represent data, such as:

* Classic **ALV Grid/List** - to show transparent table data

* Modern ALV, like **IDA**, **PIVB** etc - for tables

* **ALV hierarchy, ALV tree** - to show hierarchy related data

* **FIORI** tools to display tables (**design studio**, lists etc) - for tables too

All these tools are great for displaying table data, but sometimes SAP data is not a table structured, so, it's hard to display this kind of data via these tools.

## Non table-like types of SAP data

For example, I think a lot of us make a lot of diagrams with explanation of the business processes with accounts postings as a **T-accounting view**, like this:

![](/legacyfs/online/storage/blog_attachments/2023/08/ScreenShot2023-08-20-at-21.24.08@2x.png)

Another example - visualisation of **production processes** like chain of:

materials->PP orders->semi-finished goods->another PP order->finish good->sales

Like this:

![](/legacyfs/online/storage/blog_attachments/2023/08/ScreenShot2023-08-21-at-11.49.20@2x.png)

All these data are impossible (or really hard) to represent by table view. Also, existing SAP tools (like FIORI lighthouse app ["Display Journal Entries in T-Account View"](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/index.html#/detail/Apps('F3664')/S26OP) or [SAP Graph](https://help.sap.com/docs/graph)) are not so helpful in some cases.So, I think to show these kind of data I should use another approach for visualisation, like, for example Graphs at SAP GUI (SAPLogon) interface.

## What is Graphs?

**Graph** is a structure amounting to a [set](https://en.wikipedia.org/wiki/Set_%28mathematics%29 "Set (mathematics)") of objects in which some pairs of the objects are in some sense "related". The objects correspond to mathematical abstractions called *[vertices](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29 "Vertex (graph theory)")* (also called *nodes* or *points*) and each of the related pairs of vertices is called an *edge* (also called *link* or *line*).[[1]](https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29#cite_note-:0-1) Typically, a graph is depicted in [diagrammatic form](https://en.wikipedia.org/wiki/Diagrammatic_form "Diagrammatic form") as a set of dots or circles for the vertices, joined by lines or curves for the edges.

Here's a good explanation [Wikipedia. Graph (discrete mathematics)](https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29)

## How Graphs can be stored and visualised?

To show Graphs I will use [graphviz](https://graphviz.org/) solution.

Graphviz is **open source** graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks.

Just to understand how Graphviz works. I can create a HTML file with simple structure of Nodes and Edges like this:

```
digraph G {

  a -> b1;

  b1 -> c;

  a -> b2;

  b2 -> c;

}
```

And open this HTMS file at any browser to get a visualisation:

![](/legacyfs/online/storage/blog_attachments/2023/08/ScreenShot2023-08-20-at-21.21.09@2x.png)

To store Graph data I'll use a simplest approach - store all nodes and edges at two tables. Another options of storing graph data you may find [here](https://medium.com/%40siddarthsiddhu58/graph-storage-technique-7d32861956f0)

## Technical realisation of graphs at ABAP

### How to store graph as an internal table

To store Graph data at SAP I used a two internal tables:

* First one to store **Nodes (or *vertices)***. Here should be a unique node ID and some node attributes

|
 **Node ID (key)** |
 **Name** |
 **Other attributes** |

|
 ID 1 |
 Node one |
 Color, values, texts etc |

|
 ID 2 |
 Node two |
 ... |

* Second one - for **Edges**. Here's a info for relationship between Nodes and additional Edge attributes

|
 **Node From (key)** |
 **Node to (key)** |
 **Edge attributes** |

|
 ID 1 |
 ID 2 |
 Texts, amounts, color etc |

### Class to create HTML file of graph

Solution for working with Graphviz at ABAP has been developed by [github marcellourbani/abapgraph](https://github.com/marcellourbani/abapgraph)

I'll use this one, you can install it to your system via **ABAPGit** or manually (link above).

Simple example how it works:

a) Create a Node structure via **se11**

![](/legacyfs/online/storage/blog_attachments/2023/08/ScreenShot2023-08-21-at-13.29.58@2x.png)

b) Create a Edge structure via **se11**

![](/legacyfs/online/storage/blog_attachments/2023/08/ScreenShot2023-08-21-at-13.31.15@2x.png)

c) Create a report, select necessary data into two internal tables lt\_nodes[] (with p.a structure) and lt\_edges[] (with p.b structure), and create a Graph, like this:

```
*Create Graph

graph = zcl_abap_graph=>create( ).

*Add Nodes

zcl_abap_graph_node_record=>create(...)

*Add Edges (links)

<Node from>-cl->linkto( destination = <Node to> label = .....