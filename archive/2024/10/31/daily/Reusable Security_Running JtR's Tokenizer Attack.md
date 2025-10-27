---
title: Running JtR's Tokenizer Attack
url: https://reusablesec.blogspot.com/2024/10/running-jtrs-tokenizer-attack.html
source: Reusable Security
date: 2024-10-31
fetch_date: 2025-10-06T18:53:08.425615
---

# Running JtR's Tokenizer Attack

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Running JtR's Tokenizer Attack

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[October 29, 2024](https://reusablesec.blogspot.com/2024/10/running-jtrs-tokenizer-attack.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJaKbqa6YaCWitjU5BcXz9W2ALnRN_cdAIEV27_Jk9T1GP1fnjPX0vKdmXaXAq0ZzgwfCa8pbWVmZ-QFnAOxvpXCtYL3B4M4EvDyptRPzfJTBAhNd5DqJ3FlNupD2fKpaqBSfe-bcDl-bPRmAvcLdV5PYlZmwMdLDulh04mClWlbZBfxkBnIZfLuo_B2s/s16000/title_tokenize.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJaKbqa6YaCWitjU5BcXz9W2ALnRN_cdAIEV27_Jk9T1GP1fnjPX0vKdmXaXAq0ZzgwfCa8pbWVmZ-QFnAOxvpXCtYL3B4M4EvDyptRPzfJTBAhNd5DqJ3FlNupD2fKpaqBSfe-bcDl-bPRmAvcLdV5PYlZmwMdLDulh04mClWlbZBfxkBnIZfLuo_B2s/s1083/title_tokenize.webp)

**Disclaimer 1:** This blog post is on a new and still under development toolset in John the Ripper. Results depict the state of the toolset as-is and may not reflect changes made as the toolset evolves.

**Disclaimer 2:** I really need to run some actual tests and password cracking sessions using this attack, but I'm splitting that analysis up into a separate blog post. Basically I have enough forgotten drafts sitting in my blogger account that I didn't want to add another one by trying to "finish" this post before hitting publish. So stay tuned for new posts if you want to see how effective this attack really is.

## Introduction:

It's been about 15 years since I last wrote about John the Ripper's Markov based Incremental mode attacks [[Link](https://reusablesec.blogspot.com/2009/11/analysis-of-10k-hotmail-passwords-part.html)] [[Link 2](https://reusablesec.blogspot.com/2010/01/analysis-of-10k-hotmail-passwords-part.html)]. 15 years is a long time! A lot of work has been done applying Markov based attacks to password cracking sessions, ranging from the OMEN approach to Neural Network based password crackers. That's why I was so excited to see a new proof of concept (PoC) enhancement of JtR's Incremental mode that was just published by JtR's original creator SolarDesigner.

The name of this enhancement is likely going to change over time. Originally it was described in an e-mail thread as "Markov phrases". That's not a bad descriptor, but doesn't really get to the heart of the current PoC. Therefore in this blog post I'm going to call this attack after the new script SolarDesigner released (tokenize.pl) and just refer to it as a "Tokenizer Attack". I think this  gets closer to conveying how the underlying enhancement differs from the original Incremental attack which the tokenizer attack is built on.

The next question of course is "What does this new enhancement do?" To take a step back, what make Markov attacks "Markovian" is they represent the conditional probability of tokens appearing together. For example, if you see the letter '**q**' in an English word, the next letter is very likely to be a '**u**'. How far you look ahead to apply this probability is measured by the "order" of the Markov chain. So the above example would describe a first-order Markov process. If we extended this and said that given a '**q**' and then a '**u**', the next most likely character would be a '**e**', now we are talking about a second-order Markov process. Where this starts to play out compared to a first-order process is that **'qu' -> 'e'** with a high probability but the highest probability next character for the substring **'tu**' might be **'r'**.  Therefore the highest probable letter following a '**u**' might change based on the letter before the '**u**' Basically the order represents the "memory" of the Markov chain. It can remember X previous tokens of the string it is generating.

The reason I bring this up is that JtR's Incremental mode works with trigraphs which "roughly" can be represented by second-order Markov processes. I use "roughly" since like most Markov implementations, Incremental mode contains nuances and differences from the abstract/academic definition of Markov based processes. Those nuances aren't super important for this current investigation/blog-post so I'm going to gloss over them for now.

One interesting area of research is implementing "variable order" Markov processes. Aka some particularly likely substrings might be created by a third/fourth/fifth/sixth order Markov process, but other less likely transitions might be implemented in a lower order (first/second) Markov process. As an example of that, if you were using a second order Markov chain the initial letters '**or**' might generate a next letter of '**k**' with a high probability, but if you take a larger step back and see the earlier letters are '**passwor**' then the next letter will almost certainly be a '**d**' instead. Based on this, it's tempting to "apply the largest memory possible" to your Markov processes. The limiting factor though is if you extend things out too much you run into overtraining issues, not being able to generate substrings not seen in the training data, and general implementation issues (the size of your Markov grammar explodes). So being able to dynamically switch how much memory/state you are keeping track of can be very helpful when generating password guesses. While more research is needed, this is my current theory why the CMU Neural Network Markov based attacks [[Link](https://github.com/cupslab/neural_network_cracking)] outperform other Markov implementations. I strongly suspect the Neural Network makes use of a variable order Markov process when generating guesses.

That's a lot of words/background to say that JtR's Tokenizer attack can be thought of as a way to incorporate variable length Markov orders into JtR's current Incremental mode attack. It does this by identifying certain likely substrings (aka "tokens") and then replacing them in the training set with a "placeholder" character. So for example the likely substring "love" might be replaced with the hex value of x15. This would normally be an unprintable character in ASCII ([NAK](https://www.ascii-code.com/)), but it allows JtR's normal Incremental mode charset to be trained using these replacements. The resulting Incremental charset will have probability information for generating the character "**x15**" (NAK) as part of a password guess. Now (NAK) isn't actually part of a real password (unless the user did something really cool). This means when running a password cracking session, you'll need to then apply an External mode to translate these guesses back into the full ASCII text outputs. For example the guess "I(x15)MyWife" would be translated by the External mode into "IloveMyWife" which can then be fed into a real password cracking session.

While I can certainly dive more into the details of the tokenizer attack, this intro is already too long. So lets instead look at how to run it!

## References:

* Post by SolarDesigner announcing the release of the tokenize.pl script: [[Link](https://www.openwall.com/lists/john-users/2024/10/27/1)]
* John the Ripper Bleeding Edge: [[Link](https://github.com/openwall/john/tree/bleeding-jumbo)]

## Configuring The Attack:

#### 1) Update JtR Bleeding Edge:

* The new code, (including tokenize.pl) is available in the newest version of JtR Bleeding Jumbo.
* To make use of it, clone the gihub repository and make sure you are on the "bleeding-jumbo" branch which is the default. [[Link](https://github.com/openwall/john/tree/bleeding-jumbo)]
* (Optional) Rebuild JtR from source.

+ This is optional since the new code "should" work with older versions of JtR. But you might want to rebuild JtR to be on the safe side.

#### 2) Create a Custom Incremental .CHR File:

* **Run the new tokenize.pl script on your training passwords.**

+ **No...