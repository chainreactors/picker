---
title: Embedded Steampunk – What’s under the hood? Part III
url: https://blogs.sap.com/2023/02/11/embedded-steampunk-whats-under-the-hood-part-iii/
source: SAP Blogs
date: 2023-02-12
fetch_date: 2025-10-04T06:25:42.625419
---

# Embedded Steampunk – What’s under the hood? Part III

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Embedded Steampunk – What’s under the hood? Part I...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161359&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Embedded Steampunk – What’s under the hood? Part III](/t5/technology-blog-posts-by-members/embedded-steampunk-what-s-under-the-hood-part-iii/ba-p/13557867)

![amangarg1](https://avatars.profile.sap.com/8/f/id8f6af096c82ae9d45cd6649babc0a7426fef5f4175b47a3bcae1ed9b04aac701_small.jpeg "amangarg1")

[amangarg1](https://community.sap.com/t5/user/viewprofilepage/user-id/14709)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161359)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161359)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557867)

‎2023 Feb 11
5:40 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161359/tab/all-users "Click here to see who gave kudos to this post.")

4,441

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP NetWeaver Application Server for ABAP for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server%2520for%2520ABAP%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/67838200100800006918)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP NetWeaver Application Server for ABAP for SAP S/4HANA Cloud

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer%2Bfor%2BABAP%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/67838200100800006918)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (6)

Welcome to Part III of blog post series Embedded Steampunk – What’s under the hood?

1. [How to use Embedded Steampunk in S/4 HANA 2022 on premise system,](https://blogs.sap.com/2023/01/14/embedded-steampunk-whats-under-the-hood-part-i/)

2. [RAP as the programming model of choice in Embedded Steampunk](https://blogs.sap.com/?p=1682482&preview=true&preview_id=1682482),

3. [Restricted ABAP in Embedded Steampunk with tried out examples](https://blogs.sap.com/2023/01/30/embedded-steampu%E2%80%A6he-hood-part-iii/) (current topic),

4. ADT tips which might be useful.

###### *Hyperlinks to topic #4 will be updated here once it is published*

---

***NOTE: The term Embedded Steampunk is now replaced with “The SAP S/4HANA Cloud ABAP Environment”, as suggested in this [blog](https://blogs.sap.com/2022/09/01/evolution-of-abap/)***

---

In part I, we observed how ABAP turns into Restricted ABAP as soon as we switch ABAP Language version from *Standard ABAP* to *ABAP for Cloud Development*. Let's try to discover more about Restricted ABAP by having a look at few tried out examples. We will also see how error texts point to successor object name, hence making a developer's life easier ![:winking_face:](/html/@A88DCF6C8F85E444D0A74266620F2583/emoticons/1f609.png ":winking_face:")

## Restricted ABAP in Embedded Steampunk with tried out examples:

### Direct (or even indirect) use of tables not permitted in repository objects

![](/legacyfs/online/storage/blog_attachments/2023/01/1-69.png)

Direct use of table not allowed in class/FMs

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/01/2-45.png)

Error

---

### Use of table not allowed in USING parameter in AMDP methods

![](/legacyfs/online/storage/blog_attachments/2023/01/3-33.png)

Table not allowed in USING clause of AMDP

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/01/4-27.png)

Error

---

### Direct use of table(as a data source) not permitted in ABAP for Cloud CDS

![](/legacyfs/online/storage/blog_attachments/2023/02/15-1.png)

Direct use of table not allowed in ABAP cloud CDS

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/02/16-2.png)

Error Details

---

### Direct use of table(as an association) not permitted in ABAP for Cloud CDS

![](/legacyfs/online/storage/blog_attachments/2023/01/5-26.png)

use of table as association not allowed

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/01/6-23.png)

Error

---

### Direct use of table not permitted in RAP Behavior Definition

![](/legacyfs/online/storage/blog_attachments/2023/01/7-21.png)

use of table not allowed in RAP BDEF

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/01/8-20.png)

Error

Wondering how to specify draft tables or how to specify persistent tables while building RAP based services or APIs on ABAP Cloud?

Nothing to worry, we have RAP BO Interfaces available now in S/4 HANA 2022 On Premise to serve this purpose ![:winking_face:](/html/@A88DCF6C8F85E444D0A74266620F2583/emoticons/1f609.png ":winking_face:")

Learn more about RAP BO Interfaces [here](https://help.sap.com/docs/btp/sap-abap-restful-application-programming-model/business-object-interface).

---

### Not allowed to release DB tables

![](/legacyfs/online/storage/blog_attachments/2023/01/9-12.png)

Not allowed to release tables

After seeing above restrictions, this makes sense ![:grinning_face_with_smiling_eyes:](/html/@0C88A64C095E3C2FA8EB9A5FADAD5068/emoticons/1f604.png ":grinning_face_with_smiling_eyes:")

---

### Use of unreleased APIs not permitted

![](/legacyfs/online/storage/blog_attachments/2023/02/10-3.png)

Unreleased Class not permitted

Unreleased Class:

![](/legacyfs/online/storage/blog_attachments/2023/02/11-4.png)

Unreleased Class

Error Details:

![](/legacyfs/online/storage/blog_attachments/2023/02/12-4.png)

Error Details

***Note: Error text points to the successor objects, that's the most beautiful part ![:slightly_smiling_face:](/html/@91D3E334D8D95BECA16E36EA295E2455/emoticons/1f642.png ":slightly...