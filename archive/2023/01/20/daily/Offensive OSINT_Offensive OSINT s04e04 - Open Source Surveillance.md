---
title: Offensive OSINT s04e04 - Open Source Surveillance
url: https://www.offensiveosint.io/offensive-osint-s04e04-open-source-surveillance/
source: Offensive OSINT
date: 2023-01-20
fetch_date: 2025-10-04T04:22:13.980361
---

# Offensive OSINT s04e04 - Open Source Surveillance

[![Offensive OSINT](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

* [Home](/)
* [About me](/about-me/)
* [Open Source Surveillance](https://www.os-surveillance.io)
* [kamerka.io](https://www.kamerka.io)
* [Sign up](/signup/)
* [Account](/account/)
* [Sign in](/signin/)
* [Patreon](https://patreon.com/offensiveosint)

##### Search Here

×

## Offensive OSINT s04e04 - Open Source Surveillance

* Wojciech

  [![Wojciech](/content/images/size/w100/2023/02/OffensiveOsint-logo-RGB-2.png)](/author/wojciech/)

[Wojciech](/author/wojciech/)
19 Jan 2023 • 17 min read

![Offensive OSINT s04e04 - Open Source Surveillance](/content/images/2023/01/01_OSS_logo_podstawowe-1.png)

Open Source Surveillance takes intelligence gathering and cyber espionage to a whole new level. It can be used for offensive security, but from the other hand can be also helpful in OSINT and law enforcement investigations. Thanks to 18 modules, OSS can show real-time view of the city from variety of cameras, social media posts or Internet facing devices. Read article to get familiar with the tool and potential cases it can help with.

**Due to size of the screenshots please turn** on desktop version if you are on mobile.

![](https://www.offensiveosint.io/content/images/2023/01/oss1-2.png)

Open Source Surveillance in Tokyo

**TL;DR**

*Open Source Surveillance is real-time intelligence gathering tool, which uses data from variety of sources, including social media, cameras, transportation, Internet of things and Industrial Control System devices, WIFI network and much more.*

**More info & screenshots**

[https://www.os-surveillance.io](https://www.os-surveillance.io/?ref=offensiveosint.io)

Newest update

> Gather geo intel in a blink of an eye with new Open Source Surveillance update. It brings new modules, improved interface and enhanced performance to collect data even more efficiently. Now it's easier than ever to detect, track, and monitor potential threats in real-time. [#OSINT](https://twitter.com/hashtag/OSINT?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [pic.twitter.com/WekVAgx9GZ](https://t.co/WekVAgx9GZ?ref=offensiveosint.io)
>
> — Offensive OSINT (@the\_wojciech) [March 30, 2023](https://twitter.com/the_wojciech/status/1641502920901287942?ref_src=twsrc%5Etfw&ref=offensiveosint.io)

## Access

~~Application is almost done, there are some small UI/CSS bugs or unexpected exceptions, but it's fully working intelligence gathering tool that can give a lot of fun and help with variety of cases.
If you are law enforcement officer, investigative journalist, intelligence analyst or OSINT researcher and want to give the tool a try please reach out to me from your corporate email address. Please also let me know if you are subscriber via Paypal or Stripe to get access~~

Patreon access

[Offensive OSINT s04e05 - Open Source Surveillance - Patreon

In this post I would like to share my plans about Open Source Surveillance project and how you can participate and create best OSINT tool ever. First things first, I’m excited to announce I started Patreon to get help with the project as well as create community of OSINT professionals

![](https://www.offensiveosint.io/content/images/size/w256h256/2020/07/oo.png)Offensive OSINTWojciech

![](https://www.offensiveosint.io/content/images/2023/01/01_OSS_logo_podstawowe-2.png)](https://www.offensiveosint.io/offensive-osint-s04e05-open-source-surveillance-patreon/)

Wait for gif to load which presents live view of the tool

![](https://www.offensiveosint.io/content/images/2023/01/oss-1.gif)

## Introduction

Nowadays, almost every our step is tracked and under surveillance. It does not matter if it's online activity or 'on the ground', have you ever thought how many cameras are you on during simple walk in your city? How many Snaps, Instagram photos or Tweets are being taken at specific location? Where are unsecure Wifi networks that might end in cyber security breach? Are there any Internet facing Industrial Control System devices operating in critical infrastructure?

Open Source Surveillance can give you answer for above questions and much much more depending on your goal, whether it's getting access to some devices, finding exact coordinates of the photo or checking activity on social media during protests.

Tool itself is quite complex (design, implementation, API sources) but the concept stays as easy as possible, and User Interface is very intuitive, so let's talk about the project and how to get out of it as much as possible.

![](https://www.offensiveosint.io/content/images/2023/01/cns-1.png)

## Open Source Surveillance

Tool has been developed to assist in variety of OSINT investigations that require to research specific place or location. First case that comes to mind is geolocation task of some photo. If you suspect that picture might have been taken in some city, you can easily scan for current and historical view via Snapchat, Twitter, Instagram, Flickr and even YouTube, or look on live footage from street cameras. However, possibilities of the tool are much more beyond that.

### Choosing a target

As mentioned, tool is most useful when gathering intelligence about specific places, which can be country, city, district or even street. I recommend to set your target as a city and around 40-50km around it, since some sources are not always accurate. You can add as many 'targets' i.e. places to scan, as you want, and each one has separate 'workspace', which is independent from other searches.

Give your investigation a title, select place you want to research and click Save.

![](https://www.offensiveosint.io/content/images/2023/01/case-1.png)

### API Keys

In the background, database with predefined keys exists and provide the keys, depending on usage and rate limitations. So during big load and lot of requests it might be unavailable. In that case, user needs to provide their own API keys or tokens for each affected module in "Keys" tab.

### Modules

Modules are separated by category and all of them are quite different from each other. It's related to how some API works. As a quick example - Flickr shows photos in 5km radius but Wigle can present results only on given boundaries.

![](https://www.offensiveosint.io/content/images/2023/01/montral1-1.png)

Modules & features

Almost each module has option to Scan, Show results from database and Hide from map for better customization of all findings.

We will quickly go through all modules to get acquainted with method of operating and what kind of findings we can expect.

## Social Media

We all know that almost every social media platform allow to add location to your posts including ones with photos and videos, so it's relatively easy to extract all information especially when service has an API, like Twitter.

### Twitter ‌

![](https://www.offensiveosint.io/content/images/2023/01/twitt-2.png)

Every tweet is saved into database, with all gathered details, and can be accessed anytime. We know in this case, this Mexican Bar is 3 Amigos.

![](https://www.offensiveosint.io/content/images/2023/01/twitt1-1.png)

### Snapchat

Snapchat is not accurate, but gives you all Snaps in 5 kilometres radius. If there are more than one Snap, you can view them all in the popup on the map.

![](https://www.offensiveosint.io/content/images/2023/01/snap-1.png)

Twitter & Snapchat

### Flickr

Flickr from the other hand is the most accurate from all of the social medias, and there are literally thousands picture in every city, what is very useful for OSINT geolocation tasks.

![](https://www.offensiveosint.io/content/images/2023/01/flickr1-1.png)

Twitter & Snapchat & Flickr

Very accurate location of Flickr photos

![](https://www.offensiveosint.io/content/images/2023/01/flickr2-1.png)

### Instagram

Instagram works differently than previous modules, it shows places that are "registered" in Instagram and Meta in general. Aft...