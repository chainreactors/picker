---
title: OMEN Improvements
url: https://reusablesec.blogspot.com/2025/08/omen-improvements.html
source: Reusable Security
date: 2025-08-11
fetch_date: 2025-10-07T00:17:13.861562
---

# OMEN Improvements

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### OMEN Improvements

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[August 09, 2025](https://reusablesec.blogspot.com/2025/08/omen-improvements.html "permanent link")

> ***“If I had an hour to solve a problem, I would spend 55 minutes thinking about the problem and five minutes finding the solution.”***

> **-*****Proverb falsely attributed to Albert Einstein***

# Introduction:

I'm a big fan of graphing password cracking sessions. It's a good way to figure out what's working and what isn't by highlighting trends that get lost in the final "cracking success" number. The very first thing I look for in these graphs is saw-tooth steps. This is an easy way to spot potential improvements. If you suddenly see a quick run of cracks in your password cracking success rate, which is what these saw-tooth steps represent, that implies you can optimize your cracking session by moving that attack earlier in your workflow. Now you need to temper that with the realization that no two password sets are exactly the same, you don't want to overtrain your cracking sessions on one particular dataset, and often these improvements come about because you learn some target specific information part-way through your cracking session. But all that being said, these saw-tooth steps are a great place to start your investigations.

These saw-tooth steps are very evident in the current OMEN cracking sessions as you can see in the graph below. This post will cover my investigation into making OMEN better based on these observations. But if you take anything away from this post, it's really that you should graph your cracking sessions, (ideally using a linear and not logarithmic scale), as chances are it will help you optimize your cracking techniques as well.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNhzcLReqZcsC5a4zPx2S_hMirG-AqUO6Bmg-gEfw3S3VYwNSrPjc511vry_n4Cji6TTLCW_qyg3ygSK1tYv-4SP0mrW_EvADpKfE70JRQrfAbrOPExjL7P-GmhJPxQBNjbhdtS9NfMBwhWO9I06pJLZPV3iOSE71lv9PvePdJRlEtCfry1jt0F3uAa6E/s16000/image.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNhzcLReqZcsC5a4zPx2S_hMirG-AqUO6Bmg-gEfw3S3VYwNSrPjc511vry_n4Cji6TTLCW_qyg3ygSK1tYv-4SP0mrW_EvADpKfE70JRQrfAbrOPExjL7P-GmhJPxQBNjbhdtS9NfMBwhWO9I06pJLZPV3iOSE71lv9PvePdJRlEtCfry1jt0F3uAa6E/s903/image.webp)

# OMEN Background:

At a high level OMEN is simply another Markov based password guess generator. What makes it stand out from other Markov approaches though is in how it calculates probability thresholds for generating guesses. Rather than ordering likely "next characters" in an array or queue and selecting the next most likely option (such as Hashcat's Markov or "roughly" like JtR's Incremental), or multiplying probabilities together and using a probability threshold (like JtR's --Markov option), OMEN instead assigns each transition a "cost" between 0-10, and then allocates a total "guessing budget" for generating guesses based on the current "level" it is at. So for an OMEN level 4 guess, it would have a "budget" of 4 it needs to spend on all the transitions when creating a guess. The nice thing about this is that when calculating an OMEN guess, you only need to do integer addition. This is a huge bonus from a speed perspective since multiplying floats (like JtR's Markov) is expensive. This approach also gives you much more granular control about the different probability costs associated with a transition compared to using an array based ranking which is what Hashcat does.

The key thing to keep in mind are there are 4 items that OMEN can spend its budget on, of which 3 are currently in use:

* **Initial Probability (IP)**: This is the first N-1 characters to start a password guess with.

+ If you have a NGram length of 4, this is the first 3 characters of your password guess.
+ The IP is trained from the start of all passwords in the training set
+ Because the IP isn't trained on the full password, there tends to be a lot of gaps. For example, when trained on a 1 million subset of RockYou with the default alphabet of 72 characters, the total keyspace would be around 373k lines, but the OMEN IP list only contains roughly 90k lines.

* **Length (LN):** The total length of the password guess

+ OMEN prioritizes guesses based on their length so if a password guess has a "non-standard" length it is penalized with a higher cost.
+ The reason I want to highlight this is because **\*\*Spoiler\*\*** this is where some of the improvements can be made in the standard OMEN algorithm.

* **Conditional Probability (CP):** This is the likelihood of the "next" character appearing.

+ For example if the previous three characters are "que", the CP cost of the next letter being '[e,s]' might be 0, and the next letters being '[a,n]' might have a CP cost of 1.

* **End Probability (EP) (NOT USED):** The probability of the last couple of characters in a password

+ Note: Neither the Rub-SysSec or Py-OMEN currently use EP even though both the tools still calculate it. This is because testing revealed using EP makes the guesses significantly worse. I know that sounds counter-intuitive, but that's why we run tests!

# OMEN Investigation:

To better investigate OMEN attacks, there are three repos I'll be using:

* **Py-OMEN:** A python implementation of the Rub-SysSec OMEN attack

+ **Link:** <https://github.com/lakiw/py_omen>
+ **Comments:** I've been fixing this up so it actually works. This is the same algorithm as the OMEN implementation in the PCFG toolset but it is standalone without any of the other PCFG code. So if you are running real cracking sessions I'd still recommend using the PCFG toolset instead, but this standalone version is easier to work with when investigating improvements to OMEN.

* **Password Research Tools:** Allows graphing and investigating the effectiveness of password attacks.

+ **Link:** <https://github.com/lakiw/Password_Research_Tools>
+ **Comments:** After many years, I'm also updating this toolset to add a few more features. Specifically I can send it debug statements from my guess generator and it'll include when in the guessing process the statement was outputted. This is helpful for investigating when OMEN levels change. All graphs here are generated using that tool + Excel.

* **Pretty Cool Fuzzy Guesser (PCFG):** My main password guess generating toolset.

+ **Link:** <https://github.com/lakiw/pcfg_cracker>
+ **Comments:** Hey, if I'm going to make an improvement in how guesses are generated, of course I'm going to use that to upgrade my main toolset!

The first thing I did when investigating the saw-tooths in OMEN attacks was to run a cracking session and save all the **CRACKED** passwords to file as well as collect data for my graphs. That way when I wanted to dig into a particular run of cracked passwords from looking at the graph I can see what those passwords are. An example cracking session can be seen as follows:

* python3 enumNG.py -r mod\_rockyou1 | python3 ../Password\_Research\_Tools/checkpass.py -m 1000000000 -t ../../research/password\_lists/rockyou/rockyou\_32.txt --cracked\_file rockyou1\_vs\_rockyou32.cracked

**Note:** You can also do something similar with Hashcat giving it the flag "**--outfile-format=2,4**" which will output the plaintext password followed by the guess number. Another option to make parsing easier is to save the hex\_plain vs. the raw plaintext using the flag "**--outfile-format=3,4**". This can be annoying as it requires the extra step of decoding the plaintext password to do any manual analysis, but that's often a lot less annoying than dealing with parsing issues.

**Hashcat Feature Request: (NOTE: This may be outdated since the new version of Hashcat has a ton o...