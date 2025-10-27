---
title: The FIPS Compliance of HKDF
url: https://words.filippo.io/dispatches/fips-hkdf/
source: Filippo Valsorda
date: 2024-09-26
fetch_date: 2025-10-06T18:23:35.388399
---

# The FIPS Compliance of HKDF

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

25 Sep 2024

# The FIPS Compliance of HKDF

HKDF is an HMAC-based key-derivation function specified in RFC 5869. It’s nice and we generally like using it. FIPS (Federal Information Processing Standards) is used generally as a moniker for the set of standards, recommendations, and guidance published by the U.S. National Institute of Standards and Technology, and more specifically for FIPS 140, the standard concerning the validation of cryptographic modules. There are a number of regulatory settings (such as FedRAMP) that require FIPS 140 compliance, and it often doesn’t let us have nice things. As of earlier this year, I decided to finally bite the bullet and [pursue a FIPS 140-3 validation](https://github.com/golang/go/issues/69536) for the Go cryptography standard library, trying to retain as many nice things as possible, so I am diving into the finer details of what’s allowed and what’s not.

The FIPS compliance of HKDF is a somewhat confusing and controversial topic, partially because the normative reference is split over at least four separate documents, but in practice it’s approved for almost any purpose.

[NIST SP 800-133 Rev. 2](https://csrc.nist.gov/pubs/sp/800/133/r2/final), Recommendation for Cryptographic Key Generation, discusses in Section 6.2 the derivation of symmetric keys, and presents two categories of key-derivation methods:

1. one-step KDFs, defined in SP 800-108 for general purpose use or in SP 800-56C for use on the shared secrets produced by key-agreement schemes;[1](#fn:other)
2. two-step extraction-then-expansion key-derivation procedures, defined in Section 6.3 (extraction) and SP 800-108 (expansion) for general purpose use or again in SP 800-56C for use as part of key-agreement schemes.

Here the path bifurcates, depending on whether HKDF is being used as part of a key-agreement scheme. Key agreement is defined as

> A (pair-wise) key-establishment procedure in which the resultant secret keying material is a function of information contributed by both participants so that neither party can predetermine the value of the secret keying material independently of the contributions of the other party; contrast with key transport.

… essentially Diffie-Hellman.[2](#fn:kem) (See also [FIPS 140-3 Implementation Guidance](https://csrc.nist.gov/CSRC/media/Projects/cryptographic-module-validation-program/documents/fips%20140-3/FIPS%20140-3%20IG.pdf) D.F.)

![The dramatic crossroads meme, but both roads lead to light, one is labeled key-agreement, the other symmetric key derivation](https://assets.buttondown.email/images/e75a4c48-7e13-4454-af28-b7c080b086bc.jpg)

## HKDF as part of key-agreement

Let’s start with the key-agreement case, as it’s somewhat more straightforward.

[NIST SP 800-56C Rev. 2](https://csrc.nist.gov/pubs/sp/800/56/c/r2/final), Recommendation for Key-Derivation Methods in Key-Establishment Schemes, presents a Two-Step Key Derivation in Section 5. As acknowledged at the bottom of Section 5.1, when instantiated with HMAC, an empty IV, and a Feedback Mode KDF for expansion, this is equivalent to HKDF.

> RFC 5869 specifies a version of the above extraction-then-expansion key-derivation procedure using HMAC for both the extraction and expansion steps.

The salt can be negotiated, a fixed value, or all zeroes, like in HKDF. Using the output of one Extract step for multiple Expand operations is explicitly approved, as long as the same HMAC function is used in both.

The input key material can be concatenated with other values, a common practice with Diffie-Hellman contributions:

> this Recommendation permits the use of a “hybrid” shared secret of the form Z ′ = Z || T, a concatenation consisting of a “standard” shared secret Z that was generated during the execution of a key-establishment scheme (as currently specified in [SP 800-56A] or [SP 800-56B]) followed by an auxiliary shared secret T that has been generated using some other method

HKDF as part of key-agreement can be CAVP-tested stand-alone as “KDA HKDF Sp800-56Cr2” per IG D.F.

[Edit 2025-02-09: replaced with the following section.] ~~Note that the one-step key derivation defined in SP 800-56C is a counter-based KDF (i.e. neither HKDF-Extract nor HKDF-Expand) so it doesn’t seem to be FIPS-compliant to skip either the extract or expand step as part of key-agreement.~~

### HKDF-Extract as KDA OneStepNoCounter

The one-step key derivation defined in SP 800-56C is a counter-based KDF, so it doesn’t allow HKDF-Extract on its own, without HKDF-Expand. However, Implementation Guidance D.P “SP 800-56Crev2 One-Step Key Derivation Function Without a Counter” introduces a variant without a counter if the output size is less than or equal to the hash output size.

When using HMAC, it boils down to `HMAC(salt, Z || FixedInfo)`, aka HKDF-Extract.

This can be CAVP-tested as “KDA OneStepNoCounter Sp800-56Cr2”.

## HKDF as a general-purpose KDF

Until recently I was under the impression that HKDF was only allowed as part of key-agreement. That’s not the case!

### HKDF-Expand as a SP 800-108 KDF

HKDF-Expand on its own turns out to be a mode of [NIST SP 800-108 Rev. 1 Upd. 1](https://csrc.nist.gov/pubs/sp/800/108/r1/upd1/final), Recommendation for Key Derivation Using Pseudorandom Functions, which defines approved general-purpose KDFs (and is referenced by SP 800-133 above for one-step KDFs).

I initially thought that not to be the case, because the Feedback Mode KDF is defined in Section 4.2 as computing `HMAC(K_in, K(i-1) || i || FixedInfo)` while HKDF-Expand computes `HMAC(K_in, K(i-1) || info || i)`. Note the order of counter `i` and `info`. Everything else in the SP 800-108 Feedback Mode KDF could be tweaked to land at HKDF, but I found nothing in the text that allowed swapping the order.

![The Process from SP 800-108 Section 4.2](https://assets.buttondown.email/images/54ac7c14-249e-4c90-a5f0-28da94e9c527.png)

However, SP 800-56C claims explicitly that HKDF is a profile of its two-step key-derivation method, and describes the expansion step simply by reference to SP 800-108!

> One of the general-purpose, PRF-based key-derivation functions defined in SP 800-108 shall be used for key expansion.

To confirm this, I went looking at the [ACVP tests for SP 800-108](https://pages.nist.gov/ACVP/draft-celi-acvp-kbkdf.html#section-7.3.2), and indeed there’s a `fixedDataOrder` parameter which “describes where the counter appears in the fixed data” and that can be set to `"after fixed data"`. The relevant ACVP test vectors[3](#fn:mystery) [pass when applied to HKDF-Expand](https://go.dev/play/p/zEmD3VIHtB7), proving that it’s an approved version of SP 800-108.

Note that in order to use HKDF-Expand in the approved mode of operation for this purpose, the FIPS 140 cryptographic module will need to include the SP 800-108 Feedback KDF in its certificate.

### HKDF-Extract per SP 800-133

Ok, so HKDF-Expand is a general purpose KDF, but what about HKDF-Extract?

SP 800-133 Rev. 2, published in 2020, added a new method to Section 6.3, Symmetric Keys Produced by Combining (Multiple) Keys and Other Data. The new Method 3, called “a key-extraction process” is simply `HMAC(salt, K || … || D || …)` aka HKDF-Extract!

While the other methods require multiple keys, or both a key and other data, Method 3 requires n (the number of keys) ≥ 1 and m (the other data) ≥ 0, so it’s explicitly allowed even with a single key as input. The salt can be a secret or non-secret value. Alternative orderings of keys and data are explicitly permitted.

This is confirmed by IG 2.4.B, which states “the underlying functions performed within the [n.d.a. HKDF-based] TLS 1.3 KDF map to NIST approved standards, namely: SP 800-133rev2 (Section 6.3 Option #3), SP 800-56Crev2, and SP 800-108”.

There is no CAVP testing or CAST requirement for SP 800-133 Section 6.3 but IG D.H requires Vendor A...