---
title: UI5con 2023 – Vanilla Web Component
url: https://blogs.sap.com/2023/07/07/ui5con-2023-vanilla-web-component/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:30.177659
---

# UI5con 2023 – Vanilla Web Component

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* UI5con 2023 - Vanilla Web Component

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160883&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5con 2023 - Vanilla Web Component](/t5/technology-blog-posts-by-members/ui5con-2023-vanilla-web-component/ba-p/13555255)

![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[WouterLemaire](https://community.sap.com/t5/user/viewprofilepage/user-id/9863)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160883)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160883)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555255)

‎2023 Jul 07
10:07 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160883/tab/all-users "Click here to see who gave kudos to this post.")

1,079

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (1)

# Introduction

In the next following blog post series, I’ll show how to create a Web Component and consume it in UI5! This is based on my UI5con session of 2023 together with peter.muessig .

- Vanilla Web Component (this one): <https://blogs.sap.com/2023/07/07/ui5con-2023-vanilla-web-component/>
- UI5 Web Component: <https://blogs.sap.com/2023/07/07/ui5con-2023-ui5-web-component/>
- Generate UI5 Library & Controls for UI5 Web Components: <https://blogs.sap.com/2023/07/07/ui5con-2023-generate-ui5-library-controls-for-ui5-web-components/>
- Consume UI5 Controls based on UI5 Web Components inside a UI5 app: [https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside...](https://blogs.sap.com/2023/07/07/ui5con-2023-consume-ui5-controls-based-on-ui5-web-components-inside-a-ui5-app/)

Web Components is a different technology which is the foundation for many new UI5 controls, especially all the controls in the sap.ui.webc library. It is now also possible to create your own UI5 control starting from a Web Component. When using a Web Component for a UI5 control it will have a big impact on the performance of the rendering of UI5 controls including the full UI5 app. Therefore, it is important to understand how Web Components work and create Web Components in the best possible way. Controls are the foundation of the UI5 framework, the better the web components, the better UI5 apps will run.

The official definition of WebComponents: Web components are a set of web platform APIs that allow you to create new custom, reusable, encapsulated HTML tags to use in web pages and web apps. Custom components and widgets build on the Web Component standards, will work across modern browsers, and can be used with any JavaScript library or framework that works with HTML. Read more here: [Introduction - webcomponents.org](https://www.webcomponents.org/introduction)

With UI5 Web Components it is important to understand how Web Components work in general. Once we understand how they work, we can look on how to integrate them. For this, I created a Vanilla Web Component which I’ll convert later into a UI5 Web Component. Afterwards, I’ll integrate this in a UI5 app.

![](/legacyfs/online/storage/blog_attachments/2023/07/image1-1.png)

I made a Web Component for the famous Star Wars intro with a title, logo and a list of episodes:

![](/legacyfs/online/storage/blog_attachments/2023/07/image2-1.png)

# Web Component Usage

The html behind this star wars intro is nothing more than the following html:

![](/legacyfs/online/storage/blog_attachments/2023/07/image3-3.png)

Thanks to Web Components I can simple use the html tags “space-intro” and “space-article” but behind those tags is some logic hidden. The Web Component allows us to use our custom created html tags multiple times and always behave in the same way. The Web Component comes with his own html template, css stylesheet and a JavaScript/TypeScript class.

Full index.html page code: <https://github.com/lemaiwo/space-webcomponent/blob/main/index.html>

# Register Web Component tags

The **custom html tags** are connected to the Web Component by registering the JavaScript/TypeScript class as a customElement with the name of the html tag. This is done by using the define function on the global variable “customElements” :

* space-intro with SpaceComponent

* space-article with SpaceArticleComponent

# Web Component classes

The Web Component classes extend from the class HTMLElement which is the base class for a Web Component.

I have two Web Components:

* Space Component: This is the main Web Component with the intro, logo and background

* Space Item Component: This is used for showing one or multiple episodes inside the Space Component.

![](/legacyfs/online/storage/blog_attachments/2023/07/image4-2.png)

Both Web Components act as parent and child where Space is the parent of Space Item.

In the constructor we attach the shadow root to the Web Component. The shadow root is key for encapsulating the Web Component, read more about shadow dom here: <https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM>

Once the shadowroot is attached, we need to add the html template to the shadowroot. The html template can be defined in different ways, in the JavaScript/TypeScript class as a concatenated string or using the html tag template in the html. In this case, I used the html “template” tag in the index.html page just because it is easier to read and maintain:

![](/legacyfs/online/storage/blog_attachments/2023/07/image5-1.png)

Once the template is set, we can set the values of the Web Component attributes into the template.

In this specific case, the constructor also contains some logic for generating the stars in the background.

![](/legacyfs/online/storage/blog_attachments/2023/07/image6-1.png)

In the SpaceComponent one attribute is defined as “observedAttribute”: “intro”. This means that the Web Component will react on any changes of this attribute by calling the “attributeChangedCallback” function. This is also the place to update the intro value in the template:

![](/legacyfs/online/storage/blog_attachments/2023/07/image7-1.png)

The Web Component class for Space Article is a bit more simplified. It only has two attributes, title and body. The constructor is similar to the one of the Space Web Component, attach ShadowRoot, add html template and set the values in the template:

![](/legacyfs/online/storage/blog_attachments/2023/07/image8.png)

Again, make the attributes observable and set the values into the template:

![](/legacyfs/online/storage/blog_attachments/2023/07/image9.png)

With that, the two Web Components are created.

Full code of the Web Component is avai...