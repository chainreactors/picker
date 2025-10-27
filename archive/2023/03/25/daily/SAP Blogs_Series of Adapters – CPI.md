---
title: Series of Adapters – CPI
url: https://blogs.sap.com/2023/03/24/series-of-adapters-cpi/
source: SAP Blogs
date: 2023-03-25
fetch_date: 2025-10-04T10:36:46.086189
---

# Series of Adapters – CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Series of Adapters - CPI

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160431&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Series of Adapters - CPI](/t5/technology-blog-posts-by-members/series-of-adapters-cpi/ba-p/13552325)

![GopisettySai](https://avatars.profile.sap.com/9/d/id9d26e04e850d83c4f9c8bcce278074a6d90aacf36113b4f8ad2af62fe7b4e093_small.jpeg "GopisettySai")

[GopisettySai](https://community.sap.com/t5/user/viewprofilepage/user-id/149967)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160431)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160431)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552325)

‎2023 Mar 24
11:57 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160431/tab/all-users "Click here to see who gave kudos to this post.")

18,654

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

Chapter 1 - HTTP Adapter

In the world of enterprise integration, adapters play a crucial role in connecting different systems and applications. In SAP CPI (Cloud Platform Integration), there are a wide variety of adapters available that can work as both sender and receiver, allowing data to flow seamlessly between different systems.

In this blog post, we'll take a closer look at the HTTP adapter, one of the most widely used adapters in SAP CPI. We'll explore its features, use cases, and provide step-by-step instructions for configuring the adapter as both a sender and receiver.

By the end of this blog post, readers will have a better understanding of the HTTP adapter and how it can be used to integrate systems in their organization.

HTTP Adapter Overview

The HTTP adapter is a lightweight adapter that can be used as both a sender and receiver to exchange data between different systems over HTTP/HTTPS protocols. The HTTP adapter supports various message formats such as XML, JSON, and plain text, making it a versatile option for integration scenarios.

Use Cases

The HTTP adapter can be used in a wide range of integration scenarios, including:

* Connecting cloud and on-premise systems

* Exchanging data with external partners and vendors

* Integrating different applications within an organization

## Configuring the Sender HTTP Adapter:

![](/legacyfs/online/storage/blog_attachments/2023/03/Sender_HTTP_Adapter.png)

#### Address Field:

The Address field should start with '/ ' and can contain alphanumeric values, '\_' and '/ '. For example, a valid address is /test/123

#### Authorization:

You can select one of the following options:

1)User role

Allows you to enter a role based on which the inbound authorization is checked.

The role ESBMessaging.send is provided by default. It is a predefined role provided by SAP which authorizes a sender system to process messages on a tenant.

2)Client Certificate

Allows you to select one or more client certificates (based on which the inbound authorization is checked).

Choose Add Option to add a new certificate for inbound authorization for the selected adapter. You can then select a certificate stored locally on your computer. You can also delete certificates from the list.

For each certificate, the following attributes are displayed: Subject DN (information used to authorize the sender) and Issuer DN (information about the certificate authority that issues the certificate).

In SAP BTP cockpit, select the subaccount that hosts your SAP Cloud Integration virtual environment and create a service instance and service key.

Proceed as described under [Creating Service Instance and Service Key for Inbound Authentication](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/19af5e205fe14af6a4f8a9fd80d4dc92.html).

For this use case, specify the service instance and service key parameters as follows:

![](/legacyfs/online/storage/blog_attachments/2023/03/Service_Instance-1.png)

#### CSRF Protected:

This option prevents Cross-Site Request Forgery (CSRF), which is a malicious online attack. Such attacks expose user content without their authorization.

#### Conditions:

Body Size : It gives you option to set a maximum size limit to the payload body.

![](/legacyfs/online/storage/blog_attachments/2023/03/conditions.png)

## Configuring the Receiver HTTP Adapter:

![](/legacyfs/online/storage/blog_attachments/2023/03/Receiver_http_adapter.png)

#### Address:

Enter the target system URL, which we need to connect. If we need to connect to a dynamic URL then we can pass the URL from runtime. If we are getting the URL from headers, we need to specify ${header.name} if it is from exchange property, we need to specify ${property.name}.

#### Query:

Every URL call contains a query, when we are posting data to the receiver system. That query cannot be given in the address field. The Query can be externalized, and we can get it from the runtime too like URL.

#### Proxy Type:

The type of proxy that we are using to connect to the target system:

1)Internet: If we are connecting to a cloud system, we can use the option “Internet”.

2)On-Premise : If we are connecting to a on-premise system, then we need to add the URL in cloud connector

#### Location Id:

These can be used only when we select the On-Premise proxy type.

#### Method:

This gives the scope what http operation need to perform. CPI is covered with all the HTTP operations like GET, POST,DELETE,DYNAMIC,HEAD,PUT,PATCH,TRACE.

#### Authentication:

It Defines in which authentication method we need to connect to the receiver system.

We can use :

1)None

If there is no authentication method, then we will use None method.

2)Basic

If we receiver system has basic method, we will add the user-id and password in security material and call the key value.

And we have other Methods like Client Certificate, Oauth2 credentials, OAuth2 SAML Bearer Assertion.

Where we will be using the methods according to the receiver system and do the necessary configuration.

#### Timeout:

It gives us scope to wait for the response back from receiver system without terminating the message processing.

#### Throw Exception on Failure:

By default, the option is enabled. This option throws an exception w...