---
title: ThreadContext in  SAP Cloud SDK Version 4
url: https://blogs.sap.com/2022/11/30/threadcontext-in-sap-cloud-sdk-version-4/
source: SAP Blogs
date: 2022-12-01
fetch_date: 2025-10-04T00:11:23.005576
---

# ThreadContext in  SAP Cloud SDK Version 4

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* ThreadContext in SAP Cloud SDK Version 4

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161317&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ThreadContext in SAP Cloud SDK Version 4](/t5/technology-blog-posts-by-sap/threadcontext-in-sap-cloud-sdk-version-4/ba-p/13560544)

![charlesdubois](https://avatars.profile.sap.com/4/4/id4450144d666d4c622a7a62829d6afc812fc3d240634dbc12aee23fb989b72942_small.jpeg "charlesdubois")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[charlesdubois](https://community.sap.com/t5/user/viewprofilepage/user-id/795487)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161317)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161317)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560544)

‎2022 Nov 30
7:45 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161317/tab/all-users "Click here to see who gave kudos to this post.")

1,200

* SAP Managed Tags
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)

* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)

View products (3)

With the [release of version 4.0.0](https://blogs.sap.com/2022/10/20/version-4-of-the-sap-cloud-sdk-for-java-is-here/), the `ThreadContext` has seen major changes in the SAP Cloud SDK.
This blog post will explain the changes we made that simplify running tasks on different threads with the `ThreadContext` attached.

## What is a ThreadContext?

The SAP Cloud SDK for Java provides a so-called [`ThreadContext`](https://help.sap.com/doc/b579bf8578954412aea2b458e8452201/1.0/en-US/com/sap/cloud/sdk/cloudplatform/thread/ThreadContext.html).
It serves as thread-safe storage for potentially sensitive information.
A few of the most important objects stored are:

* The current *Tenant*

* The current *Principal* (User)

* The [JSON Web Token](https://jwt.io) (JWT)

This information is used throughout the SAP Cloud SDK to provide features like tenant and principal isolation, JWT verification and authorization against other systems and services.
Every servlet that is received in its own thread, will receive a `ThreadContext`.
This ensures different tenants and users are properly isolated.

## A Typical Use Case

Let's say we need to run a **lengthy operation** upon receiving a request.
The simple solution would be to **block the servlet** for as long as the operation takes:

```
@RestController

public class HelloWorldController

{

    @GetMapping( "/hello" )

    public String getHello()

    {

        final ThreadContext currentContext = ThreadContextAccessor.getCurrentContext();

        database.store(currentTenant);// long-running operation

        return "Hello";

    }

}
```

Because the Spring servlet has its own thread we automatically get access to the `ThreadContext`.

But our users now experience **long loading times** because the servlet takes a long time to answer.
We need to offload the long-running operation to another thread.

### Asynchronous Operations with SAP Cloud SDK Version 3

We can call an `@Async` annotated method:

```
@RestController

public class HelloWorldController

{

    @Autowired

    private DatabaseAccess databaseAccess;

    @GetMapping( "/hello" )

    public String getHello()

    {

        databaseAccess.store();

        return "Hello";

    }

}
```

The `@Async` method must be public in another class to be executed in a separate thread:

```
@EnableAsync

@Configuration

public class DatabaseAccess

{

    @Async

    public String store()

    {

        final ThreadContext currentContext = ThreadContextAccessor.getCurrentContext();// doesn't work

        database.store(currentTenant);// long-running operation

        return "success";

    }

}
```

However, this breaks the Multi Tenancy of the SAP Cloud SDK.
We cannot access the current tenant in the new thread.

#### Propagate the ThreadContext

We can try to use the `ThreadContextExecutor` to propagate the `ThreadContext` to the new thread:

```
@RestController

public class HelloWorldController

{

    @Autowired

    private DatabaseAccess databaseAccess;

    @GetMapping( "/hello" )

    public String getHello()

    {

        final ThreadContextExecutor executor = new ThreadContextExecutor();

        databaseAccess.store(executor);

        return "Hello";

    }

}
```

```
@EnableAsync

@Configuration

public class DatabaseAccess

{

    @Async

    public String store( ThreadContextExecutor executor )

    {

        return executor.execute(() -> {

            final ThreadContext currentContext = ThreadContextAccessor.getCurrentContext();// unreliable

            database.store(currentTenant);// long-running operation

            return "success";

        });

    }

}
```

But the access is unreliable because **the `ThreadContext` will get removed** when the servlet is finished.
We can also see that the resulting code has a lot of **boilerplate code**.
Let's take a look at how this use case would be done with SAP Cloud SDK 4.

### Asynchronous Operations with SAP Cloud SDK Version 4

With version 4 you can simplify your code for running asynchronous tasks with the newly introduced `ThreadContextExecutors`:

```
Future runningTask = ThreadContextExecutors.submit(() -> operation());
```

This functionality is conveniently integrated to work with Springs `@Async` annotation like so:

```
@RestController

public class HelloWorldController

{

    @Autowired

    private DatabaseAccess databaseAccess;

    @GetMapping( "/hello" )

    public String getHello()

    {

        databaseAccess.store();

        return "Hello";

    }

}
```

```
@Configuration

public class DatabaseAccess

{

    @Async

    public void store()

    {

        database.store(TenantAccessor.getCurrentTenant());// long-running operation

    }

}
```

This is thanks to this `@Configuration` all methods annotated with `@Async` will have the `ThreadContext` available:

```
@EnableAsync

@Configuration

public class AsynchronousConfiguration implements AsyncConfigurer

{

    @Override

    public Executor getAsyncExecutor()

    {

        return ThreadContextExecutors.getExecutor();

    }

}
```

This already comes out of the box on newly generated applications such as `scp-cf-spring`.
You can read more about the `@Async` functionalit...