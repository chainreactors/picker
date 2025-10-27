---
title: Fiori PO Approver app Forward button customization from ECC backend
url: https://blogs.sap.com/2023/08/25/fiori-po-approver-app-forward-button-customization-from-ecc-backend/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T11:59:58.161113
---

# Fiori PO Approver app Forward button customization from ECC backend

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Fiori PO Approver app Forward button customization...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165507&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fiori PO Approver app Forward button customization from ECC backend](/t5/technology-blog-posts-by-members/fiori-po-approver-app-forward-button-customization-from-ecc-backend/ba-p/13580901)

![jayesh_mudaliar](https://avatars.profile.sap.com/0/b/id0bc52d9bf0c87db815f369efd03d5ca5d98c2bb9b15c2909674b80e3e3820b1f_small.jpeg "jayesh_mudaliar")

[jayesh\_mudaliar](https://community.sap.com/t5/user/viewprofilepage/user-id/230182)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165507)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165507)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580901)

‎2023 Aug 25
9:43 PM

0
Kudos

2,196

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP NetWeaver](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver/pd-p/01200314690800000134)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP NetWeaver

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver/pd-p/01200314690800000134)
* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)

View products (6)

Hello Fellow Developers,

Let me directly dive into the requirement, We are currently hosting Fiori on top of ECC backend. The requirement came while enabling the PO approval using My Inbox.

The first part of customization comes on the Forward Button. As per the approval matrix the approvers were maintained in the PPOME structure. The problem occurred when the approver was forwarding the PO to another approver. However, on clicking the Forward button it was displaying all the list of Users from SU01. This was creating a lot of confusion for the approvers. So the initial requirement came as to fix the list that was appearing on clicking the Forward Button.

I will be displaying the 2 possible approach for Forward Button customization from the Backend.

**Approach 1 – Creating the custom class and attaching it in Service Implementation.**

**Approach 2 – Implement the BADI to change the values fetched from the Standard.**

Let’s start with the first approach.

The standard ODATA for PO approval is GBAPP\_POAPPROVAL.

Step 1 . Open your Gateway system -> Execute /IWBEP/REG\_SERVICE and maintain the service details

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture1-37.png)

Step 2 Maintain the Class name in DPC.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture2-23.png)

**Note : Creating of the class would be in the Backend System**

**Step 3 Open Backend System and Create the class maintained in Gateway system.**

You can copy/maintain the redefinition of the methods as per your need. Super class should be maintained as the /IWBEP/CL\_MGW\_PUSH\_ABS\_DATA. This will redirect the data flow of standard Odata call into the Custom Implementation.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture3-16.png)

I have copied all the methods from the standard class into my custom class to avoid any discrepancies. My requirement is also very small that’s why I didn’t wanted to touch other functionality so copying worked for me.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture4-18.png)

Just for showing from where the whole list of users were displaying. Please follow through as this is kind of RCA.

If you drill down into the GET\_ENTITYSET. You may find this
WHEN cl\_gbapp\_apv\_po\_mdp=>cty\_entities-agent.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture5-16.png)

This gets triggered for the event of Forwarding the work item to another approver. However, if you go into GET\_AGENT\_LIST method. You may find

CALL METHOD lo\_cmn->get\_users\_for\_forwarding.

This method is responsible for displaying all the lists of user from SU01 which is kind of misleading in our case.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture6-14.png)

**Step 4 Modify the Approver List**

So to suffice this requirement you can write your own logic and bypass the GET\_AGENT\_LIST method at the following place and the new list will be forwarded to the UI again as the output.

Create the list of approvers which you want to show and pass the list in lt\_forward\_users.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture7-15.png)

This is a long way approach where a lot of customization can be done as per your requirements.

**Approach 2 – BADI Extensibility Approach**

**Normally for any custom enhancements we can directly enhance the ODATA however for the case of PO Approver app SAP has provided an option for BADI Extensibility for PO Approve application.**

**Step 1**

**Go to SE18 in the backed system.**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture8-16.png)

**Step 2 Create Implementation under Definition GBAPP\_APV\_PO\_RDP**

If you are not familiar with creating implementations follow through / skip to next step.

Right click on implementation -> Create Badi Implementation -> Specify the Enhancement Implementation & Short Text.

**![](/legacyfs/online/storage/blog_attachments/2023/08/Picture9-14.png)**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture10-13.png)

Once you specify the Enhancement Implementation system will ask for BADI Implementation.

Maintain them.

**![](/legacyfs/online/storage/blog_attachments/2023/08/Picture11-14.png)**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture12-13.png)

**![](/legacyfs/online/storage/blog_attachments/2023/08/Picture13-11.png)**

**Note : You can reuse the same enhancement implementation for other requirements as well related to PO approve applications extensibility . No need to create every time.**

**Step 3 – Implementation of Class**

In the Implementing class you may find all the lists of methods present.

**![](/legacyfs/online/storage/blog_attachments/2023/08/Picture14-11.png)**

The first method IF\_G...