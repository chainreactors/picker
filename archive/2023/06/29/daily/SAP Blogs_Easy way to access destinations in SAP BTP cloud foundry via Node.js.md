---
title: Easy way to access destinations in SAP BTP cloud foundry via Node.js
url: https://blogs.sap.com/2023/06/28/easy-way-to-access-destinations-in-sap-btp-cloud-foundry-via-node.js/
source: SAP Blogs
date: 2023-06-29
fetch_date: 2025-10-04T11:47:46.255646
---

# Easy way to access destinations in SAP BTP cloud foundry via Node.js

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Easy way to access destinations in SAP BTP cloud f...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159704&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Easy way to access destinations in SAP BTP cloud foundry via Node.js](/t5/technology-blog-posts-by-members/easy-way-to-access-destinations-in-sap-btp-cloud-foundry-via-node-js/ba-p/13547880)

![kallolathome](https://avatars.profile.sap.com/8/d/id8dd1f1faeeb17582fb46ef15990b58394c58a7ec855824cb21f8cc8a8a158479_small.jpeg "kallolathome")

[kallolathome](https://community.sap.com/t5/user/viewprofilepage/user-id/14879)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159704)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159704)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13547880)

‎2023 Jun 28
7:34 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159704/tab/all-users "Click here to see who gave kudos to this post.")

10,143

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Connectivity service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Connectivity%2520service/pd-p/67837800100800004901)
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

* [SAP Connectivity service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BConnectivity%2Bservice/pd-p/67837800100800004901)
* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (6)

## Introduction

I've checked blog-posts for accessing the destinations having authentication **OAuth2ClientCredentials** in Cloud Foundry via **Node.js** . But I didn't find any code working properly.

Then I came across iobert's blog post about [Using the Destination service in SAP BTP, Cloud Foundry Environment](https://blogs.sap.com/2018/10/08/using-the-destination-service-in-the-cloud-foundry-environment/). The blog-post is really very nice and helpful. But there was one problem. The library: [request](https://www.npmjs.com/package/request) used is deprecated.

So, thought of rewriting the code using the [axios](https://www.npmjs.com/package/axios) library. The sample code snippet is provided below for reference.

**Pre-requisites:**  Please bind your application with the instances of **Destination Service** & **Authorization and Trust Management Service** respectively.

## Solution

```
// imports

const express = require("express");

const cfenv = require('cfenv');

const axios = require("axios");

const app = express();

const PORT = process.env.PORT || 4000;

const getProjectDef = async (req, res) => {

    const MAX_ROWS = "1000";

    // Get the UAA and destination services

    const UAA_SERVICE = cfenv.getAppEnv().getService('UAA_INSTANCE_NAME');

    const DESTINATION_SERVICE = cfenv.getAppEnv().getService('DESTINATION_SERVICE_NAME');

    // Combine the client ID and secret for the UAA service into a single string

    const UAA_CREDENTIALS = DESTINATION_SERVICE.credentials.clientid + ':' + DESTINATION_SERVICE.credentials.clientsecret;

    // Set the name of the destination to retrieve and the endpoint to call

    const DESTINATION_NAME = 'DESTINATION_NAME';

    const END_POINT = 'END_POINT_URL';

    // Set the payload for the POST request to the UAA to get a token

    const post_payload = {

        'client_id': DESTINATION_SERVICE.credentials.clientid,

        'grant_type': 'client_credentials'

    };

    // Set the configuration options for the POST request to the UAA

    const post_config = {

        method: 'POST',

        url: UAA_SERVICE.credentials.url + '/oauth/token',

        headers: {

            'Authorization': 'Basic ' + Buffer.from(UAA_CREDENTIALS).toString('base64'), // Encode the client ID and secret as base64

            'Content-type': 'application/x-www-form-urlencoded'

        },

        data: new URLSearchParams(post_payload).toString() // Encode the payload as x-www-form-urlencoded

    };

    // Make the POST request to the UAA to get a token

    axios(post_config)

        .then((response) => {

            if (response.status === 200) {

                const token = response.data.access_token; // Get the token from the response data

                // Set the configuration options for the GET request to the destination service

                const get_config = {

                    method: 'GET',

                    url: DESTINATION_SERVICE.credentials.uri + '/destination-configuration/v1/destinations/' + DESTINATION_NAME,

                    headers: {

                        'Authorization': 'Bearer ' + token // Include the token in the authorization header of the GET request

                    }

                };

                // Make the GET request to the destination service to retrieve the destination configuration

                axios(get_config)

                    .then((response) => {

                        const DESTINATION = response.data; // Get the destination configuration from the response data

                        // Get the auth token from the destination configuration

                        const token = DESTINATION.authTokens[0];

                        // Set the configuration options for the POST request to the endpoint of the destination service

                        // a CPI is built over the BAPI: BAPI_PROJECTDEF_GETLIST with OAuth2ClientCredentials authentication

                        const options = {

                            method: 'POST',

                            url: DESTINATION.destinationConfiguration.URL + END_POINT,

                            headers: {

                                'Authorization': `${token.type} ${token.value}` // Include the auth token in the authorization header of the GET request

                            },

            ...