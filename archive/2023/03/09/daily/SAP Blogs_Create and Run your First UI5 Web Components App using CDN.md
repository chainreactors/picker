---
title: Create and Run your First UI5 Web Components App using CDN
url: https://blogs.sap.com/2023/03/08/create-and-run-your-first-ui5-web-components-app-using-cdn/
source: SAP Blogs
date: 2023-03-09
fetch_date: 2025-10-04T09:01:32.385712
---

# Create and Run your First UI5 Web Components App using CDN

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Create and Run your First UI5 Web Components App u...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163589&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create and Run your First UI5 Web Components App using Bundle.esm.js](/t5/technology-blog-posts-by-sap/create-and-run-your-first-ui5-web-components-app-using-bundle-esm-js/ba-p/13567365)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163589)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163589)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567365)

‎2023 Mar 08
6:03 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163589/tab/all-users "Click here to see who gave kudos to this post.")

1,333

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

Dear All,

This blog aims to explain how you can build **UI5 webcomponents application** using bundle.esm.js for your developers to create something new.. This is lightweight and easy to develop according to your need by using Web components provided in documentation.

**SAP UI5 Webcomponents Documentation** : <https://sap.github.io/ui5-webcomponents/>

**Todos API from**  <https://jsonplaceholder.typicode.com/>

---

![UI5 Web Components – Fiorisiert SAP nun das WWW?! » vogel304.de](https://pbs.twimg.com/media/DzIse6JXQAARcwc?format=jpg&name=small)

## Create App using Todos API data in UI5 Webcomponents

The simplest example is the very obvious getting data from Todos API to UI5 application. To run this application we will be using the Bundle.esm.js. First, let us create an `index.html` file with basic HTML structure. For simplicity, we will be writing the js code in the same file.

```
<html>

	<head>

		<meta http-equiv="X-UA-Compatible" content="IE=edge">

		<meta charset="utf-8">

		<title>Todos API Built in UI5</title>

		<script src="https://sap.github.io/ui5-webcomponents/assets/js/ui5-webcomponents/bundle.esm.js" type="module"></script>

		<script src="https://unpkg.com/@luigi-project/container" type="module"></script>

		<script data-ui5-config type="application/json">{"theme": "sap_horizon"}</script>

		<style>

			html, body {

				margin: 0;

			}

			luigi-container {

				position: absolute;

				width: 100%;

				left: 0;

				top: var(--_ui5_shellbar_root_height);

				bottom: 0;

			}

		</style>

	</head>

	<body>

		<ui5-shellbar primary-title="{JSON} Placeholder">

			<ui5-avatar slot="profile" icon="customer"></ui5-avatar>

			<img slot="logo" src="https://sap.github.io/ui5-webcomponents/assets/images/sap-logo-svg.svg"/>

		</ui5-shellbar>

        <!--- Bug to reported

        <ui5-message-strip style="line-height: 1.4rem" design="Information">Information MessageStrip</ui5-message-strip>

        --->

<!--

        <style>

            .backgro {

                background: rgba(224,224,224,0.5)

            }

        </style>

        <div class="backgro">

            <div class="fd-col fd-col--12 main-title">

                <ui5-title slot="title" level="H3">       Result table</ui5-title>

            </div>

        </div>        -->

        <!---<h3>{{ utc_dt }}</h3>---->

        <br> <br>

        <ui5-label class="samples-big-margin-right" for="myInput" required show-colon>User Name</ui5-label>

        <ui5-input id="myInput" placeholder="Enter your Name" required></ui5-input>

        <ui5-label class="samples-big-margin-right" for="myPassword" required show-colon>Password</ui5-label>

        <ui5-input id="myPassword" type="Password" value-state="None" placeholder="Enter your Secret Code" required></ui5-input>

        <ui5-button id="ui5Button" design="Emphasized">Submit</ui5-button>

        <!--- Bug to reported

        <ui5-message-strip design="Positive" style="width: 200px;" hide-close-button>Successfull login!</ui5-message-strip>

        -->

        <br> <br>

    <div>

        <ui5-title slot="title" level="H3">     Todos API</ui5-title>

    </div>

    <div>

        <ui5-table class="demo-table" id="productsTable" no-data-text="No Data" show-no-data>

            <!-- Columns -->

            <ui5-table-column slot="columns">

                <span style="line-height: 1.4rem">userId</span>

            </ui5-table-column>

            <ui5-table-column slot="columns" min-width="800">

                <span style="line-height: 1.4rem">id</span>

            </ui5-table-column>

            <ui5-table-column slot="columns" min-width="600" popin-text="Dimensions" demand-popin class="table-header-text-alignment">

                <span style="line-height: 1.4rem">title</span>

            </ui5-table-column>

            <ui5-table-column slot="columns" min-width="600" popin-text="Weight" demand-popin class="table-header-text-alignment">

                <span style="line-height: 1.4rem">completed</span>

            </ui5-table-column>

    </div>

        <template id="productrow">

            <ui5-table-row>

                <ui5-table-cell data-attribute="userId"></ui5-table-cell>

                <ui5-table-cell data-attribute="id"></ui5-table-cell>

                <ui5-table-cell data-attribute="title"></ui5-table-cell>

                <ui5-table-cell data-attribute="completed"></ui5-table-cell>

            </ui5-table-row>

        </template>

        <script type="text/javascript" charset="utf-8">

            const ui5Button = document.querySelector('ui5-button')

            ui5Button.addEventListener('click', addData)

            async function addData() {

                const response = await fetch('https://jsonplaceholder.typicode.com/todos')

                const products = await response.json()

                const table = document.querySelector('ui5-table')

                products.forEach(product => {

                    const tableRow = document.createElement('ui5-table-row')

                    for (const [key, value] of Object.entries(product)) {

                        const tableCell = document.createElement('ui5-table-cell')

                        tableCell.innerHTML = value

                        tableRow.append(tableCell)

                    }

                    table.appendChild(tableRow)

                });

            }

        </script>

	</body>

</html>
```

Open the file in a web browser and you s...