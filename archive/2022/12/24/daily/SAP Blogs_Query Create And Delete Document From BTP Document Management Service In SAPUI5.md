---
title: Query Create And Delete Document From BTP Document Management Service In SAPUI5
url: https://blogs.sap.com/2022/12/23/query-create-and-delete-document-from-btp-document-management-service-in-sapui5/
source: SAP Blogs
date: 2022-12-24
fetch_date: 2025-10-04T02:25:23.443193
---

# Query Create And Delete Document From BTP Document Management Service In SAPUI5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Query Create And Delete Document From BTP Document...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160603&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Query Create And Delete Document From BTP Document Management Service In SAPUI5](/t5/technology-blog-posts-by-sap/query-create-and-delete-document-from-btp-document-management-service-in/ba-p/13558012)

![Jacky_Liu1](https://avatars.profile.sap.com/0/c/id0c96fbc6ecfa4651eccd3b5e561d0848734220dc92c2198772bae6ac9168e7b7_small.jpeg "Jacky_Liu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jacky\_Liu1](https://community.sap.com/t5/user/viewprofilepage/user-id/132085)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160603)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160603)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558012)

‎2022 Dec 23
12:00 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160603/tab/all-users "Click here to see who gave kudos to this post.")

3,074

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Document Management service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520Management%2520service/pd-p/73555000100800002121)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Document Management service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BDocument%2BManagement%2Bservice/pd-p/73555000100800002121)

View products (3)

In my blog [Download And View PDF document From BTP Document Management Service In SAPUI5](https://blogs.sap.com/2022/12/08/download-and-view-pdf-document-from-btp-document-management-service/).   I have demo how to view PDF document from BTP Document Management Service(BTP CMIS) . But customers need to realize other requirements like query, create and delete documents in BTP CMIS in SAPUI5.  To query documents, we can use [cmis query](https://chemistry.apache.org/docs/cmis-samples/samples/query-examples/index.html).( Text search base on file content is not supported in BTP CMIS currently) . I will demo the steps to realize these 3 requirements, the readers can realize others requirements like query, create, delete folder also base on [CMIS api](https://api.sap.com/package/SAPDocumentManagementServiceIntegrationOptionCMISAPI/rest) in API Hub .

## Prerequisite:

1, You have installed [CF Client](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/4ef907afb1254e8286882a2bdef0edf4.html) .

2, You have installed [Nodejs](https://nodejs.org/en/download/) .

3,  You have installed  [Cloud MTA Build Tool](https://sap.github.io/cloud-mta-build-tool/download/) .

4, You have finished [Initial Setup for Document Management Service, Integration Option](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/bc0f1ec7d5374b968e0b0de6db470c94.html).

5, You have finished [Onboarding Repository](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/b37799034e81433c8312864b0b5a2fab.html).

6, Destination for CMIS service key has been created as step 1 in  [blog](https://blogs.sap.com/2022/11/29/upload-rendered-pdf-document-into-btp-document-manangement-service-in-sapui5-application/) .

7, You have installed [VSCode](https://code.visualstudio.com/download) (optional).

## Steps :

### Step 1:  Generate SAPUI5 project with [easy-ui5](https://blogs.sap.com/2021/04/09/easy-ui5-3.0-from-community-contributions-to-community-plugins/comment-page-1/#comment-650586) .

![](/legacyfs/online/storage/blog_attachments/2022/12/Q01.jpg)

Use the following commands to open the project with visual code .

![](/legacyfs/online/storage/blog_attachments/2022/12/q2.jpg)

### Step 2:  Change the view MainView.view as the following code:

```
<mvc:View controllerName="com.sap.cmissearch4.controller.MainView" xmlns:u="sap.ui.unified" xmlns:mvc="sap.ui.core.mvc" displayBlock="true" xmlns="sap.m">

	<Page id="page" title="{i18n>title}">

		<customHeader>

			<Bar id="bar1">

				<contentLeft>

					<Image id="image1" src="https://unpkg.com/fundamental-styles@0.10.0/dist/images/sap-logo.png" />

					<Label id="label1" text="BTP CMIS Search" />

				</contentLeft>

			</Bar>

		</customHeader>

		<content>

			<Table id="table1" inset="true" items="{/results}" busy="{viewModel>/isBusy}">

				<columns>

					<Column id="headcolumn1">

						<header>

							<Label id="tablelabel" text="FileName">

							</Label>

						</header>

					</Column>

					<Column id="headcolumn7">

						<header>

							<Label id="tablelabe7" text="objectId">

							</Label>

						</header>

					</Column>

					<Column id="headcolumn2">

						<header>

							<Label id="tablelabel2" text="createdBy">

							</Label>

						</header>

					</Column>

					<Column id="headcolumn3">

						<header>

							<Label id="tablelabel3" text="ObjectTypeId">

							</Label>

						</header>

					</Column>

					<Column id="headcolumn4">

						<header>

							<Label id="tablelabel4" text="Actions">

							</Label>

						</header>

					</Column>

				</columns>

				<items>

					<ColumnListItem id="items">

						<cells>

							<Text id="text1" text="{succinctProperties/cmis:name}" />

							<Text id="text4" text="{succinctProperties/cmis:objectId}" />

							<Text id="text2" text="{succinctProperties/cmis:createdBy}" />

							<Text id="text3" text="{succinctProperties/cmis:objectTypeId}" />

							<HBox id="actionhbox">

								<Button id="buttondelte" icon="sap-icon://delete" press="pressDelete" />

							</HBox>

						</cells>

					</ColumnListItem>

				</items>

				<headerToolbar>

					<Toolbar id="toolbar1">

						<content>

							<Title id="toolbartitle" text="Ducuments" width="25%" />

							<ToolbarSpacer id="toolspace">

							</ToolbarSpacer>

							<Label id="filenamelabel" width="5%" text="FileName" />

							<Input id="filename" width="40%" />

							<Button id="button1" icon="sap-icon://search" width="15%" text="Search" press="pressQuery" />

							<Button id="button2" icon="sap-icon://add" width="15%" text="UploadFile" press="pressCreate" />

						</content>

					</Toolbar>

				</headerToolbar>

			</Table>

		</content>

	</Page>

</mvc:View>
```

### Step 3:  Change the controller MainView.controller.js as the following code:

Note:

4c0973e8-a785-4789-a048-067d42f97873 is the created repository id in prerequisite 5 .

```
// @ts-nocheck

sap.ui.de...