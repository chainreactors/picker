---
title: Prepare Oracle Driver vsolution in SAP Data Intelligence
url: https://blogs.sap.com/2023/06/30/prepare-oracle-driver-vsolution-in-sap-data-intelligence/
source: SAP Blogs
date: 2023-07-01
fetch_date: 2025-10-04T11:53:59.357037
---

# Prepare Oracle Driver vsolution in SAP Data Intelligence

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Prepare Oracle Driver vsolution in SAP Data Intell...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157155&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Prepare Oracle Driver vsolution in SAP Data Intelligence](/t5/technology-blog-posts-by-sap/prepare-oracle-driver-vsolution-in-sap-data-intelligence/ba-p/13548533)

![cschuerings](https://avatars.profile.sap.com/8/2/id825d0dfd54e5e47e23c1eac1009344827b234c817258c39dc7bb9a353bdfe0c8_small.jpeg "cschuerings")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[cschuerings](https://community.sap.com/t5/user/viewprofilepage/user-id/123540)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157155)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157155)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548533)

‎2023 Jun 30
9:58 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157155/tab/all-users "Click here to see who gave kudos to this post.")

1,099

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)

View products (1)

In case you want to connect SAP Data Intelligence to Oracle, the oracle driver needs to be prepared according to the [Data Intelligence: Administration Guide -> ORACLE Connection](https://help.sap.com/docs/SAP_DATA_INTELLIGENCE/ca509b7635484070a655738be408da63/e5eb77dc74a4413d817912655233a7cc.html?locale=en-US).

The steps, which are mentioned in the Prerequisites section, require an UNIX environment. If you try to execute the steps on a windows machine, symbolic links are lost and the oracle driver vsolution is not recognized.

The following guide explains how the Prerequisite steps can be executed in the SAP Data Intelligence environment within 3 steps.

[Guide created & tested with Data Intelligence Cloud Version 2308.14.35]

## Step 1: Prepare a Dockerfile

Create a new Dockerfile (You can refer [creating dockerfiles](https://help.sap.com/docs/SAP_DATA_INTELLIGENCE/1c1341f6911f4da5a35b191b40b426c8/62d1df08fa384d0e88bbe9b7cbd2c3fb.html?locale=en-US) for the detailed steps of creating a Dockerfile in SAP Data Intelligence). The first instructions are copied from the org.opensuse sample in Data Intelligence and are needed to run a graph with this Docker container.

```
FROM opensuse/leap:15.4

# Install required tools and Python 3.9

RUN zypper --non-interactive update && \

 zypper --non-interactive install --no-recommends --force-resolution \

     tar \

     gzip \

     gcc \

     gcc-c++ \

     wget \

     libgthread-2_0-0 \

     python39 \

     python39-pip

 # Install required python modules

RUN python3.9 -m pip --no-cache install \

   tornado==6.1.0 \

   jsonpath-python==1.0.5 \

   oauthlib==3.1.0 \

   requests-oauthlib==1.3.1 \

   pandas==1.2.5 \

   pyarrow==4.0.1 \

   u-msgpack-python==2.7.1

# Setup dedicated vflow user

RUN groupadd -g 1972 vflow && useradd -g 1972 -u 1972 -m vflow

USER 1972:1972

WORKDIR /home/vflow

ENV HOME=/home/vflow
```

Next we add the instructions for the oracle driver preparation to the Dockerfile (Hint: Here we use Oracle driver version 19.17.0.0 here). The instructions are explained in [Data Intelligence: Administration Guide -> ORACLE Connection](https://help.sap.com/docs/SAP_DATA_INTELLIGENCE/ca509b7635484070a655738be408da63/e5eb77dc74a4413d817912655233a7cc.html?locale=en-US).

The output of the instructions is a zip file within the Docker container in the current working directory.

```
## Start preparing Oracle driver

USER root

# Install zip and unzip

RUN zypper --non-interactive install --no-recommends --force-resolution zip unzip

USER 1972

# Download Oracle driver package

RUN curl -s --location https://download.oracle.com/otn_software/linux/instantclient/1917000/instantclient-basiclite-linux.x... --output instantclient-basiclite-linux.x64-19.17.0.0.0dbru.zip

RUN mkdir -p oracle_vsolution/content/files/flowagent

RUN unzip instantclient-basiclite-linux.x64-19.17.0.0.0dbru.zip -d oracle_vsolution/content/files/flowagent/

RUN echo '{    "name": "vsolution_oracle",    "version": "19.17.0",    "format": "2",    "dependencies": []}' > oracle_vsolution/manifest.json

RUN mkdir -p oracle_vsolution/content/files/flowagent/orapki

# Download Oracle JDBC

RUN curl -s --location https://download.oracle.com/otn-pub/otn_software/jdbc/1917/ojdbc8-full.tar.gz > ojdbc8-full.tar.gz

RUN tar -xzvf ojdbc8-full.tar.gz

RUN cp ojdbc8-full/oraclepki.jar oracle_vsolution/content/files/flowagent/orapki/

RUN cp ojdbc8-full/osdt_core.jar oracle_vsolution/content/files/flowagent/orapki/

RUN cp ojdbc8-full/osdt_cert.jar oracle_vsolution/content/files/flowagent/orapki/

RUN echo 'ORACLE_INSTANT_CLIENT=./instantclient_19_17' > oracle_vsolution/content/files/flowagent/oracle.properties

RUN echo 'NLS_LANG=AMERICAN_AMERICA.UTF8' >> oracle_vsolution/content/files/flowagent/oracle.properties

RUN echo 'ORACLE_ORAPKI_PATH=./orapki' >> oracle_vsolution/content/files/flowagent/oracle.properties

# create oracle solution

RUN cd oracle_vsolution && zip -y -r oracle_vsolution.zip ./

RUN mv oracle_vsolution/oracle_vsolution.zip ./
```

Last add the following tags to the Dockerfile:

* oracle\_driver

* python36

* tornado 5.0.2

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-tags.png)

##

## Step 2: Create a Pipeline

Next, a Data Intelligence Pipeline is needed to copy the oracle\_vsolution zip archive from the Docker container into the Data Intelligence filesystem.

The first python operator is used to send a *cp oracle\_vsolution.zip /vrep/oracle\_vsolution.zip* statement to the Command Executor operator. After the successful copy operation, the graph is terminated.

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-graph.png)

```
{

	"properties": {},

	"description": "Copy oracle driver solution from the Docker container to the DI filesystem.",

	"processes": {

		"commandexecutor1": {

			"component": "com.sap.system.commandExecutor",

			"metadata": {

				"label": "Command Executor",

				"x": 292,

				"y": 40,

				"height": 80,

				"width": 120,

				"generation": 1,

				"config": {

					"cmdLine": "bash"

				}

			}

		},

		"python3operator1": {

			"component": "com.sap.system.python3Operator",

			"metadata": {

				"label": "Python3: Trigger command",

				"x": 24,

				"y": 40,

				"height": 80,

				"width": 120,

				"extensible": true,

				"filesRequired": [

					"script.py"

				],

				"generation": 1,

				"config": {

					"script": "def gen():\n    api.send(\"output\", \"cp oracle_vsolution.zip /vrep/oracle_vsolution.zip\")\n\napi.add_generator(gen)\n"

				},

				"additionaloutports": [

					{

						"name": "output",

						"type": "string"

					}

				...