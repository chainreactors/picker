---
title: Opened and Returned HU first. FUFO, FRFO principle. Definition and implementation via SAP EWM BADI
url: https://blogs.sap.com/2023/04/15/opened-and-returned-hu-first.-fufo-frfo-principle.-definition-and-implementation-via-sap-ewm-badi/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:27.893859
---

# Opened and Returned HU first. FUFO, FRFO principle. Definition and implementation via SAP EWM BADI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Opened and Returned HU first. FUFO, FRFO principle...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4620&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Opened and Returned HU first. FUFO, FRFO principle. Definition and implementation via SAP EWM BADI](/t5/supply-chain-management-blog-posts-by-members/opened-and-returned-hu-first-fufo-frfo-principle-definition-and/ba-p/13553602)

![gorbenkoteh](https://avatars.profile.sap.com/4/6/id46ee6e66e93c22dabdfa29c69de688bd03ae6636bed22ff4c9e0a1d8e92ee3c3_small.jpeg "gorbenkoteh")

[gorbenkoteh](https://community.sap.com/t5/user/viewprofilepage/user-id/594529)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4620)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4620)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553602)

‎2023 Apr 15
4:31 PM

[6
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4620/tab/all-users "Click here to see who gave kudos to this post.")

4,984

* SAP Managed Tags
* [EWM - Quality Management](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Quality%2520Management/pd-p/8dbbb533-ae73-41e6-aaf4-f085c0b172a8)
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Quality Management

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BQuality%2BManagement/pd-p/8dbbb533-ae73-41e6-aaf4-f085c0b172a8)

View products (2)

# Intro:

In Logistic well-known such terms as FEFO, LIFO and FIFO. In this blog-post we invent a few new logistic terms and realize a logic from it  via SAP EWM BADI implementation

## **FEFO:**

First Expired, First Out (FEFO) is a term used in field inventory management to describe a way of dealing with the logistics of products that have a limited shelf life. These items include perishable products or consumer goods with a specified expiration date. The product with the deadline for the next intake will be the first to be served or removed from stock. FEFO is majorly used in the pharmaceutical and chemical industries where expired dates are calculated based on a batch-expired date or shelf-life time.

## **FIFO:**

First In, First Out (FIFO) is a term means that has entered our logistics process must be the first one to comes out. It is the most widely used logistics management method. The objective is to achieve a good rotation of the parts. It is an excellent method so that the parts that are already manufactured come out quickly and do not generate unnecessary stock.

## **LIFO:**

Last In First Out (LIFO) is a term means that the last goods to be stocked are the first goods to be removed.

For warehouses related to pharmaceutical industry a few additional terms can be invented in this blog-post.

## **FUFO:**

First Uncovered First Out (FUFO)

Explanation:  In pharm industry working via GMP standards [1] raw material from inbound deliveries to warehouse  have a inbound quality control via special

quality control team.

For example: inbound delivery contains a 50 pcs of potassium sorbate.

Common used in pharma industry formula quantity pcs for sample selection=1.5\*sqrt (total quantity in inbound delivery)

So for use case with potassium sorbate sample qnt will be    1.5\*sqrt(50 pcs) = 11 pcs.

Quality control team in special room open a 11 pcs for sample selection.

In total we have a 50 pcs with the same batch, with the same shelf life and receipt date.

Obviously opened pcs should have higher priority opposed not opened pcs for transfer raw material from warehouse to production.

For this blog-post we will call this as principle of FUFO.

## **FRFO:**

First Returned First Out  (FRFO)

Explanation:

Let's imagine a modern production.

For the production of a specific batch of products, raw materials e.g.  A, B, C, D, etc. are needed from the warehouse.

For companies with SAP Landscape  - ERP-operator (employee from production department) create in SAP ECC(or SAP S/4HANA) Outbound delivery with direction from warehouse to production with raw-materials (e.g. A,B,C,D etc) and releases it to SAP EWM

A situation is possible when, after the production of a batch, some part of the raw material remains, which must be handed over to the warehouse where the raw materials will await the production of the next batch.

ERP-operator (employee from production department) create in SAP ECC(or SAP S/4HANA) Inbound delivery with direction from production to warehouse with  remaining raw-materials (e.g. A,B,C,D etc) and releases it to SAP EWM.

Obviously returned to warehouse pcs should have higher priority opposed not returned pcs for transfer raw material from warehouse to production at the next iteration.

For this blog-post we will call this as principle of FRFO

## **Business problem.**

For outbound deliveries with raw materials  in direction warehouse -> production a next industry-specific sorting logic must be implemented in SAP EWM:

Priority 1. Batches with minimal shelf life (FEFO)

Priority 2.  Bathes entered on warehouse first (FIFO)

Priority 3. Bathes returned from production line (FRFO)

Priority 4. Bathes stored in a uncovered handle units (FUFO)

# Realization.

To solve this business problem we can implement BADI  */SCWM/EX\_CORE\_RMS\_DETERMINE* with customer-specific code.

Let's do it step by step.

## Step 1. Overview of /SCWM/EX\_CORE\_RMS\_DETERMINE

BADI purpose:  customer specific sorting or filtering of quants, which SAP EWM has determined according to standard settings.

**Input:**

IS\_LTAP - warehouse task structure for which the quantum is searched

IS\_MAT\_GLOBAL - global material data

IS\_MAT\_LGNUM - warehouse number specific material data

IT\_MAT\_UOM - material data by unit of measure

IS\_T331 - storage type data for which the run is performed

IS\_T333 - settings data of the warehouse process type with which the quant search is performed

IT\_QMAT - table of quants that the SAP EWM found according to the standard strategy

IV\_REM\_RULE - material issue strategy, which was determined according to the settings

IO\_LOG - log object

IV\_ROW - log object  (row)

**Output:**

ET\_QMAT\_CUS - the output table of quants that the system will use if we need changes.

EV\_SET - sign that you need to use ET\_QMAT\_CUS

CS\_ORDIM\_CUST - warehouse task data in a custom structure

For implementation of this BADI, we need a algorithms for determining opened and returned HU first.

Describe it in the next steps.

## Step 2. Let's define an Opened HU

For FUFO principle implementations we

must distinguish a opened HU from an unopened one.

From warehouse to warehouse this approach can be different.

But the method described below may be some idea, a draft just for your project.

In my case we have a storage area[2...