---
title: SAP Commissions – Smart Data Integration[SDI] – Part 7d
url: https://blogs.sap.com/2023/06/11/sap-commissions-smart-data-integrationsdi-part-7d/
source: SAP Blogs
date: 2023-06-12
fetch_date: 2025-10-04T11:45:50.429635
---

# SAP Commissions – Smart Data Integration[SDI] – Part 7d

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions – Smart Data Integration[SDI] – Pa...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6108&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions – Smart Data Integration[SDI] – Part 7d](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-smart-data-integration-sdi-part-7d/ba-p/13561984)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6108)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6108)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561984)

‎2023 Jun 11
9:05 AM

[2
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6108/tab/all-users "Click here to see who gave kudos to this post.")

1,689

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)

View products (2)

Dear All,

This article is intended for database admins, consultants, customers & partners to enable the **OdataAdapter**  & configure in your SDI Project![](/legacyfs/online/storage/blog_attachments/2023/06/Open-Data-Protocol-OData-Services-for-SAP-Business-Suite.png)

---

## Create a Remote Source

Right-click on **Remote Sources**. Choose **Add Remote Source**![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-17_20-46-51.png)
Here you can define the Source Name (arbitary), the Adapter will be the OdataAdapter![](/legacyfs/online/storage/blog_attachments/2023/06/2023-06-11_09-39-50.png)

Select Credentials Mode : Technical User which supports currently Basic Authentication and in future it will support Client Credentials.

Note : Credentials is your SAP Commissions RestAPI User ( Refer the SAP Commissions Blogs on RestAPI)![](/legacyfs/online/storage/blog_attachments/2023/06/2023-06-11_09-40-11.png)
Click **Create**

Check the remote objects to make sure configuration has been successful and to complete the validation below.![](/legacyfs/online/storage/blog_attachments/2023/06/2023-06-11_09-51-23.png)
Also you can CREATE REMOTE SOURCE using below statement in your webIDE

```
CREATE REMOTE SOURCE "Odata_Pipeline"
ADAPTER "ODataAdapter" AT LOCATION DPSERVER
CONFIGURATION '<?xml version="1.0" encoding="UTF-8"?>
               <ConnectionProperties name="UI">
               <PropertyEntry name="URL">https://<TENANTID>.callidusondemand.com:443/TrueComp-SaaS/CommissionsService.svc</PropertyEntry>
               <PropertyEntry name="proxyserver"></PropertyEntry>
               <PropertyEntry name="proxyport"></PropertyEntry>
               <PropertyEntry name="truststore"></PropertyEntry>
               <PropertyEntry name="isﬁletruststore"></PropertyEntry>
               <PropertyEntry name="supportformatquery">true</PropertyEntry>
               <PropertyEntry name="requireCSRFheader"></PropertyEntry>
               <PropertyEntry name="CSRFheadername"></PropertyEntry>
               <PropertyEntry name="CSRFheaderfetchvalue"></PropertyEntry>
               <PropertyEntry name="supportdatefunctions"></PropertyEntry>
               <PropertyEntry name="shownavigationproperties"></PropertyEntry>
               <PropertyEntry name="supportEncodingGzip"></PropertyEntry>
               <PropertyEntry name="followRedirects"></PropertyEntry>
               <PropertyEntry name="extraconnectionparameters"></PropertyEntry>
               <PropertyEntry name="verifyServerCertiﬁcate"></PropertyEntry>
               </ConnectionProperties> '
               WITH CREDENTIAL TYPE 'PASSWORD' USING
               '<CredentialEntry name="password">
               <user>enter your username</user>
               <password>enter your password here </password>
               </CredentialEntry>';
```

## For GCP

```
CREATE REMOTE SOURCE "Odata_Pipeline" ADAPTER "ODataAdapter" AT LOCATION DPSERVER CONFIGURATION
'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ConnectionProperties name="connection_properties">
<PropertyEntry name="URL">https://XXXXX.app.dev.commissions.dev.sap/cng-pipeline/odata/</PropertyEntry>
<PropertyEntry name="authenticationType">OAuth2</PropertyEntry>
<PropertyEntry name="oauth2TokenEndpoint">https://XXXXXXX.accounts.ondemand.com/oauth2/token</PropertyEntry>
<PropertyEntry name="enableSSLAnonymous">True</PropertyEntry>
</ConnectionProperties>'
    WITH CREDENTIAL TYPE 'PASSWORD' USING
    '<CredentialEntry name="oauth2" displayName="OAuth2 Credential">
<user displayName="OAuth2 Client ID">256aa599-09eb-42da-b048-78942728f9ac</user>
<password displayName="OAuth2 Client Secret">?SnLvKMjrM1X15rv-RuTDrV5XX:TVPJbI</password>
</CredentialEntry>';
```

---

## Create a Virtual Table

you will have to create a Virtual table by connecting to your remote source to load the data into table.

```
CREATE VIRTUAL TABLE "EXT"."VT_Pipeline" at "Odata_Pipeline"."<NULL>"."<NULL>"."PipelineRuns";
```

you can preview your Virtual table if that’s displaying all the Pipeline fields (Table : CS\_PLRUN)![](/legacyfs/online/storage/blog_attachments/2023/06/2023-06-11_10-02-54.png)
**R**eferences

[SAP Commissions – Smart Data Integration[SDI] – Part 1](https://blogs.sap.com/2021/08/02/sap-commissions-smart-data-integrationsdi-part-1/)

[SAP Commissions – Smart Data Integration[SDI] – Part 2](https://blogs.sap.com/2022/02/01/sap-commissions-smart-data-integrationsdi-part-2/)

[SAP Commissions – Smart Data Integration[SDI] – Part 3](https://blogs.sap.com/2022/02/08/sap-commissions-smart-data-integrationsdi-part-3/)

[SAP Commissions – Smart Data Integration[SDI] – Part 4](https://blogs.sap.com/2022/04/07/sap-commissions-smart-data-integrationsdi-part-4/)

[SAP Commissions – Smart Data Integration[SDI] – Part 5](https://blogs.sap.com/2022/04/07/sap-commissions-smart-data-integrationsdi-part-4/)

[SAP Commissions – Smart Data Integration[SDI] – Part 6](https://blogs.sap.com/2023/03/25/sap-commissions-smart-data-integrationsdi-part-6/)

[SAP Commissions – Smart Data Integration[SDI] – Part 7a](https://blogs.sap.com/2023/05/19/sap-commissions-smart-data-integrationsdi-part-7/)

[SAP Commissio...