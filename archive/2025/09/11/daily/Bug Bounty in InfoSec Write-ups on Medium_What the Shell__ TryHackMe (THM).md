---
title: What the Shell?| TryHackMe (THM)
url: https://infosecwriteups.com/what-the-shell-tryhackme-thm-248b5d58f128?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:58:00.438877
---

# What the Shell?| TryHackMe (THM)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F248b5d58f128&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40Deepika-001%2Fwhat-the-shell-tryhackme-thm-248b5d58f128&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40Deepika-001%2Fwhat-the-shell-tryhackme-thm-248b5d58f128&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

# **What the Shell?**| TryHackMe (THM)

[![Deepika B](https://miro.medium.com/v2/resize:fill:64:64/1*h5OM2iGXy_anSDpsRvuDwQ.jpeg)](/%40Deepika-001?source=post_page---byline--248b5d58f128---------------------------------------)

[Deepika B](/%40Deepika-001?source=post_page---byline--248b5d58f128---------------------------------------)

14 min read

·

Mar 21, 2025

--

Share

## -Privilege Escalation

## Task 1 :What is a shell?

shells are what we use when interfacing with a Command Line environment (CLI). In other words, the common bash or sh programs in Linux are examples of shells, as are cmd.exe and Powershell on Windows. When targeting remote systems it is sometimes possible to force an application running on the server (such as a webserver, for example) to execute arbitrary code. When this happens, we want to use this initial access to obtain a shell running on the target.

**Two types of shell:**

***Reverse Shel****l* — force the remote server to send the local machine command line access to the remote server

***Bind Shell*** — Local Machine hacks in the target machine by opening a port on the server, so that can execute further commands.

## Task 2 :Tools

Netcat: A general tool.

Socat: A more stable and stronger version of Netcat.

**Metasploit — multi/handler:**The `exploit/multi/handler` module of the Metasploit framework is, like socat and netcat, used to receive reverse shells.

**Msfvenom:**Like multi/handler, msfvenom is technically part of the Metasploit Framework, however, it is shipped as a standalone tool. Msfvenom is used to generate payloads on the fly. Whilst msfvenom can generate payloads other than reverse and bind shells, these are what we will be focusing on in this room.

--

--

[![Deepika B](https://miro.medium.com/v2/resize:fill:96:96/1*h5OM2iGXy_anSDpsRvuDwQ.jpeg)](/%40Deepika-001?source=post_page---post_author_info--248b5d58f128---------------------------------------)

[![Deepika B](https://miro.medium.com/v2/resize:fill:128:128/1*h5OM2iGXy_anSDpsRvuDwQ.jpeg)](/%40Deepika-001?source=post_page---post_author_info--248b5d58f128---------------------------------------)

[## Written by Deepika B](/%40Deepika-001?source=post_page---post_author_info--248b5d58f128---------------------------------------)

[11 followers](/%40Deepika-001/followers?source=post_page---post_author_info--248b5d58f128---------------------------------------)

·[22 following](/%40Deepika-001/following?source=post_page---post_author_info--248b5d58f128---------------------------------------)

Cybersecurity Engineer | Curious learner exploring the world of security, Linux, and hacking. Sharing insights and write-ups along the way 👩🏻‍💻👾

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----248b5d58f128---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----248b5d58f128---------------------------------------)

[About](/about?autoplay=1&source=post_page-----248b5d58f128---------------------------------------)

[Careers](/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----248b5d58f128---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----248b5d58f128---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----248b5d58f128---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----248b5d58f128---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----248b5d58f128---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----248b5d58f128---------------------------------------)