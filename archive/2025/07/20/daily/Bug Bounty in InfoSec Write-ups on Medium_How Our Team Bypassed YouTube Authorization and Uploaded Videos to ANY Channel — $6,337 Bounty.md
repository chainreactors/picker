---
title: How Our Team Bypassed YouTube Authorization and Uploaded Videos to ANY Channel — $6,337 Bounty
url: https://infosecwriteups.com/how-our-team-bypassed-youtube-authorization-and-uploaded-videos-to-any-channel-6-337-bounty-d39df15f11df?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-20
fetch_date: 2025-10-06T23:28:33.377083
---

# How Our Team Bypassed YouTube Authorization and Uploaded Videos to ANY Channel — $6,337 Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd39df15f11df&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-our-team-bypassed-youtube-authorization-and-uploaded-videos-to-any-channel-6-337-bounty-d39df15f11df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-our-team-bypassed-youtube-authorization-and-uploaded-videos-to-any-channel-6-337-bounty-d39df15f11df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d39df15f11df---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d39df15f11df---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 💥 How *Our Team* Bypassed YouTube Authorization and Uploaded Videos to ANY Channel — $6,337 Bounty

[![Aditya Sunny](https://miro.medium.com/v2/resize:fill:64:64/1*XcAW_t_riaR4a4fPbM4VcA.webp)](https://adityasunny06.medium.com/?source=post_page---byline--d39df15f11df---------------------------------------)

[Aditya Sunny](https://adityasunny06.medium.com/?source=post_page---byline--d39df15f11df---------------------------------------)

3 min read

·

Jul 19, 2025

--

1

Listen

Share

🧠 Quick Summary

In this post, I explain how I discovered a severe **authorization bypass vulnerability** in YouTube’s internal tool, **Video Builder** ([https://director.youtube.com](https://director.youtube.com/)). This tool allows advertisers to easily create and upload video ads to their YouTube channels.

Due to a missing authorization check in the backend, any user with access to this tool could upload a video to **any YouTube channel** by simply modifying the `channelId` parameter in a specific request. This meant that attackers could target **any verified or influential YouTube channel** and upload content without their permission.

Google acknowledged the vulnerability, resolved it quickly, and awarded me **$6,337** under their **Google Vulnerability Reward Program (VRP)**.

## 🎮 Background: What is YouTube Video Builder?

**YouTube Video Builder** is a lightweight video creation tool for businesses and advertisers. It helps create short promotional videos (typically 6–15 seconds) using static assets like logos, images, and text animations.

Key features:

* Templates for quick video generation
* Brand customization options
* Direct integration for uploading to a connected YouTube channel

The tool is available only via invitation or request, making it relatively unknown to the public.

Press enter or click to view image in full size

![]()

REWARD PROOF

## 🕵️‍♂️ The Discovery Process

## 1. Gaining Access

I gained access to YouTube Video Builder via my Google Ads account. Once inside, I explored the video creation flow.

## 2. Creating a Sample Video

I selected a template, added sample brand assets (logo, image, and tagline), and moved through the creation steps.

## 3. Intercepting the Upload Request

During the final step (video upload), I clicked “Save Video” and intercepted the outgoing request using **Burp Suite**.

**Endpoint:**

```
POST https://director.youtube.com/videobuilder/_/rpc/Image2VideoUiService/UploadToYouTube
```

**Original payload:**

```
{
  "channelId": "UCabc123xyz...",
  "videoTitle": "Aditya Test Video",
  "videoPrivacy": "unlisted",
  ...
}
```

## 4. The Attack Idea

I had a simple but powerful thought:

> *“What if I change the* `channelId` *to a channel I don't own?"*

I extracted a public YouTube channel ID (easily available from any channel URL).

## 5. Replaying with a Different Channel ID

I modified the payload to include a different `channelId`:

```
{
  "channelId": "UCnOtMyChAnNeL123",
  "videoTitle": "Test Attack Video",
  ...
}
```

I resent the request.

## 6. Success: Unauthorized Upload

The server responded successfully and returned:

```
{
  "videoId": "dEfaUlTxXyZ123"
}
```

This meant my video had been uploaded to the **targeted channel** without any form of authorization. The video was set to “unlisted” and visible to anyone with the link.

## 🎯 Real-World Impact

This bug could allow:

* Uploading defaming or malicious videos to **any channel**
* Damaging brand reputation or spreading misinformation
* Targeting high-profile influencers, businesses, or even political accounts

For example:

> *An attacker could upload a scam video to a verified channel and promote it using that channel’s reputation.*

Although the video would be unlisted, it would still be accessible to the channel owner and anyone with the video link.

🔍 Root Cause Analysis

The vulnerability stemmed from a classic **IDOR (Insecure Direct Object Reference)** issue.

## Problem:

The backend **did not validate** whether the user making the upload request was authorized to use the provided `channelId`.

## What Should Have Happened:

The server should verify that the authenticated user actually manages or owns the YouTube channel associated with the provided `channelId`.

## 💡 How Google Could Have Prevented It

1. **Strict Backend Authorization**

* Validate ownership of `channelId` on the server side.

1. **Don’t Trust Client-Side Inputs**

* Never rely on client-submitted values for sensitive identifiers.

1. **Regular Security Audits of Internal Tools**

* Internal or invite-only tools must go through the same security checks as public-facing services.

## 🔥 Proof of Concept (PoC) Recap

1. Accessed YouTube Video Builder via Google Ads
2. Created a sample ad video
3. Intercepted final upload request
4. Replaced `channelId` with that of a public channel
5. Sent the request
6. Server responded with a valid `videoId` — upload successful

## 📙 Conclusion

This bug was simple in execution but had the potential for massive impact. It showed how trusting frontend data, even in internal tools, can lead to critical authorization issues.

## Key Takeaways:

* Always validate ownership and access at the backend
* Frontend controls are never enough
* Even restricted tools can have dangerous flaws

## 👨‍💻 About the Author

**Aditya Sunny**
 Bug Bounty Hunter | Security Heroes Honoree
 Reported to: Meta, Google, Dell, Bajaj Finserv
 📷 Instagram: [@hackerdiary100](https://instagram.com/hackerdiary100)
 📝 Medium blog:

[Yeswehack](https://medium.com/u/b8ebb8852210?source=post_page---user_mention--d39df15f11df---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d39df15f11df---------------------------------------)

[Google](https://medium.com/tag/google?source=post_page-----d39df15f11df----------------------------------...