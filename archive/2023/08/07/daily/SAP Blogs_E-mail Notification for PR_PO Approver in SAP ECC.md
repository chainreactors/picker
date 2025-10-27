---
title: E-mail Notification for PR/PO Approver in SAP ECC
url: https://blogs.sap.com/2023/08/06/e-mail-notification-for-pr-po-approver-in-sap/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:39.229057
---

# E-mail Notification for PR/PO Approver in SAP ECC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* E-mail Notification for PR/PO Approver in SAP ECC

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164443&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [E-mail Notification for PR/PO Approver in SAP ECC](/t5/technology-blog-posts-by-members/e-mail-notification-for-pr-po-approver-in-sap-ecc/ba-p/13575385)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164443)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164443)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575385)

‎2023 Aug 06
9:52 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164443/tab/all-users "Click here to see who gave kudos to this post.")

11,739

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)

View products (6)

# E-mail Notification for PR/PO Approver in SAP ECC

# Release Procedure for PR/PO

<https://youtu.be/twGrdPSU1VI>

PDF :

<https://icedrive.net/s/APyBWPS1tfDC5XRWt6wgj4DwAWhV>

Approvers may want to be instantly informed about the documents for approval. There are some standard and non-standard ways to do this. Some BADIs can be used for this process. Also, the workflow can be copied and a mail step can be added to the new workflow. But I want to show the standard way for this process. I will try to explain it step by step as much as I can.

### PRE REQUIS

###

### Define Release Procedure for Purchase Orders

In this step, you set up the release procedure for purchase orders (POs) and can link it to workflow. (Note that in this context "releasing" means "approving", or giving the "green light" to a document.)

**Requirements**

* In the case of a release procedure linked to workflow, you must have previously created the user names, positions, jobs, etc. that you here assign to the release code in the organizational plan and must have linked them to the relevant standard tasks in task-specific Customizing (Basis -> Business Management -> Business Workflow -> Perform Task-Specific Customizing).

* You must assign the authorization **M\_EINK\_FRG** to the persons who are to be involved in the release procedure (**Authorization Management** -> Create Authorization Profiles and Assign to Users).

**Activities**

Here you define the following:

* Release group

* Release codes

* Release indicator

* Release strategy

* Workflow

**Release group**

Create a release group for your release procedure and assign it to a class. In the process, you assign [**release conditions**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.352AD58C88E65CD5E10000009B38F974) to the release procedure.

**Release codes**

Here you create the [**release codes**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.3526BFF1AFAB52B9E10000009B38F974) you need for your [**release strategy**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.3526BFF3AFAB52B9E10000009B38F974) and assign the codes to your release group. If a release code is to be used in workflow, indicate this accordingly in the **Workflow** field

The **Workflow** indicator is also used to control [**role resolution**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.3526B123AFAB52B9E10000009B38F974):

* "1 - Role Resolution with Group, Code and Plant (T16FW)"

Here you use a role resolution that is supplied in the standard system. To do so, you must assign the release point in the section **Workflow** (see below).

* "9 - Role Resolution via User Exit"

Here you use the [**customer exit**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.3526B1B7AFAB52B9E10000009B38F974) M06E0005 to define a role resolution of your own.

**Release indicators**

A [**release indicator**](https://saphtmlphtmlviewer.sap.com/SAPEVENT%3ADOCU_LINK/DS%3AGLOS.352AC0A188E65CD5E10000009B38F974) shows the release status of a PO.

Via the following settings, you can define the release indicators you need for your release procedure:

* The **Released** indicator is used to specify whether messages (PO documents in output format) may be transmitted for a purchase order with this indicator.

* The **Changeability** indicator shows the effect of changes to the PO (a change to a PO may require a new release strategy to be determined, for instance).

* By means of the **Value change** indicator, you can specify that the release strategy is to be re-started if a PO is changed and the value of a PO item thereby increases by a certain percentage (e.g. 10%). Set the **Changeability** indicator to "4 - Changeable, new release in case of new strategy or value change" or "6 - Changeable, new release in case of new strategy or value change/outputted" and enter a percentage in the **Value change** field.

**Attention**:
The following release indicators are necessary for **every** release procedure:

* + Release indicator for **initial status**
    If the PO is subject to a release strategy, it must normally be released before it can be transmitted to the vendor. Therefore, when a PO is created, it is assigned a release indicator that blocks it from being outputted in message form.
    The **Released** indicator must *not* be selected for this indicator.

* + Release indicator for **released status**
    This indicator is assigned to the PO when it is released.
    The **Released** indicator **must** be selected for this indicator.

**R...