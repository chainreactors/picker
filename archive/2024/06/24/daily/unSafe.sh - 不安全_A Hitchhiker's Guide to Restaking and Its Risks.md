---
title: A Hitchhiker's Guide to Restaking and Its Risks
url: https://buaq.net/go-246774.html
source: unSafe.sh - 不安全
date: 2024-06-24
fetch_date: 2025-10-06T16:54:49.471871
---

# A Hitchhiker's Guide to Restaking and Its Risks

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f01bdf5a04813fd4dfdf0f941072cbfb.jpg)

A Hitchhiker's Guide to Restaking and Its Risks

...Pandora's box has been opened, and there's no going back...Restaking is here. It's new, it's comp
*2024-6-23 22:0:22
Author: [hackernoon.com(查看原文)](/jump-246774.htm)
阅读量:6
收藏*

---

***...Pandora's box has been opened, and there's no going back...***

Restaking is here. It's new, it's complex, and it's changing Ethereum.

Sriram Kannan and his team at Eigen Layer created restaking. It lets Ethereum stakers secure other networks too. Jessy Cheng calls it "inevitably coming true" [5].

Restaking makes Ethereum staking more interesting. It could change the whole system. It offers benefits but also brings risks.

This guide explains restaking. We'll cover how it works, what it might do, and what could go wrong. If you care about a decentralized internet, you need to understand this.

But first, let's talk about staking. It's the foundation of restaking, and it's key to networks like Ethereum.

## Staking

Staking secures blockchain networks without mining. In proof-of-stake (PoS), validators put up cryptocurrency as collateral. The more they stake, the more likely they are to validate transactions and earn rewards.

Staking does two things:

* It makes people behave honestly.
* It keeps the network secure.

To be a validator, you "bond" some cryptocurrency. This shows you're committed. In return, you earn rewards.

If validators misbehave, they get "slashed." They lose some of their stake. This keeps everyone in line.

Some systems, like Ethereum, let you delegate your staking rights. You pick a staking service provider (SSP) to do the work for you. This is called Delegated Proof of Stake (DPoS) [6].

In short, staking keeps PoS networks running. It rewards good behavior and punishes bad. DPoS makes it easier for more people to join in.

Now that we understand staking, let's look at restaking.

## Restaking

Restaking expands the power of ETH stakers. It allows them to secure Ethereum and other protocols simultaneously, essentially "renting out" their staked ETH. Stakers agree to additional slashing conditions in exchange for rewards from securing oracles, layer 2 chains, bridges, and more.

The process works like this: Instead of setting a regular withdrawal address for staked ETH, you direct it to an Eigen Layer smart contract called an "eigenpod." This pod is jointly controlled by you and Eigen Layer.

Restaking adds complexity to the staking model. In the EigenLayer system, a delegator (or restaker) chooses a Strategy, which includes an Operator and the Actively Validated Services (AVSs) that the Operator supports. Operators must perform duties set by AVS protocols or face penalties like slashing (losing part of their stake) or jailing (being banned from operations) [7].

If you validate honestly across all opted-in protocols, you can withdraw freely. However, violating conditions on any protocol risks slashing a portion of your staked ETH. There's also an off-chain component: running node software for each additional protocol you're securing.
Restaking's potential impact rivals that of MEV (maximal extractable value). It opens up a vast design space, akin to modding a video game, but with far higher stakes—we're dealing with global economic infrastructure.

This innovation could fundamentally alter ETH's properties as an asset, much like EIP-1559 did. It maximizes opportunities for positive-sum games and allows academic research to transition into real-world applications.

## Cryptoeconomic Security and Its Challenges

Cryptoeconomic security is vital in decentralized systems. It measures the economic cost of corrupting a network. In Proof of Stake (PoS) networks, security stems from the total value of staked tokens [8].

Building strong cryptoeconomic security is a challenge for decentralized applications (dapps). Each new dapp often requires its own staking network, leading to fragmentation and limited security for individual services.

Restaking addresses these issues with a novel approach. By enabling ETH stakers to "restake" their assets across multiple services, it creates pooled security and a free market for trust. This allows dapps to leverage Ethereum's robust security without building their own staking networks from scratch [8].

EigenLayer's documentation describes 'pooled security' as a way to reuse economic security by allowing different AVSs to share a common base. In theory, this significantly increases the cost of compromising any individual AVS, as the shared security pool far exceeds what a single AVS could achieve alone [9].

The platform also offers 'attributable security', which is specific to each AVS and only slashable by that AVS. This is intended to provide additional guarantees for AVS customers, though its practical effectiveness remains to be seen [9].

EigenLayer aims to achieve economies of scale by allowing AVSs to share the same underlying smart contract infrastructure. While this could make collective security purchasing more efficient, it also introduces potential risks, such as increased complexity and interdependence between AVSs [9].

The combination of pooled and attributable security is EigenLayer's approach to flexibly and efficiently scaling economic security. While promising, this innovation comes with its own set of challenges and uncertainties that will need to be carefully monitored and addressed as the system develops.

## Concerns and Open Questions

Restaking isn't without its critics. Vitalik Buterin, for one, worries about stakers becoming "polyamorous." He sees potential dangers in this, particularly for Ethereum's economic security.

Several key questions remain unanswered:

* How will restaking alter Ethereum's security model?
* What new vulnerabilities might it create?
* How will it affect ETH's supply and demand?
* How will stakers use their new capabilities?

These aren't small concerns. They touch on the core of how Ethereum functions and how it might evolve.

Yet, for all the risks and unknowns, restaking's potential is hard to ignore. If it works, it could dramatically boost crypto's ability to create win-win economic scenarios. It might even push the technology into the mainstream.

Sriram Kannan frames it in evolutionary terms. He argues that humans' big advantage is our ability to "cooperate flexibly in large numbers." Restaking could take this to a new level. By reducing trust barriers, it might let us coordinate in ways we've never seen before.

We're watching a new economic model take shape. It's uncharted territory, full of both promise and peril. But one thing's for sure: it's an exciting time to be involved in this space.

## Restaking Architecture: A Symbiotic Relationship

The restaking ecosystem thrives on the symbiotic relationship between three key players: Actively Validated Services (AVSs), Operators, and Restakers.

![Restaking process](https://hackernoon.imgix.net/images/HFUEKwOWUPZSlUykLPDZ2wtZy5O2-2h93084.png?auto=format&fit=max&w=1920)

### Actively Validated Services (AVSs): Leveraging Ethereum's Security

AVSs are blockchain applications that could potentially use a restaking protocol to secure their transactions with Ethereum's validation mechanism. This approach would allow AVSs to bootstrap their security more efficiently and cost-effectively than setting up their own consensus mechanisms.

AVSs come in various forms, each serving a unique purpose:

* Layer-2 chains
* Data availability layers
* Sequencers
* dApps
* Cross-chain bridges
* Virtual machines

Traditionally, AVSs had to create their o...