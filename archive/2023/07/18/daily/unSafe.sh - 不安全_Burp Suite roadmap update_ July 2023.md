---
title: Burp Suite roadmap update: July 2023
url: https://buaq.net/go-172255.html
source: unSafe.sh - 不安全
date: 2023-07-18
fetch_date: 2025-10-04T11:52:40.620842
---

# Burp Suite roadmap update: July 2023

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

![](https://8aqnet.cdn.bcebos.com/8c4ae571298ed85b48aff1604e96c1ce.jpg)

Burp Suite roadmap update: July 2023

Matt Atkinson |17 July 2023 at 14
*2023-7-17 22:26:13
Author: [portswigger.net(查看原文)](/jump-172255.htm)
阅读量:32
收藏*

---

Matt Atkinson |
17 July 2023 at 14:26 UTC

![Burp Suite July 2023 roadmap update](https://portswigger.net/cms/images/85/0c/509d-article-2023-road-map-article-update.png)

Check out our roadmap for [Burp Suite](https://portswigger.net/burp) and find out what exciting features are coming your way over the next 12 months.

## Burp Suite Professional

### Added to the roadmap

Added **BChecks - testing tool** - When creating custom [BChecks](https://portswigger.net/blog/bchecks-houston-we-have-a-solution) for [Burp Scanner](https://portswigger.net/burp/vulnerability-scanner), it's vital to test them thoroughly, to gain confidence that they're working correctly. We're going to make it just as easy to test your BChecks as it was to write them, by introducing a BCheck testing tool. You'll be able to send suitable requests to the tool, and use them as test cases to confirm that your BCheck is working.

Added **Code your own view filters** - Sometimes, Burp's built-in options for filters like the Proxy HTTP history filter don't do exactly what you need. You're limited by the checkboxes provided and the ways the settings are combined. We're going to give you a brand new way to customize Burp Suite using your own code, directly from the UI. You'll be able to quickly and easily create a view filter that does exactly what you need, showing just the items you are interested in.

Added **Burp Scanner auto configuration** - Currently, you have to manually configure Burp Scanner to ensure good performance when scanning certain types of web application. Failure to do this could mean missed attack surface. We will give Burp Scanner the ability to configure itself based on the type of web application you are scanning. This will improve crawl coverage, without the need for any manual configuration.

Added **Notes everywhere** - If you've used comments in Burp's tables to record information about HTTP messages, then you'll know that they can be a bit cramped and difficult to use. We're going to introduce a much-improved Notes feature - enabling you to write free-form multi-line notes, to capture everything you know about an HTTP message.

Added **Enhanced tables** - If you've ever used Burp Suite in anger, you'll know that it makes heavy use of tables to display key data. But these can be somewhat inflexible, with little scope for customization. We're going to change tables in Burp so that they work more consistently - and enhance them to give you more control. You'll be able to show and hide different columns, move them around, and you'll gain new capabilities for search and export.

Added **Service worker networking** - Burp Scanner's crawler doesn't properly support service workers and [WebSockets](https://portswigger.net/web-security/websockets) messages that occur during scans. This can cause some applications to function incorrectly - potentially leading to incomplete scan coverage. We will give Burp Scanner the ability to properly crawl service workers and WebSockets messages - eliminating this problem.

Added **[API scanning](https://portswigger.net/burp/vulnerability-scanner/api-security-testing) improvements** - Although Burp Scanner can understand many features of an OpenAPI definition and scan them appropriately, coverage isn't always as good as it could be. This is because scanning currently doesn't support some popular API features. We will add these features to Burp Scanner - enabling greatly improved coverage of web APIs.

Added **Browser performance enhancements** - Burp Scanner uses embedded browsers to navigate web sites effectively while scanning. But using a pool of browsers can consume significant system resources, which impairs performance. We will change Burp Scanner so that it uses fewer browser instances, each containing multiple isolated tabs, to enable parallel navigation. This will make scanning more efficient.

### Work in progress

WIP **Improved Burp Scanner interface** - It's not always easy to see the actions that Burp Scanner has carried out during a scan - or the attack surface it's discovered. [Burp Suite Professional](https://portswigger.net/burp/pro) 2023.5.2 brought you a new [crawl paths view](https://www.youtube.com/watch?v=Z8YWwWEyOmg&list=PLoX0sUafNGbGlLmZItn6zG2wRo5JOouiB&index=8) - which goes some way to addressing this problem. But more improvements to Burp Scanner's interface are currently in development, and in coming releases, you'll see some exciting new ways to visualize scan activity.

WIP **Customizable user interface** - Burp is a complex beast - and most testers have their own idiosyncratic way of working with it. This means that a fixed user interface will never be optimized for everyone. Especially once you start extending Burp Suite with BApps, you might find that real estate among your tabs is limited, to say the least. So work is underway to make Burp's user interface far more customizable. You'll finally be able to make it your own. And (because I know some of you will ask) - yes - if you want to hide Sequencer, you'll be able to hide Sequencer.

WIP **Start scan from uploaded API definition** - Work is progressing on giving Burp Scanner the ability to ingest an API definition you have given it, as part of its launch process. It will then use this API definition to seed its scan. This will bring you two main benefits when [scanning APIs](https://portswigger.net/burp/vulnerability-scanner/api-security-testing). Firstly, you will gain the ability to properly scan APIs that lack a hosted definition (as is often the case) - and secondly, you will be able to scan only a particular API - ignoring the rest of the application it's attached to.

WIP **[Access control](https://portswigger.net/web-security/access-control) scan checks** - When you provide Burp with a set of credentials or a [recorded login](https://portswigger.net/burp/vulnerability-scanner/authenticated-scanning) to authenticate with a site, it has a good understanding of what represents authenticated and unauthenticated content on that site. This puts it in a good position to understand [access control vulnerabilities](https://portswigger.net/web-security/access-control). We recognize the value of this area, and we are exploring the best ways to bring access control scan checks to Burp Scanner.

### Released

Released **BChecks** - The 2023.6.2 release introduced BChecks - a quick and easy way to extend Burp Scanner in Burp Suite Professional, using a simple text-based language. Now you can use Burp Scanner to scan for anything you want to look for.

Released **Additional Montoya API functionality** - Following the release of Burp's new Montoya API, we have introduced a number of new API features. Among other things, you can now work with WebSockets when building Burp extensions (BApps), and your BApps are now able to store and manage data in project files. While we will continue to add features to the Montoya API, it is already more powerful than Burp's old API ever was.

Released **Collaborator payloads in Intruder attacks** - Burp Suite Professional's 2023.3.2 release gave you the ability to dynamically generate Collaborator payloads in Intruder attacks. This enables you to automate out-of-band (OAST) attacks much more easily than was previously possible in Burp Suite.

Released **Burp Organizer** - The 2023.5.2 release introduced Burp Organizer - a brand new tool within Burp ...