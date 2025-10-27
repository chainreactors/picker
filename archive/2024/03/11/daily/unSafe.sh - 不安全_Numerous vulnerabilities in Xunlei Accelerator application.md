---
title: Numerous vulnerabilities in Xunlei Accelerator application
url: https://buaq.net/go-227200.html
source: unSafe.sh - 不安全
date: 2024-03-11
fetch_date: 2025-10-04T12:08:16.731677
---

# Numerous vulnerabilities in Xunlei Accelerator application

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

![]()

Numerous vulnerabilities in Xunlei Accelerator application

Xunlei Accelerator (迅雷客户端) a.k.a. Xunlei Thunder by the China-based Xunlei Ltd. is
*2024-3-10 22:55:33
Author: [govuln.com(查看原文)](/jump-227200.htm)
阅读量:41
收藏*

---

Xunlei Accelerator (迅雷客户端) a.k.a. Xunlei Thunder by the China-based Xunlei Ltd. is a wildly popular application. According to the [company’s annual report](https://ir.xunlei.com/static-files/3100b981-4a23-460b-8342-a0446ffff2c4) 51.1 million active users were counted in December 2022. The company’s Google Chrome extension 迅雷下载支持, while not mandatory for using the application, had 28 million users at the time of writing.

![Screenshot of the application’s main window with Chinese text and two advertising blocks](https://govuln.com/2024/03/06/numerous-vulnerabilities-in-xunlei-accelerator-application/screenshot.png)

I’ve found this application to expose a massive attack surface. This attack surface is largely accessible to arbitrary websites that an application user happens to be visiting. Some of it can also be accessed from other computers in the same network or by attackers with the ability to intercept user’s network connections ([Man-in-the-Middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)).

It does not appear like security concerns were considered in the design of this application. Extensive internal interfaces were exposed without adequate protection. Some existing security mechanisms were disabled. The application also contains large amounts of third-party code which didn’t appear to receive any security updates whatsoever.

I’ve reported a number of vulnerabilities to Xunlei, most of which allowed remote code execution. Still, given the size of the attack surface it felt like I barely scratched the surface.

Last time Xunlei made security news, it was due to distributing a malicious software component. Back then [it was an inside job](https://news.softpedia.com/news/Company-Admits-Its-Employees-Bundled-Malware-with-Xunlei-Download-Manager-390840.shtml), some employees turned rouge. However, the application’s flaws allowed the same effect to be easily achieved from any website a user of the application happened to be visiting.

#### Contents

* [What is Xunlei Accelerator?](#what-is-xunlei-accelerator)
* [The built-in web browser](#the-built-in-web-browser)
  + [The trouble with custom Chromium-based browsers](#the-trouble-with-custom-chromium-based-browsers)
  + [Protections disabled](#protections-disabled)
  + [Censorship included](#censorship-included)
  + [Native API](#native-api)
  + [Getting into the Xunlei browser](#getting-into-the-xunlei-browser)
  + [The fixes](#the-fixes)
* [The main application](#the-main-application)
  + [Outdated Electron framework](#outdated-electron-framework)
  + [Cross-site scripting vulnerabilities](#cross-site-scripting-vulnerabilities)
  + [Impact of executing arbitrary code in the renderer process](#impact-of-executing-arbitrary-code-in-the-renderer-process)
  + [The (lack of) fixes](#the-lack-of-fixes)
* [The XLLite application](#the-xllite-application)
  + [Overview of the application](#overview-of-the-application)
  + [The “pan authentication”](#the-pan-authentication)
  + [Achieving code execution via plugin installation](#achieving-code-execution-via-plugin-installation)
  + [The fixes](#the-fixes-1)
* [Plugin management](#plugin-management)
  + [The oddities](#the-oddities)
  + [Example scenario: XLServicePlatform](#example-scenario-xlserviceplatform)
  + [The (lack of?) fixes](#the-lack-of-fixes-1)
* [Outdated components](#outdated-components)
* [Reporting the issues](#reporting-the-issues)

## What is Xunlei Accelerator?

Wikipedia lists Xunlei Limited’s main product as a Bittorrent client, and maybe a decade ago it really was. Today however it’s rather difficult to describe what this application does. Is it a download manager? A web browser? A cloud storage service? A multimedia client? A gaming platform? It appears to be all of these things and more.

It’s probably easier to think of Xunlei as an advertising platform. It’s an application with the goal of maximizing profits through displaying advertising and selling subscriptions. As such, it needs to keep the users on the platform for as long as possible. That’s why it tries to implement every piece of functionality the user might need, while not being particularly good at any of it of course.

So there is a classic download manager that will hijack downloads initiated in the browser, with the promise of speeding them up. There is also a rudimentary web browser (two distinctly different web browsers in fact) so that you don’t need to go back to your regular web browser. You can play whatever you are downloading in the built-in media player, and you can upload it to the built-in storage. And did I mention games? Yes, there are games as well, just to keep you occupied.

Altogether this is a collection of numerous applications, built with a wide variety of different technologies, often implementing competing mechanisms for the same goal, yet trying hard to keep the outward appearance of a single application.

## The built-in web browser

### The trouble with custom Chromium-based browsers

Companies love bringing out their own web browsers. The reason is not that their browser is any better than the other 812 browsers already on the market. It’s rather that web browsers can monetize your searches (and, if you are less lucky, also your browsing history) which is a very profitable business.

Obviously, profits from that custom-made browser are higher if the company puts as little effort into maintenance as possible. So they take the open source Chromium, slap their branding on it, maybe also a few half-hearted features, and they call it a day.

Trouble is: a browser has a massive attack surface which is exposed to arbitrary web pages (and ad networks) by definition. Companies like Mozilla or Google invest enormous resources into quickly plugging vulnerabilities and bringing out updates every six weeks. And that custom Chromium-based browser also needs updates every six weeks, or it will expose users to known (and often widely exploited) vulnerabilities.

Even merely keeping up with Chromium development is tough, which is why it almost never happens. In fact, when I looked at the unnamed web browser built into the Xunlei application (internal name: TBC), it was based on Chromium 83.0.4103.106. Being released in May 2020, this particular browser version was already three and a half years old at that point. For reference: Google fixed eight actively exploited zero-day vulnerabilities in Chromium in the year 2023 alone.

Among others, the browser turned out to be vulnerable to CVE-2021-38003. There is [this article](https://medium.com/numen-cyber-labs/from-leaking-thehole-to-chrome-renderer-rce-183dcb6f3078) which explains how this vulnerability allows JavaScript code on any website to gain read/write access to raw memory. I could reproduce this issue in the Xunlei browser.

### Protections disabled

It is hard to tell whether not having a pop-up blocker in this browser was a deliberate choice or merely a consequence of the browser being so basic. Either way, websites are free to open as many tabs as they like. Adding `--autoplay-policy=no-user-gesture-required` command line flag definitely happened intentionally however, turning off video autoplay protections.

It’s also notable that Xunlei revives Flash Player in their browser. Flash Player support has been disabled in all browsers in December 2020, for various reasons including security. Xunlei didn’t mer...