---
title: Securing the Quantum Age
url: https://www.paloaltonetworks.com/blog/2025/08/securing-the-quantum-age/
source: Palo Alto Networks Blog
date: 2025-08-15
fetch_date: 2025-10-07T00:50:55.874330
---

# Securing the Quantum Age

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/)
* Securing the Quantum Age

# Securing the Quantum Age

Link copied

By [Richu Channakeshava](/blog/author/richu-channakesha/ "Posts by Richu Channakeshava") and [Sean Morgan](/blog/author/sean-morgan/ "Posts by Sean Morgan")

Aug 14, 2025

7 minutes

[Announcement](/blog/category/announcement/)

[Points of View](/blog/category/points-of-view/)

[Public Sector](/blog/category/public-sector/)

[CISOs](/blog/tag/cisos/)

[Orion](/blog/tag/orion/)

[Quantum](/blog/tag/quantum/)

[Quantum Security](/blog/tag/quantum-security/)

[thought leadership](/blog/tag/thought-leadership/)

# Palo Alto Networks Announces New Quantum Security Innovations

*New Cryptography Inventory Tool, Quantum-Optimized Firewalls and PAN-OS 12.1 Enable Quantum Readiness*

The cybersecurity landscape is rapidly shifting due to a risk that’s quietly brewing in the background: the race to achieve quantum supremacy. Quantum computing has long promised to redefine what’s possible in technology, with its ability to solve complex problems exponentially faster than classical computers. This technological breakthrough promises many benefits likely to unlock trillions in economic value but will also introduce major new risks to the cryptographic foundations of modern cybersecurity. Despite this significance, quantum is still often dismissed as a problem too far away to worry about.

