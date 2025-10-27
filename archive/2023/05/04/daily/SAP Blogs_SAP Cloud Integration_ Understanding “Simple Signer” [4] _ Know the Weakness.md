---
title: SAP Cloud Integration: Understanding “Simple Signer” [4] : Know the Weakness
url: https://blogs.sap.com/2023/05/03/sap-cloud-integration-understanding-simple-signer-4-know-the-weakness/
source: SAP Blogs
date: 2023-05-04
fetch_date: 2025-10-04T11:39:46.648892
---

# SAP Cloud Integration: Understanding “Simple Signer” [4] : Know the Weakness

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud Integration: Understanding “Simple Signe...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164029&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud Integration: Understanding “Simple Signer” [4] : Know the Weakness](/t5/technology-blog-posts-by-sap/sap-cloud-integration-understanding-simple-signer-4-know-the-weakness/ba-p/13568798)

![CarlosRoggan](https://avatars.profile.sap.com/1/a/id1a877e70b0b26812aab6fdc00c32b7299259da741950a6ac3a41385c571c8436_small.jpeg "CarlosRoggan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[CarlosRoggan](https://community.sap.com/t5/user/viewprofilepage/user-id/5495)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164029)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164029)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568798)

‎2023 May 03
7:10 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164029/tab/all-users "Click here to see who gave kudos to this post.")

1,411

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (6)

**SAP Cloud Integration** (CPI) provides functionality to automatically sign a message with a digital signature using the [*Simple Signer*](https://blogs.sap.com/2023/04/19/sap-cloud-integration-understanding-simple-signer/).
In the [previous](https://blogs.sap.com/2023/04/25/sap-cloud-integration-understanding-simple-signer-3-verify-signature-in-node.js-app) blog post we've learned how to verify such signature with Node.js in an HTTP receiver.
Today we're going to show the weakness of that scenario by simulating a hacker exploit.

Quicklinks:
[Sample Code](#appendix1)

## Content

[0.](#preparation) Prerequisites
[1.](#intro) Introduction
[2.](#hacker) Hacker Scenario
[2.1.](#node) Create Node.js App
[2.2.](#iflow) Create iFlow
[2.3.](#run) Run
[A](#appendix1)ppendix 1: Hacker Scenario Code

## 0. Prerequisites

* Today's tutorial builds upon the Node.js scenario created in the [previous blog post](https://blogs.sap.com/2023/04/25/sap-cloud-integration-understanding-simple-signer-3-verify-signature-in-node.js-app).
  So please follow that blog first to create the sample project and iFlow.

* The [Simple Signer Blog Post](https://blogs.sap.com/2023/04/19/sap-cloud-integration-understanding-simple-signer/) explains the basics about digital signatures and how to create them in CPI.

* One previous blog post showed how to verify a signature with Groovy and it contains a [little recap about digital signatures](https://blogs.sap.com/2023/04/20/sap-cloud-integration-understanding-simple-signer-2-verify-with-groovy-script/#intro).

* For remaining open questions I recommend the [Security Glossary](https://blogs.sap.com/2022/11/04/sap-btp-security-glossary/).

* To follow this tutorial, access to a Cloud Integration tenant is required, as well as basic knowledge about creating iFlows.

* You should be familiar with Node.js, even though the tutorial can be followed without local Node.js [installation](https://nodejs.org).

## 1. Introduction

Starting from [previous](https://blogs.sap.com/2023/04/25/sap-cloud-integration-understanding-simple-signer-3-verify-signature-in-node.js-app) tutorial, we created a scenario as follows:
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Create message with some important content.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Create digital signature with *Simple Signer*, it stores the signature in a header.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Create a header with algorithm info.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") In Groovy script, fetch corresponding public key and store it in a header.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Send the message via HTTP adapter to REST endpoint.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Create Node.js server app exposing an endpoint that receives the message.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Read headers to extract public key, algorithm info and signature.
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") Verify the digital signature in Node.js code.

As we’ve learned, the digital signature covers the following security aspects:
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") The integrity of the message content is guaranteed via hash
- > modifying the content would result in different hash value
![:small_blue_diamond:](/html/@6F9A18D4E429DF7C534F75A67831F93C/emoticons/1f539.png ":small_blue_diamond:") The authenticity of the signature is ensured via encrypting the hash with private key
-> modifying the hash + encrypting with new private key results in failing decryption

Looks nice, comfortable and easy to maintain in case of changing keys.

However, in the previous blog post we already stated that it was a bad idea…
This gives us the opportunity to showcase today why it was a bad idea.
The next blog post will show how it can be improved...