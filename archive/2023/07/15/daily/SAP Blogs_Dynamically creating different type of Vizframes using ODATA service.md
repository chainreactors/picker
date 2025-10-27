---
title: Dynamically creating different type of Vizframes using ODATA service
url: https://blogs.sap.com/2023/07/14/dynamically-creating-different-type-of-vizframes-using-odata-service/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:52:57.131332
---

# Dynamically creating different type of Vizframes using ODATA service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Dynamically creating different type of Vizframes u...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161652&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Dynamically creating different type of Vizframes using ODATA service](/t5/technology-blog-posts-by-members/dynamically-creating-different-type-of-vizframes-using-odata-service/ba-p/13559266)

![shravanr_in37](https://avatars.profile.sap.com/1/a/id1a9fdd706412f1384fa91df5c79ad70c3f923f822ca821727faa3efea0d21105_small.jpeg "shravanr_in37")

[shravanr\_in37](https://community.sap.com/t5/user/viewprofilepage/user-id/175490)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161652)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161652)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559266)

‎2023 Jul 14
7:02 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161652/tab/all-users "Click here to see who gave kudos to this post.")

1,372

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (3)

In this blog, I am going to explain How create a different type of Vizframes dynamically using ODATA Service.

**Problem:**

In order to create different types of Vizframes dynamically using ODATA Service to display the data in graphical representation.

**Steps Include:**

Right click on the workspace and hover on New and select Project from Template.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-1-2.png)

Select template type as SAPUI5 Application and click on Next.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-2-1.png)

Give the Project name and namespace of the project and click on the Next.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-3-1.png)

If you want to change the View Name or View Type, you can change in below screen. I choose for this project is View type is “XML” and View Name is View1 which will be show by default and click on finish.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-4.png)

Project will be created in the workspace as below.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-5.png)

To integrate the ODATA service to the project right click on project-> New -> oData Service as below.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-6-1.png)

In the sources, select Service Catalog and click on the drop down of the available destinations and choose the right destination as below.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-7.png)

Select the services which you are going to use as below and click on Next.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-8.png)

Click on Finish as below.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-9.png)

Please follow the view code from below, here I used Input to type the URL of ODATA service, ComboBox  is to select the vizType and Submit button is to handle the URL when click on it.

```
<mvc:View controllerName="com.dynamicChartsdynamicCharts.controller.View1" xmlns:html="http://www.w3.org/1999/xhtml"

	xmlns:mvc="sap.ui.core.mvc" displayBlock="true" xmlns="sap.m" xmlns:core="sap.ui.core" xmlns:l="sap.ui.layout"

	xmlns:chart="sap.suite.ui.commons" xmlns:f="sap.ui.layout.form" xmlns:viz.data="sap.viz.ui5.data"

	xmlns:viz.feeds="sap.viz.ui5.controls.common.feeds" xmlns:viz="sap.viz.ui5.controls" class="sapUiSizeCompact">

	<App>

		<pages>

			<Page title="{i18n>title}">

				<content>

					<Input width="25%" value="{valueModel>/input}" placeholder="{i18n>inputText}" />

					<ComboBox items="{path: 'comboModel>/items'}" selectedKey="{valueModel>/comboBox}"

						value="{valueModel>/comboBox}" placeholder="{i18n>comboText}">

						<items>

							<core:Item key="{comboModel>viztype}" text="{comboModel>viztype}"/>

						</items>

					</ComboBox>

					<Button type="Emphasized" text="Submit" press="onSubmitInput" class="sapUiSmallMarginBegin"/>

					<VBox>

						<chart:ChartContainer visible="{valueModel>/visibleChart}">

							<chart:ChartContainerContent>

								<chart:content>

									<viz:VizFrame id="idVizFrame1" uiConfig="{applicationSet:'fiori'}" vizProperties="{employeeData>/properties}"

										vizType="{employeeData>/vizType}" height="300px">

										<viz:dataset>

											<viz.data:FlattenedDataset data="{path: 'employeeData>/'}">

												<viz.data:dimensions>

													<viz.data:DimensionDefinition name="performance" value="{employeeData>/Name}"/>

												</viz.data:dimensions>

												<viz.data:measures>

													<viz.data:MeasureDefinition name="op2022" value="{employeeData>/Op2022}"/>

													<viz.data:MeasureDefinition name="op2021" value="{employeeData>/Op2021}"/>

													<viz.data:MeasureDefinition name="op2023" value="{employeeData>/Op2023}"/>

												</viz.data:measures>

											</viz.data:FlattenedDataset>

										</viz:dataset>

										<viz:feeds>

											<viz.feeds:FeedItem type="Measure" uid="{employeeData>/measureUid}" values="op2022,op2021,op2023"/>

											<viz.feeds:FeedItem type="Dimension" uid="{employeeData>/dimensionUid}" values="performance"/>

										</viz:feeds>

									</viz:VizFrame>

								</chart:content>

							</chart:ChartContainerContent>

						</chart:ChartContainer>

					</VBox>

				</content>

			</Page>

		</pages>

	</App>

</mvc:View>
```

This is the model which I am going to bind to the comboBox from below json file from model folder.

![](/legacyfs/online/storage/blog_attachments/2023/07/picture-10.png)

Below code is the controller code for the above view.

```
sap.ui.define([

	"sap/ui/core/mvc/Controller",

	"sap/ui/model/json/JSONModel",

	"sap/m/MessageBox"

], function(Controller, JSONModel, MessageBox) {

	"use strict";

	return Controller.extend("com.dynamicChartsdynamicCharts.controller.View1", {

		onInit: function() {

			var that = this;

			var oModel = new JSONModel(jQuery.sap.getModulePath("com.dynamicChartsdynamicCharts", "/model/comboModel.json"));

			that.getView().setModel(oModel, "comboModel");

			var value = new JSONModel({

				input: "",

				comboBox: "",

				visibleChart: false

			});

			that.getView().setModel(value, "valueModel");

		},

		onSubmitInput: function() {

			var that = this;

			var url = that.getView().getModel("valueModel").getData().input;

			that.handlingInput(url);

		},

/*Below code is to handle the input and to mak...