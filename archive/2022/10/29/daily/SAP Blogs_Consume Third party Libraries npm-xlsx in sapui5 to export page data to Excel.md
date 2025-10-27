---
title: Consume Third party Libraries npm-xlsx in sapui5 to export page data to Excel
url: https://blogs.sap.com/2022/10/28/consume-third-party-libraries-npm-xlsx-in-sapui5-to-export-page-data-to-excel/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:21.034898
---

# Consume Third party Libraries npm-xlsx in sapui5 to export page data to Excel

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Consume Third party Libraries npm-xlsx in sapui5 t...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160861&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Consume Third party Libraries npm-xlsx in sapui5 to export page data to Excel](/t5/technology-blog-posts-by-members/consume-third-party-libraries-npm-xlsx-in-sapui5-to-export-page-data-to/ba-p/13555025)

![rajesh_salapu](https://avatars.profile.sap.com/7/b/id7bcb4054ee6c7dcd06df3e347c0129a67d4959e2c0c1ada464dc1d7337b9d570_small.jpeg "rajesh_salapu")

[rajesh\_salapu](https://community.sap.com/t5/user/viewprofilepage/user-id/773332)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160861)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160861)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555025)

‎2022 Oct 28
7:13 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160861/tab/all-users "Click here to see who gave kudos to this post.")

4,613

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

Hi Readers!!

Hope Everyone are doing Good and safe.

In this blog post I am going to demonstrate how you can Export exact page data to Excel using npm-xlsx libraries with adding excel Styles.

Why npm-xlsx : This is the third party library generally used for Exporting and data to XLSX file with adding Styles , formatting etc..

**Steps includes**:

1. Create a Form and Table in View

2. Declaring third party library in controller

3. Export button Functionality.

4. Output

### **1.****Create a Form and Table in View:**

Created Simple form for displaying Employee details and Created a Table for Displaying Employee last 6 years Address.

```
<mvc:View controllerName="comThird_party_application.controller.View1" xmlns:mvc="sap.ui.core.mvc" displayBlock="true" xmlns="sap.m"

	xmlns:l="sap.ui.layout" xmlns:f="sap.ui.layout.form" xmlns:core="sap.ui.core">

	<App>

		<pages>

			<Page title="{i18n>title}">

				<content>

					<VBox class="sapUiSmallMargin">

						<f:SimpleForm id="Form2" editable="false" layout="ResponsiveGridLayout" title="Employee Details" labelSpanXL="4" labelSpanL="6"

							labelSpanM="6" labelSpanS="12" adjustLabelSpan="false" emptySpanXL="0" emptySpanL="4" emptySpanM="0" emptySpanS="0" columnsXL="2"

							columnsL="2" columnsM="2" singleContainerFullSize="false">

							<f:content>

								<Label text="Name "/>

								<Text text="Rajesh"/>

								<Label text="Id "/>

								<Text text="123456"/>

								<Label text="Company "/>

								<Text text="Mouritech "/>

								<Label text="Phone Number "/>

								<Text text="123456"/>

							</f:content>

						</f:SimpleForm>

					</VBox>

					<Table width="auto" id="imTable" items="{path: 'Model>/results'}" class="sapUiResponsivePadding tableCls" growingScrollToLoad="true"

						alternateRowColors="true" growing="true" growingThreshold="20">

						<headerToolbar>

							<Toolbar>

								<content>

									<ToolbarSpacer/>

									<Label text="Employee Address Data of last 6 years " design="Bold"/>

									<ToolbarSpacer/>

								</content>

							</Toolbar>

						</headerToolbar>

						<columns>

							<Column id="col1"  width="5rem">

								<Label text="House Number" wrapping="true" design="Bold"></Label>

							</Column>

							<Column id="col2"  width="6rem">

								<Label text="Village/City" wrapping="true" design="Bold"></Label>

							</Column>

							<Column id="col3" minScreenWidth="Desktop" demandPopin="true"  width="6rem">

								<Label text="Phone Number" wrapping="true" design="Bold"></Label>

							</Column>

							<Column id="col4" minScreenWidth="Desktop" demandPopin="true"  width="6rem">

								<Label text="Pincode" wrapping="true" design="Bold"></Label>

							</Column>

						</columns>

						<items>

							<ColumnListItem>

								<cells>

									<Text text="{Model>H_no}"/>

									<Text text="{Model>city}"/>

									<Text text="{Model>Phone_number}"/>

									<Text text="{Model>Pincode}"/>

								</cells>

							</ColumnListItem>

						</items>

					</Table>

				</content>

				<footer>

					<Bar>

						<contentRight>

							<Button tooltip="Excel To Excel" text="Excel To Excel" icon="sap-icon://print" press="onPrint" type="Accept"/>

						</contentRight>

					</Bar>

				</footer>

			</Page>

		</pages>

	</App>

</mvc:View>
```

**Page Output :**

**![](/legacyfs/online/storage/blog_attachments/2022/10/page-Output.png)**

Output of view

### **2.Declaring third party library in controller**:

As per page output we have to Export page data with same design and adding colors to output sheet by using npm-xlsx libraries.

Create libs folder in webapp and Create a .js file I the name of “styleXLSX” and paste the code from given link:

[“https://github.com/gitbrent/xlsx-js-style/blob/master/dist/xlsx.bundle.js”](https://github.com/gitbrent/xlsx-js-style/blob/master/dist/xlsx.bundle.js)

First load the npm-xlsx library data in libs folder and declare that library in controller.

“$**.sap.require("com/Dynamic\_CustomExport/libs/styleXLSX")**;”

### **3.Export button Functionality:**

First, we have to create a Html table as per our Output data. Then convert to Dom element by using DOM Parser. Then convert this Dom element to Work sheet using “XLSX.utils.table\_to\_sheet” method in npm-xlsx.

```
// Simple form Data

var Form2contents = that.getView().byId("Form2").getContent();

//Table Data

			var data = that.getView().getModel("Model").getData().results;

//creating a html table

			var html = "";

			html += "<tr>" +

				"<th colspan = 4>" + "Employee Details" + "</th>" + "</tr>" +

				"<tr>" + "<td colspan = 3>" + Form2contents[0].getText() + "</td>" +

				"<td colspan = 1>" + Form2contents[1].getText() + "</td>" + "</tr>" +

				"<tr>" + "<td colspan = 3>" + Form2contents[2].getText() + "</td>" +

				"<td colspan = 1>" + Form2contents[3].getText() + "</td>" + "</tr>" +

				"<tr>" + "<td colspan = 3>" + Form2contents[4].getText() + "</td>" +

				"<td colspan = 1>" + Form2contents[5].getText() + "</td>" + "</tr>" +

				"<tr>" + "<td colspan = 3>" + Form2contents[6].getText() + "</td>" +

				"<td colspan = 1>" + Form2contents[7].getText() + "</td>" + "</tr>" +

				"<tr>" + "</tr>" + "<tr>" + "</tr>";

			html += "<tr>" + "<th colspan = 4>" + "Employee Address Data of last 6 years " + "</th>" + "</tr>";

			html += "<tr>" +

				"<td>" + "House Number" + "</td>" +

				"<td>" + "Village/City" + "</td>" +

				"<td>" + "Phone Number" + "</td>" +

				"<td>" + "Pincode" + "</td>" + "</tr>";

//adding table data dynamically

			for (var k = 0; k < data.length; k++) {

				html += "<tr>" +

					"<td>" + (data[k].H_no) + "</td>" +

					"<td>" + data[k].city + "</td>" +

					"<td>" + data[k].Phone_number + "</t...