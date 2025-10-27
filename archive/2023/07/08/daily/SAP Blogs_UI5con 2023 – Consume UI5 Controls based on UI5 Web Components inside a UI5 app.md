---
title: UI5con 2023 – Consume UI5 Controls based on UI5 Web Components inside a UI5 app
url: https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5-app/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:33.762564
---

# UI5con 2023 – Consume UI5 Controls based on UI5 Web Components inside a UI5 app

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* UI5con 2023 – Consume UI5 Controls based on UI5 We...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160899&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5con 2023 – Consume UI5 Controls based on UI5 Web Components inside a UI5 app](/t5/technology-blog-posts-by-members/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5/ba-p/13555282)

![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[WouterLemaire](https://community.sap.com/t5/user/viewprofilepage/user-id/9863)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160899)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160899)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555282)

‎2023 Jul 07
10:07 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160899/tab/all-users "Click here to see who gave kudos to this post.")

580

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

# Introduction

In this blog post series, I’ll show how to create a Web Component and consume it in UI5! This is based on my UI5con session of 2023 together with peter.muessig .

- Vanilla Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-vanilla-web-component/>
- UI5 Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-ui5-web-component/>
- Generate UI5 Library & Controls for UI5 Web Components: <https://blogs.sap.com/2023/07/07/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/>
- Consume UI5 Controls based on UI5 Web Components inside a UI5 app (this one): [https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside...](https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5-app/)

Final test in this blog post series, use the UI5 Controls based on UI5 Web Components through a UI5 library in a UI5 app.

![](/legacyfs/online/storage/blog_attachments/2023/07/image1-4.png)

# Run the demo app

* Clone the demo app to test the control

```
git clone https://github.com/lemaiwo/ui5-space-webcomponent-app.git
```

![](/legacyfs/online/storage/blog_attachments/2023/07/image2-4.png)

* Navigate to the project

```
cd ui5-space-webcomponent-app
```

* Install dependencies

```
npm i
```

* Run the app

```
npm start
```

And we have a UI5 app running that consumes UI5 Controls from a UI5 Library that uses UI5 Web Components underneath:

![](/legacyfs/online/storage/blog_attachments/2023/07/image3-6.png)

#

# How it is connected:

## Load the library

The library is loaded by defining this in the manifest.json as a dependency:

![](/legacyfs/online/storage/blog_attachments/2023/07/image4-5.png)

## Use the control

The control can be used in the a view as any normal UI5 control and benefit of all the UI5 functionalities:

* Define the namespace at the top:

![](/legacyfs/online/storage/blog_attachments/2023/07/image5-4.png)

* Use the namespace with the name of the control inside the view:

![](/legacyfs/online/storage/blog_attachments/2023/07/image6-3.png)

## Connect the library

With the new UI5 Tooling we can simply connect to the library by defining it as an npm dependency:

![](/legacyfs/online/storage/blog_attachments/2023/07/image7-3.png)

The full sample project is available on GitHub: <https://github.com/lemaiwo/ui5-space-webcomponent-app>

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5%2Fba-p%2F13555282%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Basic code's of ABAP](/t5/technology-q-a/basic-code-s-of-abap/qaq-p/14231152)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday
* [Build a Code-based Agent using SAP AI Core with Next.js and the Vercel AI SDK](/t5/technology-blog-posts-by-sap/build-a-code-based-agent-using-sap-ai-core-with-next-js-and-the-vercel-ai/ba-p/14230640)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate Guide to SAP S/4HANA Master Data - Part 5](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-part-5/ba-p/14229426)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f...