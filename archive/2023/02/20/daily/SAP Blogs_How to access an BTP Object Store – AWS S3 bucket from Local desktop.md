---
title: How to access an BTP Object Store – AWS S3 bucket from Local desktop
url: https://blogs.sap.com/2023/02/19/how-to-access-an-btp-object-store-aws-s3-bucket-from-local-desktop/
source: SAP Blogs
date: 2023-02-20
fetch_date: 2025-10-04T07:33:21.576897
---

# How to access an BTP Object Store – AWS S3 bucket from Local desktop

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to access an BTP Object Store - AWS S3 bucket ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158558&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to access an BTP Object Store - AWS S3 bucket from Local desktop](/t5/technology-blog-posts-by-sap/how-to-access-an-btp-object-store-aws-s3-bucket-from-local-desktop/ba-p/13552292)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158558)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158558)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552292)

‎2023 Feb 19
8:40 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158558/tab/all-users "Click here to see who gave kudos to this post.")

7,210

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (3)

Dear All,

To upload the files into an S3 bucket, there is other recommend way is using a desktop tool that will preserve the directory structure and will recover if your network connection is interrupted.

Amazon S3 (Simple Storage Service) is a cloud storage service that allows users to store and retrieve any amount of data, at any time, from anywhere on the web. S3 buckets are a popular storage option for businesses and individuals because they offer scalable, low-cost storage for a wide variety of use cases.![](/legacyfs/online/storage/blog_attachments/2023/02/90b4db10eb1e3764de8e519f6b8411d7.png)

# Object Store on SAP BTP

Store and manage the blobs/objects on SAP BTP.**Overview of Object store**

Object Store service on SAP BTP lets you store and manage objects, which involves creation, upload, download, and deletion. This service is specific to the IaaS layer such as **Azure Blob Storage, Amazon Web Services, and Google Cloud Platform**![](/legacyfs/online/storage/blog_attachments/2023/02/SAA-1.png)

First you'll need to have created an S3 bucket to upload to. [Here are the instructions](https://discovery-center.cloud.sap/index.html#/serviceCatalog/object-store/?region=all) to do this.

---

### How to get AWS S3 (**Simple Storage Service) bucket key pair from SAP BTP**

Once you enabled Object store and referenced to cloud foundry app, you would see this below account details to S3 bucket.![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18_18-14-02.png)

---

### Uploading a file to an Object store - AWS S3 bucket from Windows

Download and install [WinSCP](https://winscp.net/eng/download.php)

Configure the connection in WinSCP:

1. Select "New site"
2. In the New site dialog, select Amazon S3 protocol
3. In the "Host" field, enter "s3.amazonaws.com
4. Enter the *Access Key ID* and *Secret Access Key*
5. Click 'Advanced'![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18_11-44-55.png)
6. Click "Directories" (in the "Environment" section)
7. In the 'Remote Directory" field, enter the S3 *bucket name*
8. *![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18_11-47-36-1.png)*Click "S3" (in the "Environment" section) - Select AWS Region
   ![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18_11-46-38-1.png)

1. Once connected, you can drag-and-drop the top-level directories into the S3 bucket. This will recursively upload the files and sub-directories.

   ![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18_11-49-15-1.png)

In above use case, **SAP Commissions** sql files are stored in AWS S3 Bucket for Touchless Deployment which is maintained through version control by an admin.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [amazon s3](/t5/tag/amazon%20s3/tg-p/board-id/technology-blog-sap)
* [objectstore](/t5/tag/objectstore/tg-p/board-id/technology-blog-sap)
* [s3](/t5/tag/s3/tg-p/board-id/technology-blog-sap)
* [s3bucket](/t5/tag/s3bucket/tg-p/board-id/technology-blog-sap)

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fhow-to-access-an-btp-object-store-aws-s3-bucket-from-local-desktop%2Fba-p%2F13552292%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [🚀 Mastering the Essentials: Your Journey into SAP S/4HANA Starts Here!](/t5/technology-blog-posts-by-members/mastering-the-essentials-your-journey-into-sap-s-4hana-starts-here/ba-p/14229489)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate SAP S/4HANA Guide: From Master Data to End-to-End Processes](/t5/technology-blog-posts-by-members/the-ultimate-sap-s-4hana-guide-from-master-data-to-end-to-end-processes/ba-p/14228226)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Maintain File In WEB Repository](/t5/technology-blog-posts-by-members/maintain-file-in-web-repository/ba-...