---
title: Troubleshooting HTTP errors in SAP Cloud Integration (Inbound)
url: https://blogs.sap.com/2022/12/28/troubleshooting-http-errors-in-sap-cloud-integration-inbound/
source: SAP Blogs
date: 2022-12-29
fetch_date: 2025-10-04T02:39:53.045518
---

# Troubleshooting HTTP errors in SAP Cloud Integration (Inbound)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Troubleshooting HTTP errors in SAP Cloud Integrati...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160216&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Troubleshooting HTTP errors in SAP Cloud Integration (Inbound)](/t5/technology-blog-posts-by-sap/troubleshooting-http-errors-in-sap-cloud-integration-inbound/ba-p/13556953)

![vitor_lemberck](https://avatars.profile.sap.com/6/3/id63f65c8c78aa9158a8b0ba969e6ac98e4994949e0b14539b23317cc3c5bb32e5_small.jpeg "vitor_lemberck")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[vitor\_lemberck](https://community.sap.com/t5/user/viewprofilepage/user-id/240248)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160216)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160216)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556953)

‎2022 Dec 28
8:37 AM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160216/tab/all-users "Click here to see who gave kudos to this post.")

17,477

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (2)

## Introduction

The focus of the blog is to help you understand and analyze all the HTTP errors that happen during the connection from your sender system to your Cloud Integration (inbound). Also, this blog will provide some troubleshooting tips that will help better understand where exactly is the problem and how to avoid/prevent it in the future
To better understand this blog post, it is expected that you have some kind of knowledge of Cloud Integration Inbound configuration. It is advised to read SAP Help below, which has a great explanation of how each type of Inbound configuration works:

* [Configuring Inbound Communication](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/62690e524ddc4b9b9fb95a25928a08b0.html)

It is also advisable to read the Blog below (depending on whether your environment system is NEO or Cloud Foundry) for a better explanation of the configuration using Client Certificates:

* [Cloud Integration on CF – How to Setup Secure HTTP Inbound Connection with Client Certificates](https://blogs.sap.com/2019/08/14/cloud-integration-on-cf-how-to-setup-secure-http-inbound-connection-with-client-certificates/)
* [Cloud Integration – How to Setup Secure HTTP Inbound Connection with Client Certificates](https://blogs.sap.com/2017/06/05/cloud-integration-how-to-setup-secure-http-inbound-connection-with-client-certificates/)

## Troubleshooting

After creating your scenario to connect to Cloud Integration, some types of HTTP errors may appear in the sender side. Each error has a few different causes, for example, the HTTP 404 error can be caused by a wrong endpoint configuration or an internal problem in the worker nodes of your system. To distinguish what is causing the error and how to solve it, we can use some logs and tips.

### Necessary traces/logs

Cloud Integration has two logs that together can provide more detailed information about the problem. You can access this log from the Monitoring Dashboard. In the section *Access Logs* select the *System Log Files* tile. You get a list of log files with the most recent files at the top. There are one or more *HTTP Access or LJS/Trace* files with nearly the same time stamp, one for each runtime node started in your tenant. Because you don’t know at which runtime node the request arrives, you need to check all of those files. Later in the blog, I will give tips on which file to download to check for errors more precisely.

**Note:** The Default trace logs from Cloud Integration may be named LJS\_trace.log or Trace.log (depending on whether your system is in NEO or Cloud Foundry) but they are the same logs.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-21_15-11-44.gif)
**HTTP Access Log:**
For each inbound call reaching the Cloud Integration runtime node, one line is written into the HTTP Access Log containing the IP address of the calling system, the certificate or user contained in the request, the date, the path, and the HTTP return code. Through this blog, we can also be sure that the call has reached Cloud Integration. The line in the log file has the following format:

* <IP Address> – <certificate or user> [<Date>] GET <path> HTTP/1.1 <return code>

**LJS log or Trace log**:
If the certificate is received, but there is an error during the authorization check, you should consult the *LJS Trace* (also known as *CP Default Trace)* for more details about the error. The formatting of the log that is written to this trace log is varied and can depend on each thread. But it usually has this format:

* <Timestamp> #<Timezone>#<Severity>#<Class>##<user>#

Sample:

* 2022 12 21 10:35:00#+00#ERROR#com.sap.it.nm.core.concurrent.lock.ClusterLock##anonymous#

**Log Node ID**
The log ID is what links an HTTP to an LJS. If your tenant has multiple runtime nodes you can use the ID of your HTTP logs to know which LJS/Trace log to use to check for more details of the error. Check the name of the *HTTP Access Log* file, where you found the request, to get the ID of the runtime node (LJS/Trace file). The name of the file has the following format: *http\_access\_<**Node ID**>\_<date>.log*. The Node ID is the ID of the runtime node, that received the request. Search for the corresponding *CP Default Trace* with the same node ID, file name format: ljs\_trace\_<**Node ID**>\_<date>.log.

### Additional necessary information

In addition to the logs, the following information (in the *Sample* part) will help in analyzing the problem. The main one is the *Path* of your Iflow. The *Path* is the URL that your Iflow uses to identify external calls. It is unique to each Iflow and when called by some system it will start the Iflow. It is set in the sender adapter (parameter *Address*) of your iflow.

1. Go to your Cloud Integration Monitor > Click in *All* tile of *Manage Integration Content;*
2. Search for the Integration Iflow in *Search Field*;
3. Check the *Endpoint* tab.

![](/legacyfs/online/storage/blog_attachments/2022/12/endpointMa.gif)
The path of our example iflow will be '*http/Inboudtestconnection'.*![](/legacyfs/online/storage/blog_attachments/2022/12/Endpoint.png)

### Analyzing the Problem

Now we have the necessary information from the Iflow where the error is happening (using the *Path*) and we know which logs to use. For better accuracy of the analysis, it is advisable that you reproduce the problem again (callin...