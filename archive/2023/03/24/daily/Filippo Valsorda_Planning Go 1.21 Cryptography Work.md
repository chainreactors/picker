---
title: Planning Go 1.21 Cryptography Work
url: https://words.filippo.io/dispatches/go-1-21-plan/
source: Filippo Valsorda
date: 2023-03-24
fetch_date: 2025-10-04T10:28:02.299975
---

# Planning Go 1.21 Cryptography Work

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

23 Mar 2023

# Planning Go 1.21 Cryptography Work

As most of you are tired to hear by now, I am [a professional, full-time open-source maintainer](https://words.filippo.io/full-time-maintainer/), and a lot of my time is spent maintaining the Go cryptography standard libraries.

Go’s development follows a fixed calendar with two development windows and two releases every year. I try to write about what I plan to do / be involved in for the next release at the beginning of the cycle, and about what happened at the end of the cycle.

This is the planning overview for the Go 1.21 release. There is some exciting API work going on, as well as some satisfying follow-ups on stuff that landed in Go 1.20.

Now is a very good time to provide feedback (and you can do that by just replying to this if you’re reading it in your inbox)! You can also [take a look at my public GitHub Projects planning board](https://github.com/users/FiloSottile/projects/2).

## Follow-ups

Go 1.20 was a big release for cryptography, so there are a few items to follow-up on, to tie up loose ends while the iron is hot. (That is, while I still have any context paged into my brain.)

## crypto/ecdh follow-ups

The new [crypto/ecdh package](https://pkg.go.dev/crypto/ecdh) made its debut in Go 1.20.

This means that we can [deprecate almost all of crypto/elliptic](https://go.dev/cl/459977) in Go 1.21.[1](#fn:np1) We leave undeprecated only the Curve singletons returned by [`P256()`][] and the like, needed to use the crypto/ecdsa APIs. crypto/ecdsa doesn’t actually use crypto/elliptic code besides switching on these values, so crypto/elliptic is now a glorified enum and a legacy compatibility layer. As always, deprecated doesn’t mean removed: per the [Go 1 Compatibility Promise](https://go.dev/doc/go1compat) crypto/elliptic keeps working, but [staticcheck](https://staticcheck.io/) will yell at you about using it.

There is *one* meaningful bit of functionality in crypto/elliptic that is not in crypto/ecdh yet: compressed point encodings for NIST curves. [I explored the topic and proposed an API in the original discussion](https://github.com/golang/go/issues/52221#issuecomment-1111153164) but then decided to wait to add those APIs. “No is temporary, yes is forever.” If anyone uses compressed point encodings, now would be the time to reach out!

Oh, also P-224, but that’s on purpose and I think we got away with it.

Finally, we can now [rewrite golang.org/x/crypto/curve25519 as a crypto/ecdh.X25519 wrapper](https://go.dev/cl/451115), hopefully bringing down the number of -25519 implementations in the Go project to one: crypto/internal/edwards25519 (available externally as [filippo.io/edwards25519](https://filippo.io/edwards25519)), used by crypto/ecdh and crypto/ed25519, and transitively by the x/crypto/ed25519 and x/crypto/curve25519 wrappers. We’ll wait a few releases before dropping the pre-Go 1.20 compatibility layer from x/crypto.

## crypto/rsa follow-ups

The other big change of Go 1.20 has been migrating crypto/rsa away from math/big to crypto/internal/bigmod (available externally as [filippo.io/bigmod](https://filippo.io/bigmod)). Dear reader, I’ll be honest, I did not expect this to land, but it did!

The switch came with a significant performance degradation: between approximately 15% (RSA-2048 on amd64) and 45% (RSA-4096 on arm64), despite dropping in some dedicated amd64 [Avo-generated](https://github.com/mmcloughlin/avo) assembly. That’s counter-intuitive: I expected the more-specific crypto/internal/bigmod to be faster than math/big, despite having to waste some cycles on keeping computations constant-time. Turns out that an implementation technique used in crypto/internal/bigmod since its initial submission might be based on outdated wisdom that I also assumed was still true. The idea was that splitting numbers into 63-bit “unsaturated limbs” allows for faster Montgomery multiplication, because it allows [a result in the hot loop to fit in 128 bits](https://cs.opensource.google/go/go/%2B/master%3Asrc/crypto/internal/bigmod/nat.go;l=626;drc=335e7647f53293eb320c1f069eaf0ff641810d6d), so two registers. Well, turns out that might be true in portable C, but if you have access to the add-with-carry instructions of most modern processors, using saturated 64-bit limbs and keeping the carries in flags across loop iterations is faster. That’s what the math/big assembly does.

The good news is that we have pure-Go access to these “addition chains” thanks to [math/bits.Add](https://pkg.go.dev/math/bits#Add). The bad news is that Montgomery multiplication needs to keep track of *two* carry bits across loop iterations, and while possible (that’s what ADX is for, it’s just ADC that uses a different flag) [it’s too much for the compiler to figure out](https://abyssdomain.expert/%40commaok%40inuh.net/109934357847363407)[2](#fn:maybe), so we’re stuck with assembly. I have [a CL that switches bigmod to using math/big’s assembly core](https://go.dev/cl/471259) and it brings crypto/rsa within 5% of its Go 1.19 performance without even using all the assembly. It needs cleaning up, but I expect RSA on Go 1.21 to be at least as fast as on Go 1.19, maybe faster.[3](#fn:arches)

Aside from clawing back performance, there’s [a laundry list of follow-ups](https://github.com/golang/go/issues/57752).

* [`PrivateKey.Validate`][] and [`PrivateKey.Equal`][] still use math/big and need porting to bigmod or other constant-time code.
* [The race detector makes the new code dramatically slower.](https://github.com/golang/go/issues/56980) If that’s still the case after the changes above, we probably need to drop some `go:norace` annotations.
* The deprecation of the unused `GenerateMultiPrimeKey` was reverted at the last minute to [go through the proposal process](https://go.dev/issue/56921). It’s now ready to land.
* A couple docs fixups.

## New API proposals

There are a few ongoing proposal discussions that thanks to [the new release calendar with shorter freezes](https://github.com/golang/go/wiki/Go-Release-Cycle) have a good chance of landing into Go 1.21 changes.

### crypto/tls support for QUIC

Damien Neil, Marten Seemann, and I have been [discussing the APIs that crypto/tls needs to expose to support QUIC and HTTP/3](https://go.dev/issue/44886). These higher level protocols use TLS 1.3 for the handshake, but then derive their own keys and have their own record encryption, since they don’t run over simple TCP streams. Marten has a fork of crypto/tls for his [quic-go](https://github.com/quic-go/quic-go) implementation, which is a maintenance and ecosystem pain point. The new APIs are intended to let quic-go drop the fork and depend on behavior covered by the Go 1 Compatibility Promise, as well as to support [an HTTP/3 implementation in the standard library](https://go.dev/issue/58547).

It’s a large and important change, because we’ll be maintaining these APIs in perpetuity, and we have to decide even fundamental architecture details like what side “drives” the handshake: is the caller injecting data, or is crypto/tls requesting it with callbacks from a blocking handshake function? The current design is interesting: the API works synchronously, with the QUIC implementation calling a crypto/tls function to provide incoming bytes, and effectively getting back any bytes it needs to send back, if any. *How* it gets those bytes back is somewhat weird: it provides callbacks that are called synchronously by crypto/tls before returning; semantically the parameters of those callbacks are just fancy return values of the crypto/tls methods. I am going to try proposing switching them to proper return values to make the semantics clearer and the implementation simpler. What makes the design interesting is that this simple and natural API is a poor match for the internals of crypto/tls, which ar...