---
title: Create Keystore (SSH Key) for SAP Commissions Data Loader (CDL) in SAP Cloud Integration CPI
url: https://blogs.sap.com/2023/03/28/create-keystore-ssh-key-for-sap-commissions-data-loader-cdl-in-sap-cloud-integration-cpi/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:00:56.217846
---

# Create Keystore (SSH Key) for SAP Commissions Data Loader (CDL) in SAP Cloud Integration CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Create Keystore (SSH Key) for SAP Commissions Data...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161465&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create Keystore (SSH Key) for SAP Commissions Data Loader (CDL) in SAP Cloud Integration CPI](/t5/technology-blog-posts-by-members/create-keystore-ssh-key-for-sap-commissions-data-loader-cdl-in-sap-cloud/ba-p/13558541)

![Kim_Heckscher](https://avatars.profile.sap.com/f/a/idfac3da2c73c7ec3ccd8d75ca12d0ee7c9af0e4d63e92b7d25ed9def87aeb5fe6_small.jpeg "Kim_Heckscher")

[Kim\_Heckscher](https://community.sap.com/t5/user/viewprofilepage/user-id/171749)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161465)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161465)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558541)

‎2023 Mar 28
11:31 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161465/tab/all-users "Click here to see who gave kudos to this post.")

6,454

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

# Use Case

Commissions Data Loader (CDL) is a vital component of the Commissions application. CDL allows you to securely import and export critical business data to and from the Commissions application, enabling you to easily synchronize and share data within your organization for further processing.

Using CDL, you can import and export data pertaining to the business objects that are defined in Commissions. You can transfer data in bulk, to and from the following workspaces in Commissions:

* Orders and Transactions workspace for Results

* Participants, Positions, and Titles workspace for Organization

* Categories, Products, Customers, and Postal Codes workspace for Classification

With the SAP Cloud integration (CPI) we will securely import and export the critical business data to and from our ECC Eco System to the development and productive SAP Commissions Data Loader Dropbox (CDL.

# Process Overview

Perform the following Steps:

1. Download and install the SSH/SFTP Client. CDL works with any standard SSH/SFTP client application. The most commonly used free SSH/SFTP client for Windows is WinSCP. You can download and install WinSCP from <https://winscp.net/eng/download.php>. To illustrate a typical client setup process, WinSCP is used as an example in this documentation.

2. Generate an SSH Public/Private key pair in your SSH client. For example, in WinSCP client, PuTTYgen is used to generate the SSH2 key. We support setting **SSH 2 (RSA)**to **4096**

3. Associate the key pair with your email address to help you identify the key later on. For example, in WinSCP client, you can specify your email address in Key Comment

4. Save the public and private key pair. Specify a file name for the public and private key and save the key files in the same location. We recommend that you save the key files in a location that you can easily find later.

5. Open the Public SSH2 key file using any text editor and copy the public key. Send support the public key by logging a ticket. Your ticket must also include information about the customer tenant id you will be connecting to. Our technical operations team will install your public key in the Secure Box and give you access to your SFTP Dropbox (via a support ticket). You will then receive details about the SFTP File Protocol, Hostname, Port, and Username from the technical operations team.

6. To perform file transfers, log in to your SFTP Dropbox using the credentials provided by the operations team. When connecting to SFTP, you must provide the private key for authentication. For example, in WinSCP, the private key is updated in **Advanced Settings**> **Manage** > **Edit option**> **Private Key File**.

7. Convert your Private Key with Puttygen to an OpenSSH Key

8. Import the OpenSSH Key to CPI Keystore.

9. Test your Connection on CPI

# Requirements

* [Puttygen.exe](https://www.puttygen.com/download-putty) (Click on link to the left and scroll down to find the download relevant to you)

* (S)FTP Client: Used to transfer files over the internet, for example, [WinSCP](https://winscp.net/eng/download.php)

* SAP Commissions URL, for example, <https://<tenant>.callidusondemand.com/SalesPortal/#!/>

# Create SSH Key Pair with puttygen.

1. Create SSH key with Puttygen
   ![](/legacyfs/online/storage/blog_attachments/2023/03/Create-SSH-key-with-Putty-1.png)

2. Save private-key once as standard (e.g. WinSCP) and one as openssh key
   ![](/legacyfs/online/storage/blog_attachments/2023/03/export-openssh.png)

3. Save public-key - e.g. to send by SR to SAP for the Commission Data Loader (CDL) Dropbox
   ![](/legacyfs/online/storage/blog_attachments/2023/03/save-publickey.png)

*Change the filetype to **.txt** for uploading to Service Request Management of SAP Commissions.*

# Get access to the Commission Dropbox

Now you have to create an Service Request on Service Request Management for SAP Commission. Open the Service Catalog and select “**Sales Performance Management SPM**” and
the Service “**SPM - Dropbox and, Landing Pad Shell Access Request**”

LINK: [SAP Commission - Services Request Management - SRM](https://itsm.services.sap/srm?id=lob_services)
![](/legacyfs/online/storage/blog_attachments/2023/03/itsm_SRM.png)

Fill out the Request:
![](/legacyfs/online/storage/blog_attachments/2023/03/CDL_Req1_03.png)

*The filetype of the attached publickey needs to be “txt” for uploading to Service Request Management of SAP Commissions**.*

# Import SSH Key into CPI Keystore

After you send the public key to SRM of Sale Performance Management (SPM) you can add your Key Pair to your CPI Keystore.

1. Open the Keystore of your SAP Cloud Integration (CPI) (Monitor)
   ![](/legacyfs/online/storage/blog_attachments/2023/03/CPI_1_01.png)

2. Add SSH Key
   ![](/legacyfs/online/storage/blog_attachments/2023/03/CPI_1_02.png)

3. Example to fill out the Form
   ![](/legacyfs/online/storage/blog_attachments/2023/03/CPI_1_03.png)

4. Finally saved SSH Key on CPI Keystore:
   ![](/legacyfs/online/storage/blog_attachments/2023/03/CPI_1_04.png)

# Test your SSH Key with your Tenant

After the feedback from Suppport of successful placement of your Public Key you can Now you’re your SFTP Connection.

Open your Cloud Integration Tenant and select Monitoring Oveview / Connectivity
<https://<YOURID>-tmn.hci.eu2.hana.ondemand.com/itspaces/shell/monitoring/Connectiv...