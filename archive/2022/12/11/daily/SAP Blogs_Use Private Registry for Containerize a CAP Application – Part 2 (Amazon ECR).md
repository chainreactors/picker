---
title: Use Private Registry for Containerize a CAP Application – Part 2 (Amazon ECR)
url: https://blogs.sap.com/2022/12/10/use-private-registry-for-containerize-a-cap-application-part-2-amazon-ecr/
source: SAP Blogs
date: 2022-12-11
fetch_date: 2025-10-04T01:12:20.134702
---

# Use Private Registry for Containerize a CAP Application – Part 2 (Amazon ECR)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Use Private Registry for Containerize a CAP Applic...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161430&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Use Private Registry for Containerize a CAP Application – Part 2 (Amazon ECR)](/t5/technology-blog-posts-by-sap/use-private-registry-for-containerize-a-cap-application-part-2-amazon-ecr/ba-p/13560809)

![lalitmohan](https://avatars.profile.sap.com/4/d/id4dd8a7a057f018170e1925ef2a912e57921bd84e15123909d0de4b3dd687ddbc_small.jpeg "lalitmohan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[lalitmohan](https://community.sap.com/t5/user/viewprofilepage/user-id/1038)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161430)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161430)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560809)

‎2022 Dec 10
6:05 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161430/tab/all-users "Click here to see who gave kudos to this post.")

1,139

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (1)

Welcome Back! In my first blog post([click here](https://blogs.sap.com/2022/11/01/use-private-registry-for-containerize-a-cap-application-part-1/)), we tried to understand the advantages of private registries over public registries. Additionally, we understand how to choose the best container registry based on customers' needs and compare the leading container registries available in the market.

One of the top registries in the current market is [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/)**,**an AWS-managed container image registry service that is secure, scalable, and reliable. It offers resource-based permissions on private and public image repositories using AWS IAM. For additional information, [click here](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).

This blog article aims to use the Amazon ECR to containerize your Simple CAP Application. It includes tagging the local image to the Private registry tags and pushing it to the Amazon ECR private repositories, as well as how to pull the application's image and run it.![](/legacyfs/online/storage/blog_attachments/2022/11/1-62.png)

## Prerequisite

You need to have the following:

1. A valid AWS account is configured with multi-factor authentication (MFA) to help protect your AWS resources. If not, please follow the [Create and Activate a new AWS account.](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)

2. [Install the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)for your operating system. If already installed, check the CLI version and update it if required.

3. Install the CDS tools by following the steps mentioned in the [link](https://cap.cloud.sap/docs/get-started/#local-setup).

4. **Git** is the version control system that you need to download files. If you don’t have it, go to [Git downloads](https://git-scm.com/downloads), pick the installer appropriate for your operating system and install it.

5. Choose **VS Code** as an editor. If you don’t have it, go to the [Visual Studio Code](https://code.visualstudio.com/) homepage and install it.

6. You need to have a server-side javascript runtime environment called NodeJS. [Download](https://nodejs.org/en/) and install (Node.js version 12.x or 14.x is recommended).

## Let’s proceed step by step

Before we will start, first download the repository, and then the relevant branch will be selected. Go to your computer's terminal and enter the following:

```
git clone https://github.com/SAP-samples/cloud-cap-risk-management

cd cloud-cap-risk-management

git checkout create-ui-fiori-elements
```

### **Step 1: Run the CAP Application in a Docker Container Locally**

Since we intend to use the CAP Application's docker image, we need to create a docker image for the CAP application. You must create a file called a Dockerfile that specifies how to build the image and what to do when it is executed.

Create a file named Dockerfile and add the following lines to it:

```
FROM node:14-slim

WORKDIR /usr/src/app

COPY gen/srv .

RUN npm install

COPY app app/

COPY db/data db/data/

RUN find app -name '*.cds' | xargs rm -f

EXPOSE 4004

USER node

CMD [ "npm", "start" ]
```

Since you don't want to start from scratch, the FROM directive at the beginning of the file specifies the base image you want to utilise. In this case, you utilise a public image that comes pre-installed with NodeJS 14.x. Following that, you declare that the CAP default port 4004 is open to outside traffic and start the CAP server with npm.

To simplify, we can try out the scenario without an external database server. First, delete the developer dependency for sqlite3 and then it can be introduced again as a runtime dependency.

```
npm i sqlite3 -P
```

Add the following snippet to the package.json file:

```
{

  "name": "capapp",

  ...

  "cds": {

    "requires": {

      "db": {

        "kind": "sql"

      }

    }

  }

}
```

Run cds build first since the image uses the build results from the gen/srv folder before you can create it.

```
cds build
```

Build the docker image locally:

```
docker build -t capapp .
```

Docker images are made up of various "filesystem layers." Your customized Docker image is a layer on top of the basic image. A file can be added or removed for each layer.

Run the Docker Container:

```
docker run --rm -p 4004:4004 -t capapp
```

This instructs Docker to expose port 4004 on the host to traffic from Port 4004 on the Docker container. You could also use a different host port, but let's keep things straightforward.

The CAP service is now available at <http://localhost:4004>.

### **Step 2: Create the** **IAM user's****Access Keys & Add Permission.**

Open the IAM console by logging into the AWS Management Console at <https://console.aws.amazon.com/iam/>

Select **Users** in the navigation pane and choose the **Security credentials** tab after selecting the user's name. Make a note of the **Serial numbe**r, or select [Assign MFA device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) from [Multi-factor authentication(MFA)](https://aws.amazon.com/iam/features/mfa/) if you don't have a virtual MFA device.

![](/legacyfs/online/storage/blog_attachments/2022/12/12-4.png)

Select **Create access key** from the Access keys section.

![](/legacyfs/online/storage/blog_attachments/2022/12/13-4.png)

**Note:** S...