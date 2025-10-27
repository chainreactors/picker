---
title: “YOLO” is not a valid hash construction
url: https://blog.trailofbits.com/2024/08/21/yolo-is-not-a-valid-hash-construction/
source: Trail of Bits Blog
date: 2024-08-22
fetch_date: 2025-10-06T18:03:24.018395
---

# “YOLO” is not a valid hash construction

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# “YOLO” is not a valid hash construction

Opal Wright

August 21, 2024

[cryptography](/categories/cryptography/)

Among the cryptographic missteps we see at Trail of Bits, “let’s build our own tool out of a hash function” is one of the most common. Clients have a problem along the lines of “we need to hash a bunch of different values together” or “we need a MAC” or “we need a key derivation function for passwords,” and the closest tool at hand is a hash function.

These needs are often met with what could be called “YOLO” constructions: *ad-hoc* functions that “solve” the instant problem in a way that’s obvious, straightforward, and usually wrong.

The fact is, these problems are harder than they seem. For us, it can be frustrating to see home-rolled solutions over and over in the products clients bring us because the problems have already been solved. So let’s discuss a few of the YOLO constructions we frequently see, what’s wrong with them, and what to do instead.

### YoloMultiHash

This is the most common YOLO construction we see at Trail of Bits. Clients often use this when they have complex data structures or arrays of values and need to turn them into a Fiat-Shamir transcript.

#### The YOLO construction

Given a hash function *H* and a set of messages *M̂ = {M*1*,M*2*,…,Mn}*, select a separator string *S*, and compute *YoloMultiHash(M̂) = H(M*1‖*S*‖*M*2‖*S*‖*…*‖*S*‖*Mn)*.

#### The problem

The issue we run into here is *ambiguous encoding*.

What happens if the messages can contain the separator *S* as a substring? Suppose the message *Mi* contains *S* as a substring. Split *Mi* into *Mi = M′**i*‖*S*‖ *M′′i* and define *M̃ = {M*1*,…,M′i,M′′i,…,Mn}*. Then we have *YoloMultiHash(M̂) = YoloMultiHash(M̃)*. That’s two semantically distinct inputs that lead to the same hash value. This is akin to breaking the collision resistance requirement of a good hash function, which is a *Very Bad Thing* (tm).

