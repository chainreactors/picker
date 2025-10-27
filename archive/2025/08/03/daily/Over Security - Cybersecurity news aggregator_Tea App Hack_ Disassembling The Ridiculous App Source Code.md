---
title: Tea App Hack: Disassembling The Ridiculous App Source Code
url: https://medium.com/@jankammerath/tea-app-hack-disassembling-the-ridiculous-app-source-code-bc585e15bf4f
source: Over Security - Cybersecurity news aggregator
date: 2025-08-03
fetch_date: 2025-10-07T00:47:39.884911
---

# Tea App Hack: Disassembling The Ridiculous App Source Code

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fbc585e15bf4f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40jankammerath%2Ftea-app-hack-disassembling-the-ridiculous-app-source-code-bc585e15bf4f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40jankammerath%2Ftea-app-hack-disassembling-the-ridiculous-app-source-code-bc585e15bf4f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

# Tea App Hack: Disassembling The Ridiculous App Source Code

[![Jan Kammerath](https://miro.medium.com/v2/resize:fill:64:64/1*f1ckfFZTi4jOIEO6ZPO8CQ.jpeg)](/%40jankammerath?source=post_page---byline--bc585e15bf4f---------------------------------------)

[Jan Kammerath](/%40jankammerath?source=post_page---byline--bc585e15bf4f---------------------------------------)

6 min read

·

Aug 1, 2025

--

14

Share

By now, everyone has heard of the “[Tea app](https://apps.apple.com/us/app/tea-dating-advice/id6444453051)” getting hacked: “[Hackers leak 13,000 user photos and IDs from the Tea app](https://www.nbcnews.com/tech/social-media/tea-app-hacked-13000-photos-leaked-4chan-call-action-rcna221139)”. It’s a Flutter app for Android and iOS, written by [a guy with 6 months programming experience](https://www.linkedin.com/in/seancook1/). The “tea app” allows women to gossip about men on dating portals. I disassembled the source code, so you don’t have to. Let’s do a quick dive through it.

Press enter or click to view image in full size

![]()

A gossip app that received an instant Karma hit for being absolutely ridiculous

If you are as unexcited as I am about this, please stay tuned. I will also explain step by step on how to disassemble the source code of any Android app. This article won’t just plainly explain the ridiculous amateurish mistakes that got the app hacked, but also how it was done. So if you’re not here for the app, I hope you stay for the disassembly process.

## Disassembling the Android app

To get the source code of the app, we just go to its website under [teaforwomen.com](https://www.teaforwomen.com/). There, we’ll find a Google Play Store link that’ll take us to the store listing. In the address bar, we’ll see the following URL.

```
https://play.google.com/store/apps/details?id=com.tea.tea
```

We’re only interested in knowing the app id, which is “com.tea.tea”. That’s the unique identifier of their Android app. Since we want to disassemble the app into source code, we’ll need the APK or XAPK file with…

--

--

14

[![Jan Kammerath](https://miro.medium.com/v2/resize:fill:96:96/1*f1ckfFZTi4jOIEO6ZPO8CQ.jpeg)](/%40jankammerath?source=post_page---post_author_info--bc585e15bf4f---------------------------------------)

[![Jan Kammerath](https://miro.medium.com/v2/resize:fill:128:128/1*f1ckfFZTi4jOIEO6ZPO8CQ.jpeg)](/%40jankammerath?source=post_page---post_author_info--bc585e15bf4f---------------------------------------)

[## Written by Jan Kammerath](/%40jankammerath?source=post_page---post_author_info--bc585e15bf4f---------------------------------------)

[15.9K followers](/%40jankammerath/followers?source=post_page---post_author_info--bc585e15bf4f---------------------------------------)

·[42 following](/%40jankammerath/following?source=post_page---post_author_info--bc585e15bf4f---------------------------------------)

I love technology, programming, computers, mobile devices and the world of tomorrow. Check out [kammerath.com](http://kammerath.com) and follow me on [github.com/jankammerath](http://github.com/jankammerath)

## Responses (14)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----bc585e15bf4f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----bc585e15bf4f---------------------------------------)

[About](/about?autoplay=1&source=post_page-----bc585e15bf4f---------------------------------------)

[Careers](/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----bc585e15bf4f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----bc585e15bf4f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----bc585e15bf4f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----bc585e15bf4f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----bc585e15bf4f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----bc585e15bf4f---------------------------------------)