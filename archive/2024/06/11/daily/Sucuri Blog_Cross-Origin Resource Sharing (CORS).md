---
title: Cross-Origin Resource Sharing (CORS)
url: https://blog.sucuri.net/2024/06/cross-origin-resource-sharing.html
source: Sucuri Blog
date: 2024-06-11
fetch_date: 2025-10-06T16:55:21.075933
---

# Cross-Origin Resource Sharing (CORS)

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
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Cross-Origin Resource Sharing (CORS)

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* June 10, 2024

![What Is Cross-Origin Resource Sharing (CORS)?](https://blog.sucuri.net/wp-content/uploads/2022/11/BlogPost_Feature-Image_1490x700_How-to-Use-Cross-Origin-Resource-Sharing-CORS-Security-Headers-820x386.jpg)

Thanks to the rapid growth of JavaScript frameworks like Angular, React, and Vue, **Cross-Origin Resource Sharing (CORS)** has become a popular word in the developer’s vocabulary — and for good reason. It’s common practice for modern web applications to load resources from multiple domains. But accessing these website resources from different origins requires a thorough understanding of CORS.

In this post, we’ll take a look at what CORS is and why proper implementation is an important component of building secure websites and applications. We’ll also examine some common examples of how to use CORS, dive into preflight requests, and discuss how to protect your website against attacks.

**Contents:**

* **[What is Cross-Origin Resource Sharing?](#what-is-cors)**
* **[Why do I need CORS?](#why-cors)**
* **[How does CORS work?](#how-does-cors-work)**
* **[How do I enable CORS on my server?](#how-to-enable-cors-server)**
* **[How do I enable CORS on WordPress?](#how-to-enable-cors-wordpress)**
* **[Detecting and mitigating CORS-related vulnerabilities](#vulnerabilities)**
* **[Example: CORS Policy for an API endpoint](#example)**
* **[Website security with CORS](#website-security-cors)**

## What is Cross-Origin Resource Sharing?

CORS (Cross-Origin Resource Sharing) is a mechanism that gives permissions for resources to load from one origin to another while maintaining the integrity of the site and securing it from unauthorized access. This security measure is used by popular web browsers like Chrome and Mozilla Firefox to tell which cross-site requests are safe.

For security reasons, modern browsers restrict access from scripts to other resources that exist outside their domain using the **same-origin policy**. This policy was defined in response to malicious actions like stealing private data from other web servers or [cross-site request forgery (CSRF)](https://sucuri.net/guides/what-is-csrf/) attacks.

[![Cross-origin resource sharing browser response](https://blog.sucuri.net/wp-content/uploads/2022/11/22-sucuri-CORS-Security-Header-Blog-Image-1.png)](https://blog.sucuri.net/wp-content/uploads/2022/11/22-sucuri-CORS-Security-Header-Blog-Image-1.png)

Unfortunately, this **same-origin policy** turned out to be pretty restrictive for developers who want to fetch different resources from multiple origins. So to relax restrictions a bit, the CORS HTTP protocol was developed to tell browsers allow restricted resources on a web page to be requested from other domains.

For example, here’s a possible scenario for requesting information from an external source such as an API (a pretty common practice for client-side JavaScript code):

1. The resource origin makes a preflight request to the external web server using CORS headers.
2. The external web server then validates this preflight request to verify that scripts are allowed to make the request.
3. Once verified, the external web server responds with its own set of HTTP headers which define acceptable request methods, origins, and custom headers.

This final server response may also include information about whether it’s acceptable to pass along credentials such as authentication headers.

## Why do I need CORS?

If you want to use resources from another server apart from your own, you’re going to need to use CORS to accomplish this.

Some examples of what you can do with CORS include:

* Use web fonts or stylesheets like [Google Fonts](https://fonts.googleapis.com/) or [Typekit](https://fonts.adobe.com/typekit) from a remote domain
* Show user locations on a map by calling the Google Map API: ***https://maps.googleapis.com/maps/api/js***
* Display tweets from a Twitter handle by calling the Twitter API: ***https://api.twitter.com/xxx/tweets/xxxxx***
* Use a headless CMS for content
* Access any API hosted on a different domain or subdomain

As you can see, CORS is an important protocol for making cross-domain requests possible, in cases where there’s legitimate need.

## How does Cross-Origin Resource Sharing (CORS) work?
...