---
title: Create and publish your own project templates in SAP Business Application Studio
url: https://blogs.sap.com/2022/11/27/create-and-publish-your-own-project-templates-in-sap-business-application-studio/
source: SAP Blogs
date: 2022-11-28
fetch_date: 2025-10-03T23:55:05.182653
---

# Create and publish your own project templates in SAP Business Application Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Create and publish your own project templates in S...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161093&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create and publish your own project templates in SAP Business Application Studio](/t5/technology-blog-posts-by-sap/create-and-publish-your-own-project-templates-in-sap-business-application/ba-p/13559751)

![avitalmargalit](https://avatars.profile.sap.com/b/9/idb924861f1a714e69021cc96dfde549a37924b139b2095329fe38d112a048280d_small.jpeg "avitalmargalit")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[avitalmargalit](https://community.sap.com/t5/user/viewprofilepage/user-id/584343)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161093)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161093)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559751)

‎2022 Nov 27
3:42 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161093/tab/all-users "Click here to see who gave kudos to this post.")

3,572

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (3)

How many times have you thought “I wish I could save this application as a template”, or “I wish I could easily generate this code and share it with others”?

Well, we’ve thought about this too! With SAP Business Applications Studio (aka BAS), you can create a template using the open-source [Yeoman](https://yeoman.io/) for project generation framework and share it with others. You can't imagine how simple it is.

If you are thinking of creating a template in BAS, this blog is for you.

In this blog I will show you how to convert your yeoman generator into a BAS template. But don’t worry, it’s worth the effort because most BAS users are using the ‘Template wizard’ to create their new projects. The wizard contains a step-by-step graphical user interface, and it also allows users to explore and select the project template that best fits their needs.

Note that when customers use your template, they will become the owners of the code they write.

![](/legacyfs/online/storage/blog_attachments/2022/11/ApplicationWizard.png)

Application Wizard in SAP Business Application Studio

Before you start, keep in mind that the Yeoman generator should be short (we recommend up to 6 or 7 questions/decisions), and it should generate a complete set of resources that the developer can build/run/deploy. It is OK not to provide an answer for all the questions (e.g., it may not be bound to a service). The generator can create placeholders that can be replaced by the user or another generator at a later stage. Each generator should create a markdown file noting what was generated and how to proceed.

The flexibility acquired from this type of template fits the 'Grow-as-you-go' concept we believe in, where the developers can run generators whenever they need them.

Let’s dive to understand how this is done!

## Yeoman Generator Creation

To create your template, you must first create a yeoman generator on which it will be based.

To do so, please follow the steps in the [Yeoman](https://yeoman.io/) documentation.

## Making your generator accessible as a template

Once you have created a template based on your yeoman generator, you want to make it accessible from BAS so that your users can search for it in the BAS Template wizard.

The steps for making this happen are different if you are an extension developer for BAS or not.

### If you already have a VS Code extension

* Declare your Yeoman generator as being of type `project` in your generator's '[package.json](https://github.wdf.sap.corp/devx-wing/generator-s4-ext/blob/71e05cfc029873cd5f89e2061bbe51930eee3105/package.json#L102)' file.
  For example:

```
```javascript

"generator-filter": {

    "type": "project"

  },

```
```

* Use the following example in your generator's '[package.json](https://github.wdf.sap.corp/devx-wing/vscode-wing-welcome-screen/blob/64a9fa3172b1e607eba96648185d03456f8f1c42/wing-vsix/package.json#L46)' file <https://github.com/SAP/yeoman-ui/blob/master/packages/generator-foodq/package.json>

### **If you don’t have a VS Code extension**

* Upload your generator to the [Yeoman generator registry](https://yeoman.io/generators/), and then install it in BAS. To do so, in the command palette, enter ‘Template Wizard’, then click Explore and Install Generators from the upper-right corner of the Template wizard.

![](/legacyfs/online/storage/blog_attachments/2022/11/ExploreTemplate.png)

Explore and Install Template in SAP Business Application Studio

* The Explore and Install Generators tool opens in a new tab showing the generators from the [Yeoman generator registry](https://yeoman.io/generators/). Click Install. The generator is added to your machine and can now be selected from the Template Wizard. This will make your template visible in the Template Wizard.

## Best practices for writing a Yeoman Generator for BAS

Provide a prompt(s) and the questions (within each prompt) used in the wizard, including the default answers.

Prompts can be added to the metadata so that the developers can have an indication of which steps they have left. If there are no prompts in the metadata, or the generator adds prompts dynamically, then they are added dynamically to the UI.

The Yeoman Player receives prompts and renders them to steps and questions according to the question type (input, list, confirmation, etc.). The player is an extensible component that can support more question and custom types in the future.

Each template contains the following metadata:

* List of the prompts to show in the UI

* Image

* Name

* Description

* More information

To render your generator well in the wizard, follow these guidelines:

* Group several questions into a single prompt – all questions in the same prompt will render as a single wizard step.

* Guide the user by showing the prompts in advance.

You can further enhance your generator by adding subgenerators, adding hints and questions, adding a logger, and more, see this [example](https://github.com/SAP/yeoman-ui/tree/ma...