---
title: What is Error 404? How to Fix & Troubleshoot 404’s On Your Site
url: https://buaq.net/go-173529.html
source: unSafe.sh - 不安全
date: 2023-08-03
fetch_date: 2025-10-04T12:00:29.267692
---

# What is Error 404? How to Fix & Troubleshoot 404’s On Your Site

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9d9dc7265fed1356c01fe02cf635d4da.jpg)

What is Error 404? How to Fix & Troubleshoot 404’s On Your Site

The notorious Error 404 Not Found stands firmly at the top of the list of most common website issues
*2023-8-2 23:55:0
Author: [blog.sucuri.net(查看原文)](/jump-173529.htm)
阅读量:38
收藏*

---

The notorious **Error 404 Not Found** stands firmly at the top of the list of most common website issues. Encountering this HTTP status code indicates that your requested page is nowhere to be found on the server.

A **404 Page Not Found** error most typically occurs when a page or resource can’t be tracked down — often the result of it being moved or deleted entirely from the server. However, 404’s can also happen due to a mistyped URL leading to a dead or broken link, or a page that has been relocated without a proper 301 redirect.

Furthermore, too many unexpected **404 errors** can sour the user experience for your visitors and increase bounce rates, potentially impacting your website’s rankings and traffic.

Despite the prevalence of this client-side issue, troubleshooting a 404 is often a quick and painless task. In this article, we’ll delve into the primary causes of 404’s and outline a number of ways to fix these pesky errors on your website.

**Contents:**

* [What is a 404 error?](#what-is-404-error)
* [How are 404 errors different from other client side errors?](#how-are-404s-different)
* [What are the most common causes of a 404 error?](#common-causes-404-error)
* [How do I fix a 404 Not Found error on my website?](#how-to-fix-404-error)
* [Can a 404 error be caused by malware?](#404s-malware)

## What is a 404 error?

The Internet Engineering Task Force defines error 404 as follows:

> The 404 (Not Found) status code indicates that the origin server did not find a current representation for the target resource or is not willing to disclose that one exists.
>
> **A 404 status code does not indicate whether this lack of representation is temporary or permanent; the 410 (Gone) status code is preferred over 404 if the origin server knows, presumably through some configurable means, that the condition is likely to be permanent.**

A 404 error is a client-side error that manifests when the server of a particular website fails to locate the requested page. This implies that the client (your browser) manages to connect with the host (the server of the website) successfully. However, the host is unable to locate the precise resource that was requested, such as a specific URL or filename.

![Example of a 404: Not Found error message. ](https://blog.sucuri.net/wp-content/uploads/2023/08/example-post-name.png)

### Examples of a 404 error:

As an illustration, if someone attempts to access **https://example.com/example-post-name** but there’s no content on the site with the slug **example-post-name**, a 404 error would be displayed in your browser. This is because although the web server is operating normally, it couldn’t locate the requested resource.

This error is not limited to posts or pages either. Any missing assets can trigger a 404 error on the server, including missing image files, JavaScript, CSS, and so forth.

404 error messages can appear in various formats, but they all mean the same thing. Here are a few variations of 404’s you might encounter in your browser:

* 404
* 404 Not Found
* 404 Error
* HTTP Error 404
* Temporary Error (404)
* We can’t find the page you’re looking for.
* The requested URL was not found on this server.
* The website cannot display the page – HTTP 404.
* Is currently unable to find this request. HTTP ERROR 404.

These are just a handful of the potential messages you might see when encountering a 404 error. In fact, many modern websites set up their own custom “404 not found” error pages to entertain and assist visitors.

Sometimes, 404 error pages are even visually indistinguishable from a normal home page, but their HTTP headers explicitly report the status: “**HTTP/1.1 404 Not Found**”

## How is error 404 different from other client side errors?

There are many types of client side error codes and they all mean different things.

To help you understand the difference between 404 errors and other types of 4xx errors, we’ve outlined some of the common types of client side responses you might encounter in your browser.

|  |  |
| --- | --- |
| **Client Error** | **Description** |
| 400: Bad Request | This error code means that the server couldn’t understand the request due to invalid syntax or request message framing, or deceptive request routing.. |
| 401: Unauthorized | This error indicates that the client lacks valid credentials and must authenticate itself to get the requested response. |
| 402: Payment Required | This status code is a non-standard response indicating that the client must make a payment to access the requested resource. |
| 403: Forbidden | This status code indicates that the server has received and understood the request but is unable to authorize it. |
| 404: Not found | This status code is one of the most common errors and simply means that the server can’t find the requested resource. |
| 405: Method Not Allowed | The server has recognized the method, but it has been disabled or cannot be used. |
| 406: Not Acceptable | The server cannot produce a response matching the list of acceptable values defined in the request’s headers. |
| 407: Proxy Authentication Required | This is similar to a 401 error, but it indicates that the client must authenticate itself with a proxy. |
| 408: Request Timeout | This error occurs when the server would like to shut down a non-responsive connection. |
| 409: Conflict | This means that the request could not be completed due to a conflict with the current state of the server. |
| 410: Gone | This status code is used to indicate that the requested resource is no longer available and will not be available again. |

Now that we’ve got a handle on the various types of client side errors, let’s take a look at some of the potential causes for a 404 error on your website.

## What are the most common causes of a 404 error?

A 404 error is a specific issue indicating that a requested resource on a website cannot be found. These can arise from various minor to severe issues.

Unlike 401 or [403 errors](https://blog.sucuri.net/2023/06/what-is-a-403-error-how-to-fix-it.html), a 404 error doesn’t typically provide a precise explanation of the problem (nor a direct solution).

Let’s examine some potential causes of a 404 on your site:

* The requested URL is incorrect or has been changed
* The requested web page or resource has been deleted from the server
* The resource exists, but your website’s configuration or file permissions have been altered and web server processes can’t locate it
* Broken or dead links within your website point to a web page that doesn’t exist
* The website’s sitemap is outdated and web crawlers are still trying to access non-existent URLs
* There was a change in your website’s domain name
* There are incorrect redirects or rewrites in the .htaccess file
* The requested web page or resource never existed in the first place

## How do I fix a 404 error on my website?

Here are a few ways to troubleshoot 404 errors to get your broken pages back up and running — and get rid of links pointing to non-existent pages.

### 1. Clear your browser cache

This is a good troubleshooting step. This confirms that the problem isn’t caused by cached data on your end.

Here’s how to clear your cache on Google Chrome.

1. Launch your Chrome browser.
2. Locate and click on the icon with the thre...