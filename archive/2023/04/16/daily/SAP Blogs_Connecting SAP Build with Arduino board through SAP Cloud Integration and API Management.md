---
title: Connecting SAP Build with Arduino board through SAP Cloud Integration and API Management
url: https://blogs.sap.com/2023/04/15/connecting-sap-build-with-arduino-board-through-sap-cloud-integration-and-api-management/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:25.294055
---

# Connecting SAP Build with Arduino board through SAP Cloud Integration and API Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Connecting SAP Build with Arduino board through SA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160656&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Connecting SAP Build with Arduino board through SAP Cloud Integration and API Management](/t5/technology-blog-posts-by-members/connecting-sap-build-with-arduino-board-through-sap-cloud-integration-and/ba-p/13553639)

![former_member793421](https://avatars.profile.sap.com/former_member_small.jpeg "former_member793421")

[former\_member793421](https://community.sap.com/t5/user/viewprofilepage/user-id/793421)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160656)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160656)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553639)

‎2023 Apr 15
7:10 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160656/tab/all-users "Click here to see who gave kudos to this post.")

2,055

* SAP Managed Tags
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

View products (5)

# Scenario Overview

The idea behind this project came as soon as I got my hands on an Arduino ESP32 board. With the help of SAP Build, I created a mobile application that communicates with the board using the architecture provided by the [SAP Business Technology Platform](https://www.sap.com/products/technology-platform.html) and it's able to do multiple tasks. For the sake of simplicity, we stuck to only turning on and off LEDs that are connected to the Arduino ESP32 board, but this type communication can support any sort of task by controlling the power output of the board pins.

## Solution Overview

The following picture gives an overview of the intended setup of the solution and the request flows in between:

![](/legacyfs/online/storage/blog_attachments/2023/04/hackathon.drawio-2.png)

Solution Overview

An end user can use the [SAP Build](https://www.sap.com/products/technology-platform/low-code.html) mobile application, go into the buttons page and turn ON or OFF the LEDs connected to the Arduino ESP32 board. In the background there are multiple calls being made between several platforms, in the end succesfully changing the output power of the pins.

## Technical setup

The first step was to find a way to expose the Arduino ESP32 Board to the Internet, and it meant we had to create a HTTP Web Server. This was possible using a C++ script that uses a WiFi library, connects to the local WiFi and generates a local server.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-6-3.png)

HTTP Server start-up

Using GET calls from Postman or any web browser to the local host ( - <http://<router_IP>:<port>>; ) we are able to set the output power of the LEDs.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-7-1.png)

HTTP GET Calls for each LED

SAP Build is not able to do any sort of call to unsecured servers, so it meant we had to use SAP Cloud Connector to expose it to the internet in a secure communication and SAP Cloud Integration in order to be able to access the on-premise location.

In the [SAP Cloud Connector](https://help.sap.com/docs/r/cca91383641e40ffbe03bdc78f00f681/Cloud/en-US/e6c7616abb5710148cfcf3e75d96d596.html) we exposed the local host as a Non-SAP system, and then we added the resources that we needed - the paths for turning on or off the LEDs.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-5-2.png)

SAP Cloud Connector Setup

After this step, we can go into [SAP Cloud Integration](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/e12c09cc8e9b4574b092d8964b049ce6.html?locale=en-US) and create a small iFlow that uses a HTTP Sender adapter in order to be called from SAP Build and a HTTP Receiver adapter for the communication with the Arduino board.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-8-1.png)

SAP Cloud Integration Setup

The first Groovyscript extracts the query parameters sent by SAP Build :

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-9-1.png)

Groovyscript for parameter extraction

I will later go back to this step because I will explain how the parameter value work, because as you can see, we have a value map in this script.

In order to succesfully call SAP Cloud Integration endpoints from SAP Build, we had to dive into SAP API Management and handle the CORS policies.

As a reference for this part we have used [this](https://blogs.sap.com/2022/07/26/integrate-sap-appgyver-with-sap-integration-suite-consuming-an-integration-flow-levering-sap-api-management-policies/) and [this](https://blogs.sap.com/2022/12/15/cloud-integration-with-sap-build-app-appgyver/) blogs by priyanka2018and mariajosemq741 and we have binded the HTTP endpoint of the above iFlow with an API created by us that is handling the 'OPTIONS' header, thus enabling communication with SAP Build.

![](/legacyfs/online/storage/blog_attachments/2023/04/WhatsApp-Image-2023-04-15-at-21.23.27.jpeg)

SAP Build home page

Going to the SAP Build part, we had to create logic behind a button in order to do proper GET calls to the LEDs for the SAP Cloud Connector to interpret them.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-12.png)

SAP Build Data page for connections

Adding the ApiKey provided by the binded application in [API Management](https://help.sap.com/docs/sap-api-management/sap-api-management/what-is-api-management?locale=en-US) is mandatory, otherwise SAP Build won't be able to do any sort of call because of the CORS policies not being satisfied.

![](/legacyfs/online/storage/blog_attachments/2023/04/MicrosoftTeams-image-11.png)

SAP Build Buttons page

The logic behind each button handles two calls that are triggered by pressing them. The fi...