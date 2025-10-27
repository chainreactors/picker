---
title: Analyzing JtR's Tokenizer Attack (Round 1)
url: https://reusablesec.blogspot.com/2024/11/analyzing-jtrs-tokenizer-attack-round-1.html
source: Reusable Security
date: 2024-11-18
fetch_date: 2025-10-06T19:14:19.337975
---

# Analyzing JtR's Tokenizer Attack (Round 1)

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Analyzing JtR's Tokenizer Attack (Round 1)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[November 17, 2024](https://reusablesec.blogspot.com/2024/11/analyzing-jtrs-tokenizer-attack-round-1.html "permanent link")

# [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD_dEl1BAM2hPt6wFL_MakWAGFnu5rdoTREK63zbfB770GJNdZAFYLGdGDHgpjlvHHhsCLKm6if1Fu2iDw8u8JOcSeoU2KbdPlaxCWFuz7kJamDGFmLpR1mkOS1maDzxBgQR7Zg6QWIaenljrTfslYgXtc2lIamLsw34MVaFnvz3LAlheIGLQGZU1fd6w/s16000/cat_computer.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD_dEl1BAM2hPt6wFL_MakWAGFnu5rdoTREK63zbfB770GJNdZAFYLGdGDHgpjlvHHhsCLKm6if1Fu2iDw8u8JOcSeoU2KbdPlaxCWFuz7kJamDGFmLpR1mkOS1maDzxBgQR7Zg6QWIaenljrTfslYgXtc2lIamLsw34MVaFnvz3LAlheIGLQGZU1fd6w/s1100/cat_computer.webp)

# Introduction / Goals / Scope:

