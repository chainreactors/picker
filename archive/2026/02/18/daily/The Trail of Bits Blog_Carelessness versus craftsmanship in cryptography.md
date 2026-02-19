---
title: Carelessness versus craftsmanship in cryptography
url: https://blog.trailofbits.com/2026/02/18/carelessness-versus-craftsmanship-in-cryptography/
source: The Trail of Bits Blog
date: 2026-02-18
fetch_date: 2026-02-19T04:21:27.067865
---

# Carelessness versus craftsmanship in cryptography

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Carelessness versus craftsmanship in cryptography

[Opal Wright](/authors/opal-wright/)

February 18, 2026

[cryptography](/categories/cryptography/), [vulnerabilities](/categories/vulnerabilities/), [vulnerability-disclosure](/categories/vulnerability-disclosure/)

Page content

* [Reusing initialization vectors](#reusing-initialization-vectors)
* [aes-js and pyaes](#aes-js-and-pyaes)
  + [The default IV problem](#the-default-iv-problem)
  + [Other issues](#other-issues)
    - [Lack of modern cipher modes](#lack-of-modern-cipher-modes)
    - [Timing problems](#timing-problems)
    - [Lack of updates](#lack-of-updates)
    - [Developer response](#developer-response)
* [Craftsmanship](#craftsmanship)
  + [strongMan VPN Manager](#strongman-vpn-manager)
  + [Doing it right](#doing-it-right)
* [A difference in approaches](#a-difference-in-approaches)

Two popular AES libraries, aes-js and pyaes, “helpfully” provide a default IV in their AES-CTR API, leading to a large number of key/IV reuse bugs. These bugs potentially affect thousands of downstream projects. When we shared one of these bugs with an affected vendor, strongSwan, the maintainer provided a model response for security vendors. The aes-js/pyaes maintainer, on the other hand, has taken a more… cavalier approach.

Trail of Bits doesn’t usually make a point of publicly calling out specific products as unsafe. Our motto is that we don’t just fix bugs—we fix software. We do better by the world when we work to address systemic threats, not individual bugs. That’s why we work to provide static analysis tools, auditing tools, and documentation for folks looking to implement cryptographic software. When you improve systems, you improve software.

But sometimes, a single bug in a piece of software has an outsized impact on the cryptography ecosystem, and we need to address it.

This is the story of how two developers reacted to a security problem, and how their responses illustrate the difference between carelessness and craftsmanship.

## Reusing initialization vectors

Reusing a key/IV pair leads to serious security issues: if you encrypt two messages in CTR mode or GCM with the same key and IV, then anybody with access to the ciphertexts can recover the XOR of the plaintexts, and that’s a very bad thing. Like, “[your security is going to get absolutely wrecked](https://www.nsa.gov/portals/75/documents/about/cryptologic-heritage/historical-figures-publications/publications/coldwar/venona_story.pdf)” bad. One of our cryptography analysts has written an [excellent introduction to the topic](https://blog.trailofbits.com/2024/09/13/friends-dont-let-friends-reuse-nonces/), in case you’d like more details; it’s great reading.

Even if the XOR of the plaintexts doesn’t help an attacker, it still makes the encryption very brittle: if you’re encrypting all your secrets by XORing them against a fixed mask, then recovering just one of those secrets will reveal the mask. Once you have that, you can recover all the other secrets. *Maybe* all your secrets will remain secure against prying eyes, but the fact remains: in the very best case, the security of *all* your secrets becomes no better than the security of your *weakest* secret.

## aes-js and pyaes

As you might guess from the names, [aes-js](https://github.com/ricmoo/aes-js) and [pyaes](https://github.com/ricmoo/pyaes) are JavaScript and Python libraries that implement the AES block cipher. They’re pretty widely used: the Node.js package manager (npm) repository lists [850 aes-js dependents](https://www.npmjs.com/package/aes-js?activeTab=dependents) as of this writing, and GitHub estimates that over 700,000 repositories integrate aes-js and nearly 23,000 repositories integrate pyaes, either as direct or indirect dependencies.

Unfortunately, despite their widespread adoption, aes-js and pyaes suffer from a careless mistake that creates serious security problems.

### The default IV problem

We’ll start with the biggest concern Trail of Bits identified: when instantiating AES in CTR mode, aes-js and pyaes do not require an IV. Instead, if no IV is specified, libraries will supply a default IV of `0x00000000_00000000_00000000_00000001`.

Worse still, the documentation provides *examples* of this behavior as typical behavior. For example, this comes from the [pyaes README](https://github.com/ricmoo/pyaes/blob/23a1b4c0488bd38e03a48120dfda98913f4c87d2/README.md?plain=1#L55):

```
aes = pyaes.AESModeOfOperationCTR(key)
plaintext = "Text may be any length you wish, no padding is required"
ciphertext = aes.encrypt(plaintext)
```

The first line ought to be something like `aes = pyaes.AESModeOfOperationCTR(key, iv)`, where `iv` is a randomly generated value. Users who follow this example will always wind up with the same IV, making it inevitable that many (if not most) will wind up with a key/IV reuse bug in their software. Most people are looking for an easy-to-use encryption library, and what’s simpler than just passing in the key?

That apparent simplicity has led to widespread use of the “default,” creating a multitude of key/IV reuse vulnerabilities.

### Other issues

#### Lack of modern cipher modes

aes-js and pyaes don’t support modern cipher modes like AES-GCM and AES-GCM-SIV. In most contexts where you want to use AES, you likely want to use these modes, as they offer authentication in addition to encryption. This is no small issue: even for programs that use aes-js or pyaes with distinct key/IV pairs, AES CTR ciphertexts are still *malleable*: if an attacker changes the bits in the ciphertext, then the resulting bits in the plaintext will change in exactly the same way, and CTR mode doesn’t provide any way to detect this. This can allow an attacker to recover an ECDSA key by tricking the user into signing messages with a series of related keys.

Cipher modes like GCM and GCM-SIV prevent this by computing keyed “tags” that will fail to authenticate when the ciphertext is modified, even by a single bit. Pretty nifty feature, but support is completely absent from aes-js and pyaes.

#### Timing problems

On top of that, both aes-js and pyaes are vulnerable to side-channel attacks. Both libraries use lookup tables for the AES S-box, which enables cache-timing attacks. On top of that, there are timing issues in the PKCS7 implementation, enabling a padding oracle attack when used in CBC mode.

#### Lack of updates

aes-js hasn’t been updated since 2018. pyaes hasn’t been touched since 2017. Since then, a number of issues have been filed against both libraries. Here are just a few examples:

* Outdated distribution tools for pyaes (it relies on `distutils`, which has been deprecated since October 2023)
* Performance issues in the streaming API
* UTF-8 encoding problems in aes-js
* Lack of IV and key generation routines in both

#### Developer response

Finally, in 2022, an issue was filed against aes-js about the default IV problem. The developer’s response ended with the following:

> The AES block cipher is a cryptographic **primitive**, so it’s very important to understand and use it properly, based on its application. It’s a powerful tool, and with great power, yadda, yadda, yadda. :)

Look, even at the best of times, cryptography is a minefield: a space full of hidden dangers, where one wrong step can blow things up entirely. When designing tools for others, developers have a responsibility to help their users avoid foreseeable mistakes—or at the very least, to avoid making it more likely that they’ll step on such landmines. Writing off a serious concern like this with “yadda, yadda, yadda” is deeply concerning.

In November 2025, we reached out to the maintainer via email and via X, but we received no response.

The original design decision to include a default IV was a mistake, but an understandable one for somebo...