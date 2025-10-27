---
title: Power of serverless with SAP BTP, Kyma runtime. Base image override.
url: https://blogs.sap.com/2023/01/29/power-of-serverless-with-sap-btp-kyma-runtime.-base-image-override./
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:12.988829
---

# Power of serverless with SAP BTP, Kyma runtime. Base image override.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Power of serverless with SAP BTP, Kyma runtime. Ba...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157578&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Power of serverless with SAP BTP, Kyma runtime. Base image override.](/t5/technology-blog-posts-by-sap/power-of-serverless-with-sap-btp-kyma-runtime-base-image-override/ba-p/13549795)

![quovadis](https://avatars.profile.sap.com/5/f/id5f0d9937a29017f07c2dd14f033b8d49b11261952ae7ce68ec448c7d5c66f338_small.jpeg "quovadis")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[quovadis](https://community.sap.com/t5/user/viewprofilepage/user-id/743)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157578)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157578)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549795)

‎2023 Jan 29
9:28 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157578/tab/all-users "Click here to see who gave kudos to this post.")

2,066

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

|
 [![](/legacyfs/online/storage/blog_attachments/2021/06/SAP_Business_Technology_Platform_R.png)](https://www.sap.com/products/business-technology-platform.html) |

|
 [![Serverless architecture](https://raw.githubusercontent.com/kyma-project/serverless-manager/main/docs/assets/svls-architecture.svg)](https://kyma-project.io/#/serverless-manager/user/technical-reference/04-10-architecture) |
 This brief is to demonstrate how one can leverage selected SAP BTP Kyma runtime serverless features.    This instalment covers:    * **how to override a base function image** |

|
 Requirements and Disclaimers:    * [https://github.com/SAP-samples/kyma-runtime-extension-samples/tree/main/kyma-serverless#requirements...](https://github.com/SAP-samples/kyma-runtime-extension-samples/tree/main/kyma-serverless#requirements-and-disclaimers)         ---     Sample code:    * [Power of serverless with SAP BTP, Kyma runtime code sample](https://github.com/SAP-samples/kyma-runtime-extension-samples/tree/main/kyma-serverless/fun)  * [hana-cloud gist](https://gist.github.com/ptesny/382b08659eb8952fda35aedd824c0274#file-hana-cloud-md) |

# Putting it all together.

SAP BTP, Kyma runtime is SAP's fully managed commercial kubernetes offering, part of SAP Business Technology Platform. It is often bundled with SAP Commerce Cloud and nowadays is becoming an extensibility runtime of choice.

[Kyma](https://github.com/kyma-project/kyma/releases/tag/2.19.2) brings additional modules on top of a kubernetes cluster. And [**serverless manager**](https://github.com/kyma-project/serverless-manager/tree/main) is one of them.

Good to know:

* The **serverless** features described in this and following instalments can be used with both **unmanaged** [OS Kyma](https://kyma-project.io/) on [Gardener](https://gardener.cloud/) and **SAP-managed** SAP BTP, Kyma runtime.

## [Serverless Architecture](https://kyma-project.io/docs/kyma/latest/05-technical-reference/00-architecture/svls-01-architecture/)

The serveless [architecture](https://kyma-project.io/docs/kyma/latest/05-technical-reference/00-architecture/svls-01-architecture/) is far from being trivial. Please study the diagram carefully.

Next, let's have a look at the [Function's specification](https://kyma-project.io/#/serverless-manager/user/technical-reference/07-70-function-specification).

Seemingly, one of the coolest features with Kyma **serverless** CRD is the ability to [override](https://kyma-project.io/#/serverless-manager/user/technical-reference/07-70-function-specification?id=override-runtime-image) the base runtime image of a function.

This can be really useful when the [default runtime image](https://console.cloud.google.com/gcr/images/kyma-project/eu/function-runtime-nodejs16) is just not good enough to accommodate some specific runtime dependencies.

However, please mind the gap. The kyma default base runtime function images are Alpine based. And Alpine based nodejs images have an extremely low count of security vulnerabilities;

## [Override function base image](https://kyma-project.io/#/serverless-manager/user/technical-reference/07-70-function-specification?id=override-runtime-image)

For the sake of this brief, let's try it out with the **nodejs16** functions. However, same approach is valid with any other supported serverless runtime, for instance with python 3.9.

In order to replace a default base image of a nodejs16 function we should try to understand how kyma does it.

Let's have a look at a [Dockerfile definition](https://github.com/kyma-project/serverless-manager/blob/main/components/runtimes/nodejs/nodejs16/Dockerfile) used by kyma itself to create a function base image, namely:

```
# image base on 16.19.0-alpine3.17

FROM node@sha256:e427ffd1ba7915ca8d8aeba45806ef3f1f1e6b65ce152b363645cd7428f8d75a

ARG NODE_ENV

ENV NODE_ENV $NODE_ENV

ENV npm_config_cache /tmp/

RUN mkdir -p /usr/src/app

RUN mkdir -p /usr/src/app/lib

WORKDIR /usr/src/app

COPY package.json /usr/src/app/

RUN npm install && npm cache clean --force

COPY lib /usr/src/app/lib

COPY server.js /usr/src/app/server.js

CMD ["npm", "start"]

EXPOSE 8888
```

The build of the above Dockerfile will result in the following [stock image](https://console.cloud.google.com/gcr/images/kyma-project/eu/function-runtime-nodejs16%40sha256%3A84379029e4b8b041236176ab56e8c4da3dc3a1e7fc6d72c571a07b12321a122f/details), that eventually will be used in the function kaniko build

```
eu.gcr.io/kyma-project/function-runtime-nodejs16:v20230117-d8ab8401
```

Good to know:

* The docker files used in the function build are stored as config maps in a kyma cluster namespaces. Goto your cluster to look them up.

### Building a custom image.

In order the build a custom image first you need to clone the project kyma github [repository](https://github.com/kyma-project/kyma):

```
gh repo clone kyma-project/kyma

cd components/function-runtimes/nodejs16/

...............

add your Dockerfile, build the custom image and push it

to an internet facing docker repository

...............

cp Dockerfile Dockerfile.custom.nodejs16

nano Dockerfile.cus...