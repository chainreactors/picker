---
title: What we learned about TEE security from auditing WhatsApp's Private Inference
url: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/
source: The Trail of Bits Blog
date: 2026-04-07
fetch_date: 2026-04-08T04:37:29.550501
---

# What we learned about TEE security from auditing WhatsApp's Private Inference

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# What we learned about TEE security from auditing WhatsApp's Private Inference

[Trail of Bits](/authors/trail-of-bits/)

April 07, 2026

[audits](/categories/audits/), [trusted-execution-environment](/categories/trusted-execution-environment/), [cryptography](/categories/cryptography/), [meta](/categories/meta/)

Page content

* [The challenge of using AI with end-to-end encryption](#the-challenge-of-using-ai-with-end-to-end-encryption)
* [Key lessons for TEE deployments](#key-lessons-for-tee-deployments)
  + [Lesson 1: Never trust data outside your measurement](#lesson-1-never-trust-data-outside-your-measurement)
  + [Lesson 2: Do not trust data outside your measurement (have we already mentioned this?)](#lesson-2-do-not-trust-data-outside-your-measurement-have-we-already-mentioned-this)
  + [Lesson 3: Correctly verify security patch levels](#lesson-3-correctly-verify-security-patch-levels)
  + [Lesson 4: Attestations need freshness guarantees](#lesson-4-attestations-need-freshness-guarantees)
  + [How Meta fixed the remaining issues](#how-meta-fixed-the-remaining-issues)
* [Beyond individual vulnerabilities: Systemic challenges in TEE deployment](#beyond-individual-vulnerabilities-systemic-challenges-in-tee-deployment)
* [The path forward for securely deploying TEEs](#the-path-forward-for-securely-deploying-tees)

WhatsApp’s new “Private Inference” feature represents one of the most ambitious attempts to combine end-to-end encryption with AI-powered capabilities, such as message summarization. To make this possible, Meta built a system that processes encrypted user messages inside trusted execution environments (TEEs), secure hardware enclaves designed so that not even Meta can access the plaintext. Our [now-public audit](https://github.com/trailofbits/publications/blob/master/reviews/2025-08-meta-whatsapp-privateprocessing-securityreview.pdf), conducted before launch, identified several vulnerabilities that compromised WhatsApp’s privacy model, all of which Meta has patched. Our findings show that TEEs aren’t a silver bullet: every unmeasured input and missing validation can become a vulnerability, and to securely deploy TEEs, developers need to measure critical data, validate and never trust any unmeasured data, and test thoroughly to detect when components misbehave.

## The challenge of using AI with end-to-end encryption

WhatsApp’s Private Processing attempts to resolve a fundamental tension: WhatsApp is end-to-end encrypted, so Meta’s servers cannot read, alter, or analyze user messages. However, if users also want to opt in to AI-powered features like message summarization, this typically requires sending plaintext data to servers for computationally expensive processing. To solve this, Meta uses TEEs based on AMD’s SEV-SNP and Nvidia’s confidential GPU platforms to process messages in a secure enclave where even Meta can’t access them or learn meaningful information about the message contents.

The stakes in WhatsApp are high, as vulnerabilities could expose millions of users’ private messages. Our review identified 28 issues, including eight high-severity findings that could have enabled attackers to bypass the system’s privacy guarantees. The following sections explore noteworthy findings from the audit, how they were fixed, and the lessons they impart.

## Key lessons for TEE deployments

### Lesson 1: Never trust data outside your measurement

In TEE systems, an “attestation measurement” is a cryptographic checksum of the code running in the secure enclave; it’s what clients check to ensure they’re interacting with legitimate, unmodified software. We discovered that WhatsApp’s system loaded configuration files containing environment variables *after* this fingerprint was taken (issue TOB-WAPI-13 in the report).

This meant that a malicious insider at Meta could inject an environment variable, such as `LD_PRELOAD=/path/to/evil.so`, forcing the system to load malicious code when it started up. The attestation would still verify as valid, but the attacker’s malicious code would be running inside, potentially violating the system’s security or privacy guarantees by, for example, logging every message being processed to a secret server.

Meta fixed this by strictly validating environment variables: they can now contain only safe characters (alphanumeric plus a few symbols like dots and dashes), and the system explicitly checks for dangerous variables like `LD_PRELOAD`. Every piece of data your TEE loads must either be part of the measured boot process or be treated as potentially hostile.

### Lesson 2: Do not trust data outside your measurement (have we already mentioned this?)

ACPI tables are configuration data that inform an operating system about the available hardware and how to interact with it. We found these tables weren’t included in the attestation measurement (TOB-WAPI-17), creating a backdoor for attackers.

Here’s why this matters: a malicious hypervisor (the software layer that manages virtual machines) could inject fake ACPI tables defining malicious “devices” that can read and write to arbitrary memory locations. When the secure VM boots up, it processes these tables and grants the fake devices access to memory regions that should be protected. An attacker could use this to extract user messages or encryption keys directly from the VM’s memory, and the attestation report will still verify as valid and untampered.

Meta addressed this by implementing a custom bootloader that verifies ACPI table signatures as part of the secure boot process. Now, any tampering with these tables will change the attestation measurement, alerting clients that something is wrong.

### Lesson 3: Correctly verify security patch levels

AMD regularly releases security patches for its SEV-SNP firmware, fixing vulnerabilities that could allow attackers to compromise the secure environment. The WhatsApp system did check these patch levels, but it made an important error: it trusted the patch level that the firmware *claimed* to be running (in the attestation report), rather than verifying it against AMD’s cryptographic certificate (TOB-WAPI-8).

An attacker who had compromised an older, vulnerable firmware could simply lie about their patch level. Researchers have publicly demonstrated attacks that can extract encryption keys from older SEV-SNP firmware versions. An attacker could use these published techniques against WhatsApp users to exfiltrate secret data while the client incorrectly believes it’s connected to a secure, updated system.

Meta’s solution was to validate patch levels against the VCEK certificate’s X.509 extensions. These extensions are cryptographically signed data from AMD that can’t be forged by compromised firmware.

### Lesson 4: Attestations need freshness guarantees

Before our review, when a client connected to the Private Processing system, the server would generate an attestation report proving its identity, but this report didn’t include any timestamp or random value from the client (TOB-WAPI-7). This meant that an attacker who compromised a TEE once could save its attestation report and TLS keys, then replay them indefinitely.

Achieving a one-time compromise of a TEE is typically much more feasible and much less severe than a persistent compromise affecting each individual session. For example, consider an attacker who can extract TLS session keys through a side channel attack or other vulnerability. For a single attack, the impact tends to be short-lived, as the forward security of TLS makes the exploit impactful for only a single TLS session. However, without freshness, that single success becomes a permanent backdoor because the TEE’s attestation report from that compromised session can be replayed indefinitely. In particular, the attacker can now run a fake server anywhere in t...