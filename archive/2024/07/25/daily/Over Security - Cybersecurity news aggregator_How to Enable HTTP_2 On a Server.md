---
title: How to Enable HTTP/2 On a Server
url: https://blog.sucuri.net/2024/07/how-to-enable-http-2-on-a-server.html
source: Over Security - Cybersecurity news aggregator
date: 2024-07-25
fetch_date: 2025-10-06T17:44:34.711103
---

# How to Enable HTTP/2 On a Server

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Security Education](https://blog.sucuri.net/category/security-education)

# How to Enable HTTP/2 On a Server

[![](https://secure.gravatar.com/avatar/28c9f086a2ef4d4beae4637238919c78849f979bae5f3b369c9083b1ed0bffc7?s=60&d=mm&r=g)](https://blog.sucuri.net/author/klknight)

[Kyle Knight](https://blog.sucuri.net/author/klknight)

* July 24, 2024

![How to Enable HTTP/2 On a Server](https://blog.sucuri.net/wp-content/uploads/2024/07/Blog-Post-How-to-Enable-HTTP2-On-a-Server-820x385.png)

HTTP/2 is a game-changer in web protocol technology, offering significant improvements in speed, efficiency, and security over its predecessor, HTTP/1.1. With features like multiplexing, header compression, and server push, HTTP/2 can drastically reduce web page load times and enhance the overall user experience. Additionally, HTTP/2 is enabled by default for [Sucuri’s Web Application Firewall (WAF)](https://sucuri.net/website-firewall/), making it even easier to leverage these benefits right out of the box.

In this blog, we’ll demystify HTTP/2 and guide you through the process of enabling it on your server using common control panels like Plesk and cPanel. We’ll break down the steps, providing detailed instructions and important notes to ensure a smooth transition. Let’s get started!

## What is HTTP/2?

To understand better, it’s worth noting its origins. HTTP/2, a major revision of the HTTP network protocol, was officially approved in 2015. Based on Google’s SPDY protocol, it is designed to improve the speed, efficiency, and security of data transfer between a client and server.

If you can believe it, the original HTTP/1.1 was standardized all the way back in 1997! The web has come a long way since then, and HTTP/2 addresses many of the performance limitations of its predecessor.

## HTTP/2 vs. HTTP/1.1

Understanding the differences between HTTP/2 and HTTP/1.1 can highlight why the newer protocol is so beneficial.

### Connection management

* **HTTP/1.1:** Uses a single connection per request-response pair. This means that for each resource (like images, scripts, and stylesheets), a new connection must be established, leading to inefficiencies and increased latency.

* **HTTP/2:** Utilizes a single connection for multiple streams, allowing for multiple requests and responses to be sent simultaneously over one connection. This multiplexing reduces the overhead and latency associated with establishing multiple connections.

![Display list of http 2 connections in browser](https://blog.sucuri.net/wp-content/uploads/2024/07/http2-connection-management.png)

### Header compression

* **HTTP/1.1:** Headers are sent as plain text, which can become quite large and add significant overhead, especially with repeated requests.

* **HTTP/2:** Implements header compression using the HPACK algorithm, reducing the size of headers and thus the amount of data that needs to be transferred.

### Data format

* **HTTP/1.1:** Uses a text-based format, which is less efficient and more prone to errors during parsing.

* **HTTP/2:** Adopts a binary format, which is more efficient for both transmission and parsing, reducing the likelihood of errors.

### Server push

* **HTTP/1.1:** The server can only respond to requests made by the client, which means the client must always initiate requests for resources.

* **HTTP/2:** Introduces server push, allowing the server to send resources to the client proactively before they are requested, reducing load times for web pages by preloading critical resources.

## The need for HTTP/2

With the growing complexity of web applications and user expectations for instant access, the need for a more efficient protocol became apparent. HTTP/2 offers several enhancements over HTTP/1.1.

### Growing complexity of web content

Websites today are far more complex than they were in the late 1990s. Modern web pages often include numerous resources such as images, JavaScript files, CSS stylesheets, and more. Each of these resources requires a separate request, and with HTTP/1.1, this can lead to significant inefficiencies and delays.

### Performance bottlenecks

HTTP/1.1’s request-response model can quickly become a bottleneck, especially on mobile networks or in high-latency environments. The need for multiple connections and the overhead of large headers can slow down page loads, frustrating users and potentially driving them away.

### Enhanced security requirements

Security is a top priority for web users and developers alike. HTTP/2 requires the use of SSL/TLS, ensuring that data is encrypted during transmission. This not only enhances security but also helps build user trust.

### Improved user experience

In an era where milliseconds count, improving load times c...