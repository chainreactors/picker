---
title: Upload data from excel in CAP (Node.js)
url: https://blogs.sap.com/2022/11/21/upload-data-from-excel-in-cap-node.js/
source: SAP Blogs
date: 2022-11-22
fetch_date: 2025-10-03T23:23:25.881642
---

# Upload data from excel in CAP (Node.js)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Upload data from excel in CAP (Node.js)

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160719&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Upload data from excel in CAP (Node.js)](/t5/technology-blog-posts-by-members/upload-data-from-excel-in-cap-node-js/ba-p/13554121)

![KM11](https://avatars.profile.sap.com/b/2/idb267968448abbf535bdab905846a4be043d1b51768c5859fac62ee34cf8b7a24_small.jpeg "KM11")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[KM11](https://community.sap.com/t5/user/viewprofilepage/user-id/16357)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160719)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160719)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554121)

‎2022 Nov 21
9:58 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160719/tab/all-users "Click here to see who gave kudos to this post.")

15,791

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (2)

*This example demonstrates how to upload data from excel into HANA cloud tables. This can be beneficial for mass upload of data using excel.*

A fiori elements list report is created to display and upload the data into the tables. Upload button is added as an extension to the List Report Application.

**The upload entity in this can be re-used for updating data in multiple tables/entities.**

The uploaded data is parsed and inserted into respective entity. We can write validations before upload by internally invoking the custom handlers of the respective entity using srv.run.

const query = INSERT.into(entity).entries(data);

let srv = awaitcds.connect.to('StudentsSrv');

const Result = await srv.run(query);

**CAP DB and SRV Artifacts :**

```
Database :

entity Students : cuid {

 StudentId: String(6);

 FirstName: String;

 LastName: String;

 DOB: Date;

 Address: String;

}

Service:

service StudentsSrv {

@cds.persistence.skip

@odata.singleton

 entity ExcelUpload {

        @Core.MediaType : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        excel : LargeBinary;

    };

entity Students as projection on db.Students

}

Service.js: ( Custom Handlers)

srv.on('PUT', “ExcelUpload", async (req, next) => {

        if (req.data.excel) {

            var entity = req.headers.slug;

            const stream = new PassThrough();

            var buffers = [];

            req.data.excel.pipe(stream);

            await new Promise((resolve, reject) => {

                stream.on('data', dataChunk => {

                    buffers.push(dataChunk);

                });

                stream.on('end', async () => {

                    var buffer = Buffer.concat(buffers);

                    var workbook = XLSX.read(buffer, { type: "buffer", cellText: true, cellDates: true, dateNF: 'dd"."mm"."yyyy', cellNF: true, rawNumbers: false });

                    let data = []

                    const sheets = workbook.SheetNames

                    for (let i = 0; i < sheets.length; i++) {

                        const temp = XLSX.utils.sheet_to_json(

                            workbook.Sheets[workbook.SheetNames[i]], { cellText: true, cellDates: true, dateNF: 'dd"."mm"."yyyy', rawNumbers: false })

                        temp.forEach((res, index) => {

                            if (index === 0) return;

                            data.push(JSON.parse(JSON.stringify(res)))

                        })

                    }

                    if (data) {

                            const responseCall = await CallEntity(entity, data);

                            if (responseCall == -1)

                                reject(req.error(400, JSON.stringify(data)));

                            else {

                                resolve(req.notify({

                                    message: 'Upload Successful',

                                    status: 200

                                }));

                        }

                    }

                });

            });

        } else {

            return next();

        }

    });

 srv.before('POST', 'Students', async (req) => {

       //Custom validations can be put, if required before upload

 };

 srv.on('POST', 'Students', async (req) => {

     //return reponse to excel upload entity .

    });

 async function CallEntity(entity, data) {

    if (entity === Students) {

      //If any custom handling required for a particular entity

    }

    const insertQuery = INSERT.into(entity).entries(data);

    // This calls the service handler of respective entity. It can be used if any custom

    validations need to be performed. or else custom handlers can be skipped.

    let srv = await cds.connect.to('StudentsSrv');

    const insertResult = await srv.run(insertQuery);

    let query = SELECT.from(entity);

    await srv.run(query);

    return insertResult; //returns response to excel upload entity

};
```

**CAP APP Artifacts:**Create a list report application using fiori template and extend the application to add custom upload button on the list page.

```
Manifest.json

     "controlConfiguration": {

                                "@com.sap.vocabularies.UI.v1.LineItem": {

                                    "actions": {

                                        "Upload": {

                                            "id": "UploadButton",

                                            "text": "Upload",

                                            "press": "com.test.ExtensionController.Upload",

                                            "requiresSelection": false

                                        },

ExcelUploadDialog.fragment.xml:

<core:FragmentDefinition xmlns:core="sap.ui.core"

    xmlns:u="sap.ui.unified"

    xmlns="sap.m">

    <Dialog id="_IDDialog"

        title=“Excel Upload"

        class="sapUiResponsiveContentPadding"

        beforeOpen=".onBeforeOpen"

        afterClose=".onAfterClose">

        <content>

            <u:FileUploader id="uploader"

                fileType="xlsx"

                multiple="false"

                uploadUrl=“StudentsSrv/ExcelUpload/excel"

                fileAllowed=".onFileAllowed"

                fileEmpty=".onFileEmpty"

     ...