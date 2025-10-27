---
title: [Part – 1] Enrich CAP based Services with Behaviors using Annotations
url: https://blogs.sap.com/2023/01/28/part-1-enrich-cap-based-services-with-behaviors-using-annotations/
source: SAP Blogs
date: 2023-01-29
fetch_date: 2025-10-04T05:07:43.466956
---

# [Part – 1] Enrich CAP based Services with Behaviors using Annotations

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* [Part - 1] Enrich CAP based Services with Behavior...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159888&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [[Part - 1] Enrich CAP based Services with Behaviors using Annotations](/t5/technology-blog-posts-by-sap/part-1-enrich-cap-based-services-with-behaviors-using-annotations/ba-p/13556011)

![Ajit_K_Panda](https://avatars.profile.sap.com/d/1/idd1af3570ab5bb3989d673b6d8c6f5694a20b5738460036d1f11cdae23d7c6864_small.jpeg "Ajit_K_Panda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ajit\_K\_Panda](https://community.sap.com/t5/user/viewprofilepage/user-id/16653)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159888)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159888)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556011)

‎2023 Jan 28
3:55 PM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159888/tab/all-users "Click here to see who gave kudos to this post.")

6,800

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

#### **Introduction**

Cloud Application Programming Model (CAP) is a set of languages, libraries, and tools that are used to create robust services and applications for businesses on SAP Business Technology Platform (BTP). It leads developers down a "golden path" of tried-and-true best practices and a plethora of out-of-the-box solutions to recurring tasks.

A CAP application typically provides services defined in CDS models and served by NodeJS and JAVA runtimes. They represent a domain's behavioral aspects in terms of exposed entities, actions, and events.

In this blogpost, we will see how a CAP based service can be enriched with additional functional or business capabilities in addition to CRUD operations using diverse set of annotations.

#### **Overview of Annotations**

An annotation enriches a service definition with metadata and provides semantical information. Annotations are prefixed with @ and can be placed before a definition, after the defined name or at the end of a definition as shown below.

```
@before entity Foo @inner {
@before simpleElement @inner : String @after;
@before structElement @inner {/* elements */ }. }
```

Multiple annotations can be placed in each spot separated by whitespaces or enclosed in @(...) and separated by comma. It is also possible to add annotations in a separate file using annotate directive.

```
annotate Foo with @(readonly: true);
annotate Foo:simpleElement with @readonly;
```

All annotations are mapped to EDMX outputs i.e. OData metadata as a Term with either a primitive value, a record value, or collection values.

```
<Annotations Target="MyService.Customers">
   <Annotation Term="Common.Label" String="Customer"/>
   <Annotation Term="Common.ValueList">
      <Record Type="Common.ValueListType">
         <PropertyValue Property="Label" String="Customers"/>
         <PropertyValue Property="CollectionPath" String="Customers"/>
      </Record>
   </Annotation>
</Annotations>
```

You can find more information about this [here](https://cap.cloud.sap/docs/advanced/odata#annotations).

#### **Glossary of Annotations [part -1]**

##### ***Access Control Annotations***

> **⇒[ @readonly ]** :

It is used to protect against write or delete operations and can be used for both entities and elements of an entity.

```
annotate Customers with @readonly;
```

Here, Customers can only be read. Create, Update & Delete operations are prohibited. This adds following semantical information to service metadata:

```
<Annotations Target="Service.EntityContainer/Customers">
	<Annotation Term="Capabilities.DeleteRestrictions">
		<Record Type="Capabilities.DeleteRestrictionsType">
			<PropertyValue Property="Deletable" Bool="false"/>
		</Record>
	</Annotation>
	<Annotation Term="Capabilities.InsertRestrictions">
		<Record Type="Capabilities.InsertRestrictionsType">
			<PropertyValue Property="Insertable" Bool="false"/>
		</Record>
	</Annotation>
	<Annotation Term="Capabilities.UpdateRestrictions">
		<Record Type="Capabilities.UpdateRestrictionsType">
			<PropertyValue Property="Updatable" Bool="false"/>
		</Record>
	</Annotation>
</Annotations>
```

Hence @readonly is equals to *@Capabilities: {Insertable: false, Updatable: false, Deletable: false}*;

When a create/update/delete operation is made, an error will be returned as response with error code 405 – Method not allowed.

```
annotate Customers:creditCardNo  with @readonly;
```

It adds following details to the service metadata:

```
<Annotations Target="Service.Customers/creditCardNo">
	<Annotation Term="Core.Computed" Bool="true"/>
</Annotations>
```

If a CREATE or UPDATE operation provides value for such fields like creditCardNo, values are ***silently ignored***

> **⇒[ @insertonly ]** :

Simillar to @readonly, Only CREATE operation is allowed on entity which is annotated with @insertonly. @insertonly annotation can only be annotated with an entity. All other operations like READ, UPDATE, DELETE are prohibited.

```
annotate Customers with @readonly;
```

> **⇒[ @restrict / @requires ]** :

By default CAP based services do not have any access control. To protect your resources according to business requirements, annotations @restrict and @requires can be used. These annotations can be used to define authorizations by choosing proper heirarchy level.

For example, you can define restriction on service level which will apply to all entities in the service. It is also possible to define restrictions on an entity or an instance of an entity.

Authorization is a complex and large topic. Hence this is not covered in this blogpost. More information can be found on [this page](https://cap.cloud.sap/docs/guides/authorization#restrict-annotation).

#### ***Input Validation Annotations***

> **⇒[ @mandatory ]** :

Checks are made for nonempty input on elements designated with @mandatory. Trimmed empty string, null are considered empty input and not allowed. However, for an integer element, 0 is considered nonempty input and allowed.  If an empty input is pro...