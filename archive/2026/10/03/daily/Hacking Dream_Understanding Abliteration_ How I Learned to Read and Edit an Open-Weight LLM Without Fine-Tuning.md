---
title: Understanding Abliteration: How I Learned to Read and Edit an Open-Weight LLM Without Fine-Tuning
url: https://www.hackingdream.net/2026/10/understanding-abliteration-how-i-learned-to-edit-an-open-weight-llm-without-finetuning.html
source: Hacking Dream
date: 2026-10-03
fetch_date: 2026-10-04T07:37:44.879590
---

# Understanding Abliteration: How I Learned to Read and Edit an Open-Weight LLM Without Fine-Tuning

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Understanding Abliteration: How I Learned to Read and Edit an Open-Weight LLM Without Fine-Tuning

[October 03, 2026](https://www.hackingdream.net/2026/10/understanding-abliteration-how-i-learned-to-edit-an-open-weight-llm-without-finetuning.html "permanent link")

# LLM Abliteration: My Qwen Experiments Without Fine-Tuning

By [Bhanu Namikaze](https://www.hackingdream.net/p/about-author.html) · Updated October 3, 2026

On this page: 52 sections

* [What I mean by "uncensored"](#what-i-mean-by-uncensored)
* [Before abliteration: understand what is actually inside the model](#before-abliteration)
* [The most important number: 1536](#the-most-important-number)
* [The embedding matrix](#the-embedding-matrix)
* [What is a transformer layer?](#what-is-a-transformer-layer)
* [The residual stream](#the-residual-stream)
* [What are Q, K, V and O?](#what-are-qkvo)
* [Why are K and V only 256?](#why-are-k-and-v-only-256)
* [What is an attention head?](#what-is-an-attention-head)
* [What does `o_proj` do?](#what-does-oproj-do)
* [The MLP side: gate, up and down](#the-mlp-side)
* [Why we care about `o_proj` and `down_proj`](#why-we-care-about-oproj-and-downproj)
* [A simple script to inspect an open model](#a-simple-script)
* [How do I see the actual matrix values?](#how-do-i-see-the-actual-matrix-values)
* [We do not find a "refusal matrix"](#we-do-not-find-a-refusal-matrix)
* [Hidden activations versus weights](#hidden-activations-versus-weights)
* [Capturing a layer's activation](#capturing-a-layers-activation)
* [Turning two behaviors into a direction](#turning-two-behaviors-into-a-direction)
* [What do the direction's numbers mean?](#what-do-the-directions-numbers-mean)
* [Measuring whether the direction actually separates behavior](#measuring-whether-the-direction-actually-separates-behavior)
* [Representation is not the same thing as control](#representation-is-not-the-same-thing-as-control)
* [How do we test causality?](#how-do-we-test-causality)
* [Why sweep multiple layers?](#why-sweep-multiple-layers)
* [Experiment scope and limitations](#experiment-scope-and-limitations)
* [What happened in Qwen](#what-happened-in-qwen)
* [Looking inside the layer](#looking-inside-the-layer)
* [Steering is not necessity](#steering-is-not-necessity)
* [I removed it from `o_proj` and `down_proj`](#i-removed-it-from-oproj-and-downproj)
* [Why writer ablation failed](#why-writer-ablation-failed)
* [The model rebuilt the direction](#the-model-rebuilt-the-direction)
* [So I tried persistent multi-layer ablation](#so-i-tried-persistent-multi-layer-ablation)
* [Representation, control and necessity are three different questions](#representation-control-and-necessity-are-three-different-questions)
* [How do the matrices get changed without training?](#how-do-the-matrices-get-changed-without-training)
* [Standalone weight-projection code](#standalone-weight-projection-code)
* [Why `gate_proj` is different](#why-gateproj-is-different)
* [Runtime ablation is not identical to weight editing](#runtime-ablation-is-not-identical-to-weight-editing)
* [Weight editing does not mean fine-tuning](#weight-editing-does-not-mean-fine-tuning)
* [Can TensorFlow automatically find the refusal matrices?](#can-tensorflow-automatically-find-the-refusal-matrices)
* [How this translates to refusal research](#how-this-translates-to-refusal-research)
* [Why refusal experiments are interesting to a red teamer](#why-refusal-experiments-are-interesting-to-a-red-teamer)
* [My current workflow: Abliteration Workbench](#my-current-workflow-abliteration-workbench)
* [A separate held-out Workbench validation](#held-out-workbench-validation)
* [Running the Workbench on Qwen](#running-the-workbench-on-qwen)
* [What if I want another model?](#what-if-i-want-another-model)
* [MoE makes this harder](#moe-makes-this-harder)
* [What my Qwen experiment actually taught me](#what-my-qwen-experiment-actually-taught-me)
* [Why I do not immediately save an edited checkpoint](#why-i-do-not-immediately-save-an-edited-checkpoint)
* [Abliteration is geometry](#abliteration-is-geometry)
* [A compact mathematical summary](#a-compact-mathematical-summary)
* [What I would tell someone starting today](#what-i-would-tell-someone-starting-today)
* [Final thoughts](#final-thoughts)
* [Related reading](#related-reading)

A practical guide to model internals, steering, ablation, and weight editing based on my Qwen experiments.

**In short:** LLM abliteration identifies a behavior direction in a model's activations, tests whether changing that direction affects behavior, and can project it out of selected weights without gradient-based fine-tuning. This article follows the experiments that led me from representation to causal testing.

When I first started looking into LLM abliteration, I had a fairly simple question:

> If I have the weights of an open model, where exactly is a behavior such as refusal, verbosity, or conciseness stored, and how do I change it?

At first I imagined there might be something like a "refusal matrix."

Find the matrix. Change some numbers. Save the model.

It turns out that this mental model is much too simple.

An LLM contains billions of parameters, but behavior does not usually map cleanly to one parameter, one matrix, or even one transformer layer. What we can often find instead is a **direction in the model's activation space** that correlates with a behavior.

Once we find such a direction, we can experimentally push the model along it, remove it, watch whether later layers recreate it, and eventually, when the evidence supports it, modify the matrices that write into that space.

That family of techniques is what people usually mean when they talk about **abliteration**.

The technique became widely known following research showing that refusal behavior in a number of chat models could be associated with a surprisingly low-dimensional, in many cases effectively one-dimensional, direction in the residual stream. Removing that direction reduced refusal, while adding it could induce refusal even for harmless requests. [Arditi et al.'s refusal-direction paper](https://arxiv.org/abs/2406.11717)

The community later popularized the term *abliteration* for using this observation to identify a direction and project it out of activations or weights. [Hugging Face abliteration guide](https://huggingface.co/blog/mlabonne/abliteration)

As a red teamer, I found the id...