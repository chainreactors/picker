---
title: SAP Datasphere: On Premise SFTP connectivity
url: https://blogs.sap.com/2023/03/18/sap-datasphere-on-premise-sftp-connectivity/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:18.778366
---

# SAP Datasphere: On Premise SFTP connectivity

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Datasphere: On Premise SFTP connectivity

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160227&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere: On Premise SFTP connectivity](/t5/technology-blog-posts-by-members/sap-datasphere-on-premise-sftp-connectivity/ba-p/13551226)

![shoeb_k79](https://avatars.profile.sap.com/e/3/ide338ad6707f341f451792874b0329eb594b2b1ecf03eab7caed878e679c3eba7_small.jpeg "shoeb_k79")

[shoeb\_k79](https://community.sap.com/t5/user/viewprofilepage/user-id/13031)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160227)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160227)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551226)

‎2023 Mar 18
6:57 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160227/tab/all-users "Click here to see who gave kudos to this post.")

13,420

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration, secure connectivity add-on](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration%252C%2520secure%2520connectivity%2520add-on/pd-p/67837800100800004900)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration, secure connectivity add-on

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration%25252C%2Bsecure%2Bconnectivity%2Badd-on/pd-p/67837800100800004900)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

View products (4)

Hello,

**Introduction:**

In this blog post we will be discussing the steps required to setup connectivity between SAP Datasphere (formerly Data Warehouse Cloud) and SFTP data source hosted on-premise.

**Components involved:**

* SAP DWC/Datasphere

* SAP Cloud Connector - on premise

* SFTP server - on Premise

The connectivity type used will be 'Generic SFTP' and it will support 'Data flows'.

**Pre requisites:**

* The firewall rules must be adjusted to allow SAP Cloud connector to connect with SFTP server.

* SAP Datasphere is allowed to connect with SAP CC.

* You must have access to Cloud Connector administration.

* You must also have administration credentials on SAP DWC/Dataspehere.

**Step 1: SAP Datashphere environment**

Collect details of your DWC environment - log in DWC -> System -> Administration -> Data Source Configuration

make note of account information, subaccount, Region, user and also make sure that you have the password for the subaccount user.

![](/legacyfs/online/storage/blog_attachments/2023/03/screen1-1.jpg)

Subaccount Information

**Step 2: SAP Cloud Connector**

Log in to SAP Cloud Connector - Click on ‘Connector’ -> Add Subaccount

![](/legacyfs/online/storage/blog_attachments/2023/03/screen2-1.jpg)

Fill the subaccount information picked from DWC in Step1

![](/legacyfs/online/storage/blog_attachments/2023/03/screen3-1.jpg)

*Take note of the 'Location ID'. It will be used later in the steps.*

*Location ID is defined by us, it is a unique ID for the account.*

When the account is set-up we can select to switch account to view its status

![](/legacyfs/online/storage/blog_attachments/2023/03/screen4-6.jpg)

**Step 3: SAP Cloud Connector**

In the Cloud Connector -> select sub account and then click 'Cloud To On-Premise'

![](/legacyfs/online/storage/blog_attachments/2023/03/screen5-1.jpg)

On the 'Access Control' tab click +

![](/legacyfs/online/storage/blog_attachments/2023/03/screen6-1.jpg)

For SFTP connectivity (*or for any other non-SAP connectivity*) - select the following options

![](/legacyfs/online/storage/blog_attachments/2023/03/screen7-3.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/screen8-1.jpg)

Fill in the SFTP server details

![](/legacyfs/online/storage/blog_attachments/2023/03/screen9-1.jpg)

On the next screen - define a virtual host and port. The virtual host and port will be used for connectivity on the cloud side.

![](/legacyfs/online/storage/blog_attachments/2023/03/screen10-1.jpg)

Review summary and finish the setup

![](/legacyfs/online/storage/blog_attachments/2023/03/screen11-1.jpg)

To check and validate the connectivity from Cloud Connector

![](/legacyfs/online/storage/blog_attachments/2023/03/screen12-1.jpg)

**Step 4: SAP Datasphere**

Log on to the DWC environment : Go to ‘system' -> 'administration’  -> 'Data Source Configuration'

Click - 'Add a new location'

Add the cloud connector location ID which we created in SAP Cloud Connector subaccount setup.

![](/legacyfs/online/storage/blog_attachments/2023/03/screen13-1.jpg)

click create.

Next,

Click on ‘Connections’ -> navigate to the appropriate SPACE ID which you want to use for connectivity.

click 'create'

![](/legacyfs/online/storage/blog_attachments/2023/03/screen14-1.jpg)

select the connection type -'Generic SFTP'

![](/legacyfs/online/storage/blog_attachments/2023/03/screen15.jpg)

Fill the respective fields

![](/legacyfs/online/storage/blog_attachments/2023/03/screen16.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/screen17.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/screen18.jpg)

*\*Note that the host key will be provided by the SFTP administrator.*

*Procedure to generate the host key is explained [here](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/5454a8cfdb9845a9b6c772d63b8e92ec.html)*

*\*Authentication can be user/password based or it can also be SSH type.*

*\*Desired root path can also be defined for browsing objects.*

Finalize the connection

![](/legacyfs/online/storage/blog_attachments/2023/03/screen19.jpg)

'validate' the connection from DWC

![](/legacyfs/online/storage/blog_attachments/2023/03/screen20-1.jpg)

Successful connection will return the following

![](/legacyfs/online/storage/blog_attachments/2023/03/screen21-1.jpg)

**Conclusion:**

Source data on the SFTP servers can easily be accessed using the procedure defined above.

Data Flows are enabled without the need to set any additional connection properties.

**Troubleshooting:**

Cloud Connector Troubleshooting, logs and traces:

Update the trace level by clicking edit button and select the highlighted parameters

![](/legacyfs/online/storage/blog_attachments/2023/03/screen22.jpg)

Ljs trace and traffic trace will be helpful in troubleshooting scenarios.

Regards,

Shoeb

--

**References:**

[https://help.sap.com/docs/SAP\_DATASPHERE/9f804b8efa8043539289f42f372c4862/5454a8cfdb9845a9b6c772d63b...](https:/...