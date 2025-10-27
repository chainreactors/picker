---
title: The subtle art of jailbreaking LLMs
url: https://andpalmier.com/posts/jailbreaking-llms/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-18
fetch_date: 2025-10-06T19:15:16.675195
---

# The subtle art of jailbreaking LLMs

[↓Skip to main content](#main-content)

[andpalmier](/)

[Home](/)
[About](/about/)

* [Home](/)
* [About](/about/)

# The subtle art of jailbreaking LLMs

17 November 2024·15 mins

![andpalmier](/img/img_hu15764436753934245777.jpeg)

Author

andpalmier

cyber threat researcher, eternal noob, As Roma fan

Table of Contents

* [Introduction](#introduction)
* [LLMs basics](#llms-basics)
  + [Tokenization](#tokenization)
* [Jailbreaking LLMs](#jailbreaking-llms)
* [Common LLMs attack methods](#common-llms-attack-methods)
  + [Role-playing](#role-playing)
  + [Prompt Injection Attacks](#prompt-injection-attacks)
  + [Prompt rewriting](#prompt-rewriting)
    - [Language](#language)
    - [ASCII Art - ArtPrompt](#ascii-art---artprompt)
    - [Disguise and Reconstruction Attack (DRA)](#disguise-and-reconstruction-attack-dra)
  + [LLMs vs LLMs](#llms-vs-llms)
    - [Prompt Automatic Iterative Refinement (PAIR)](#prompt-automatic-iterative-refinement-pair)
    - [Iterative Refinement Induced Self-Jailbreak (IRIS)](#iterative-refinement-induced-self-jailbreak-iris)
  + [Token-Level Jailbreaking](#token-level-jailbreaking)
* [Conclusion](#conclusion)
* [Additional resources](#additional-resources)

Table of Contents

* [Introduction](#introduction)
* [LLMs basics](#llms-basics)
  + [Tokenization](#tokenization)
* [Jailbreaking LLMs](#jailbreaking-llms)
* [Common LLMs attack methods](#common-llms-attack-methods)
  + [Role-playing](#role-playing)
  + [Prompt Injection Attacks](#prompt-injection-attacks)
  + [Prompt rewriting](#prompt-rewriting)
    - [Language](#language)
    - [ASCII Art - ArtPrompt](#ascii-art---artprompt)
    - [Disguise and Reconstruction Attack (DRA)](#disguise-and-reconstruction-attack-dra)
  + [LLMs vs LLMs](#llms-vs-llms)
    - [Prompt Automatic Iterative Refinement (PAIR)](#prompt-automatic-iterative-refinement-pair)
    - [Iterative Refinement Induced Self-Jailbreak (IRIS)](#iterative-refinement-induced-self-jailbreak-iris)
  + [Token-Level Jailbreaking](#token-level-jailbreaking)
* [Conclusion](#conclusion)
* [Additional resources](#additional-resources)

## Introduction

Lately, my feed has been filled with posts and articles about jailbreaking Large Language Models. I was completely captured by the idea that these models can be tricked into doing almost anything but only as long as you ask the right way, as if it were a strange manipulation exercise with a chatbot:

*“In psychology, manipulation is defined as an action designed to influence or control another person, usually in an underhanded or unfair manner which facilitates one’s personal aims.”* ([Wikipedia](https://en.wikipedia.org/wiki/Manipulation_%28psychology%29))

In some cases, it could be relatively easy to make LLMs reply with text that could be considered harmful, even if you have little experience playing around with them. However, the most effective attacks are often more complex than they first appear.

Out of curiosity, I decided to take a look into what researchers are doing in this field and how challenging jailbreak an LLM can really be. This blog post is a summary of what I found: I hope you’ll like it!

Before discussing the jailbreaking techniques and how they work, I’ll try to briefly summarize some concepts which will be useful to understand the rest of the post.

I’m not an AI expert, so this is post is from someone coming at it from the security world. I did my best to understand the details, but I’m only human, so if I’ve gotten anything wrong, feel free to let me know! :)

## LLMs basics

This section serves as a **very minimal** introduction to some concepts which can help understanding the rest of the post. If you’re interested in a much more complete overview of the concepts below, be sure to check out the [3Blue1Brown playlist on Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi).

Just like other Machine Learning models, LLMs have to go through a phase of **training** before actually being useful: this is when the model is exposed to large datasets and *“learns”* from the observed data. For training LLMs, the models are fed huge amounts of text from various sources (books, websites, articles…) and they *“learn”* patterns and the statistical correlation in the input data.

![meme on LLMs learning](/images/posts/jailbreaking-llms/learns.jpg)

I promise this is the only meme you’ll find in this post

For example, if a model sees the phrase *“the Colosseum is in Rome”* enough times, it will get better at associating *“Colosseum”* with *“Rome”*. Over time, the model gets so good at spotting patterns that it starts to *“understand”* language; which in reality means that it learns to predict the next word in a sequence, similarly to what the auto-complete feature of the keyboards in our smartphones do.

![Text prediction example](/images/posts/jailbreaking-llms/text_predict.gif)

Gif from [Towards Data Science](https://towardsdatascience.com/sentence-generation-with-n-gram-21a5eef36a1b)

When we type a question or a prompt, the LLM takes it and generates a response by predicting the most likely sequence of words based on what it has *“learned”*.
However, since most of the prompts are unique, even slightly rephrased prompts can produce wildly different answers: this fundamental unpredictability of the model is often what allows jailbreak attack to exist.

### Tokenization

When training LLMs, a big challenge is represented by the fact that understanding language can be very complicated for statistical models. That’s why before training or generating responses, LLMs have to break down text into smaller chunks called **tokens** in order to be able to process it. These tokens could be individual words, sub-words, or even just characters, depending on the tokenizer.

To explain how tokenization works in simple terms, let’s say we have the sentence: *“I’m an As Roma fan”*. Tokens could be individual words or parts of words. In this case, ChatGPT splits it into 5 tokens :`["I'm", "an", "As", "Roma", "fan"]` (notice how “`I'm`” is a single token in this case). Each token is then matched to a number using a vocabulary, which is a predefined list containing all possible tokens. To continue with our example, the tokens might get converted as below:

```
"I'm"  → 15390
"an"   → 448
"As"   → 1877
"Roma" → 38309
"fan"  → 6831
```

Instead of the words, ChatGPT will now be able to work with the array of numbers `[15390, 448, 1877, 38309, 6831]`, and try to predict the next token in the sentence.

You can check out how LLMs process text with your own examples using [the OpenAI tokenizer](https://platform.openai.com/tokenizer).

That being said, we can now move to the most interesting part of the post!

## Jailbreaking LLMs

The term “jailbreaking” was first used for iOS devices, and it referred to the act of bypassing the software restrictions on iPhones and iPods, enabling users to perform unauthorized actions, like sideloading applications or install alternative app stores ([times are different now..](https://support.apple.com/en-mk/117767)).

In the context of generative AI, “jailbreaking” refers instead to tricking a model into **producing unintended outputs using specifically crafted prompts**.

Jailbreaking LLMs is often associated with malicious intent and attributed to threat actors trying to exploit vulnerabilities for harmful purposes. Although this is certainly true, security researchers are also actively exploring these techniques and coming up with new ones, to try to improve the defenses of such systems, similarly to what they do when red teaming other systems.

By finding vulnerabilities in these models, they can help developers ensure that the AI behaves as intended, avoiding responses which may be considered harmful or unexpected. If you still consider jailbreak attacks to be inherently malicious, you may be surprised to know that even **OpenAI emphasizes the need for red-teaming LLMs**: as security researchers he...