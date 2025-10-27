---
title: UI5con 2023 – Generate UI5 Library & Controls for UI5 Web Components
url: https://blogs.sap.com/2023/07/07/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:36.258600
---

# UI5con 2023 – Generate UI5 Library & Controls for UI5 Web Components

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* UI5con 2023 – Generate UI5 Library & Controls for ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160885&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5con 2023 – Generate UI5 Library & Controls for UI5 Web Components](/t5/technology-blog-posts-by-members/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/ba-p/13555261)

![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[WouterLemaire](https://community.sap.com/t5/user/viewprofilepage/user-id/9863)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160885)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160885)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555261)

‎2023 Jul 07
10:06 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160885/tab/all-users "Click here to see who gave kudos to this post.")

912

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

# Introduction

In this blog post series, I’ll show how to create a Web Component and consume it in UI5! This is based on my UI5con session of 2023 together with peter.muessig .

- Vanilla Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-vanilla-web-component/>
- UI5 Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-ui5-web-component/>
- Generate UI5 Library & Controls for UI5 Web Components (this one): <https://blogs.sap.com/2023/07/07/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/>
- Consume UI5 Controls based on UI5 Web Components inside a UI5 app: [https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside...](https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5-app/)

After transforming my Web Component to a UI5 Web Component, time has come to bring it to UI5. We do this by generating a library with a UI5 control for each Web Component. From here it can be used inside a UI5 app as any other UI5 control.

![](/legacyfs/online/storage/blog_attachments/2023/07/image1-3.png)

# Generate library

For generating the library we can use easy-ui5. This has a new generator for this: “library-webc”:

![](/legacyfs/online/storage/blog_attachments/2023/07/image2-3.png)

The generator will ask the same questions as the library generator that we all know with one additional question. It will ask for the UI5 Web Component package. This can be an npm package or a local folder. In my case, I use the folder “./spacepackage” as the UI5 Web Component project and the library are in the same root folder.

![](/legacyfs/online/storage/blog_attachments/2023/07/image3-5.png)

# Prepare project

Open the generated project and install all dependencies using:

```
npm i
```

This template comes with two new commands in the package.json:

* ui5:prebuild

* generate

![](/legacyfs/online/storage/blog_attachments/2023/07/image4-4.png)

# Run prebuild

Execute the prebuild with the following command:

```
npm run ui5:prebuild
```

This will copy all the generrated files from the UI5 Web Component dist folder into the thirdparty folder and integrate it into UI5.

![](/legacyfs/online/storage/blog_attachments/2023/07/image5-3.png)

This will generate a thirdparty folder with all UI5 Web Component resources:

![](/legacyfs/online/storage/blog_attachments/2023/07/image6-2.png)

If you compare the dist folder of the UI5 Web Component and the thirdparty folder of the UI5 Library, you’ll find all the same files except for the TypeScript files.

![](/legacyfs/online/storage/blog_attachments/2023/07/image7-2.png)

It will also integrate the resources as UI5 resources by adding the define function at the top:

![](/legacyfs/online/storage/blog_attachments/2023/07/image8-1.png)

# Run generate

The second command to generate the UI5 controls can be triggered with the following script:

```
npm run generate
```

This script will generate a UI5 control for each UI5 Web Component and generated the library.js file

![](/legacyfs/online/storage/blog_attachments/2023/07/image9-1.png)

Now we have all the missing library files + controls:

![](/legacyfs/online/storage/blog_attachments/2023/07/image10-1.png)

The metadata of the controls (properties,events and aggregations) are generated based on the JSDoc in the UI5 Web Component:

* @type is used for the type of the property

* [@name](/t5/user/viewprofilepage/user-id/1407015) for the name

* @defaultValue for the name

![](/legacyfs/online/storage/blog_attachments/2023/07/image11-1.png)

# Test the generated controls

With the UI5 Web Component resources being copied and controls generated, it is time to test the controls from in the library.

For this we need to provide an example in the kitchen and copy the image:

![](/legacyfs/online/storage/blog_attachments/2023/07/image12.png)

Once everything is in place we can test it by running the start script:

```
npm run start
```

![](/legacyfs/online/storage/blog_attachments/2023/07/image13.png)

This will open the kitchen.html page with the UI5 Control running in it. Under the hood, the UI5 control will use the UI5 Web Component resources for the rendering:

![](/legacyfs/online/storage/blog_attachments/2023/07/image14.png)

The full example is available on GitHub: <https://github.com/lemaiwo/ui5-space-webcomponent-library>

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fui5con-2023-generate-ui5-library-controls-for-ui5-web-components%2Fba-p%2F13555261%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Time-series Forecasting with Generative AI: Integrating HANA AI Toolkit with Joule in SAP Build Code](/t5/technology-blog-posts-by-sap/time-series-forecasting-with-generative-ai-integrating-hana-ai-toolkit-with/ba-...