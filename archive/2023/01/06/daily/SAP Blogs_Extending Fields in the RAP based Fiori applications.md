---
title: Extending Fields in the RAP based Fiori applications
url: https://blogs.sap.com/2023/01/05/extending-fields-in-the-rap-based-fiori-applications/
source: SAP Blogs
date: 2023-01-06
fetch_date: 2025-10-04T03:09:33.292539
---

# Extending Fields in the RAP based Fiori applications

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Extending Fields in the RAP based Fiori applicatio...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162454&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extending Fields in the RAP based Fiori applications](/t5/technology-blog-posts-by-members/extending-fields-in-the-rap-based-fiori-applications/ba-p/13563970)

![VijayCR](https://avatars.profile.sap.com/5/d/id5dec9917d1d4a6afdb1c924dc1f0d19cccdfabf28cb31d70a37ff6e8b182bcc2_small.jpeg "VijayCR")

[VijayCR](https://community.sap.com/t5/user/viewprofilepage/user-id/38084)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162454)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162454)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563970)

‎2023 Jan 05
7:56 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162454/tab/all-users "Click here to see who gave kudos to this post.")

10,120

* SAP Managed Tags
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (1)

Hello SAP Experts,

Field Extensions in a Fiori Applications is the most common requirements in many S/4 HANA projects. However this blog will focus on the RAP based Standard Fiori app Extensions for the Custom /Standard Fields.

The below flow charts will illustrate the different decisions and possibilities in extending the custom fields/standard for a RAP based Fiori applications

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-7.png)

RAP Custom Field Extension

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-5.png)

*RAP Custom Field Extension*

**Custom field extension for a Managed Scenario :**

Let us extend a custom field for the below Fiori application .

<https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F4710')/S24OP>

* As per the above flow chart check if there is any business context available for this application ,if found create a custom field as shown below and enable the  app context in any available

![](/legacyfs/online/storage/blog_attachments/2023/01/Custom-Standard-Field-In-App-Managed.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Custom-Standard-Field-In-App-Managed3.png)

Enable the Application in scope

![](/legacyfs/online/storage/blog_attachments/2023/01/Custom-Standard-Field-In-App-Managed2.png)

Publish the custom field

* Now go and Verify the CDS Entity if the Extended Custom field is visible as a CDS extension ?

* Navigate to the CDS View entity from the Service Binding UI\_PROMISETOPAY\_MANAGE

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-8-1.png)

CDS extension is generated

![](/legacyfs/online/storage/blog_attachments/2023/01/Custom-Standard-Field-In-App-Managed4-1.png)

* Now verify if the field is available in the Fiori application Manage Promises to Pay

![](/legacyfs/online/storage/blog_attachments/2023/01/Custom-Standard-Field-In-App-Managed5.png)

Thus you can extend the custom field in Managed scenario of RAP

**Standard field Extension in an Un Managed Scenario :**

Let us extend the below Un-Managed Application Process Receivables ( Version 2 )

<https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F0106A')/S24OP>

Let us try to add some additional fields which are missing in the below Invoices tab in the object page of the application :

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-9.png)

* Now let us verify the CDS Entity behind the Invoices tab and extend it with the missing standard field as shown in the below example![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed1.png)

* ```
  extend view entity R_CollectionsInvoiceTP with

  {

    _OperationalAcctgDocItem.PaymentTerms as paymenterms

  }

  ​
  ```

* Now lets test if this CDS extension works in case of Un-Managed Scenario . As we see below the field is extended however the value is filled as empty as this is a implemented via a query class .

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed2-1.png)

and the Fiori app is extended now to show the standard field

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed6.png)

* Now let us verify if this is a dynamic or a static/BAPI call in the query class to fetch the data .

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed5.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed3.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed4.png)

* From the above screenshots its evident that the query is class is using a CDS view P\_COLLECTIONSINVOICEMEMORY to fetch the data and fill the fields  that is the reason why table [@RT](/t5/user/viewprofilepage/user-id/30203)\_Data is not filled with data even tough the custom entity shown the field .

* Next step is extend the P\_COLLECTIONSINVOICEMEMORY CDS view to get the payment terms field .

```
@AbapCatalog.sqlViewAppendName: 'ZI_invmem'

@EndUserText.label: 'CDS Extension for Invoice'

extend view I_CollectionsInvoiceMemory with Zi_collinvmem

{

_OperationalAcctgDocItem.PaymentTerms as PaymentTerms

}
```

```
@AbapCatalog.sqlViewAppendName: 'zp_collext'

@EndUserText.label: 'CDS Extension for Invoice'

extend view P_CollectionsInvoiceMemory with ZP_coll_Ext

{

PaymentTerms

}
```

After Extended the Query CDS view with the required field now the Fiori Application shows the values during the execution after refresh :

![](/legacyfs/online/storage/blog_attachments/2023/01/Standard-Field-In-App-Un-Managed7-1.png)

Thus you can extend RAP based application for both custom /standard fields for both Managed and Un-managed scenarios

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fextending-fields-in-the-rap-based-fiori-applications%2Fba-p%2F13563970%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  6 ...