That’s changing with the convergence of AI and quantum computing. Researchers are now [leveraging AI to reduce some of the key barriers to quantum computing](https://thequantuminsider.com/2025/01/06/ai-for-quantum-error-correction-a-comprehensive-guide-to-using-artificial-intelligence-to-improve-quantum-error-correction/#:~:text=For%20instance%2C%20Google%20Quantum%20AI,in%20their%20superconducting%20quantum%20processors.), like automating qubit error correction and optimizing quantum algorithms. This means cryptographically relevant quantum computing (CRQC) – the point at which quantum systems can break today’s public key cryptography – could arrive sooner than the industry initially projected. [McKinsey (2024)](https://www.mckinsey.com/~/media/mckinsey/business%20functions/mckinsey%20digital/our%20insights/steady%20progress%20in%20approaching%20the%20quantum%20advantage/quantum-technology-monitor-april-2024.pdf) predicted a CRQC could break the most common public-key encryption algorithms as soon as 2027, while [Gartner (2025)](https://www.gartner.com/en/articles/post-quantum-cryptography) predicts that most conventional asymmetric cryptography would be unsafe to use by 2029.

Governments around the world have taken notice, developing new national quantum readiness strategies, including requirements to migrate to new quantum resistant Post-Quantum Cryptographic (PQC) standards, like those developed by the [United States National Institute of Standards and Technology (NIST)](https://csrc.nist.gov/projects/post-quantum-cryptography). Organizations are also experimenting with solutions beyond PQC migration, adopting technologies like Quantum Random Number Generation (QRNG) and Quantum Key Distribution (QKD) to build additional resilience to unforeseen computational advancements.

These emerging quantum readiness strategies have another common thread: emphasizing the critical role technology providers can play to proactively lead in the quantum era. At Palo Alto Networks, we’re meeting this moment by announcing a comprehensive suite of new quantum security capabilities as part of [PAN-OS 12.1 Orion](/blog/2025/08/paves-way-for-quantum-ready-security/) and our new quantum-optimized fifth-generation Next-Generation Firewalls (NGFW). These capabilities will empower organizations globally, across government and critical infrastructure, to accelerate their quantum readiness in alignment with emerging global and regional standards. Here is how our new capabilities can help your organization meet some of the fundamental imperatives of quantum readiness:

#### **Discover — Conducting Automated Cryptographic Inventories**

* *Challenge:* Establishing foundational visibility of your organization’s cryptographic usage is often cited as the best first step to kick-start quantum readiness. But legacy cryptographic inventory technologies have been insufficient, providing an incomplete and static snapshot of cryptography usage, failing to connect cryptography to sensitive data, and unable to empower users to take remediation action in real-time.
* *Solution:* Palo Alto Networks announced [Strata Cloud Manager's **‘***Quantum Readiness***’** view](https://live.paloaltonetworks.com/t5/community-blogs/unlock-your-quantum-defense-introducing-the-quantum-readiness/ba-p/1232791) and a forthcoming ‘*Cryptographic Inventory*’ insights dashboard to help you prepare for the quantum era. Organizations can gain visibility and take control of their cryptographic risk posture across users and applications from a single management interface. With *Quantum Readiness* view, we’re introducing several capabilities:

1. 1. Inventory and assess cryptography usage as secure, weak or vulnerable.
   2. Validate compliance with a range of government standards and regulations.
   3. Remediate and upgrade to PQCs through an inline workflow.

#### ![](/blog/wp-content/uploads/2025/08/Quantum-Readiness-View-230x144.png)

#### **Dep****loy — Migrating to PQC-Enabled Technologies**

* *Challenge*: Once an organization establishes visibility of its cryptographic risk posture through inventorying, then migrating high-risk systems to new PQC standards is another critical step in quantum readiness. This action is particularly time sensitive for organizations that hold data with long-term value. Adversaries are already conducting ‘harvest now, decrypt later’ attacks with the intent to decrypt once a quantum computer becomes available. Collaborating with technology partners who are proactive and transparent about their products’ supportability with PQC standards is a critical part of quantum readiness.
* *Solution:* PAN-OS 12.1 Orion, running on our fourth-generation and newly announced fifth-generation NGFWs, now includes support for all NIST standard algorithms: [FIPS 203: ML-KEM](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf?_cldee=s5r3Da8sdXFcbaKDCuF8O4zhdAu8J_Fgz56D_BvvI_kMXR7jDAXGMKxGH0k-Z4Qm&recipientid=contact-7a175f2aab22eb11a813000d3ab0a7d2-2617be969e124935a6cf769dc185f17c&esid=ee740eb2-6159-ef11-bfe2-7c1e52207b24), [FIPS 204: ML-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf?_cldee=s5r3Da8sdXFcbaKDCuF8O4zhdAu8J_Fgz56D_BvvI_kMXR7jDAXGMKxGH0k-Z4Qm&recipientid=contact-7a175f2aab22eb11a813000d3ab0a7d2-2617be969e124935a6cf769dc185f17c&esid=ee740eb2-6159-ef11-bfe2-7c1e52207b24), [FIPS 205: SLH-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf?_cldee=s5r3Da8sdXFcbaKDCuF8O4zhdAu8J_Fgz56D_BvvI_kMXR7jDAXGMKxGH0k-Z4Qm&recipientid=contact-7a175f2aab22eb11a813000d3ab0a7d2-2617be969e124935a6cf769dc185f17c&esid=ee740eb2-6159-ef11-bfe2-7c1e52207b24) and other prestandard algorithms – HQC, Classic McEliece, BIKE, Frodo. PAN-OS 12.1 Orion also delivers Quantum-safe site-to-site [VPN](https://live.paloaltonetworks.com/t5/community-blogs/palo-alto-networks-extends-support-for-quantum-safe-vpn-with-rfc/ba-p/585492) Tunnels and SSL/TLS sessions to protect against more immediate “harvest now, decrypt later” attacks.

Our implementation is focused on providing a more seamless transition to quantum-safe algorithms with prioritization:

1. *Global interoperability* through alignment with international standards and regional requirements, such as those in the [European Union](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography), [United Kingdom](https://www.ncsc.gov.uk/guidance...