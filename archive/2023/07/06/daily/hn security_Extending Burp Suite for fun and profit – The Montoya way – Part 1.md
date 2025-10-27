---
title: Extending Burp Suite for fun and profit – The Montoya way – Part 1
url: https://security.humanativaspa.it/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-1/
source: hn security
date: 2023-07-06
fetch_date: 2025-10-04T11:53:51.886347
---

# Extending Burp Suite for fun and profit – The Montoya way – Part 1

[![logo](https://hnsecurity.it/wp-content/uploads/2025/09/HN_Security_v2.svg)](https://hnsecurity.it/)

* [Home](https://hnsecurity.it)
* [Company](https://hnsecurity.it/company/)
* [Services](https://hnsecurity.it/services/)
  + [Red Teaming](https://hnsecurity.it/services/red-teaming/)
  + [DORA TLPT](https://hnsecurity.it/services/threat-led-penetration-test-dora/)
  + [AI Red Teaming](https://hnsecurity.it/services/ai-red-teaming/)
  + [Network Assessment](https://hnsecurity.it/services/network-assessment/)
  + [Web Assessment](https://hnsecurity.it/services/web-application-assessment/)
  + [Mobile Assessment](https://hnsecurity.it/services/mobile-application-assessment/)
  + [Mainframe Assessment](https://hnsecurity.it/services/mainframe-assessment/)
  + [Cloud Assessment](https://hnsecurity.it/services/cloud-assessment/)
  + [OT Assessment](https://hnsecurity.it/services/ot-assessment/)
  + [IoT Assessment](https://hnsecurity.it/services/iot-assessment/)
  + [Hardware Assessment](https://hnsecurity.it/services/hardware-assessment/)
  + [Security by Design](https://hnsecurity.it/services/security-by-design/)
* [Blog](https://hnsecurity.it/blog/)
* [Careers](https://hnsecurity.it/careers/)
* [Contacts](https://hnsecurity.it/contacts/)
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-1/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/BURP-uai-836x836.jpg)

# Extending Burp Suite for fun and profit – The Montoya way – Part 1

July 5, 2023|[![Federico Dotta](https://hnsecurity.it/wp-content/uploads/2025/09/Dotta-sm-150x150.jpg)](https://hnsecurity.it/blog/author/federico-dotta/)By [Federico Dotta](https://hnsecurity.it/blog/author/federico-dotta/)

[Articles](https://hnsecurity.it/blog/category/articles/ "View all posts in Articles"), [Tools](https://hnsecurity.it/blog/category/tools/ "View all posts in Tools")

1. **-> Setting up the environment + Hello World**
2. [Inspecting and tampering HTTP requests and responses](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-2/)
3. [Inspecting and tampering WebSocket messages](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-3/)
4. [Creating new tabs for processing HTTP requests and responses](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-4/)
5. [Adding new functionalities to the context menu (accessible by right-clicking)](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-5/)
6. [Adding new checks to Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-6/)
7. [Using the Collaborator in Burp Suite plugins](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-7/)
8. [BChecks – A quick way to extend Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-8/)
9. … and much more!

Hi there!

I have been thinking for a long time about releasing a course or lessons on **developing extensions** for [Burp Suite](https://portswigger.net/burp) (and to tell you the truth, I had already created a draft course with accompanying extensions some time ago), and what better opportunity than the release of a new API to start the project!

Burp Suite is an exceptional suite of tools that currently stands unparalleled in the world of web application penetration testing. In addition to the HTTP proxy, it provides fuzzing tools, an excellent automated scanner, a request repeater tool, and more. However, personally, the tool I find most remarkable since I started using Burp is undoubtedly the [Extender](https://portswigger.net/burp/extender).

The Extender offers a set of APIs that allow for convenient and effective extension of every tool offered by Burp Suite. It provides full control to the penetration tester over all outgoing requests and incoming responses, enabling enhanced customization and flexibility. Thanks to it, over time, **third-party plugins** have been developed that can support frameworks and protocols, handle complex situations, identify issues, integrate Burp Suite with external tools, and, more generally, make the life of a penetration tester easier by maximizing effectiveness and results.

Since I started doing this job, I have developed dozens (if not hundreds, I’m starting to feel old) of plugins. Some of the more structured ones have been published on GitHub, such as [Brida](https://github.com/federicodotta/Brida) or [Java Deserialization Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner). However, the majority of them were quickly created for a specific purpose during a specific task. Some examples include transparently managing encryption layers for HTTP requests in a mobile application, automatically modifying attack payloads sent to a web application to bypass a WAF, applying a signature to requests directed at an API, transparently handling protocols and encodings, and so on.

This post will be the first in a **series**, where we will explore how to develop plugins for Burp Suite that can assist us during everyday analyses, from the simplest ones to the most complex ones. We will explore in detail what the Burp Suite APIs offer and the types of plugins we can create, making an effort to navigate the documentation effectively (which, at first glance, can be a bit challenging for some aspects).

Let’s start with the first question. What can we do with Burp Suite’s Extender? Well, a lot of things. Some examples are:

* Inspect and/or edit all requests exiting from every tool in Burp Suite and all responses coming to them (even WebSocket messages from the release of the Montoya API!)
* Extend Burp Suite **GUI** with new contents, adding custom tabs, entries in the main menu and in the context menu, HTTP or WebSocket message editor tabs, and so on
* Add checks to the active and passive **Scanner** or even custom insertion points in which scanner payloads will be inserted (useful to handle data formats not known by Burp Suite or if we want to insert attack payloads in the middle of the value of a parameter)
* Create payloads for the **Intruder** or process each payload before it is inserted into the requests
* Control the requests processed by the **Proxy**, inspect them, modify them, and decide whether they should be intercepted or not
* Use the **Collaborator** in our plugins, generating URLs and monitoring the interactions
* View and modify sitemap, vulnerabilities, and scope
* And much more!

Well, second question. In which language can we write a plugin for Burp Suite? With the **old API** you could choose between **Java, Python** (using Jython, an implementation of Python in Java) **and Ruby** (using JRuby, an implementation of Ruby in Java). Unfortunately (?), **Java is the only choice with the new** **Montoya API**.

To be honest, in many situations, in my opinion, Java was still the best choice. Python could be a convenient choice for small extensions, but for more complex ones (especially those with a GUI), Java greatly simplified matters. Even if the plugin was written in Python, it had to interact with the Java objects provided by Burp and with the graphical components of Swing (because Burp Suite itself is coded in Java). I can assure you that, especially in the latter case, it was not an enjoyable experience. In addition, Jython does not currently support Python 3, which would require writing extensions with Python 2. I only mentioned Python because, honestly, I have never written (or seen) an extension written in Ruby. 🙂

So, since the following tutorials will focus on the new Montoya APIs, we will proceed using Java.

First, using a Java IDE is...