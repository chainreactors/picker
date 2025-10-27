---
title: A Cryptographic Near Miss
url: https://words.filippo.io/dispatches/near-miss/
source: Filippo Valsorda
date: 2023-04-12
fetch_date: 2025-10-04T11:30:02.240370
---

# A Cryptographic Near Miss

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

11 Apr 2023

# A Cryptographic Near Miss

Go 1.20.2 [fixed](https://groups.google.com/g/golang-announce/c/3-TpUx48iQY) a small vulnerability in the `crypto/elliptic` package. The impact was minor, to the point that I don’t think any application was impacted, but the issue was interesting to look at as a near-miss, and to learn from.

Fundamentally, a scalar multiplication function was returning the wrong value for a very specific input because of a combination of the pre-existing complexity and unsafety of some optimized assembly, of undocumented assumptions, and of the neverending state of flux of open source code.

Let’s start from some necessary building blocks, look at how the vulnerability happened, and talk about what we can learn from it.

## Background

“Scalar multiplication” is a fancy way of saying multiplication by repeated additions. Elliptic curves only have a point addition operation, so to multiply a point by 5 we do P + P + P + P + P. Sort of.

Since the “scalar” is very large (and because we want to do this in constant time), we use a trick where we execute a sequence of additions and doublings (which are just a special case of additions). [I gave an explanation of this technique in my Black Hat 2018 talk](https://www.youtube.com/watch?v=zPj5tTFDql0), where I presented a *different* attack against this same code.

The idea is that to multiply P by 44 (`0b101100`) we do the following operations

```
Q = 0 + P = 0b1 * P
Q = Q * 2 = 0b10 * P
Q = Q * 2 = 0b100 * P
Q = Q + P = 0b101 * P
Q = Q * 2 = 0b1010 * P
Q = Q + P = 0b1011 * P
Q = Q * 2 = 0b10110 * P
Q = Q * 2 = 0b101100 * P 🎉
```

To make it constant time we actually always do the addition after every doubling, and then throw away the result if we weren’t supposed to do it, but anyway you get the gist.

To make it faster we actually don’t move one bit at a time, and instead multiply e.g. five times and then add between 1 \* P and 31 \* P, which we precomputed into a table before starting. To make it even faster, we use [Booth encoding](https://web.archive.org/web/20180716222422/http%3A//bwrcs.eecs.berkeley.edu/Classes/icdesign/ee241_s00/PAPERS/archive/booth51.pdf) from 1950 (!!!) so we actually add *or subtract* up to 16 \* P, reducing the table size, but at this point I am just boring you with unnecessary details.

The important thing to note is that there is nothing in this algorithm that needs the scalar to have a specific size or lie in a specific range.

Scalars, when applied to a specific curve, do have a “order” though, in the same way that hours on a clock have order 12. If you pass the order values wrap around, so if the order is Q and you multiply by Q + 30 (*foreshadowing*), then it’s the same as multiplying by 30. Keep this in mind, too.

Finally, there’s something you need to know about that addition operation. [Until 2015](https://eprint.iacr.org/2015/1060), we had to use separate formulas for adding two different points and for doubling a point. If you tried to use the addition formula on two equivalent points, stuff would break. That was a major selling point of Edwards curves like Curve25519 over the NIST curves, since we knew “complete” addition formulas for the former. We now know complete formulas for the NIST curves as well, but certain “safe curves” comparisons as well as some implementations haven’t been updated in ten years.

## History

With all that background out of the way, we can move on to history. Normally, history is part of the background, but this time the history is pretty much the root cause of the bug.

crypto/elliptic started out with [a very generic, extremely not constant time implementation of a double-and-add chain](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20.2%3Asrc/crypto/elliptic/params.go;l=297-305). Being variable time, it had no qualms doing [a conditional check on point equality](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20.2%3Asrc/crypto/elliptic/params.go;l=170-172), switching to the doubling formula. In that sense, it was “complete” even if the formulas were not. It accepted scalars of any size, because why not I guess, scalars are just a string of bits.

That wasn’t very fast (or secure) though! So at some point large amounts of (constant-time) assembly were added, written specifically to speed up the P-256 curve. This assembly does windowed double-and-add, Booth encoding, the works. The scalar multiplication loop was optimized specifically for 256-bit scalars, since that’s the length of the order of P-256 scalars, and you can expect scalars in protocols like ECDH and ECDSA to be reduced modulo the order. If the input was higher (or shorter) than the order of the curve, it was reduced using the variable-time math/big, which was *fine* because it wouldn’t happen in actual high-level protocols, I guess. This assembly code also implemented raw incomplete formulas. That was fine because if the scalar doesn’t overflow the order of the curve, we can show that the left-hand side of the additions in the loop can never match a value from the addend table. Ok.

Finally, over the past few years I’ve been engaging in a large refactor of the crypto/elliptic and crypto/rsa backends to remove its dependency on math/big. [We’ve talked about it before.](https://words.filippo.io/dispatches/go-1-20-cryptography/#cryptoecdh) For [the new scalar multiplication loops](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20.2%3Asrc/crypto/internal/nistec/p256.go;l=357-383) I’ve implemented a simple windowed scalar multiplication using complete formulas and formally-verified generated code. It’s pretty neat, I think. However, the P-256 assembly is still faster, so I pulled it into the new API, along with its special scalar multiplication loop.

Since that loop assumes the scalar is 256 bits, I introduced a requirement in the new API that the scalar size match the curve order size. I didn’t require the scalar to be actually reduced modulo the order because it felt like an unfair requirement: the consumer of this API doesn’t necessarily have a constant-time big integer library to do the reduction or even check the condition! Requiring that felt like a way to force the caller to re-introduce the variable-time code I was trying to excise, and anyway, there’s nothing that requires the scalar to be reduced, it just needs to be the right number of bits for the loop… right?

## Bug!

The bug is sitting in the section above, in plain sight, but I don’t blame you if you didn’t spot it. I didn’t! [Guido Vranken reported](https://github.com/golang/go/issues/58647) that trying to multiply a point—any P-256 point, really—by Q + 30 returns the wrong result. As far as I can tell, it’s literally only that one value. I kinda wonder how he found it, I guess he tested low values vs. low values added to the order. [That’s how we are testing for it now, at least.](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20.2%3Asrc/crypto/internal/nistec/nistec_test.go;l=233-239)

So what happened? Well, while neither the old generic nor the new scalar multiplication loops have any requirement on the value of the scalar, the P-256 loop assumed the scalar is reduced modulo the order of the curve. Otherwise, the intermediate value can overflow during the computation and end up equal to the precomputed value it’s being added to, and the incomplete formulas can’t handle that. Before my refactor, this was not a problem because the scalar was reduced with math/big as a way to implement the old API. The addition function even returned a bit to let the caller know if the points were equal, but it was ignored in the scalar multiplication loop ([as opposed to the general Add function](https://cs.opensource.google/go/go/%2B/master%3Asrc/crypto/internal/nistec/p256_asm.go;l=391)) because presumably they knew they could rely on the scalar to be r...