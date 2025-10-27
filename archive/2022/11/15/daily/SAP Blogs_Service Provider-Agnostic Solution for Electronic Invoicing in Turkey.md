---
title: Service Provider-Agnostic Solution for Electronic Invoicing in Turkey
url: https://blogs.sap.com/2022/11/14/service-provider-agnostic-solution-for-electronic-invoicing-in-turkey/
source: SAP Blogs
date: 2022-11-15
fetch_date: 2025-10-03T22:45:04.484050
---

# Service Provider-Agnostic Solution for Electronic Invoicing in Turkey

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Service Provider-Agnostic Solution for Electronic ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155137&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Service Provider-Agnostic Solution for Electronic Invoicing in Turkey](/t5/technology-blog-posts-by-sap/service-provider-agnostic-solution-for-electronic-invoicing-in-turkey/ba-p/13542201)

![former_member810647](https://avatars.profile.sap.com/former_member_small.jpeg "former_member810647")

[former\_member810647](https://community.sap.com/t5/user/viewprofilepage/user-id/810647)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155137)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155137)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13542201)

‎2022 Nov 14
10:11 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155137/tab/all-users "Click here to see who gave kudos to this post.")

2,325

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Document and Reporting Compliance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520and%2520Reporting%2520Compliance/pd-p/73554900100700003181)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Document and Reporting Compliance

  Software Product](/t5/c-khhcw49343/SAP%2BDocument%2Band%2BReporting%2BCompliance/pd-p/73554900100700003181)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (4)

### **Introduction**

To date, the eInvoicing solution for Turkey supported only one particular service provider. With this change, it is now possible to integrate with any service provider in Turkey to submit electronic invoices. To integrate with another service provider, it is necessary for the provider to first create a service based on the API definition which has been published on [SAP API Business Hub](https://api.sap.com/api/API_TURKEY_GENERIC_EINVOICE_SERVICE/overview). This API will then be consumed by SAP for eInvoicing. The below eInvoices are supported for this solution.

1. Basic eInvoices

2. Commercial eInvoices

3. Consumer eInvoices

4. Export Registration eInvoices

5. Incoming Basic eInvoices

6. Incoming Commercial eInvoices

Additionally, the following log files have been made available for improved response tracking, which you can access by choosing Goto ->  History in the eDocument Cockpit:

* Response file from a service provider upon successful submission of documents. The file type is **RESP\_SENT**.

* Response file from a service provider upon successful cancellation of consumer invoices. The file type is **RESP\_CANC**.

### **Customizing**

To enable the service provider agnostic solution, you need to configure the below value mappings for the AIF namespace **/EDOTR**

1. **SERVICE\_PROVIDER**

   In this value mapping, you have to indicate your service provider by entering the corresponding eDocument class. Configure the value mapping as follows:

   * + eDocument Class Name: If your service provider is Foriba, enter **`CL_EDOC_TR_SP_FIT`**. If you use any other service provider, enter **`CL_EDOC_TR_SP_GEN`**`,` this will enable the service provider agnostic solution.

     + Internal Value: `SRVCE_PROV.`

2. **SERV\_PROV\_PARAMS**

In this value mapping, you set the parameters that depend on service providers. The below two parameters are supported as of now:

1. 1. 1. **INV\_DOCTYP** - This parameter is used to configure the document type for outgoing eInvoice XMLs as supported by your service provider. The available document types are 'ENVELOPE' or 'INVOICE'.

      2. **PACK\_SIZE** - This parameter is used to control how many incoming documents can be fetched in a single request. This can vary across service providers.

You need to configure the value mapping as follows:

* + - Service Provider-Dependent Parameter: Choose a parameter from the input help. The available parameters include:

      * **INV\_DOCTYP**(Document Type in Outgoing Invoice XML File)

      * **PACK\_SIZE**(Size of Incoming Message Package)

    - Parameter Value: Enter the parameter value.

Please note that this value mapping needs to be configured after discussing it with your service provider, and it is only required if you are using the provider-agnostic solution.

### Integration Flows

![](/legacyfs/online/storage/blog_attachments/2022/09/2022-09-30_16-20-25.png)

The below two new integration flows have been introduced in the package SAP Document and Reporting Compliance: Electronic Invoices and Delivery Notes for Turkey which need to be configured and deployed.

1. Turkey Invoice via Any Service Provider

2. Turkey eArsiv via Any Service Provider

Steps to configure and deploy the integration flows are mentioned in the integration guides attached to the package. Please note that Turkey Invoice via Any Service Provider needs to be configured and deployed even if you are only using the eArsiv solution. These integration flows are available in the latest version of the package.

### Additional Information

If you are using SAP S/4HANA Cloud, then the solution is already available for use with the 2208 release.

If you are an OP customer, please implement the SAP Notes below to receive the solution.

* [3125170](https://launchpad.support.sap.com/#/notes/3125170) - eDocument Turkey - eInvoice - Service Provider-Agnostic Solution: Pre-Requisite Objects

* [3219903](https://launchpad.support.sap.com/#/notes/3219903) - eDocument Turkey - Service Provider-Agnostic Solution for eInvoice: Proxy objects

* [3134407](https://launchpad.support.sap.com/#/notes/3134407) - eDocument Turkey - eInvoice: Service Provider-Agnostic Solution (Basic Solution)

* [3129528](https://launchpad.support.sap.com/#/notes/3129528) - eDocument Turkey - eInvoice: Service Provider-Agnostic Solution (Full Solution)

* [3249682](https://launchpad.support.sap.com/#/notes/3249682) - eDocument Turkey - eInvoice - Service Provider-Agnostic Solution: AIF Customizing (SAP ERP)

* [3249773](https://launchpad.support.sap.com/#/notes/3249773) - eDocument Turkey - eInvoice - Service Provider-Agnostic Solution: AIF Customizing (SAP S/4HANA)

If you are a service provider looking to support eInvoicing solution, then you can visit the API package [SAP Document and Reporting Compliance: Electronic Documents for Turkey](https://api.sap.com/package/SAPDocumentandReportingComplianceElectronicDocumentsforTurkey/soap). The API definition for eInvoicing can be found under the ...