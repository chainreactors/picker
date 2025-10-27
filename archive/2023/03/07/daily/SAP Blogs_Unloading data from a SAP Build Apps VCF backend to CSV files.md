---
title: Unloading data from a SAP Build Apps VCF backend to CSV files
url: https://blogs.sap.com/2023/03/06/unloading-data-from-a-sap-build-apps-vcf-backend-to-csv-files/
source: SAP Blogs
date: 2023-03-07
fetch_date: 2025-10-04T08:48:19.068382
---

# Unloading data from a SAP Build Apps VCF backend to CSV files

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Unloading data from a SAP Build Apps VCF backend t...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162054&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Unloading data from a SAP Build Apps VCF backend to CSV files](/t5/technology-blog-posts-by-sap/unloading-data-from-a-sap-build-apps-vcf-backend-to-csv-files/ba-p/13562490)

![fvettore64](https://avatars.profile.sap.com/0/2/id02ee692fbc9aa65b782c7393195a470d93bd6aa82ced0bb4ee982cca8fa3c8af_small.jpeg "fvettore64")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[fvettore64](https://community.sap.com/t5/user/viewprofilepage/user-id/122719)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162054)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162054)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562490)

‎2023 Mar 06
11:42 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162054/tab/all-users "Click here to see who gave kudos to this post.")

3,695

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (1)

In my previous blog, I showed [how data from a CSV files can be loaded into a SAB Build Apps Visual Cloud Functions (VCF) backend](https://blogs.sap.com/2023/02/24/loading-data-from-a-csv-file-into-sap-build-app-vcf-backend/).

Today I want to cover another use case: you developed a SAP Build Apps application and you ran it for some times in a BTP subaccount, saving valuable data into the VCF backend. Now you need to migrate you application to another subaccount and you want to move also the data you saved into the backend.

As I mentioned in my previous blog, at present, VCF does not provide the ability to massively load or unload data using, for instance, a CSV file.

In this article I'll explain how data can be unloaded from your VCF backend to CSV files. Data saved into CSV files can be used for for migration purposes but also for different activities: for instance you can load them into an Excel sheet and perform massive manipulations on them.

Let's start the development of our application just creating a new project, enabling the BTP authentication and installing the integration with the VCF backend you want to use. [This blog post](https://blogs.sap.com/2022/12/08/unboxing-application-backends-in-sap-build-apps-entities/) explains how to complete this task (please see the *Enabling the Backend from the UI* section).

Then we need to install an additional component from the Marketplace, for managing the download of the CSV file. This can be done just clicking on Marketplace:

![](/legacyfs/online/storage/blog_attachments/2023/02/Screenshot-2023-02-22-at-14.16.51.png)

and searching for “file”:

![](/legacyfs/online/storage/blog_attachments/2023/02/Screenshot-2023-02-22-at-14.19.44.png)

and selecting and installing the required component: “Download Base64 text as file (web only)”.

On the empty UI Canvas, we just need to add a button and, maybe, some text providing an explanation:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-03-at-09.32.21.png)

We define the variables needed by the processing logic:

**Variable Name: ObjectLists**

**Variable Type: Data Variable**

This variable must be defined for reading a collection of records from the VCF backend:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-03-at-09.39.59.png)

The default Data Variable Logic must be removed, because we want our logic to be executed after pressing the button, not when loading the initial page.

Just another variable needs to be declared:

**Variable Name: convertedText**

**Variable Type: text.**

Here following the logic to be defined for the *Unload Data* button:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-03-at-09.53.59.png)

Let's review each single steps:

**Get Record Collection:** this step reads all the record we've in the VCF backend.

**Set Data Variable:** this step fills the ObjectList data variable with all the record read in the previous step.

**JS:** this step is the heart of our unloading process and it is implemented as a JavaScript routine. The routine scans all the records from the ObjectList data variable (in input) and it generates a text variable as output that contains all the records in CSV format. Here following the code I used:

```
try {

    a = inputs.input1;

    for (var i = 0; i < a.length; i++) {

                  delete a[i].id

                }

    let topLine = Object.keys(a[0]).join(";");

    const lines = a.reduce( (acc, val) =>

    acc.concat( Object.values(val).join(";") ), [] );

    const csv = topLine.concat(`\r\n${lines.join("\r\n")}`);

    return { result: csv };

}

catch (err) {

    const error = {

      code: 'unknownError',

      message: 'Something went wrong.',

      rawError: err,

    }

    return [1, { error }]

    }
```

Please notice that on row #4 I've removed the property *id* from all the records. This is because I want my CSV file does not contain the UUID generated automatically by VCF when loading data. If you want to have this information in you CSV file, you should remove the rows #3, #4 and #5.

If you don't like to use the JavaScript component, you can replace it defining some more variables and using one or more Set Variable components with some formulas: the JavaScripts functions I used here (join, concat, reduce, keys) are also available in SAP Build Apps formulas.

SAP Build Apps provides a rich set of functions for manipulating strings, lists and objects.

**Set Page Variable:** this steps sets the variable convertedText to the output of the previous step, encoding it to the base64 format. I used the following formula:

```
ENCODE_BASE64(outputs["Function"].result)
```

**Download Base64 text as file (web only):** this step downloads the CSV file to your PC. You should configure it providing as input the convertedText variable, defining the name assigned to the file when downloaded (in my case: Output.csv) and setting the MIME Type to Plain Text:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-03-at-10.33.30.png)

Our app is now ready. You can run it just clicking on LAUNCH, opening the preview portal and selecting the Web Preview option.

After clicking the Unload Data button, the CSV file will be downloaded to your PC (maybe your should provide some authorisation, depending on the settings of your browser).

The CSV file can be edited using a text editor or Excel and it can be uploaded to the VCF backend of another BTP subaccount, using the approach I described in my previous blog.

If your VCF backend contains few records (50 - 100), this application is enough...