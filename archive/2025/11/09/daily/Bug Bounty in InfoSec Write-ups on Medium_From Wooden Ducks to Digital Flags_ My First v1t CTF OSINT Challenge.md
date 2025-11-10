---
title: From Wooden Ducks to Digital Flags: My First v1t CTF OSINT Challenge
url: https://infosecwriteups.com/from-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:36.714129
---

# From Wooden Ducks to Digital Flags: My First v1t CTF OSINT Challenge

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F84c38c9fbcb8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-84c38c9fbcb8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-84c38c9fbcb8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Wooden Ducks to Digital Flags: My First v1t CTF OSINT Challenge

[![Chetan Chinchulkar](https://miro.medium.com/v2/resize:fill:64:64/1*b3FG33fV4gKML4sEy1Zd7A.jpeg)](https://medium.com/%40omnipresent_?source=post_page---byline--84c38c9fbcb8---------------------------------------)

[Chetan Chinchulkar](https://medium.com/%40omnipresent_?source=post_page---byline--84c38c9fbcb8---------------------------------------)

5 min read

·

17 hours ago

--

Listen

Share

## When a Halloween decoration becomes your next cybersecurity puzzle

![]()

**Difficulty:** Beginner-Friendly | **Category:** OSINT

Hey there,

I’m Chetan Chinchulkar (aka **omnipresent**), and I’m that person who spends their weekdays as an SDE and weekends hunting flags like they’re Pokémon. Currently sitting in the **top 1% on TryHackMe** ([check out my profile](https://tryhackme.com/p/omnipresent)), I’ve developed what my friends call an “unhealthy obsession” with CTFs. I prefer to call it “passionate dedication.” 😄

This past weekend, I dove into the **v1t CTF**, and I wanted to share not just how I solved one of the challenges, but also my thought process — because honestly, that’s where the real learning happens.

## 🦆 The Challenge: Duck Company

**Category:** OSINT
**Description:**

> I found this company selling this cute wooden duck for the halloween but i forgot where link web store :< can you help me find it

**Flag format:** `v1t{example.com}`

**What we got:** A single image of an adorable wooden duck with magical vibes and a pumpkin (perfect for Halloween, honestly).

![]()

When I first saw this, my immediate thought was: “Okay, someone’s testing my Google-fu.” But as any seasoned CTF player knows, it’s never *just* about Googling. Or is it? 🤔

## 🔍 My Approach: The OSINT Methodology

Here’s the thing about OSINT challenges — they’re like detective work, but instead of a magnifying glass, you’ve got browser tabs. Lots of them.

## Step 1: Check the Metadata (Because Why Not?)

My first instinct with any image-based OSINT challenge is to check for hidden metadata. You’d be surprised how often people leave GPS coordinates, camera info, or other juicy details in their photos.

**Tool of choice:** `exiftool`

```
exiftool duck_image.jpg
```

I ran this expecting… well, *something*. But nope — nothing particularly useful jumped out. No hidden coordinates, no secret messages in the EXIF data. Just a regular image file.

**Lesson learned:** Always check metadata first, but don’t be disappointed when it’s a dead end. It’s about eliminating possibilities.

## Step 2: Reverse Image Search (The Classic Move)

Alright, metadata was a bust. Time for the bread and butter of OSINT: **Google Reverse Image Search**.

I uploaded the image to Google Images and hit search. Within seconds, results started pouring in:

Press enter or click to view image in full size

![]()

Search results from google

**Bingo!** 🎯

The search revealed this was a **“DCUK Magician Duckling”** — available on Amazon, eBay, and… wait for it… a dedicated website.

Now, here’s where I could’ve just grabbed the first result and called it a day. However, something I’ve learned from countless CTFs (and a few embarrassing incorrect submissions) is: **always verify before submitting**.

## Step 3: Digging Deeper (The Patience Game)

The flag format was `v1t{example.com}`, which meant I needed a domain name. Amazon and eBay are retailers, not the actual company. So I kept scrolling through the results.

That’s when I spotted it: **www.dcuk.com**

I clicked through and landed on the official DCUK website. And there it was — the *exact* wooden duck from the challenge image, sitting pretty in their product catalog.

Press enter or click to view image in full size

![]()

**The “aha!” moment:** This wasn’t just *a* place selling the duck — this was *the* company that makes them. Given the challenge name was literally “Duck Company,” this had to be it.

## 🚩 The Flag

```
v1t{dcuk.com}
```

**Submitted. Accepted. Victory!**

Press enter or click to view image in full size

![]()

## What I Learned (And What You Can Take Away)

### 1. Don’t Rush the First Answer

When I saw Amazon and eBay in the results, I could’ve stopped there. But CTFs reward thoroughness. The extra 30 seconds of scrolling made all the difference.

### 2. Context Matters

The challenge name “Duck Company” was a hint. In OSINT, every piece of information — even the challenge title — can guide you to the answer.

### 3. Methodology Over Speed

I could’ve skipped the metadata check, but having a systematic approach means you don’t miss obvious wins when they *do* appear in other challenges.

### 4. Tools Are Your Friends

* **exiftool** — Metadata extraction
* **Google Reverse Image Search** — Visual recognition
* **Critical thinking** — The most important tool (can’t install this one via apt-get, unfortunately)

## OSINT Tools I Keep in My Arsenal

For those just getting into OSINT challenges, here are some tools I regularly use:

* [**exiftool**](https://github.com/exiftool/exiftool) — Image metadata analysis
* **Google Reverse Image Search** — Visual identification
* [**TinEye**](https://tineye.com/) — Alternative reverse image search
* [**Sherlock**](https://github.com/sherlock-project/sherlock) — Username enumeration across platforms
* [**theHarvester**](https://github.com/laramies/theHarvester) — Email and subdomain gathering
* [**Maltego**](https://www.maltego.com/) — Relationship mapping (for complex investigations)

## 🤔 How Would You Have Solved This?

Here’s what I’m curious about: Would you have approached this differently? Maybe used TinEye instead of Google? Or perhaps you have a favorite OSINT framework I should check out?

Drop your thoughts in the comments — I’m always looking to learn new techniques from the community!

## 🎯 What’s Next?

This is just the first of my **v1t CTF writeup series**. I’ll be pu...