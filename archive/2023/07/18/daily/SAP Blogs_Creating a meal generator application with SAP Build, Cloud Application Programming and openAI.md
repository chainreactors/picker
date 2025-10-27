---
title: Creating a meal generator application with SAP Build, Cloud Application Programming and openAI
url: https://blogs.sap.com/2023/07/17/creating-a-meal-generator-application-with-sap-build-cap-and-openai/
source: SAP Blogs
date: 2023-07-18
fetch_date: 2025-10-04T11:54:42.104441
---

# Creating a meal generator application with SAP Build, Cloud Application Programming and openAI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creating a meal generator application with SAP Bui...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161953&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating a meal generator application with SAP Build, Cloud Application Programming and openAI](/t5/technology-blog-posts-by-members/creating-a-meal-generator-application-with-sap-build-cloud-application/ba-p/13560570)

![former_member793421](https://avatars.profile.sap.com/former_member_small.jpeg "former_member793421")

[former\_member793421](https://community.sap.com/t5/user/viewprofilepage/user-id/793421)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161953)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161953)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560570)

‎2023 Jul 17
1:06 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161953/tab/all-users "Click here to see who gave kudos to this post.")

4,051

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (6)

# Scenario Overview

By integrating [SAP Business Technology Platform](https://www.sap.com/products/technology-platform.html) products with openAI GPT and Google APIs I have managed to create an application that generates meal suggestions based on a list of ingredients.

The idea behind this proof of concept is to give it the list of ingredients I have in my fridge and receive meal suggestions, because you are someone like me who cooks almost daily, sometimes you run of out ideas.

The ingredients are stored in a [SAP HANA](https://help.sap.com/docs/hana-cloud) dabase, which is exposed in a [CAP](https://cap.cloud.sap/docs/) application. I send prompts to the openAI API and based on the response I can dinamically generate an image sample, meal steps and also update the table in case I want to make that meal.

All the SAP products are being used on a trial environment, so if you do want to do anything similar to what I did make sure to read the [SAP Tutorials for Developers](https://developers.sap.com/tutorial-navigator.html)

## Solution Overview

The following picture gives an overview of the intended setup of the solution and the request flows in between:

![](/legacyfs/online/storage/blog_attachments/2023/07/MicrosoftTeams-image-3-1.png)

Solution Overview

The end user can use the [SAP Build](https://www.sap.com/products/technology-platform/low-code.html) mobile application, add/remove ingredients in the database and also generate meal samples.

![](/legacyfs/online/storage/blog_attachments/2023/07/1_Homescreen.png)

Application Home Screen

## Technical setup

### CAP Application

The application created in [SAP Business Application Studios](https://help.sap.com/docs/bas) and it consists of creating multiple services and functions which are being called from SAP Build.

![](/legacyfs/online/storage/blog_attachments/2023/07/3_Functions_b.png)

CAP Application Services

I have exposed three services :

/catalog/Foods - which can be called with any CRUD operation to access the list of ingredients.

/Fridge - which I used in order to do the logic for the openAI API Calls

/delete - used to delete all the rows in the table.

In the catalog-service.js we can find all the service functions, like for example the one I created for the openAI integration.

![](/legacyfs/online/storage/blog_attachments/2023/07/3_Functions.png)

Sample function from the server .js

For integration with SAP Build we also had to cope with the [CORS policies](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/2d7115b0e0aa4f78bfd9c06fdc1fe4f6/883074bbfe304f7c86e4b5088783a706.html) :

![](/legacyfs/online/storage/blog_attachments/2023/07/4_CORS.png)

CORS Policy script

### SAP HANA Database

I am using a trial [SAP HANA Database](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/df0b4d0a3927472b85aed51efbb33c94.html) instance on Cloud Foundry, and as a prerequisite for this I had to create SAP HANA Schemas & HDI Container + SAP HANA Cloud services.

The database is a simple one, without datalake, in which I created a table in order to store my ingredients.

![](/legacyfs/online/storage/blog_attachments/2023/07/5_HANADB.png)

SAP HANA Database

For testing locally, I used a sample csv in order to generate my hdbcalculationviews and tables.

For deployment to Cloud Foundry i used the MTA Module Template to generate my mtar file, and then with mbt build and cf deploy commands I was able to deploy it to Cloud Foundry.

### openAI Chat Completions API

I used the API in order to receive meal suggestions.

![](/legacyfs/online/storage/blog_attachments/2023/07/3_Functions-1.png)

API Call to openAI

The function selects all the rows from the table and creates a prompt of this format :
> ```
> const message = `I have in my fridge ${result}. I want you to suggest me a meal that I can make with these ingredients. I need you to reply ONLY WITH a JSON-format message with 4 nodes: MealPossible with values yes/no if there is any meal that you can suggest, SuggestedMeal where you put the suggested meal name and Quantities node that contains an array with necessary quantities(meal for one) in kg and the ingredient name. Forth node will be Steps which contains all the steps required to make the dish. If the MealPossible node value is no, do not send the other nodes.`;
> ```

I have requested a JSON format because it's helping me build the logic in the SAP Build applicati...