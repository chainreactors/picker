---
title: BackDoor 1: Walkthrough of NET-SQUARE Hacking Warm-Up Mobile Application Challenge
url: https://infosecwriteups.com/backdoor-1-walkthrough-of-net-square-hacking-warm-up-mobile-application-challenge-7433b8e1a482?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-02
fetch_date: 2025-10-02T19:30:40.960566
---

# BackDoor 1: Walkthrough of NET-SQUARE Hacking Warm-Up Mobile Application Challenge

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7433b8e1a482&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbackdoor-1-walkthrough-of-net-square-hacking-warm-up-mobile-application-challenge-7433b8e1a482&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbackdoor-1-walkthrough-of-net-square-hacking-warm-up-mobile-application-challenge-7433b8e1a482&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7433b8e1a482---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7433b8e1a482---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# BackDoor 1: Walkthrough of NET-SQUARE Hacking Warm-Up Mobile Application Challenge

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:64:64/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---byline--7433b8e1a482---------------------------------------)

[Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---byline--7433b8e1a482---------------------------------------)

3 min read

·

Jun 9, 2021

--

Share

![]()

Recently got an opportunity to participate in a CTF (Capture-The-Flag) event which was organized by **NET-SQUARE**. They had their different set of challenges with respect to Mobile, Web, Network, Source Code, and Thick/Thin Client. So, there were few quite interesting mobile application challenges and here we will be discussing one of them.

> ***Note****: Those who want to explore and want to try the challenges on their own before reading the walkthrough can access the applications from the* [*GitHub*](https://github.com/jain6196/NET-SQUARE-Mobile-Application-Challenges) *repository. The application can be downloaded from [*[*here*](https://github.com/jain6196/NET-SQUARE-Mobile-Application-Challenges/blob/main/Backdoor1/backdoor1.apk)*]. Kindly share your experience with me in the comment box.*

**Challenge Description**: The application hides username and password inside the application and we need to find the credentials using various tools and techniques to log in.

**Tools Used :**

> [***adb***](https://www.xda-developers.com/install-adb-windows-macos-linux/) *: command line tool that lets you communicate with device*
>
> [***apktool***](https://ibotpeaches.github.io/Apktool/) *: command line tool for reverse engineering android applications*
>
> [***jadx-gui***](https://github.com/skylot/jadx) *: tool for producing Java source code from Android Dex and APK files*
>
> [***Android Studio***](https://developer.android.com/studio/?gclid=EAIaIQobChMIrK6UjcPr6wIVzKuWCh2ViASpEAAYASAAEgJ_qvD_BwE&gclsrc=aw.ds) ***:*** *official Integrated Development Environment (IDE) for Android app development*
>
> [***Device***](https://www.genymotion.com/) *: Android Device/Android Studio*…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7433b8e1a482---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7433b8e1a482---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7433b8e1a482---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7433b8e1a482---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--7433b8e1a482---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:96:96/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--7433b8e1a482---------------------------------------)

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:128:128/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--7433b8e1a482---------------------------------------)

[## Written by Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---post_author_info--7433b8e1a482---------------------------------------)

[103 followers](https://saurabh-jain.medium.com/followers?source=post_page---post_author_info--7433b8e1a482---------------------------------------)

·[105 following](https://medium.com/%40saurabh-jain/following?source=post_page---post_author_info--7433b8e1a482---------------------------------------)

Security Enthusiast Linkedin : <https://www.linkedin.com/in/saurabh-jain-503991165/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----7433b8e1a482---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7433b8e1a482---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7433b8e1a482---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7433b8e1a482---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7433b8e1a482---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7433b8e1a482---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7433b8e1a482---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7433b8e1a482---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7433b8e1a482---------------------------------------)