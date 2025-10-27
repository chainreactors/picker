---
title: SAP Analytics Cloud Application Designer – Alternative to avoid onInitialization
url: https://blogs.sap.com/2023/04/02/sap-analytics-cloud-application-designer-alternative-to-avoid-oninitialization/
source: SAP Blogs
date: 2023-04-03
fetch_date: 2025-10-04T11:30:08.332439
---

# SAP Analytics Cloud Application Designer – Alternative to avoid onInitialization

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Analytics Cloud Application Designer - Alterna...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163018&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Analytics Cloud Application Designer - Alternative to avoid onInitialization](/t5/technology-blog-posts-by-members/sap-analytics-cloud-application-designer-alternative-to-avoid/ba-p/13567165)

![jorge_sousa1](https://avatars.profile.sap.com/f/6/idf64995367ec63ceb73093d31a3335bef7c65b5c463f45f5de0e81439b9cae925_small.jpeg "jorge_sousa1")

[jorge\_sousa1](https://community.sap.com/t5/user/viewprofilepage/user-id/194305)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163018)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163018)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567165)

‎2023 Apr 02
10:16 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163018/tab/all-users "Click here to see who gave kudos to this post.")

2,441

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)

View products (3)

This short document explain one possible alternative to avoid the utilization of code in the "***onInitialization***", mainly when we need to improve performance in our ***SAC AD*** (when it's possible).

When we introduce code in the "***onInitialization***" we are stacked with the performance of execution sequencial instructions one by one. In some cases just to introduce code "***onInitialization***" we increase the duration in more 5 seconds.

In the below points I want to explain how we can use an alternative option to initialize our application without of the use of "***onInitialization***" in the canvas.

# **Alternative to "onInitialization"**

To achieve this we need to use two techniques:

1. Create a **Custom Widget** (CW).

2. Use of ***onPostMessageReceive***.

"***onPostMessageReceive***" is an event called when the application receives a message from another component like a hosting page or a custom widget. It's important to check the origin of this post messages.

![](/legacyfs/online/storage/blog_attachments/2023/04/SAC_CW_Canvas_PostMessage.png)

In this alternative the idea is to create a simple CW with a simple property (Builder Panel) that allows to specify the ***"message"*** / "method" to send as a **postMessage**. The code can be inserted in ***"onCustomWidgetAfterUpdate(changedProperties)"***.

As son as the CW is loaded during the runtime of the application the "***postMessage"*** is sent to the application and the event ***"onPostMessageReceived"*** is triggered. Here is where we can call the list of functions or instructions to execute.

# Use of Simple Custom Widget (CW)

This simple CW must have at least:

1. The ***JSON*** file definition.

2. The ***Javascript*** for the main/core CW definition.

3. The ***Javascript*** for the builder panel properties definition.

You can find more details how to create a CW in some blogs or also in the SAP Help:

[https://help.sap.com/docs/SAP\_ANALYTICS\_CLOUD/0ac8c6754ff84605a4372468d002f2bf/2524b21ac5ec45649a64f...](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/0ac8c6754ff84605a4372468d002f2bf/2524b21ac5ec45649a64f9dd1c934718.html)

The ***JSON*** file could be for example as the below one:

```
{

    "name": "SAC OnInitialization",

	"description": "SAC OnInitialization Avoid CW",

	"eula": "EULA",

	"vendor": "jmlds",

	"license": "1.0",

	"id": "com.sap.jmlds.oninitialization.widget",

	"newInstancePrefix": "SACOnInitializationAvoidCW",

	"version": "1.0.0",

	"icon": "",

	"webcomponents": [

		{

			"kind": "main",

			"tag": "com-sap-jmlds-oninitialization-main",

			"url": "https://myserver.com/tools/performance/sacperf_main.js?ver=1.0.2",

			"integrity": ""	,

			"ignoreIntegrity": true

		},

		{

			"kind": "builder",

			"tag": "com-sap-jmlds-oninitialization-bp",

			"url": "https://myserver.com/tools/performance/sacperf_bp.js?ver=1.0.1",

			"integrity": "",

			"ignoreIntegrity": true

		}

	],

	"properties": {

		"width": {

			"type": "integer",

			"default": 50

		},

		"height": {

			"type": "integer",

			"default": 20

		},

		"method": {

			"type": "string",

			"description": "Method",

			"default": "onInitialization"

		}

	},

	"methods": {

		"clear": {

			"description": "Clear the resultset"

		}

	},

	"events": {

		"onClick": {

			"description": "Only for Visible Process Click"

		}

	}

}
```

The builder panel ***JavaScript*** file must contains the property for the ***"m****ethod" / "message"*** configuration:

```
(function()  {

	let base = document.createElement("template");

	base.innerHTML = `

		<form id="frmSacPerf">

			<fieldset>

				<legend>Method Call</legend>

				<table>

					<tr>

						<td>Name of the Method</td>

						<td><input id="id_method" type="text" size="20" maxlength="25"></td>

					</tr>

				</table>

				<input type="submit" style="display:none;">

			</fieldset>

		</form>

		<style>

		:box {

			display: block;

			padding: 1px 1px 1px 1px;

		}

		</style>

	`;

	class PanelSacPerf extends HTMLElement {

		constructor() {

			super();

			this._shadowRoot = this.attachShadow({mode: "open"});

			this._shadowRoot.appendChild(base.content.cloneNode(true));

			this._shadowRoot.getElementById("frmSacPerf").addEventListener("submit", this._submit.bind(this));

		}

		_submit(e) {

			e.preventDefault();

			this.dispatchEvent(new CustomEvent("propertiesChanged", {

					detail: {

						properties: {

							method: this.method

						}

					}

			}));

		}

		set method(setMethod) {

			this._shadowRoot.getElementById("id_method").value = setMethod;

		}

		get method() {

			return this._shadowRoot.getElementById("id_method").value;

		}

	}

	customElements.define("com-sap-jmlds-oninitialization-bp", PanelSacPerf);

})();
```

The main ***JavaScript*** that must send the message to the canvas receiver must have at least, the definition of the template, the constructor, the declaration of the custom element and the function / event "***onCustomWidgetAfterUpdate(changedProperties)":***

```
(function () {

    let template = document.createElement('template');

    template.innerHTML =

    `<button type="button...