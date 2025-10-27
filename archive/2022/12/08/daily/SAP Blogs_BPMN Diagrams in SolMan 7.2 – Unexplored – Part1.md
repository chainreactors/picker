---
title: BPMN Diagrams in SolMan 7.2 – Unexplored – Part1
url: https://blogs.sap.com/2022/12/07/bpmn-diagrams-in-solman-7.2-unexplored-part1/
source: SAP Blogs
date: 2022-12-08
fetch_date: 2025-10-04T00:53:04.767035
---

# BPMN Diagrams in SolMan 7.2 – Unexplored – Part1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* BPMN Diagrams in SolMan 7.2 - Unexplored - Part1

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163348&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BPMN Diagrams in SolMan 7.2 - Unexplored - Part1](/t5/technology-blog-posts-by-members/bpmn-diagrams-in-solman-7-2-unexplored-part1/ba-p/13568991)

![VigneshPrabhu99](https://avatars.profile.sap.com/6/f/id6f7eb1ce861e0bdf689b43fb0dc6ecad325fd2fd8bde3c210d77c68d81e114aa_small.jpeg "VigneshPrabhu99")

[VigneshPrabhu99](https://community.sap.com/t5/user/viewprofilepage/user-id/44981)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163348)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163348)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568991)

‎2022 Dec 07
5:11 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163348/tab/all-users "Click here to see who gave kudos to this post.")

2,211

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SOLMAN Process Management](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Process%2520Management/pd-p/876619786935845126962162607976597)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Process Management

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BProcess%2BManagement/pd-p/876619786935845126962162607976597)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (3)

Hello All,

I am so excited to write this blog on BPMN Diagram features in SAP Solution Manager 7.2 that are almost unknown and unexplored by many of us.

I got a chance to explore and unwind the features & capabilities of the in-built BPMN editor in SAP SolMan 7.2 system.

Come, let us see about each diagram type one by one,

**Universal Diagrams:**

Universal diagrams are used to model different sorts of diagrams including value chain diagram, capability maps, application landscapes, process landscapes, or any other kind of diagram. Unlike other diagrams, the universal diagrams don't follow given strict semantics.

Now let us see in detail about the options that are available for a user who creates Universal diagrams.

*Shapes in Universal Diagram:*

Below are the various shapes available when you are creating a universal diagram

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_1.jpg)

Shapes available in Universal Diagram

*Context Menu in Universal Diagram:*

In general, there are four parts of context menu objects that are available based on where you click on the screen,

#1 - When clicking the object

#2 - When right-click an object

#3 - When clicking the text symbol

#4 - When right-clicking a text symbol

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_3-2.jpg)

Context Menu options vary depending on where you click in the screen

*Section Palette in Universal Diagram:*

Section Palette shows the folders, Scenario, Process, Master Data, Organizational unit and Process steps that is present in the Solution Documentation Hierarchy, and you can include the required existing diagrams as a reference as shown below

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_6.jpg)

Section Palette in Universal Diagram

Click on the value chain diagram from above screenshot, it leads to all the associated Processes as below,

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_7.jpg)

Value chain diagram

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_5.jpg)

Universal Diagram with Color variation

**Collaboration Diagram:**

Collaboration diagrams are representations of the actual model but enrich the model with additional semantics and information. A collaboration diagram analyzes the sequence flow of processes and the exchange of messages between participants (represented as swim lanes and pools).

Now let us see in detail about the options that are available for a user who creates Collaboration diagram in SAP Solution Manager.

*Message Flow Rules:*

1. Message Flows cannot connect to objects that are within the same Pool.

2. Only those objects that can have incoming and/or outgoing Message Flows are Pool, Task, Subprocess, Start Event, Intermediate Event and End Event.

3. Start Event / End event Rules: for start event we have just incoming message flow and outgoing message for end event.

4. We can assign interface to message flow just in case of,

   * Message Flow between two pools.

   * Message Flow between pool and draft pool.

   * Message Flow between pool and Black pool.

Right click each of the event type to see the options available as shown below

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_8.jpg)

Right click Start Event and select Message Start Event

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_9.jpg)

Right click intermediate event and select Catch Message Event

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_10.jpg)

Right click Intermediate Event and select Throw Message Event

*Palette section:*

There are 2 types of palette buttons,

* Some buttons have some “instances” of objects behind them, like lane, process steps.

* Other buttons represent objects which are graphical only (like gateways, events, sub processes).

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_11.jpg)

Collaboration Diagram - Palette Section - Type 1 buttons

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_12.jpg)

Collaboration Diagram - Palette button - Type 2

First, we need to choose the Lane that represents the respective Business Process inside which Pools shall be assigned.

As said above, there are 3 sub types namely

* Current Process - Represents the current Business Process

* Pool / Draft - To represent a process which is not known in detail

* Pool / Blackbox - To depict a message flow from current process,

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_13.jpg)

Lane and Pool in a Collaboration Diagram

Once the Lane and Pool is added, we can start building the Collaboration Diagram with Process Steps (Note: These Process steps comes from existing Solution Documentation Hierarchy, in case if it is missing then we can create new ones from the diagram itself)

So, in the below screenshot we can see that from the Lane chosen i.e., the Business Process, all the underlying Process steps are automatically shown while trying to add the Process step to the Collaboration Diagram

![](/legacyfs/online/storage/blog_attachments/2022/12/PM_14.jpg)

Automatic Population of Process steps from the SOLDOC Hierarchy

We can drag and drop the r...