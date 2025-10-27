---
title: Week 6 — Learning Basic Concepts of Cybersecurity
url: https://infosecwriteups.com/week-6-learning-basic-concepts-of-cybersecurity-d2a27e136f24?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-29
fetch_date: 2025-10-06T23:51:37.494605
---

# Week 6 — Learning Basic Concepts of Cybersecurity

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd2a27e136f24&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweek-6-learning-basic-concepts-of-cybersecurity-d2a27e136f24&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweek-6-learning-basic-concepts-of-cybersecurity-d2a27e136f24&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d2a27e136f24---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d2a27e136f24---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Week 6 — *System Design Secrets: Building the Web’s Backbone*

[![Aang](https://miro.medium.com/v2/resize:fill:64:64/1*8OFSxi24TNgHQCLpC-bCGQ.jpeg)](https://iamaangx028.medium.com/?source=post_page---byline--d2a27e136f24---------------------------------------)

[Aang](https://iamaangx028.medium.com/?source=post_page---byline--d2a27e136f24---------------------------------------)

14 min read

·

Jul 27, 2025

--

Listen

Share

## Intro

Hi there! If you’re wondering who I am, I go by **@iamaangx028** on the internet — you can call me Aang :)

I am a student who is trying to get into the cybersecurity field. As a part of that journey, I would like to share my progress with all of you through weekly blogs.

***Just a small note for continuity…***

*So far, we have covered many important concepts related to the network, browser, and HTTP evolution in our previous blogs. Check out those previous blogs* [*here*](https://iamaangx028.medium.com/) *for better continuity. In this week’s blog, we will be understanding some of the important concepts of System Design. Let’s go!!*

Press enter or click to view image in full size

![]()

Let’s start the Week — 6

Before we dive into the Web application architecture, we need to understand the following concepts. We may not need to have in-depth knowledge of every component, but still, it is required to know the basic components of System Design and how they work.

Press enter or click to view image in full size

![]()

Top most important concepts in System Design

First, we need to understand the most important concepts of System design, and then how these are used to build modern web applications. Once we have a solid understanding of these concepts, we can then understand HTTP headers and further related topics.

I think we have a solid understanding of some concepts like Client-server Architecture, IP addresses, DNS, and HTTP/HTTPS. So, we need not cover them again here. Also, here we just cover the basic understanding, not in-depth knowledge. Please feel free to research a specific concept if you want. Let us start with the remaining concepts.

### **Proxy/ Reverse Proxy**

A proxy is a server that acts like a man-in-the-middle. Whenever you send a request, it first goes to the Proxy, and then the Proxy sends it to the server. These Proxies hide the Original requester’s IP address by giving their IP address to the receiver.

Whereas a Reverse proxy acts as a proxy to the server. So when a client sends the request to the server, it first reaches the reverse proxy, and then it forwards the request to the server based on the pre-defined rules. So there are two different types of Proxies: Forward Proxy and Reverse Proxy

**Forward Proxy:**

Press enter or click to view image in full size

![]()

Credits to [PowerCert](https://www.youtube.com/watch?v=RXXRguaHZs0)

So a forward proxy is there to protect the client. Also, a forward proxy can cache the pages that clients visit more often. A Forward proxy can be used for anonymity, as it can hide the requester’s IP. A Forward Proxy can log all of the requests made by the clients. So, if anything happens, engineers can analyze it. A Forward proxy can be used to bypass the restriction of the normal connection. Organizations often use these forward proxies, and employees need to connect to them.

**Reverse Proxy:**

Press enter or click to view image in full size

![]()

Credits to [PowerCert](https://www.youtube.com/watch?v=RXXRguaHZs0)

So, a Reverse proxy is there to protect the Server. A Reverse Proxy can be used as a Load Balancer too. It can serve the static files to the clients without needing to ask the servers. It can terminate the SSL and look into the request and understand what the client is requesting.

### **Latency**

Latency is the amount of delay between the request and the response. Say, for example, you send a request to a server that is in another country. Then the request has to travel to the server and come back to you with a response. So to do this round trip, it may take some time. Which is what we call Latency.

### **APIs**

Nowadays, web applications are doing more complex operations. The request & responses should be in a structured format, for the client and server to process them efficiently. So, that’s where we use APIs. API stands for Application Programming Interface. This API acts as a middleman between the client and the server. Now the client and server can use this API without needing to worry about the underlying implementation.

### **Rest APIs**

APIs are of two types, REST API and SOAP API. The main difference between the two is, REST API is stateless. Which means each request is independent of other requests. Given that, in REST API, we need to provide the session cookie or the Authorization Header in every request to prove our identity. REST API are the most used APIs. REST supports HTTP methods like GET, POST, DELETE, and PUT. And web applications can use these methods to perform different operations.

### **GraphQL**

GraphQL is another type of API. This is developed by the Facebook team. To overcome some of the limitations of the REST API, the Facebook team created this. In the REST API, sometimes, the response JSON contains more data than necessary. And REST API can do only one operation/function at a time. But GraphQL can overcome these limitations by specifying which fields should be reflected in the response. And can make multiple operations in a single call.

### **Databases**

Databases are used to store information. We cannot store so much data in memory. So, to store users' data, we use separate Database servers. Usually, all of the user data is stored in these databases. The server usually reads and writes the data into the database.

### **SQL vs NoSQL**

There are typically two types of Database servers, namely SQL and NoSQL. SQL databases are the traditional databases that store data in table formats. SQL databases have...