---
title: Using Custom Actions to display PDF from SAP BTP Forms service into a CAP SAPUI5 application
url: https://blogs.sap.com/2023/01/30/using-custom-actions-to-display-pdf-from-sap-btp-forms-service-into-a-cap-sapui5-application/
source: SAP Blogs
date: 2023-01-31
fetch_date: 2025-10-04T05:13:41.811831
---

# Using Custom Actions to display PDF from SAP BTP Forms service into a CAP SAPUI5 application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Using Custom Actions to display PDF from SAP BTP F...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158839&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Custom Actions to display PDF from SAP BTP Forms service into a CAP SAPUI5 application](/t5/technology-blog-posts-by-sap/using-custom-actions-to-display-pdf-from-sap-btp-forms-service-into-a-cap/ba-p/13552996)

![rodfior](https://avatars.profile.sap.com/d/f/iddfcd2cff7cd76fd2107274131833329a17f72788218e5a4833206471e2acfe89_small.jpeg "rodfior")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[rodfior](https://community.sap.com/t5/user/viewprofilepage/user-id/130642)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158839)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158839)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552996)

‎2023 Jan 30
10:11 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158839/tab/all-users "Click here to see who gave kudos to this post.")

5,902

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)

* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (3)

## Intro

A few months ago we were working in a CAP development where after the CAP SAPUI5 application was implemented, one of the requirements that we had was generating a PDF document with Forms Service API using the document details opened with the Object Page UI5 Element.

Since the requirement was to have a button on the Object Page to generate the PDF  with the data from the specific document, we could not use the Cloud SDK to perform the API call to generate and display the PDF on screen.

Other constraint found was when trying to use CAP action through CDS, since the CDS action does not support media stream.

So the approach used was to implement it via Custom Action extending the Object Page controller. The objective of this blog is to share how it was achieved.

## Pre-requisites

We are not going into details about how to create a SAPUI5 CAP implementation or how to implement the Adobe Forms Services.

We recommend you to follow the following steps to implement the steps described in this blog

1. Configure Forms Services and create your first Form: [https://blogs.sap.com/2022/01/24/configure-the-sap-btp-cloud-foundry-environment-subaccount-with-sap...](https://blogs.sap.com/2022/01/24/configure-the-sap-btp-cloud-foundry-environment-subaccount-with-sap-forms-service-by-adobe/)

2. Create a simple CAP Application\*: <https://developers.sap.com/mission.btp-application-cap-e2e.html>. This document shows hot to implement a CAP application in VS Code, but same steps can be translated to Business Application Studio, which is the approach taken in this blog.

Having the Fiori CAP application and the SAP BTP Forms Service in place, we can go with the extension steps.

## Steps

### Bind CAP application with Forms Service Instance

In the mta.yml file, add Forms service as a Resource:

![](/legacyfs/online/storage/blog_attachments/2023/01/pic1-3.png)

Add new resource as a requirement from the CAP service:

![](/legacyfs/online/storage/blog_attachments/2023/01/pic2-7.png)

### Create a non-persistent entity implementation on the OData service.

On the  service add the following lines to create the non-persistent entity:

```
  @readonly  @cds.persistence.skip

  entity PDFdoc {

    key Id      : String(20);

        pdfFile : String

  }
```

This entity is required since we want to make the Forms Service API call within the service handler, with this we can use the current context of the OData call for the displayed document on the Object Page and pass the relevant information to the Forms Service API so the PDF is generated with the current document data.

Implement the following logic in your handler file:

\..\srv\<service-handler.js>

```
const cds = require('@sap/cds')

const tx = cds.tx();

const axios = require('axios');

module.exports = cds.service.impl(async function(srv) {

    let risksDataext;

    this.after('READ', 'Risks', risksData => {

        const risks = Array.isArray(risksData) ? risksData : [risksData];

        risks.forEach(risk => {

            if (risk.impact >= 100000) {

                risk.criticality = 1;

            } else {

                risk.criticality = 2;

            }

        });

        risksDataext = risksData;

    });

    const {Risks} = srv.entities;

    this.on ('READ', 'PDFdoc', async (req) => {

    var riskID = req.data.Id;

    let RisksData = await tx.run((SELECT.from(Risks.name)).where ({ID: riskID}));

    let xmlData = `<form1><Title>${RisksData[0].title}</Title><Description>${RisksData[0].descr}</Description><Priority>${RisksData[0].prio}</Priority><Impact>${RisksData[0].impact}</Impact><Criticality>${risksDataext.criticality}</Criticality></form1>`

    var vcap_services = JSON.parse(process.env.VCAP_SERVICES)

    if (vcap_services.adsrestapi !== undefined ){

        var username = vcap_services.adsrestapi[0].credentials.uaa.clientid

        var password = vcap_services.adsrestapi[0].credentials.uaa.clientsecret

        var authURL =  vcap_services.adsrestapi[0].credentials.uaa.url

        var apiURL =   vcap_services.adsrestapi[0].credentials.uri

    }else{

        return;

    }

     var auth = 'Basic ' + new Buffer(username + ':' + password).toString('base64');

     var tokenOptions = {

            'method': 'POST',

            'url': authURL + "/oauth/token?grant_type=client_credentials",

            'headers': {

                'Authorization': 'Bearer ' + token,

                'Content-Type': 'application/json'

            },

            'redirect': 'follow'

        };

       const tokenResponse = await axios(tokenOptions);

        const tokenjson = await tokenResponse.json();

        const token = tokenjson.access_token;

        var bodyE = new Buffer(xmlData).toString('base64');

        var xdpVal = "riskform/RiskForm"

        var base64Pdf = JSON.stringify({

            "xdpTemplate": xdpVal,

            "xmlData": bodyE,

            "formType": "print",

            "formLocale": "",

            "taggedPdf": 1,

            "embedFont": 0

        })

        var o...