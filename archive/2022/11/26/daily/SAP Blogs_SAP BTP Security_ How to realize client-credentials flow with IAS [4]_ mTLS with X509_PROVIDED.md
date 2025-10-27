---
title: SAP BTP Security: How to realize client-credentials flow with IAS [4]: mTLS with X509_PROVIDED
url: https://blogs.sap.com/2022/11/25/sap-btp-security-how-to-realize-client-credentials-flow-with-ias-4-mtls-with-x509_provided/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:49:01.906539
---

# SAP BTP Security: How to realize client-credentials flow with IAS [4]: mTLS with X509_PROVIDED

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BTP Security: How to realize client-credential...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160589&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP Security: How to realize client-credentials flow with IAS [4]: mTLS with X509\_PROVIDED](/t5/technology-blog-posts-by-sap/sap-btp-security-how-to-realize-client-credentials-flow-with-ias-4-mtls/ba-p/13557956)

![CarlosRoggan](https://avatars.profile.sap.com/1/a/id1a877e70b0b26812aab6fdc00c32b7299259da741950a6ac3a41385c571c8436_small.jpeg "CarlosRoggan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[CarlosRoggan](https://community.sap.com/t5/user/viewprofilepage/user-id/5495)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160589)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160589)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557956)

‎2022 Nov 25
1:58 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160589/tab/all-users "Click here to see who gave kudos to this post.")

3,505

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (6)

This blog post shows how to get a client certificate in an easy way.
We do the required steps with respect to the certificate in understandable manual way.
The goal is to replace the X509\_GENERATED statement, which we used in previous tutorial.
The setup is a simple client-credentials scenario.

Used technologies:
SAP Business Technology Platform (SAP BTP), Cloud Foundry Environment,
SAP Cloud Identity Services – Identity Authentication (IAS),
Node.js.

Quicklinks:
[Quick Guide](#quickguide)
[Sample Code](#appendix1)

## Content

[0.](#intro) Introduction
[1.](#preparation) Preparation
[2.](#client_cert) Client Certificate
2.1. Generate Certificate
2.2. Adapt Certificate
[3.](#app) Sample Scenario
3.1. Identity Service
3.2. Backend Application
3.3. Frontend Application
3.4. Deploy
[4.](#run) Run
[Appendix](#appendix1): Sample Code

## 0.1. Introduction

In this hands-on tutorial, we're using the same setup and scenario like in previous tutorial, so please see [here](https://blogs.sap.com/2022/11/03/sap-btp-security-how-to-realize-client-credentials-flow-with-ias/#intro) for the description.
Just a few words to introduce the focus of the tutorial.

In the [previous tutorial](https://blogs.sap.com/2022/11/07/sap-btp-security-how-to-realize-client-credentials-flow-with-ias-2-mtls/) we learned how to use a **client certificate** to request a JWT token (instead of user/password, i.e. clientid/secret).
We didn’t care about **how** to obtain the certificate itself.
In our manifest, we used the binding parameter X509\_GENERATED which means that the identity service generates a certificate for us, on the fly, during binding.

However, this is not the recommended way, as it reveals the private key in the binding.
It is just faster for prototyping, as it doesn’t require any additional steps.
So it is typically used for quick sample apps, like the one in the previous tutorial.

Today, we’re going through the longer way.

In the manifest (or service-key), for binding parameters, there’s a different option: X509\_PROVIDED.
We’ve seen it already and always wondered what it means and how to use it...?

What it means:
In our manifest file, we specify this binding parameter for the identity service
(alternatively, it can be specified for service key or for manually binding command).
By using this option, we’re saying that WE are going to provide the certificate.
Means, we HAVE the client certificate.
As a consequence, this setting requires that we SEND it.
Means, that in this case a second setting becomes mandatory: the certificate parameter.
As value of this param, we specify our certificate itself.

That’s all about the X509\_PROVIDED.

Now we’re wondering: how to obtain a client certificate?
In this blog post we’re learning a very simple way.
It is not the recommended approach for professional enterprise development, but it is easy to follow and helps to learn the basics.

What we’re going to do:
Go to IAS to generate a certificate.
Convert the result to make it usable in our sample application.
Use the result in X509\_PROVIDED parameter instead of X509\_GENERATED.
Run the sample application (same as [before](https://blogs.sap.com/2022/11/03/sap-btp-security-how-to-realize-client-credentials-flow-with-ias/)) with that certificate.

Scenario:
For your convenience, a quick look at the scenario:

![](/legacyfs/online/storage/blog_attachments/2022/11/diagram1-1.jpg)

Out of scope:
Authorization handling. The backend application doesn’t require any scope/role for accessing the endpoint.

Disclaimer:
The procedure explained here is meant to show usage of certificates in a simple way.
Although better than using the “GENERATED” statement, it is still not the recommended way for enterprise applications.
Furthermore, this is not an official reference application, I’m just sharing my personal experiences.

## 0.2. Prerequisites

To follow this tutorial, we need

* Access to an IAS tenant with admin permission.

* Access to *SAP Business Technology Platform* (SAP BTP) and permission to create instances and to deploy applications.

* Basic [Node.js](https://nodejs.org/en/) skills.

* Some basic understanding of [OAuth](https://blogs.sap.com/2019/05/06/sap-cloud-platform-backend-...