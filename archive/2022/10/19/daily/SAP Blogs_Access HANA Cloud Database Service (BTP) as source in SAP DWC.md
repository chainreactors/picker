---
title: Access HANA Cloud Database Service (BTP) as source in SAP DWC
url: https://blogs.sap.com/2022/10/18/access-hana-cloud-database-service-btp-as-source-in-sap-dwc/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:14:55.265496
---

# Access HANA Cloud Database Service (BTP) as source in SAP DWC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Access HANA Cloud Database Service (BTP) as source...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159890&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Access HANA Cloud Database Service (BTP) as source in SAP DWC](/t5/technology-blog-posts-by-members/access-hana-cloud-database-service-btp-as-source-in-sap-dwc/ba-p/13548777)

![sukanya_krishnan](https://avatars.profile.sap.com/5/d/id5d114c7e075632f72864f863330f9854f72dc6c8c6fdd37b2cd85fd12d01b564_small.jpeg "sukanya_krishnan")

[sukanya\_krishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/210193)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159890)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159890)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548777)

‎2022 Oct 18
6:07 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159890/tab/all-users "Click here to see who gave kudos to this post.")

2,300

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

**Overview**

SAP DWC can connect to several SAP and Non-SAP sources. It can connect to SAP sources -  S/4HANA , SAP ECC , SAP Success Factors etc. ; SAP Data Warehouses -  SAP BW4HANA , SAP HANA Database ; Open Connectors , oData/REST API's etc. Let's understand how SAP DWC can connect to HANA Cloud database service, up and running in SAP BTP.

Integrate SAP DWC and HANA Cloud Service in SAP BTP

Two options to integrate

1. Use the HANA cloud underneath of DWC  - read/write data from HDI container in DWC

2. If separate HANA Cloud instance is running as service in BTP, same can be used as source in DWC

* For the first option, we need to map the HDI Container (created in BTP) with DWC tenant . Support ticket needs to be raised for this with DWC tenant details , BTP Organization and Space. This mapping can be possible only if "The SAP Data Warehouse Cloud tenant and SAP Business Technology Platform organization and space are in the same data center (for example, eu10, us10)."

* For the second option, we can access HDI container of HANA Cloud (database service in BTP) in SAP DWC by just leveraging the run time credentials

In this blog we would be focusing on second option

**Pre-requisites**

* Access to BTP  ( In this blog, I leveraged trial version)

* HANA database as service in BTP

* Ensure you have subscription to BAS - Business Application Studio and your dev space is up and running

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img1-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img2.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img3.png)

Now let's create a project with HANA artifacts and access the same from DWC

* Create a project leveraging HANA artifacts. I have created a calculation view accessing SBOOK table o SFLIGHT schema and calculated the "Number of booking made per Agency on specific dates"

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img4-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img5.png)

Now let's access this view in DWC

* Identify the run time credentials to be leveraged for DWC

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img6.png)

* In the BTP cockpit, you will find the new HDI project that's created "TheProj-hdidb-ws-tbgc4" and service key associated to it. Click on the Key.

  + Row 12 has the runtime user ( one with suffix \_RT)

  + Row 9 has the password

  + Copy the host id from Row 8

  + Copy the certificate enclosed between "BEGIN CERTIFICATE" and  "END CERTIFICATE" and create a \*.cer file

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img7.png)

* DWC accepts only "Base 64 encoded X.509" certificate format .In case your certificate is not in this format, you can export to required format. Click on "Copy to File" button in Details tab

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img8.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img9.png)

Now log into DWC

* In the configuration tab, upload the certificate just created

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img10.png)

* Go to Connections and create the connection with the credentials we noted down above

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img11.png)

* Both data flows and remote tables can be created leveraging this connection. Now we can access the view we create in BTP HANA Cloud

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img12.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog5Img13.png)

**Summary**

We have now created a connection between HANA Database service in BTP and SAP DWC. Using this we can access the tables in HANA and create the modelling here in DWC or directly access the calculation views created in HANA. HANA & DWC artifacts can also be exposed as oData Services.

* [BTP](/t5/tag/BTP/tg-p/board-id/technology-blog-members)
* [DWC](/t5/tag/DWC/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Faccess-hana-cloud-database-service-btp-as-source-in-sap-dwc%2Fba-p%2F13548777%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  13m ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  21m ago
* [Creating a Hybrid CAP (Node.js) Profile with PostgreSQL on BTP from Business Application Studio](/t5/technology-blog-posts-by-members/creating-a-hybrid-cap-node-js-profile-with-postgresql-on-btp-from-business/ba-p/14233631)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Calculation View Features of 2025 QRC3](/t5/technology-blog-posts-by-sap/calculation-view-features-of-2025-qrc3/ba-p/14192411)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [How to Enable SAP Authentication for Vite-React app Using xs-security.json & mta?](/t5/technology-q-a/how-to-enable-sap-authentication-for-vi...