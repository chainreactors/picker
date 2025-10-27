---
title: Third-party subcontracting process overview in SAP S/4HANA
url: https://blogs.sap.com/2023/06/10/third-party-subcontracting-process-overview-in-sap-s-4hana/
source: SAP Blogs
date: 2023-06-11
fetch_date: 2025-10-04T11:45:21.239954
---

# Third-party subcontracting process overview in SAP S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Third-party subcontracting process overview in SAP...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161118&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Third-party subcontracting process overview in SAP S/4HANA](/t5/technology-blog-posts-by-members/third-party-subcontracting-process-overview-in-sap-s-4hana/ba-p/13556558)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161118)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161118)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556558)

‎2023 Jun 10
8:49 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161118/tab/all-users "Click here to see who gave kudos to this post.")

21,082

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [MM Purchasing](https://community.sap.com/t5/c-khhcw49343/MM%2520Purchasing/pd-p/507573428100543543566493124410813)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [MM Purchasing

  Software Product Function](/t5/c-khhcw49343/MM%2BPurchasing/pd-p/507573428100543543566493124410813)

View products (7)

In third-party subcontracting process the delivery of the goods required by the customer is not done by sales organization where customer orders. Instead, the request of the goods is forwarded to an external vendor who sends the material directly to the customer.
Here is what happens in third-party subcontracting process:
1. Customer orders goods and a sales order is created in a sale organization.
2. Subcontracting Purchase requisition is created automatically when sales order is saved.
3. Purchase order is created at the vendor in the MM purchasing application (manually or automatically)
4. If the vendor does the outbound delivery to the customer, the goods receipt can be posted in SAP.
5. Invoice receipt is created (invoice from vendor)
6. Invoice to customer is created (order-based invoice)

SALES ORDER
Third-party subcontracting process is triggered when the sales order with third-party item is created. Depending on settings done in customization third-party subcontracting item categories can be automatically determined by the system (automatic third-party subcontracting processing) or they can be changed from standard item to third-party subcontracting item category in sales order (manual third-party subcontracting processing).

SPRO

Sales order type used for third-party – OR (standard order)

Define Item Category Groups for third-party subcontracting

Schedule line category for third-party – DS

Item category for third-party subcontracting– TADS
Let’s look deeper into the settings in the system done for automatic and standard third-party process:
ITEM CATEGORY TADS:

Create PO Automatic indicator is not marked in TADS.

ITEM CATEGORY DETERMINATION

Item category group can be found in material master, Sales: Sales org.2 view.

To flag a material master directly for subcontracting, choose a half finished (HALB) or finished (FERT) material, and in the MRP2 tab maintain the Special Procurement field with option 30 for the plant, as shown below.

SCHEDULE LINE CATEGORY DS

Item category TADS will be determined automatically for standard order (OR) and item category group BADS (third-party subcontracting item).

Data: Order type = NB, Item Category = L and Acct.AssgntCat = X is the data for Purchase requisition.

If it is filled like above the purchasing requisition will be created automatically as standard purchasing requisition (NB), with item category S and acc.assign cat X.

The mapping of item category (from 3 to L) can be found in IMG: MM->Purchasing->Define External Representation of item categories. The definition of account assignment category can be found in IMG: MM->Purchasing->Account assignment->Maintain acc.\*\*\*. Categories

SCHEDULE LINE CATEGORY DETERMINATION

THIRD-PARTY SUBCONTRACTING PURCHASE REQUISITION

After saving sales order with item category TAS the purchase requisition is automatically created. In order to see the document go to: Environment -> Status overview and expand data for item, then expand data for purchase requisition as well:

Double click on the requisition number and you will be taken to the purchase requisition document.

The other way is to go to schedule line where you can find the purchase requisition number.

If third-party item has more than one schedule line with confirmed quantity > 0, then new item in purchase requisition is created for each schedule line.

It is wise to have the vendor determined in source of supply at this stage of the process (i.e. source list)

ME13

ME03

MANUAL PURCHASE ORDER
The purchase requisition needs to be converted into purchase order in MM (t-code me21n or me58). The purchase order document type is NB (standard order), item category L, that must be assigned to account. Thus account assignment category needs to be given. In this example it is X (automatically taken during conversion from purchase requisition, as it was defined in item category DS).

The definition of acct assignment category can be found in IMG: MM->Purchasing->Account assignment->Maintain acc.\*\*\*. categories:

The mapping of item categories: IMG: MM->Purchasing->Define External Representation of item categories:

AUTOMATIC PURCHASE ORDER
As it was written before – the purchase requisition is created automatically when sales order is saved. It is possible to automatize the next step, the creation of purchase order, as well.

ME59N

M...