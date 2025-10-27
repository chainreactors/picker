---
title: Embedded Steampunk – What’s under the hood? Part II
url: https://blogs.sap.com/2023/01/21/embedded-steampunk-whats-under-the-hood-part-ii/
source: SAP Blogs
date: 2023-01-22
fetch_date: 2025-10-04T04:33:19.858578
---

# Embedded Steampunk – What’s under the hood? Part II

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Embedded Steampunk – What’s under the hood? Part I...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163465&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Embedded Steampunk – What’s under the hood? Part II](/t5/technology-blog-posts-by-members/embedded-steampunk-what-s-under-the-hood-part-ii/ba-p/13570047)

![amangarg1](https://avatars.profile.sap.com/8/f/id8f6af096c82ae9d45cd6649babc0a7426fef5f4175b47a3bcae1ed9b04aac701_small.jpeg "amangarg1")

[amangarg1](https://community.sap.com/t5/user/viewprofilepage/user-id/14709)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163465)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163465)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570047)

‎2023 Jan 21
10:13 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163465/tab/all-users "Click here to see who gave kudos to this post.")

6,076

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (5)

Welcome to Part II of blog post series Embedded Steampunk – What’s under the hood?

1. [How to use Embedded Steampunk in S/4 HANA 2022 on premise system,](https://blogs.sap.com/2023/01/14/embedded-steampunk-whats-under-the-hood-part-i/)

2. [RAP as the programming model of choice in Embedded Steampunk](https://blogs.sap.com/?p=1682482&preview=true&preview_id=1682482)(current topic),

3. [Restricted ABAP in Embedded Steampunk with tried out examples](https://blogs.sap.com/2023/02/11/embedded-steampunk-whats-under-the-hood-part-iii/),

4. ADT tips which might be useful.

###### *Hyperlinks to topics #3,4 will be updated here once they are published*

---

***Update: The term Embedded Steampunk is now replaced with “The SAP S/4HANA Cloud ABAP Environment”, as suggested in this [blog](https://blogs.sap.com/2022/09/01/evolution-of-abap/)***

---

In part I, we have seen how to use Embedded Steampunk in SAP S/4 HANA 2022 on premise.

Now let's see how Embedded Steampunk promotes ABAP RESTful Application Programming Model (RAP) as the programming model of choice to build Fiori App and services. We would also see how to generate RAP based services in a few clicks using Generate ABAP Repository Objects.

## RAP as the programming model of choice in Embedded Steampunk

Let's try to create OData services in different ways and see which way is supported in Embedded Steampunk.

### 1. Generate OData service using OData.publish Annotation

#### Exposing a CDS with ABAP Language version **Standard ABAP** as an OData service

![](/legacyfs/online/storage/blog_attachments/2023/01/1-39.png)

Exposing CDS with language version Standard ABAP

### Outcome: Exposed successfully

#### Exposing same CDS with ABAP Language version ABAP for Cloud Development as an OData service (Embedded Steampunk)

![](/legacyfs/online/storage/blog_attachments/2023/01/2-19.png)

Exposing CDS with language version ABAP Cloud

### Outcome: Exposure not allowed

**Error Details:**

![](/legacyfs/online/storage/blog_attachments/2023/01/3-13.png)

Error details

---

### 2. Generate OData service using ABAP Programming model for SAP Fiori

#### Exposing a CDS with ABAP Language version Standard ABAP using BOPF programming model

![](/legacyfs/online/storage/blog_attachments/2023/01/4-12.png)

Standard ABAP with ABAP Programming model for SAP Fiori

### Outcome: Exposed successfully

#### Exposing same CDS with ABAP Language version ABAP for Cloud Development using BOPF programming model (Embedded Steampunk)

![](/legacyfs/online/storage/blog_attachments/2023/01/5-14.png)

ABAP Cloud with ABAP Programming model for SAP Fiori

### Outcome: Exposure not allowed

**Error Details:**

![](/legacyfs/online/storage/blog_attachments/2023/01/6-12.png)

Error details

---

### 3. Generate OData service in SAP Gateway Service Builder(SEGW)

Generating OData service via SEGW is not possible because the standard interfaces used in generated MPC/DPC classes are not released, hence not permitted to be used in ABAP Cloud development.

![](/legacyfs/online/storage/blog_attachments/2023/01/SEGW.png)

SEGW based oData service

### Outcome: Exposure not allowed

---

### 4. Generate OData service using ABAP RESTful Application Programming Model(RAP)

Generating an OData service via RAP is usually quick, as it allows us to focus more on implementing business logic than worrying about the technical aspects. What's even quicker is generating a RAP based OData service with a few clicks through **Generate ABAP Repository Objects**
> Generate ABAP Repository Objects is now available with SAP S/4 HANA 2022 On Premise as well.

Let's see how to create RAP based service in a few clicks:

*Step 1:*

Right click on your database table on top of which you want to build the RAP Data model, and select Generate ABAP Repository Objects to open Generator wizard and select Generator ''ABAP RESTful Application Programming Model: UI Service''

![](/legacyfs/online/storage/blog_attachments/2023/01/7-10.png)

Generator wizard

*Step 2:*

Click next and enter data model, behavior, service definition, service binding names and select binding type

![](/legacyfs/online/storage/blog_attachments/2023/01/8-9.png)

Enter data model and service binding details

*Step 3:*

Click next to preview generator output before generating the repository objects

![](/legacyfs/online/storage/blog_attachments/2023/01/9-5.png)

Preview generator output

*Step 4:*

Select Transport Request and click Finish

![](/legacyfs/online/storage/blog_attachments/2023/0...