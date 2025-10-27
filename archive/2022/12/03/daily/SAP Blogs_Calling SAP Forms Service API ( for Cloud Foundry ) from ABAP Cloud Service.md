---
title: Calling SAP Forms Service API ( for Cloud Foundry ) from ABAP Cloud Service
url: https://blogs.sap.com/2022/12/02/calling-sap-forms-service-api-for-cloud-foundry-from-abap-cloud-service/
source: SAP Blogs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:32.752415
---

# Calling SAP Forms Service API ( for Cloud Foundry ) from ABAP Cloud Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Calling SAP Forms Service API ( for Cloud Foundry ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162781&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Calling SAP Forms Service API ( for Cloud Foundry ) from ABAP Cloud Service](/t5/technology-blog-posts-by-members/calling-sap-forms-service-api-for-cloud-foundry-from-abap-cloud-service/ba-p/13565651)

![parichaypatra](https://avatars.profile.sap.com/6/3/id633c8281c633b969123db8083493cba295e81fc0fc312f1023ca644178078ce8_small.jpeg "parichaypatra")

[parichaypatra](https://community.sap.com/t5/user/viewprofilepage/user-id/44865)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162781)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162781)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565651)

‎2022 Dec 02
9:52 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162781/tab/all-users "Click here to see who gave kudos to this post.")

2,983

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (4)

Hello everyone. The purpose of this document is to shed some light on the process to call Adobe Forms Service API (for Cloud Foundry environment) from ABAP cloud. It sometimes becomes very confusing because of the different components involved especially when you are implementing the ABAP part.

Let’s begin with the prerequires first. We need: -

* SAP BTP CF Environment

* Forms Service by Adobe (You must have a valid license; it is not free).

* SAP Destination Service

* Adobe Live Cycle Designer

* ABAP Cloud Service

Here in this blog, I shall mostly focus on the backend part and so to proceed, you need to create an application from which you will call the API.

Once done, let us follow the steps we are discussing here.

**Create a destination in BTP**

We have created an instance of the Adobe Form Service and created the service key. The details from the service key will be needed to create the cloud destination.

Please refer below configuration to set up the destination.

Service Instance name: ‘ADOBE\_FORMS\_SRV\_CF’

Destination Name: ‘ADOBE\_FORMS\_DEST\_CF’

<Type>: ‘**HTTP’**

<Proxy Type>: ‘**Internet’**

<Authentication>: ‘**OAuth2ClientCredentials’**

<URL>: Value of Rest API URL

<Client ID>: Value of **clientid** in the service key

<Client Secret>: Value of **clientsecret** in the service key

*<Token* Service User>: Value of **clientid** in the service key

<Token Service Password>: Value of **clientsecret** in the service key

<Token Service URL> : Value of XSUAA <url> in the service key followed by /**oauth/token?grant\_type=client\_credentials**

( For me it is something like below:- <https://<xyzabcd>.authentication.us10.hana.ondemand.com/oauth/token?grant_type=client_credentials> )

![](/legacyfs/online/storage/blog_attachments/2022/12/n1.png)

*Point to be noted:* ‘/oauth/token?grant\_type=client\_credentials’ is required for successful authentication.

Additional Property: -

scope: **generate-ads-output**

trustall: **true**

![](/legacyfs/online/storage/blog_attachments/2022/12/n2.png)

Testing the configuration.

![](/legacyfs/online/storage/blog_attachments/2022/12/n3.png)

**Create a Communication Arrangement for ABAP Service**

We also need a communication arrangement using scenario **SAP\_COM\_0503**. You can refer [help.sap ( Communication Arrangement for Forms Service )](https://help.sap.com/docs/CP_FORMS_BY_ADOBE/dcbea777ceb3411cb10500a1a392273e/265dfc44ab754ac19da5cd3ada856cee.html#create-a-communication-arrangement) for details of this configuration.

**Call the API from ABAP**

Now we will create the implementation of the backend logic (in ABAP ) to call the rest api.

I have created a transformation in ABAP to convert the data into XML in a predefined format. Field names are kept same in data model, transformation and xdp template in Adobe Live Cycle Designer.

![](/legacyfs/online/storage/blog_attachments/2022/12/n4.png)

Now we have three major steps to follow.

**Create the request object instance** and for this, we need the destination, uri of API  and other details like query parameter and header details of the request.

![](/legacyfs/online/storage/blog_attachments/2022/12/n5.png)

**Note**: The API endpoint will be different for Neo Environment. Please check API Hub for API Endpoint for Neo.

**Prepare the data and convert it to XML via transformation.**

![](/legacyfs/online/storage/blog_attachments/2022/12/n6.png)

**Build the template and then call API.**

![](/legacyfs/online/storage/blog_attachments/2022/12/n7.png)Here, few things to notice.

* **XDP Template** is <Form\_Name>/<Template\_Name>. It is the name of the document when you download it from Template Store.

* **Form Type** has to be one of three options available (i.e interactive, print, dynamicInteractive).

**Interactive:** Editable Forms

**Print:** Non-Editable Forms

**Dynamicinteractive:** Editable Forms + Freely Expandable Sections.

*Below code sample is written by me for demo purpose and not for productive environment*.

```
CLASS zdmo_ads_assistance DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

    TYPES: BEGIN OF ty_doc,

             docnum(10)   TYPE c,

             docchild(10) TYPE c,

           END OF ty_doc,

           ts_docs TYPE ty_doc,

           BEGIN OF struct,

             xdp_template TYPE string,

             xml_data     TYPE string,

             form_type    TYPE string,

             form_locale  TYPE string,

             tagged_pdf   TYPE string,

             embed_font   TYPE string,

           END OF struct,

           BEGIN OF ty_header,

             DocumentNumber(10)    TYPE c...