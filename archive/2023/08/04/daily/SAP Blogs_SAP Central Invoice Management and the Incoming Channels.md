---
title: SAP Central Invoice Management and the Incoming Channels
url: https://blogs.sap.com/2023/08/03/sap-central-invoice-management-and-the-incoming-channels/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:38.963251
---

# SAP Central Invoice Management and the Incoming Channels

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Central Invoice Management and the Incoming Ch...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53912&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Central Invoice Management and the Incoming Channels](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-central-invoice-management-and-the-incoming-channels/ba-p/13574079)

![LouayAbuomar](https://avatars.profile.sap.com/9/9/id99e37d77792b3f687c0bcc82c9aa54e84e9ff7fc90ce8f72364866a4ba831f6a_small.jpeg "LouayAbuomar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[LouayAbuomar](https://community.sap.com/t5/user/viewprofilepage/user-id/658653)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53912)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53912)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13574079)

‎2023 Aug 03
7:35 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53912/tab/all-users "Click here to see who gave kudos to this post.")

2,512

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP S/4HANA Cloud Public Edition Sourcing and Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sourcing%2520and%2520Procurement/pd-p/a906d110-8210-4641-9e54-4744b42f06d0)
* [SAP Business Network for Procurement and SAP Business Network for Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Procurement%2520and%2520SAP%2520Business%2520Network%2520for%2520Supply%2520Chain/pd-p/67838200100800005701)
* [SAP Ariba Central Invoice Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Central%2520Invoice%2520Management/pd-p/73554900100800002863)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP S/4HANA Cloud Public Edition Sourcing and Procurement

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSourcing%2Band%2BProcurement/pd-p/a906d110-8210-4641-9e54-4744b42f06d0)
* [SAP Business Network for Procurement and SAP Business Network for Supply Chain

  SAP Business Network for Procurement and SAP Business Network for Supply Chain](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BProcurement%2Band%2BSAP%2BBusiness%2BNetwork%2Bfor%2BSupply%2BChain/pd-p/67838200100800005701)
* [SAP Ariba Central Invoice Management

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BCentral%2BInvoice%2BManagement/pd-p/73554900100800002863)

View products (4)

Accounts Payable organizations often face challenges in processing incoming invoices that arrive in various formats. While many customers have benefited from the automation provided by the Business Network, there is still a significant percentage of invoices that arrive manually, either through emails or traditional mail. At SAP, we recognize this challenge and have dedicated considerable attention to developing **SAP Central Invoice Management** to address these invoice incoming channels. Here are the key features:

+ Integrating **SAP Central Invoice Management** with the SAP Business Network: This integration empowers customers to leverage the full potential of the SAP Business Network, enabling them to send invoices directly to their buyers through the network. Suppliers can also integrate their backend systems with SAP Business Network to efficiently track generated invoices against received orders. This is a roadmap item so stay tuned for upcoming developments on this [roadmap](https://roadmaps.sap.com/board?range=FIRST-LAST&PRODUCT=73554900100800002863#Q3%202023).

+ File extraction from email: Many companies receive supplier invoices in different formats (e.g., PDF, JPEG, PNG, and TIFF) as file attachments to emails. Currently, Accounts Payable clerks or Shared Services Center employees must manually process these emails, save the invoice files into specific folders, and then manually upload them to SAP Central Invoice Management to create Supplier Invoices. This process is time-consuming and requires significant effort. To streamline this process, we have introduced an IRPA Bot that automatically uploads supplier invoice files to **SAP Central Invoice Management**. The bot scans incoming emails to extract supplier invoice files based on accepted formats and automatically uploads them to **SAP** **Central Invoice Management** system for further processing.

![](/legacyfs/online/storage/blog_attachments/2023/08/Screenshot-2023-08-02-at-12.49.44-PM.png)

+ Structured Data Inbound: We will introduce an API aimed at simplifying the invoice creation process by enabling the direct transmission of structured supplier invoice data. This eliminates the requirement for processing readable documents using techniques an OCR. Furthermore, this feature offers the option of receiving the original electronic invoice as an attachment, according to your preference. This is a roadmap item so stay tuned for upcoming developments on this [roadmap](https://roadmaps.sap.com/board?range=FIRST-LAST&PRODUCT=73554900100800002863#Q3%202023).

+ Manual upload: For invoices that were not transferred through the automated channels mentioned above, the "upload invoices" application allows end-users to manually upload invoices. The system then transforms these invoices into structured formats, making it possible to store them in **SAP** **Central Invoice Management**.

At SAP, we continuously strive to improve and simplify the invoice management process to enhance efficiency and accuracy for our customers.

Additionally, I would like to invite you to explore our previous blogs that showcase the exciting innovations introduced in Central Invoice Management. To access these informative resources, please follow these links: [Astrid Luckart Blog](https://blogs.sap.com/2023/05/24/sap-central-invoice-management-key-innovations-2305-release/), and [Roxana Craciun Blog](https://blogs.sap.com/2023/05/04/sap-central-invoice-management/).

By following my profile, you can stay informed about future releases and updates on **SAP Central Invoice Management**. Don't miss out on the latest advancements that can revolutionize your financial processes.

**For more information on SAP Central Invoice Management, check out the following links:**

+ [SAP Procurement Release Readiness Community](https://community.sap.com/topics/intelligent-spend-management/release-readiness-procurement) for release information

+ Help Portal Product Page for [SAP Central Invoice Management](https://help.sap.com/docs/CENTRAL_INVOICE_MANAGEMENT)

+ [SAP Central Invoice Management Overview blog](https://blogs.sap.com/2023/05/04/sap-central-invoice-mana...