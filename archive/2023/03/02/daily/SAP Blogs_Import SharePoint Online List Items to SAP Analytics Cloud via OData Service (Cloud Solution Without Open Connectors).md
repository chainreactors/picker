---
title: Import SharePoint Online List Items to SAP Analytics Cloud via OData Service (Cloud Solution Without Open Connectors)
url: https://blogs.sap.com/2023/03/01/import-sharepoint-online-list-items-to-sap-analytics-cloud-via-odata-service-cloud-solution-without-open-connectors/
source: SAP Blogs
date: 2023-03-02
fetch_date: 2025-10-04T08:26:34.425393
---

# Import SharePoint Online List Items to SAP Analytics Cloud via OData Service (Cloud Solution Without Open Connectors)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Import SharePoint Online List Items to SAP Analyti...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160805&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Import SharePoint Online List Items to SAP Analytics Cloud via OData Service (Cloud Solution Without Open Connectors)](/t5/technology-blog-posts-by-sap/import-sharepoint-online-list-items-to-sap-analytics-cloud-via-odata/ba-p/13558595)

![Wu-Dongxue](https://avatars.profile.sap.com/b/0/idb00ddfd7a1eb8b7a05dfb17c21657cb3cf373763c79c2a537d74fc98c08207d3_small.jpeg "Wu-Dongxue")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Wu-Dongxue](https://community.sap.com/t5/user/viewprofilepage/user-id/144417)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160805)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160805)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558595)

‎2023 Mar 01
11:14 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160805/tab/all-users "Click here to see who gave kudos to this post.")

7,316

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, connectivity](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520connectivity/pd-p/0db4caf8-3039-4a93-9d11-543de33255a4)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Analytics Cloud, connectivity

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bconnectivity/pd-p/0db4caf8-3039-4a93-9d11-543de33255a4)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (5)

# Context

With the increasing demands of the SAC users who want to connect to SharePoint List for data visualization and data analysis, I figured out a solution for SAC import connectivity against SharePoint Online List items via BTP Cloud Integration. To achieve it, I deployed an OData API Artifact to retrieve items from SharePoint List without Open Connectors and map entity framework. Compare to the method with Open Connectors, it simplified workflows and we don't need to configure EDMX or XSD files manually. This blog is to provide End to End connectivity guidance from SharePoint List Add-in Registration to SAC Connection Set up through SAP Integration Suite. Currently, we are not able to use the OAuth2 Client Credentials authentication method directly in SAC against SharePoint Online List as there is one more key-value pair (resource: 00000003-0000-0ff1-ce00-000000000000/<yourSharePointDomain>@TenantID) is required by SharePoint Online when getting the access\_token and SAC didn't provide a place to input this value in the connection dialog. Hence, the below method can be treated as a workaround without modifying the SharePoint OAuth issuer.

# Table of Contents

1. Register SharePoint Add-in

2. Assign Permission to Add-in

3. Obtain ClientID@TenantID

4. Use Postman to Get/Test Access Token and Credentials

5. Create OAuth2 credentials in Cloud Integration Suite

6. Create an OData API artifact in a Package

7. Bind Data Source

8. Configure OData Receiver

9. Configure Message Mapping

10. Deploy OData API

11. Create Instance and Credentials

12. Test Deployed OData API in Postman

13. Create/Test OData Service Connection in SAC

# Preparation:

* Found OData Service Endpoint URL of SharePoint Online subsite [https://<yourSharePointDomain>/sites/205434/\_vti\_bin/listdata.svc/](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/)

* Make sure we get list items from above URL by adding the list name at the end of the URL [https://](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/WuTestList2)[<yourSharePointDomain>](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/)[/sites/205434/\_vti\_bin/listdata.svc/WuTestList2](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/WuTestList2)

* Save xml file from [https://](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/%24metadata)[<yourSharePointDomain>](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/)[/sites/205434/\_vti\_bin/listdata.svc/$metadata](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/%24metadata)

* Copy the XML file and past it, then rename the file extension of the copied one to .edmx![](/legacyfs/online/storage/blog_attachments/2023/02/XML-and-EDMX-file.png)

# 1. Register SharePoint Add-in

1. Go to [https://](https://sap.sharepoint.com/sites/205434/_layouts/15/appregnew.aspx)[<yourSharePointDomain>](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/)[/sites/205434/\_layouts/15/appregnew.aspx](https://sap.sharepoint.com/sites/205434/_layouts/15/appregnew.aspx)

2. Click “Generate” for both Client id and Client Secret

3. Give a friendly name

4. Add Domain and Redirect URI

5. Click “Create” and note down the information

   |
    Client Id:            5d57...8bac    Client Secret:    bbc7...TTA=    Title:      WuTestList2App    App Domain:      localhost    Redirect URI:      <https://localhost> |

# 2. Assign Permission to Add-in

1. Go to [https://](https://sap.sharepoint.com/sites/205434/_layouts/15/appinv.aspx)[<yourSharePointDomain>](https://sap.sharepoint.com/sites/205434/_vti_bin/listdata.svc/)[/sites/205434/\_layouts/15/appinv.aspx](https://sap.sharepoint.com/sites/205434/_layouts/15/appinv.aspx)

2. Copy Client Id into the App id filed

3. Click “Lookup”

4. Copy below XML to Permission Request XML. **Please also refer to learn.microsoft.com “[Table 2. SharePoint add-in permission scope URIs and available rights](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/add-in-permissions-in-sharepoint#permission-request-scopes-for-list-content-and-library-content:~:text=Table%202.%20SharePoint%20add%2Din%20permission%20scope%20URIs%20and%20available%20rights)****” And narrow down the permission according to the organization's security policy**. In this example, I will copy all of them to provide insights into how it impacts permissions.

5. ```
   <AppPermissionRequests AllowAppOnlyPolicy="true">

     <AppPermissionRequest Scope="http://sharepoint/content/sitecollect...