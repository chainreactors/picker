---
title: [Part – 2] Enrich CAP based Services with Behaviors using Annotations
url: https://blogs.sap.com/2023/01/29/part-2-enrich-cap-based-services-with-behaviors-using-annotations/
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:16.003632
---

# [Part – 2] Enrich CAP based Services with Behaviors using Annotations

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* [Part – 2] Enrich CAP based Services with Behavior...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160067&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [[Part – 2] Enrich CAP based Services with Behaviors using Annotations](/t5/technology-blog-posts-by-sap/part-2-enrich-cap-based-services-with-behaviors-using-annotations/ba-p/13556413)

![Ajit_K_Panda](https://avatars.profile.sap.com/d/1/idd1af3570ab5bb3989d673b6d8c6f5694a20b5738460036d1f11cdae23d7c6864_small.jpeg "Ajit_K_Panda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ajit\_K\_Panda](https://community.sap.com/t5/user/viewprofilepage/user-id/16653)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160067)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160067)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556413)

‎2023 Jan 29
1:39 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160067/tab/all-users "Click here to see who gave kudos to this post.")

4,235

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

### **Introduction**

In my previous blog post [[Part – 1] Enrich CAP based Services with Behaviors using Annotations](https://blogs.sap.com/2023/01/28/part-1-enrich-cap-based-services-with-behaviors-using-annotations/), We explored how to enrich CAP based services with access control and input validation related behavioral capabilities using annotations.

In this blog post, We will see about Service/API Annotations, Persistence Annotations, OData Annotations to alter behavior of services.

### **Glossary of Annotations [part -2]**

#### ***Service / APIs Annotations***

> **⇒[ @cds.autoexpose ]** :

An entity annotated with [@CDS](/t5/user/viewprofilepage/user-id/1434188).autoexpose is automatically exposed in services if it is associated by other entities which are explicitly exposed in service. Let's look at a simple example.

***Example - 1***@cds.autoexpose entity Industries { key id : String(3); name : String(100); } entity Companies : cuid { name :String(100); info. :String(200); industry:Association to Industries;}
service Service @(path: '/browse'){ entity Companies as projection on Companies; }

|  |  |
| --- | --- |
| schema.cds | service.cds |
|  |

In above example, Companies is explicitly provided in Service. Also Companies is associated to Industries and Industries entity is annotated with [@CDS](/t5/user/viewprofilepage/user-id/1434188).autoexpose. Hence Industries is also added to the services. However only READ operation is allowed on Industries. If you want to make Industries write enabled as well, then it needs to be explicitly exposed in Service.

This is particularly helpful in case of Code Lists that is used in UI.

> **⇒[ @cds.api.ignore ]** :

This annotation is used to supress unwanted entity fields. Note that, It only supresses regular properties and does not supress navigation property.

From Example 1, if info is annotated with [@CDS](/t5/user/viewprofilepage/user-id/1434188).api.ignore then it is ommited from the service and if industry is annotated with [@CDS](/t5/user/viewprofilepage/user-id/1434188).api.ignore then industry\_id (foregin key) is omitted. However industry navigation property is still available in the service as shown below.

```
<EntityType Name="Companies">
   <Key>
      <PropertyRef Name="ID"/>
   </Key>
   <Property Name="ID" Type="Edm.Guid" Nullable="false"/>
   <Property Name="name" Type="Edm.String" MaxLength="100"/>
   <NavigationProperty Name="industry" Type="Service.Industries">
      <ReferentialConstraint Property="industry_id" ReferencedProperty="id"/>
   </NavigationProperty>
   <Property Name="industry_id" Type="Edm.String" MaxLength="3"/>
</EntityType>
```

> **⇒[ @cds.query.limit ]** :

READ operation on an entity provides 1000 entries at maximum. if more than 1000 entries are there, then it can be retrieved using $skiptoken. However this can be influenced using [@CDS](/t5/user/viewprofilepage/user-id/1434188).query.limit annotation. It has 2 properties: default and max.

***default***: defines the number of items that are provided if no $top was specified.
***max:*** defines the maximum number of items that are provided, regardless of $top

```
@cds.query.limit.default: 20
@cds.query.limit.max: 100
service Service @(path: '/browse'){
    entity Customers as projection on db.Customers;
    entity CustomerAddresses as projection on db.Addresses;

    @cds.query.limit: { default: 10, max: 200 }
    entity Companies as projection on db.Companies;
}
```

In above example, 20 entries are provided by default for read operations on Customers and CustomerAddresses, but only 10 entries are provided for Companies. The maximum number of entries that can be retrieved for Customers and CustomerAddressed is 100. However, 200 entries for Companies can be retrieved at once.

Note: The closest limit applies, that means, an entity-level limit overrides that of its service, and a service-level limit overrides the global setting.

> #### **⇒[ @odata.etag ]** :

CAP runtimes support optimistic concurrency control and caching techniques using ETags. An ETag identifies a specific version of a resource found at a URL. When updating, deleting, or invoking the action associated with an entity, you use the ETag value in an If-Match or If-None-Match header.

The value of an ETag element should uniquely change with each update per row. The modifiedAt element from the managed aspect is a good candidate.

```
annotate Service.Companies:modifiedAt with @odata.etag;
```

> Use *exclusive* locks when reading entity data with the *intention to update* it in the same transaction and you want to prevent the data to be read or updated in a concurrent transaction.
>
> Use *shared* locks if you only need to prevent the entity data to be updated in a concurrent transaction, but don’t want to block concurrent read operations.

For exclusive locks or shaed locks, it has to be handled with custom logic using *[.forUpdate()](https://cap.cloud.sap/docs/node.js/cds-ql#select-forUpdate)* and *[.forShareLock()](https://ca...