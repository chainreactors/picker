---
title: Building cryptographic agility into Sigstore
url: https://blog.trailofbits.com/2026/01/29/building-cryptographic-agility-into-sigstore/
source: The Trail of Bits Blog
date: 2026-01-29
fetch_date: 2026-01-30T04:02:40.754071
---

# Building cryptographic agility into Sigstore

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Building cryptographic agility into Sigstore

[Riccardo Schirone](/authors/riccardo-schirone/)

January 29, 2026

[cryptography](/categories/cryptography/), [open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/)

Page content

* [Sigstore’s cryptographic constraints](#sigstores-cryptographic-constraints)
* [The dangers of cryptographic flexibility](#the-dangers-of-cryptographic-flexibility)
* [The solution: Controlled cryptographic flexibility](#the-solution-controlled-cryptographic-flexibility)
* [The implementation](#the-implementation)
  + [Phase 1: Establishing common ground](#phase-1-establishing-common-ground)
  + [Phase 2: Service-level updates](#phase-2-service-level-updates)
  + [Phase 3: Client integration](#phase-3-client-integration)
  + [Validation: Proving it works](#validation-proving-it-works)
* [Cryptographic flexibility in action](#cryptographic-flexibility-in-action)
* [Future-proofing Sigstore](#future-proofing-sigstore)

Software signatures carry an invisible expiration date. The container image or firmware you sign today might be deployed for 20 years, but the cryptographic signature protecting it may become untrustworthy within 10 years. SHA-1 certificates become worthless, weak RSA keys are banned, and quantum computers may crack today’s elliptic curve cryptography. The question isn’t whether our current signatures will fail, but whether we’re prepared for when they do.

Sigstore, an open-source ecosystem for software signing, recognized this challenge early but initially chose security over flexibility by adopting new cryptographic algorithms as older ones became obsolete. By hard coding ECDSA with P-256 curves and SHA-256 throughout its infrastructure, Sigstore avoided the dangerous pitfalls that have plagued other crypto-agile systems. This conservative approach worked well during early adoption, but as Sigstore’s usage grew, the rigidity that once protected it began to restrict its utility.

Over the past two years, Trail of Bits has collaborated with the Sigstore community to systematically address the limitations of aging cryptographic signatures. Our work established a centralized algorithm registry in the Protobuf specifications to serve as a single source of truth. Second, we updated Rekor and Fulcio to accept configurable algorithm restrictions. And finally, we integrated these capabilities into Cosign, allowing users to select their preferred signing algorithm when generating ephemeral keys. We also developed Go implementations of post-quantum algorithms LMS and ML-DSA, demonstrating that the new architecture can accommodate future cryptographic standards. Here is what motivated these changes, what security considerations shaped our approach, and how to use the new functionality.

## Sigstore’s cryptographic constraints

Sigstore hard codes ECDSA with P-256 curves and SHA-256 throughout most of its ecosystem. This rigidity is a deliberate design choice. From Fulcio certificate issuance to Rekor transparency logs to Cosign workflows, most steps default to this same algorithm. Cryptographic agility has historically led to serious security vulnerabilities, and focusing on a limited set of algorithms reduces the chance of something going wrong.

This conservative approach, however, has created challenges as the ecosystem has matured. Various organizations and users have vastly different requirements that Sigstore’s rigid approach cannot accommodate. Here are some examples:

* **Compliance-driven organizations** might need NIST-standard algorithms to meet regulatory requirements.
* **Open-source maintainers** may want to sign artifacts without making cryptographic decisions, relying on secure defaults from the public Sigstore instance.
* **Security-conscious enterprises** may want to deploy internal Sigstore instances using only post-quantum cryptography.

Furthermore, software artifacts remain in use for decades, meaning today’s signatures must stay verifiable far into the future, and the cryptographic algorithm used today might not be secure 10 years from now.

These challenges can be addressed only if Sigstore allows for a certain degree of cryptographic agility. The goal is to enable controlled cryptographic flexibility without repeating the security issues that have affected other crypto-agile systems. To address this, the Sigstore community has developed a [design document](https://docs.google.com/document/d/18vTKFvTQdRt3OGz6Qd1xf04o-hugRYSup-1EAOWn7MQ/edit?tab=t.0#heading=h.op2lvfrgiugr) outlining how to introduce cryptographic agility while maintaining strong security guarantees.

## The dangers of cryptographic flexibility

The most infamous example of problems caused by cryptographic flexibility is [the JWT](https://jwt.io/introduction) `alg:` `none` vulnerability, where some JWT libraries treated tokens signed with the `none` algorithm as valid tokens, allowing anyone to forge arbitrary tokens and “sign” whatever payload they wanted. Even more subtle is the [RSA/HMAC confusion attack in JWT](https://portswigger.net/web-security/jwt/algorithm-confusion), where a mismatch between what kind of algorithm a server expects and what it receives allows anyone with knowledge of the RSA public key to forge tokens that pass verification.

The fundamental problem in both cases is in-band algorithm signaling, which allows the data to specify how it should be protected. This creates an opportunity for attackers to manipulate the algorithm choice to their advantage. As the cryptographic community has learned through painful experience, cryptographic agility introduces significant complexity, leading to more code and increased potential attack vectors.

## The solution: Controlled cryptographic flexibility

Instead of allowing users to mix and match any algorithms they want, Sigstore introduced predefined algorithm suites, which are complete packages that specify exactly which cryptographic components work together.

For example, `PKIX_ECDSA_P256_SHA_256` not only includes the signing algorithm (ECDSA P-256), but also mandates SHA-256 for hashing. A `PKIX_ECDSA_P384_SHA_384` suite pairs ECDSA P-384 with SHA-384, and `PKIX_ED25519` uses Ed25519 and SHA-512. Users can choose between these suites, but they can’t create dangerous combinations, such as ECDSA P-384 with MD5.

Critically, the choice of which algorithm to use comes from out-of-band negotiation, meaning it’s determined by configuration or policy, not by the data being signed. This prevents the in-band signaling attacks that have plagued other systems.

## The implementation

To enable cryptographic agility across the Sigstore ecosystem, we needed to make coordinated changes that would work together seamlessly. Cryptography is used in several places within the Sigstore ecosystem; however, we primarily focused on enabling clients to change the signing algorithm used to sign and verify artifacts, as this would have a significant impact on end users. We tackled this change in three phases.

### Phase 1: Establishing common ground

We introduced a centralized [algorithm registry](https://github.com/sigstore/protobuf-specs/blob/966b43d006e7fc938b30724933af34c8e351f2a1/protos/sigstore_common.proto#L46-L129) in the Protobuf specifications that defines all [allowed algorithms](https://github.com/sigstore/sigstore/blob/1e63a2159e71d968a5fa46215280103844797ee8/pkg/signature/algorithm_registry.go#L154) and their details. We also implemented [default mappings](https://github.com/sigstore/sigstore/blob/1e63a2159e71d968a5fa46215280103844797ee8/pkg/signature/algorithm_registry.go#L238-L298) from key types to signing algorithms (e.g., ECDSA P-256 keys automatically use ECDSA P-256 + SHA-256), eliminating ambiguity and providing a single source of truth for all Sigstore components.

### Phase 2: Service-level updates...