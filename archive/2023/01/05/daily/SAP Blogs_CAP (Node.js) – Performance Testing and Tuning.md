---
title: CAP (Node.js) – Performance Testing and Tuning
url: https://blogs.sap.com/2023/01/04/cap-node.js-performance-testing-and-tuning/
source: SAP Blogs
date: 2023-01-05
fetch_date: 2025-10-04T03:03:59.630163
---

# CAP (Node.js) – Performance Testing and Tuning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CAP (Node.js) - Performance Testing and Tuning

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162334&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CAP (Node.js) - Performance Testing and Tuning](/t5/technology-blog-posts-by-members/cap-node-js-performance-testing-and-tuning/ba-p/13563060)

![martinstenzig](https://avatars.profile.sap.com/d/5/idd53ea4eb4603b9104e696b9b59b69ad4a7c9aefcbdccd537f39ad5cddbc61391_small.jpeg "martinstenzig")

[martinstenzig](https://community.sap.com/t5/user/viewprofilepage/user-id/268)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162334)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162334)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563060)

‎2023 Jan 04
7:38 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162334/tab/all-users "Click here to see who gave kudos to this post.")

3,397

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (1)

## Background

It all started with a little project I was working on to synchronize thousands of records from SuccessFactors into a HANA database.

(Yes, I know there are more automatic ways than writing something yourself, but when you know SuccessFactors you know that no SF system API's look the same.)

The structure of my solution is as follows:

1. I have microservice #1 that merely exposes an ODATA API on top of my generic data model. The business layer does nothing but receive data from the POST request and write it to the database.

2. My second microservice #2 is a NodeJS application that reads the data from the SuccessFactors ODATA API and calls microservice #1 to write the data to the database.

But between the two services I want to optimize the performance and possibly have multiple instances of microservice #2 to transfer different entities at the same time.

## Options

1. **Sequential**
   The obvious option is to post my records sequentially to the target service. This is the most straight forward approach, but it is also the slowest.

2. **Parallel**
   The second option is to post my records in parallel. It's not a bad idea, but you quickly try to figure out how many parallel requests you can make before you start to get errors. Errors can materialize in the express stack, in the BTP as the BTP thinks you are executing a DoS attack or in the processing of the database requests as you might run out of connections in the connection pool.

3. **Batch**
   The third option I thought would be my solution was a batch request. I could take all my records and post them in one request. This would be the most efficient way to transfer data, but as the name indicates and the specification states, it will receive the information as a batch, but process them sequentially on the server.

4. **BatchParallel**
   A fourth option I never implemented might be a combination of option 2 and 3. You could optimize the batch size and number of parallel connections.

5. **Custom REST**
   The option that the CAP development team recommended is without a doubt the best option. You can add a generic REST endpoint to your service (micrososervice #1) that will receive the data itself and the name of the entity you want to write to. Then you call the services with the complete data set. The implementation will do an optimized, single insert into the database with optimal performance and the complete dataset.

## Preliminary Test Results

You can find the details [here](https://github.com/RizInno/cds-load-test/blob/main/doc/performance_results.md)
![](https://martin.stenzig.com/blogimages/cds-load/graph-local2btp.png)

![](https://martin.stenzig.com/blogimages/cds-load/graph-local2btp-zoomed.png)

## Observations

* [SAP CAP](https://cap.cloud.sap/docs/) is a great framework to provide easy ODATA access to your data model.

* For most of you out there that use CAP as a mere backend for UI apps, you might never have to worry about this.

* As expected, sequential single request processing is the slowest approach. The problem is amplified if you have to include network latency as a factor.

* Utilizing batch processing or parallel processing are good ways to improve performance, but require additional effort in tuning the connection pool. As our detailed test results show, the default connection pool settings are not optimal for high volume through put and lead to various errors (getaddrinfo ENOTFOUND, 502 - Bad Gateway, 503 - Service Unavailable).

* The custom REST endpoint approach is the fastest and most efficient approach, but requires additional effort to implement and maintain. In version 6.4 of CAP you must patch CAP to allow for larger request bodies. You can find details in the description of the [Reference Server.](https://github.com/RizInno/cds-load-refsrv) In this implementation I skipped over proper error handling.

## Test Environment

To test the performance of the different options I created a simple test environment.

1. A reference service that allows the simulation of a CAP service with a single entity data model.
   [https://github.com/RizInno/cds-load-refsrv](https://github.com/RizInno/cds-load-refsrv "https://github.com/RizInno/cds-load-refsrv")

2. A test app that can put some load on the reference service to simulate the load.
   [https://github.com/RizInno/cds-load-test](https://github.com/RizInno/cds-load-test "https://github.com/RizInno/cds-load-test")

![](https://martin.stenzig.com/blogimages/cds-load/cds-load-test.png)

## The boundaries

1. ECONNRESET on too many parallel requests When I increase my number of concurrent connections to >= 550 and iterations in approximately 5s cycles a few calls will execute successfully, but after a few iterations I will get an 'ECONNRESET' error when establishing the connnection to the server. There seems to be challenge on the express side when hitting 1000 parallel requests.

   See this StackOvervflow article for additional details: [https://stackoverflow.com/questions/53340878/econnreset-in-express-js-node-js-with-multiple-requests](https://stackoverflow.com/questions/53340878/econnreset-in-express-js-node-js-with-multiple-requests "https://stackoverflow.com/questions/53340878/econnreset-in-express-js-node-js-with-multiple-requests")

2. BTP DoS attack prevention When you have microservice #2 running locally and #1 deployed to the BTP then you will run into DoS attack prevention. The BTP will block requests from the same IP at about 900 requests. This usually materializes in a client side error: getaddrinfo ENOTFOUND

3. 503 - Service Unavailable - Service unavailable is usually an indication of the connection po...