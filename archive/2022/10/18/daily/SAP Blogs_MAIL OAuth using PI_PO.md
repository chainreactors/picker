---
title: MAIL OAuth using PI/PO
url: https://blogs.sap.com/2022/10/17/mail-oauth-using-pi-po/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:07:01.009609
---

# MAIL OAuth using PI/PO

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* MAIL OAuth using PI/PO

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/158840&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [MAIL OAuth using PI/PO](/t5/technology-blog-posts-by-members/mail-oauth-using-pi-po/ba-p/13542839)

![dilipkkp2412](https://avatars.profile.sap.com/8/4/id8486a1fd18112a304415a6925abb012dc657ac5faa5c646a8f40b336f01fd0eb_small.jpeg "dilipkkp2412")

[dilipkkp2412](https://community.sap.com/t5/user/viewprofilepage/user-id/528730)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=158840)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/158840)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13542839)

‎2022 Oct 17
9:13 PM

0
Kudos

4,205

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)

View products (1)

## Overview:

* Business Requirement: Read mails from a specific mail-folder having specific subject line of a Microsoft outlook mail-account, extract the attachments (.csv files) and store them into local directories.

* Mail OAuth can also be achieved using Mail Adapters "Configure OAuth" Authentication feature.

* This blog gives an overview of an alternative (Java-Map) can be used into the PI/PO interface, where "Mail OAuth 2.0" (access token based) authentication mechanism is been applied.

## Pre-requisites:

Following pre-requisites needs to be taken care of:

1. Get specific mail-id's credentials like Client\_ID, Client\_Secret, Tenant\_ID. For same, below Microsoft Guide link can be referred:

   * [Authenticate an IMAP, POP or SMTP connection using OAuth](https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth)

   * [Quickstart: Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

2. Understand how to fetch Access-Token using Microsoft-outlook-API protocols as below:

   * URL:          [https://login.microsoftonline.com/<token-ID>/oauth2/v2.0/token](https://login.microsoftonline.com/%3Ctoken-ID%3E/oauth2/v2.0/token)

   * Method:     POST

   * Headers:    "Content-Type", "application/x-www-form-urlencoded"

   * Request:

     + grant\_type      client\_credentials

     + client\_id          *<mail-id's secret value>*

     + client\_secret   *<mail-id's secret value>*

     + scope               <https://outlook.office365.com/.default>

   * ```
     grant_type=client_credentials&client_id=<client-ID-value>&client_secret=<client-secret-value>&scope=https://outlook.office365.com/.default​
     ```

   * Response:

     ```
     {

         "token_type": "Bearer",

         "expires_in": 3599,

         "ext_expires_in": 3599,

         "access_token": "<access token value>"

     }
     ```

   * Using POSTMAN tool, we can call access-token API as depicted in below screen![](/legacyfs/online/storage/blog_attachments/2022/10/postman.png)

   * Here, TLS version and Cipher Suite required for this API also needs to be understood, the same should be present in PI/PO layer as well.

3. To allow connection between PI/PO and outlook mail, the Firewall whitelisting rule should be in place having source as PI/PO system and destination having below Microsoft's FQDN

   * login.microsoftonline.com    HTTPS-Port 443

   * outlook.office.com                HTTPS-Port 443

   * outlook.office365.com          HTTPS-Port 443, IMAP-Port 993, 143, POP3-Port 110, SMTP-Port 25

4. PI/PO system should support/have below:

* + TLS Protocol TLSv1.2

  + Cipher Suite  ECDHE-RSA-AES256-GCM-SHA384   [ in PI/PO ssl.properties having  "cipherSuite=TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384" ]

  + SSL ICM parameter at Kernel/OS layer "icm/HTTPS/client\_sni\_enabled = TRUE"

  + In PI/PO, import below SSL certificate chain of '<https://login.microsoftonline.com>'

  + ![](/legacyfs/online/storage/blog_attachments/2022/10/cert1-1.png)

  + Note: While running Java-Map from PI/PO layer, using XPI\_INSPECTOR LOG, we can understand in below screen, how SSL handshake takes place between PI/PO and login.microsoftonline.com while fetching the access-token :

    ![](/legacyfs/online/storage/blog_attachments/2022/10/ssl1.png)

##

## Mail OAuth using Java-Map Technique**:**

* Create a PI/PO interface as asynchronous outbound FILE-to-FILE

* Here, we need to have a dummy file in SAP-Folder. Configure Sender-FILE adapter channel to read this file on an fix poll interval (hourly, daily etc. as per business needs), keep processing mode 'Test'.

* Configure Receiver-FILE adapter channel to create a dummy file with different name having overwrite feature enabled.

* In ESR, create a SWCP and Namespace with dummy Data & Message Type. Import this Java-Map jar file and utilize into Operation Map.

* In ID, create integration configuration object (ICO), utilize the operation map having Java-Map program.

* Working of this PI/PO interface will be as follows:

  + On fix poll interval, say 2 hours, Sender-FILE-CC will keep reading dummy file from sap folder, which interns invokes Java-Map program and post Java-Program logic processing a dummy file will be created using Receiver-FILE-CC having Java-Map logs.

* The functionalities of Java-Map program is as follows:

  + Get Mail-ID's access token

  + Utilize the access-Token in next API, which is to read the unread mails of a specific mail-folder with specific subject-line.

  + **Note:** For reference, this Java-Map also has option about how to perform basic authentication (user-id/password based) to a mail account

###

### Contents of the Java map program:

1. Jar file ‘**aii\_map\_api.jar**’

   * Import it in Eclipse but no need to import in PI/PO ‘Enterprise Service Repository (ESR)’

2. Jar file ‘**javax.mail-1.6.2.jar**’

   * Import it in Eclipse but no need to import in PI/PO ‘ESR'

3. XML file ‘**credentialsMail.xml**’

   * Import this into Java-Program as resource file | This has mail account credentials (Test / Production both) in below XML structure manner

   * ```
     <?xml version="1.0" encoding="UTF-8"?>

     <MailCredentials>

     	<TEST>

     		<mail_clientId>***</mail_clientId>

     		<mail_tenantId>***</mail_tenantId>

     		<mail_secret>***</mail_secret>

     		<mail_scopeUrl>https://outlook.office365.com/.default</mail_scopeUrl>

     		<mail_accessTokenUrl>https://login.microsoftonline.com/(mail_tenantId)/oauth2/v2.0/token</mail_accessTokenUrl>

     		<mail_protocol>imaps</mail_protocol>

     		<mail_userEmail>XSD@ASD.com</mail_userEmail>

     		<mail_userPassword>ASA@ASASFDFD</mail_userPassword>

     		<mail_host>outlook.office365.com</mail_host>

     		<mail_port>993</mail_port>

     		<mail_folderToRead>Testing</mail_folderToRead>

     		<mail_subj...