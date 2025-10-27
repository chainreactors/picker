---
title: #SAPCAP: Win Customer Trust using Data Privacy and Protection Services on BTP – Part 2
url: https://blogs.sap.com/2023/03/18/sapcap-win-customer-trust-using-data-privacy-and-protection-services-on-btp-part-2/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:30.285945
---

# #SAPCAP: Win Customer Trust using Data Privacy and Protection Services on BTP – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* #SAPCAP: Win Customer Trust using Data Privacy and...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162192&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [#SAPCAP: Win Customer Trust using Data Privacy and Protection Services on BTP - Part 2](/t5/technology-blog-posts-by-sap/sapcap-win-customer-trust-using-data-privacy-and-protection-services-on-btp/ba-p/13562912)

![Ajit_K_Panda](https://avatars.profile.sap.com/d/1/idd1af3570ab5bb3989d673b6d8c6f5694a20b5738460036d1f11cdae23d7c6864_small.jpeg "Ajit_K_Panda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ajit\_K\_Panda](https://community.sap.com/t5/user/viewprofilepage/user-id/16653)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162192)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162192)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562912)

‎2023 Mar 18
6:51 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162192/tab/all-users "Click here to see who gave kudos to this post.")

1,469

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

|
 **Blogs in this Series [#CAP #DPP]**    1. [Part 1 : DPP Terminologies and PDM Overview](https://blogs.sap.com/2023/03/18/sapcap-win-customer-trust-using-data-privacy-and-protection-services-on-btp-part-1/)  2. [Part 2 : Personal Data Annotations in CAP and Integration with PDM](https://blogs.sap.com/2023/03/18/sapcap-win-customer-trust-using-data-privacy-and-protection-services-on-btp-part-2/)  3. [Part 3 : Explore PDM Application features](https://blogs.sap.com/2023/03/18/sapcap-win-customer-trust-using-data-privacy-and-protection-services-on-btp-part-3/) |

### **Introduction:**

Having covered the theoretical foundations in previous blog of this series, let's examine the implementation of the CAP based application and the steps of integrating DPP services.

We will use a sample application ‘Game Shop’ which is used to order one or more Games for a customer. The sample application looks like as shown below. You can find the code of sample application for this blog here: [ [cap-dpp-example](https://github.com/SAP-samples/btp-cap-demo-usecases/tree/main/cap-dpp-example) ].

In Game Shop Sample, sandbox launchpad is used to provide an entry point for both Manage Customers application and Manage Orders application where Manage Customers application is used to manage/modify customer details and  Manage Orders application is used to manage/modify orders for a customer.

### **Managing Data Privacy with CAP Applications:**

CAP simplifies compliance with data privacy regulations for applications by automating repetitive tasks using annotated models. It assists you in meeting specific data privacy requirements through different SAP BTP services like Personal Data Manager by using annotations and configurations.

To use Personal Data Manager Service (PDM) on BTP, we need to provide an OData or Rest based service that serves personal data stored in our application. In addition, PDM requires certain annotations to interpret the service to extract and render personal data on ui. Annotations required for PDM can be part of service metadata document or can also be provided with a separate endpoint. You can find more information about required annotations for PDM are on following pages: [OData V2 Annotations](https://help.sap.com/docs/PERSONAL_DATA_MANAGER/620a3ea6aaf64610accdd05cca9e3de2/66570273d5ff492aad06ab76765275e4.html), [OData V4 Annotations](https://help.sap.com/docs/PERSONAL_DATA_MANAGER/620a3ea6aaf64610accdd05cca9e3de2/5a55fae1eb7c496c92c56071186d76b3.html)

In CAP, *‘@PersonalData’* annotations are used to suggest entities or elements/fields in your domain model which will have personal data.

* *Entity Level Annotations:* Entity-level annotations indicate which entities are relevant for data privacy

* *Key-Level Annotations:* Key-level annotations indicate the corresponding key information

* *Field-Level Annotations:* Field-level annotations tag which fields are relevant for data privacy in detail.

Now, Let’s add an OData service to the sample application which will provide the Data Subject’s (individuals) personal data used in the application and add entity/key/field level annotations required for PDM.

```
using {sap.cap.dpp as db} from '../db/schema';

service PdmService {

    entity Customers               as projection on db.Customers;

    entity CustomerPostalAddresses as

        select from db.Addresses {

            *,

            type.name as addressType                };

    entity CustomerEmailAddresses  as

        select from db.EmailAddresses {

            *,

            emailType.name as emailAddressType      };

    entity OrderItemView           as

        select from db.Orders {

            key items.ID         as Item_ID,

                ID               as Order_ID,

                orderNo          as Order_No,

                customer.ID      as Customer_ID,

                customer.email   as Customer_Email,

                items.game.title as Item_Game,

                items.quantity   as Item_Quantity,

                items.netprice   as Item_NetPrice   };

}
```

As shown above, ‘DppService’ OData service provides four entities i.e. Customers, Postal Address, Email Address and OrderItemView. OrderItemView is used to provide transactional information about the Data Subjects (Individuals)
> ***Annotations***

```
annotate service.Customers with @PersonalData: {

    DataSubjectRole: 'Customer',

    EntitySemantics: 'DataSubject'

};

annotate service.CustomerPostalAddresses with @PersonalData: {

    Dat...