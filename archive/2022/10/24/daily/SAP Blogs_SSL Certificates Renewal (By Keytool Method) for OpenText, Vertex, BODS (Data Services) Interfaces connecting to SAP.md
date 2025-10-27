---
title: SSL Certificates Renewal (By Keytool Method) for OpenText, Vertex, BODS (Data Services) Interfaces connecting to SAP
url: https://blogs.sap.com/2022/10/23/ssl-certificates-renewal-by-keytool-method-for-opentext-vertex-bods-data-services-interfaces-connecting-to-sap/
source: SAP Blogs
date: 2022-10-24
fetch_date: 2025-10-03T20:43:21.102213
---

# SSL Certificates Renewal (By Keytool Method) for OpenText, Vertex, BODS (Data Services) Interfaces connecting to SAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SSL Certificates Renewal (By Keytool Method) for O...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67216&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SSL Certificates Renewal (By Keytool Method) for OpenText, Vertex, BODS (Data Services) Interfaces connecting to SAP](/t5/enterprise-resource-planning-blog-posts-by-members/ssl-certificates-renewal-by-keytool-method-for-opentext-vertex-bods-data/ba-p/13552557)

![kiranchavan0912](https://avatars.profile.sap.com/2/1/id21e77e5d4804dd6e9f376c90fb45c5f77e8bf9c7f489f91e512219783cad0f1c_small.jpeg "kiranchavan0912")

[kiranchavan0912](https://community.sap.com/t5/user/viewprofilepage/user-id/808708)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67216)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67216)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552557)

‎2022 Oct 23
8:37 PM

0
Kudos

6,476

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

Hello Everyone,

Recently, We have renewed the SSL certificates for OpenText, Vertex, BODS (Data Services) Interfaces hosted on windows environment and connecting to SAP S4HANA system. All above mentioned Interfaces are well known and widely used with SAP systems. The SSL certificate renewal process is quite similar for all above mentioned interfaces, as tomcat is being used to provide SSL functionality. We will be using **keytool** to generate the CSR and install the certificate in windows.

**Steps:**

**1.** First step is to figure out, how the existing SSL setup has been done. Check the installation directories of applications (OpenText, Vertex, BODS). also checkout the **tomcat\conf** folder is maintained under which windows drive. You will find **server** file with extension **XML**.This is the file where this entire process plays around.

**2.**The **server.xml** file looks like below if you open it in notepad. Basically you need to find section where **.jks** or **.p12** file is mentioned with path.

![](/legacyfs/online/storage/blog_attachments/2022/10/xml-file.png)

sample paths to get server.xml file for interfaces :

**Data services(BODS)** - *D:\SAP BusinessObject\Tomcat\conf\<sever.xml>*

**OpenText -**  *C:\Program Files\ Apache Software Foundation\ Tomact 8.5\conf\<sever.xml>*

**Vertex-**  *E:\Vertex\Oseries\Tomact\conf\<sever.xml>*

*Note. Above mentioned paths are given for example purpose, It may change in your environment, so check accordingly before proceeding.*

**3.** Now we will need keytool application to generate the CSR and install the certificates.Use the '**keytool.exe**' tool within the '**javasdk\bin**' or '**java\bin**' or '**sapjvm\bin**' folder, so check accordingly in your windows server.

**4.** Now to generate CSR, you have use **command prompt/ cmd** of your windows server (where application is installed) in administrator mode.

**5.** Before running below keytool command, navigate to path where keytool application is present. For simplicity lets create one SSL2 folder in C drive and we will be using the same folder to place new files which is getting generated now onwards.

After that run below command:

**keytool -genkeypair -keyalg RSA -keysize 2048 -alias <your Alias> -ext SAN=dns:<your required dns>,keystore <C:\SSL2\XYZ.jks> -storetype JKS -dname "EMAILADDRESS=<Email Details>,CN=<your data>,O=<your data >,L=<>,C=<your data>"**

Note: CN, O, L,C details you will find in your old certificate under details tab under subject.

![](/legacyfs/online/storage/blog_attachments/2022/10/CSR.png)

This will ask to give keystore password, I would prefer to give same password which is used for previous .jks file, hence kindly give the same password which is maintained in server.xml file. Refer 1st screenshot of this blog i.e step 2.

*Note: As per above screenshot my keytool executable file is present under* *E:\SAP BusinessObject\SAP BusinessObject Enterprise XI 4.0\win64\_x64\sapjvm\bin file path hence, I navigated to this path then ran the command*.

**6.** Next step is to generate the certificate request. Use below command for the same.

**keytool -certreq -file C:\SSL2\ABC.csr -keystore C:\SSL2\XYZ.jks -alias <Your Alias> -ext SAN=dns<your required dns>,"EMAILADDRESS=<Email Details>,CN=<your data>,O=<your data >,L=<>,C=<your data>"**

![](/legacyfs/online/storage/blog_attachments/2022/10/xml-file-2.png)

Note: In above screenshot, multiple dns entries have been added. so consider accordingly as per your requirement.

Here, use the same keystore password which you have used in step 5.

**7.** Important point is to note down the alias name, which you had used to create .jks and .csr file. It should be the same and same needs to be used at the time of certificate import to .jks.

**8.** Step 6 will generate the **ABC.csr** file at SSL2 folder in C drive, share the same file to the certification authority and get it signed. certification Authority will generate the certificate and share with you.Validate the SAN (dns), validity of the new certificate.Get the Root and intermediate certificate exported from this certificate and place them at SSL2 Folder itself.

**9.** In order to import the certificate. Basically you have to import Root, Intermediate and Server certficate to the  **XYZ.jks** file, which was generated in step 5.

**10.** Use below commands to import the certificate to **XYZ.jks** file, which is ultimately being used in **server.xml** file to provide SSL functionality.

**Commands:**

1. **keytool -import -trustcacerts -alias ROOT -file C:\SSL2\<Root\_certficate\_name.cer > -keystore C:\SSL2\XYZ.jks**

2. **keytool -import -trustcacerts -alias Intermediate -file C:\SSL2\<Intermediate\_certficate\_name.cer> -keystore C:\SSL2\XYZ.jks**

3. **keytool -import -trustcacerts -alias <Your alias> -file C:\SSL2\<Your\_New\_certfiacte.cer> -keystore C:\SSL2\XYZ.jks**

**11.** After executing 1st Root certificate command it will give you the prompt for keystore password, here use the password which was being used throughout to generate csr. and next Prompt will be that Trust this certificate? wherein you have  to write **yes**

**12.** This way you have to add all three certificate to your **XYZ.jks** file.

Note: For Root and Intermediate certificate addition the message you will get is '**Certificate was added to keystore'** and for last server certficate you will get the message that '**Certificate reply was installed in keystore'**

**13.** Now next step is to maintain this **XYZ.jks** file in **server.xml** file. Make sure you are taking backup of server.xml file before editing the same. To edit the file open notepad in administrator mode and then edit the file.

**14**.After maintaining the **XYZ.jks** file and keystore password in server.xml file, you need to take tomca...