---
title: OCC (Open Content Connector) / SAP EHS Classic
url: https://blogs.sap.com/2022/10/23/occ-open-content-connector-sap-ehs-classic/
source: SAP Blogs
date: 2022-10-24
fetch_date: 2025-10-03T20:43:23.305273
---

# OCC (Open Content Connector) / SAP EHS Classic

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* OCC (Open Content Connector) / SAP EHS Classic

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1444&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [OCC (Open Content Connector) / SAP EHS Classic](/t5/product-lifecycle-management-blog-posts-by-members/occ-open-content-connector-sap-ehs-classic/ba-p/13555254)

![christoph_bergemann](https://avatars.profile.sap.com/5/e/id5e3a7f2ffc11dc9fba8f98dd7d1a14d1d00b4797e02d7e5ee19cde7d7811ec24_small.jpeg "christoph_bergemann")

[christoph\_bergemann](https://community.sap.com/t5/user/viewprofilepage/user-id/182445)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1444)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1444)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555254)

‎2022 Oct 23
5:22 PM

[1
Kudo](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1444/tab/all-users "Click here to see who gave kudos to this post.")

5,222

* SAP Managed Tags
* [SAP Environment, Health, and Safety Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Environment%252C%2520Health%252C%2520and%2520Safety%2520Management/pd-p/01200615320800000062)

* [SAP Environment, Health, and Safety Management

  SAP Environment, Health, and Safety Management](/t5/c-khhcw49343/SAP%2BEnvironment%25252C%2BHealth%25252C%2Band%2BSafety%2BManagement/pd-p/01200615320800000062)

View products (1)

# Introduction

The Blogs:

<https://blogs.sap.com/2019/07/23/data-handling-for-the-ehs-open-content-connector/>

and

<https://blogs.sap.com/2014/11/13/rule-sets-secondary-data-determination/>

and

<https://blogs.sap.com/2017/07/01/occ-load-options/>

seems not to help the EHS community

Questions regarding the use of OCC are asked quite often.

This Blog tries not to provide answers to the questions but to list threads with OCC questions of interest.

To use OCC as an option (in EHS Classic) the following need to be stated:

1. We have limited documentation in SAP IMG

2. We have limited documentation on SAP Marketplace

3. We have some quite good documents in place regarding how to prepare "Load File"

4. But limited documentation  how to do the "specific" set up

   1. E.g. how to enable the needed "RFC" connection

   2. How to install and use the software locally

   3. How to handle "Unicode" related issues

   4. etc

OCC is a good tool for doing regulator updated and if needed you can use it as well to do upload for e.g. "Density" or other data. But it is (like WWI) to a certain extent like: Start the work, crawl, walk and after some time you can run.

The "Load File option with EXCEL" is niece (but tricky to use (e.g. Unicode story etc.)

You should use the most up to date OCC software locally. You should check for SAP errors in this area as well from time to time (check SAP Marketplace for relevant OSS Notes)

# Technique

To use the OCC: we need a relevant "User Exit" to do so. Here you have the SAP IMG which tries to guide you. You start with the "hit list" in CG02 (Edit Mode) (Online Mode of use of OCC) and start the job. In most cases: you are on the "safe side" to use the "Online Mode". This mode has more options than the "offline mode".

BUT as you block/lock the specifications in CG02 in the "Edit" mode.. you should not do an upoad for to many specifications in one run and you should not try to load for "all properties" in one run.

It is more or less VERY tricky if there is a "load error"... so if your load file was not prepared correct sometimes you will get "useless" data. This is the "nightmare" in using the tool. There are not so many options in the place to "delete" then the useless data and to start again.

# Overview of questions

OCC seems now to have more interest as in the past. Here some links discussing the use of OCC. You will find much more like these questions. In many cases: The answers/discussion in the relevant threads will hel you to install and use the tool properly.

The questions can be grouped in:

* what is the difference of "online" to "offline" mode

* issues in getting SAP connected to OCC (RFC etc. etc.)

* Difference regarding "legal content" load and data load a such

* Topic of "examples" (EXCEL Template, step by step guidelines etc.)

* Difference "Data Editor" <=> OCC

* etc.

# SAP Marketplace

I have done a research in SAP Marketplace. We have many OSS Notes to consider for using SAP EHS OCC tool (October 2022). Please check SAP Marketplace if you have trouble with the OCC tool.

Using as a search term "EHS OCC" i can find roughly 130 threads discussing OCC. If you change your search: you find may be more.

# Use of OCC

OCC can be used to load "regulatory content" but as well data like "density" etc.

Depending on the starting postion: the use of OCC can be helpful if you need to support data migration topics.

The only "con" is this:

If you use the "EXCEL" template for doing the load (specification load): It is not easy to understand how to prepare the EXCEL file. This process can take a huge amount of time (e.g. select the correct phrase etc.) as the data model in EHS is such "big" (many properties etc.). Even is you focus on Safety Data Sheet like properties: This is a big work to support.

Therefore: in many cases it is a good idea to "spli" the story. E.g. create first the specifications as such and the do a "step by step" load of the objects using the OCC approach. May be start "simple". Properties like "Form", "State of matter", "Odor" are "simple" properties. Same liek "first Aid" proeprties etc.

Properties in the area of "tox", "Ecotox" are complex properties.

You should split as well your load between properties of type "composition/Spec. Listing". To do the load you have first to prepare the objects in the system

Data regarding "Dangerous Good" should be any how seperated from the load.

# Examples of threads

<https://answers.sap.com/questions/13475669/occ-configuration-ehs.html>

<https://answers.sap.com/questions/8925647/ehs-occ.html>

<https://answers.sap.com/questions/13712315/real-substance-status-occ-ehs.html>

<https://answers.sap.com/questions/11731011/registry-entry-not-found-occ-ehs.html>

<https://answers.sap.com/questions/66885/how-to-upload-xml-file-un-regulation-updates-in-sa.html>

<https://answers.sap.com/questions/13658726/sap-occ-ehs-risk-classification-dg-data.html>

<https://answers.sap.com/questions/6543969/ehs-data-upload-from-content-providers-through-ehs.html>

<https://answers.sap.com/questions/13737956/rfc-error-system-failure-ehs-occ-content-service-1.html>

<https://answers.sap.com/questions/13559498/ehs-occ-import-substance-nature.html>

<https://answers.sap.com/questions/64132/sap-ehs-occ-removing-nol.html>

<https://answers.sap.com/questions/8996734/sap-ehs-occ-question.html>

<https://answers.sap.com/questions/13666148/how-to-mark-a-checkbox-using-sap-occ-ehs.html>

<https://answers.sap.com/questions/13646281/sap-occ-ehss-dg-data.html>

<https://answers.sap.com/ques...