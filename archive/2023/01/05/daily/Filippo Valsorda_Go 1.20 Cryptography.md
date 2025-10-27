---
title: Go 1.20 Cryptography
url: https://words.filippo.io/dispatches/go-1-20-cryptography/
source: Filippo Valsorda
date: 2023-01-05
fetch_date: 2025-10-04T03:03:44.286650
---

# Go 1.20 Cryptography

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

4 Jan 2023

# Go 1.20 Cryptography

[The ~~first~~ second release candidate of Go 1.20 is out](https://groups.google.com/g/golang-dev/c/MtxdaVmTgQk/m/xm6rLPFHAQAJ)![1](#fn:second) This is the first release I participated in as an independent maintainer, after [leaving Google](https://twitter.com/FiloSottile/status/1522671407636877315) to become a professional Open Source maintainer. (By the way, that’s going great, and I’m going to write more about it here soon!)

I’m pretty happy with the work that’s landing in it. There are both exciting new APIs, and invisible deep backend improvements that are going to make code more maintainable and secure in the long run. All the main work mentioned in the [planning post](https://words.filippo.io/dispatches/go1-20/) got done, and then some (but not the “stretch goals”). The whole release is pretty exciting, too, and you should check out the [release notes](https://tip.golang.org/doc/go1.20) (although [the cryptography parts might not be complete yet](https://go.dev/cl/459978)).

## crypto/ecdh

The standard library is gaining a new package: [`crypto/ecdh`](https://pkg.go.dev/crypto/ecdh%40go1.20rc1). Here’s what I said about it in [the Go 1.20 planning post](https://words.filippo.io/dispatches/go1-20/).

> The most visible change will be the landing the new [`crypto/ecdh` package][] I [proposed](https://github.com/golang/go/issues/52221) and [implemented](https://go.dev/cl/398914) earlier this year. The package provides a safe, `[]byte`-based, easy to use API for Elliptic Curve Diffie-Hellman over Curve25519 and NIST curves (P-256 and company, but no P-224 if we can get away with it).
>
> `crypto/ecdh` was made possible by a long-running refactor of the elliptic curve implementations in the standard library. Between Go 1.17 and Go 1.19, most critical code was moved to safer low-level APIs under `crypto/internal/nistec` and `crypto/internal/edwards25519`, large pieces were replaced with code generated from [fiat-crypto](https://github.com/mit-plv/fiat-crypto)’s formally verified models, making every curve constant time, most group logic was replaced with modern complete formulas, and even [the assembly was massaged to implement the same functions on all architectures](https://go-review.googlesource.com/c/go/%2B/396255) and fit the nistec API. [Some assembly is gone](https://go-review.googlesource.com/c/crypto/%2B/315269), actually!
>
> ([Here are all the changes.](https://go-review.googlesource.com/q/hashtag%3Acrypto-elliptic-refactor) [A couple nifty uses of generics in there if you’re curious.](https://cs.opensource.google/go/go/%2B/master%3Asrc/crypto/ecdh/nist.go;l=16-29;drc=d88d91e32e1440307369d50ba17ce622399a8bc1))
>
> The goal of the package is to replace the major use case for the **now-deprecated** `crypto/elliptic` API, which has a hardcoded dependency on the variable-time, large, and complex `math/big` package. `crypto/elliptic` is now no more than a compatibility wrapper. Any more advanced uses of `crypto/elliptic` can switch to [filippo.io/nistec](https://filippo.io/nistec) which is an exported version of `crypto/internal/nistec`, or [filippo.io/edwards25519](https://filippo.io/edwards25519) which is an exported version of `crypto/internal/edwards25519`.
>
> What’s left to do in Go 1.20 then?
>
> First, actually landing the new package, [which is already submitted](https://go.dev/cl/398914)! Then, adding and reviewing new tests (including [Wycheproof integration](https://go-review.googlesource.com/c/crypto/%2B/424274) by Roland), which actually revealed there are [fewer (!!) edge cases than I had originally documented](https://go-review.googlesource.com/c/go/%2B/425463). Finally, reviewing [the BoringCrypto integration by Russ](https://go-review.googlesource.com/c/go/%2B/423363).

The package landed successfully, and all the mentioned Go 1.20 work got done. The full `crypto/elliptic` deprecation will actually have to wait until Go 1.22, because of the [deprecation policy](https://go.dev/wiki/Deprecated):

> If function F1 is being replaced by function F2 and the first release in which F2 is available is Go 1.N, then an official deprecation notice for F1 should not be added until Go 1.N+2. This ensures that Go developers only see F1 as deprecated when all supported Go versions include F2 and they can easily switch.

The idea is making sure projects don’t have to support both APIs at the same time to keep supporting Go 1.20 while not getting deprecation warnings. I still have [an outstanding CL](https://go.dev/cl/459977) to deprecate the very low-level operations (point addition, and custom curves) that are not being replaced by anything in the standard library. (Instead, they should migrate to third-party modules like `filippo.io/nistec` or `filippo.io/edwards25519`.)

There was one last-minute API change: we got a [request on the issue tracker](https://go.dev/issue/56052) for a `PrivateKey` interface, to allow using private keys stored on hardware or remote modules, like the popular [`crypto.Signer`][]. We went back and forth a bit on it and discussed it with Russ Cox and concluded that PrivateKey doesn’t need to be an interface, but rather needs to implement one, like `ecdsa.PrivateKey` implements `crypto.Signer`. This led to moving the `ECDH` method from [the `Curve` interface][] to the `PrivateKey` type. We don’t define the interface ourselves because we don’t consume it anywhere, but an application that wishes to accept both `crypto/ecdh`-implemented keys and hardware-backed ones can define something like

```
type ecdhPrivateKey interface {
    Curve() ecdh.Curve
    ECDH(remote *ecdh.PublicKey) ([]byte, error)
    Equal(x crypto.PrivateKey) bool
    Public() crypto.PublicKey
    PublicKey() *ecdh.PublicKey
}
```

thanks to the magic of Go’s implicitly implemented interfaces. This still uses the `ecdh.PublicKey` concrete type, but values of that type can be easily constructed for hardware keys with `Curve.NewPublicKey`. What it does not support is other curves, which I am ok with.

Also, this makes the `Curve` interface solely an abstraction to produce keys on a certain curve, while the ECDH operation itself is a method of the private key, which feels more correct and elegant. Concretely, to implement this we added a private method to `Curve` which the private types returned by `P256()`, `X25519()`, etc. implement, and `PrivateKey.ECDH` calls. The reason for this is making it clear to the linker and to [vulncheck](https://pkg.go.dev/golang.org/x/vuln/vulncheck) that if you only ever call `X25519()`, the P-256 code is not reachable, so it doesn’t have to be linked into the binary and you don’t need to be notified of any vulnerabilities. [We have a test for this.](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20rc1%3Asrc/crypto/ecdh/ecdh_test.go;l=423-489) (Yes I love static analysis tests.)

Finally, we implemented support for parsing and marshaling public and private keys in PKIX and PKCS #8 format, respectively. NIST keys don’t have different OIDs to distinguish ECDH keys from ECDSA keys, so they always parse into `crypto/ecdsa` keys, which then have a new `ECDH()` method to return the equivalent `crypto/ecdh` key.

Since it also implements X25519 alongside ECDH over NIST curves, `crypto/ecdh` will in due time replace `golang.org/x/crypto/curve25519`, too, finally bringing down the number of 25519 implementations in `crypto/...` and `x/crypto` to one!

([CL 450816](https://go.dev/cl/450816), [CL 450815](https://go.dev/cl/450815), [CL 450335](https://go.dev/cl/450335), [CL 425463](https://go.dev/cl/425463), [CL 402555](https://go.dev/cl/402555), [CL 398914](https://go.dev/cl/398914), [CL 423363](https://go.dev/cl/423363), [CL 451115](https://go.dev/cl/451115))

## bigmod replaces math/big

*happy dance*

`math/big` is not exposed to attacker-controlled inputs anym...