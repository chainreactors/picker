---
title: Breathe Life into Your Services by Using Actions and Functions in SAP Cloud Application Programming Model
url: https://blogs.sap.com/2023/07/14/breathe-life-into-your-services-by-using-actions-and-functions-in-sap-cloud-application-programming-model/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:53:02.548330
---

# Breathe Life into Your Services by Using Actions and Functions in SAP Cloud Application Programming Model

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Breathe Life into Your Services by Using Actions a...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160246&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Breathe Life into Your Services by Using Actions and Functions in SAP Cloud Application Programming Model](/t5/technology-blog-posts-by-sap/breathe-life-into-your-services-by-using-actions-and-functions-in-sap-cloud/ba-p/13557116)

![UliBestfleisch](https://avatars.profile.sap.com/9/5/id9509feaf2430249cd1f540d8ccb0b775176bebf8c3ae6d2628e56af222712427_small.jpeg "UliBestfleisch")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[UliBestfleisch](https://community.sap.com/t5/user/viewprofilepage/user-id/215265)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160246)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160246)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557116)

‎2023 Jul 14
6:52 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160246/tab/all-users "Click here to see who gave kudos to this post.")

4,673

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (1)

When building your application with the [SAP Cloud Application Programming Model](https://cap.cloud.sap/) you can make use of [actions and functions](https://cap.cloud.sap/docs/guides/providing-services#custom-actions-functions). A question that often comes up is when you should use these and what their benefit is. In this blog I want to share my perspective and why I consider them an important element in application development.

## May I Introduce: Actions and Functions in CAP

Simply put, [actions and functions in CAP](https://cap.cloud.sap/docs/guides/providing-services#custom-actions-functions) are like methods in object-oriented programming. Actions have side-effects on application state, whereas functions are pure and free of side-effects. Like methods, both actions and functions can have parameters and a return value. Functions are required to have a return value, for actions this is optional.

A further differentiation is that of bound vs. unbound. Staying in the OO metaphor bound actions and bound functions are instance methods, unbound actions and unbound functions are static methods.

Let’s look at a variation of the bookshop example to illustrate the ideas and start with an excerpt from the data model, that contains a publication status of a book. Please note that *publicationStatus* is a read-only element.

```
entity Book : managed {

  key ID : UUID;

  title  : String;

  summary : String;

  @readonly

  publicationStatus: String enum {

    UNPUBLISHED;

    PUBLISHED;

    DELISTED;

  } default 'UNPUBLISHED';

}
```

On top there are two services: A maintenance service for maintaining the book catalog, and a book selling service that allows consumers to buy books. Let’s first have a look at the book maintenance service:

```
service BookMaintenanceService {

    entity Book as projection on samples.Book actions {

        action publish();

        action delist();

    };

    action applyDiscount(percentage: Decimal, validFrom: Date, validTo: Date);

}
```

There are two bound actions on a book: *publish* and *delist*. The action implementation (not shown here) will set the publication status on a book, which is not changeable directly being annotated with *@readonly*. The third action *applyDiscount* is an unbound action that will set a discount on all books within a certain timeframe.

The book selling service contains a bound action *addToShoppingCart* on the book that obviously adds the book to a consumer shopping cart. The bound function *calculateDeliveryDate* determines the delivery date of a book given the country and address.

```
service BookSellingService {

    entity Book as projection on samples.Book actions {

        action addToShoppingCart();

        function calculateDeliveryDate(country: Country, address: String) returns Date;

    }

}
```

Actions and functions are a [concept of OData](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793737) that has been adopted by CDS and CAP. Consequently, actions and functions are exposed by CAP using the OData protocol. [This cheat sheet](https://blogs.sap.com/2021/08/21/cheat-sheet-for-uri-patterns-for-calling-odata-actions-and-functions/) summarizes nicely how in OData actions and functions can be called. You can also [call actions and functions programmatically](https://cap.cloud.sap/docs/guides/providing-services#calling-actions-or-functions) on CAP services, in both CAP Node.js and CAP Java.

Actions and functions are [nicely integrated into Fiori Elements](https://cap.cloud.sap/docs/advanced/fiori#actions) and can be declaratively put on object pages and list reports where they will simply become buttons for users.

## Situations for Actions

In my experience you should consider using actions in the following situations:

1. An important business process step is triggered where you need *a controlled way of getting from state A to state B*. A typical example is status of an entity that often represents a business process step. Of course, one can model a status element and allow this element to be changed directly. However, you may not want to allow every status transition, or check pre-conditions for a status change. In our books example you might want to check the completeness of book details before publishing it. An action gives you a direct, explicit lever to do so. Dedicated buttons on the user interface (different from create, update, and delete) are an indication that you are triggering such a dedicated business process step.If you’d implement this as part of an update request, you can achieve this as well. However you need to figure out from the changed elements what the actual business intent behind was. This might be doable for single elements, but it gets more difficult if multiple elements are involved.

2. The state of more than one entity needs to be changed in a consistent, transactional manner. In this case you would use an unbound action.

3. If there is the need to control authorization for certain state change, this is an indicator to introduce a dedicated action. Actions also give you means to control authorization, as they can be annotated with *@requires*, like in this example:

```
@requires: 'Publisher' action publish();
```

If you are working with domain-driven design (DDD) there is a straight-forward translation: each command in your model that is different from create, update and delete is a ...