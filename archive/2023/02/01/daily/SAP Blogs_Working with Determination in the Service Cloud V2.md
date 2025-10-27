---
title: Working with Determination in the Service Cloud V2
url: https://blogs.sap.com/2023/01/31/working-with-determination-in-the-service-cloud-v2/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:19:59.568024
---

# Working with Determination in the Service Cloud V2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Working with Determination in the Service Cloud V2

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6284&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Working with Determination in the Service Cloud V2](/t5/crm-and-cx-blog-posts-by-members/working-with-determination-in-the-service-cloud-v2/ba-p/13556679)

![aditya19](https://avatars.profile.sap.com/8/a/id8a5c77daafcf32096b535eedce6814e3dcb503301e9b9275fab5402efce1edfc_small.jpeg "aditya19")

[aditya19](https://community.sap.com/t5/user/viewprofilepage/user-id/121806)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6284)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6284)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556679)

‎2023 Jan 31
5:20 PM

[9
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6284/tab/all-users "Click here to see who gave kudos to this post.")

4,075

* SAP Managed Tags
* [SAP Cloud Portal service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Portal%2520service/pd-p/01200314690800003678)
* [SAP CRM Service Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520CRM%2520Service%2520Manager/pd-p/67837800100800006431)
* [SAP Service Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520Cloud/pd-p/73555000100700000801)
* [C4C Service](https://community.sap.com/t5/c-khhcw49343/C4C%2520Service/pd-p/569449780209093647095570245113309)
* [CRM Service](https://community.sap.com/t5/c-khhcw49343/CRM%2520Service/pd-p/336839465795980684603250734763165)
* [SAP Field Service Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Field%2520Service%2520Management/pd-p/73554900100700002181)

* [SAP CRM Service Manager

  SAP CRM Service Manager](/t5/c-khhcw49343/SAP%2BCRM%2BService%2BManager/pd-p/67837800100800006431)
* [SAP Cloud Portal service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BPortal%2Bservice/pd-p/01200314690800003678)
* [CRM Service

  Software Product Function](/t5/c-khhcw49343/CRM%2BService/pd-p/336839465795980684603250734763165)
* [C4C Service

  Software Product Function](/t5/c-khhcw49343/C4C%2BService/pd-p/569449780209093647095570245113309)
* [SAP Field Service Management

  Software Product](/t5/c-khhcw49343/SAP%2BField%2BService%2BManagement/pd-p/73554900100700002181)
* [SAP Service Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BService%2BCloud/pd-p/73555000100700000801)

View products (6)

Objective: Creating a custom logic using Determination.

SAP recently announced a new service solution called SAP Service Cloud V2. The new SAP Service Cloud that uses sap business technology platform (BTP) revolutionizes the service industry with a focus on customer service, providing meaningful connections with speed of service, proposing quick solutions and with a modern and customizable interface.

With SAP Service Cloud Version 2, the service agents have customer information at their fingertips. Using the collaboration tools and knowledge base, the agents can quickly address customer issues. With vast integration capabilities, the agents can stay up to date on the latest service requests, comments, discussions, and decisions online. Service Cloud Version 2 automatically assigns tasks to a case based on the relevant attributes to help and guide service agents through complex processes. Extensibility allows partners to extend the software platform without having to modify the original codebase. As a result, you can add to the base functionality of the system, thereby offering new capabilities and outputs.

In the Service Cloud V2, we can create custom logic to automatically update some fields based on certain conditions or to raise errors. Custom logics can be of two types – Determinations and Validations. Using Validations, the customer can raise an error or warning message in the system using certain conditions. Whereas using Determinations, the customer can assign certain value to a field or update a field based on certain conditions. Using determinations, customer can either default or propose the value or mandate a certain value.

**Creating a determination:**

Here, I am creating a determination which works with the Cases (tickets). The custom logic will work in such a way that if the ‘caseType’ of the case is ‘Request Product Repair’ and its ‘origin’ is ‘Email’, then the ‘Priority’ of the case should change to ‘Immediate’ automatically.

1. A determination can be created in “Extensibility Admin”. To navigate to determination-

Click on your user profile -> select settings (all the settings are listed here) -> search Extensibility (Extensibility Administration comes under a group called Extensibility) -> click on Extensibility Administration. These steps will land you on this page-

![](/legacyfs/online/storage/blog_attachments/2023/01/1-68.png)

The page displays a list of all business entities in the left panel. These entities are grouped by services.

2. Click on a service and it displays all the available entities.

Here, we are selecting the entity ‘case’ under ‘case service’, where we want to determine the priority of a case using determination. Once you click on the entity, 4 tabs appear on the left side of the screen – custom fields, field attributes, validations and determinations.

![](/legacyfs/online/storage/blog_attachments/2023/01/2-39.png)

3. Go to the Determinations tab and click the Create Determination icon (+). The system will launch the determination editor tab.

![](/legacyfs/online/storage/blog_attachments/2023/01/3.1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/3.2.png)

The editor has three main blocks:

Header: Specify the determination name, event, and description here.

![](/legacyfs/online/storage/blog_attachments/2023/01/head.png)

Condition: Set the desired conditions using a flow-based visual condition editor.

![](/legacyfs/online/storage/blog_attachments/2023/01/cond.png)

 Assignment: Assign a value to specific fields.

![](/legacyfs/online/storage/blog_attachments/2023/01/assig.png)

4. In the header block, enter the name of the determination.

Entity is pre-selected. And then choose the event. There are 2 types of events:

* Pre Hook: You can use it to default or suggest standard and custom field values. The user can change the field values. Where both standard fields and extension fields can be modified.

* Post Hook: It can only be used to update or mandate the custom field values. The user cannot overwrite the field values.

Finally, add the description:

![](/legacyfs/online/storage/blog_attachments/2023/01/4-25.png)

5. In the condition box, set the desired condition.

We can add multiple conditions by clicking the Add Condition icon (+). To remove a condition, click the Remove Condition (x). To clear all conditions in a block, click the Delete Condition Block icon. Under the Summary header, the system shows you a summary of all the conditions that you’ve entered.

![](/legacyfs/online/storage/blog_attachments/...