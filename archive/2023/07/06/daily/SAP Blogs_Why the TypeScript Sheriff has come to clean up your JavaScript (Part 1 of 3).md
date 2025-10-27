---
title: Why the TypeScript Sheriff has come to clean up your JavaScript (Part 1 of 3)
url: https://blogs.sap.com/2023/07/05/why-the-typescript-sheriff-has-come-to-clean-up-your-javascript-part-1-of-3/
source: SAP Blogs
date: 2023-07-06
fetch_date: 2025-10-04T11:53:39.223833
---

# Why the TypeScript Sheriff has come to clean up your JavaScript (Part 1 of 3)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Why the TypeScript Sheriff has come to clean up yo...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160136&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Why the TypeScript Sheriff has come to clean up your JavaScript (Part 1 of 3)](/t5/technology-blog-posts-by-members/why-the-typescript-sheriff-has-come-to-clean-up-your-javascript-part-1-of-3/ba-p/13550500)

![MikeDoyle](https://avatars.profile.sap.com/d/d/iddd343c4ce4009cd31298242b5200ad82602dd6bd1a1b2b32c410bcfcb4459445_small.jpeg "MikeDoyle")

[MikeDoyle](https://community.sap.com/t5/user/viewprofilepage/user-id/13892)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160136)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160136)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550500)

‎2023 Jul 05
5:26 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160136/tab/all-users "Click here to see who gave kudos to this post.")

2,137

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

**TLDR**: TypeScript simply adds types to JavaScript.  We can reduce run-time errors by catching more bugs at design-time. It doesn't ruin the flexibility and expressiveness of JavaScript and it's easy to start using TypeScript in your SAP development today.

![](/legacyfs/online/storage/blog_attachments/2023/07/cactus2.png)

JavaScript is one of the most important programming languages. In the 2023 Stack Overflow developer survey it was listed as *the*[most commonly used language amongst professional developers](https://survey.stackoverflow.co/2023/#most-popular-technologies-language-prof).   I enjoy using JavaScript because I find it's flexibility is conducive to good '[flow](https://www.bbc.com/worklife/article/20190204-how-to-find-your-flow-state-to-be-peak-creative)'. It's easy for me to 'express myself' as I write.

It's also pervasive because it runs almost everywhere. Every modern browser has a JavaScript runtime, but of course it can [run on servers](https://nodejs.org/) too.

A downside of the *dynamic* typing inherent in JavaScript (as opposed to the *static* typing of Java, for example) is that it's easy for type-related bugs to slip through the net and materialise as run-time errors.

What if there was a way to catch these bugs at design-time, without spoiling the expressiveness and flexibility of JavaScript? Such a tool would have a big potential to change the world, because of the near-ubiquity of JavaScript . Happily there is such a tool, and it goes by the name of [**TypeScript**](https://www.typescriptlang.org/).

In this short series I would like to introduce you to TypeScript and explain how it can improve your JavaScript development.  I will focus on the SAP ecosystem and I hope to share the perspective of a new convert, not an expert (because I am not a TypeScript expert).

To learn more we must head to the 'old west' where we will meet the TypeScript Sheriff.  He's tough on type errors but don't worry for your safety.  As long as you aren't a cowboy coder you have nothing to fear...

![](/legacyfs/online/storage/blog_attachments/2023/07/Scene4.jpeg)

The TypeScript Sheriff

### Why TypeScript?

The easiest way to explain *why*TypeScript exists is to consider a simple example. Here we scaffold a function to book a ticket on a stagecoach, then we call the function to book a seat from San Francisco to Boulder City

```
function stagecoachBook(startPoint, endPoint, date) {

    //logic here

}

stagecoachBook(new Date("1860-06-17T00:00:00"), "San Francisco", "Boulder City");
```

This JavaScript code looks good, but when we run it what will happen? A run-time error!  Whilst we have the correct number of parameters, they aren't in the right order.  Many [IDEs](https://www.freecodecamp.org/news/what-is-an-ide-in-programming-an-ide-definition-for-developers/) (& [linters](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/)) won't pick this up.  It might be easy enough to find the bug (depending on our test coverage) but what if the mistake is in a obscure piece of code that only runs in exceptional circumstances?

Far better to introduce static types, as in this TypeScript example below.  Now we specify the types of the function parameters

```
function stagecoachBook(startPoint: string, endpoint: string, date: Date) {

    //logic here

}

stagecoachBook(new Date("1860-06-17T00:00:00"), "San Francisco", "Boulder City");
```

The IDE will give us an error like this:
> **Argument of type 'Date' is not assignable to parameter of type 'string'.**

So much better to find our error at design-time! Other common type errors prevented are typos in function names and assignments to constants (using *const* when you should have used *let*).

Zooming up from the desert weeds to a wider vista it should be obvious that the advantages are more than just avoiding the errors shown in these simple examples.  Explicitly declaring types makes code easier to read. In larger codebases it makes life much easier if consumers of library functions can see exactly what parameters they should pass.

Another big advantage is that including types enables the IDE to support code completion, which makes us more productive. Imagine if you have an entity with a large number of properties. How great to have code completion on those property names.

Do you think TypeScript might assist you in your JavaScript programming?  Would you like to reduce the number of runtime errors you have to remediate?  If so **move on to [Part 2](https://blogs.sap.com/2023/07/05/typescript-sheriff-how-can-i-use-typescript-in-the-sap-ecosystem/) in the series**, in which we will discuss how to use TypeScript in the SAP ecosystem. **[Part 3](https://blogs.sap.com/2023/07/05/typescript-sheriff-tips-for-newbies-part-3-of-3/) will cover some tips** to help you get started.

* [typescript](/t5/tag/typescript/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already regist...