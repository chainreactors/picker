---
title: Post-Quantum Cryptography in 2025 – Migration Paths, Early Movers and CISO/RedTeam Impact
url: https://www.darknet.org.uk/2025/10/post-quantum-cryptography-in-2025-migration-paths-early-movers-and-ciso-redteam-impact/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:08:31.641476
---

# Post-Quantum Cryptography in 2025 – Migration Paths, Early Movers and CISO/RedTeam Impact

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Post-Quantum Cryptography in 2025 – Migration Paths, Early Movers and CISO/RedTeam Impact

October 22, 2025

Views: 285

Quantum-safe cryptography has moved from planning to deployment. In August 2024, NIST approved the first post-quantum Federal Information Processing Standards, which it described as the moment to “begin transitioning to the new standards,” a clear signal that the window for preparation has closed and implementation must start ([NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)). For organisations with data retention horizons beyond five years, the harvest-now, decrypt-later threat is no longer theoretical; it is an operational risk.

![Post-Quantum Cryptography in 2025 - Migration Paths, Early Movers and CISORedTeam Impact](https://www.darknet.org.uk/wp-content/uploads/2025/10/Post-Quantum-Cryptography-in-2025-Migration-Paths-Early-Movers-and-CISO-RedTeam-Impact-640x427.jpg)

## PQC Overview

NIST’s approvals covered three standards, including ML-KEM for key encapsulation and ML-DSA for signatures, and the agency reiterated the migration message in its Computer Security Resource Center note announcing FIPS 203, 204, and 205 ([Announcing Approval of Three FIPS for Post-Quantum Cryptography](https://csrc.nist.gov/news/2024/postquantum-cryptography-fips-approved)). In March 2025, the institute added another piece to the portfolio by selecting HQC as the fifth algorithm moving into the standards pipeline, which further cements the direction of travel for implementers ([NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)).

Real-world deployments are arriving. OpenSSH documents that it introduced a second post-quantum key agreement, mlkem768x25519-sha256, which will become the default scheme in OpenSSH 10.0 in April 2025. This change affects server-side defaults in one of the most widely used secure transport stacks (OpenSSH: Post-Quantum Cryptography). At the same time, Cloudflare reported that post-quantum TLS to origin is available for customers today, and it has measured PQC usage across a meaningful slice of live traffic ([Cloudflare now uses post-quantum cryptography to talk to origins](https://blog.cloudflare.com/post-quantum-to-origins/)).

## What’s Happening in the Industry

### Case study: OpenSSH shifts to a PQ-hybrid default

OpenSSH’s maintainers explain that the project first offered post-quantum key agreement in version 9.0, then added ML-KEM + X25519 as a second option in version 9.9, setting it as the default in version 10.0. In version 10.1, users are warned when sessions fall back to non-PQ key exchange ([OpenSSH: Post-Quantum Cryptography](https://www.openssh.com/pq.html)). That decision impacts millions of systems, since enterprise SSH baselines often track OpenSSH defaults, and it raises the floor for long-term confidentiality of administrative traffic.

### Case study: Post-quantum to origin at CDN scale

Cloudflare’s engineering post shows customers can enable post-quantum TLS from edge to origin, which turns PQ into a practical control for production websites rather than a lab pilot ([Cloudflare now uses post-quantum cryptography to talk to origins](https://blog.cloudflare.com/post-quantum-to-origins/)). The company’s broader telemetry update also quantified PQ handshakes as a non-trivial share of global TLS 1.3 connections, indicating measurable adoption across the open Internet ([The state of the post-quantum Internet](https://blog.cloudflare.com/pq-2024/)).

### Case study: PQ-secure SSH access on a major developer platform

GitHub’s security engineering team announced new post-quantum-secure SSH key exchange support, documenting the algorithms and operational impact for developers who manage code over SSH at scale ([Post-quantum security for SSH access on GitHub](https://github.blog/engineering/platform-security/post-quantum-security-for-ssh-access-on-github/)). This matters because developer workflows often hold the keys to production, so PQ-hybrid adoption in developer tooling reduces long-term exposure of source code and deployment pipelines.

## Detection Vectors and TTPs

Hybrid deployments introduce detectable artifacts. Larger ClientHello messages, additional key shares, and PQ-hybrid cipher suite identifiers are all signals that can help asset discovery. Network defenders can use these markers to find PQ-enabled services, while red teams can profile downgrade behaviour when middleboxes or legacy clients force non-PQ fallbacks. For context on what a mature migration looks like in practice, see our internal analysis of enterprise readiness that reviews hybrid TLS rollouts and control points across load balancers and proxies ([Post-Quantum Cryptography Implementation Enterprise-Readiness Analysis](https://www.darknet.org.uk/2025/06/post-quantum-cryptography-implementation-enterprise-readiness-analysis/)).

Harvest-now, decrypt-later changes logging priorities. Teams should tag encrypted data stores with retention greater than five years, then monitor who exports those archives and from where. Suppose you need a public benchmark for adoption pace to calibrate expectations. In that case, Cloudflare’s telemetry provides an Internet-wide reference point that your own metrics can track against ([The state of the post-quantum Internet](https://blog.cloudflare.com/pq-2024/)).

## Industry Response

The UK’s National Cyber Security Centre has started publishing concrete timelines for migration and guidance on planning, which moves PQC from optional research into programme work with milestones ([Timelines for migration to post-quantum cryptography](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines)). That direction aligns with the US position where the NSA’s CNSA 2.0 materials set expectations for quantum-resistant algorithms across National Security Systems by the mid-2030s ([Post-Quantum Cybersecurity Resources](https://www.nsa.gov/Cybersecurity/Post-Quantum-Cybersecurity-Resources/)).

Vendors are packaging enablement paths. AWS documents a hybrid post-quantum option for SSH in its Transfer Family service, which gives enterprises a managed way to test PQ-hybrid handshakes against real workloads without rebuilding their stack ([Using hybrid post-quantum key exchange with AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/post-quantum-security-policies.html)). As more platforms follow OpenSSH and GitHub, expect your third-party risk reviews to include PQ controls and downgrade handling.

## CISO Playbook

* Run a cryptographic inventory. Tag TLS endpoints, SSH bastions, VPNs, and databases that carry data with retention beyond five years, then prioritise PQ-hybrid for those paths first ([NIST Releases First 3 Finalized Post-Quantum Encryption ...