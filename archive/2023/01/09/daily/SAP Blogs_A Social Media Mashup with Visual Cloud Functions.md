---
title: A Social Media Mashup with Visual Cloud Functions
url: https://blogs.sap.com/2023/01/08/a-social-media-mashup-with-visual-cloud-functions/
source: SAP Blogs
date: 2023-01-09
fetch_date: 2025-10-04T03:21:30.720358
---

# A Social Media Mashup with Visual Cloud Functions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* A Social Media Mashup with Visual Cloud Functions ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161701&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [A Social Media Mashup with Visual Cloud Functions (Part I)](/t5/technology-blog-posts-by-sap/a-social-media-mashup-with-visual-cloud-functions-part-i/ba-p/13561507)

![Dan_Wroblewski](https://avatars.profile.sap.com/d/6/idd630780f059388c9e8e8fa9d85021d5fbf6d51e34b585117ee5e4425f1998531_small.jpeg "Dan_Wroblewski")

![Developer Advocate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Developer Advocate")
[Dan\_Wroblewski](https://community.sap.com/t5/user/viewprofilepage/user-id/72)

Developer Advocate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161701)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161701)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561507)

‎2023 Jan 08
2:10 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161701/tab/all-users "Click here to see who gave kudos to this post.")

2,239

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (2)

Last month, 9958e4b6df99431a84a41b015b639ac8 started our [Build Bros series](https://blogs.sap.com/tag/buildbros/) of SAP Build example apps with an [app](https://blogs.sap.com/2022/12/14/build-bros-handling-file-upload-via-http-request/) that uploads files and integrates with AWS.

|
 **Read part II**  <https://blogs.sap.com/2023/01/11/a-social-media-mashup-with-visual-cloud-functions-part-ii/>    **You want to create this yourself?**  <https://developers.sap.com/mission.sap-build-apps-social-media.html>    **Or do you want to simply import and run?**  See the "Sources" section below |
  |

Now it's my turn. Here's an example of using the new SAP Build Apps backend feature (aka, Visual Cloud Functions) to create a social media mashup with your SAP business data. Using the [Northwind OData service](https://services.odata.org/v4/northwind/northwind.svc/), I'll let users rate products and then have a chat around a specific product.

* On the products page, users will see a list of products with average ratings and number of ratings. They can click a product to go to its page.

* On a specific product's page, users can see the latest comments for that product, can rate the product, and can add a comment.

![](/legacyfs/online/storage/blog_attachments/2023/01/Page1.png)![](/legacyfs/online/storage/blog_attachments/2023/01/Page2.png)

Notice that the comments are sorted (showing latest first) and paginated on demand, so that just 3 are shown but if the user wants to see earlier ones they can click **More** and additional items are retrieved.

## What's interesting here

A few things I think are cool here:

* **Social Media mashup** – We have both business data in the app (from external API), and social data (from internal to the app).

* **Visual Cloud Functions** – The app uses the new Visual Cloud Functions, and there is a use case for a server-side function which massages and aggregates the data before bringing it to the front end.

* **Paging** – I implemented a mechanism to show only the latest comments, but the user can click **More** and then the next messages are retrieved.

* **Mashup components** – A lesser discussed feature of SAP Build Apps is the ability to create your own components. Here, I mashed up the *Large Image List Item* component with the *Star Rating* component, and created my own properties within the composite component.

##

## How I built the backend

In this blog, I'll describe the backend. In the next blog, I'll describe the front-end.

In the lobby, I clicked **Create → Build an Application → Application Backend**, and created a project called **Product Rating**

![](/legacyfs/online/storage/blog_attachments/2023/01/Backend.png)

In the **Entities** tab, I created 2 entities.

![](/legacyfs/online/storage/blog_attachments/2023/01/NewEntity.png)

The 2 entities are:

* **Rating** for tracking every time someone rated a product.

* **Comment** for tracking every comment added to a product.

![](/legacyfs/online/storage/blog_attachments/2023/01/Myentities.png)

Then in the **Functions** tab, I created a new function:

![](/legacyfs/online/storage/blog_attachments/2023/01/NewFunction.png)

I wanted to have the output something like the following JSON, showing for every product the average ratings and the number of ratings:

```
[{"productID":"4","avg":4,"count":1},

{"productID":"1","avg":2.888888888888889,"count":9},

{"productID":"2","avg":2,"count":1}]
```

So I needed to first get the data from the ratings entity. I clicked **+** and selected **Retrieve records**.

![](/legacyfs/online/storage/blog_attachments/2023/01/RetrieveRecords.png)

And then selected the Rating entity.

![](/legacyfs/online/storage/blog_attachments/2023/01/Rating.png)

This brings all the records, but now I have to create function to turn all those records into what I need. So on the right, we can define the output by clicking **Output Value**.

![](/legacyfs/online/storage/blog_attachments/2023/01/NewOutput.png)

I called my output value **Ratings** and then I clicked **Set Formula** to get the formula editor.

![](/legacyfs/online/storage/blog_attachments/2023/01/NewOutput2.png)

This was the formula I used:

```
GROUP(outputs["Rating / Records listed"].records, item.productId, {productID: key, avg: AVERAGE(PLUCK(items,"rating")), count: COUNT(items) } )
```

The formula does the following:

1. Groups all the records by product ID.

2. For each group/product ID, I create an object with the following fields:

   * product ID

   * the average of the ratings from all of the groups records

   * the count of the group's records.

###

### Deployment

Deployment is pretty easy, and there aren't a lot of choices. Just go to the **Deployments** tab, and if all goes well, click **Review and Deploy**. It will take a minute or so, and you will see a **blue** dot and *Progressing*, and when all is done it turns **green** and says *Healthy*.

![](/legacyfs/online/storage/blog_attachments/2023/01/Deployment.png)

If you make changes that could cause problems for the front-end, it will warn you, but you will still be able to deploy. Certain changes, like changing the data type of an already deployed field, are forbidden.

Once you've deployed the entities, you can go back to the **Entities** tab and add data to them. For this project I didn't need to add any data. If you need to, click **Browse Data → New Record**.

![](/legacyfs/online/storage/blog_attachments/2023/01/Browse1.png)
...