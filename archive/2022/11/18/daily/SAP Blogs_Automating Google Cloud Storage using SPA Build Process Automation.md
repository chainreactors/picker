---
title: Automating Google Cloud Storage using SPA Build Process Automation
url: https://blogs.sap.com/2022/11/17/automating-google-cloud-storage-using-spa-build-process-automation/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:31.321799
---

# Automating Google Cloud Storage using SPA Build Process Automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Automating Google Cloud Storage using SAP Build Pr...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157535&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automating Google Cloud Storage using SAP Build Process Automation](/t5/technology-blog-posts-by-sap/automating-google-cloud-storage-using-sap-build-process-automation/ba-p/13549567)

![former_member43760](https://avatars.profile.sap.com/former_member_small.jpeg "former_member43760")

![Employee](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Employee")
[former\_member43760](https://community.sap.com/t5/user/viewprofilepage/user-id/43760)

Employee

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157535)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157535)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549567)

‎2022 Nov 17
6:10 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157535/tab/all-users "Click here to see who gave kudos to this post.")

1,726

* SAP Managed Tags
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (2)

In this blog we are going to see how we can use the SPA Google Cloud Storage SDK to automate [Google Cloud Storage](https://cloud.google.com/storage/docs)

Google Cloud Storage provides an object storage repository like Amazon S3. An object is basically any sort of file which needs to be stored to be delivered later via a Content Delivery Network. The object can also be archived in case of long-term storage.

The first thing needed to use Cloud storage is a billable project in GCP. Inside this project you can create multiple ‘*buckets’* into which your objects will go.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture1-39.png)

The overall idea behind this organization is that, if your company has multiple apps, you can go ahead and create a project for each of those and place the content used by those apps in a bucket. Alternatively, you can also have a single project, place the data of your different apps in different buckets respectively.

The **Google Cloud Storage SDK** can help you automate everything from bucket creation to uploading objects.

![](/legacyfs/online/storage/blog_attachments/2022/11/GCSSDK.png)

Below scenario explains how you can you use this SDK. But here are some pre-requisites:

You need a project created in Google Cloud Platform and a service account created inside that project. [This](https://help.sap.com/docs/IRPA/91fd961a0d1048b99f907becae5bc362/6c1eeb35f12d4f4c8349d3d15045a030.html?q=Google%20Authorization)  page explains how you can create a service account in GCP, also make sure you have the Cloud Platform scope enabled: ***<https://www.googleapis.com/auth/cloud-platform>***. Once the service account is created, go to IAM in GCP and make sure you have the following permissions enabled for your service account:

![](/legacyfs/online/storage/blog_attachments/2022/11/IAM-2.png)

In addition to this, depending on your organizations’ cloud policies, you might have to enable ‘Storage Object Admin’ permission for the service account on each bucket that has been created:

![](/legacyfs/online/storage/blog_attachments/2022/11/ObjectPerms.png)

On the SPA side of things, we need to create an automation and add the Google Authorization SDK and the Google Cloud Storage SDK.

![](/legacyfs/online/storage/blog_attachments/2022/11/SDks-2.png)

**Automation Scenario**

* Authorize the bot, using service account authentication.

* Create a bucket

* Upload multiple objects in a folder within that bucket

* While uploading we will compress certain objects which are bigger in size.

* Iterate through the list of objects in that folder.

* Download them one by one.

Let’s see how each step is done in detail below:

**Authorize the bot:**

Once you create a service, you need to create a key file, which would then have to be              provided to the “**Authorize Google (Service Account)**” activity. This activity also needs to know the list of scopes for which bot has access, in this case it needs only the “GoogleCloudPlatformScope”. For further details about Authorization, you can refer this [blog](https://blogs.sap.com/2022/11/14/authorizing-sap-process-automation-to-automate-google-applications/) .

![](/legacyfs/online/storage/blog_attachments/2022/11/Auth.png)

**Create a bucket**

We then add the create bucket activity. This activity takes as mandatory input, the bucket name, and the project id of the GCP project in which this bucket must be created. Here you must give a globally unique name, and the project id can be procured from the GCP console. The highlighted area below is the project id.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step2.png)

There is non-mandatory input called the storage class, it is based on this input that the SLAs are guaranteed. If you don’t provide a value, we will use the default ‘Standard’ storage class. You can also read more about storage classes [here](https://cloud.google.com/storage/docs/storage-classes).

![](/legacyfs/online/storage/blog_attachments/2022/11/Step21.png)

**Upload Objects**

Next, we are going to upload 2 files into the bucket. One of them is sample purchase order which    is a PDF and the other one is a MP4 file explaining how to create a purchase order. Let’s look at the screen shot below:

![](/legacyfs/online/storage/blog_attachments/2022/11/upload.png)

As you can see, we have used the “Upload Object (Google Cloud Storage)” activity to perform the upload. The first parameter is the path of the file that is to be uploaded. The second parameter is the bucket name which we have procured from the output of the “Create Bucket (Google Cloud Storage)” activity from Step 2.  The third parameter “destinationPath” which is not mandatory, asks you for a specific folder in the bucket into which the object needs to be uploaded. In this case we want them to be stored under the *purchaseOrders* folder. If the folder does not exist, one is created for you.

Once the activity runs, you can see the PDF uploaded into your bucket under the *purchaseOrders* folder.

![](/legacyfs/online/storage/blog_attachments/2022/11/uploadres1.png)

The MP4 file is also uploaded in a similar manner:

![](/legacyfs/online/storage/blog_attachments/2022/11/mp4.png)

But you might notice one minor difference here. Here the *gzip* parameter is set to true. This means that the MP4 file will be compressed and uploaded. This is useful when uploading l...