---
title: Cracking JWTs: A Bug Bounty Hunting Guide [Part 5]
url: https://infosecwriteups.com/cracking-jwts-a-bug-bounty-hunting-guide-part-5-2791be30bd17?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-09
fetch_date: 2025-10-06T22:51:49.654493
---

# Cracking JWTs: A Bug Bounty Hunting Guide [Part 5]

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2791be30bd17&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcracking-jwts-a-bug-bounty-hunting-guide-part-5-2791be30bd17&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcracking-jwts-a-bug-bounty-hunting-guide-part-5-2791be30bd17&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2791be30bd17---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2791be30bd17---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Cracking JWTs: A Bug Bounty Hunting Guide [Part 5]

## JWT Authentication Bypass via `kid` Header Path Traversal — A Sneaky Admin Takeover

[![Aditya Bhatt](https://miro.medium.com/v2/resize:fill:64:64/1*6TFmlC58KtmaRsYHdjy9Qg.jpeg)](https://medium.com/%40adityabhatt3010?source=post_page---byline--2791be30bd17---------------------------------------)

[Aditya Bhatt](https://medium.com/%40adityabhatt3010?source=post_page---byline--2791be30bd17---------------------------------------)

6 min read

·

Jun 7, 2025

--

Listen

Share

> “Sometimes all it takes is a null byte and some path traversal to crack an admin panel wide open.” ~ Aditya Bhatt

## ✨ Preface

This is Part 5 of my “Cracking JWTs: A Bug Bounty Hunting Guide” series, where I deep-dive into real-world JWT misconfigurations using PortSwigger labs. If you’ve missed the earlier writeups, make sure to check out:

* [JWT Series on Medium](https://medium.com/%40adityabhatt3010/list/cracking-jwts-a-bug-bounty-hunting-guide-289859dc4985)
* [Part 1 — JWT HS256 None Bypass](/cracking-jwts-a-bug-bounty-hunting-guide-99d6c21d78c9)
* [Part 2 — JWT Key Confusion Exploitation](/cracking-jwts-a-bug-bounty-hunting-guide-part-2-7bd111ddadd8)
* [Part 3 — JWT](/cracking-jwts-a-bug-bounty-hunting-guide-part-3-4cee87018c39) `[jwk](/cracking-jwts-a-bug-bounty-hunting-guide-part-3-4cee87018c39)` [Header Injection](/cracking-jwts-a-bug-bounty-hunting-guide-part-3-4cee87018c39)
* [Part 4 — JWT](/cracking-jwts-a-bug-bounty-hunting-guide-part-4-ad98636c5238) `[jku](/cracking-jwts-a-bug-bounty-hunting-guide-part-4-ad98636c5238)` [Header Injection](/cracking-jwts-a-bug-bounty-hunting-guide-part-4-ad98636c5238)

This series unpacks how insecure JWT handling can lead to full authentication bypasses, privilege escalations, and even complete admin takeovers 💀

Press enter or click to view image in full size

![]()

JWT Article Index

## 🔐 Quick Primer — JWT & the `kid` Header

JWTs (JSON Web Tokens) are stateless tokens used for authentication. They are signed using either a symmetric (`HS256`) or asymmetric (`RS256`) key and verified by the server before granting access.

The `kid` (Key ID) header is a hint to the server about which key to use when verifying the JWT signature. In a secure setup, this value should be matched against a static list of trusted key identifiers.

But when developers directly use the `kid` value to build a path and read secret keys from the filesystem, attackers can abuse it with path traversal — and even point it to `/dev/null` to get verified with a null byte. That's exactly what this attack leverages.

Press enter or click to view image in full size

![]()

JWT Article 5

## 🚨 TL;DR

In this write-up, we exploit a poorly implemented JWT validation mechanism that uses the `kid` header to load a key from the server's file system. By using path traversal to point the `kid` to `/dev/null` and signing the token with a null byte (`AA==`), we impersonate the admin user and delete other users. 🧨

## 🛠️ Lab Setup — PortSwigger’s Playground

* Lab: JWT authentication bypass via `kid` header path traversal
* Account: wiener:peter
* Goal: Access `/admin` as administrator and delete the user `carlos`

## 🔬 Exploit Walkthrough (Step by Step PoC)

This ain’t your average PoC. We’re going full gladiator mode — step-by-step, raw hacking, no fluff.

> *📌 Tool of Choice: Burp Suite + JWT Editor Extension — aka Hacker’s Swiss Army Knife 🗿*

Press enter or click to view image in full size

![]()

### 1. Enter the Arena

Launch the lab and log in using your trusted duo: `wiener:peter`.

Press enter or click to view image in full size

![]()

Screenshot 1

🪪 Credentials? Check. Lab loaded? Check. Adrenaline? Hell yeah.

### 2. Touch the Forbidden Door

Try accessing `/admin`. You’ll be stopped at the gate:

> *“Admin interface only available if logged in as an administrator.” 🛑 But guess what? We* become *the admin.*

Press enter or click to view image in full size

![]()

Screenshot 2

### 3. Intercept That Sweet Packet

Capture the `/admin` request in Burp and slam it into Repeater.

⏳ It's about to get spicy.

Press enter or click to view image in full size

![]()

Screenshot 3

### 4. Blacksmith Forge: Null Byte Key

* Go to JWT Editor > Keys > New Symmetric Key
* Forge a new key like the cyberblacksmith you are.
* Manually set the `k` value to `AA==` (Base64 for null byte) ☠️ That's right — we’re signing this bad boy with *nothing*.

Press enter or click to view image in full size

![]()

Screenshot 4

### 5. Prep the Payload

Head back to JWT tab in Repeater. Highlight the token. You’re now holding a digital grenade.

Press enter or click to view image in full size

![]()

Screenshot 5

### 6. Mold the Header of Doom

* Set `sub` to `"administrator"` — that’s who we are now
* Set `kid` to: `../../../../../../../dev/null`

🎯 Precision path traversal — deep into the abyss.

Press enter or click to view image in full size

![]()

Screenshot 6

### 7. Sign It Like a Legend

Click Sign, select the null-byte key, and tick `Don’t modify the header`. You’re not just modifying a token. You’re rewriting fate. 🗿🔥

Press enter or click to view image in full size

![]()

Screenshot 7

### 8. Send It. Smash It. Own It.

Hit Send — and BOOM 💥 You’ve bypassed auth. You’re inside `/admin`.

No keys. No doors. Just brains and bytes.

Press enter or click to view image in full size

![]()

Screenshot 8

### 9. Pull the Trigger on Carlos

Find: `/admin/delete?username=carlos` .

Paste it into the URL bar — fire it off like a precision-guided cyber missile. 🧨 Carlos? Eliminated.

Press enter or click to view image in full size

![]()

Screenshot 9

### 10. Confirm the Kill 🏁

Right-click → Show in Browser.

Paste that final URL — *Mission Complete,* hacker. 🧠💀

Press enter or click to view image in full size

![]()

## 🧩 Why This Works

The app is dynamically building a file path based on the `kid` value and using it to read the secre...