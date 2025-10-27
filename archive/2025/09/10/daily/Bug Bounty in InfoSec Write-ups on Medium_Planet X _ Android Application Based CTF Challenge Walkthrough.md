---
title: Planet X : Android Application Based CTF Challenge Walkthrough
url: https://infosecwriteups.com/planet-x-android-application-based-ctf-challenge-walkthrough-778547aac015?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:53:56.415786
---

# Planet X : Android Application Based CTF Challenge Walkthrough

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F778547aac015&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fplanet-x-android-application-based-ctf-challenge-walkthrough-778547aac015&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fplanet-x-android-application-based-ctf-challenge-walkthrough-778547aac015&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-778547aac015---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-778547aac015---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Planet X :** Android Application Based CTF Challenge **Walkthrough**

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:64:64/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---byline--778547aac015---------------------------------------)

[Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---byline--778547aac015---------------------------------------)

8 min read

·

Sep 27, 2020

--

Share

![]()

Planet-X is an intermediate level Android application CTF challenge. The aim of this CTF challenge is to learn and concentrate on the basic flaws which are found while performing security assessment of a mobile application.

We will be observing the basic misconfigurations which will lead our path and help us to find the flag.

Let’s take a minute to thank [Moksh](https://in.linkedin.com/in/moksh-makhija) for creating this challenge. If someone wants to try and solve the challenge before going through the walkthrough, the link for the CTF can be found [[here](https://github.com/lucideus-repo/cybergym/tree/master/cybergym1/mobile/lab1)] and the application can be downloaded from [[here](https://github.com/lucideus-repo/cybergym/tree/master/cybergym1/mobile/lab1/app/release)].

So, before beginning the walkthrough, highlighting the fact that the challenge can be solved in two different ways. Both the ways teach us something unique and make us aware about the security flaws.

Just stay connected till the end….

First Approach is basically the intended way how the challenge was designed to be solved.

**Tools Used :**

> [**adb**](https://www.xda-developers.com/install-adb-windows-macos-linux/) : command line tool that lets you communicate with device
>
> [**apktool**](https://ibotpeaches.github.io/Apktool/) : command line tool for reverse engineering android applications
>
> [**jadx-gui**](https://github.com/skylot/jadx) : tool for producing Java source code from Android Dex and APK files

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--778547aac015---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--778547aac015---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--778547aac015---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--778547aac015---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--778547aac015---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:96:96/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--778547aac015---------------------------------------)

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:128:128/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--778547aac015---------------------------------------)

[## Written by Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---post_author_info--778547aac015---------------------------------------)

[103 followers](https://saurabh-jain.medium.com/followers?source=post_page---post_author_info--778547aac015---------------------------------------)

·[105 following](https://medium.com/%40saurabh-jain/following?source=post_page---post_author_info--778547aac015---------------------------------------)

Security Enthusiast Linkedin : <https://www.linkedin.com/in/saurabh-jain-503991165/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----778547aac015---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----778547aac015---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----778547aac015---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----778547aac015---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----778547aac015---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----778547aac015---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----778547aac015---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----778547aac015---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----778547aac015---------------------------------------)