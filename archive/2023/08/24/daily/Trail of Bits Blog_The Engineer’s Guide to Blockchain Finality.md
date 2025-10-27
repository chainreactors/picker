---
title: The Engineer’s Guide to Blockchain Finality
url: https://blog.trailofbits.com/2023/08/23/the-engineers-guide-to-blockchain-finality/
source: Trail of Bits Blog
date: 2023-08-24
fetch_date: 2025-10-04T12:00:39.333535
---

# The Engineer’s Guide to Blockchain Finality

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The Engineer’s Guide to Blockchain Finality

[Benjamin Samuels](https://x.com/thebensams)

August 23, 2023

[vulnerability-disclosure](/categories/vulnerability-disclosure/), [blockchain](/categories/blockchain/)

Many security-critical off-chain applications use a simple block delay to determine finality: the point at which a transaction becomes immutable in a blockchain’s ledger (and is impossible to “undo” without extreme economic cost). But this is inadequate for most networks, and can become a single point of failure for the centralized exchanges, multi-chain bridges, and L2 scaling solutions that rely on transaction finality. Without proper consideration of a blockchain’s finality criteria, transactions that appear final can be expunged from the blockchain by a malicious actor in an event called a re-org, leading to double-spend attacks and value stolen from the application.

We researched several off-chain applications and L2 networks and discovered two L2 clients, Juno and Pathfinder, that either were not checking for finality or incorrectly used block delays to detect whether Ethereum blocks were finalized. We disclosed our findings to each product team, and fixes were published shortly after disclosure in version [v0.4.0](https://github.com/NethermindEth/juno/releases/tag/v0.4.0) for Juno and [v0.6.2](https://github.com/eqlabs/pathfinder/releases/tag/v0.6.2) for Pathfinder. This blog post gathers the knowledge and insights we gained from this research. It explains the dangers of reorgs, the differences between distinct finality mechanisms, and how to prevent double-spend attacks when writing applications that consume data from different kinds of blockchains.

## Understanding re-orgs

When a user submits a transaction to a blockchain, it follows a lifecycle that is nearly identical across all blockchains. First, their transaction is gossiped across the blockchain’s peer-to-peer network to a block proposer. Once a block proposer receives the transaction and includes it in a block, the block is broadcast across the network.

Here is where the problems begin: some blockchains don’t explicitly define who the next block proposer should be, and the ones that do need a way to recover if that proposer is offline. These conditions lead to situations where there are two or more valid ways for the blockchain to proceed (a fork), and the network has to figure out which fork should be canonical.

[![](/img/wpdump/bf61f2d1d21f2e18e517037a2db50501.png)](/img/wpdump/bf61f2d1d21f2e18e517037a2db50501.png)

*Figure 1: Two miners on a PoW network propose a valid block for slot 4 at the same time.*

Blockchains are designed with these issues in mind and define a fork choice rule to determine which fork should be considered canonical. Forks can sometimes last for multiple blocks, where different portions of the network consider a different chain to be canonical.

[![](/img/wpdump/3989488e815c136c3164da7fb8cebaaa.png)](/img/wpdump/3989488e815c136c3164da7fb8cebaaa.png)

*Figure 2: A PoW network where block candidates for slots 4, 5, and 6 were mined in quick succession and built on different parents, leading to a fork.*

Assuming there is no bug in the network’s software, the fork will eventually be reconciled, leading to a single fork becoming canonical. The other forks, their blocks, and their transactions are expunged from the blockchain’s history, called a re-org.

When a transaction is expunged from the chain via a re-org, that transaction may either be re-queued for inclusion in a new block, or otherwise have its ordering or block number changed to whatever it is in the canonical chain. Attackers can leverage these changes to modify a transaction’s behavior or cancel the transaction entirely based on which fork it is included on.

[![](/img/wpdump/bad01969928c08838c042cde61d70afe.png)](/img/wpdump/bad01969928c08838c042cde61d70afe.png)

*Figure 3: A network after a three-block re-org. Transactions in blocks 4a, 5a, and 6a are no longer part of the canonical chain.*

Re-orgs are a normal part of a blockchain’s lifecycle, and can happen regularly due to factors like block production speed, network latency, and network health. However, attackers can take advantage of (and even orchestrate!) re-orgs to perform double-spend attacks, a category of attack where an attacker submits a deposit transaction, waits for it to be included in a block, then orchestrates a re-org to expunge their transaction from the canonical chain while still receiving credit for their deposit on the off-chain application.

It is for this reason that finality considerations are important. If a centralized exchange or bridge indexes a deposit transaction that is not final, it is vulnerable to double-spend attacks by way of an attacker causing a re-org of the blockchain.

Blockchains use a variety of different consensus algorithms and thus have a variety of different finality conditions that should be considered for each chain.

## Probabilistic finality

*Examples: Bitcoin, Binance Smart Chain (pre-BEP-126), Polygon PoS, Avalanche – or generally any PoW-based blockchain*

Chains using probabilistic finality are unique in that their blocks are never actually finalized—instead, they become probabilistically final, or more “final” as time goes on. Given enough time, the probability that a previous block will be re-orged off the chain approaches zero, and thus the block becomes final.

In most probabilistically final chains, the fork choice rule that determines the canonical chain is based on whichever fork has the most blocks built on top of it, called Nakamoto consensus. Under Nakamoto consensus, the chain may re-org if a longer chain is broadcast to the network, even if the longer chain excludes blocks/transactions that were already included in the shorter chain.

### Double-spend attacks on probabilistic proof-of-work networks

The classic attack against proof-of-work networks is a 51% re-org attack. This attack requires an off-chain exchange, bridge, or other application that indexes deposit transactions very quickly, ideally indexing blocks as soon as they are produced or with an exceedingly short delay.

The attacker must accumulate, purchase, or rent enough computing resources so the attacker controls the majority of the hash power on the network. This means the attacker has enough resources to privately mine a chain that’s longer than the honest canonical chain. Note that this is a probabilistic attack; control over 51% of the network’s hash power makes the attack an eventual certainty. An attacker could theoretically perform double-spend attacks with much less than 51% of the network’s hash power, but it may require many attempts before the attack succeeds.

Once the mining resources are ready, the attacker submits a transaction on the public, canonical chain to deposit funds from their wallet to the exchange/bridge.

Immediately afterward, the attacker must create a second, conflicting transaction that transfers funds from their wallet to another attacker-controlled address. The attacker configures their mining resources to mine a new fork that includes the transfer transaction instead of the deposit transaction.

[![](/img/wpdump/c30b268669ccee01198975a028e894b0.png)](/img/wpdump/c30b268669ccee01198975a028e894b0.png)

*Figure 4: The attacker creates a private fork that includes their transfer transaction instead of the deposit transaction.*

Given that the attacker controls the majority of the hash power on the network, eventually their private fork will have more blocks than the canonical fork. Once they have received credit for the deposit transaction and their private fork has more blocks than the canonical chain, the attacker instructs their network to publish the private chain’s blocks to the honest nodes following the canonical chain.

The hon...