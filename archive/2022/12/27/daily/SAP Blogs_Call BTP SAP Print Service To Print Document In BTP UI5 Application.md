---
title: Call BTP SAP Print Service To Print Document In BTP UI5 Application
url: https://blogs.sap.com/2022/12/26/call-btp-sap-print-service-to-print-document-in-btp-ui5-application/
source: SAP Blogs
date: 2022-12-27
fetch_date: 2025-10-04T02:32:59.747240
---

# Call BTP SAP Print Service To Print Document In BTP UI5 Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Call BTP SAP Print Service To Print Document In BT...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160821&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Call BTP SAP Print Service To Print Document In BTP UI5 Application](/t5/technology-blog-posts-by-sap/call-btp-sap-print-service-to-print-document-in-btp-ui5-application/ba-p/13558654)

![Jacky_Liu1](https://avatars.profile.sap.com/0/c/id0c96fbc6ecfa4651eccd3b5e561d0848734220dc92c2198772bae6ac9168e7b7_small.jpeg "Jacky_Liu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jacky\_Liu1](https://community.sap.com/t5/user/viewprofilepage/user-id/132085)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160821)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160821)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558654)

‎2022 Dec 26
9:17 AM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160821/tab/all-users "Click here to see who gave kudos to this post.")

3,945

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)
* [NW ABAP Print and Output Management](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Print%2520and%2520Output%2520Management/pd-p/334558737810127171897316045257708)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [NW ABAP Print and Output Management

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BPrint%2Band%2BOutput%2BManagement/pd-p/334558737810127171897316045257708)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

In my blog [Test BTP SAP Print Service With Postman,](https://blogs.sap.com/2022/12/25/test-btp-sap-print-service-with-postman/) I have explained how to SAP Print Service with postman. In this blog, I will explain how to use it to print document in an UI5 application deployed in BTP cloud foundry run time. To use a PDF document, I will combine the code with my blog [Render and View PDF in SAP UI5 with Forms service by adobe in BTP](https://blogs.sap.com/2022/11/23/render-and-view-pdf-in-sap-ui5-with-forms-service-by-adobe-in-btp/).

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

![](/legacyfs/online/storage/blog_attachments/2022/12/p21-1.jpg)

Use the following commands to open the project with visual code .

![](/legacyfs/online/storage/blog_attachments/2022/12/p22-2.jpg)

### Step 2:  Change the view MainView.view as the following code:

```
<View controllerName="com.sap.printui5.controller.MainView" xmlns:mvc="sap.ui.core.mvc" xmlns:core="sap.ui.core" displayBlock="true" xmlns="sap.m">

	<Page id="page" title="{i18n>title}" showNavButton="true">

		<content>

			<VBox width="100%" direction="Column" id="vbox0" alignContent="Center">

				<items>

					<HBox width="100%" id="hbox1">

						<items>

							<Label id="filenamel" width="200px" class="sapUiSmallMargin" text="FileName:" />

							<Input id="filename" width="200px"  editable="true" />

						</items>

					</HBox>

					<HBox id="hbox4">

						<Select id="select1" showSecondaryValues="true" width="200px" class="sapUiSmallMargin" items="{ path: '/templates' }">

							<core:ListItem id="listitem1" text="{name}" />

						</Select>

						<Button text="PDF Render" id="button2" class="sapUiSmallMargin" type="Emphasized" width="200px" press="pdfRender" />

					</HBox>

				</items>

				<HBox width="100%" id="hbox5">

					<Select id="select" showSecondaryValues="false" class="sapUiSmallMargin" width="200px" items="{ path: '/printQs' }">

						<core:ListItem id="listitem" text="{qname}" additionalText="{qdescription}" />

					</Select>

					<Button text="Send To PrintQ" id="button3" class="sapUiSmallMargin" type="Emphasized" width="200px" press="pdfPrint" />

				</HBox>

				<ScrollContainer id="scrollc1" height="100%" width="100%" horizontal="true" vertical="true">

					<FlexBox id="flexb1" direction="Column" renderType="Div" class="sapUiSmallMargin">

						<PDFViewer id="pdfview" source="{/Source}" title="{/Title}" height="{/Height}">

							<layoutData>

								<FlexItemData id="flexitemdata1" growFactor="1" />

							</layoutData>

						</PDFViewer>

					</FlexBox>

				</ScrollContainer>

			</VBox>

		</content>

	</Page>

</View>
```

### Step 3:  Create folder service under webapp, create file named FileUpload.js under folder service . Change the file FileUpload.js as the following code:

```
// @ts-ignore

sap.ui.define("FileUpload", [

    "sap/ui/base/Object"

], function (ui5Object) {

    "use strict";

    return ui5Object.extend("ui5applicationmodule.service.FileUpload", {

        printDm: function (content, filename) {

            return new Promise((resolve, reject) => {

                // @ts-ignore

                var data = new FormData();

                data.append("media", c...