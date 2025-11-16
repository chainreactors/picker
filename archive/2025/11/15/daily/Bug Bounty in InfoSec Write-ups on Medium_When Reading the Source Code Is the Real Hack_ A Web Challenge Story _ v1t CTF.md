---
title: When Reading the Source Code Is the Real Hack: A Web Challenge Story | v1t CTF
url: https://infosecwriteups.com/when-reading-the-source-code-is-the-real-hack-a-web-challenge-story-v1t-ctf-b6adfcaa0fee?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-15
fetch_date: 2025-11-16T03:18:43.693267
---

# When Reading the Source Code Is the Real Hack: A Web Challenge Story | v1t CTF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb6adfcaa0fee&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-reading-the-source-code-is-the-real-hack-a-web-challenge-story-v1t-ctf-b6adfcaa0fee&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-reading-the-source-code-is-the-real-hack-a-web-challenge-story-v1t-ctf-b6adfcaa0fee&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b6adfcaa0fee---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b6adfcaa0fee---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# When Reading the Source Code Is the Real Hack: A Web Challenge Story | v1t CTF

## Sometimes the best hacking tool is just… reading comprehension

[![Chetan Chinchulkar](https://miro.medium.com/v2/resize:fill:64:64/1*b3FG33fV4gKML4sEy1Zd7A.jpeg)](https://medium.com/%40omnipresent_?source=post_page---byline--b6adfcaa0fee---------------------------------------)

[Chetan Chinchulkar](https://medium.com/%40omnipresent_?source=post_page---byline--b6adfcaa0fee---------------------------------------)

7 min read

·

21 hours ago

--

Listen

Share

Press enter or click to view image in full size

![]()

**Difficulty:** Beginner-Friendly | **Category:** Web Exploitation

Hello everyone

I'm Chetan Chinchulkar (aka **omnipresent**), and we're switching gears! After conquering two OSINT challenges ([*the wooden duck mystery*](/from-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8) and [*the Among Us university*](https://medium.com/%40omnipresent_/00bba5775179)), it’s time to dive into **web exploitation**.

Now, before you imagine me typing furiously with a hoodie on in a dark room (okay, maybe that’s accurate sometimes 😅), let me tell you about a challenge that taught me an important lesson: **sometimes the best hacking technique is just knowing how to read.**

## The Challenge: Login Panel

**Category:** Web Exploitation
**Points:** 100
**Description:** Simple login panel
**URL:** <https://tommytheduck.github.io/login>

**What we got:** A URL leading to a login prompt. That’s it. No hints, no files, just a login form staring back at me.

When I first opened this challenge, I thought, “Alright, time to break out the big guns — SQL injection, XSS, brute force…” But then I remembered something my mentor once told me:

> “Before you try to break in through the window, check if the door is unlocked.”

Wise words. Let’s see how they applied here.

## My Approach: From Brute Force Dreams to Reality Checks

## Step 1: The Classic Default Credentials Dance

Look, I know it’s 2025 (well, almost 2026), but you’d be *shocked* how often default credentials still work. So naturally, my first move was trying the classics:

* `admin:admin` ❌
* `admin:password` ❌
* `user:user` ❌
* `user:password` ❌ (had to try it)

**Result:** Nope, nope, and more nope.

Okay, so the challenge creator wasn’t *that* generous. Fair enough. Time to dig deeper.

## Step 2: View Page Source (The Underrated MVP)

Here’s something I’ve learned from CTFs: **View Page Source is your best friend in web challenges.** It’s like the metadata check of OSINT — you always do it, even when you think it won’t help.

I right-clicked, hit “View Page Source,” and there it was — the entire login logic laid bare in beautiful, unobfuscated JavaScript.

Press enter or click to view image in full size

![]()

**My immediate reaction:** “Wait… they just… left the hashes in the source code? In *client-side* JavaScript?”

Yes. Yes, they did. And honestly? This is more common in real-world applications than you’d think

## Step 3: Understanding the Code (Reading Comprehension FTW)

Let me break down what this code is doing, because understanding is half the battle:

1. **Takes user input** — Username and password from prompt boxes
2. **Hashes them** — Uses SHA-256 to hash both inputs
3. **Compares hashes** — Checks if your hashed inputs match the hardcoded hashes
4. **Reveals the flag** — If they match, alerts the flag in format `username{password}`

**Key observations:**

* The hashing algorithm is **SHA-256** (clearly stated in the code)
* The username hash: `ba773c013e5c07e8831bdb2f1cee06f349ea1da550ef4766f5e7f7ec842d836e`
* The password hash: `48d2a5bbcf422ccd1b69e2a82fb90bafb52384953e77e304bef856084be052b6`
* The flag format is literally given: `username{password}`

So now the challenge becomes: **crack these SHA-256 hashes.**

## Step 4: Hash Cracking (Or: Why Rainbow Tables Exist)

Now, I *could* fire up Hashcat and start a brute force attack. Set up a wordlist, configure the hash mode for SHA-256, let my laptop fan scream for a while…

**Or…**

I could check if these hashes are already cracked and sitting in an online database. Because let’s be real — if the challenge creator used common passwords (and they usually do for beginner challenges), someone’s already cracked them.

I headed over to [**CrackStation**](https://crackstation.net/), pasted both hashes, and hit “Crack Hashes.”

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

**Boom! 💥**

* Username hash → `v1t`
* Password hash → `p4ssw0rd`

**Fun fact:** The password is literally “password” with leetspeak. Classic CTF move. I respect it.

## Step 5: Assembling the Flag

Remember the flag format from the code?

```
alert(username + '{' + password + '}');
```

So: `v1t` + `{` + `p4ssw0rd` + `}`

## The Flag

```
v1t{p4ssw0rd}
```

**Submitted. Accepted. Web challenge conquered! 🎉**

## What This Challenge Taught Me

### 1. Client-Side Security Is Not Security

Storing credentials (even hashed ones) in client-side JavaScript is a massive security flaw. Anyone can view the source code and extract sensitive information. This challenge is a perfect example of what *not* to do in real-world applications.

**Real-world lesson:** Always validate and authenticate on the server-side, never trust the client.

### 2. Reading > Tools (Sometimes)

I could’ve gone straight to automated tools, but taking 2 minutes to read and understand the code saved me time and gave me the exact information I needed. In CTFs and real pentesting, understanding the logic is often more valuable than throwing tools at the problem.

### 3. Rainbow Tables Are Your Friend

Services like CrackStation maintain massive databases of pre-computed hashes. For common passwords, they’re instant. For CTF challenges, they’re often all you need.

**When to use what:*...