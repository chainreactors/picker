---
title: TypeScript Sheriff: Tips for newbies (Part 3 of 3)
url: https://blogs.sap.com/2023/07/05/typescript-sheriff-tips-for-newbies-part-3-of-3/
source: SAP Blogs
date: 2023-07-06
fetch_date: 2025-10-04T11:53:33.823168
---

# TypeScript Sheriff: Tips for newbies (Part 3 of 3)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* TypeScript Sheriff: Tips for newbies (Part 3 of 3)

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160534&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [TypeScript Sheriff: Tips for newbies (Part 3 of 3)](/t5/technology-blog-posts-by-members/typescript-sheriff-tips-for-newbies-part-3-of-3/ba-p/13552828)

![MikeDoyle](https://avatars.profile.sap.com/d/d/iddd343c4ce4009cd31298242b5200ad82602dd6bd1a1b2b32c410bcfcb4459445_small.jpeg "MikeDoyle")

[MikeDoyle](https://community.sap.com/t5/user/viewprofilepage/user-id/13892)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160534)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160534)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552828)

‎2023 Jul 05
5:31 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160534/tab/all-users "Click here to see who gave kudos to this post.")

1,589

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

**TLDR:**We *can* use TypeScript types in every line of our code, but that doesn't mean that we *have* to use them in every line.  You can configure the TypeScript compiler as well as clearing its cache, if you need to. Let the IDE handle those imports.

If you need a recap on why we use TypeScript and how we use it **check out [Part 1](https://blogs.sap.com/2023/07/05/why-the-typescript-sheriff-has-come-to-clean-up-your-javascript-part-1-of-3/) and [Part 2](https://blogs.sap.com/2023/07/05/typescript-sheriff-how-can-i-use-typescript-in-the-sap-ecosystem/) of this series.**

![](/legacyfs/online/storage/blog_attachments/2023/07/cactus2-1.png)

In this final post of the series I will share some tips on how to use TypeScript in your SAP-ecosystem development.  I'm a recent convert (or 'reformed character' if you prefer) rather than a TypeScript expert, but I hope this perspective will be useful for others.

### Use the import prompt

We use import statements to reference the types provided by the various frameworks that I discussed in the previous post. This is particularly important in UI5 development where we need to need to use the types that correspond to the UI controls on our views. The good news is that our IDE can add the import statements for us.

In this example, from SAP Business Application Studio,  we can click on the Quick Fix prompt.....

![](/legacyfs/online/storage/blog_attachments/2023/07/Import1.jpg)

...and then choose from the list of matching types

![](/legacyfs/online/storage/blog_attachments/2023/07/Import2.png)

The import statement will be added for us.  In this case there is ambiguity (which 'Button' class are we referencing?) but if the module name is unique the import will be added automatically.

### Watch your case

In TypeScript, as in JavaScript, primitives are written all lower case: e.g. ***s**tring, **n**umber, **b**oolean*.  Object types have title case: e.g. *Date*. With *string* in particular you need to be careful to [use the correct case](https://www.geeksforgeeks.org/what-is-the-difference-between-string-and-string-in-typescript/).  As we are usually referring the primitive type we should almost always be using **s**tring rather than **S**tring in our types.

### Less is more

Once I was up and running with TypeScript I loved using types and declared an explicit type everywhere I could.  The downside to this is that the code becomes a little 'busy'.

TypeScript is smart enough to distinguish between situations in which an explicit type is needed and when there is no ambiguity and the type can be inferred, so in my opinion it's best to leave out the explicit types unless they add value. Consider the following example. The calculateAgeAtDeath function accepts a Sheriff object as a parameter and returns the age of the that sheriff (a number).  The return type of the function is explicitly declared as is the type of the variable we assigned to it.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-05-at-11.34.00-am.png)

Both of these declarations are redundant and can be removed.  The return type of the function will always be number, because are returning the difference between two numbers.  If so, the variable to which we assign that return value will also be a number.  We can dispense with the types altogether.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-05-at-3.02.34-pm.png)

### Clearing the cache

Very occasionally your IDE may report spurious errors.  This can be resolved by clearing the cache of the TypeScript compiler.  In Business Application Studio (or Visual Studio Code) this can be done with the *Restart TS Server* command.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-05-at-3.03.40-pm.png)

Use the menu path *View->Command Palette* then type to filter the commands until *Restart TS Server* appears. NB You must have a .ts file open in the editor when you launch the Command Palette, otherwise this command won't appear.

### Taking a break from types

Of course when using TypeScript we want to declare types wherever they resolve ambiguity and add value (see above).  There may occasionally be times however when you feel that including types is too difficult or impedes your 'flow' too much.

One simple approach in this scenario is to [use the generic *any*type](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html#any).  This is a way to acknowledge that a type is appropriate but still leave the exact type to be inferred at run-time.

```
let something: any = …
```

If you're doing this then your code may have a .ts suffix but it isn't really superior to the plain JavaScript we are replacing! For this reason you are risking a knock at the door from the TypeScript Sheriff

![](/legacyfs/online/storage/blog_attachments/2023/07/Scene4-2.jpeg)

The TypeScript Sheriff

There are also [annotations](https://timmousk.com/blog/typescript-ignore-next-line/#:~:text=To%20ignore%20all%20TypeScript%20compiler%20errors%...