This is a follow-up to my previous blog post looking at how to install/run the new John the Ripper Tokenizer attack [[Link](https://reusablesec.blogspot.com/2024/10/running-jtrs-tokenizer-attack.html)]. The focus of this post will be on performing a first pass analysis about how the Tokenizer attack actually performs.

Before I dive into the tests, I want to take a moment to describe the goals of this testing. My independent research schedule is largely driven by what brings me joy. Because of that I'm trying to get better at scoping efforts to something I can finish in a couple of days. It's easy to be interested in something for a couple of days! Therefore, my current plan is to run a couple of tests to get a high level view of how the Tokenizer attack performs and then see where things go.

To that end, this particular blog post will focus on three main "tests" to answer a couple of targeted questions.

**Test 1: Analyze how sensitive Tokenizer is to the size of the training data**

* **Question:** How sensitive is the Tokenizer attack to being trained on 1mil, or 30+ mil passwords?
* **Impact:** Knowing this is important since it determines if the Tokenizer attack can be effective when trained on smaller datasets. This could be a community or language specific target, or a dataset targeting a specific password creation policy.
* **Secondary Reason:** Identifying early on how sensitive Tokenizer is to the training size it will help inform other testing options I have available to me. For example can I train it on a subset of RockYou passwords, and then test it against a different subset from that same breach? Also, full disclosure, I made a mistake somewhere along the line of training the Tokenizer in my previous blog post that led me to think it was more sensitive to the training data size then it actually was.

**Test 2: Compare a short (5 billion guess)Tokenizer attack against Incremental and OMEN.**

* **Question:** How does the Tokenizer attack compare to other Markov based attacks?
* **Impact:** This will provide a quick gut check on if there is value in the tokenizer as-is or if this is more an academic tool to learn from. Aka should I start to incorporate it into my password cracking attacks now, or is it more like the neural network GAN attacks [[Link](https://arstechnica.com/information-technology/2023/04/the-passgan-ai-password-cracker-what-it-is-and-why-its-mostly-hype/)] which were interesting research and a basis to build upon, but are worse than current methods in every way?
* **Limits on Scope:**

+ I'm sticking to OMEN and Incremental since they are very similar attacks to tokenizer.
+ There absolutely are other attack types I could run, such as Hashcat's Markov, mask attacks, JtR's --Markov mode, PRINCE, etc. To address this, I'm going to use standard training/test datasets so that way you can compare these other attacks to the Incremental/OMEN results to extrapolate how they would perform compared to Tokenizer.
+ There are also a ton of variations of these attacks! For example I could use reduced character sets such as "lowernum" vs. just training on the full set of passwords in the training lists. I'm going to defer that type of experimentation for now and hopefully revisit it when digging into how to optimize cracking sessions.

**Test 3: Compare Tokenizer and CutB as Part of a Larger Password Cracking Session**

* **Question:** How does Tokenizer fit in with a larger password cracking session where various wordlist attacks have already been run?
* **Impact:** "Brute-Force" attacks like Incremental are usually run after wordlist attacks have been exhausted. Therefore it's important to understand how Tokenizer performs after all the "easy" passwords have already been cracked.
* **Note 1:** I'm going to be comparing Tokenizer against CutB since that is often used in a "throw the kitchen sink" sessions such as those in EvilMog's random ad-hoc methodology described [[here](https://github.com/evilmog/hashcat-scripts)].

# Tests:

**Note on Testing Tools:**

* The primary testing tool suite I'm using to analyze password cracking success is checkpass.py [[Link](https://github.com/lakiw/Password_Research_Tools)]
* Checkpass works using plaintext passwords and generates statistics about how effective a password cracking session is. I can then paste those statistics into Excel to generate graphs.
* When performing analysis on hashed passwords, this means I need to crack them first. This can be done in a couple of different ways:

+ If I've performed a lot of password cracking on the list before and have it at around 96% success rate I can generally use those plains without having to worry too much about the 4% of uncracked passwords
+ I can also download wordlists from hashmob [[Link](https://hashmob.net/resources/hashmob)] that will often achieve a high success rate since most of the lists I deal with are already on hashmob's public cracking targets.
+ Finally, I can simply run the attacks I'm analyzing twice, once as a real password cracking attack, and the second time against the plains using checkpass to make some nice graphs.

Below is an example of how I run checkpass.py and use that to generate these graphs. Note: Checkpass can also create a list of uncracked passwords. This is helpful since it lets me chain together different attacks to simulate more complex cracking sessions.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzVz6IyvTfNp6l7FjBvvu9Qjcq6aHopTxhww26WSmU3hIk8kcW2dUPNDeUUOK9HzegFYwA0df88ZI5LbssjlzJtyWCBvggivvHQdiQi_Bal9RYDSOf7H8Z3meMq6-9VRZRVzdxiAHPicuAGPnTLn9zHnmlspiICCrzNhZIQcS1hWpqfKDYgvgZn3vWHQc/s16000/checkpass.png "Spoiler Alert!")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzVz6IyvTfNp6l7FjBvvu9Qjcq6aHopTxhww26WSmU3hIk8kcW2dUPNDeUUOK9HzegFYwA0df88ZI5LbssjlzJtyWCBvggivvHQdiQi_Bal9RYDSOf7H8Z3meMq6-9VRZRVzdxiAHPicuAGPnTLn9zHnmlspiICCrzNhZIQcS1hWpqfKDYgvgZn3vWHQc/s2145/checkpass.png)

## **Test 1: Analyze how sensitive Tokenizer is to the size of the training data**

**Training: RockYou**

**Note on RockYou Dataset:** The RockYou dataset contains duplicate passwords as well as all the encoding weirdness found in the original dump. I randomized the order of the passwords in it to avoid any correlations between passwords present in the original dump, and split it into 32 1-million subsets to allow training/testing against different passwords.

* **Tokenize1:** Trained on a 1 million subset of RockYou
* **Tokenize2:** Trained on a different 1 million subset of RockYou
* **Tokenize\_Full:** Trained on the full set of 32 million+ RockYou passwords

**Testing: LinkedIn 2012 Data Breach**

**Notes on LinkedIn 2012 Dataset:**

* **Origin:** There are several different LinkedIn datasets from the 2012 Linkedin data breach [[Link](https://en.wikipedia.org/wiki/2012_LinkedIn_hack)]. For this test, I'm going to use the original du...