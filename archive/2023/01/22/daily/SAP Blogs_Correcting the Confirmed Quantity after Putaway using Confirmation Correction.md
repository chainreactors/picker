---
title: Correcting the Confirmed Quantity after Putaway using Confirmation Correction
url: https://blogs.sap.com/2023/01/21/correcting-the-confirmed-quantity-after-putaway-using-confirmation-corrections/
source: SAP Blogs
date: 2023-01-22
fetch_date: 2025-10-04T04:33:25.309992
---

# Correcting the Confirmed Quantity after Putaway using Confirmation Correction

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Correcting the Confirmed Quantity after Putaway us...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4501&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Correcting the Confirmed Quantity after Putaway using Confirmation Correction](/t5/supply-chain-management-blog-posts-by-members/correcting-the-confirmed-quantity-after-putaway-using-confirmation/ba-p/13548660)

![shivaewm](https://avatars.profile.sap.com/8/c/id8cb0bc6f5cf9f126184f2df919fdacd32504626db1e4ac660be4e8c9b9a7aa84_small.jpeg "shivaewm")

[shivaewm](https://community.sap.com/t5/user/viewprofilepage/user-id/727522)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4501)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4501)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548660)

‎2023 Jan 21
5:12 AM

[8
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4501/tab/all-users "Click here to see who gave kudos to this post.")

19,150

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)

View products (3)

After the completion/confirmation of the putaway task, sometimes it gets noticed that there is a difference in the quantity being confirmed versus the the delivered quantity. There may be a chance of wrong counting and inputting the wrong quantity due to human error.. If there is a difference then this difference needs to be adjusted to avoid the difference in the physical stock between the systems.

If the same product is supplied by multiple supplier then it will become a tedious task to identify the discrepancy.

This blog post provides a high-level overview of the confirmation correction functionality after the completion the putaway task.

The system allows the user to modify/update the quantity received using the confirmed warehouse task using the handheld device or the standalone GUI transaction code if the time delay has not exceeded. If the time delay set up has exceeded then the system changes the status of the delivery to the 'DCO' and sends the GR information to the ECC/ERP system.

EWM delays sending a warehouse task that has already been confirmed, corresponding to the completion delay you have specified for inbound deliveries in Customizing. In accordance with the completion delay, you can still correct the actual quantity for the destination storage bin and the batch. You make your correction and specify an exception code in the warehouse task for each delivery item.

When the completion delay has exceeded, the EWM system sets the status "DWM" for sending the completion indicator to "Completed" . By doing this, EWM also indirectly sets the completion status "DCO" for the inbound delivery to "Completed" . Once the completion status "DCO" for an inbound delivery has status value "Completed, then "EWM system initiates the goods movement activities in the ERP system. The system won't allow to make any corrections in the confirmed warehouse task.

The report /SCWM/R\_PRDI\_SET\_DWM is used to set the status "DWM" for sending the completion indicator to "Completed. When the confirmation correction activity is performed the system automatically creates a background job using the job delay with the released status. The job gets processed according to the schedule."

The confirmation correction activity uses the exception code called 'COCO' to allow the changes to the document.

Note – All the steps were configured and tested on SAP S/4 2021 Embedded system.

Deployments:

* Decentralized EWM and Embedded initial release onwards

* Application Component – SCM-EWM-WOP-BF-CC

Steps:

* **Activation of the status 'DWM'** -  IMG Path - SPRO–IMG-SCM Extended Warehouse Management-Extended Warehouse Management-Cross-Process Settings-Delivery Processing-Status Management-Define Status Profiles

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-3.png)

**Active Status**

* **Define Delay in Completion of Inbound Deliveries** - SPRO–IMG-SCM Extended Warehouse Management-Extended Warehouse Management- Goods Receipt Process- Inbound Delivery- Define Delay in Completion of Inbound Deliveries

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-4.png)

**Note:**

**Tolerance for Completion -** Sets the 'DCO' status for several items simultaneously, EWM collects all completed items for which EWM has set the *DWA* status to *Completed* within this time. The time for the tolerance must be smaller than the completion delay.

**Delay in Job Rescheduling for Setting DWM Status** - Delay in rescheduling a background job for the job to set the 'DWM' indicator. If EWM cannot set the *DWM* status within the background job, EWM schedules a new job. If you do not specify your own value, EWM uses the default value of 120 seconds

* **Exception Code 'COCO' Set up** - Make sure that the exception code 'COCO' is active for the warehouse.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-5.png)

**Note: Make the required settings for the exception code 'COCO' if not available.**

* ### **Testing**

* **Case 1 -  Confirmed quantity is more than the inbound delivery quantity.**

* + Create a Purchase order and a subsequent delivery for the PO.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-6.png)

**ERP Inbound delivery**

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-7.png)

**EWM Inbound Delivery**

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-8.png)

* + Create the warehouse task for the product. In this step, we are not packing the product and there are no HUs associated with.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-9.png)

* + Confirm the warehouse task.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-11.png)

* + Verify the background job scheduled to set the completion status.

### ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot1-12.png)

* + Now Update received/GR quantity by editing the confirmed warehouse task.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sc...