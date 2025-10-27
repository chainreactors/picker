---
title: Render and View PDF in SAP UI5 with Forms service by adobe in BTP
url: https://blogs.sap.com/2022/11/23/render-and-view-pdf-in-sap-ui5-with-forms-service-by-adobe-in-btp/
source: SAP Blogs
date: 2022-11-24
fetch_date: 2025-10-03T23:38:36.974442
---

# Render and View PDF in SAP UI5 with Forms service by adobe in BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Render and View PDF in SAP UI5 with Forms service ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160440&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Render and View PDF in SAP UI5 with Forms service by adobe in BTP](/t5/technology-blog-posts-by-sap/render-and-view-pdf-in-sap-ui5-with-forms-service-by-adobe-in-btp/ba-p/13557538)

![Jacky_Liu1](https://avatars.profile.sap.com/0/c/id0c96fbc6ecfa4651eccd3b5e561d0848734220dc92c2198772bae6ac9168e7b7_small.jpeg "Jacky_Liu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jacky\_Liu1](https://community.sap.com/t5/user/viewprofilepage/user-id/132085)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160440)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160440)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557538)

‎2022 Nov 23
11:34 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160440/tab/all-users "Click here to see who gave kudos to this post.")

6,736

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

In my blog [Configure the SAP BTP Cloud Foundry Environment Subaccount with SAP Forms Service by Adobe and Test ...](https://blogs.sap.com/2022/01/24/configure-the-sap-btp-cloud-foundry-environment-subaccount-with-sap-forms-service-by-adobe/) , we can get the base64 encoded adobe content in postman. In this blog, I will  explain how to view the rendered pdf content in SAP UI5 application .

## Prerequisites

You have a subaccount on SAP BTP, Cloud Foundry environment and the subaccount has entitlement of service Forms service by Adobe .

The  following is the detailed steps :

### Step 1. Creat destination base on service key **adobeapikey** in mentioned [blog](https://blogs.sap.com/2022/01/24/configure-the-sap-btp-cloud-foundry-environment-subaccount-with-sap-forms-service-by-adobe/)  in BTP subaccount cockpit

![](/legacyfs/online/storage/blog_attachments/2022/11/ad1.png)

### Step 2. Create a button in sap ui5 application view

![](/legacyfs/online/storage/blog_attachments/2022/11/ad2.png)

### Step 3. Create the function in controller used  in the view button in previous step.

![](/legacyfs/online/storage/blog_attachments/2022/11/ad3.png)

The following is the code :

```
sap.ui.define([

    "sap/ui/core/mvc/Controller",

    "sap/m/MessageBox",

    "sap/m/PDFViewer",

    "sap/base/security/URLWhitelist",

],

    /**

     * @param {typeof sap.ui.core.mvc.Controller} Controller

     */

    function (Controller,MessageBox,PDFViewer,URLWhitelist) {

        "use strict";

        return Controller.extend("ui5applicationmodule.controller.appsingleview", {

            onInit: function () {

            },

            pdfRender:function(){

                var printd = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><form1><LabelForm><DeliveryId>Mirum est ut animus agitatione motuque corporis excitetut.</DeliveryId><Position>Ego ille</Position><MaterialNo>Si manu vacuas</MaterialNo><Quantity>Apros tres et quidem</Quantity><Package>Mirum est</Package><QRCode>01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789</QRCode></LabelForm><LabelForm><DeliveryId>Ad retia sedebam: erat in proximo non venabulum aut lancea, sed stilus et pugilares:</DeliveryId><Position>Licebit auctore</Position><MaterialNo>Proinde</MaterialNo><Quantity>Am undique</Quantity><Package>Ad retia sedebam</Package><QRCode>01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789</QRCode></LabelForm><LabelForm><DeliveryId>meditabar aliquid enotabamque, ut, si manus vacuas, plenas tamen ceras reportarem.</DeliveryId><Position>Vale</Position><MaterialNo>Ego ille</MaterialNo><Quantity>Si manu vacuas</Quantity><Package>Apros tres et quidem</Package><QRCode>01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789</QRCode></LabelForm></form1>";

                var printdb64 = btoa(printd);

               var pdfcontent = {

                    embedFont: 0,

                    formLocale: "en_US",

                    formType: "print",

                    taggedPdf: 1,

                    xdpTemplate: "labelprint/PrintLabel",

                    xmlData: printdb64

                 };

                $.ajax({

                    url: "/adobeapi/v1/adsRender/pdf?templateSource=storageName&TraceLevel=0",

                    type: "POST",

                    data: JSON.stringify(pdfcontent),

                    headers: {

                        "Content-Type": "application/json"

                    },

                    async: false,

                    success: function (data) {

                        const deccont = atob(data.fileContent);

                        const byteNumbers = new Array(deccont.length);

                        for (let i = 0; i < deccont.length; i++) {

                            byteNumbers[i] = deccont.charCodeAt(i);

                        }

                 ...