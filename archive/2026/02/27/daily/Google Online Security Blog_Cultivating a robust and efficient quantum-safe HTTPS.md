---
title: Cultivating a robust and efficient quantum-safe HTTPS
url: http://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html
source: Google Online Security Blog
date: 2026-02-27
fetch_date: 2026-02-28T03:50:13.902141
---

# Cultivating a robust and efficient quantum-safe HTTPS

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Cultivating a robust and efficient quantum-safe HTTPS](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html "Cultivating a robust and efficient quantum-safe HTTPS")

February 27, 2026

Posted by Chrome Secure Web and Networking Team

Today we're announcing a new program in Chrome to make HTTPS certificates secure against quantum computers. The Internet Engineering Task Force (IETF) recently created a working group, [PKI, Logs, And Tree Signatures](https://datatracker.ietf.org/wg/plants/about/) (“PLANTS”), aiming to address the performance and bandwidth challenges that the increased size of [quantum-resistant cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) introduces into TLS connections requiring [Certificate Transparency](https://certificate.transparency.dev/howctworks/) (CT). We recently [shared](https://blog.google/innovation-and-ai/technology/safety-security/the-quantum-era-is-coming-are-we-ready-to-secure-it/) our call to action to secure quantum computing and have written about challenges introduced by quantum-resistant cryptography and some of the steps we’ve taken to address them in earlier [blog](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html) [posts](https://blog.chromium.org/2024/05/advancing-our-amazing-bet-on-asymmetric.html).

To ensure the scalability and efficiency of the ecosystem, Chrome has no immediate plan to add traditional X.509 certificates containing post-quantum cryptography to the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md). Instead, Chrome, in collaboration with other partners, is developing an [evolution](https://drive.google.com/file/d/1KQXAGBHXR4S_prwFrZlyfA6DrpvfJwuJ/view) of HTTPS certificates based on [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) (MTCs), currently in development in the PLANTS working group. MTCs replace the heavy, serialized chain of signatures found in traditional PKI with compact [Merkle Tree proofs](https://research.swtch.com/tlog#merkle_trees). In this model, a Certification Authority (CA) signs a single "Tree Head" representing potentially millions of certificates, and the "certificate" sent to the browser is merely a lightweight proof of inclusion in that tree.

### Why MTCs?

MTCs enable the adoption of robust post-quantum algorithms without incurring the massive bandwidth penalty of classical X.509 certificate chains. They also decouple the security strength of the corresponding cryptographic algorithm from the size of the data transmitted to the user. By shrinking the authentication data in a TLS handshake to the absolute minimum, MTCs aim to keep the post-quantum web as fast and seamless as today’s internet, maintaining high performance even as we adopt stronger security. Finally, with MTCs, transparency is a fundamental property of issuance: it is impossible to issue a certificate without including it in a public tree. This means the security properties of today’s CT ecosystem are included by default, and without adding extra overhead to the TLS handshake as CT does today.

### Chrome’s MTC Propagation Plan

Chrome is already experimenting with MTCs with real internet traffic, and we intend to gradually build out our deployment such that MTCs provide a robust quantum-resistant HTTPS available for use throughout the internet.

Broadly speaking, our rollout spans three distinct phases.

* **Phase 1 (UNDERWAY):** In [collaboration](https://www.google.com/url?q=https://blog.cloudflare.com/bootstrap-mtc/&sa=D&source=docs&ust=1770666818817662&usg=AOvVaw3YI8DKCxh8bqHxgrDZe04O) with Cloudflare, we are conducting a feasibility study to evaluate the performance and security of TLS connections relying on MTCs. To ensure a seamless and secure experience for Chrome users who might encounter an MTC, every MTC-based connection is backed by a traditional, trusted X.509 certificate during this experiment. This "fail safe" allows us to measure real-world performance gains and verify the reliability of MTC issuance without risking the security or stability of the user's connection.

* **Phase 2 (Q1 2027):** Once the core technology is validated, we intend to invite CT Log [operators](https://certificate.transparency.dev/logs/) with at least one “[usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)” log in Chrome before February 1, 2026 to participate in the initial bootstrapping of public MTCs. These organizations have already demonstrated the operational excellence and high-availability infrastructure required to run global security services that underpin TLS connections in Chrome. Since MTC technology shares significant architectural similarities with CT, these operators are uniquely qualified to ensure MTCs are able to get off the ground quickly and successfully.

* **Phase 3 (Q3 2027):** Early in Phase 2, we will finalize the requirements for onboarding additional CAs into the new Chrome Quantum-resistant Root Store (CQRS) and corresponding Root Program that only supports MTCs. This will establish a modern, purpose-built trust store specifically designed for the requirements of a post-quantum web. The Chrome Quantum-resistant Root Program will operate alongside our [existing Chrome Root Program](https://security.googleblog.com/2023/05/how-chrome-root-program-keeps-users-safe.html) to ensure a risk-managed transition that maintains the highest levels of security for all users. This phase will also introduce the ability for sites to opt in to downgrade protections, ensuring that sites that only wish to use quantum-resistant certificates can do so.

This area is evolving rapidly. As these phases progress, we will continue our active participation in standards bodies such as the IETF and [C2SP](https://github.com/C2SP/C2SP), ensuring that insights gathered from our efforts flow back towards standards, and that changes in standards are supported by Chrome and the CQRS.

### Cultivating new practices and policy for a more secure and reliable web

We view the adoption of MTCs and a quantum-resistant root store as a critical opportunity to ensure the robustness of the foundation of today’s ecosystem. By designing for the specific demands of a modern, agile, internet, we can accelerate the adoption of post-quantum resilience for all web users.

We expect this modern foundation for TLS to evolve beyond current ecosystem norms and emphasize themes of security, simplicity, predictability, transparency and resilience. These properties might be expressed by:

* Grounding our approach in first principles, prioritizing only elements essential for establishing a secure connection between a server and a client.
* Utilizing [ACME](https://datatracker.ietf.org/doc/html/rfc8555)-only workflows to reduce complexity and ensure the cryptographic agility required to respond to future threats across the entire ecosystem.
* Upgrading to a modern framework for communicating revocation status. This allows for the replacement of legacy CRLs and streamlined requirements to focus only on key compromise events.
* Exploring “reproducible” [Domain Control Validation](https://security.googleblog.com/2025/12/https-certificate-industry-phasing-out.html) to create a model where proofs of domain control are publicly and persistently available, empowering any party to independently verify the legitimacy of a validation (i.e., serve as a “DCV Monitor”).
* Enhancing the CA inclusion model to prioritize proven operational excellence. By establishing a pathway where prospective MTC CA Owners can fir...