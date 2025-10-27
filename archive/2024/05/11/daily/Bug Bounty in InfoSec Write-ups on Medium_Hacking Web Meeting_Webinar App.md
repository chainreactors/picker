---
title: Hacking Web Meeting/Webinar App
url: https://infosecwriteups.com/hacking-web-meeting-webinar-app-1cb31c648752?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-11
fetch_date: 2025-10-06T17:16:16.722864
---

# Hacking Web Meeting/Webinar App

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1cb31c648752&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-web-meeting-webinar-app-1cb31c648752&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-web-meeting-webinar-app-1cb31c648752&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1cb31c648752---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1cb31c648752---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hacking Web Meeting/Webinar App

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--1cb31c648752---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--1cb31c648752---------------------------------------)

3 min read

·

Feb 23, 2024

--

Listen

Share

Hello Community,

This article is about the Web meeting App, which i was invited as a part of their private program. This was the first time that i was testing web meting app.

As usual, I started playing with the functionalities and inspecting the traffic. As this is the real time traffic Majority of the functionality was over Web Socket.

I would recommend below link to understand how to inspect and play with the web socket traffic

[## Testing for WebSocket vulnerabilities with Burp Suite

### WebSockets are long-lived connections that support asynchronous communication in both directions. They are often used…

portswigger.net](https://portswigger.net/burp/documentation/desktop/testing-workflow/websockets?source=post_page-----1cb31c648752---------------------------------------)

I found two access control Bugs while testing this app, which i have described below

## ***Bypass Public chat restriction***

This was the Web meeting app and it has two roles Presenter/Meeting Admin and attendee. As per below screenshot Presenter could set webinar option to allow only Private chat.

Press enter or click to view image in full size

![]()

Webinar Options

Using the Presenter account i enforced private chat only in webinar.

Now i joined as attendee in another browser and as expected i was only able to send chat to presenter.

Press enter or click to view image in full size

![]()

Private Chat Only

I sent message to presenter and intercepted that websocket request which contained parameter “isPrivate” with value true. I set the parameter value to false and forwarded the request as below

![]()

Websocket request updated

Request went successful and our chat message was delivered publicly. Using this vulnerability any attendee could bypass private chat restriction and send the Public Chat.

## **Shared File Delete**

There was another functionality which allows Presenter to upload file and share.

As a presenter , I uploaded and shared file as per below screenshot

Press enter or click to view image in full size

![]()

Meeting File

Press enter or click to view image in full size

![]()

Shared File

In another browser, I was logged in as an attendee and was intercepting all the traffic. Observing that reveled content id of the file shared by Presenter. so i sent one of the websocket request from the attendee traffic to Repeater and updated it with below request

Press enter or click to view image in full size

![]()

Modified Web socket Request

![]()

Server Response

Above request went through and file shared by presenter got deleted by attendee.

Using this Vulnerability any attendee could delete file shared by Presenter/Meeting Admin.

[Information Security](https://medium.com/tag/information-security?source=post_page-----1cb31c648752---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----1cb31c648752---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----1cb31c648752---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----1cb31c648752---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1cb31c648752---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1cb31c648752---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1cb31c648752---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1cb31c648752---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--1cb31c648752---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:96:96/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---post_author_info--1cb31c648752---------------------------------------)

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:128:128/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---post_author_info--1cb31c648752---------------------------------------)

[## Written by Ronak Patel](https://ronak-9889.medium.com/?source=post_page---post_author_info--1cb31c648752---------------------------------------)

[419 followers](https://ronak-9889.medium.com/followers?source=post_page---post_author_info--1cb31c648752---------------------------------------)

·[21 following](https://medium.com/%40ronak-9889/following?source=post_page---post_author_info--1cb31c648752---------------------------------------)

Cybersecurity Researcher

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----1cb31c648752---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1cb31c648752---------------------------------------)

[About](https://medium.com/about?autoplay=1&...