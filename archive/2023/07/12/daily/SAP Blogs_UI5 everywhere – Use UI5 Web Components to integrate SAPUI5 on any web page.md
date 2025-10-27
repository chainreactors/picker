---
title: UI5 everywhere – Use UI5 Web Components to integrate SAPUI5 on any web page
url: https://blogs.sap.com/2023/07/11/ui5-everywhere-use-ui5-web-components-to-integrate-sapui5-on-any-web-page/
source: SAP Blogs
date: 2023-07-12
fetch_date: 2025-10-04T11:54:39.488270
---

# UI5 everywhere – Use UI5 Web Components to integrate SAPUI5 on any web page

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* UI5 everywhere - Use UI5 Web Components to integra...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160965&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5 everywhere - Use UI5 Web Components to integrate SAPUI5 on any web page](/t5/technology-blog-posts-by-members/ui5-everywhere-use-ui5-web-components-to-integrate-sapui5-on-any-web-page/ba-p/13555468)

![DanielKawkab](https://avatars.profile.sap.com/5/d/id5d833edb9a030dd2d6792593d436398b423809e61aca3189578f7ec05a953d77_small.jpeg "DanielKawkab")

[DanielKawkab](https://community.sap.com/t5/user/viewprofilepage/user-id/10461)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160965)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160965)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555468)

‎2023 Jul 11
9:42 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160965/tab/all-users "Click here to see who gave kudos to this post.")

3,807

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

## Motivation

I really like SAPUI5 for its large control library, strong OData integration and the possibility to load other SAPUI5 apps from anywhere at any time, which creates a great time-to-value. These apps are typically running in a SAP managed environment, like a FLP, be it cloud or on-premise or the Portal service.

But what if we would be able to run SAPUI5 anywhere, even at some places like a customers website, where style guidelines play a huge role. And what if the integration of the SAPUI5 app would be nothing but **two lines of HTML**?

An **approach** to create this scenario is exactly what will be created throughout this blog post.

**Maybe one more thing about the integration of SAPUI5 applications in style-dependent environments:**UI5 comes with an out-of-the-box set of themes you can use right away. Even though i like themes like Horizon and Fiori very much, I don't think these will resemble most customers style guidelines. And this is okay, since the said SAP-managed environments are mostly for internal use (not a 100% true for the Portal Service). If you would like to place your app in a non-internal environment, you would need to take care of the styling yourself, like with for example creating a custom theme.

## The fundamental idea

A [UI5 Web Component](https://sap.github.io/ui5-webcomponents/) can be considered as a kind of SAPUI5 control, just without being connected to the whole SAPUI5 ecosystem and lifecycle. Web Components are lightweight, modular and come with lots of features as i18n-support, theming and a wide range of existing components, that you can use right away. They are based on web standards and use the browser's Custom Elements API to create custom HTML tags that reflect a web component.

As mentioned, web components are usually something like a buttons, card, or an input field. They are lightweight components that you can embed on any website in the form of an HTML tag.

**Example:**To embed a button, you just need to add the HTML tag "<ui5-button>" to the HTML code of your web page.

The idea behind this approach is to display not just a single "control" by adding the HTML tag to your page, but to display an entire SAPUI5 application by doing so. For this, a custom UI5 Web Component must be created, which internally will load the SAPUI5 app and display it on the page.

So we will not use one of the existing Web Components that are already provided, but create a fresh one we can fill with logic ourselves.

### Note

Since I only want to present the said scenario, I will limit myself technically to the most necessary. Therefore I will not use Typescript and PNPM in this blog post.

## What you need:

* [node.js](https://nodejs.org/en/download) (>= 16.18)

* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

* [yeoman](https://github.com/SAP/generator-easy-ui5)

* [UI5 cli](https://sap.github.io/ui5-tooling/v3/pages/CLI/)

## 1. Create a SAPUI5 application

To embed an UI5 app, we first of all need an UI5 app. Fortunately we can use the Yeoman [easy-ui5-generator](https://github.com/SAP/generator-easy-ui5) to speed things up:

* Install easy-ui5-generator via your terminal => npm install -g yo generator-easy-ui5

* Navigate to the folder your project will be contained in

* yo easy-ui5 app

**Select the following options:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Bildschirm­foto-2023-07-09-um-20.37.00.png)

After this you will have a pretty empty, but working UI5 application.

## 2. Create a UI5 Web Component

In our scenario we do not want to use the already existing Web Components, but we want to create a custom one. For this we have to initialize a UI5 Web Components project:

* Via your terminal navigate to your target folder

* Run "npm init @ui5/webcomponents-package@1.15.1"

**Select the following options:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Bildschirm­foto-2023-07-08-um-13.00.57.png)

You can now follow the command displayed in your terminal to start up your custom Web Component and check what i looks like.

## 3. Prepare your SAPUI5 app for consumption

Since this blog is all about showing the integration of our SAPUI5 app in our UI5 web component, we do not need to change or adjust our SAPUI5 app. **One thing we need to do, though, is take care of CORS,** since the UI5 Tooling server won't enable us to respond with custom headers.

For this we create an approuter, which will simply server our static files. In your SAPUI5 applications root folder create a folder approuter and add the following files to it:

### package.json

```
{

    "name": "ui5wc-with-ui5-ui5-ar",

    "version": "0.0.1",

    "scripts": {

      "start": "node index.js"

    },

    "dependencies": {

      "@sap/approuter": "^14.0.0"

    }

  }
```

Here we add "@sap/approuter" as a dependency, since we want to use the routing capabilities of the approuter later on. The "start"-script will not just start the approuter from the installed package folder, but start the index.js-file, which we will create now.

### index.js

```
const approuter = require("@sap/approuter");

const ar = approuter();

process.env.PORT = process.env.PORT || 3000;

ar.beforeRequestHandler.use(function myMiddleware(req, res, next) {

  res.setHeader("access-control-allow-origin", "*");

  next();

});

ar.start();
```

This file will be started by our "start"-script. Since this is supposed to be an approuter we must require the approuter package and start it manually. The important thing here is, that we insert a custom middleware, in which we can set custom headers. For our scenario we set the "access-control-allow-origin"-header to handle CORS.

### xs-app.json

```
{

    "authenticationMethod": "none",

    "rout...