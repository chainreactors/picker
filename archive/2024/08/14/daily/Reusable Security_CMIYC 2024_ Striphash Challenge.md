---
title: CMIYC 2024: Striphash Challenge
url: https://reusablesec.blogspot.com/2024/08/cmiyc-2024-striphash-challenge.html
source: Reusable Security
date: 2024-08-14
fetch_date: 2025-10-06T18:03:02.174329
---

# CMIYC 2024: Striphash Challenge

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### CMIYC 2024: Striphash Challenge

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[August 12, 2024](https://reusablesec.blogspot.com/2024/08/cmiyc-2024-striphash-challenge.html "permanent link")

[![An AI generated image of a kitten in a top hat sitting on a computer and playing with letter blocks](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEVSF7lA3rqSdT8tbHlyl_K-pAEsRMZ_veGJ1_akjddgl4IV93AVDFYvbS8X3xAD2iDfaAVdb7DqucDSixYADEjLsiJq1sK5gSzOs4yJ2WJ4xLp1Mi2v8J8jNZLQbob7Baayk-LEWJ6CU3prvi2pNy-9quzoJJo8VXgOZnSM2p1LIrCFaqWrm1DhNq2Pw/s16000/cmiyc2024_banner1.webp "I tried to get Midjourney to spell out Korelogic on the blocks, but totally failed")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEVSF7lA3rqSdT8tbHlyl_K-pAEsRMZ_veGJ1_akjddgl4IV93AVDFYvbS8X3xAD2iDfaAVdb7DqucDSixYADEjLsiJq1sK5gSzOs4yJ2WJ4xLp1Mi2v8J8jNZLQbob7Baayk-LEWJ6CU3prvi2pNy-9quzoJJo8VXgOZnSM2p1LIrCFaqWrm1DhNq2Pw/s831/cmiyc2024_banner1.webp)

> ***"I can accept failure. Everyone fails at something. But I can't accept not trying.***"

> **- Michael Jordan**

# Introduction:

First off, I really want to thank the team over at Korelogic for putting together a truly impressive contest. Korelogic always uses the CMIYC contest to push for change/improvements in password cracking tools and this event in particular was jam packed with different challenges that forced teams to really stretch their skills vs. letting their GPUs go Brrrrrrrrrrrr.

Second, I'd like to compliment the skill shown by all the players. One thing Korelogic mentioned after the contest was that the Street challenges were the same level of difficulty as those given to the Pro teams. Looking at the scoreboard and seeing street teams succeed like they did highlights the the level of ability on display. As far as the number of players who just popped on to learn something new, that's also impressive  There's a ton of stuff going on during Defcon and the fact that someone decided to try their hand at a password cracking competition vs. one of the other million neat things happening is really special.

One thing that really struck me about this year's CMIYC competition was the amount of content in it. In past years I felt like I had a chance to really experience about 50-70% of the contest (the slow hashes always gave me a problem). This year I felt the number was closer to 10%. I'd see a new PCAP get dropped and go "Wow, that would be fun to decrypt. I'm sure it would give tips and/or new hashes to crack, but I have no free time to mess with that so moving on..." That's where having a blog is nice. I can revisit these challenges at my leisure, as well as incorporate lessons learned from other players' experiences and writeups. To that end I'm going to try and make a number of smaller blog posts focusing on individual aspects of the contest. Now there is going to be a lot of overlap since everything is related, but hopefully this can keep things more manageable for me so that I actually post something vs. having an entry sit in my draft folder for the next several years.

## Important Links, Tools, and References for this Post:

* **My JupyterLab Password Cracking Framework**

+ **Link:** <https://github.com/lakiw/Jupyter-Password-Cracking-Framework>
+ **Reason:** This contest was the first time I really got to use the Jupyter Lab Password Cracking Framework in real time during a competition. While there were a lot of rough spots, it proved very helpful for dealing with the Radmin and Striphash challenges. A lot of the code I'm going to show in this blog entry is a screenshot from the tool which you can download. My apologies for not including text, but I don't know of a way to reliably render code blocks in Google blogger. Long story short, being able to download, run, and view the JupyterLab notebooks will help add context around a lot of the items discussed in this blog post.
+ **Disclaimer:** I need to clean my Notebooks from the contest up before I push them to Github. So it may be a week or so before I actually update the repo with the examples I'm showing here.

* **Example Hashcat Formatted Hashes**

+ **Link:**<https://hashcat.net/wiki/doku.php?id=example_hashes>
+ **Reason:** You really should have this page bookmarked regardless of if you are competing in a competition or not. Whenever I'm starting a non-standard password cracking session I find myself referring back to this site to try to figure out what type of hash I'm dealing with, or to understand how I need to format it so I can crack it with Hashcat.

* **Example John the Ripper Formatted Hashes**

+ **Link 1:** <https://openwall.info/wiki/john/sample-hashes>
+ **Link 2:** <https://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats>
+ **Reason:** Just like with Hashcat, it's helpful to have some examples when trying to crack newly encountered hash formats in John the Ripper. These sites are a bit harder to read and search than Hashcat's site, but they are still a super helpful resource.

* **Korelogic Score Page**

+ **Link:** <https://contest-2024.korelogic.com/stats.html>
+ **Reason:** This was how I figured out what hash types were being provided to us to crack

* **ADSync Hash Format**

+ **Link:** <https://aadinternals.com/talks/Attacking%20Azure%20AD%20by%20abusing%20Synchronisation%20API.pdf>
+ **Reason:** Not super applicable to these challenges, but I wanted to put it here so I won't forget about it when talking about cracking ADSync hashes later.

* ThatOnePasswordWas40Passwords CMIYC2024 Writeup:

+ **Link:** <https://github.com/ThatOnePasswordWas40Passwords/crackmeifyoucan/tree/main/2024>
+ **Reason:** An excellent writeup by the winner of this year's Street competition. I highly recommend checking it out. I'm certainly still going through it and trying to learn from their experiences!

## Loading the Mixed Hash Lists:

**Description of Hash Lists:**

At the start of the contest Korelogic provided two PGP password encrypted files as well as the decryption password. The first file, cmiyc-2024\_street\_passwd\_1, was a standard mixed hash list consisting of various different hash types in the general format:

* username:hash

The hashes themselves were not identified so it was up to players to figure out what hash format they were targeting. Admittedly you can often let your cracking tool autodetect hash formats, but like everything this contest provided some "twists" which meant you couldn't just rely on your password cracker's autodetect feature.

The second challenge file was a PGP password encrypted tar file, which Korelogic also provided the password for. This tar file contained a number of different encrypted hint files as well as a Windows registry entry containing Radmin password hashes. For now though, let's focus on the first mixed hash list.

**Identifying Hash Types and Loading Them In the Framework:**

One quick way to know what hash formats might show up in that mixed hash list is to simply look at the Korelogic scoreboard. There they listed a number of different formats:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0z_1n6fFFM-x5tRvsHrp-3UCEVwS3D1DeeLVwOZEfBELF7YQ9mweJ4v9b8uQ1bTriTB06TrBa83LURjzUclQh5fNp8M7KW0RovJTxCNg-d8ZHyThB7ZS1rG6NJ4CVpul2du6eyJULiAXWyLqfM_rpZgC09p6VT-m5RL7IP8uMOUVI6-AS0ddDH2kYSk8/w300-h400/score_value.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0z_1n6fFFM-x5tRvsHrp-3UCEVwS3D1DeeLVwOZEfBELF7YQ9mweJ4v9b8uQ1bTriTB06TrBa83LURjzUclQh5fNp8M7KW0RovJTxCNg-d8ZHyThB7ZS1rG6NJ4CVpul2du6eyJULiAXWyLqfM_rpZgC09p6VT-m5RL7IP8uMOUVI6-AS0ddDH2kYSk8/s525/score_value.png)

I'll admit while some of these formats were familiar, a lot of them such as striphash, radmin3 and adsync I've never rea...