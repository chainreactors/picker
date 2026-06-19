---
title: The Road to Post-Quantum Readiness Part 1 of 2: Understanding the Risk
url: https://blog.nviso.eu/2026/06/18/the-road-to-post-quantum-readiness-part-1/
source: NVISO Labs
date: 2026-06-18
fetch_date: 2026-06-19T07:07:19.396820
---

# The Road to Post-Quantum Readiness Part 1 of 2: Understanding the Risk

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# The Road to Post-Quantum Readiness Part 1 of 2: Understanding the Risk

[Sven-Christian Kruse](https://blog.nviso.eu/author/sven-christian-kruse/)

[Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/), [Cryptography](https://blog.nviso.eu/category/cryptography/)

June 18, 2026June 18, 2026
12 Minutes

By

[Sven-Christian Kruse](https://blog.nviso.eu/author/sven-christian-kruse/) , [Milan Velle](https://blog.nviso.eu/author/milan-velle/)

June 18, 2026

## Introduction

Merely a few years ago, when asking about the state of quantum computing or the need for Post-Quantum Cryptography (PQC), the response would usually revolve around the ongoing PQC competition that NIST had brought to life in an attempt to identify algorithms for standardization. [In 2022, Cloudflare started experimenting](https://blog.cloudflare.com/post-quantum-for-all/)[1](#e7016647-5812-40ff-833b-41cb98eb0754) with hybrid key agreement on its production edge, though most of the world outside a handful of research labs had barely registered that any of this mattered. The core argument of that work was that organizations needed to start preparing *before* the standards were finalized, because migrating cryptography in a large enterprise takes years and quantum computers don’t wait for anybody’s roadmap.

Today, those standards are no longer a draft. The algorithms are running in your browser. They are available in AWS, Azure, and Google Cloud. Yet, by most estimates, the vast majority of companies have still done nothing.

This is **Part 1 of a 2-part series** and focuses on the fundamentals of Post-Quantum Cryptography: the underlying risk, the core concepts, and the current state of standards and deployment.

If you are only looking for the **practical enterprise migration playbook**, you can start with **Part 2**. It is designed to be read independently.

**This part covers:**

* **Why Quantum Computing Changes Cryptography**
  + Classical Cryptography Depends on Hard Problems
  + Quantum Computing Expands What Can Be Solved Efficiently
  + Shor Breaks Public-Key Crypto, Grover Weakens Symmetric Crypto
  + What Post-Quantum Cryptography Actually Is
* **Harvest Now, Decrypt Later**
* **PQC Has Moved from Standards to Deployment**
  + The First NIST Standards Are Final
  + Governments Have Started Putting Dates on the Calendar
  + Browsers, Clouds, and the Internet Edge Have Already Moved
  + Why Hybrid Deployment Is the Current Default
* **Key Acronyms** (*A short glossary of acronyms used in this article is included at the end*)

If you are already comfortable with the mathematical background, you can skim the first section and jump ahead to **Harvest Now, Decrypt Later** or **PQC Has Moved from Standards to Deployment**.

## Why Quantum Computing Changes Cryptography

Let us start by looking at quantum computers. These are machines that use qubits and quantum-mechanical effects such as superposition and entanglement to solve certain problems much more efficiently than classical machines. They are not better at everything, but they have the capability to **solve some specific problems dramatically faster, and in some important cases exponentially faster**, **than our current “classical” computers**.

### Classical Cryptography Depends on Hard Problems

To visualize this, we will have a very brief look at something called **complexity theory**. This is a field focused on classifying mathematical problems based on their difficulty and helps us distinguish between problems that can be solved efficiently and those that become infeasible at scale. This is at the heart of cryptography, because many **cryptographic systems rely on problems that are believed to be computationally hard for adversaries, while still being efficient for legitimate users that have the right key.**

In the pre-quantum computing era, when we only relied on classical computers, two important problem classes from complexity theory were:

* **P-Problems – “Polynomial time”**: These are problems that can be solved efficiently by classical computers. In practice, this means the time needed to solve them grows at a manageable rate as the input becomes larger. Examples include arithmetic, sorting, and pattern matching in text.

* **NP-Problems – “Non-deterministic Polynomial time”**: These are problems for which a proposed solution can be verified efficiently, even if finding that solution may be very difficult.

*A useful way to think about this is a puzzle: solving it may take a long time, but once someone gives you an answer, verifying whether it is correct can be done quickly.*

For cryptography, the key takeaway is not that it relies on NP-problems in general, but that **it relies on specific** **mathematical problems that appear computationally hard to reverse without secret information**. In the classical world, this includes problems such as integer factorization and the discrete logarithm problem, which form the basis of much of today’s asymmetric cryptography.

The figure below illustrates this simplified classical view: efficiently solvable problems lie in P, while problems like factoring and discrete logarithms were long treated as computationally hard in practice for classical adversaries and were therefore relied on heavily for classical asymmetric cryptography, such as RSA (named after its creators Rivest, Shamir, and Adleman, and based on the factorization problem) and ECC (Elliptic Curve Cryptography, which is based on the discrete logarithm problem).

![](https://blog.nviso.eu/wp-content/uploads/2026/05/image-12.png)

Figure 1: Complexity of classical algorithms

---

### Quantum Computing Expands What Can Be Solved Efficiently

Quantum computing, with its quantum-mechanical characteristics, has changed this picture for some problem classes, which is why it has such a significant impact on modern cryptography: problems that were believed to be infeasible for classical computers, such as factoring and discrete logarithms, can become efficiently solvable with the...