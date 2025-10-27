---
title: MTE As Implemented, Part 2: Mitigation Case Studies
url: https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html
source: Project Zero
date: 2023-08-03
fetch_date: 2025-10-04T12:01:22.415689
---

# MTE As Implemented, Part 2: Mitigation Case Studies

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Wednesday, August 2, 2023

### MTE As Implemented, Part 2: Mitigation Case Studies

By Mark Brand, Project Zero

## Background

In 2018, in the [v8.5a version](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-a-profile-architecture-2018-developments-armv85a) of the ARM architecture, ARM proposed a hardware implementation of tagged memory, referred to as MTE (Memory Tagging Extensions).

In [Part 1](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html) we discussed testing the technical (and implementation) limitations of MTE on the hardware that we've had access to. This post will now consider the implications of what we know on the effectiveness of MTE-based mitigations in several important products/contexts.

To summarize - there are two key classes of bypass techniques for memory-tagging based mitigations, and these are the following (for some examples, see [Part 1](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html)):

1. Known-tag-bypasses - In general, confidentiality of tag values is key to the effectiveness of memory-tagging as a mitigation. A breach of tag confidentiality allows the attacker to directly or indirectly ensure that their invalid memory accesses will be correctly tagged, and are therefore not detectable.
2. Unknown-tag-bypasses - Implementation limits might mean that there are opportunities for an attacker to still exploit a vulnerability despite performing memory accesses with incorrect tags that could be detected.

There are two main modes for MTE enforcement:

1. Synchronous (sync-MTE) - tag check failures result in a hardware fault on instruction retirement. This means that the results of invalid reads and the effects of invalid writes should not be architecturally observable.
2. Asynchronous (async-MTE) - tag check failures do not directly result in a fault. The results of invalid reads and the effects of invalid writes are architecturally observable, and the failure is delivered at some point after the faulting instruction in the form of a per-cpu flag.

Since Spectre, it has been clear that using standard memory-tagging approaches as a "hard probabilistic mitigation"[1](#h.xivuzilpjgfi) is not generally possible. In any context where an attacker can construct a speculative side-channel, known-tag-bypasses are a fundamental weakness that must be accounted for.

Another proposed approach is combining MTE with another software approach to construct a "hard deterministic mitigation"[2](#h.2li82hlequ8). The primary example of this would be the [\*Scan+MTE combinations](https://security.googleblog.com/2022/05/retrofitting-temporal-memory-safety-on-c.html) proposed in Chrome to mitigate use-after-free vulnerabilities by ensuring that a tag is not re-used for an allocation while there are any stale pointers pointing to that allocation.

In this case, is async-MTE sufficient as an effective mitigation? We have demonstrated techniques that allow an unknown-tag-bypass when using async-MTE, so it seems clear that for a "hard" mitigation, (at least) sync-MTE will be necessary. This should not, however, be interpreted as implying that such a "soft" mitigation would not prove a significant inconvenience to attackers - we're going to discuss that in detail below.

## How much would MTE hurt attackers?

In order to understand the "additional difficulty" that attackers will face in writing exploits that can bypass MTE based mitigations, we need to consider carefully the context in which the attacker finds themself.

We have made some assumptions here about the target reliability that a high-tier attacker would want as around 95% - this is likely lower than currently expected in most cases, but probably higher than the absolute limit at which an exploit might become too unreliable for their operational needs. We also note that in some contexts an attacker might be able to use even an extremely unreliable exploit without significantly increasing their risk of detection. While we'd expect attackers to desire (and invest in) achieving reliability, it's unlikely that even if we could force an upper bound to that reliability this would be enough to completely prevent exploitation.

However, any such drop in reliability should generally be expected to increase detection of in-the-wild usage of exploits, increasing the risk to attackers accordingly.

An additional note is that most unknown-tag-bypasses would be prevented by the use of sync-MTE, at least in the absence of specific weaknesses in the application which would over time likely be fixed as exploits are observed exploiting those weaknesses.

We consider 4 main contexts here, as we believe these are the most relevant/likely use-cases for a usermode mitigation:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Context | Mode | Bypass techniques | | | | | |
| known-tag-bypass | | | unknown-tag-bypass | | |
| Chrome: Renderer Exploit | async | Trivial ♻️ | | | Likely trivial ♻️ | | |
| sync | Trivial ♻️ | | | Bypass techniques should be rare 🛠️ | | |
| Chrome: IPC Sandbox Escape | async | Likely possible in many cases ♻️ | | | Likely possible in many cases 🐛\* | | |
| sync | Likely possible in many cases ♻️ | | | Bypass techniques should be rare 🛠️ | | |
| Android: Binder Sandbox Escape | async | Difficulty will depend on service | | | Difficulty will depend on service 🐛\* | | |
| sync | Difficulty will depend on service | | | Bypass techniques should be rare 🛠️ | | |
| Android: Messaging App Oneshot | async | Likely impossible in most cases | | | Good enough bugs will be very rare 🐛\* | | |
| sync | Likely impossible in most cases | | | Bypass techniques should be rare 🛠️ | | |

The degree of pain for attackers caused by needing to bypass MTE is roughly assessed from low to very high.

♻️: Once developed, generic bypass technique can likely be shared between exploits.

🛠️: Limited supply of bypass techniques that could be fixed, eventually eliminating this bypass.

🐛: Additional constraints imposed by bypass techniques mean that the subset of issues that are exploitable is significantly reduced with MTE.

\* Note that it's also potentially possible to design software to make exploitation of these unknown-tag-bypass techniques more restrictive by eg. inserting system calls in specific choke-points. We haven't investigated the practicality or limitations of such an approach at this time, but it is unlikely to be generally applicable especially where third-party code is involved.

### Chrome: Javascript -> Compromised Renderer

Spectre-type speculative side-channels can be used to break tag confidentiality, so known-tag-bypasses are a certainty.

For unknown-tag-bypasses, javascript should in most situations be able to avoid system calls for the duration of their exploit, so the exploit needs to complete within the soft time constraint.

It's likely that both known-tag-bypass and unknown-tag-bypass techniques can be made generic and reused across multiple different vulnerabilities.

### Chrome: Compromised Renderer -> Mojo IPC Sandbox Escape

It is likely that Spectre-type speculative side-channels can be used to break tag confidentiality, so known-tag-bypasses are a possibility.

For unknown-tag-bypasses, we believe that there are circumstances under which multiple IPC messages can be processed without a system call in between. This does not hold for all situations, and the current public state-of-the-art techniques for Browser process IPC exploitation would perform multiple system calls and would not be suitable.

It's possible that a generic speculative-side-channel attack could be developed that would allow reuse of techniques for known-tag-bypasses against a specific privileged process (likely the Browser process). Any unknown-tag-bypass exploit would...