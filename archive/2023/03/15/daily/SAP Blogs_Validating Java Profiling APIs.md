---
title: Validating Java Profiling APIs
url: https://blogs.sap.com/2023/03/14/validating-java-profiling-apis/
source: SAP Blogs
date: 2023-03-15
fetch_date: 2025-10-04T09:35:31.891420
---

# Validating Java Profiling APIs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Validating Java Profiling APIs

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157451&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Validating Java Profiling APIs](/t5/technology-blog-posts-by-sap/validating-java-profiling-apis/ba-p/13549325)

![JohannesBechberger](https://avatars.profile.sap.com/c/5/idc5e1135285c1ada7827c86b7ed2c6652149fe44be8e72c02f59de2be90e1f5c3_small.jpeg "JohannesBechberger")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[JohannesBechberger](https://community.sap.com/t5/user/viewprofilepage/user-id/123886)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157451)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157451)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549325)

‎2023 Mar 14
5:32 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157451/tab/all-users "Click here to see who gave kudos to this post.")

747

* SAP Managed Tags
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)
* [SAP Java Virtual Machine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Java%2520Virtual%2520Machine/pd-p/01200615320800003576)

* [SAP Java Virtual Machine

  SAP Java Virtual Machine](/t5/c-khhcw49343/SAP%2BJava%2BVirtual%2BMachine/pd-p/01200615320800003576)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (2)

In my last post, I covered a correctness bug in the fundamental Java profiling API AsyncGetCallTrace that I found just by chance. Now the question is: Could we find such bugs automatically? Potentially uncovering more bugs or being more confident in the absence of errors. I already wrote code to test the stability of the profiling APIs, testing for the lack of fatal errors, in my [jdk-profiling-tester](https://github.com/parttimenerd/jdk-profiling-tester) project. Such tools are invaluable when modifying the API implementation or adding a new API. This post will cover a new prototypical tool called [trace\_validation](https://github.com/parttimenerd/trace_validation) and its foundational concepts. I focus here on the AsyncGetCallTrace and GetStackTrace API, but due to the similarity in the code, JFR should have similar correctness properties.

*The tool took far longer to bring to a usable(ish) state; this is why I didn't write a blog post last week. I hope to be on schedule again next week.*

## AsyncGetCallTrace and GetStackTrace

A short recap from my blog series ["Writing a Profiler from Scratch"](https://mostlynerdless.de/blog/tag/writing-a-profiler-from-scratch/): Both APIs return the stack trace for a given thread at a given point in time (A called B, which in turn called C, ...):

![](https://mostlynerdless.de/wp-content/uploads/2023/01/asgct_2-2000x1125.png)

AsyncGetCallTrace

The only difference is that AsyncGetCallTrace (ASGCT) returns the stack trace at any point in the execution of the program and GetStackTrace (GST) only at specific safe points, where the state of the JVM is defined. GetStackTrace is the only official API to obtain stack traces but it has precision problems. Both don't have more than a few basic tests in the OpenJDK.

## Correctness

But when is the result of a profiling API deemed to be correct? If it matches the execution of the program.

This is hard to check if we don't modify the JVM. But it is relatively simple to check for small test cases where the most runtime is spent in a single method. We can then check directly in the source code whether the stack trace makes sense. We will come back to this answer soon.

The basic idea for automation is to automatically compare the returns of the profiling API to the returns of an oracle. But, we sadly don't have an oracle for the asynchronous AsyncGetCallTrace yet, but we can create one by weakening our correctness definition and building up our oracle in multiple stages.

## Weakening the correctness definition

In practice, we don't need the profiling APIs to return the correct result in 100% of all cases and for all frames in the trace. Typical profilers are sampling profilers and therefore approximate the result anyway. This makes the correctness definition easier to test, as it lets us make the trade-off between feasibility and precision.

## Layered oracle

The idea is now to build our oracle in different layers. We are starting with basic assumptions and writing tests to verify that the layer above is probably correct too. This is leading us to our combined test of asynchronous AsyncGetCallTrace. This has the advantage that every check is relatively simple, which is essential because the whole oracle depends on how much we trust the basic assumptions and the tests that verify that a layer is correct. I describe the layers and checks in the following:

![](https://mostlynerdless.de/wp-content/uploads/2023/03/layers.png)

Different layers of trace\_validation

## Ground layer

We start with the most basic assumption as our ground layer: An approximation of the stack traces can be obtained by instrumenting the byte code at runtime. The idea is to push at every entry of a method the method and its class (the frame) onto a stack and to pop it at every exit:

```
class A {

 void methodB() {

   // ...

 }

}
```

... is transformed into ...

```
class A {

 void methodB() {

   trace.push("A", "methodB");

   // ...

   trace.pop();

 }

}
```

The instrumentation agent modifies the bytecode at runtime, so every exit of the method is recorded. *I used the great [Javassist](https://www.javassist.org/) library for the heavy lifting.* We record all of this information in thread-local stacks.

This does not capture all methods, because we cannot modify native methods implemented in C++, but it covers most of the methods. This is what I meant by an approximation before. A problem with this is the cost of the instrumentation. We can make a trade-off between precision and usefulness by only instrumenting some of the methods.

We can ask the stack data structure to approximate the current stack trace in the middle of every method. These traces are by construction correct, especially when we implement the stack data structure in native code, only exposing the `Trace::push` and `Trace::pop` methods. This limits the code reordering by the JVM.

## GetStackTrace layer

As I described above, this API is the official API to get the stack traces and it is not limited to basic stack walking, as it walks only when the JVM state is defined. One could therefore assume that it returns the correct frames. This is what I did in my previous blog post. But we should test this assumption: We can create a native `Trace::check` which calls GetStackTrace and checks that all frames of `Trace` are present and in the correct order. Calls to this method are inserted after the call to `Trace::push` at the beginning o...