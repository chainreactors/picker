---
title: Lazy Loading Columns with Intersection Observer (SAPUI5)
url: https://blogs.sap.com/2022/10/14/lazy-loading-columns-with-intersection-observer-sapui5/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:33.647953
---

# Lazy Loading Columns with Intersection Observer (SAPUI5)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Lazy Loading Columns with Intersection Observer (S...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/157698&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Lazy Loading Columns with Intersection Observer (SAPUI5)](/t5/technology-blog-posts-by-members/lazy-loading-columns-with-intersection-observer-sapui5/ba-p/13535522)

![duncanbarre](https://avatars.profile.sap.com/f/b/idfb7b79b974df30515903a609702f4b865c9f8989a150d7dc644f5aa80d07a343_small.jpeg "duncanbarre")

[duncanbarre](https://community.sap.com/t5/user/viewprofilepage/user-id/39426)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=157698)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/157698)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13535522)

‎2022 Oct 14
7:12 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/157698/tab/all-users "Click here to see who gave kudos to this post.")

2,070

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Web IDE](https://community.sap.com/t5/c-khhcw49343/SAP%2520Web%2520IDE/pd-p/73554900100700001351)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Web IDE

  Software Product](/t5/c-khhcw49343/SAP%2BWeb%2BIDE/pd-p/73554900100700001351)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (4)

Hello World!
This is my first blog! I recently had a requirement where the client wanted 365 columns in a table. The goal was to edit the schedule of multiple employees in one table over the period of a year. Another requirement was to scroll horizontally (just like Excel). Although the Fiori guidelines clearly states ([source](https://experience.sap.com/fiori-design-web/grid-table/)![:disappointed_face:](/html/@C726EA8897DBCB545126E7A86E5A4D50/emoticons/1f61e.png ":disappointed_face:")
> Try to avoid horizontal scrolling in the default delivery
>
> Try to minimize the number of columns

To comply with these requirement I wanted to find a way to fix the performance. The issue lies in loading the app. I needed to find a way to lazy load the columns, so the app doesn't open with 365 columns all at once. I know there is lazy loading for records, but there doesn’t seem to be lazy loading for columns. So this is my workaround. Let’s start this up!

### Part 1: Create Table

*(scroll down to part 2 if you already have a table)*

Create a new project and download [this json file](https://github.com/duncanbarre/zLazyLoad/blob/main/webapp/json/data.json) (for mock data). You can put it in a folder if you like, I put it a new folder named ‘json’.

![](/legacyfs/online/storage/blog_attachments/2022/10/json.png)

Add the json to the manifest as a datasource and as a model:

```
"sap.app": {

	"dataSources": {

		"yearJson": {

			"uri": "json/data.json",

			"type": "JSON"

		}

	},

...

"models": {

		"i18n": {

			"type": "sap.ui.model.resource.ResourceModel",

			"settings": {

				"bundleName": "lazyload.zLazyLoad.i18n.i18n"

			}

		},

		"YearModel": {

			"type": "sap.ui.model.json.JSONModel",

			"dataSource": "yearJson"

		}

	},
```

First create a table in the view. For padding purposes I also added dynamic page:

```
<mvc:View controllerName="lazyload.zLazyLoad.controller.start" xmlns:mvc="sap.ui.core.mvc" displayBlock="true" xmlns="sap.m" xmlns:f="sap.f"

	xmlns:ui="sap.ui.table">

	<App id="app">

		<f:DynamicPage id="mainPage">

			<f:content>

				<ui:Table id="scheduleTableYear" fixedColumnCount="2" selectionMode="None" rows="{YearModel>/employees}"></ui:Table>

			</f:content>

		</f:DynamicPage>

	</App>

</mvc:View>
```

For the purpose of this table it’s practical to add Momentjs (there are multiple ways to add Momentjs, but i’ve added it directly as a file). You can [download the file here](https://github.com/duncanbarre/zLazyLoad/blob/main/webapp/libs/moment.js) and place it in a new folder ‘libs’. Add momentjs and JSONModel at the top and make the controller globally accessible. Also add two functions setScreenModel and createYearTable which we are going to write next:

```
var mainController;

sap.ui.define([

	"sap/ui/core/mvc/Controller",

	"./../libs/moment",

	"sap/ui/model/json/JSONModel",

], function (Controller, momentjs, JSONModel) {

	"use strict";

	return Controller.extend("lazyload.zLazyLoad.controller.start", {

		onInit: function () {

			mainController = this;

		        this.setScreenModel();

         		this.createYearTable();

               }
```

Next, create the columns dynamically, because writing 365 columns in the xml view seems like a lot of work ![:winking_face:](/html/@4EE0D1333C2C259B59B0E8C55B5F4FAD/emoticons/1f609.png ":winking_face:")

```
createYearTable: function () {

			this.oTableYear = this.getView().byId("scheduleTableYear");

			/**********************

			 *  1. add team /name  *

			 **********************/

			this.oTableYear.addColumn(new sap.ui.table.Column({

				label: "Team",

				template: new sap.m.Text({

					text: "{YearModel>TEAM}"

				})

			}));

			this.oTableYear.addColumn(new sap.ui.table.Column({

				label: "Naam",

				template: new sap.m.Text({

					text: "{YearModel>NAME}"

				})

			}));

			/*****************

			 *  2. add days  *

			 ****************/

			const dateCurrentYear = new Date(2022, 0, 1);

			const dateNextYear = new Date(2022 + 1, 0, 1);

			do {

				const month = moment(dateCurrentYear).locale('nl').format('MMMM').toUpperCase();

				const fieldDay = `{YearModel>${month}/DAY${dateCurrentYear.getDate()}}`;

				const newInput = new sap.m.Input({

					value: fieldDay

				}).addStyleClass("select--scheduletype");

				let columnVisible = `month${dateCurrentYear.getMonth() + 1}`;

				this.oTableYear.addColumn(new sap.ui.table.Column({

					visible: "{screenModel>/" + columnVisible + "}",

					width: "110px",

					headerSpan: mainController.getHeaderSpan(dateCurrentYear),

					multiLabels: [

						new sap.m.Label({

							text: moment(dateCurrentYear).locale('nl').format('MMM D')

						}),

						new sap.m.Label({

							text: moment(dateCurrentYear).locale('nl').format('dd')

						}),

						new sap.m.Label({

							text: `week ${moment(dateCurrentYear).locale('nl').isoWeek()}`

						})

					],

					template: newInput

				}));

				dateCurrentYear.setDate(dateCurrentYear.getDate() + 1);

			} while (dateCurrentYear.getFullYear() < dateNextYear.getFullYear());

		},
```

Adding headerspan for the weeks and days:

```
getHeaderSpan: function (oDay) {

			let headerSpan = [0, 0, 7];

			let count = 1;

			const count...