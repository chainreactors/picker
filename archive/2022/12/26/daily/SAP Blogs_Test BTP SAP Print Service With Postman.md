---
title: Test BTP SAP Print Service With Postman
url: https://blogs.sap.com/2022/12/25/test-btp-sap-print-service-with-postman/
source: SAP Blogs
date: 2022-12-26
fetch_date: 2025-10-04T02:31:05.631515
---

# Test BTP SAP Print Service With Postman

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Test BTP SAP Print Service With Postman

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160752&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Test BTP SAP Print Service With Postman](/t5/technology-blog-posts-by-sap/test-btp-sap-print-service-with-postman/ba-p/13558408)

![Jacky_Liu1](https://avatars.profile.sap.com/0/c/id0c96fbc6ecfa4651eccd3b5e561d0848734220dc92c2198772bae6ac9168e7b7_small.jpeg "Jacky_Liu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jacky\_Liu1](https://community.sap.com/t5/user/viewprofilepage/user-id/132085)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160752)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160752)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558408)

‎2022 Dec 25
4:56 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160752/tab/all-users "Click here to see who gave kudos to this post.")

2,518

* SAP Managed Tags
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (2)

In the blog [SAP Print Service](https://blogs.sap.com/2021/03/02/sap-print-service/), markus.berg has introduce BTP SAP Print Service. In my following 2 blogs, I will introduce how to configure, how to test, and how to use it in UI5 . There is mission [Add Printing Label to Your User Experience for SAP S/4HANA Cloud](https://discovery-center.cloud.sap/protected/index.html#/missiondetail/3766/3805/).in which a S4Hana Cloud side by side extension for label printing has been introduced in detail.  Configure printing service is big part of it . You can find detailed information in the mission also .

### Prerequisite:

You have installed [postman](https://www.postman.com/downloads/) on your computer .

### Step 1, Check entitlement in BTP cockpit in your sub-account, the following 3 printing service plans should be listed .

To do this, the role Subaccount Admin should be assigned to your user . If you can not find the following 3 print service plans , please contact your BTP customer success manager .

![](/legacyfs/online/storage/blog_attachments/2022/12/p01-scaled.jpg)

### Step 2, Onboarding.

In this step you will create service instances for plan sender and receiver.Service keys for plan sender and receiver will be created .To take out this step you can use [Booster](https://help.sap.com/docs/SCP_PRINT_SERVICE/07d0692a5a994703992d7538ad78d54b/16db0e9ca4784733954253e80c518c27.html) from BTP cockpit in global account. Plan sender is used to upload document and create printing task. Plan receiver will be used by cloud printing manager to connect.

![](/legacyfs/online/storage/blog_attachments/2022/12/p2-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/p3-1-scaled.jpg)

### Step 3, Create subscription for print service plan standard configure authorization

You can following the [document](https://help.sap.com/docs/SCP_PRINT_SERVICE/07d0692a5a994703992d7538ad78d54b/1d0ff45da748477daad74fc619948879.html) to create print service subscription .

For authorization configuration , you can follow the following documents :

[Defining and Bundling Roles](https://help.sap.com/docs/SCP_PRINT_SERVICE/07d0692a5a994703992d7538ad78d54b/3f49b088f5b948af8afa4682c931618c.html)

[Assigning Role Collections to Users](https://help.sap.com/docs/SCP_PRINT_SERVICE/07d0692a5a994703992d7538ad78d54b/e0f578278b784a598caef3ab4bdb6f3c.html)

[Configuring Role Collection](https://help.sap.com/docs/SCP_PRINT_SERVICE/07d0692a5a994703992d7538ad78d54b/9ae895e0327c476081a6b719e31ef282.html)

### Step 3, Create printQ .

![](/legacyfs/online/storage/blog_attachments/2022/12/p4-1-scaled.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/p5-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/p6-1-scaled.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/p7-1.jpg)

### Step 4, Note down service key information of service instance of plan sender .

![](/legacyfs/online/storage/blog_attachments/2022/12/p16-1-scaled.jpg)

Note down the information in the red frame .

![](/legacyfs/online/storage/blog_attachments/2022/12/p17-2.jpg)

### Step 5, Save postman collection content as a  json file.

```
{

	"info": {

		"_postman_id": "43b9377d-9355-4e0b-bd4f-044c9deb6d9d",

		"name": "print",

		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"

	},

	"item": [

		{

			"name": "Step1 Get Token",

			"event": [

				{

					"listen": "test",

					"script": {

						"exec": [

							"pm.collectionVariables.set(\"bearToken\",\"Bearer \".concat(pm.response.json().access_token))"

						],

						"type": "text/javascript"

					}

				}

			],

			"request": {

				"auth": {

					"type": "basic",

					"basic": [

						{

							"key": "password",

							"value": "{{printclientsecret}}",

							"type": "string"

						},

						{

							"key": "username",

							"value": "{{printclientkey}}",

							"type": "string"

						}

					]

				},

				"method": "POST",

				"header": [],

				"body": {

					"mode": "urlencoded",

					"urlencoded": [

						{

							"key": "grant_type",

							"value": "client_credentials",

							"type": "default"

						}

					]

				},

				"url": {

					"raw": "{{printtokenurl}}",

					"host": [

						"{{printtokenurl}}"

					]

				}

			},

			"response": []

		},

		{

			"name": "Step2 Get PrintQ",

			"event": [

				{

					"listen": "test",

					"script": {

						"exec": [

							"pm.collectionVariables.set(\"printQ\",pm.response.json()[0].qname)"

						],

						"type": "text/javascript"

					}

				},

				{

					"listen": "prerequest",

					"script": {

						"exec": [

							"pm.request.addHeader(\"Authorization\",pm.collectionVariables.get(\"bearToken\"));"

						],

						"type": "text/javascript"

					}

				}

			],

			"request": {

				"auth": {

					"type": "oauth2",

					"oauth2": [

						{

							"key": "clientId",

							"value": "{{printclientkey}}",

							"type": "string"

						},

						{

							"key": "accessTokenUrl",

							"value": "{{printtokenurl}}",

							"type": "string"

						},

						{

							"key": "grant_type",

							"value": "client_credentials",

							"type": "string"

						},

						{

							"key": "clientSecret",

							"value": "{{printclientsecret}}",
...