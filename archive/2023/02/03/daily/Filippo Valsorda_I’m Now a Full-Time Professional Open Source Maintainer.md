---
title: I’m Now a Full-Time Professional Open Source Maintainer
url: https://words.filippo.io/full-time-maintainer/
source: Filippo Valsorda
date: 2023-02-03
fetch_date: 2025-10-04T05:33:03.626892
---

# I’m Now a Full-Time Professional Open Source Maintainer

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

2 Feb 2023

# I’m Now a Full-Time Professional Open Source Maintainer

Last May [I left my job on the Go team at Google](https://twitter.com/FiloSottile/status/1522671407636877315) to experiment with more sustainable paths for open-source maintainers. I held on to my various maintainer hats ([Go cryptography](https://words.filippo.io/dispatches/go-1-20-cryptography/), transparency tooling, [age](https://age-encryption.org), [mkcert](https://mkcert.dev), [yubikey-agent](https://github.com/FiloSottile/yubikey-agent)…), iterated on the model since September, and I’m happy to report that **I am now a full-time independent open-source maintainer**. That means I spend most of my time on maintenance, and I offer retainers to companies that benefit from my work and from access to my planning and my expertise. I now have six amazing clients, and I’m making an amount of money equivalent to my Google total compensation package,[1](#fn:tc) which proves the thesis that it’s possible to be a professional maintainer earning rates competitive with the adjacent market for senior software engineers.

For this first client cohort, I focused on companies that already understand open source, that work in fields adjacent to mine, and that I could reach through my network. My first client, who believed in the project before I even had a prospectus or contract tiers, is Glasklar Teknik AB, a new sister company to [Mullvad VPN](https://mullvad.net/en/).[3](#fn:mullvad) Glasklar funds the development of [Sigsum](https://www.sigsum.org/), an open-source public transparency log designed to produce offline-verifiable proofs, that came out of [system transparency](https://www.system-transparency.org/) research by Mullvad. I’ve been working on Sigsum and on a framework and ecosystem of compatible and aligned open-source transparency tooling, and the collaboration has been great. In the order they joined, then came: [Protocol Labs](https://protocol.ai/), who maintains IPFS and Filecoin, and whose [R&D team](https://research.protocol.ai/) produces [excellent research on zero knowledge proofs and cryptography](https://research.protocol.ai/areas/cryptography/); [Latacora](https://www.latacora.com/), a retained security team for startups, who amongst other things makes resources such as myself available to their clients; the [Interchain Foundation](https://interchain.io/), themselves the stewards of the development of the open-source Cosmos SDK, a large critical Go+cryptography project; [Smallstep](https://smallstep.com/), who provides easy-to-use PKI and Zero Trust tools (largely written in Go!) to manage human and machine identities; and [Tailscale](https://tailscale.com/), a mesh VPN that feels like magic, with [a passion for JSON, SQLite](https://tailscale.com/blog/database-for-2022/), and Go.[2](#fn:sponsored)

![The six logos of my clients: Sigsum, Protocol Labs, Latacora, Interchain Foundation, Smallstep, Tailscale](https://assets.buttondown.email/images/13d4d773-20a4-400e-aab8-f3a7b42850a1.png)

I’m sharing details about my progress to hopefully popularize the model, and eventually help other maintainers adopt it, although I’m not quite ready to recommend anyone else drop everything to try this just yet.

This experiment started from the observation that despite being critical for the functioning of the Internet—and, by extension, the economy—the role of open-source maintainer has not yet found a sustainable manifestation. Virtually all maintainers are either volunteers or full-time employees of large companies. Foundations on average [don’t pay maintainers](https://twitter.com/fux0r/status/1470034538923503621). A few projects manage to fundraise by selling support contracts or getting feature-scoped sponsorships.

All these models fail to align incentives with those of the project. Volunteerism is self-evidently not sustainable, as people’s life circumstances change.[4](#fn:volunteer) Full-time corporate employment scales poorly over time and especially when the project succeeds.[5](#fn:fulltime) Support contracts take significant time away from the actual maintenance work. Feature-scoped sponsorships reward *increasing* future maintenance burden without funding it.

What I’m doing is different, and I’m hoping it will be more sustainable, as well as reproducible for others. I am a professional full-time independent open-source maintainer. I’m funded through retainer agreements with a number of clients, and I get to focus primarily on maintenance work.

I’m not selling support hours or hard project deliverables. Instead, my clients get value in three ways:

1. they mitigate the business risk of a project they depend on going unmaintained, with its security and development velocity implications;
2. we establish a channel for reciprocal access, ensuring better outcomes for both them and the project; and
3. at the highest contract tiers, I’m available for advice on any topic I am an expert in, beyond the strict scope of the open-source project.

The business risk mitigation proposition is what every sponsorship offers, so it’s not at all innovative, but it’s important to forward-looking companies.

I’ve written before about [the value of reciprocal access](https://words.filippo.io/dispatches/reciprocal/), but it boils down to this: I go in, meet the engineers, and learn what parts of my projects they use and how; then, I keep those use cases in mind in my own planning and I reach out and involve them for feedback when there are relevant changes on the roadmap. This improves outcomes for everyone: I want my projects to work well for users (regardless of whether they are paying me) and no one wants to find out something’s wrong after the release. Companies could get this “for free” by closely monitoring the issue tracker themselves and being active in development discussions, but dedicating an engineer to that task would probably be more expensive than my rate!

The expert advisor service at the top contract tier is a recent evolution of the model, based on conversations with Kaylyn Gibilterra, Kelsey Hightower, and others. I’m available to these clients for advice on all the topics I’ve become an expert in through my open-source maintenance years: cryptography, protocols, their implementations, Go, software supply chain security, open source, transparency logs, PKIs… The main concern I had attaching this to the offering was how reproducible it is: I know I can make a living as an advisor myself, but is it something that open-source maintainers can do reproducibly to financially sustain a main focus on project work? My hypothesis is that it is a great match for maintainers at large: maintainers are very legibly and recognizably experts in their field, *because* they maintain open-source software. If a company already uses my cryptography software, that’s probably the reason they believe I’m an expert in cryptography, and that they could use a cryptography advisor. It all correlates well, and would apply to any maintainer of a critical piece of open-source software: Kubernetes maintainers are orchestration and platform experts, ffmpeg maintainers are A/V experts, web server maintainers are HTTP experts. It also aligns incentives well with those of my projects: I’m an expert *because* I’m a maintainer, so it’s both in my clients’ and in my own interest for me to keep doing maintenance work.

I used a key word above: *critical*. The model I am experimenting with is geared towards the maintainers of critical open-source projects. In the metaphor of [the XKCD comic you’ve all probably seen](https://xkcd.com/2347/) it’s meant to work for the projects at the bottom of the pile, maybe not for the ones at the very top. However, what’s critical depends on the client’s perspective, and many projects are critical for at least some businesses. This is how I frame it: if t...