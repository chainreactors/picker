---
title: Cloud cryptography demystified: Google Cloud Platform
url: https://blog.trailofbits.com/2024/08/05/cloud-cryptography-demystified-google-cloud-platform/
source: Trail of Bits Blog
date: 2024-08-06
fetch_date: 2025-10-06T18:03:49.307059
---

# Cloud cryptography demystified: Google Cloud Platform

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Cloud cryptography demystified: Google Cloud Platform

Scott Arciszewski

August 05, 2024

[cryptography](/categories/cryptography/)

*This post, the second in our series on cryptography in the cloud, provides an overview of the cloud cryptography services offered within Google Cloud Platform (GCP): when to use them, when not to use them, and important usage considerations. Stay tuned for future posts covering other cloud services.*

At Trail of Bits, we frequently encounter products and services that use cloud providers’ cryptography offerings to satisfy their security goals. However, some cloud providers’ cryptography tools and services have opaque names or non-obvious use cases. This guide—informed by Trail of Bits’ extensive auditing experience—dives into the differences between these services and explains important considerations, helping you choose the right solution to enhance your project’s security.

### Introduction

At the time this post is published, Google Cloud Platform’s cryptography offerings are decidedly fewer than those of Amazon Web Services, which we [discussed in the previous entry to this series](https://blog.trailofbits.com/2024/02/14/cloud-cryptography-demystified-amazon-web-services/).

Intuitively, less stuff can be good: with fewer services and software to keep track of, your users’ complexity and cognitive load are minimized. However, this does come with the risk that your service or software becomes a sort of Swiss army knife: adequate at several things, but excellent at nothing.

We will explore three cryptography products in Google Cloud Platform and the Google-recommended solution for client-side encryption.

### Google Cloud Services

#### Cloud KMS

**You want to use Cloud KMS:** If you’re working with Google Cloud Platform in any capacity.

You can think about Cloud KMS as actually being three different products that offer different protection levels in one convenient API:

1. Cloud KMS with software keys
2. Cloud HSM, which performs all cryptographic operations in the HSM hardware
3. Cloud EKM, where keys are stored in an external provider, for customers that need to maintain sovereignty over their encryption materials

Regardless of which of the three products you end up using, you can use it with the Google KMS API. In turn, you can use your secrets with all other GCP services that would otherwise use Cloud KMS for key management.

Unless told otherwise, you almost certainly don’t need Cloud HSM or Cloud EKM.

##### When to use Google Cloud HSM

If you care about FIPS 140 validation levels greater than 1, then Cloud HSM is essential to your use case. Otherwise, you don’t need it.

If you’re unsure if you care about this, keep in mind that FIPS 140 level 1 is essentially the minimum bar that must be cleared for any cryptographic modules used in services being sold to the US government through FedRAMP, and doesn’t significantly impact cryptographic security.

There are customers that care about level 1 vs level 3, but chances are you’ll know if you’re dealing with one.

##### When to use Google Cloud EKM

If your nation’s regulators insist that you maintain control over the cryptographic materials, you can use Cloud EKM to meet their requirements without ripping out the entirety of your cloud architecture.

Otherwise, just using Cloud KMS with software keys gets the job done.

#### Secret Manager

**You want to use Google Cloud Secret Manager:** If you need to manage and rotate service passwords (e.g., to access a relational database).

**You don’t want to use Google Cloud Secret Manager:** If you’re looking to store your online banking passwords.

If you’ve ever used a password manager, Secret Manager should be a familiar experience. It stores secrets that your application needs to run in the Google Cloud environment–such as database passwords, API keys, and other sensitive information that you really shouldn’t commit directly into your source code.

Secret Manager uses [a versioning mechanism](https://cloud.google.com/secret-manager/docs/view-secret-version) to maintain a history of past credentials, which is useful for avoiding operational events during secret rotation.

#### Confidential Computing

**You want to use Confidential Computing:** If you’re sure it’s appropriate for your threat model.

**You don’t want to use Confidential Computing:** If you aren’t sure, or don’t even have a threat model. (Trail of Bits conducts both lightweight and traditional threat models; [contact us](https://www.trailofbits.com/contact/) if you need help with this!)

Broadly speaking, Confidential Computing is like DRM, except with an inverted power dynamic.

Confidential Computing aspires to allow you to compute without your service provider knowing what software you’re running or what data said software is processing.

This isn’t just one technology, but a suite of different tools and techniques that strive towards this goal. Some techniques proposed by academic researchers rely on **homomorphic encryption**. Others rely on trusted execution environments.

Google has multiple irons in this fire, so we expect this to change over time as new techniques emerge, but their current offerings rely on AMD SEV as a Trusted Execution Environment. Unfortunately, there have been side-channel attacks against AMD SEV over the past few years (i.e., [CVE-2021-46744](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-1033.html) and [CVE-2023-20575](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3004.html)).

![](/img/wpdump/e4174ec33f02e36f66adcc48f75614ee.jpg)

Meme inspired by [this tweet](https://twitter.com/softminus/status/1364336476792627204)

It’s difficult to distill clear guidance in a generally available blog post without any context on what you might be building, or what threats you’re trying to protect against, but if I had to say something short and pithy here: Proceed carefully and consult with experts.

### Client-side cryptography for GCP

*[Three Tools for the Zero-trust infra hype](https://cloud.google.com/products?hl=en#security-and-identity),
[Seven for the product team set on no-code](https://cloud.google.com/products?hl=en#productivity-and-collaboration),
[Nine for DBAs of all stripes](https://cloud.google.com/products?hl=en#databases),
One for the Math Nerds to protect data flows
In the Cloud of Google where Containers lie.
One Tink to encrypt all, One Tink for signing,
One Tink to manage keys, and ensure context binding
In the Cloud of Google where Containers lie.*
(with apologies to [Tolkien](https://tolkiengateway.net/wiki/Ring_Verse#Ring-verse))

**Tink** is the sole cryptography library developed by Google that GCP customers are encouraged to use for client-side encryption for Google’s cloud products.

#### What Tink does well

As one might expect, Tink provides all of [the basic functions that one would need from a client-side cryptography library](https://developers.google.com/tink/scenario-overview): Tink encrypts and decrypts data; signs messages and verifies signatures; and even provides dedicated utilities for deterministic encryption and working with structured data.

But Tink also ships [a JSON Web Tokens (JWT) module](https://developers.google.com/tink/jwt) that successfully ignores [the unsafe parts of the JOSE standards](https://scottarc.blog/2023/09/06/how-to-write-a-secure-jwt-library-if-you-absolutely-must/).

Beyond the refusal to support totally unsafe options, such as [`alg=none`](https://www.howmanydayssinceajwtalgnonevuln.com/), the biggest reason why Tink’s JWT library is safer than most comes down to a cryptography engineering principle: keys in Tink aren’t just raw byte strings.

Tink enforces the tenet that a cryptography key’s identity is [both the raw bytes and the parameter choices](https://web.archive.org/web/2022082408...