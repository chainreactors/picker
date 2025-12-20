---
title: Building a Transparent Keyserver
url: https://words.filippo.io/keyserver-tlog/
source: Filippo Valsorda
date: 2025-12-19
fetch_date: 2025-12-20T03:13:57.447154
---

# Building a Transparent Keyserver

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

19 Dec 2025

# Building a Transparent Keyserver

Today, we are going to build a keyserver to lookup [age](https://age-encryption.org/) public keys. That part is boring. What’s interesting is that we’ll apply the same transparency log technology as the Go Checksum Database to keep the keyserver operator honest and unable to surreptitiously inject malicious keys, while still protecting user privacy and delivering a smooth UX. You can see the final result at [keyserver.geomys.org](https://keyserver.geomys.org). We’ll build it step-by-step, using modern tooling from the tlog ecosystem, integrating transparency in less than 500 lines.

I am extremely excited to write this post: it demonstrates how to use a technology that I strongly believe is key in protecting users and holding centralized services accountable, and it’s the result of years of effort by me, the [TrustFabric](https://transparency.dev/) team at Google, the [Sigsum](https://www.sigsum.org/) team at [Glasklar](https://www.glasklarteknik.se/), and many others.

> This article is being cross-posted on the [Transparency.dev Community Blog](https://blog.transparency.dev/).

Let’s start by defining the goal: we want a secure and convenient way to fetch [age](https://age-encryption.org/) public keys for other people and services.[1](#fn:emailage)

The easiest and most usable way to achieve that is to build a centralized keyserver: a web service where you log in with your email address to set your public key, and other people can look up public keys by email address.

![the keyserver web UI](https://assets.buttondown.email/images/d4f72ca6-0ff7-4b1b-8890-1b8f0cbfad90.png)

Trusting the third party that operates the keyserver lets you solve identity, authentication, and spam by just delegating the responsibilities of checking email ownership and implementing rate limiting. The keyserver can send a link to the email address, and whoever receives it is authorized to manage the public key(s) bound to that address.

I had Claude Code [build the base service](https://github.com/FiloSottile/torchwood/commit/f191bdbadeb9c9c15ba0a9995dffdb20651710da), because it’s simple and not the interesting part of what we are doing today. There’s nothing special in the implementation: just a Go server, an SQLite database,[2](#fn:json) a lookup API, a set API protected by a CAPTCHA that sends an email authentication link,[3](#fn:broadcast) and a Go CLI that calls the lookup API.

## Transparency logs and accountability for centralized services

A lot of problems are shaped like this and are much more solvable with a trusted third party: PKIs, package registries, voting systems… Sometimes the trusted third party is encapsulated behind a level of indirection, and we talk about Certificate Authorities, but it’s the same concept.

Centralization is so appealing that even the OpenPGP ecosystem embraced it: after the [SKS pool was killed by spam](https://words.filippo.io/openpgp-is-broken/), a [new OpenPGP keyserver](https://keys.openpgp.org/) was built which is just a centralized, email-authenticated database of public keys. Its [FAQ](https://keys.openpgp.org/about/faq/#third-party-signatures) claims they don’t wish to be a CA, but also explains they don’t support the (dubiously effective) Web-of-Trust at all, so effectively they can only act as a trusted third party.

The obvious downside of a trusted third party is, well, trust. You need to trust the operator, but also whoever will control the operator in the future, and also the operator’s security practices. That’s asking a lot, especially these days, and a malicious or compromised keyserver could provide fake public keys to targeted victims with little-to-no chance of detection.

**Transparency logs are a technology for applying cryptographic accountability to centralized systems with no UX sacrifices.**

A transparency log or tlog is an append-only, globally consistent list of entries, with efficient cryptographic proofs of inclusion and consistency. The log operator appends entries to the log, which can be tuples like *(package, version, hash)* or *(email, public key)*. The clients verify an inclusion proof before accepting an entry, guaranteeing that the log operator will have to stand by that entry in perpetuity and to the whole world, with no way to hide it or disown it. As long as *someone* who can check the authenticity of the entry will *eventually* check (or “monitor”) the log, the client can trust that malfeasance will be caught.

Effectively, a tlog lets the log operator stake their reputation to borrow time for collective, potentially manual verification of the log’s entries. This is a middle-ground between impractical local verification mechanisms like the [Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust), and fully trusted mechanisms like centralized X.509 PKIs.

> If you’d like a longer introduction, [my Real World Crypto 2024 talk](https://youtu.be/SOfOe_z37jQ) presents both the technical functioning and abstraction of modern transparency logs.

There is a whole ecosystem of interoperable tlog tools and publicly available infrastructure built around [C2SP](https://c2sp.org/) specifications. That’s what we are going to use today to add a tlog to our keyserver.

> If you want to catch up with the tlog ecosystem, [my 2025 Transparency.dev Summit Keynote](https://www.youtube.com/watch?v=B-0ZW1ovPmk) maps out the tools, applications, and specifications.

### tlogs vs Certificate Transparency vs Key Transparency

If you are familiar with Certificate Transparency, tlogs are derived from CT, but with a few major differences. Most importantly, there is no separate entry producer (in CT, the CAs) and log operator; moreover, clients check actual inclusion proofs instead of SCTs; finally, there are stronger split-view protections, as we will see below. The [Static CT API](https://c2sp.org/static-ct-api) and [Sunlight](https://sunlight.dev) CT log implementation were a first [successful](https://letsencrypt.org/2025/06/11/reflections-on-a-year-of-sunlight) step in moving CT towards the tlog ecosystem, and a proposed design called [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-davidben-tls-merkle-tree-certs/) redesigns the WebPKI to have tlog-like and tlog-interoperable transparency.

In my experience, it’s best *not* to think about CT when learning about tlogs. A better production example of a tlog is the [Go Checksum Database](https://golang.org/design/25530-sumdb), where Google logs the module name, version, and hash for every module version observed by the Go Modules Proxy. The module fetches happen over regular HTTPS, so there is no publicly-verifiable proof of their authenticity. Instead, the central party appends every observation to the tlog, so that any misbehavior can be caught. The `go get` command verifies inclusion proofs for every module it downloads, protecting 100% of the ecosystem, without requiring module authors to manage keys.

> Katie Hockman gave [a great talk on the Go Checksum Database](https://www.youtube.com/watch?v=KqTySYYhPUE) at GopherCon 2019.

You might also have heard of [Key Transparency](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/). KT is an overlapping technology that was deployed by Apple, WhatsApp, and Signal amongst others. It has similar goals, but picks different tradeoffs that involve significantly more complexity, in exchange for better privacy and scalability in some settings.

## A tlog for our keyserver

Ok, so how do we apply a tlog to our email-based keyserver?

It’s pretty simple, and we can do it with [a 250-line diff](https://github.com/FiloSottile/torchwood/commit/d031d34ec656156d51df074ae8823edd60329d92) using [Tessera](https://github.com/transparency-dev/tessera) and [Torchwood](https://filippo.io/torchwood). Tessera is a general-purpose...