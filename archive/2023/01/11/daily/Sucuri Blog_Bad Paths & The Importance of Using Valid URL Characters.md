---
title: Bad Paths & The Importance of Using Valid URL Characters
url: https://blog.sucuri.net/2023/01/bad-paths-the-importance-of-using-valid-url-characters.html
source: Sucuri Blog
date: 2023-01-11
fetch_date: 2025-10-04T03:30:50.849697
---

# Bad Paths & The Importance of Using Valid URL Characters

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

# Bad Paths & The Importance of Using Valid URL Characters

[![](https://secure.gravatar.com/avatar/a4279e88699c65065bb98c4cdfe5a2b6d92871222bf48497bb57af68b2ef6019?s=60&d=mm&r=g)](https://blog.sucuri.net/author/marc2)

[Marc Kranat](https://blog.sucuri.net/author/marc2)

* January 10, 2023

![Bad Paths & The Importance of Using Valid URL Characters](https://blog.sucuri.net/wp-content/uploads/2023/01/BlogPost_Feature-Image_1490x700_Bad-Paths-820x386.png)

To ensure that your web files and pages are accessible to a wide range of users with various different devices and operating systems, it’s important to use valid URL characters. Unsafe characters are known to cause compatibility issues with various browser clients, web servers, and even lead to incompatibility issues with web application firewalls.

In this post I’ll be summarizing [OWASP best practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) and [rfc3986 documentation](https://www.rfc-editor.org/rfc/rfc3986) to describe what a bad path is, why you should use valid URL characters, and how to properly encode characters to avoid problems.

**Contents:**

* **[What is a valid URL?](#what-is-a-valid-url)**
* **[What’s the difference between URLs, URIs, and Paths?](#difference-between-urls-uris-paths)**
* **[Unsafe characters](#unsafe-characters-in-urls)**
* **[Reserved characters](#reserved-characters-in-urls)**
* [**Safe characters**](#safe-characters-in-urls)

## What is a valid URL?

A valid URL (Uniform Resource Locator) is a string of characters that specify the location of resources on the internet or private networks (intranets).

Let’s break the components of a URL down a bit more in detail:

* **Uniform** – as in a codified / standardized in RFC 3986 and its many related articles.
* **Resource** – as in any server resources and can be used by a network connected client which might be an HTML page, an image or any other file.
* **Location** – a location to this resource is provided, it is common for a URL to be called a URI, where the I stands for Identifier.

A valid URL may include the following components:

* A protocol, such as “http”, “https”, “ftp”, etc. These may also be expressed as 433 the [default port for HTTPS](https://blog.sucuri.net/2023/11/https-protocol-what-is-the-default-port-for-ssl-common-tcp-ports.html)
* A domain name or IP address, such as “myawsomesite.com” or “192.168.0.1”.
* An optional path, such as “/index.php” or “/myftpfolder/”.
* An optional query string, such as “?param=value
* An optional fragment, such as “#section1”

### Example of a valid URL:

```
https://myawesomesite.com/index.php?param1=value1
```

While not all components are required beyond a protocol and a domain name or IP address, this format must be followed.

## What’s the difference between URLs, URIs, and Paths?

There is quite a bit of confusion between the meaning of URLs, URIs, and Paths. So let’s take a brief moment to examine the differences between them.

### URL (Uniform Resource Locator)

A URL (Uniform Resource Locator) is a specific type of URI (Uniform Resource Identifier) that is used to identify the location of a resource on the internet. It specifies the protocol to be used to access the resource, as well as the address of the resource on the internet.

For example, “<https://sucuri.net/path/to/exampleresource>” is a URL.

### URI (Uniform Resource Identifier)

A URI (Uniform Resource Identifier) is a string of characters that identify a name or a resource on the internet. URIs can be broken down into two types: URLs and URNs (Uniform Resource Names). A URL is a specific type of URI that specifies the location of a resource on the internet, while a URN is a type of URI that identifies the resource by name, rather than by location.

Some examples of a URI might include:

* **“mailto:person@example.com”** – specifies an email address
* **“https://sucuri.net”** – specifies the location of a resource on the internet
* **“file://path/to/some/file”** – specifies the location of a file on your local computer

### Path

A **path** is a sequence of directories or folders that specifies the location of a file or resource on a computer or network. A path can be either absolute or relative. An absolute path is a complete path that starts from the root directory and specifies the exact location of the file or resource, while a relative path is a partial path that specifies the location of the file or resource relative to the current directory.

In summary:

* A URL is a specific type of URI that specifies the location of a re...