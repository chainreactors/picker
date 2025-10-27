---
title: How to Set Cache Control Headers
url: https://blog.sucuri.net/2024/07/how-to-set-cache-control-headers.html
source: Over Security - Cybersecurity news aggregator
date: 2024-07-12
fetch_date: 2025-10-06T17:45:40.773655
---

# How to Set Cache Control Headers

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# How to Set Cache Control Headers

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* July 11, 2024

![Cache Control Headers](https://blog.sucuri.net/wp-content/uploads/2023/03/23-BlogPost_Feature-Image_1490x700_What-is-Headless-CMS-Security-Benefits-820x386.jpg)

When it comes to your website performance, every millisecond counts. Whether you’re managing a personal blog or a large-scale e-commerce site, the speed at which your pages load can profoundly impact everything from user experience to search engine rankings. This is where using HTTP headers, specifically cache control headers, can come in *really* handy.

HTTP headers are the core component of HTTP requests and responses. They carry important information about the client-browser request or the server response that precedes the actual content of the message. Among these, cache control headers play a key role in how web content is cached. They dictate whether, how, and for how long the data fetched by a browser should be stored in the cache. This not only speeds up access to frequently requested resources but also reduces bandwidth and hosting costs by minimizing the need for resources to be repeatedly sent across the network.

The **Cache-Control** header, introduced with HTTP/1.1, is particularly powerful for managing browser and intermediary caches. It allows web developers and server admins to specify directives that control cache dynamics, such as:

* How long a file should be stored before it is considered stale
* Whether a file should be stored at all

This is important for optimizing content delivery and ensuring that users receive the most current version of your website without any unnecessary delays.

In this post, we’ll explore the syntax of cache control directives, explain the various types, and discuss how they can be effectively implemented to enhance your website’s performance. These headers will help to ensure a faster, more efficient site that keeps your site visitors engaged (and most importantly — satisfied).

## What are cache control headers?

At its core, the **Cache-Control** HTTP header defines a set of directives sent from a web server that instructs the browser on how to handle caching for the website’s content. These directives are included in HTTP response headers and determine whether resources on a website can be stored in the browser’s cache and under what conditions.

## How cache control headers work

Cache control headers allow developers to dictate how, when, and even *if* caching occurs in a browser or any intermediary like the Sucuri CDN (Content Delivery Network). These headers provide specific directives that guide the caching process, helping ensure that users receive the best balance between load times and fresh content.

### Common cache control directives

Let’s take a look at the most common cache control directives.

##### max-age=[seconds]

Specifies the maximum amount of time a resource will be considered fresh. This is perhaps the most commonly used directive because it directly controls how long a file should be stored in cache before it’s considered stale and is the basic setting needed to make caching work on most devices.

##### s-maxage

The **s-maxage** setting tells shared caches, like those used by multiple visitors or devices (such as CDNs or web accelerators), how long they can keep a copy of a web page. It allows you to control how often these shared caches update their content compared to private caches.

##### stale-if-error

The **stale-if-error** setting allows a cached page to be served even after it has expired if the original web server returns an error. This helps keep your website available by showing an older version of the page instead of an error message. You need to set a private or shared cache duration to use this option, and it can be set for hours or days.

##### stale-while-revalidate

The **stale-while-revalidate** setting lets shared caches serve an old version of a web page while they update the cached copy in the background. This improves loading times because visitors don’t have to wait for the updated content. Like **stale-if-error**, it requires a private or shared cache duration, and can be used together with **stale-if-error**. This setting is useful for ensuring quick page loads while keeping content reasonably fresh.

##### Pagination

When this option is set, older pages will be cached for longer tha...