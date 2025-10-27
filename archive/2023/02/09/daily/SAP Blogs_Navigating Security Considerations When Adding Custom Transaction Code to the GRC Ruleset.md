---
title: Navigating Security Considerations When Adding Custom Transaction Code to the GRC Ruleset
url: https://blogs.sap.com/2023/02/08/navigating-security-considerations-when-adding-custom-transaction-code-to-the-grc-ruleset/
source: SAP Blogs
date: 2023-02-09
fetch_date: 2025-10-04T06:07:29.346672
---

# Navigating Security Considerations When Adding Custom Transaction Code to the GRC Ruleset

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Navigating Security Considerations When Adding Cus...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5386&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Navigating Security Considerations When Adding Custom Transaction Code to the GRC Ruleset](/t5/financial-management-blog-posts-by-members/navigating-security-considerations-when-adding-custom-transaction-code-to/ba-p/13562259)

![debashish-sarma](https://avatars.profile.sap.com/8/2/id8201317f3f28f1aeaaeab275ce12d31aec878d6c935754f5fbf6d5e9e834c3ba_small.jpeg "debashish-sarma")

[debashish-sarma](https://community.sap.com/t5/user/viewprofilepage/user-id/592607)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5386)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5386)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562259)

‎2023 Feb 08
4:07 PM

[5
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5386/tab/all-users "Click here to see who gave kudos to this post.")

6,622

* SAP Managed Tags
* [SAP Access Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Access%2520Control/pd-p/01200615320800000796)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [SAP Access Control

  SAP Access Control](/t5/c-khhcw49343/SAP%2BAccess%2BControl/pd-p/01200615320800000796)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/02/CB50A872-FAF4-4E35-B925-E1E43D641A42.jpeg)*\*image1*

**Introduction:** Businesses are always evolving their operations to keep up with the needs of the market. More often than not, special requirements arise that require customized coding to meet the business needs. SAP customers may implement special coding through ABAP language (in the form of a custom transaction) to add new functions to the system that are not available on the standard platform. As a result, they can unintentionally create security loopholes that make SAP environments susceptible to cyber attacks. An efficient ABAP code for a custom transaction must contain elements that can protect against security threats such as hard coded user and password, sod risk relevance, sap non-compliance ABAP coding, etc. Subsequently, it must be determined whether such custom transactions need to be included in SoD risk matrix.

This blog is more of a checklist which discusses the key considerations you should make prior to adding a custom transaction code to a ruleset in GRC, to ensure that your system remains safe and secure, and risks are accurately monitored while operating at maximum efficiency.

**Assumptions:** You are familiar with configuring SOD functions and risks in SAP GRC ruleset, or have a basic understanding of it.

**Analyzing Custom Transactions from a Security Point-of-view:**

**a)** First things first, always ensure to have a thorough look at the Functional Specification (FS) and/or Technical Specification (TS) documents to get a clear understanding of the custom transaction and its functionalities.

**b)** Check if the program developed for the custom transaction code has the AUTHORITY-CHECK statements to protect the data and business logic along with the return code (SY-SUBRC) logic. Return logic is used to return the transaction to a consistent state when access is denied to a user. Below is an example of an AUTHORITY-CHECK statement with the return logic in a standard SAP program:![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-27.png)

The program associated with a custom transaction can also be identified in the following ways:

* Using transaction code SE93. Below is an example of a standard SAP transaction SU01 and its associated program from SE93 screen.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-12.png)

* Using SAP table TSTC. Please note that there might be situations when TSTC doesn’t provide the mapping of transaction code to program. It is because for programs that have been assigned a transaction code that uses a start object of “Transaction with parameters”, the program name is in the parameters. For these transactions, PGMNA in table TSTC will be blank. The additional information that links the program name to the transaction code is found in table TSTCP (Parameters for Transactions).

**c)** Ensure that the SU24 configuration is performed and contains all the authorization objects that are being called in the Program Code. Verify the same using the program “RS\_ABAP\_SOURCE\_SCAN”.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture3-10.png)

Repeating the obvious fact, authorization objects with Check Indicator as “Check” and Proposal value as “Yes” in SU24, will get automatically added to the PFCG roles when the corresponding transaction is added to the Role Menu. Ensure these objects are included in AUTHORITY-CHECK statements of the custom program.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-11.png)

**d)** It is recommended to run the transaction on your own in the Development or Test environment, just to validate it works in the same manner as mentioned in the Functional Specification document and to rule out any untoward exceptions.

**e)** Determine if the custom transaction is updating records in a specific table in SAP or it is just a report transaction. Based on this sensitivity analysis, it can be decided whether the custom transaction needs to be included in the SOD matrix or not.

**f)** Fiori Launchpad over time has emerged as the primary interface for users, hence, it is necessary to check if there is any Fiori app associated with the custom transaction that has been configured to make it accessible in the Fiori launchpad, which in turn will have to be added to the SOD matrix.

If you are interested to know more on how to incorporate Fiori apps and services in the SOD ruleset, please refer to the SAP Blog: [https://blogs.sap.com/2021/07/12/how-to-incorporate-sap-fiori-appfapp-and-servicesvc-in-the-ruleset....](https://blogs.sap.com/2021/07/12/how-to-incorporate-sap-fiori-appfapp-and-servicesvc-in-the-ruleset./)

**g)** It is also recommended to check with your System Administrator Team (BASIS Team) to carry out a performance analysis on the custom transaction code in order to avoid any potential system performance issue.

**h)** By this time, we must have identified the business process associated with the custom transaction and the functionality it enables in the system. Next step is to search for the best fit SOD function in GRC so that the custom transaction, its permissions along with the Fiori app and services (if any) can be added to it. If no suitable match can be found, better to create a new SOD function and then map it to the risk with which it is conflicting. Of course, this has to be done...