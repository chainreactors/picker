---
title: Things to know when using SAP_CUST client copy profile
url: https://blogs.sap.com/2022/11/17/things-to-know-when-using-sap_cust-client-copy-profile/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:33.645759
---

# Things to know when using SAP_CUST client copy profile

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Things to know when using SAP\_CUST client copy pro...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163428&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Things to know when using SAP\_CUST client copy profile](/t5/technology-blog-posts-by-members/things-to-know-when-using-sap-cust-client-copy-profile/ba-p/13569857)

![gyang001](https://avatars.profile.sap.com/0/d/id0d861249135da4aaddede4e5eb6b0fa1042b2a49b1842ab7cc29d26947366529_small.jpeg "gyang001")

[gyang001](https://community.sap.com/t5/user/viewprofilepage/user-id/146031)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163428)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163428)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569857)

‎2022 Nov 17
6:01 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163428/tab/all-users "Click here to see who gave kudos to this post.")

16,893

* SAP Managed Tags
* [NW Client/Server Technology (CST)](https://community.sap.com/t5/c-khhcw49343/NW%2520Client%252FServer%2520Technology%2520%28CST%29/pd-p/344886954246398291691406520294131)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [NW Client/Server Technology (CST)

  Software Product Function](/t5/c-khhcw49343/NW%2BClient%25252FServer%2BTechnology%2B%252528CST%252529/pd-p/344886954246398291691406520294131)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (2)

* **The Purpose of Creating a Multi-clients S/4HANA System**

During large scale S/4HANA implementation projects for On-premise or Private Cloud versions, it is by far the common practice to establish multiple ‘working’ clients in each SAP systems of the 3 tiers (Dev, QA, Prod) or 4 tiers (Dev, QA, Preprod, Prod) landscape. This is to cover the many different system usages which are often parallel and intensive during the project execution, e.g. Mock Data Load, System Integration Test, Training, User Acceptance Test, Performance Test, Dress Rehearsal etc.

* **Client Copy and Client Copy Data Profiles**

The most efficient way to establish these clients is a Basis activity which is called ‘Client Copy’. It can either be done locally in one system or remotely across two different systems. This procedure helps to save the effort to rebuild the configuration (or technically the content in client specific configuration tables) within the newly created client by retaining configuration of the source client.

SAP has given a couple of ‘Client Copy Profiles’ which can be used by Basis consultant to specify the scope of data to be copied from the source client to the target client in a client copy execution. ![](/legacyfs/online/storage/blog_attachments/2022/11/New-Bitmap-Image.jpg)

Among these many options the mainstream ones are

SAP\_ALL: All client specific tables except change documents

SAP\_CUST: Customizing including users, roles and authorization

SAP\_USER: Users, roles and authorization only

* **The** **Demand of a Clean Client and Recommended Approach**

From a requirement perspective, it is very common for someone to request a ‘Clean’ client to be setup during the project execution: all configurations, settings and coding that has been built by Functional and Technical Consultants are retained in the client, but no master or transactional data is retained. So that a new data load, a new testing activity can be started on a clean baseline. From a technical perspective, this requirement can also be translated to a more straightforward way. Every (client specific) table that is supposed to be populated by transports imports should be retained in this new client, and everything else that is locally populated by some sort of manual steps in the client should not be retained in this new client.

It is a strong recommendation from me to always retain a ‘Reference’ client in each and every system including production. This client should be created as a blank client by ways of Basis installation/setup. This client should always be updated by all the transports moved across the landscape and strictly nothing more! No one should ever be given user access to this reference client to do anything. This client can thus be used at any time to create a ‘Clean’ client or clean down the data in an existing client by a client copy activity using ‘SAP\_ALL’ profile.

* **SAP****\_CUST Client Copy Profile and Its Side Effect**

In an unfortunate case, the ‘Reference’ client might not have been established from the beginning in a system, or a compromise had been made to populate the client with data for some purpose either due to system size restriction or project timeline restrictions. Under these circumstances when a request to establish a ‘Clean’ client comes it might be considered by some Basis consultant as a workable approach to copying from an existing ‘working’ client using ‘SAP\_CUST’ profile, hoping it will retain configuration but clean data. Yes this included myself. But you should be aware of these things that might surprise you:

* **Content that should have been retained but are not:**

- House banking customizing

The configuration is accessible via path: IMG->Financial Accounting->Bank Accounting->Bank Accounts->Define House Banks or FI12 tcode.

And it is absolutely transportable between systems. However the underlying tables (e.g. T012) are categorized as ‘A’ therefore will not be retained in a ‘SAP\_CUST’ client copy.

It is at the same time not a ‘current setting’ configuration means you have to open the client (SCC4) for this configuration to be amended by a banking function consultant.

- Event linkage activate status

Event linkage is widely used in business workflow to allow an event to trigger a workflow task. Tcode used to active event linkage is SWETYPV and it is transportable. However the underlying table SWFDEVENA is categorized as ‘A’ (for security reasons? According to note 2851092).

Update: seems from S/4 2020, the table has now become ‘C’ thus included in ‘SAP\_CUST’ profile.

- TVARVC
Entries in TVARVC table are defined in tcode STVARV, one of a convenient place to maintain global parameters to be used in ABAP code or batch job variant definition. It is a transportable configuration including both the parameters’ definition and the values. However, surprisingly it is also not retained in a ‘SAP\_CUST’ client copy.

![](/legacyfs/online/storage/blog_attachments/2022/11/New-Bitmap-Image-1.jpg)

- Fiori UI Adaptation

Since the launch of Fiori UI, user adaptation has been a widely welcomed feature. In reality, these adaptations are mostly done by IT consultants instead of end users because it is still too ‘technical’ for a user to take on this task. If some fields have been added to a standard Fiori UI in Dev, it can be transported across systems by Transport Requests, however be ready these fields won’t be there in ...