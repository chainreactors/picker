---
title: SAP Commissions – Smart Data Integration[SDI] – Part 7a
url: https://blogs.sap.com/2023/05/20/sap-commissions-smart-data-integrationsdi-part-7a/
source: SAP Blogs
date: 2023-05-21
fetch_date: 2025-10-04T11:37:48.150181
---

# SAP Commissions – Smart Data Integration[SDI] – Part 7a

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions – Smart Data Integration[SDI] – Pa...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5988&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions – Smart Data Integration[SDI] – Part 7b](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-smart-data-integration-sdi-part-7b/ba-p/13559343)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5988)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5988)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559343)

‎2023 May 20
8:11 AM

0
Kudos

1,613

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)

View products (2)

Dear All,

This article is intended for database admins, consultants, customers & partners to enable the File Adapter using **PGP/GPG encryption** & configure encrypted sample data from your local file path to load into your SDI Project

In this blog, PGP tool is installed, we will be encrypting the source file provided by customer (extract & dump regularly) in the local path where DP Agent is installed and public & secret key is saved for decrypting the files.
Few customers may not connect to their local database (source) due to privacy & security.

![](/legacyfs/online/storage/blog_attachments/2023/05/FPy0L2AXEAALdP5.jpg)

**PGP VERSION**
You must use a version older than GnuPGP 2.3 or a version compatible with -rfc4880.

---

## Download & Install PGP Tool

For example if using Kleopatra you can use the version 3.3.16 or older: (this is specifically tested with 3.1.15 from <https://gpg4win.org/change-history.html>)

## Version which works![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-15-30.png)

After you installed, Create your Key

Export your Public Key & Private Key into your local path and keep it safe. Ensure your Certificate Key expiry date is still valid.   ( **Do not share it to anyone)**![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_14-55-23.png)

The PGP Secret Key Path represents the PGP Private key. This is used for decrypting the file. The Third Party Public Key Path represents the PGP Public Key. This is used to read the PGP Signature. Prior to DP Agent version 2.6.3 all PGP encrypted files needed to be signed and therefore the Third Party Public Key Path parameter must be maintained in the remote source and the public key present in the FileAdapter local store.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-30-42.png)

## Prepare a file for upload

Download [this sample file](https://github.com/SAPDocuments/Tutorials/blob/master/tutorials/haas-dm-connect-sdi/salarydata.csv) into the default workspace.

The default workspace is located in <<ROOT DIRECTORY>>\workspace, for example, \usr\sap\dpa\workspace

Select the file which you need to encrypt![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-17-38.png)
Review the file which you need to sign/encrypt![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-17-55-1.png)
Enter the Passphrase which you set as per your certificate signature.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-18-13.png)
File is encrypted successfully and you can see your encrypted file in your path.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-18-50.png)
The datafiles being sent to the DP Agent needs to end with .gpg. File with the extension .pgp are not supported

This is how it should look like in your directory for file to process.. ![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_13-43-07.png)
Create a text file called salarydata.cfg with the following content:

```
#Configuration file for data load

CODEPAGE=UTF-8

ERROR_ON_COLUMNCOUNT=false

ESCAPE_CHAR=\

EXPONENTIAL=E

FORCE_DIRECTORY_PATTERN=C:\usr\sap\dataprovagent\Datafiles

FORCE_FILENAME_PATTERN=salarydata.csv

FORMAT=CSV

LENIENT=true

LOCALE=en_US

ROW_DELIMITER=\n

SKIP_HEADER_LINES=1

COLUMN=id;INTEGER;

COLUMN=salary;INTEGER;

COLUMN=start_year;INTEGER;

COLUMN=gender;NVARCHAR(256);

COLUMN=region;NVARCHAR(256);

COLUMN=T-Level;NVARCHAR(256);
```

Save the configuration file in the same directory.

---

Create a Remote Source

Go back to the Database Explorer. You will see the adapter under Catalog -> Remote Source

Right-click on **Remote Sources**. Choose **Add Remote Source**

Here you can define the Source Name (arbitary), the Adapter will be the FileAdapter ![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-26-43.png)

Provide the location of the PGP keys. You get asked for their location when registering the FileAdapter preferences and in the remote source.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-30-15.png)
Scroll down to the credentials and choose **Technical User** as the credentials mode and enter the access token in the **AccessToken** field. If you used the example token before, enter FileToken. (Refer Part 7 how to generate fileAdapter token)

Also you need to provide PGP Passpharse which you set while installing your PGP.. this will enable to decrypt the file while proceessing![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-29-30.png)
Click **Create**

Check the remote objects to make sure configuration has been successful and to complete the validation below.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-19_12-26-08.png)
Also you can CREATE REMOTE SOURCE using below statement in your webIDE

```
CREATE REMOTE SOURCE "SDI_FileAdapter_encryption" ADAPTER "FileAdapter" AT LOCATION AGENT "Localfiledump2process"

CONFIGURATION

'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<ConnectionProperties>

	<PropertyEntry name="rootdir">C:\usr\sap\dataprovagent\Datafiles</PropertyEntry>

	<PropertyEntry name="fileformatdir">C:\usr\sap\dataprovagent\Datafiles</PropertyEntry>

	<PropertyEntry name="usecdc">true</PropertyEntry>

	<PropertyEntry name="source_options">lo...