---
title: Datasig: Fingerprinting AI/ML datasets to stop data-borne attacks
url: https://blog.trailofbits.com/2025/05/02/datasig-fingerprinting-ai/ml-datasets-to-stop-data-borne-attacks/
source: The Trail of Bits Blog
date: 2025-05-03
fetch_date: 2025-10-06T22:27:40.967529
---

# Datasig: Fingerprinting AI/ML datasets to stop data-borne attacks

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Datasig: Fingerprinting AI/ML datasets to stop data-borne attacks

Boyan Milanov

May 02, 2025

[machine-learning](/categories/machine-learning/), [research-practice](/categories/research-practice/), [open-source](/categories/open-source/)

Page content

* [Why your AI security is incomplete without data traceability](#why-your-ai-security-is-incomplete-without-data-traceability)
  + [The rise of AIBOM tools](#the-rise-of-aibom-tools)
  + [Why training data is so hard to track](#why-training-data-is-so-hard-to-track)
  + [Datasig’s approach: Fingerprinting that works](#datasigs-approach-fingerprinting-that-works)
* [Under the hood: How datasig works](#under-the-hood-how-datasig-works)
  + [The fingerprinting process](#the-fingerprinting-process)
* [Real-world validation: The MNIST test case](#real-world-validation-the-mnist-test-case)
  + [Fingerprinting testing](#fingerprinting-testing)
* [What’s next for Datasig](#whats-next-for-datasig)

Today we’re releasing Datasig, a lightweight tool that solves one of AI security’s most pressing blindspots: knowing exactly what data was used to train your models. Datasig generates compact, unique fingerprints for AI/ML datasets that let you compare training data with high accuracy—without needing access to the raw data itself. This critical capability helps AIBOM (AI bill of materials) tools detect data-borne vulnerabilities that traditional security tools completely miss.

Training data is a major attack vector against AI systems. Attackers can use techniques like data poisoning to backdoor models, leak private information, or silently introduce bias—often leaving no obvious traces of their handiwork. When these attacks happen, most organizations can’t even answer a simple question: “What data did we actually use to train this model?”

Without data traceability, you can’t verify a model’s integrity, audit for compliance, or investigate security incidents. Yet the AI ecosystem still lacks tools to fingerprint training data without storing the entire dataset (which is often impractical for privacy, legal, and storage reasons).

Datasig creates unique identifiers and compact fingerprints for AI/ML datasets that make it easy to automate comparing datasets with great accuracy and without access to the raw data. It proposes a theoretical solution to dataset fingerprinting and provides a practical implementation, as we demonstrate on the MNIST vision dataset.

This post reviews the AI/ML security research that motivates Datasig, describes how our prototype works in detail, and discusses its future evolution.

Ready to dive straight into the code? Check out [Datasig on GitHub](https://github.com/trailofbits/datasig).

## Why your AI security is incomplete without data traceability

Traditional security tools have blindspots when it comes to AI’s unique attack surface. Your SBOM might tell you which libraries your model is using, but it knows nothing about the data that shaped your model’s behavior. This blind spot creates a perfect opportunity for attackers.

### The rise of AIBOM tools

AI Bill of Materials (AIBOM) tools are emerging to fill this gap, aiming to document the entire AI supply chain. But there’s a critical piece missing: a reliable way to track and verify training data. Without this capability, these tools can’t answer fundamental questions like:

* Was this model trained on poisoned data?
* Did sensitive information leak into the training set?
* Are two models using the same datasets, making them vulnerable to the same attacks?

### Why training data is so hard to track

Tracing datasets isn’t as simple as adding a dependency to your requirements.txt file. Three key challenges make this particularly difficult:

1. **Data volatility**: Datasets evolve constantly. Without capturing the exact state at training time it becomes impossible to reproduce or verify anything about training data.
2. **Scale and privacy issues**: Storing complete copies of training data is often impractical or legally problematic, especially for large datasets containing personal information.
3. **Different vulnerability patterns**: data-borne vulnerabilities are inherently different from traditional software vulnerabilities, and traditional dependency scanning can’t check for the presence of vulnerable data.

### Datasig’s approach: Fingerprinting that works

Datasig helps trace and verify what data was used to train a model without storing all the data itself. It does so by using a novel dataset fingerprinting approach that generates unique identifiers and compact fingerprints for AI/ML datasets. This allows upstream AIBOM tools to compare datasets with great accuracy without access to the actual training data, improving dataset verifiability and traceability in AI/ML systems. More precisely, fingerprints allow AIBOM tools to:

* Verify dataset provenance
* Compare datasets to identify potential vulnerabilities based on similarity
* Track dataset evolution across model versions
* Detect when a model might have been trained on compromised data

## Under the hood: How datasig works

Datasig’s dataset fingerprinting approach is based on [MinHash Signatures](https://aksakalli.github.io/2016/03/01/jaccard-similarity-with-minhash.html). Datasig takes the dataset as input and outputs a list of binary hash values that mathematically corresponds to a MinHash Signature. This fingerprint can be compared to another to estimate how similar the corresponding datasets are. Here’s how it works:

### The fingerprinting process

1. **Canonization**: Datasig first transforms the dataset into a standardized format. We hash each individual data point (image, text sample, etc.) to create a flat set of hash values.
2. **MinHash transformation**: We then apply MinHash algorithms to this canonical representation, generating a fixed-size signature that preserves similarity relationships. This MinHash signature is the dataset fingerprint.
3. **Comparison**: The fingerprint can then be compared directly to other fingerprints to measure dataset similarity without needing the original data.

![How fingerprinting works: Each dataset is independently processed to create a compact signature. These signatures can be compared directly to estimate dataset similarity without accessing the original data.](/img/datasig_figure_1.png)

Figure 1: How fingerprinting works: Each dataset is independently processed to create a compact signature. These signatures can be compared directly to estimate dataset similarity without accessing the original data.

This approach leverages mathematical properties of MinHash to make fingerprints an excellent approximation of how similar two datasets are in terms of identical data points (see the [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)). In our experiments, we use fingerprints consisting of 400 hashes, which give a bounded error margin as small as 5%. Accuracy can be bolstered by generating longer fingerprints, at the cost of heavier computations.

We’re preparing a technical whitepaper that dives deeper into the mathematical foundations, but the key takeaway is this: Datasig’s approach is mathematically sound, produces compact fingerprints, and maintains high accuracy across diverse dataset types.

## Real-world validation: The MNIST test case

To demonstrate Datasig’s effectiveness, we put it to the test with the MNIST dataset—a standard computer vision benchmark. Our implementation supports PyTorch vision datasets out of the box, with a clean, straightforward API:

![MNIST test case](/img/datasig_figure_2.png)

### Fingerprinting testing

We wrote [tests](https://github.com/trailofbits/datasig/blob/6d925bcc9f7bc581cbbb4eb7625efea9f95e6d64/datasig/test/test_torch_mnist.py#L425-L449) on MNIST data that build datasets of various degrees of similarity, compute their fingerprints, a...