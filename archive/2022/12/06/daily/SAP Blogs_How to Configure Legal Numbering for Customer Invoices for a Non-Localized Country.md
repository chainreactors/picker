---
title: How to Configure Legal Numbering for Customer Invoices for a Non-Localized Country
url: https://blogs.sap.com/2022/12/05/how-to-configure-legal-numbering-for-customer-invoices-for-a-non-localized-country/
source: SAP Blogs
date: 2022-12-06
fetch_date: 2025-10-04T00:34:15.432248
---

# How to Configure Legal Numbering for Customer Invoices for a Non-Localized Country

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to Configure Legal Numbering for Customer Invo...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52685&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Configure Legal Numbering for Customer Invoices for a Non-Localized Country](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-configure-legal-numbering-for-customer-invoices-for-a-non-localized/ba-p/13565242)

![Manjushree96](https://avatars.profile.sap.com/0/9/id098862d625f71e8fc3a5fc74286a8951211b02ef9680cc8a2cd215e49dbf99fe_small.jpeg "Manjushree96")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Manjushree96](https://community.sap.com/t5/user/viewprofilepage/user-id/37976)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52685)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52685)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565242)

‎2022 Dec 05
9:44 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52685/tab/all-users "Click here to see who gave kudos to this post.")

1,052

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)
* [SAP Cloud Applications Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Applications%2520Studio/pd-p/67837800100800006741)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)
* [SAP Cloud Applications Studio

  SAP Cloud Applications Studio](/t5/c-khhcw49343/SAP%2BCloud%2BApplications%2BStudio/pd-p/67837800100800006741)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

This blog outlines Configuring Legal ID in Cloud Application Studio at detailed level over the existing model in SAP Business ByDesign.

Configuration of Legal ID in SAP Business ByDesign solution is outlined as following.

1. The Fine-Tuning activity to maintain “Document Numbering Formats for Customer Invoicing” is accessible in the SAP Business ByDesign, Business Configuration WorkCentre

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture1-6.png)

        2.  This leads to a Document Numbering screen where there are more options of numbering for              various countries. There is an option even for Numbering Formats for Legal ID as highlighted![](/legacyfs/online/storage/blog_attachments/2022/12/Picture2-4.png)

3. The Numbering Formats for Legal ID Business Configuration view enables you to set rules to define ***Numbering formats for Legal IDs in invoicing documents***. You can access this view in the **Business Configuration** WorkCentre **-> Document Numbering Formats for Customer Invoicing** fine tuning activity

***Steps to Configure the Legal ID Numbering Functionality for Customer Invoices:***

1. Create new BC Set for Legal Document Class

In the Solution Explorer, right-click the Business Configuration node and select *Create Business Configuration Set*.The Business Configuration Wizard opens.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture3-3.png)

2.Name and select the type of BC Object

Select *Use SAP Business Configuration Object* as Type of Business Configuration Object. Provide a name and a description for *Legal Document Class* object.

Select name of Business Configuration object as *BusinessTransactionDocumentLegalClassificationCode.* If not present in the drop down, then search for the object using Search button![](/legacyfs/online/storage/blog_attachments/2022/12/Picture4.jpg)

3.Define the Required values

Define the required values in the pop-up for the business configuration set resulting from the *Next* button. Provide values for each column and proceed further with *Next* button![](/legacyfs/online/storage/blog_attachments/2022/12/Picture5.jpg)

4.Review and Finish

On the final page of the wizard, review the summary. *Finish* creating the new BC set. After activation and deployment of your solution, you can see the results in fine-tuning.![](/legacyfs/online/storage/blog_attachments/2022/12/Picture6.jpg)

5.Create new BC set for Legal ID Type.

Follow above steps to create a new BC set for *Legal ID Type*. However, the Business Configuration Object for Legal ID Type is BusinessTransactionDocumentLegalIdentificationTypeCode. Also, define required values for Legal ID type, review and finish the creation of new BC set.![](/legacyfs/online/storage/blog_attachments/2022/12/Picture7.jpg)

6.Access the Fine-Tuning Activity

Now, when you launch *Numbering Formats for Legal ID* from the Fine-Tuning activity to maintain **“Document Numbering Formats for Customer Invoicing”,** the *Legal Document Class* and *Legal ID Type* shall be filled with the values provided in the Business Configuration Sets.

![](/legacyfs/online/storage/blog_attachments/2022/12/4-42.png)

7.**Create new BADI implementation**

1. Create a new solution. In the Solution Explorer, right-click on “Add-on Solution" and **Add New Item.**

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture9-2.png)

       2. Select “**Enhancement Implementation**”![](/legacyfs/online/storage/blog_attachments/2022/12/Picture10-1.png)

3.In create Enhancement implementation screen.Select

Name Space: <http://sap.com/xi/AP/CustomerInvoicing/Global>

Business Object**: CustomerInvoice**.

Enhancement Option: **PDISetLegalClassCode**![](/legacyfs/online/storage/blog_attachments/2022/12/Picture11.jpg)

4.Open the absl file SET\_LEGAL\_CLS\_CODE.absl. In absl file we have parameters InputData of Type UUID, it contains the UUID of the corresponding customer Invoice document. Using the Input Data, you can retrieve PDI enabled content of the corresponding CustomerInvoice and based on the information present in the customer invoice, you can classify the customer invoice as corresponding LegalClass, and accordingly set the result parameter of Type Business Transaction Document Legal Classification Code with the correct LegalClassCode

5.In the file EnhancementImplementation.fltr file, you can mention corresponding country filter for which you need to call this BADI.

**Summary**

Post the Enhancement of Following guide and deploying the add-on will result in additional options as Legal ID Type Fields and Legal Document Class.![](/legacyfs/online/storage/blog_attachments/2022/12/3-53.png)

Please share your feedback or thoughts in the comment section below and follow me for more blogging content on the SAP Business ByDesign.

Follow the below pages for more information:

[SAP Business ByDesign Localization](https://community.sap.com/topics/business-bydesign/localization)

[To post and answer questions on SAP Business ByDesign Localization](https://answers.sap.com/tags/190e64de-834f-49a0-bbba-822...