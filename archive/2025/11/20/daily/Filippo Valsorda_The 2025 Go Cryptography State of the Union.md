---
title: The 2025 Go Cryptography State of the Union
url: https://words.filippo.io/2025-state/
source: Filippo Valsorda
date: 2025-11-20
fetch_date: 2025-11-21T03:12:17.995353
---

# The 2025 Go Cryptography State of the Union

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

20 Nov 2025

# The 2025 Go Cryptography State of the Union

This past August, I delivered my traditional *Go Cryptography State of the Union* talk at [GopherCon US 2025](https://www.gophercon.com/) in New York.

It goes into everything that happened at the intersection of Go and cryptography over the last year.

You can watch the video (with manually edited subtitles, for my fellow subtitles enjoyers) or read the transcript below (for my fellow videos not-enjoyers).

*The annotated transcript below was made with [Simon Willison’s tool](https://tools.simonwillison.net/annotated-presentations). All pictures were taken around Rome, the Italian contryside, and the skies of the Northeastern United States.*

## Annotated transcript

![](https://assets.buttondown.email/images/a2094744-c5b9-4301-93d2-61676adee15d.jpeg)

![](https://assets.buttondown.email/images/4ff34dc1-aca8-439e-8fe4-a38237da2855.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-02.jpeg)

When I say "we," it doesn't mean just me, it means me, Roland Shoemaker, Daniel McCarney, Nicola Morino, Damien Neil, and many, many others, both from the Go team and from the Go community that contribute to the cryptography libraries all the time.

I used to do this work at Google, and I now do it as an independent as part of and leading [Geomys](https://geomys.org), but we'll talk about that later.

![](https://assets.buttondown.email/images/f5f10c2b-296f-4375-b71f-2498d5f1a796.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-03.jpeg)

When we talk about the Go cryptography standard libraries, we talk about all of those packages that you use to build secure applications.

That's what we make them for. We do it to provide you with encryption and hashes and protocols like TLS and SSH, to [help you build secure applications](https://golang.org/design/cryptography-principles).

![](https://assets.buttondown.email/images/d3c5fb80-876c-40e9-85bd-80a23e36e89f.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-04.jpeg)

The main headlines of the past year:

We shipped post quantum key exchanges, which is something that you will not have to think about and will just be solved for you.

We have solved FIPS 140, which some of you will not care about at all and some of you will be very happy about.

And the thing I'm most proud of: we did all of this while keeping an excellent security track record, year after year.

![](https://assets.buttondown.email/images/d722f8d0-f12f-477f-be25-89a7519f1157.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-05.jpeg)

This is an update to something you've seen last year.

[The Go Security Track Record](https://docs.google.com/spreadsheets/d/1kGwdnqcdfevyhbxVSUbwQTcdrmvrlCZUV4_XMiTn3qQ/view)

It's the list of vulnerabilities in the Go cryptography packages.

We don't assign a severity—because it's really hard, instead they're graded on the "Filippo's unhappiness score."

It goes shrug, oof, and ouch.

Time goes from bottom to top, and you can see how as time goes by things have been getting better. People report more things, but they're generally more often shrugs than oofs and there haven't been ouches.

![](https://assets.buttondown.email/images/f98ececb-4046-471b-ad0a-6ba080c84a33.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-06.jpeg)

More specifically, we haven't had any oof since 2023.

We didn't have any Go-specific oof since 2021.

When I say Go-specific, I mean: well, sometimes the protocol is broken, and as much as we want to also be ahead of that by limiting complexity, you know, sometimes there's nothing you can do about that.

And **we haven't had ouches since 2019**. I'm very happy about that.

![](https://assets.buttondown.email/images/f679dda9-bc5b-4b2f-9b35-95e97f5bf479.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-07.jpeg)

But if this sounds a little informal, I'm also happy to report that we had the first security audit by a professional firm.

Trail of Bits looked at all of the nuts and bolts of the Go cryptography standard library: primitives, ciphers, hashes, assembly implementations. They didn't look at the protocols, which is a lot more code on top of that, but they did look at all of the foundational stuff.

And I'm happy to say that [they found *nothing*](https://go.dev/blog/tob-crypto-audit).

![Roland and I showing off I SURVIVED TRAIL OF BITS t-shirts](https://assets.buttondown.email/images/4bd5e6be-7100-41dc-be9c-00161a1a0b78.jpeg)

Two of a kind t-shirts, for me and Roland Shoemaker.

![](https://assets.buttondown.email/images/468319e9-3f62-425b-ac8a-a5e32771c3a6.jpeg)

![](https://assets.buttondown.email/images/f671c289-0e63-47ca-a4e6-6711cb48fe7a.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-09.jpeg)

I'm happy to report that we now have ML-KEM, which is the post-quantum key exchange algorithm selected by the NIST competition, an international competition run in the open.

You can use it directly from the [crypto/mlkem](https://pkg.go.dev/crypto/mlkem) standard library package starting in Go 1.24, but you're probably not gonna do that.

![](https://assets.buttondown.email/images/8ad85b47-a2eb-4de2-8e5d-0f5c29ab8613.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-10.jpeg)

Instead, you're probably going to just use crypto/tls, which by default now uses a hybrid of X25519 and ML-KEM-768 for all connections with other systems that support it.

Why hybrid? Because this is new cryptography. So we are still *a little* worried that somebody might break it.

There was one that looked very good and had very small ciphertext, and we were all like, “yes, yes, that's good, that's good.” And then somebody broke it on a laptop. It was very annoying.

We're fairly confident in lattices. We think this is the good one. But still, we are taking both the old stuff and the new stuff, hashing them together, and unless you have both a quantum computer to break the old stuff and a mathematician who broke the new stuff, you're not breaking the connection.

crypto/tls can now negotiate that with Chrome and can negotiate that with other Go 1.24+ applications.

Not only that, we also removed any choice you had in ordering of key exchanges because we think we know better than you and— that didn't come out right, uh.

… because we assume that you actually want us to make those kind of decisions, so as long as you don't turn it off, we will default to post-quantum.

You can still turn it off. But as long as you don't turn it off, we'll default to the post-quantum stuff to keep your connection safe from the future.

![](https://assets.buttondown.email/images/a6fd1a9c-1ca9-4db3-b3aa-72b18cbae064.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-11.jpeg)

Same stuff with x/crypto/ssh. Starting in v0.38.0.

SSH does the same thing, they just put X25519 and ML-KEM-768 in a different order, which you would think doesn't matter—and indeed it doesn't matter—but there are [rules where "no, no, no, you have to put that one first." And the other rule says "no, you have to put that one first."](https://www.ietf.org/archive/id/draft-ietf-tls-ecdhe-mlkem-02.html#section-5) It's been a whole thing. I'm tired.

OpenSSH supports it, so if you connect to a recent enough version of OpenSSH, that connection is post-quantum and you didn't have to do anything except update.

![](https://assets.buttondown.email/images/bdc8faee-11fb-4d5d-9127-17ba3ea63885.jpeg)

[#](https://words.filippo.io/2025-state/#gcus25slide-12.jpeg)

Okay, but you said key exchanges *and digital signatures* are broken. What about the latter?

Well, key exchanges are urgent because of the record-now-decrypt-later problem, but unless the physicists that are developing quantum computers also develop a time machine, they can't use the QC to go back in time and use a fake signature today. So if you're ver...