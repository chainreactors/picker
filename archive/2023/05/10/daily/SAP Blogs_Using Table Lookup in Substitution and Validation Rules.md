---
title: Using Table Lookup in Substitution and Validation Rules
url: https://blogs.sap.com/2023/05/09/using-table-lookup-in-substitution-and-validation-rules/
source: SAP Blogs
date: 2023-05-10
fetch_date: 2025-10-04T11:39:24.393546
---

# Using Table Lookup in Substitution and Validation Rules

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Using Table Lookup in Substitution and Validation ...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/12928&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Table Lookup in Substitution and Validation Rules](/t5/crm-and-cx-blog-posts-by-sap/using-table-lookup-in-substitution-and-validation-rules/ba-p/13552865)

![michael_redmann](https://avatars.profile.sap.com/6/7/id673a5cba402fe2ae9be5e1b6ea149fa52b7f75a6f29008c21f8114282fa11d91_small.jpeg "michael_redmann")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[michael\_redmann](https://community.sap.com/t5/user/viewprofilepage/user-id/297942)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=12928)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/12928)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552865)

‎2023 May 09
10:38 PM

[4
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/12928/tab/all-users "Click here to see who gave kudos to this post.")

3,720

* SAP Managed Tags
* [SAP Treasury and Risk Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Treasury%2520and%2520Risk%2520Management/pd-p/73554900100700001224)
* [Customer Experience](https://community.sap.com/t5/c-khhcw49343/Customer%2520Experience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)

* [SAP Treasury and Risk Management

  Software Product](/t5/c-khhcw49343/SAP%2BTreasury%2Band%2BRisk%2BManagement/pd-p/73554900100700001224)
* [Customer Experience

  Topic](/t5/c-khhcw49343/Customer%2BExperience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)

View products (2)

## How to use table lookup in Substitution and Validation rules

Commodity Price Risk Hedge Accounting Scenario is used as sample.

Prerequisites

* S/4HANA On-Premiss or S/4 private cloud edition

* SAP Fiori launchpad in in place

Following steps need to be run and will be described in the following:

1. Create a Custom Business Object

2. Create a Maintenance View

3. Filling the database table

4. Configuration of Substitution Scenario / Rules by using table lookup

5. Test

6. Conclusion

## **Create a Custom Business Objects**

![](/legacyfs/online/storage/blog_attachments/2023/05/1-11.png)

Create Custom Business Object

Press new button – enter Name ( Fields for Identifier and Plural will be filled automatically ) and press create

![](/legacyfs/online/storage/blog_attachments/2023/05/2-3.png)

New Custom Business Object

Different Features can be selected depending on the need. In normal cases the field for *Can Be Associated* should be selected.

![](/legacyfs/online/storage/blog_attachments/2023/05/3-6.png)

Edit Custom Business Object

Under *Nodes* it can be selected what kind features this Custom Business Object should have. By default, Create, Update and Delete is selected.

![](/legacyfs/online/storage/blog_attachments/2023/05/4-3.png)

The most important part for table lookup is the definition of the fields which will be later used as input and output parameter.

Fields that are marked as key will later be marked as mandatory fields in the table lookup configuration:

* New Fields can be added by pressing NEW button.

* Every Field can have a different type

  + For the different types, the length can be adjusted

* Fields can also be selected as *Read Only*

![](/legacyfs/online/storage/blog_attachments/2023/05/5-5.png)

Edit Custom Business Object III

If needed, different logic definitions can be added by pressing the new button.

![](/legacyfs/online/storage/blog_attachments/2023/05/6-5.png)

Edit Custom Business Object IV

After the configurations are done for the Business Object it must be published by pressing the Publish button.

## **Create a Maintenance View**

How to find the automatically generated Database Table:

Enter to T-Code SM11 and Enter the newly created *Business Object* ***IDENTIFIER*** to field *Data type* and press the button *Display* --> *Content* and from here the automatically generated Database Table name can be find.

![](/legacyfs/online/storage/blog_attachments/2023/05/7-4.png)

Find the automatically generated Database Table

Generate the *Maintenance view* by adding the Database Table name and all the required fields.

Field: SAP\_UUID comes automatically when the feature for *Can Be Associated* is selected.

![](/legacyfs/online/storage/blog_attachments/2023/05/8-6.png)

Generate the Maintenance view

## **Filling Database Table**

Enter to T-Code SM30 and enter the generated Maintenance View to fill up the Database Table with all needed Rules for later usage.

![](/legacyfs/online/storage/blog_attachments/2023/05/Screenshot-2023-05-05-111929.png)

Sample of generated and filled maintenance view

## **Configuration of** **Substitution** **Scenario /** **Rules** **by using table lookup**

Create a Rule Event Based and fill in Subscreen “General Information” the mandatory fields:

* Target Field will be filled automatically with the selected key fields

* Important part here is to select the *Substitution Type* as ***TABLE LOOKUP*** and press the small tiles.

![](/legacyfs/online/storage/blog_attachments/2023/05/9-5.png)

Create a Rule Event Based

Enter search bar the *identifier* of the custom business object and select it. After that fill conditions, source field and press save.

**Note:** Source field is used for Output.

**![](/legacyfs/online/storage/blog_attachments/2023/05/10-5.png)**

Save Rule

Save and activate the rule so it can be ready to use.

**![](/legacyfs/online/storage/blog_attachments/2023/05/11-4.png)**

## Test

You can run transaction **FIN\_RE\_MAINT** testing the table lookup.

Please use one of the events mentioned in image above.

## Conclusion

Using table lookup in Substitution and Validation rules consolidates similar substitution and validation rules in a custom database and reduces the number of rules in the FIORI app "Manage Substitution and Validation Rules".

Labels

* [Technology Updates](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap/label-name/technology%20updates)

* [Commodity Derivative](/t5/tag/Commodity%20Derivative/tg-p/board-id/crm-blog-sap)
* [Commodity Price Risk Hedge Accounting](/t5/tag/Commodity%20Price%20Risk%20Hedge%20Accounting/tg-p/board-id/crm-blog-sap)
* [SAP Commodity Risk Managemen](/t5/tag/SAP%20Commodity%20Risk%20Managemen/tg-p/board-id/crm-blog-sap)
* [Substitution and Validation Rule](/t5/tag/Substitution%20and%20Validation%20Rule/tg-p/board-id/crm-blog-sap)
* [table lookup](/t5/tag/table%20lookup/tg-p/board-id/crm-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-sap%2Fusing-table-lookup-in-substitution-and-validation-rules%2Fba-p%2F13552865%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@E...