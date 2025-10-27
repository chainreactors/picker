---
title: Multi Ship-to Order (MSO)- How to (Retail/FMS))
url: https://blogs.sap.com/2023/03/26/multi-ship-to-order-mso-how-to-retail-fms/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:46:03.379067
---

# Multi Ship-to Order (MSO)- How to (Retail/FMS))

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Multi Ship-to Order (MSO)- How to (Retail/FMS))

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67418&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Multi Ship-to Order (MSO)- How to (Retail/FMS))](/t5/enterprise-resource-planning-blog-posts-by-members/multi-ship-to-order-mso-how-to-retail-fms/ba-p/13555202)

![govind_singh5](https://avatars.profile.sap.com/a/3/ida3ea81e69b257a004b3cbd360b1f1b51cf0065ae86a0a071f89ca773b1dbcb23_small.jpeg "govind_singh5")

[govind\_singh5](https://community.sap.com/t5/user/viewprofilepage/user-id/234553)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67418)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67418)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555202)

‎2023 Mar 26
4:00 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67418/tab/all-users "Click here to see who gave kudos to this post.")

3,948

* SAP Managed Tags
* [Retail](https://community.sap.com/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [SAP ERP add-on for retail](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520add-on%2520for%2520retail/pd-p/01200615320800000172)
* [SAP Fashion Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fashion%2520Management/pd-p/67838200100800006229)

* [Retail

  Industry](/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [SAP ERP add-on for retail

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2Badd-on%2Bfor%2Bretail/pd-p/01200615320800000172)
* [SAP Fashion Management

  SAP Fashion Management](/t5/c-khhcw49343/SAP%2BFashion%2BManagement/pd-p/67838200100800006229)

View products (3)

### **Introduction,**

In this blog post , we will learn steps involved in MSO Process along with Prerequisite.

Purpose -

Your customers may include large corporate groups with many of their own intermediate distribution centers or Ship-to customers depending on them. You can maintain regular business relations with all distribution centers of such a corporation, if the distribution centers and the corporation hold the same functions, for example, as a sold-to customer, a ship-to customer, and a payer.

In addition, you can accommodate orders from a corporation, in which the corporation orders goods for direct delivery to one of the following:

* Ship-to customers: The corporation specifies how many pieces of a certain article each Ship-to customer receives.

* Intermediate distribution center: Here, the distribution center takes over the actual delivery to the final destination of the customers associated with this distribution center. In this case, the distribution center is identical to the corporation or a certain customer. Even in this special case, the corporation specifies the articles and the quantity each customer receives. You flag these deliveries in your warehouse for easy recognition of what and how much each customer is to receive, so that the distribution center can deliver the goods to them as fast as possible.

Note - Configuration is not the part of this blog.

Step 1- Create MSO

MSO order will be the same as standard sales order with enhanced function to leverage multi ship partners with two different types of Partner-

1. mark for

2. Ship to

Partner type is to be selected in Multi Ship to Order Tab and Partner number is to be provided for further actions.

below example has two different partner types with two different Partner number along with their Explosion status.

![](/legacyfs/online/storage/blog_attachments/2023/03/MSO-Order.png)

MSO- Sales Order with Two Partner types

Step - 2

Explode MSO- Create Child Orders

Once MSO is created then through FSH\_MSO,it can be exploded for given Partners and child orders can be created as below-

![](/legacyfs/online/storage/blog_attachments/2023/03/MSO-Report.png)

FSH\_MSO- Explode MSO in Child Orders

Another Sales order as MSO child document will be created with provided information as follow on document from Main MSO.

![](/legacyfs/online/storage/blog_attachments/2023/03/MSO-Child-Order.png)

MSO Child Order- Display

Step- 3

Create Standard Deliveries

![](/legacyfs/online/storage/blog_attachments/2023/03/Delivery-for-Ship-to.png)

Delivery for Ship to Partner

Step - 4

Create Standard Invoice

![](/legacyfs/online/storage/blog_attachments/2023/03/Invoice-Child-Order.png)

Invoice for Child SO

Step - 5

Entire Document flow-

![](/legacyfs/online/storage/blog_attachments/2023/03/Doc-Flow.png)

Entire Document Flow

Please note Process steps could be different for client using Arun for release and optimize Supply chain.

Summary:

This Blog post is to understand MSO process in Retail/FMS system.

Kindly let me know if you have any questions on the same.

For other Retail and Fashion related topic kindly visit :

“<https://community.sap.com/topics/retail>”

For Questions and Answers on Retail kindly visit

“<https://answers.sap.com/tags/99624789925257984685885>”

For other posts on the topic Kindly visit :

<https://blogs.sap.com/tags/99624789925257984685885/>

At last thanks for motivating me for writing Blog post and kindly follow me for more upcoming valuable Blog Posts

Thanks!

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fmulti-ship-to-order-mso-how-to-retail-fms%2Fba-p%2F13555202%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enabling 'Compliance' tab in Purchase order header & Line item in SAP Public cloud](/t5/enterprise-resource-planning-q-a/enabling-compliance-tab-in-purchase-order-header-amp-line-item-in-sap/qaq-p/14234218)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [What Does Each Block Item Control in 'Define Reasons for Blocking in Shipping'?](/t5/enterprise-resource-planning-q-a/what-does-each-block-item-control-in-define-reasons-for-blocking-in/qaq-p/14234203)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [SYS not allow the ship-to party selected](/t5/enterprise-resource-planning-q-a/sys-not-allow-the-ship-to-party-selected/qaq-p/14234164)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [How to Be Linking Commercial Invoices Upload to Sales Orders](/t5/enterprise-resource-planning-q-a/how-to-be-linking-commercial-invoices-upload-to-sales-orders/qaq-p/14234159)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Int4 Suite Agents Empowers Functional Consultants To Test In...