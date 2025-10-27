---
title: UI5con 2023 – UI5 Web Component
url: https://blogs.sap.com/2023/07/07/ui5con-2023-ui5-web-component/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:27.498349
---

# UI5con 2023 – UI5 Web Component

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* UI5con 2023 – UI5 Web Component

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160898&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5con 2023 – UI5 Web Component](/t5/technology-blog-posts-by-members/ui5con-2023-ui5-web-component/ba-p/13555277)

![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[WouterLemaire](https://community.sap.com/t5/user/viewprofilepage/user-id/9863)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160898)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160898)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555277)

‎2023 Jul 07
10:08 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160898/tab/all-users "Click here to see who gave kudos to this post.")

1,021

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

# Introduction

In this blog post series, I’ll show how to create a Web Component and consume it in UI5! This is based on my UI5con session of 2023 together with peter.muessig .

- Vanilla Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-vanilla-web-component/>
- UI5 Web Component (this one): <https://blogs.sap.com/2023/07/07/ui5con-2023-ui5-web-component/>
- Generate UI5 Library & Controls for UI5 Web Components: <https://blogs.sap.com/2023/07/07/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/>
- Consume UI5 Controls based on UI5 Web Components inside a UI5 app: [https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside...](https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5-app/)

In the previous blog post, I created a Vanilla Web Component. In this blog post, I will transform the Vanilla Web Component into a UI5 Web Component. This is needed to bring the Web Component into the UI5 framework.

![](/legacyfs/online/storage/blog_attachments/2023/07/image1-2.png)

# Create package

For creating a UI5 Web Component, we start by creating a UI5 Web Component package:

* Generate a UI5 WebComponent Package

```
npm init @ui5/webcomponents-package@latest
```

* Provide the name for the package, eg.: spacepackage

* Select the preferred language, TypeScript

* Provide the name for the first UI5 WebComponent, eg.: SpaceComponent

* JSDoc namespace: leave it as it is, this is a placeholder for the namespace of the UI5 library in a later phase.

![](/legacyfs/online/storage/blog_attachments/2023/07/image2-2.png)

This will generate a project pre-configured to start developing UI5 Web Components, including a first Web Component. In my case it generated all the files for the SpaceComponent:

![](/legacyfs/online/storage/blog_attachments/2023/07/image3-4.png)

# SpaceComponent

The generator already came with sample code for the SpaceComponent. Now, I will complete this with the code I already had from my Vanilla Web Component.

* Provide the template in the SpaceComponent.hbs file: The template is almost exactly the same as for the Vanilla Web Component except it now allows to use handlebar placeholders for the attributes. This time, I provide a placeholder for intro and logo

```
<div class="star-wars-intro">

    <p class="intro-text">{{intro}}</p>

    <h2 class="main-logo">

        <img src="{{logo}}"/>

    </h2>

    <div class="main-content">

        <div class="title-content">

            <slot></slot>

        </div>

    </div>

</div>
```

Full template code: <https://github.com/lemaiwo/ui5-space-webcomponent-package/blob/main/src/SpaceComponent.hbs>

* In the SpaceComponent.ts file, include the dependency for slots which needed to use the @slot annotation

```
import slot from "@ui5/webcomponents-base/dist/decorators/slot.js";
```

* Define the properties in the SpaceComponent class: the properties have the same names that are being used in the template.

  + Small remark, the JSDoc is very important for later to create the UI5 control out of the UI5 Web Component

```
	/**

	* Defines the intro of the space component.

	*

	* @type {string}

	* @name demo.components.SpaceComponent.prototype.intro

	* @defaultvalue ""

	* @public

	*/

	@property()

	intro!: string;

	/**

	* Defines the logo of the space component.

	*

	* @type {string}

	* @name demo.components.SpaceComponent.prototype.logo

	* @defaultvalue ""

	* @public

	*/

	@property()

	logo!: string;
```

* Next to the properties, define the slot: the slot is defined as the default slot as this is the only one and I would like to use this in UI5 for the default aggregation

```
	/**

	 * Defines the articles of the component.

	 *

	 * @type {demo.components.SpaceItemComponent[]}

	 * @name demo.components.SpaceComponent.prototype.default

	 * @slot items

	 * @public

	 */

	@slot({ type: HTMLElement, "default": true })

	items!: Array<SpaceItemComponent>;
```

* Implement the logic for generating the stars using onAfterRendering function: this is a lifecycle function of UI5 Web Components and can be compared to onAfterRendering in UI5 views and controls.

```
onAfterRendering() {

	const numStars = 100;

	const mainDiv = this.shadowRoot!.querySelector(".star-wars-intro") as HTMLElement;

	// For every star we want to display

	for (let i = 0; i < numStars; i++) {

		const { top, left } = this.getRandomPosition(mainDiv);

		mainDiv.append(this.getRandomStar(top, left));

	}

}

getRandomStar(top: string, left: string) {

	const star = document.createElement("div");

	star.className = "star";

	star.style.top = top;

	star.style.left = left;

	return star;

}

getRandomPosition(element: HTMLElement) {

	return {

		top: `${this.getRandomNumber(element.offsetHeight)}px`,

		left: `${this.getRandomNumber(element.offsetWidth)}px`,

	};

}

getRandomNumber(value: number) {

	return Math.floor(Math.random() * value);

}
```

Full code for the SpaceComponent class: <https://github.com/lemaiwo/ui5-space-webcomponent-package/blob/main/src/SpaceComponent.ts>

Finally add the css style to the SpaceComponent.ts from here: <https://github.com/lemaiwo/ui5-space-webcomponent-package/blob/main/src/themes/SpaceComponent.css>

# SpaceItemComponent

Once the SpaceComponent is created we can start creating the second one which will behave as a child: “SpaceItemComponent”. This can be done by the following steps:

* Create a new component for the items: SpaceItemComponent

```
npm run create-ui5-element
```

![](/legacyfs/online/storage/blog_attachments/2023/07/image4-3.png)

* Include it in the bundle.esm.js

```
import "./dist/SpaceItemComponent.js";
```

* Provide the template in SpaceItemComponent.hbs

```...