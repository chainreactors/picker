---
title: Setting Up Point-to-Point Integration with Client-certificate based Authentication in Employee Central Payroll
url: https://blogs.sap.com/2023/01/24/setting-up-point-to-point-integration-with-client-certificate-based-authentication-in-employee-central-payroll/
source: SAP Blogs
date: 2023-01-25
fetch_date: 2025-10-04T04:43:34.552239
---

# Setting Up Point-to-Point Integration with Client-certificate based Authentication in Employee Central Payroll

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Setting Up Point-to-Point Integration with Client-...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6351&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Setting Up Point-to-Point Integration with Client-certificate based Authentication in Employee Central Payroll](/t5/human-capital-management-blog-posts-by-sap/setting-up-point-to-point-integration-with-client-certificate-based/ba-p/13570357)

![lsharma](https://avatars.profile.sap.com/6/7/id67755183b624a58dd57877974a3b091390b790c5be4c8444b9634f8cc48c8b5b_small.jpeg "lsharma")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[lsharma](https://community.sap.com/t5/user/viewprofilepage/user-id/22128)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6351)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6351)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570357)

‎2023 Jan 24
8:51 PM

[11
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6351/tab/all-users "Click here to see who gave kudos to this post.")

12,954

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central Payroll](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll/pd-p/67837800100800006744)
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)

* [SAP SuccessFactors Employee Central Payroll

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll/pd-p/67837800100800006744)
* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (3)

Setting up a point-to-point integration with client-certificate based authentication between Employee Central Payroll and SuccessFactors can provide an added layer of security for sensitive payroll data. Here are the general steps to set up such integration:

1. Obtain client certificates: Both Employee Central Payroll and SuccessFactors must have their own client certificates. These certificates are used to identify the systems during the authentication process.

2. Configure the systems: In Employee Central Payroll and SuccessFactors, configure the integration settings to use client-certificate based authentication. This includes specifying the certificate file and the private key.

3. Exchange certificates: The two systems must exchange their client certificates. This is done by sharing the certificate files between the systems.

4. Test the integration: Test the integration to ensure that the two systems are able to communicate securely.

5. Set up the data mapping: Map the data fields between Employee Central Payroll and SuccessFactors. This ensures that the data is passed between the systems correctly.

6. Configure security: Configure the security settings for the integration, such as setting up roles and permissions for users.

7. Monitor and maintain the integration: Monitor the integration to ensure that it is working correctly and make any necessary adjustments. It is important to keep the client certificates updated and maintain the integration settings to ensure that the communication between the systems remains secure.

It's important to note that this is a high-level overview of the process and the actual implementation may require additional steps and expertise.

In this blog I am going to show that how we can connect ECP with EC system using Client Certificate. Please follow the procedure as given below:

A. Start transaction STRUST in ECP and export the public key as described in [Exporting Client Certificates from STRUST](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL_PAYROLL/6267c9dbd7114f0da47b39c1b4cf0367/1b1fe9aa923847f09004127725ab17bf.html?locale=en-US&state=PRODUCTION&version=2211).

1. 1. Run transaction STRUST in the Customizing for **Integration Settings for SuccessFactors Employee Central Payroll**  **Certificate Handling**  **Export Certificates**

   2. From the left pane, select the SSL client certificate 100\_SD.![](/legacyfs/online/storage/blog_attachments/2023/01/STRUST.jpg)

      1. Double click on the certificate displayed in **Subject** of the **Own Certificate** section.

      2. Choose the edit icon and choose **Export Certificate**.

      3. In the **Export Certificate** dialog box, browse the file path in

      4. which you want to export the certificate. Provide a file name with .cer extension.

      5. Choose **File Format** as **Base64**. Choose **OK**.![](/legacyfs/online/storage/blog_attachments/2023/01/Base64.jpg)

The certificate is exported to the selected file path.

In the Employee Central Security Center, import the public key as described in [Importing Client Certificates to the Security Center](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL_PAYROLL/6267c9dbd7114f0da47b39c1b4cf0367/dae87ef7bb1949bd8bf2770351128cb1.html?locale=en-US&state=PRODUCTION&version=2211).

B. Importing Client Certificates to the Security Center

Exported certificate can be uploaded to Employee Central using the Security Center.

#### Procedure

1. First Check role based permissions for Security Center![](/legacyfs/online/storage/blog_attachments/2023/01/RBP.jpg)

2. In the Employee Central system, go to the **Security Center**.

3. Select **509 Public Certificate Mapping**.

![](/legacyfs/online/storage/blog_attachments/2023/01/Security-Center.jpg)

Security Center

4. Choose **Add**.

![](/legacyfs/online/storage/blog_attachments/2023/01/ADD.jpg)

ADD

4. Provide the following data:

|
 **Field** |
 **Description** |

|
 Configuration Name |
 Example: New X509 Certificate Mapping |

|
 Integration Name |
 Default is Employee Central Payroll |

|
 Certificate File |
 Select the corresponding file with the cer extension. |

|
 Login Name |
 Is the Employee Central user you defined in [Granting Permissions for Full Access to the CompoundEmployee API](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/5bb9a5b997a843c88e769a105e4af4d4/bc3eb7d3fca64b4a8d6f56c66183d8ef.html) |

6. Choose **Upload File**.

![](/legacyfs/online/storage/blog_attachments/2023/01/Upload.jpg)

Upload

The certificate is imported to the selected file path.

![](/legacyfs/online/storage/blog_attachments/2023/01/Upload-2.jpg)

Upload 2

Now check the Connection between ECP and EC

1. Goto Tcode HRS...