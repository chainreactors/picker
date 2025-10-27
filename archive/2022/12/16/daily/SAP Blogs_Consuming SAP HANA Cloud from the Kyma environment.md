---
title: Consuming SAP HANA Cloud from the Kyma environment
url: https://blogs.sap.com/2022/12/15/consuming-sap-hana-cloud-from-the-kyma-environment/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:06.666699
---

# Consuming SAP HANA Cloud from the Kyma environment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Consuming SAP HANA Cloud from the Kyma environment

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158722&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Consuming SAP HANA Cloud from the Kyma environment](/t5/technology-blog-posts-by-sap/consuming-sap-hana-cloud-from-the-kyma-environment/ba-p/13552718)

![tom_slee](https://avatars.profile.sap.com/6/f/id6fbfb39fad6d365c74068937133729469945b0bcc4f568f05403325ede856bfb_small.jpeg "tom_slee")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[tom\_slee](https://community.sap.com/t5/user/viewprofilepage/user-id/160000)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158722)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158722)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552718)

‎2022 Dec 15
8:59 PM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158722/tab/all-users "Click here to see who gave kudos to this post.")

8,516

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (2)

(January 2023: this material can now be found in the help at [Map an SAP HANA Database to another Environment Context | SAP Help Portal](https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/1683421d02474567a54a81615e8e2c48.html), including command-line instructions)

SAP Business Technology Platform (BTP) applications looking to store their data in SAP HANA Cloud typically do so using a HANA Cloud schema or HDI container, which is hosted in an SAP HANA database instance. For a long time, most applications on BTP were developed and deployed on the Cloud Foundry runtime environment, but recently the Kubernetes-based Kyma runtime has become increasingly important for developing and hosting applications.

Until October 2022, access to SAP HANA Cloud relied on Cloud Foundry, but with the release of [multi-environmentt HANA Cloud tools](https://blogs.sap.com/2022/09/21/sap-hana-cloud-goes-multi-environment-part-1-feature-overview/), that changed. You can now access the HANA Cloud tools to provision and manage database instances at the level of a subaccount (rather than a Cloud Foundry space), or you can [use the btp command line interface](https://blogs.sap.com/2022/12/09/automation-with-the-btp-command-line-interface-logging-in-with-passcodes/) to create, start and stop instances. However, even with this new multi-environment approach, you could not develop applications in Kyma that used HANA HDI containers or HANA schemas to store data.

(*Disclaimer:* This is probably a pretty specialized post. It takes the terms in the paragraphs above as understood. If they don't mean anything to you, this may not be the blog post for you.)

If you prefer a video introduction to this topic, you can get that from the always-excellent SAP HANA Academy channel on YouTube [here](https://www.youtube.com/watch?v=h17LuFK4RHI&list=PLkzo92owKnVw3l4fqcLoQalyFi9K4-UdY).

## Overview

With the December 2022 release of the SAP HANA Cloud Tools, you can now develop Kyma applications that work with HANA HDI containers and schemas. This blog post explains one essential part of what you need to do.

The overall process is as follows:

1. From the multi-environment edition of SAP HANA Cloud Central or using the btp CLI, provision a HANA database instance in a subaccount.

2. From the multi-environment edition of SAP HANA Cloud Central, use the "instance mapping" feature to map the instance into a Kyma namespace (or Cloud Foundry space), either in the same subaccount or in a different subaccount.

3. From the Kyma dashboard or using the kubectl CLI, create an HDI container or HANA schema service instance that creates a container or instance in the "mapped" HANA Cloud database instance.

4. From the Kyma dashboard or using the kubectl CLI, create a service binding to the HDI container.

5. Your application can now consume the HANA Cloud service through the service binding.

This blog post covers steps 2, 3, and 4. The process is not simple, but once the instance mapping is done, you may be able to use that HANA Cloud database instance for many HDI containers or schemas.

## Prerequisites

In your subaccount you must subscribe to both the SAP HANA Cloud service and the SAP HANA Schemas & HDI Containers service.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-31-47.png)

Make sure you have subscribed to the *tools* application service, which is the SAP HANA Cloud multi-environment tools.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-35-49.png)

Also make sure your SAP HANA Schemas & HDI Containers service is available in the Kyma environment. Here I will just use the *schema* service plan.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-37-19.png)

## Map a HANA Cloud database instance into a Kyma namespace

I assume you have provisioned an SAP HANA Cloud instance in your subaccount, using the [multi-environment HANA Cloud Tools](https://blogs.sap.com/2022/09/21/sap-hana-cloud-goes-multi-environment-part-1-feature-overview/). Also, that you have a Kyma namespace from where you want to access the instance. For me, that namespace is in the same subaccount, but that need not be so. Here is my namespace *tom-namespace* in the Kyma dashboard.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-00-58.png)

To map a HANA Cloud database instance you must also know the Environment Instance ID of the Kyma runtime environment. In the Kyma dashboard you can find this under Namespaces > kyma-system.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-18-14.png)

Click the kyma-system link, then go to Configuration > Config Maps, and search for sap-btp-operator-config.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-20-13.png)

Open the sap-btp-operator-config Config Map and copy the CLUSTER ID identifier to the clipboard. You will need to paste this into your SAP HANA Cloud Central instance mapping dialog.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_15-21-27.png)

Now, from SAP HANA Cloud Central, you can set up the instance mapping into your Kyma namespace.

From SAP HANA Cloud Central, click the three dots and open Manage Configuration.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-15_14-55-06.png)

Click **Edit** in the top right, then **Instance Mapping,** then **Add Mapping**. Choose a Kyma environment type, enter ...