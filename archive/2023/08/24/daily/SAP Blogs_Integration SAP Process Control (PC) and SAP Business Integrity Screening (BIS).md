---
title: Integration SAP Process Control (PC) and SAP Business Integrity Screening (BIS)
url: https://blogs.sap.com/2023/08/23/integration-sap-process-control-pc-and-sap-business-integrity-screening-bis/
source: SAP Blogs
date: 2023-08-24
fetch_date: 2025-10-04T12:00:46.327909
---

# Integration SAP Process Control (PC) and SAP Business Integrity Screening (BIS)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* GRC Tuesdays: Hidden Gems. Integration between SAP...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5456&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [GRC Tuesdays: Hidden Gems. Integration between SAP Process Control (PC) and SAP Business Integrity Screening (BIS)](/t5/financial-management-blog-posts-by-members/grc-tuesdays-hidden-gems-integration-between-sap-process-control-pc-and-sap/ba-p/13581354)

![valentynchapnyi](https://avatars.profile.sap.com/8/4/id8407fef5839f554ab29cc6ea752828dd3bd9ef53230d808aa5e1bb1e75a386a5_small.jpeg "valentynchapnyi")

[valentynchapnyi](https://community.sap.com/t5/user/viewprofilepage/user-id/157312)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5456)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5456)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581354)

‎2023 Aug 23
11:18 PM

[2
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5456/tab/all-users "Click here to see who gave kudos to this post.")

2,039

* SAP Managed Tags
* [Governance, Risk, Compliance (GRC) and Cybersecurity](https://community.sap.com/t5/c-khhcw49343/Governance%252C%2520Risk%252C%2520Compliance%2520%28GRC%29%2520and%2520Cybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

* [Governance, Risk, Compliance (GRC) and Cybersecurity

  Product Category](/t5/c-khhcw49343/Governance%25252C%2BRisk%25252C%2BCompliance%2B%252528GRC%252529%2Band%2BCybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

View products (1)

The SAP GRC Products pallet is designed to function as an integrated solution, but at times, its not a simple task to locate the right tool for a specific business process or function. Additionally, some enterprises may own applications licenses which “lying on the shelf”. An example of this is the integration capabilities between SAP Process Control (PC) and SAP Business Integrity Screening (BIS), where both tools can complement each other's strengths, allowing for a healthier control management process.

The integration of SAP Process Control (PC) and SAP Business Integrity Screening (BIS) provides following opportunities. While SAP PC is widely used for managing Internal Controls Framework, it can be extended with the automation capabilities of SAP BIS. For instance, BIS, with its HANA DB based detection system, can efficiently identify anomalies and irregularities, effectively functioning as a screening tool to detect fraudulent activities or system misuse by users. Furthermore, the integration allows seamless automation of controls, significantly reducing overload of manual validation and sampling approaches.

Let’s dive a bit deeper into both tools and review the case with example of control for duplicated invoices. This control is a crucial aspect of cash flow for most organizations, but the high volume of invoices received per month can lead to gaps in manual validation.

I also chose the example of duplicated invoices control because it is part of the business content package delivered by SAP, offering a predefined set of controls for organizations. To identify duplicated invoices from vendors, a combination of suggested indicators is used for validation:

* **Fuzzy Search**: The system employs fuzzy search algorithms to find similar reference numbers across different invoices, helping to identify potential duplicates.

* **Similar Amounts**: By checking for similar amounts based on a percentage range, the system can flag invoices that bear striking resemblances, indicating potential duplicates.

* **Payment Bank Details**: Even if vendors are different, the system examines whether the payment bank details are the same, which can reveal fraudulent activities or irregularities.

* **Vendor Name Comparison**: Comparing vendor names on different invoices aids in detecting potential duplicate transactions involving the same vendor.

* **Exclude Reversed Bookings**: Documents with reversed bookings are excluded from the analysis, ensuring a more accurate identification of potential duplicate invoices.

SAP Business Integrity Screening (BIS) constantly monitors invoices from source systems, including both SAP and non-SAP applications. When potential duplicates are detected, an alert is generated. The alert is then thoroughly investigated and assigned one of the following statuses: Confirmed (indicating a genuine duplicated invoice) or False Alarm (indicating that the flagged invoice is not a duplicate).

By incorporating these indicators and integrating BIS with PC, organizations can significantly improve their ability to detect and manage duplicated invoices, reducing the risk of financial loss and ensuring more robust control over financial processes.

Integration.

The integration process between SAP Process Control (PC) and SAP Business Integrity Screening (BIS) involves the following steps:

![](/legacyfs/online/storage/blog_attachments/2023/08/Automated-control-workflow.png)

WorkFlow

* All master data related to control is maintained in PC

* Control is linked to “Business rule” that reads confirmed alerts from BIS

* When a confirmed duplicate invoice is detected by BIS, an issue is automatically created in PC and sent to the control owner's work inbox.

Alert in BIS with “Confirmed” status:

![](/legacyfs/online/storage/blog_attachments/2023/08/Confirmed-alert-in-BIS.png)

Confirmed alert

Issue in PC:

![](/legacyfs/online/storage/blog_attachments/2023/08/Issue-in-PC.png)

Issue

* The control owner creates a remediation plan and assigns it to the responsible individual (e.g., Financial Analyst).

* The Financial Analyst performs the necessary steps following the remediation plan.

* Once the remediation is completed, the Financial Analyst submits the issue back to the control owner for validation and closure.

Summary.

In summary, the integration of SAP Process Control (PC) and SAP Business Integrity Screening (BIS) empowers organizations using SAP to effectively manage high amounts of data, ensuring swift and accurate processing. SAP PC cannot be replaced in master data management, while BIS offers a data processing engine with HANA DB tools like "fuzzy search" and "predictive analytics." By combining these applications, organizations can implement the best of both worlds, achieving comprehensive controls management and leveraging BIS's powerful capabilities to detect anomalies and irregularities across SAP and non-SAP applications.

* [GRCTuesdays](/t5/tag/GRCTuesdays/tg-p/board-id/financial-management-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-m...