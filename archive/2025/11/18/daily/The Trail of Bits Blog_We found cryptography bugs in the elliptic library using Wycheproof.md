---
title: We found cryptography bugs in the elliptic library using Wycheproof
url: https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/
source: The Trail of Bits Blog
date: 2025-11-18
fetch_date: 2025-11-19T03:12:51.740380
---

# We found cryptography bugs in the elliptic library using Wycheproof

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We found cryptography bugs in the elliptic library using Wycheproof

Markus Schiffermuller

November 18, 2025

[cryptography](/categories/cryptography/), [vulnerabilities](/categories/vulnerabilities/), [vulnerability-disclosure](/categories/vulnerability-disclosure/)

Page content

* [Methodology](#methodology)
* [Findings](#findings)
  + [CVE-2024-48949: EdDSA signature malleability](#cve-2024-48949-eddsa-signature-malleability)
  + [CVE-2024-48948: ECDSA signature verification error on hashes with leading zeros](#cve-2024-48948-ecdsa-signature-verification-error-on-hashes-with-leading-zeros)
* [On the importance of continuous testing](#on-the-importance-of-continuous-testing)
* [Coordinated disclosure timeline](#coordinated-disclosure-timeline)
  + [For CVE-2024-48949](#for-cve-2024-48949)
  + [For CVE-2024-48948](#for-cve-2024-48948)

Trail of Bits is publicly disclosing two vulnerabilities in [elliptic](https://www.npmjs.com/package/elliptic), a widely used JavaScript library for elliptic curve cryptography that is downloaded over 10 million times weekly and is used by close to 3,000 projects. These vulnerabilities, caused by missing modular reductions and a missing length check, could allow attackers to forge signatures or prevent valid signatures from being verified, respectively.

One vulnerability is still not fixed after a 90-day disclosure window that ended in October 2024. It remains unaddressed as of this publication.

![indutny/elliptic](/img/wycheproof-elliptic-library/wycheproof-1.png)

I discovered these vulnerabilities using [Wycheproof](https://github.com/C2SP/wycheproof), a collection of test vectors designed to test various cryptographic algorithms against known vulnerabilities. If you’d like to learn more about how to use Wycheproof, check out [this guide I published](https://appsec.guide/docs/crypto/wycheproof/).

In this blog post, I’ll describe how I used Wycheproof to test the elliptic library, how the vulnerabilities I discovered work, and how they can enable signature forgery or prevent signature verification.

![C2SP/wychproof](/img/wycheproof-elliptic-library/wycheproof-2.png)

## Methodology

During my internship at Trail of Bits, I wrote a [detailed guide](https://appsec.guide/docs/crypto/wycheproof/) on using Wycheproof for [the new cryptographic testing chapter of the Testing Handbook](https://appsec.guide/docs/crypto/). I decided to use the elliptic library as a real-world case study for this guide, which allowed me to discover the vulnerabilities in question.

I wrote a Wycheproof testing harness for the elliptic package, as described in the guide. I then analyzed the source code covered by the various failing test cases provided by Wycheproof to classify them as false positives or real findings. With an understanding of why these test cases were failing, I then wrote proof-of-concept code for each bug. After confirming they were real findings, I began the coordinated disclosure process.

## Findings

In total, I identified five vulnerabilities, resulting in five CVEs. Three of the vulnerabilities were minor parsing issues. I disclosed those issues in a public pull request against the repository and subsequently requested CVE IDs to keep track of them.

Two of the issues were more severe. I disclosed them privately using the GitHub advisory feature. Here are some details on these vulnerabilities.

### CVE-2024-48949: EdDSA signature malleability

This issue stems from a missing out-of-bounds check, which is specified in the [NIST FIPS 186-5](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf#page=40) in section 7.8.2, “HashEdDSA Signature Verification”:

> Decode the first half of the signature as a point `R` and the second half of the signature as an integer `s`. Verify that the integer `s` is in the range of `0 ≤ s < n`.

In the elliptic library, the check that `s` is in the range of `0 ≤ s < n`, to verify that it is not outside the order `n` of the generator point, is never performed. This vulnerability allows attackers to forge new valid signatures, `sig'`, though only for a known signature and message pair, `(msg, sig)`.

$$
\begin{aligned}
\text{Signature} &= (msg, sig) \\
sig &= (R||s) \\
s' \bmod n &== s
\end{aligned}
$$

The following check needs to be implemented to prevent this forgery attack.

```
if (sig.S().gte(sig.eddsa.curve.n)) {
    return false;
}
```

Forged signatures could break the consensus of protocols. Some protocols would correctly reject forged signature message pairs as invalid, while users of the elliptic library would accept them.

### CVE-2024-48948: ECDSA signature verification error on hashes with leading zeros

The second issue involves the ECDSA implementation: valid signatures can fail the validation check.

These are the Wycheproof test cases that failed:

* `[testvectors_v1/ecdsa_secp192r1_sha256_test.json][tc296]` special case hash
* `[testvectors_v1/ecdsa_secp224r1_sha256_test.json][tc296]` special case hash

Both test cases failed due to a specifically crafted hash containing four leading zero bytes, resulting from hashing the hex string 343236343739373234 using SHA-256:

```
00000000690ed426ccf17803ebe2bd0884bcd58a1bb5e7477ead3645f356e7a9
```

We’ll use the secp192r1 curve test case to illustrate why the signature verification fails.
The function responsible for verifying signatures for elliptic curves is located in `lib/elliptic/ec/index.js`:

```
EC.prototype.verify = function verify(msg, signature, key, enc) {
  msg = this._truncateToN(new BN(msg, 16));
  ...
}
```

The message must be hashed before it is parsed to the `verify` function call, which occurs outside the elliptic library. According to [FIPS 186-5](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf#page=34), section 6.4.2, “ECDSA Signature Verification Algorithm,” the hash of the message must be adjusted based on the order `n` of the base point of the elliptic curve:

> If `log2(n) ≥ hashlen`, set `E = H`. Otherwise, set `E` equal to the leftmost `log2(n)` bits of `H`.

To achieve this, the `_truncateToN` function is called, which performs the necessary adjustment. Before this function is called, the hashed message, `msg`, is converted from a hex string or array into a number object using `new` `BN(msg, 16)`.

```
EC.prototype._truncateToN = function _truncateToN(msg, truncOnly) {
  var delta = msg.byteLength() * 8 - this.n.bitLength();
  if (delta > 0)
    msg = msg.ushrn(delta);
  ...
};
```

The delta variable calculates the difference between the size of the hash and the order `n` of the current generator for the curve. If `msg` occupies more bits than `n`, it is shifted by the difference. For this specific test case, we use secp192r1, which uses 192 bits, and SHA-256, which uses 256 bits. The hash should be shifted by 64 bits to the right to retain the leftmost 192 bits.

The issue in the elliptic library arises because the `new BN(msg, 16)` conversion removes leading zeros, resulting in a smaller hash that takes up fewer bytes.

```
690ed426ccf17803ebe2bd0884bcd58a1bb5e7477ead3645f356e7a9
```

During the delta calculation, `msg.byteLength()` then returns 28 bytes instead of 32.

```
EC.prototype._truncateToN = function _truncateToN(msg, truncOnly) {
  var delta = msg.byteLength() * 8 - this.n.bitLength();
  ...
};
```

This miscalculation results in an incorrect delta of `32 = (288 - 192)` instead of `64 = (328 - 192)`. Consequently, the hashed message is not shifted correctly, causing verification to fail. This issue causes valid signatures to be rejected if the message hash contains enough leading zeros, with a probability of 2-32.

To fix this issue, an additional argument should be added to the verification function to allow the hash size to be parsed:

```
EC.prototype.verify = function verify(msg, signature, key, enc, msgSize) {
  msg = this._tr...