---
title: A Primer On Slowable Encoders
url: https://buaq.net/go-150230.html
source: unSafe.sh - 不安全
date: 2023-02-21
fetch_date: 2025-10-04T07:35:05.760032
---

# A Primer On Slowable Encoders

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

![](https://8aqnet.cdn.bcebos.com/3b1210366b7bbfdd833151c33d8a985a.jpg)

A Primer On Slowable Encoders

There is a specific type of cryptographic transformation that arises in storage-oriented blo
*2023-2-20 22:38:17
Author: [research.nccgroup.com(查看原文)](/jump-150230.htm)
阅读量:19
收藏*

---

There is a specific type of cryptographic transformation that arises in storage-oriented blockchains. The transformation is a “slowable” 1-1 mapping which does not involve any secrets and is tradeoff-resistant in the following sense: it should not be possible to partially compute the function, store a fraction of the function’s state and then resume and finish the computation with anything less than the overall function’s computation runtime cost. In other words, knowledge of any partial function state does not offer a significant computation speed-up advantage.

In general, storage-oriented blockchains attempt to decentralize the traditionally centralized cloud data storage solutions. This is done by creating incentives for miners to store data and release it back to users, for a fee. The underlying blockchain’s consensus algorithm requires miners to demonstrate they possess unique replicas of the data. Processing the data with a slowable encoding function throttles the miners’ ability to manipulate the consensus by reusing data served from a central data store, or reusing data they store multiple times (in order to increase their chances of winning the consensus).

In this blog post, we chat about the storage blockchain context and what motivates the need for such functions. We’ll detail on why some basic constructions based on CBC encryption mode previously discussed in [[1](https://research.protocol.ai/publications/scaling-proof-of-replication-for-filecoin-mining/fisch2018.pdf)] do not work. The fact that these constructions do not work can be seen as a doorway for research on how to build working and optimal ones – some of the papers that do that job are linked to by the end of this blog post. Therefore, this blog post can be seen as an introductory read for a specific problem storage-oriented blockchains and papers such as [[1](https://research.protocol.ai/publications/scaling-proof-of-replication-for-filecoin-mining/fisch2018.pdf),[2](https://eprint.iacr.org/2013/796),[3](https://eprint.iacr.org/2016/333),[4](https://eprint.iacr.org/2016/875.pdf),[5](https://eprint.iacr.org/2015/366)] are trying to solve.

### Why encode before storing?

As mentioned, in decentralized storage blockchains, end-users can attempt to store data for a fee and miners are incentivized to store it for sufficiently long periods of time. Ideally, data should be stored in several replicas, to avoid data loss. The network should self-heal in the sense that, if the number of replicas for a particular piece of data becomes low, incentives exist for re-replicating the lost data pieces. All in all, miners are incentivized to store as many portions/chunks of the (ever-increasing) data blob as they can. The primary resource miners are competing with is storage space. The more chunks miners can store, the more likely is they will be able to win the upcoming block mining competition.

Some challenges in this context are:

* There needs to be a way of guaranteeing that storage providers are storing unique data replicas. A centralized storage solution may offer a data storage as a service and deliver it to miners for a fee, contrary to the intent to have as many data replicas as possible.
* Miners may be incentivized to store low-entropy (eg. all-zero) chunks as opposed to storing chunks with high entropy. All-zero chunks are advantageous, as they can be compressed, taking up minimal storage. When it’s time to use data chunks to participate in consensus, such chunks can be decompressed and sent to the network. This creates an incentive for storing dummy compressible data on the network which is contrary to the original intent- and that is to have a system which stores meaningful data.

### Properties slowable encoders should satisfy

To deal with the problems above, storage-oriented blockchains came up with the following idea: miners do not compete with the exact chunk data, rather, they compete with *encoded* data, bound to unique identifiers and identities. Consider encoding data before storing it with a 1-1 function that produces random-looking (uncompressible) output, such that it satisfies the following properties:

* Slowable, ie. purposefully hard to compute (not parallelizable, memory hard, ASIC-resistant etc.)
* Tradeoff-resistant: any significant fraction of the function’s computation time should not be tradable for a fraction of the function’s (intermediate) state.
* Optionally, the data encoding may be slow in the forward direction and fast in the backward direction.

The first requirement prevents miners from encoding on the fly; for example, it should not be possible for a miner to download the data from a different provider in plaintext, quickly process it with the function and use it to participate in consensus. Alternatively, the centralized data provider may serve an already processed piece of data, however, that wouldn’t work as the identity of the miner is baked in the transformation. Finally, using a slow enough function should prevent storing data in a compressed format and processing it through the function when participating to the consensus.

For this work, it is also necessary for the function to be tradeoff-resistant in the following sense. It should not be possible to partially compute the function, store some intermediate state significantly smaller than the function output and then be able to resume the computation and finish it for a cost significantly lower than overall computation cost; otherwise, miners would be able to trade storage space for computation cost, which is essentially unwanted in this context.

Finally, depending on the underlying protocol, the third property can help ease the computation workload on the parties that verify that providers actually do store the data.

Below are some primitives that do not satisfy such a tradeoff-resistance property:

* Use a stream cipher where the key initialization phase is computationally demanding and then derive as much keystream as required. The keystream is then XOR-ed with the data. If the inner state of the stream cipher is smaller in size than the desired keystream, a miner can compute the key initialization, store the cipher’s inner state and compute the keystream on the fly.
* The following (non-injective) computation: *`H(D|1) | H(D|2) | H(D|3) | .. | H(D|n)`*, where *`D`* is data and *`H`* is a slowable hash function. Suppose the miner computes and stores a subset of *`H(seed|i)`* blobs, achieving lower storage cost. The miner then computes the remaining `H` outputs on the fly.
* Use CBC-mode with a fixed publicly known key for each block and a slowable encryption primitive. A portion of the output can be saved and used to derive the remaining blocks.

### Building slowable encoders

The following constructions mentioned in [[1](https://research.protocol.ai/publications/scaling-proof-of-replication-for-filecoin-mining/fisch2018.pdf)] build a data encoding function with arbitrary input size from a smaller block encoder with fixed-size input *E*. Both constructions are insecure, but iterating on them can result in secure ones. It should be mentioned that while the building block is a block cipher, there are no secrets in this context and all the “keys” are public values.

Consider a simple “layered CBC mode”. It depends on a constant, (publically known) key *...