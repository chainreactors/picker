---
title: TypeScript Sheriff: How can I use TypeScript in the SAP ecosystem? (Part 2 of 3)
url: https://blogs.sap.com/2023/07/05/typescript-sheriff-how-can-i-use-typescript-in-the-sap-ecosystem/
source: SAP Blogs
date: 2023-07-06
fetch_date: 2025-10-04T11:53:36.352566
---

# TypeScript Sheriff: How can I use TypeScript in the SAP ecosystem? (Part 2 of 3)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* TypeScript Sheriff: How can I use TypeScript in th...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160183&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [TypeScript Sheriff: How can I use TypeScript in the SAP ecosystem? (Part 2 of 3)](/t5/technology-blog-posts-by-members/typescript-sheriff-how-can-i-use-typescript-in-the-sap-ecosystem-part-2-of/ba-p/13550830)

![MikeDoyle](https://avatars.profile.sap.com/d/d/iddd343c4ce4009cd31298242b5200ad82602dd6bd1a1b2b32c410bcfcb4459445_small.jpeg "MikeDoyle")

[MikeDoyle](https://community.sap.com/t5/user/viewprofilepage/user-id/13892)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160183)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160183)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550830)

‎2023 Jul 05
5:30 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160183/tab/all-users "Click here to see who gave kudos to this post.")

2,174

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)

* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (4)

**TLDR**: TypeScript is nothing more than JavaScript plus types. TypeScript files with a .ts extension are transpiled to plain JavaScript files with a .js extension, so that they will be understood by a JavaScript runtime. We can use TypeScript wherever we can use JavaScript, and it's well supported in the SAP ecosystem.

Now that we have covered *why* we use TypeScript (**see [Part 1](https://blogs.sap.com/2023/07/05/why-the-typescript-sheriff-has-come-to-clean-up-your-javascript-part-1-of-3/)**), lets move on to explaining what it is and how we can use it.

![](/legacyfs/online/storage/blog_attachments/2023/07/TS-Badge-2.png)

### What is TypeScript?

As explained in the [documentation](https://www.typescriptlang.org/), TypeScript is simply JavaScript plus types.  All of JavaScript is in TypeScript.  If you are familiar with JavaScript then you will be instantly familiar with TypeScript.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-02-at-7.59.36-am.png)

TypeScript is JavaScript plus types

### How does TypeScript work?

If you have built front-end apps using JavaScript (e.g. SAP UI5) you will be familiar with [minifying](https://developer.mozilla.org/en-US/docs/Glossary/Minification) your code. The code we write gets transformed before it runs in the browser. This is just for performance reasons (to speed download). Variable names are shortened, whitespace is removed and files are combined.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-03-at-6.02.31-am.png)

With TypeScript we just add a predecessor step. The code we write gets [transpiled](https://dev.to/kealanparr/compiling-vs-transpiling-3h9i) by the TypeScript compiler before minification. The types, which the runtime doesn’t understand, are removed.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-03-at-6.10.13-am.png)

In the example above we've added types to the function signature.  We've made it clear that the arguments passed in must be of type string/string/Date (see inside parenthesis) and that a string will be returned (see immediately following parenthesis).

As you can see from the diagram, TypeScript files are distinguished by the extension .*ts* (rather than *.js*).  If you open these files they will look just like JavaScript, apart from the types you find here and there.  The transpilation step transforms .ts files to .js files, removing the types.  It is the .js files which can be interpreted by the JavaScript runtime.

Happily, when testing we can still debug the original TypeScript source code (.ts), because these files are still available (to the client browser) for download when in debug mode.

NB this example is for front-end code. With back-end code (e.g. with Node.js running on the server) we don’t need the minification step because the code doesn't need to be downloaded to a client.

### Where can we use TypeScript in an SAP context?

Consider the following scenario.  We are extending the standard functionality of our S/4HANA system.  We are using [SAP BTP](https://community.sap.com/topics/business-technology-platform) to build a side-by-side extension because we want to keep our 'core clean' and enable easy upgrades of S/4HANA.

Where can we use TypeScript in this scenario? Everywhere of course!  Out of the box we get TypeScript support from

* The [SAP Cloud Application Programming Model](https://cap.cloud.sap/docs/) (a.k.a. CAP) which we can use to provision OData services for the back-end of our application

* [SAP UI5](https://sapui5.hana.ondemand.com/), which we can use to build the user interface for the front-end of our application (consuming the CAP services)

* The [SAP Cloud SDK](https://sap.github.io/cloud-sdk/docs/js/overview) which makes it easy for us to consume external services (APIs), such as those provided by S/4HANA

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-03-at-6.42.01-am.png)

At the time of writing these frameworks differ slightly in the level of support they provide for TypeScript. The Cloud SDK, for example, already generates OData Clients in TypeScript form (.ts files) by default. UI5 provides types for controls and modules and the tooling supports TypeScript too.

CAP does provide standard types (e.g. for *Request*) and generating types for the OData services you create is a new feature (see [@cap-js/cds-typer](https://www.npmjs.com/package/%40cap-js/cds-typer)). It's aimed at those using JavaScript (not TypeScript) and in its current form there are some compatibility issues with TypeScript (running cds-ts commands can overwrite the files generated by *cds-typer)*. I would prefer that *cds-typer*would support TypeScript so that we can simply say 'the SAP BTP stack has full TypeScript support' without need of caveats.

NB I have shown an SAP-only stack here, but of course I could use non-SAP tools and frameworks too.  For example I could build the front-end with [React](https://react...