This is not a hypothetical issue, either: [it has been used to break the security of widely used libraries](https://www.verichains.io/tsshock/).

#### The better options

Instead of using YoloMultiHash, use a function that’s designed for hashing multiple independent values into a single result. The most well-known example of this would be TupleHash, defined in [SP800-185](https://www.nist.gov/publications/sha-3-derived-functions-cshake-kmac-tuplehash-and-parallelhash). Several other hash functions support or make it easy to support similar functionality; the [BLAKE3](https://github.com/BLAKE3-team/BLAKE3) specification, for instance, describes the process for creating “stateful hash objects” that can be used this way.

Alternatively, *get better at serializing your data*. If you’re trying to serialize a data structure, there are great options like [Protocol Buffers](https://protobuf.dev/), [CBOR](https://cbor.io/), and [BCS](https://github.com/diem/bcs). These all produce unambiguous encodings of your data, meaning that structures with different values won’t lead to the same hash input. As a rule of thumb, if you’re feeding structured data into a hash function, it should be in a format that can be converted losslessly back into the original data structure.

(Note that, while many serialization methods will create *unambiguous* encodings, they don’t all necessarily produce *unique* encodings. For instance, JSON is largely insensitive to changes in whitespace and element ordering, so using JSON serializations produced by different libraries could lead to different hashes. Be careful!)

### YoloMAC

#### The YOLO construction

Given a key *K* and a message *M*, compute *YoloMAC(K,M) = H(K*‖*M)*. Sometimes folks will throw in a salt value or customization string *S* to let them do domain separation—something like *YoloMAC(K,M,S) = H(K*‖*S*‖*M)*. It doesn’t really change the nature of the attacks below, so we’re just going to go with the simplified version here.

#### The first problem

The first problem with YoloMAC is well-known: length-extension attacks. If *H* is a Merkle-Damgård hash algorithm, as SHA256 is, then given *H(M)*, an attacker can compute *H(M*‖*X)* for any *X* the attacker chooses. That means that, given *YoloMAC(K,M) = H(K*‖*M)*, an attacker can compute *YoloMAC(K,M*‖*X)*, without knowing *K* or even *M*.

This may sound silly, but if you have a message that’s being protected using an encrypt-then-MAC construction, using YoloMAC is a real problem. An attacker can append garbage data to the plaintext, updating the MAC to match. Depending on the underlying format, some parsers will attempt to process the garbage data. This can cause messages not to load correctly, crash parsers, or possibly leak timing information that allows an attacker to learn about how the message is being processed.

#### The second problem

The second problem is similar to the problem with YoloMultiHash: ambiguous encoding. This issue applies whether or not the hash function is susceptible to length extension attacks, so using SHA3 or Skein or BLAKE3 won’t save you here.

Say you have a message *M* and a 256-bit key *K = K1*‖*K2*, where *K1* and *K2* are 128 bits each. Let’s suppose we compute *C1 = YoloMAC(K,M) = H(K1*‖*K2*‖*M)*.

Now let’s define *M′ = K*2‖*M* and compute our MAC using K1 as our key: *C*2 *= YoloMAC(K*1*,M′) = H(K*1‖*M′)=H(K*1‖*K*2‖*M) = C*1. We’ve just found two different message/key pairs that produce the same MAC.

Depending on the flexibility of the underlying file formats, this flexibility could allow Alice to produce a “root” message *M̃* and 128-bit deniability key *K̃* such that *M̃* parses as a valid PDF file that incriminates Bob in some sort of conspiracy with Alice, but K̃‖M̃ parses as an innocuous JPG file. Alice can negotiate a 128-bit MAC key *K* with Bob, compute *V = YoloMAC(K,K̃*‖*M̃)*, and send *V* and *K̃*‖*M̃* to Bob. Bob validates *V* and recovers the innocuous JPG file.

Alice contacts the authorities and provides them with convincing records that she sent a message to Bob with MAC *V*, then provides them with the key *K′ = K*‖*K̃* and message *M̃*. When the authorities check the authenticity of the incriminating PDF, they see that, in fact, *YoloMAC(K*‖*K̃,M̃)* matches the *V* provided by Alice.

This isn’t a pie-in-the-sky model: practical attacks have been demonstrated using a similar issue with [AES-GCM tags](https://eprint.iacr.org/2019/016.pdf).

This problem is particularly common in the case of Keccak, since [the Keccak website says](https://keccak.team/keccak_strengths.html):

> Unlike SHA-1 and SHA-2, Keccak does not have the length-extension weakness, hence does not need the HMAC nested construction. Instead, MAC computation can be performed by simply prepending the message with the key.

While Keccak doesn’t suffer from the length-extension attacks that HMAC is meant to address, the phrase “simply prepending the message with the key” carries a lot of assumptions about key length and key formatting with it.

#### The better options

Use HMAC, KMAC, or built-in tools, depending on your hash function.

If you’re using the SHA2 class of hashes (SHA256/384/512/etc.), you *need* to use HMAC; its design specifically sidesteps length extension attacks. HMAC has been around since the late 1990s; this problem has been solved for a quarter century now. It’s supported in every major cryptographic library. Python even includes it in their [standard library](https://docs.python.org/3/library/hmac.html). There’s no good reason to be rolling your own solution to this problem.

If you’re using SHA3, use KMAC. KMAC was formalized in 2016, and lots of SHA3 libraries already support it. KMAC also has several useful features:

* It can be used in XOF mode, which is useful in some situations where MACs are also used as masks for sensitive values.
* When not used as an XOF, the output length is *integ...