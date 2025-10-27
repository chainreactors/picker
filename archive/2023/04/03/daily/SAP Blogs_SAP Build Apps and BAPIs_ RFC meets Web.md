---
title: SAP Build Apps and BAPIs: RFC meets Web
url: https://blogs.sap.com/2023/04/02/sap-build-apps-and-bapis-rfc-meets-web/
source: SAP Blogs
date: 2023-04-03
fetch_date: 2025-10-04T11:30:15.237716
---

# SAP Build Apps and BAPIs: RFC meets Web

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Build Apps and BAPIs: RFC meets Web

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51126&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build Apps and BAPIs: RFC meets Web](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-build-apps-and-bapis-rfc-meets-web/ba-p/13555549)

![Gunter](https://avatars.profile.sap.com/a/4/ida479f2e0596469f30f8f256760af4a49349a092dbda1284ed2860522f6ceccd8_small.jpeg "Gunter")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Gunter](https://community.sap.com/t5/user/viewprofilepage/user-id/727)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51126)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51126)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555549)

‎2023 Apr 02
11:17 AM

[19
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51126/tab/all-users "Click here to see who gave kudos to this post.")

9,680

* SAP Managed Tags
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [NW ABAP Remote Function Call (RFC)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Remote%2520Function%2520Call%2520%28RFC%29/pd-p/100394580653750417561290171292438)
* [SAP Java Connector (JCo)](https://community.sap.com/t5/c-khhcw49343/SAP%2520Java%2520Connector%2520%28JCo%29/pd-p/564816056037766647630637313516056)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [NW ABAP Remote Function Call (RFC)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BRemote%2BFunction%2BCall%2B%252528RFC%252529/pd-p/100394580653750417561290171292438)
* [SAP Java Connector (JCo)

  Software Product Function](/t5/c-khhcw49343/SAP%2BJava%2BConnector%2B%252528JCo%252529/pd-p/564816056037766647630637313516056)
* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

View products (6)

## ![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-02-164241.jpg)*"RFC meets Web"*

### Enable all your RFC functions for web consumption without development?

Today, I'm excited to share a new thing: A proxy on SAP BTP that translates from REST to SAP RFC calls, making it possible to use BAPIs and RFC-enabled function modules on **older SAP ECC** or S/4HANA systems.

This solution is particularly useful for SAP ERP users who are looking to integrate with systems that lack the new OData APIs that are only available on newer S/4HANA systems. With the REST-to-RFC proxy, RFC meets web, creating a seamless integration experience that unlocks the full potential of your SAP ecosystem.

**Benefits:**

* Protect your past investment: Use your function modules for the web

* RFC modules turned into synchronous REST APIs

* No further development work

* Secured communication through SAP BTP destinations

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-02-160900-1.png)

Image 1: Outline of solution - it works with any RFC function module (Y/Z-RFC modules included)

In this blog post, we'll take a closer look at how this proxy works, the benefits it provides, and the impact it can have on your SAP integration projects. So, let's dive in and discover the possibilities of web meets RFC!

## Solution approach

SAP BTP offers the destination service to define ways to connect to systems. Keeping destinations separate from applications makes them reusable and easy to maintain. They come in several flavors like:

1. HTTP - for anything like REST, OData-REST, HTML and the like.

2. LDAP - Lightweight Directory Access Protocol to lookup information in a network. Often used for organizational data of entities and persons.

3. MAIL - to send emails to an SMTP server

4. RFC - Remote Function Call, this is what we look at for the cloud connector-facing side.

From here we define the first destination to the [cloud connector](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/cloud-connector) (CC) as RFC. You need to white-list the function modules you plan to use in your cloud connector instance.

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-02-165040.jpg)

Image 2: Example of an RFC destination. The ashost is as defined in your CC.

I use this destination in the Java HTTPServlet. On the consumption side you'll need another destination that you can use for e.g. SAP Build Apps and which is provided by the HTTPServlet. If you secure it with OAuth2 the config could look like that.

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-02-165543.jpg)

Image 3: REST destination for consumption of BAPIs or RFC functions in general.

Since I use xsuaa for authentication and authorization I've defined 2 scopes to allow for display and change authorization.

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-02-170311.jpg)

Image 4: POST and GET related scopes to be assigned to relevant users for consumption.

The difference between the two is that the POST will trigger a BAPI.commit and therefore posts data in your S/4HANA or ECC system while the GET doesn't. Of course it depends on how you've designed your ABAP code - standard BAPIs will adhere to this approach.

## SAP Build Apps demo: Change material master

Enough talk! Let's see a demo built with SAP Build Apps. It uses 3 BAPIs:

1. BAPI\_MATERIAL\_GETLIST - To search for materials and get them in a list

2. BAPI\_MATERIAL\_GETALL - To retrieve the details of a selected material

3. BAPI\_MATERIAL\_SAVEDATA - To change some fields in the material master

There is no development done on both backend and frontend.

### 1. Mobile application

### 2. SAP Build and S/4HANA Backend

## Solution Architecture

Below are the schematics for using the REST to RFC proxy running on BTP Cloud Foundry.

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-01-220657-1.png)

Image 2: Solution architecture for REST-RFC proxy on SAP BTP Cloud Foundry

I'll explain the technical details in a second blog if you are interested to create such a proxy on BTP for yourself.

## Conclusion

And there it is: A proxy that opens all your RFC developments to the web in a secured manner. Hope it is useful!

Check my [second blog](ht...