---
title: Analyzing Tokenizer Part 2: Omen + Tokenizer
url: https://reusablesec.blogspot.com/2024/12/analyzing-tokenizer-part-2-omen.html
source: Reusable Security
date: 2024-12-06
fetch_date: 2025-10-06T19:38:27.617266
---

# Analyzing Tokenizer Part 2: Omen + Tokenizer

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Analyzing Tokenizer Part 2: Omen + Tokenizer

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[December 04, 2024](https://reusablesec.blogspot.com/2024/12/analyzing-tokenizer-part-2-omen.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLT0GotZCs7NZD_e9nrKKOYLJ3z0jqeuxUJRgR1ywztJ8KJQu_Jh_Nd3I3WM2GQQaua3GuF1d5v_7p1KOIVOVaVcVoY82sBdw94Fhc6VLE6IABYhaCwPExZAb-8pJ0bvoLdaQxuI5Av64A6C0AH4hVnU5u3VwHSkrgfzU05k8ftK4PWaU08D0348iC20w/w640-h344/sleeping_cat2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLT0GotZCs7NZD_e9nrKKOYLJ3z0jqeuxUJRgR1ywztJ8KJQu_Jh_Nd3I3WM2GQQaua3GuF1d5v_7p1KOIVOVaVcVoY82sBdw94Fhc6VLE6IABYhaCwPExZAb-8pJ0bvoLdaQxuI5Av64A6C0AH4hVnU5u3VwHSkrgfzU05k8ftK4PWaU08D0348iC20w/s1488/sleeping_cat2.png)

> ***“I have not failed. I've just found 10,000 ways that won't work”***

> **-*****Thomas Edison***

# Introduction:

This is a continuation of a deep dive into John the Ripper's new Tokenizer attack. Instruction on how to configure and run the original version of Tokenizer can be found [[Here](https://reusablesec.blogspot.com/2024/10/running-jtrs-tokenizer-attack.html)]. As a warning, those instructions need to be updated as a new version of Tokenizer has been released that makes it easier to configure. The first part of my analysis can be found [[Here](https://reusablesec.blogspot.com/2024/10/running-jtrs-tokenizer-attack.html)].

This is going to be a bit of a weird blog entry as this is a post about **failure**. Spoiler alert: If you are reading this post to learn how to crack passwords, just go ahead and skip it. My tests **failed**, my tools **failed**, and my understanding of my tools **failed**. A disappointing number of passwords were cracked in the creation of this write-up. I'll admit, I was very tempted to shelve this blog post. But I strongly believe that documenting **failures** is important. Often when reading blog posts you don't really see the messy process that is research. Stuff just doesn't work, error messages that are obvious in retrospect are missed, and tests don't always turn out the way you expect. So as you read this, understand that it's more a journal of troubleshooting research tests when they go wrong, vs. a documentation of what to do.

To put it another way, the main audience for this blog post is:

* **My future self.** I'm really annoyed at myself for not better documenting some of my past work. I'll go into that in more detail later.
* **Password cracking tool developers.** This post won't help you crack more passwords or develop better password security strategies. Hopefully it will help those who are developing the tools to help you crack those passwords though.
* **People who play dwarf fortress and like [[Fun](https://dwarffortresswiki.org/DF2014%3AFun%26redirect%3Dno)]**.

## Question 1: Why are my Tokenizer's "first 25 guesses" different from Solar Designer's

**Background:**

In response to my previous blog entry, Solar Designer wrote: "One thing that surprised me is that your top 25 for training on RockYou Full (including dupes, right?) is different from what I had posted in here at all (even if similar)." [[Link](https://www.openwall.com/lists/john-users/2024/11/18/3)].

That's a good question, and one that I had been wondering as well. There's a couple of things that could be causing this, from the way our Linux shells handle character encoding, the order of our training lists, to differences in our training lists. Or it could be something totally different that I'm not imaginative enough to come up with yet. At a high level, it's probably not that big of a deal since our experiences running Tokenizer attacks seem roughly the same (Solar Designer has posted tests comparing it to Incremental mode, and they roughly match what I've been seeing). But this can be a useful rabbit hole to dive down since it can expose some optimizations or environmental issue that could cause problems as more people start to use this tool. There's a big gulf between "it works on my machine" and "its easy for anyone else to run".

**Conclusion Up Front:**

Tokenizer (and base-Incremental mode) seem resilient to the order of the passwords they are trained on, and setting  '**export LC\_CTYPE=C**' did not seem to impact guess generation.

**Bonus Finding:**

When manually analyzing password guesses **DO NOT** pipe the output of a password cracking session into "**less**". At least in my WSL Ubuntu shell, this seemed to add artifacts into the guesses I was creating which gave me bad data. Note, This doesn't impact running actual password cracking sessions.

Instead, when using John the Ripper, make use of the "**--max-candidates**" option. Aka:

* ./john --incremental=tokenize1 --external=untokenize1 --stdout **--max-candidates=25**

**Discussion**

This was an area where my analysis setup really let me down so I chased a lot of unproductive leads before I was able to find the ground truth. For my first test I sorted Rockyou1 and compared a Tokenizer attack trained on it to a Tokenizer attack trained on an unsorted Rockyou1 training set. Initially they appeared to generate different guesses. For example:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrbVlLBNIK84wgirG5h6tflQaQkLNj19cc6i-TRIjW4VV2d52dPtipWz9NlsmyYpqy6Z0RzDIQEZRsauXgYeF2JH5J_ciW5RdSwOyAkLo6nvAYLc9LkpHGlkXHEEdhfGP8jz2B9kKRdzbcG-ZIkoGUCB_YDOg2ylH80ZkZoEKAdhsveTyEW9OJbvfZj8s/s16000/Problems_with_less.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrbVlLBNIK84wgirG5h6tflQaQkLNj19cc6i-TRIjW4VV2d52dPtipWz9NlsmyYpqy6Z0RzDIQEZRsauXgYeF2JH5J_ciW5RdSwOyAkLo6nvAYLc9LkpHGlkXHEEdhfGP8jz2B9kKRdzbcG-ZIkoGUCB_YDOg2ylH80ZkZoEKAdhsveTyEW9OJbvfZj8s/s1166/Problems_with_less.png)

This led down an unproductive rabbit hole where I ended up generating a lot of different character sets for Incremental mode to try and track down what was causing the differences in guess generation. It wasn't until I got really frustrated and ran a "diff" on the different .chr files that Incremental mode uses and found they were EXACTLY THE SAME that I realized the problem might be in how I was displaying the guesses.

Still, I learned a few new things, and improved my testing process. So it wasn't a complete waste.

## Question 2: How does the PCFG OMEN mode attack differ from the original Rub-SysSec version?

**Background:**

This question was inspired by a comment by @justpretending on the Hashcat Discord channel.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn4n6w0TxJG8UF5pnsDyM8797CnIoZX54fIUr5Kxse5BO_TFHXNFPjLWW7PL5snKWnvLixuh2kPW8I4_sN7vJkUbIauKMcA8fE9tDQQyFJmVpVxh9NVERlsqe72PHTY5CppSud3osGA06dpWViH-EE5zlMPjiXdxqnkjfYLRKJv30kd7nX3xQZwMXM-xg/s16000/omen_modes_discord.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn4n6w0TxJG8UF5pnsDyM8797CnIoZX54fIUr5Kxse5BO_TFHXNFPjLWW7PL5snKWnvLixuh2kPW8I4_sN7vJkUbIauKMcA8fE9tDQQyFJmVpVxh9NVERlsqe72PHTY5CppSud3osGA06dpWViH-EE5zlMPjiXdxqnkjfYLRKJv30kd7nX3xQZwMXM-xg/s2156/omen_modes_discord.png)

OMEN stands for Ordered Markov ENumerator and the original paper/implementation can be found [[Here](https://github.com/RUB-SysSec/OMEN)]. I became interested in it after it was presented at PasswordsCon where it was shown to be more effective than my PCFG attack and could generate guesses at speeds making it practical. That's certainly one way to get my attention! To better understand the OMEN attack I took the Rub-SysSec OMEN code and re-implemented it in Python. The standalone version of the python code (py-omen) is still available [[Here](https://github.com/lakiw/py_omen)]. Liking what I saw, I then replaced the existing Markov attack (based on JtR's --Markov mode) in the PC...