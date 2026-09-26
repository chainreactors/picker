---
title: Don't let TEEs break your MPC
url: https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/
source: The Trail of Bits Blog
date: 2026-09-25
fetch_date: 2026-09-26T06:51:01.616272
---

# Don't let TEEs break your MPC

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Don't let TEEs break your MPC

[Paul Bottinelli](/authors/paul-bottinelli/)

September 25, 2026

[cryptography](/categories/cryptography/), [trusted-execution-environment](/categories/trusted-execution-environment/), [threshold-signatures](/categories/threshold-signatures/)

Page content

* [MPC: Security that depends on participant behavior](#mpc-security-that-depends-on-participant-behavior)
* [TEEs: Three core security guarantees](#tees-three-core-security-guarantees)
  + [How TEE attestation works](#how-tee-attestation-works)
* [The trust model clash](#the-trust-model-clash)
* [What TEEs can (and can’t) fix in MPC deployments](#what-tees-can-and-cant-fix-in-mpc-deployments)
* [A cautionary tale: Rollback attacks with threshold signatures in TEEs](#a-cautionary-tale-rollback-attacks-with-threshold-signatures-in-tees)
* [Common TEE pitfalls](#common-tee-pitfalls)
* [Best practices for combining TEEs and MPC](#best-practices-for-combining-tees-and-mpc)
* [Layered trust beats either layer alone](#layered-trust-beats-either-layer-alone)

Threshold signature schemes, a form of multi-party computation (MPC) that lets a set of parties sign together without any one of them holding the key, are increasingly deployed inside trusted execution environments (TEEs). The combination is intended to amplify security for sensitive computations: MPC distributes trust across multiple independent parties, while TEEs root trust in the hardware manufacturer and its attestation infrastructure. But subtle issues can arise when running an MPC protocol inside a TEE without accounting for the untrusted host: for example, a malicious host could roll back the filesystem state after a threshold signer deletes a used pre-signature, causing the signer to reuse their nonce share and disclose their private key share.

So is this combination worth it? Provided you treat the TEE as a defense-in-depth layer rather than a substitute for a sound protocol, the answer is yes. This blog post discusses what TEE attestation can and can’t fix in MPC deployments, explores the pitfalls we see most often in audits, and covers best practices, such as incorporating strong attestation processes and binding them to the MPC parties’ identities.

## MPC: Security that depends on participant behavior

Before diving into how TEEs and MPC interact, we need to understand what MPC means and what security guarantees it offers. MPC is a cryptographic technique that allows multiple parties to jointly compute a function over their private inputs without revealing those inputs to each other.

The security of MPC protocols depends critically on assumptions about participant behavior. The cryptographic literature uses two primary security models:

**Semi-honest (honest-but-curious) security**: In this model, all participants follow the protocol exactly as specified, but they may try to learn additional information from the messages they receive during the protocol execution. Participants can try to learn more than they should, but they don’t deviate from the protocol specification.

**Malicious security**: This stronger model assumes participants may deviate arbitrarily from the protocol. A malicious participant might send incorrectly computed values, use wrong inputs, abort the protocol at strategic moments, and behave in ways designed to compromise security or learn private information.

This distinction is important in the context of TEEs. If a TEE attestation can cryptographically guarantee that all parties are running the correct protocol implementation, it effectively elevates semi-honest protocols to provide malicious security guarantees (at least against certain classes of attacks, as we’ll discuss later). But before delving into the details, let’s discuss how TEEs work.

## TEEs: Three core security guarantees

TEEs are secure areas within a processor that provide hardware-based protection for code and data, even from privileged software like operating systems or hypervisors. TEEs offer three core security guarantees:

**Confidentiality**: Data and code are encrypted in memory and accessible only from within the TEE. This ensures that even privileged system software cannot inspect the contents of the secure computation.

**Integrity**: The data and code are protected from tampering. Any attempt to modify the TEE’s memory or execution state from outside should be detected.

**Attestation**: Remote parties can cryptographically verify what code is running in the TEE. This allows external verifiers to gain assurance about the computation being performed and the legitimacy of the TEE without trusting the host system.

This last property is particularly crucial for building distributed systems with TEEs.

### How TEE attestation works

The attestation mechanism is at the heart of TEE security. When a TEE is manufactured, it’s provisioned with a private key and a corresponding certificate that chains back to a root certificate held by a trust anchor (typically the manufacturer).

When an attestation is requested, the TEE takes measurements (cryptographic hashes of the TEE software, configuration, and hardware state). These measurements are bundled into a “quote” (a manifest of these cryptographic hashes), which the TEE then signs with its private key.

To verify these attestations, a number of checks need to be performed. However, the checks necessary in the verification process aren’t uniformly defined and are somewhat vendor-specific. For instance, [Intel’s TDX documentation](https://cc-enabling.trustedservices.intel.com/intel-tdx-enabling-guide/02/infrastructure_setup/#:~:text=TD%20Quote%20Verification%20is%20the%20process%20by%20which%20a%20TD%20Quote%20is%20verified%20in%20a%20remote%20attestation%20flow.%20This%20verification%20can%20be%20done%20by%20any%20party%20and%20the%20checks%20performed%20are%20defined%20by%20this%20party.) states:

> TD Quote Verification is the process by which a TD Quote is verified in a remote attestation flow. This verification can be done by any party and the checks performed are defined by this party.

This places significant responsibility on developers, who might not fully understand what checks are required to ensure the security of the TEE deployment.

At a minimum, a proper verification process requires:

1. Verifying the quote signature
2. Verifying the certificate chain back to the trusted root
3. Verifying the actual measurements against known-good values (often stored in binary transparency logs)

This means deploying TEE-based systems involves not just cryptographic verification but also reproducible builds and binary transparency infrastructure. The measurements in the attestation quote are simply hashes; they don’t inherently indicate whether the code is correct or malicious. To verify that the TEE is running the intended software, what is required is a trusted source of reference measurements. Reproducible builds ensure that anyone can compile the same source code and arrive at identical binaries (and thus identical measurements). Binary transparency logs provide a tamper-evident record of what measurements correspond to what software versions, allowing verifiers to check that the TEE is running legitimate, audited code rather than a compromised variant. This piece is often overlooked in TEE deployments.

## The trust model clash

Here’s where things get interesting. Multi-party computation is fundamentally about distributing trust among multiple participants. No single party should be able to compromise the computation. TEEs, in contrast, centralize trust in the hardware manufacturer that controls the root certificate.

Another important threat model shift to consider is the fundamental inversion of traditional security assumptions in TEEs. Historically, we trusted the host operating system and built our security mode...