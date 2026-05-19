---
title: Broken Authentication: How Attackers Gain Unauthorized Access to Your Application.
url: https://infosecwriteups.com/broken-authentication-how-attackers-gain-unauthorized-access-to-your-application-88f7e72439db?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-18
fetch_date: 2026-05-19T06:03:30.729563
---

# Broken Authentication: How Attackers Gain Unauthorized Access to Your Application.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbroken-authentication-how-attackers-gain-unauthorized-access-to-your-application-88f7e72439db&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbroken-authentication-how-attackers-gain-unauthorized-access-to-your-application-88f7e72439db&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-88f7e72439db---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-88f7e72439db---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Broken Authentication: How Attackers Gain Unauthorized Access to Your Application.

[![Sana Jalil](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*6u4wEjiGk55yPVgE)](https://medium.com/%40sanajalil9090?source=post_page---byline--88f7e72439db---------------------------------------)

[Sana Jalil](https://medium.com/%40sanajalil9090?source=post_page---byline--88f7e72439db---------------------------------------)

7 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D88f7e72439db&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbroken-authentication-how-attackers-gain-unauthorized-access-to-your-application-88f7e72439db&source=---header_actions--88f7e72439db---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

## Introduction: Why Broken Authentication Still Wins

Broken Authentication has been on OWASP’s radar for years — yet it remains one of the most exploited vulnerability classes in real-world applications. Why? Because developers focus on building features, and security becomes an afterthought applied inconsistently — especially across different API versions.

In this walkthrough, I’ll show you exactly how a missing rate limit on an OTP endpoint allowed me to brute-force my way into any account — completely bypassing authentication. I’ll walk you through the pentester’s thought process at every step — what to look for, why it matters, and what to do when the server pushes back.

**Step 1: Reconnaissance — Don’t Login, Explore**

The first rule of any engagement: never rush to the obvious attack. Instead of trying to brute-force the login directly, I scanned the page for alternative authentication flows. That’s when I spotted the **“Forgot Password”** option.

This is a pentester’s instinct — password reset flows are almost always weaker than the main login. They are written separately, tested less rigorously, and introduce entirely new code paths. Every feature in a reset flow — OTP delivery, email verification, token generation — is another potential crack in the wall.

**What to look for at this stage:**

* Is there a Forgot Password or account recovery option?
* Does it use OTPs, magic links, or security questions?
* Is the OTP delivered via email, SMS, or in-app notification?
* How many digits is the OTP? The input field length on the UI often reveals this.

Clicking “Forgot Password” brought up an email input field.

![]()

**Step 2: Triggering the OTP — Setting the Stage**

I entered the target’s registered email and clicked **“Send OTP.”** The app confirmed: *“OTP has been sent to your registered email.”*

I had access to that inbox — but let’s think like an attacker for a moment. All they see is this success message. No inbox, no OTP, nothing. But the server just confirmed the email exists and an OTP is on its way. For an attacker, that’s enough. The real question now is whether that OTP is short enough to guess and whether the server will let them keep trying. Two simple conditions — and if both are true, this “Forgot Password” button just became a full account takeover vector.

Press enter or click to view image in full size

![]()

With Burp Suite running as a proxy, I entered a random OTP and a test password on the Reset Password form, then hit submit. The app returned **“Invalid OTP.”** — expected, since I guessed randomly.

Press enter or click to view image in full size

![]()

## Step 3: Intercepting the Request — Understanding What’s Actually Sent

Before attempting anything further, I needed to see what the OTP verification request looks like at the network level. This is where **Burp Suite** comes in — it sits between your browser and the server, capturing every request and response passing through. Think of it as a window into the conversation your browser is having with the application.

With Burp running as a proxy, I entered a random OTP and a test password on the reset form and hit submit. The app returned **“Invalid OTP”** — expected. But what I really wanted was what Burp captured in the background:

This one request tells the whole story:

* **/v3/ in the path** — this is version 3 of the API. Older versions almost certainly exist. Filing that away for later.
* **Email + OTP + new password sent together** — a correct OTP instantly changes the account password to whatever I supply. One request, full takeover.
* **No CSRF token, no session binding** — this request can be replayed freely from Burp. The server isn’t checking whether this came from a legitimate browser session.
* **OTP is a plain 4-digit number** — just 10,000 possible values (0000–9999). A machine covers that in seconds.

Plain numeric OTP, no token binding, no visible protection — the only thing standing between me and success is rate limiting. Time to find out if it exists.

Press enter or click to view image in full size

![]()

**Step 4: Setting Up the Brute Force — Burp Intruder**

I sent the captured request to **Burp Suite’s Intruder** — a built-in tool designed for automated, customized attacks. Think of it as a robot that sends thousands of requests for you, changing one value each time.

## Get Sana Jalil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I marked the `otp` value as the injection point — the position Intruder will cycle through payloads on. I configured the payload type as **Numbers**, ranging from `0000` to `9999`, covering every possible 4-digit OTP. Then I launched the attack.

Press enter or click to view image in full size

![]()

**Step 5: First Attack — Reading What the Server Tells You**

I watched the response length column throughout — a consistent length means the same “Invalid OTP”, anything different means something changed.

First few requests held steady at `507`. Around th...