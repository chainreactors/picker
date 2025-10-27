---
title: Hosting a server-less UI5 application on AWS
url: https://blogs.sap.com/2022/12/18/hosting-a-server-less-ui5-application-on-aws/
source: SAP Blogs
date: 2022-12-19
fetch_date: 2025-10-04T01:53:53.247662
---

# Hosting a server-less UI5 application on AWS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Hosting a server-less UI5 application on AWS

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160685&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Hosting a server-less UI5 application on AWS](/t5/technology-blog-posts-by-members/hosting-a-server-less-ui5-application-on-aws/ba-p/13553891)

![archisman92](https://avatars.profile.sap.com/c/6/idc64126cdc959cc0caa95272fd1cd18aee33e2b1b1f4343387126400d3c375070_small.jpeg "archisman92")

[archisman92](https://community.sap.com/t5/user/viewprofilepage/user-id/679180)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160685)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160685)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553891)

‎2022 Dec 18
1:28 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160685/tab/all-users "Click here to see who gave kudos to this post.")

1,826

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

Dear Community,

The following blog will guide you to deploy a UI5 application on AWS S3 with Dynamo DB as backend database, Lambda as the business logic layer and API gateway which acts as a connection between the client(UI) and Lambda.

![](/legacyfs/online/storage/blog_attachments/2022/12/DemoAppArchitecture-1.jpg)

Architecture

Now lets tackle these layers one by one.

* Amazon S3:

Head over to your AWS account and search for S3. Click on the Create Bucket option as shown below.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket.jpg)

Create Bucket

In the window that appears, type in a unique name for your bucket. *Please note that the name must be unique across all accounts and regions*, which means that if I choose my bucket name to be demo-app-archisman, you will not be able to use the same name although you are working on your own private account(and maybe in a separate region).

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_1-1.jpg)

Uncheck "Block All Public Access" as shown below.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_2.jpg)

Keeping the rest of the settings as default, hit the Create Bucket button. You should be able to see a new public bucket created.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_3.JPG.png)

Next, we will navigate to our bucket and edit the bucket policy to "Allow" Get access to all the objects stored on our bucket.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_4.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_5.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_6.jpg)

Type Of Policy: S3 Bucket Policy

Effect: Allow

Principal: \*

Action: GetObject

ARN: arn:aws:s3:::demo-app-archisman/\* (make sure to paste your own unique Amazon Resource Name here and append /\* at the end which means we are granting GetObject access to all the objects within our bucket)

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_7.jpg)

Once you have correctly added the above statement, generate the policy.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_8.jpg)

You should be able to see a window pop up with the generated policy in JSON format. Copy it to clipboard.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_9.jpg)

Paste the above copied JSON into the bucket policy text area as shown below and save the changes.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_10.jpg)

Now that we have got the bucket policy out of our way, let us upload our UI5 web application onto S3. Navigate to Objects tab and click on the Upload button.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_11.jpg)

Select all the files and drag and drop them to the Upload Section.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_13.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_14.jpg)

Click on Upload. Once upload is completed, you will be able to see the uploaded files and folders in the Objects tab.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_15.jpg)

Now that the web application files are uploaded, we need to explicitly tell S3 that we are going to be hosting a static website.

Navigate to the Properties tab and in the very last section click on the Edit button for "Static Website Hosting".

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_16.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_17.jpg)

Edit the below properties and save changes.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_18.jpg)

Go back to the same section of Static website hosting and you should be able to see an endpoint Url. Click on the Url and your UI5 application is up and running.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_19.jpg)

For me, its a simple Chat Application interface.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateBucket_20.jpg)

Now that we have a static website up and running, lets work on the backend in order to make our application interactive.

* Dynamo DB:

Our choice of database here is Dynamo DB which very much resembles NoSql Mongo DB. Keeping with the theme of our application, this database again is server-less thus we do not need to worry about provisioning the right server to host our database.

Head over to the AWS service Dynamo DB and click on Create Table.

![](/legacyfs/online/storage/blog_attachments/2022/12/DynamoDb_1.jpg)

Type in your table name, the partition key(synonymous to primary key from SQL) and sort key(which is optional). If you are unsure about the Read Capacity Units and Write Capacity Units keep them as default. However, it is important to understand these while designing a production ready application as they determine how well your database performs. These units help Dynamo DB decide the number of partitions to create and in turn how efficiently the database returns the output of a query.

![](/legacyfs/online/storage/blog_attachments/2022/12/DynamoDb_2.jpg)

Click on Create Table.

Once the table is created, navigate to the table and create a few items (rows).

![](/legacyfs/online/storage/blog_attachments/2022/12/DynamoDb_3.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/DynamoDb_4.jpg)

JSON View for the above item. I wanted to show this Dynamo DB view of the JSON especially as this understanding of the structure will be needed when you write your lambda functions. "S" denotes string, "L" denotes list/array and "M" denotes map/object.

![](/legacyfs/online/storage/blog_attachments/2022/12/DynamoDb_5.jpg)

Create as many tables as your application demands and move on to creating the business logic layer...