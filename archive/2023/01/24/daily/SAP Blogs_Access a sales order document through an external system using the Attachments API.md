---
title: Access a sales order document through an external system using the Attachments API
url: https://blogs.sap.com/2023/01/23/access-a-sales-order-document-through-an-external-system-using-the-attachments-api/
source: SAP Blogs
date: 2023-01-24
fetch_date: 2025-10-04T04:38:54.510459
---

# Access a sales order document through an external system using the Attachments API

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Access a sales order document through an external ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50096&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Access a sales order document through an external system using the Attachments API](/t5/enterprise-resource-planning-blog-posts-by-sap/access-a-sales-order-document-through-an-external-system-using-the/ba-p/13548268)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50096)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50096)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548268)

‎2023 Jan 23
10:58 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50096/tab/all-users "Click here to see who gave kudos to this post.")

4,039

* SAP Managed Tags
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)

View products (4)

In this blog post, I would like to walk you through how you can access a sales order document SAP S/4HANA Cloud from an external system using the functionality of the *[Attachments](https://api.sap.com/api/API_CV_ATTACHMENT_SRV/overview)* API. To demonstrate the behavior of the API calls, I’ll be using Postman.

**Prerequisites**:

* You have setup the necessary communication arrangement along with a communication user with the necessary permissions to access the sales order document. Please refer to the following [blog](https://blogs.sap.com/2017/11/09/setting-up-communication-management-in-sap-s4hana-cloud/) to see how this is done.

  + \* The blog shows the process for the “Puchase Order intregration” communication scenario. Make sure you create a communication scenario for “Sales Order integration” (SAP\_COM\_0109) as well.

* Select a specific sales order from your S/4HANA Cloud system that you will use as an example over the course of this blog. Use the Sales Order ID shown in the “Manage Sales Order” application for this.

  + For the demo scenario, I will be using the Sales Order **324979**

Once the prerequisites are out of the way, you can proceed with the following steps:

1. Now, switch to Postman to get started with the demo. The first step is to request an x-csrf-token from the test landscape you are using.

   * Method: GET

   * Request URL:

     + <test system endpoint URL>/sap/opu/odata/sap/API\_CV\_ATTACHMENT\_SRV

   * Authorization: Basic Auth

     + Use the username and password of the communication user that you have setup in the beginning

   * Headers:

     + Key: x-csrf-token

     + Value: Fetch

   * Once you send this request, you should receive a “200” response code indicating that the request has been successfully sent. In the response section, under the “Headers” tab, copy the value of the x-csrf-token. This token will be used for the subsequent requests to authenticate your user.
     ![](/legacyfs/online/storage/blog_attachments/2023/01/response_xcsrf_token-1.png)

2. Now that we have a token, we can go ahead and send our first request to the system. This request will call the “[getAllOriginals](https://help.sap.com/docs/SAP_S4HANA_CLOUD/7489fa08cede494cbdf08fa3651598af/8b30156db25f4fd1b9b9cf1436dfd16d.html?profile=20020833)” API and fetch the metadata of the Sales order document that we are trying to view.

* + Method: GET

  + Request URL:

    - <test system endpoint URL>/sap/opu/odata/SAP/API\_CV\_ATTACHMENT\_SRV/GetAllOriginals

  + Params:

    - LinkedSAPObjectKey: <ID of the Sales order that you want to access>

      * The value must be 9 digits long, so prefix the ID of the sales order with leading zeroes as shown in the screenshot below.

      * In the example I’ve shown the Sales order ID is ‘324979’, which needs to be inputted as '0000324979'

    - BusinessObjectTypeName: 'BUS2032' (this is the BusinessObjectTypeName for Sales orders in general)
      ![](/legacyfs/online/storage/blog_attachments/2023/01/Step2_request_params_striked_out.png)

  + Authorization: Basic Auth

    - Use the username and password of the communication user that you have setup in the beginning

  + Headers:

    - Key: x-csrf-token

    - Value: <value of the token copied from Step 1>

  + Once you send this request, you should receive a “200” response code indicating that the request has been successfully sent. In the response section, under the “Body” tab, you will see a response that looks like this:
    ![](/legacyfs/online/storage/blog_attachments/2023/01/Step2_response_striked_out.png)

  + Copy the values of all the attributes of the <title> tag as you will be needing these for the next request. In the screenshot above, you will notice that the attributes “DocumentInfoRecordDocVersion” and “DocumentInfoRecordDocPart” have empty values. For these, use the values ‘00’ and ‘000’ respectively.

3. Now that we have the metadata of the sales order document we want to view, we can proceed with the final request. We now call the “[Download Attachment Content](https://help.sap.com/docs/SAP_S4HANA_CLOUD/7489fa08cede494cbdf08fa3651598af/f28b19a44a074efeb977841a1f7fa72a.html?profile=20020833)” API, which will return the sales order attachment as a pdf document.

   * Method: GET

   * Request URL:

     + <test system endpoint URL>/sap/opu/odata/ SAP/API\_CV\_ATTACHMENT\_SRV/AttachmentContentSet(DocumentInfoRecordDocType='<value from previous response>',DocumentInfoRecordDocNumber='<value from previous response>',DocumentInfoRecordDocVersion='00', DocumentInfoRecordDocPart='000', LogicalDocument='<value from previous response>',ArchiveDocumentID=’ <value from previous response>’,LinkedSAPObjectKe...