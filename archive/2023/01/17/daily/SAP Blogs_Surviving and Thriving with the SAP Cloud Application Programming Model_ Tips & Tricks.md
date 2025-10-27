---
title: Surviving and Thriving with the SAP Cloud Application Programming Model: Tips & Tricks
url: https://blogs.sap.com/2023/01/16/surviving-and-thriving-with-the-sap-cloud-application-programming-model-tips-tricks/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:42.114115
---

# Surviving and Thriving with the SAP Cloud Application Programming Model: Tips & Tricks

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Surviving and Thriving with the SAP Cloud Applicat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159320&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Surviving and Thriving with the SAP Cloud Application Programming Model: Types & Tools](/t5/technology-blog-posts-by-sap/surviving-and-thriving-with-the-sap-cloud-application-programming-model/ba-p/13554499)

![maxstreifeneder](https://avatars.profile.sap.com/5/5/id554aba802b1665d064600849415dcc661f0c985a0d9705c3a22c08fbd6170807_small.jpeg "maxstreifeneder")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[maxstreifeneder](https://community.sap.com/t5/user/viewprofilepage/user-id/95)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159320)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159320)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554499)

‎2023 Jan 16
2:03 PM

[47
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159320/tab/all-users "Click here to see who gave kudos to this post.")

6,818

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (1)

If you're anything like me, you've probably been working with the SAP Cloud Application Programming Model (CAP) for Node.js for a while now, but you may still feel like you're only scratching the surface.

Well, fear not – in this series of blog posts, I'll be sharing some tips and tricks on a variety of topics. Whether you're interested in Unit or Integration tests, enable debugging for your app that contains a Cloud Connector, using TypeScript for CAP, or working with metadata for SAP S/4HANA APIs properly, I've (hopefully) got you covered.

I have created a custom tag on the SAP Community, which serves as a marker for all blog posts in my series: [#CAPTricks](https://blogs.sap.com/tag/captricks/).

---

I work in a team called Platform Adoption & Advisory that produces lots of sample repositories for [github.com/sap-samples](https://github.com/topics/btp-use-case-factory), which showcase and combine various SAP Business Technology Platform (SAP BTP) services to extend and integrate SAP solutions, non-SAP solutions or 3rd party software like [Stripe](https://github.com/SAP-samples/btp-create-api-integrations/tree/main) or Twilio. While our focus is often on showcasing these services in context, I often find myself neglecting to deliver beautiful and stable code. Let's be real, we've (hopefully, again) all been there.

In this series of blog posts, I'll be sharing some of my experiences that might help you and who knows, they might help you too (even if you're already a seasoned Node.js/JavaScript dev). In this series, we'll cover topics ranging from the basic setup of a project that can improve your code to common challenges developers may face when working with CAP extensions for SAP systems, such as using on-premise APIs during development.

We'll delve into the general hurdles of working with full-stack CAP applications locally, whether you prefer to work in SAP Business Application Studio or Visual Studio Code. We'll explore how to make your applications as production-ready as possible, including the use of automatic tests with tools like Mocha, Chai, and WDI5. This is one of my favorite topics, and I'm excited to share my experiences and insights with you.

So, to make things a little easier on you (and mainly for me), I've broken up the content into more manageable chunks. That way, you can enjoy the ride without having to wade through a sea of tips & tricks at once. So, buckle up for a few more blog posts. I have no idea how many I'll end up with, but hey, at least you won't have to digest everything at once and I don't have to write everything at once ![:winking_face:](/html/@D1BFF04316CA1FF82DFB90B096AEEE85/emoticons/1f609.png ":winking_face:").

*Disclaimer: This series is not intended to be a comprehensive guide to best practices or anything groundbreaking, but rather a collection of personal experiences and insights that have helped me to be more productive.*

**Why I'm writing this blog post series**

As a self-proclaimed quick-and-dirty JavaScript developer (I'm not even sure I'm qualified to call myself a JavaScript developer), I struggled with CAP Node.js when it came to building samples. In an effort to improve my productivity and the maturity of the content I produce, I decided to dig deeper into some areas beyond the usual sample content. This series of blog posts is the result of that journey.

For experienced devs in these areas, it's not rocket science - it's just a piece of cake (or should I say, daily bread)! If you have any additional insights or perspectives, I'd be thrilled to have a discussion and learn from your feedback and remarks!

[Jump to the end of this blog post](#thewhy) and find a long version of why I’m writing this series.

**TypeScript for CAP**

I really appreciate the simplicity and ease of use of JavaScript compared to Java (lots of boilerplate) but my life has been full of these errors:

```
Uncaught TypeError: service.callFunction is not a function
```

That won't happen with TypeScript, most likely. You don't know anything about TypeScript yet? TypeScript is a programming language that is designed to be used with JavaScript. It takes your TypeScript code and converts it, or "transpiles" it, into regular JavaScript code that can be run in any JavaScript runtime environment. One of the main benefits of using TypeScript is that it allows developers to add optional static typing to their code, which can help catch errors and typos before the code is even executed.

This can save time and effort by catching mistakes early on in the development process, rather than having to debug issues (read more about **[why I love debugging](https://blogs.sap.com/2018/12/13/maxis-adventure-in-sap-cloud-platform-debugging/)** though ![:winking_face:](/html/@D1BFF04316CA1FF82DFB90B096AEEE85/emoticons/1f609.png ":winking_face:")) that only surface at runtime. In contrast, JavaScript is a dynamically-typed language, which means that the data type of a variable is determined at runtime and can hold values of any data type. This can make it more prone to runtime errors, as the code is not checked for correctness until it is actually executed. Features such as code completion, parameter info, quick info, and member lists, are the primary benefit of using TypeScript for me.

CAP now (for quite some time) also offers support for TypeScript, which makes it more convenient and stable to use.

Getting started with TypeScript in CAP is not difficult, and the process ...