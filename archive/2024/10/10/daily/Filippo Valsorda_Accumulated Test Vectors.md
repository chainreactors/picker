---
title: Accumulated Test Vectors
url: https://words.filippo.io/dispatches/accumulated/
source: Filippo Valsorda
date: 2024-10-10
fetch_date: 2025-10-06T18:51:57.663543
---

# Accumulated Test Vectors

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

9 Oct 2024

# Accumulated Test Vectors

I [like tests](https://youtu.be/lahO3de3k_0?feature=shared&t=1439). I especially like [reusable test vector libraries](https://github.com/C2SP/CCTV). Sometimes test vectors are lovingly handcrafted to target obscure edge-cases. Those vectors belong in [Wycheproof](https://github.com/C2SP/Wycheproof) or with the upstream specification. Sometimes though vectors are produced by sheer brute force. Enumerate every possible input and check the output. Try a million random inputs and see what happens. Combine all possible input sizes for every parameter. Make one very, very large input.

These vectors can be tremendously effective and require no prior insight into the bugs you’re hunting. If you run 300 000 random tests, you have a 99% chance of hitting any 2⁻¹⁶ edge case.[1](#fn:chance)

For example, you can get pretty good coverage of the internals of the [new post-quantum algorithm ML-KEM](https://csrc.nist.gov/pubs/fips/203/final) by generating random key pairs, passing the public key to Encapsulate and the resulting ciphertext to Decapsulate, and then making sure keys, ciphertext, and shared secret are as expected.[2](#fn:negative) The reference implementation offers [a program](https://github.com/pq-crystals/kyber/blob/d5b791c0c601b543233daccbae2845c6197a9e77/ref/test/test_vectors.c) to produce a corpus of 10 000 of these known-answer tests.

The catch is that—unless the result is self-evidently correct[3](#fn:fuzz)—you need to actually check in inputs and expected outputs *somewhere*. Those ML-KEM vectors run into the tens of megabytes, even compressed. Checking in the reference implementation is also undesirable, with its nontrivial size, incompatible build system, and different supported environments.

Here’s a trick I call **accumulated test vectors**: define a test that draws random inputs from a deterministic source,[4](#fn:sky) like an extendable-output function such as SHAKE128; accumulate the output(s) into a hash function; and check in the expected final hash. It’s a simple idea that was probably redeveloped many times, but that I have not seen documented before.

Here’s all you need to run 10 000 random ML-KEM tests equivalent to the ones from the reference implementation:

> Instantiate SHAKE128 with an empty input, call it r. Instantiate another SHAKE128, call it a. Draw a ML-KEM-768 seed from r, pass it to KeyGen\_internal. Write ek to a. Draw a message from r, pass it to Encaps\_internal. Write ct and k to a. Run Decaps and check that k matches. Draw an invalid ciphertext from r, pass it to Decaps. Write the rejection k to a. Repeat 10 000 times total. Draw 16 bytes from a, they should match `8a518cc63da366322a8e7a818c7a0d63`.

Quite a long way from tens of megabytes of JSON!

The approach also scales well with available CPU time. [In Go](https://github.com/golang/go/blob/3aa71c12eacd68ec16e7172d92aa5c6af32f0c3b/src/crypto/internal/mlkem768/mlkem768_test.go#L321-L378) we run 100 iterations for `-short` mode (in presubmit checks), 10 000 by default (taking a couple seconds in CI), and 1 000 000 on demand (for developing). That last one would have required more than a gigabyte of vectors, instead we just check in three hashes in total.

Like JSON vectors, accumulated vectors are reusable across implementations, as long as the generator and accumulator are simple enough and broadly available. The ML-KEM vectors are [available on CCTV](https://c2sp.org/CCTV/ML-KEM#accumulated-pq-crystals-vectors).

Beyond purely random inputs, accumulated tests can be defined to systematically explore large ranges of input parameters and sizes. For example we have an [accumulated cSHAKE128 test](https://go-review.googlesource.com/c/crypto/%2B/616576/4/sha3/sha3_test.go#379) that iterates through the combinations of N sizes 0 to 200, S sizes 0 to 200, and input sizes 100, 168, 200 (to cover values below, matching, and above the “rate” or block size). This exercises multiple joints at once: length prefix encoding, input chunking, and padding. It was written to be a generic test that would cover [a specific bug](https://github.com/golang/go/issues/69169) but it immediately caught an unrelated issue during a reactor.

Finally, you can do something similar to “compress” individual large vectors. For example, we now [test cSHAKE personalization strings](https://go-review.googlesource.com/c/crypto/%2B/616576/4/sha3/sha3_test.go#461) bigger than 512MiB (whose size in bits [overflows a uint32](https://github.com/golang/go/issues/66232)) by drawing them from SHAKE128 and checking the expected output. Using a deterministic source lets us compare the result with other implementations easily, although it took a couple tries because the [first one we tried also had a bug](https://github.com/paulmillr/noble-hashes/issues/101).

The main disadvantage of accumulated vectors is that if the test fails it offers no insight for debugging. I think this is well justified by the advantages, and mostly mitigated in common scenarios: when first developing an implementation intermediate values are more useful than test vectors, and while when making changes you generally have an idea of what you touched and potentially broke. A lot of cryptography engineering involves blindly looking for a bug relying only on a binary result code anyway! It’s part of the fun.

If you got this far, you might also want to follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

One of my favorite places in Rome: Tiber Island, in the middle of the river. The building occupying half of it is an active hospital with an emergency room.[5](#fn:emt) The coast is a great pacing track for long phone calls.

I’m somewhat surprised I haven’t posted this Rome picture yet. I must have taken a hundred variations of it by now: day, night, sunset, sunny, storm, flood, migratory birds. I love the water, the symmetry, and the variance over time.

![A nighttime view of Tiber Island in the middle of the Tiber River, featuring a lit stone bridge connecting the island, historic buildings with warm lighting framed by trees, and reflections of lights on the calm black water to the two sides.](https://assets.buttondown.email/images/6df09792-c227-4e85-aa2c-2475b461b932.jpeg)

My maintenance work is funded by the awesome [Geomys](https://geomys.org) clients: [Interchain](https://interchain.io/), [Smallstep](https://smallstep.com/), [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [SandboxAQ](https://www.sandboxaq.com/), [Charm](https://charm.sh/), and [Tailscale](https://tailscale.com/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)

Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. [Teleport Identity](https://goteleport.com/platform/identity/?utm=filippo&ref=words.filippo.io) is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We at [Ava Labs](https://www.avalabs.org), maintainer of [AvalancheGo](https://github.com/ava-labs/avalanchego) (the most widely used client for interacting with the [Avalanche Network](https://www.avax.network)), believe the sustainable maintenance and development of open...