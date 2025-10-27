---
title: Stalking inside of your Chromium Browser
url: https://posts.specterops.io/stalking-inside-of-your-chromium-browser-757848b67949?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2022-12-02
fetch_date: 2025-10-04T00:19:39.842308
---

# Stalking inside of your Chromium Browser

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F757848b67949&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fstalking-inside-of-your-chromium-browser-757848b67949&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fstalking-inside-of-your-chromium-browser-757848b67949&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-757848b67949---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-757848b67949---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Stalking inside of your Chromium Browser

[![Kai Huang](https://miro.medium.com/v2/resize:fill:64:64/1*Fr0dG-na-EiIU0quMCN17g.jpeg)](https://medium.com/%40Kiwids0220?source=post_page---byline--757848b67949---------------------------------------)

[Kai Huang](https://medium.com/%40Kiwids0220?source=post_page---byline--757848b67949---------------------------------------)

7 min read

·

Dec 1, 2022

--

Listen

Share

## Revisiting Remote Debugging

Okay, you got your favorite agent running on the target machine. You did a process listing, but nothing interesting popped out. You searched through every possible thing, even the trash bins to find a clue of where exactly the user hid their secrets that could get you to the user’s Azure portal.

Well, Let’s revisit the process listing a little bit, do you see it? Is Chrome running with a bunch of child processes like this?

![]()

Google Chrome Processes

Look at that, the user is surfing the web with his/her favorite browser — Chrome!

As a red teamer, I immediately thought of leveraging the remote debugging feature which is a built-in feature for all Chromium based browsers. This feature allows developers to troubleshoot using [Chrome Remote Debugging Protocols (CDP)](https://chromedevtools.github.io/devtools-protocol/) while they are doing the heavy lifting. A copy-paste description for CDP below.

*The Chrome DevTools Protocol allows for tools to instrument, inspect, debug and profile Chromium, Chrome and other Blink-based browsers. Instrumentation is divided into a number of domains (DOM, Debugger, Network etc.). Each domain defines a number of commands it supports and events it generates. Both commands and events are serialized JSON objects of a fixed structure.*

As red teamers, we can certainly abuse this feature to dump session cookies using the documented methodology by Justin Bui’s [Hands in the Cookie Jar](/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e) and an awesome python script called [cookienapper.py](https://github.com/greycatsec/cookienapper) written by [Elliot Grey](https://medium.com/%40greycatsec). But, what if the cookies expired? We just grabbed some spoiled cookies and we certainly can’t use them anywhere. Well, It will be nice if we can be notified when they log into Azure and refresh their cookies?

To recap the technique used to dump cookies, we just need to quickly kill the Chrome process.

```
kill Chromeprocess
```

Restart it to enable remote debugging, restore the previous session and load the correct user profile.

```
run "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\UserName\AppData\Local\Google\Chrome\User Data" --restore-last-session
```

Proxying [cookienapper.py](https://github.com/greycatsec/cookienapper) through a socks tunnel and profit!!

```
socks 8081 socks5
proxychains4 python3 cookienapper.py
```

We are almost there, but not yet. After inspecting the cookies we got from cookienapper, it turns out that the user was watching YouTube instead of working on Azure infrastructure deployments(a bad employee accidentally protected the company in an effortless way). So, the cookies we got were essentially useless.

## When will they start working !?

Is there a way to possibly gather some information about users’ currently opened tabs without going through dumped cookies? It is mentioned in [Hands in the Cookie Jar](/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e) by Justin, the /json endpoint will provide us with more details of each opened tab.

Press enter or click to view image in full size

![Information From /json HTTP Endpoint]()

Information From /JSON Endpoint

There are a couple of interesting fields that caught my eye, we can see the title of every tab the user has opened, and the url that the tab is currently browsing. Nice! We can sit here and refresh the “http://localhost:9222/json" page and filter out by title and URLs to see what the user is actually doing and hope the user will eventually log in to Azure so we can also enjoy the Azure cookies. Here, we can see the user is watching his/her favorite music video.

## There must be a better way

I eventually got tired of hitting the refresh button over and over, so I decided to look for alternative ways to monitor user activities. I revisited the [cookienapper.py](https://github.com/greycatsec/cookienapper) source code again and noticed that we were establishing a WebSocket connection to the “webSocketDebuggerUrl” and supplied a JSON string that looks like the following JSON

*{“id”:1, “method”:”Network.getAllCookies”}*

A quick google on the method “Network.getAllCookies” eventually led me to CDP documentation. It turns out, the method we were calling to dump cookies was just one of the commands supported by CDP.

After going through some of the domains and methods provided in the document, I landed on the domain “Target”. The description of the domain says: “Supports additional target discovery and allows attaching to them.” After taking a closer look at the methods, there is one that caught my eyes called [Target.setDiscoverTargets](https://chromedevtools.github.io/devtools-protocol/tot/Target/#method-setDiscoverTargets).

Press enter or click to view image in full size

![]()

Target.setDiscoverTargets

## What is a “target”

What are “targetCreated”, “targetInfoChanged”, “targetDestroyed”? In order to understand those, we must understand what is a “target”. This is a [short conversation](https://groups.google.com/g/chrome-debugging-protocol/c/KoxAk8F4yiU?pli=1) that explains “what is a target”, but I will also give my own understanding here. A “target” can be in the form of many types, such as “page”, or “iframe”. When you open a new tab in your browser, it creates a new blank “page” target, and when a page loads javascript, it creates a new “iframe” target. Each target will contain certain information about themselves such as “title”, “url”, “targetId” etc…

When a new target is created, the “targetCreated” event is triggered. When ...