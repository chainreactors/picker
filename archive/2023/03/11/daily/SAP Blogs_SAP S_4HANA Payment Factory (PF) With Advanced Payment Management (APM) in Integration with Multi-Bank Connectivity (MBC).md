---
title: SAP S/4HANA Payment Factory (PF) With Advanced Payment Management (APM) in Integration with Multi-Bank Connectivity (MBC)
url: https://blogs.sap.com/2023/03/10/sap-s-4hana-payment-factory-pf-with-advanced-payment-management-apm-in-integration-with-multi-bank-connectivity-mbc/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:41.304273
---

# SAP S/4HANA Payment Factory (PF) With Advanced Payment Management (APM) in Integration with Multi-Bank Connectivity (MBC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* SAP S/4HANA Finance For advanced payment managemen...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4901&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Finance For advanced payment management in Integration with SAP Multi-Bank Connectivity](/t5/supply-chain-management-blog-posts-by-members/sap-s-4hana-finance-for-advanced-payment-management-in-integration-with-sap/ba-p/13567445)

![](/skins/images/7415135DAF38A9CE6CA9238912367291/responsive_peak/images/icon_anonymous_profile.svg)

Former Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4901)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4901)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567445)

‎2023 Mar 10
9:52 PM

[25
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4901/tab/all-users "Click here to see who gave kudos to this post.")

35,085

* SAP Managed Tags
* [Banking](https://community.sap.com/t5/c-khhcw49343/Banking/pd-p/131623764915182240635655)
* [banking services from SAP](https://community.sap.com/t5/c-khhcw49343/banking%2520services%2520from%2520SAP/pd-p/01200615320800000685)
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)
* [SAP Multi-Bank Connectivity](https://community.sap.com/t5/c-khhcw49343/SAP%2520Multi-Bank%2520Connectivity/pd-p/67837800100800004307)
* [SAP Payment Approvals](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payment%2520Approvals/pd-p/01200615320800003828)
* [SAP Payment Engine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payment%2520Engine/pd-p/01200615320800001129)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [Banking

  Industry](/t5/c-khhcw49343/Banking/pd-p/131623764915182240635655)
* [banking services from SAP

  banking services from SAP](/t5/c-khhcw49343/banking%2Bservices%2Bfrom%2BSAP/pd-p/01200615320800000685)
* [SAP Multi-Bank Connectivity

  SAP Multi-Bank Connectivity](/t5/c-khhcw49343/SAP%2BMulti-Bank%2BConnectivity/pd-p/67837800100800004307)
* [SAP Payment Approvals

  SAP Payment Approvals](/t5/c-khhcw49343/SAP%2BPayment%2BApprovals/pd-p/01200615320800003828)
* [SAP Payment Engine

  SAP Payment Engine](/t5/c-khhcw49343/SAP%2BPayment%2BEngine/pd-p/01200615320800001129)
* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)

View products (7)

Advanced payment management(APM) allows you to centralize all payment activities of a corporate group. Advanced payment management supports five payment scenarios: Internal payments, payments ‘in name of’ with forwarding only, payments ‘in name of’ with routing optimization, payments 'on behalf of' and central incoming payments.

It integrates with other areas within SAP S/4HANA such as In- House Bank, In-House Cash,  Cash Management, Bank Communication Management, Bank Account Management and General Ledger.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03-08_171525088.png)

Source: SAP

As organizations scale up, there is significant increase in payment volumes and hence need to automate, streamline, optimize the end-to-end payment process across the entire group. Headquarter need the centralization of the payment approval and monitoring for subsidiaries by using a single source of truth. They need the ability to handle different payment formats centrally and automate the routing of payments to different financial institutes.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03-08_171648974.png)

Source: SAP

The system uses Bank Account Management to determine the bank account to be used, triggers approval through Bank Communication Management and once approved creates the external medium for transmission to the bank using Multi Bank Connectivity.

SAP S/4HANA Finance for advanced payment management provides centralized payment factory to manage payments from various systems – SAP, non-SAP and manual payments.

In this blog we are majorly focusing on the scenario payments ‘in name of’ with forwarding only and its basic configuration.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03-08_171841245.png)

Source: SAP

In this scenario, we want to consume a file based payment instruction in advanced payment management and send it to the bank via Multi-Bank Connectivity.

In the following I will describe the available configuration which is used for this scenario as well as the master data which needs to be created to support the scenario.

**Define Clearing Areas**

SPRO-->Financial Supply Chain Management-->Advanced Payment Management-->Basic Configuration-->Organization-->Define Clearing Areas

Clearing areas act as an org object under the client level. Users working in one clearing area do not have access to data in other clearing areas. One clearing Area we can make work for multiple company codes with different currencies.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03-08_174055394.png)

**Maintain Generic Number Ranges**

SPRO-->Financial Supply Chain Management-->Advanced Payment Management-->Basic Configuration--> Maintain Generic Number Ranges

The number range numbers are assigned to diverse number range objects in advanced payment management. A number range object is uniquely identified by its name, and you can assign a number range number starting with 01 and an end value of 99.

With the number range numbers defined here you can customize the number ranges for the following objects:

* /PF1/COLL: Number Range Object for Collectors > Not used in the Project.

* /PF1/CSTID: Customer IDs for service level agreements > Not used in the Project.

* /PF1/FH\_OL: Number Range Object List Number (Secondary Key)

* /PF1/PO\_PI: Number range for Payment Transactions (Secondary Key)

* /PF1/PO\_PO: Number range for Payment Order (Secondary Key)

* /PF1/PO\_RE: Number range Object for Recalls > not used in this Project.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03-08_174322895.png)

**Maintain Number Ranges for Payment Orders**

SPRO-->Financial Supply Chain Management-->Advanced Payment Management--> Payment Processing--> Business Objects--> Payment Order--> Maintain Number Ranges for Payment Orders

A clearing area always requires a payment order number range before payment orders can be processed in that clearing area. The payment order number is then populated in the Input Manager. You create a payment order number range for payment orders and define whether or not the payment order number is assigned internally by the system.

![](/legacyfs/online/storage/blog_attachments/2023/03/image_2023-03...