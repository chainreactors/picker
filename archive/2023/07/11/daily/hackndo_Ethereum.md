---
title: Ethereum
url: https://en.hackndo.com/ethereum/
source: hackndo
date: 2023-07-11
fetch_date: 2025-10-04T11:50:55.099188
---

# Ethereum

[![hackndo logo](/assets/icones/logo.png) hackndo](/)
[Menu](#0)

# ![hackndo logo](/assets/icones/pixis_logo.png "logo") [hackndo](/)

Think out of the box

* [Home](/)
* [About](/about/)
* [Archives](/archives/)
* [Contact me](/contact/)
* [Disclaimer](/disclaimer/)
* [Projects](/projects/)

* Links
* [Login Sécurité](https://www.login-securite.com/)

* [![Twitter](/assets/icones/social/twitter.png "Twitter")](https://twitter.com/HackAndDo "Twitter")
* [![Github](/assets/icones/social/github.png "Github")](https://github.com/hackndo "Github")
* [![Youtube](/assets/icones/social/youtube.png "Youtube")](https://www.youtube.com/channel/UC9WYWHLdu9TK-0Hu3wcHJ9g "Youtube")
* [![Discord](/assets/icones/social/discord.png "Discord")](https://discord.hackndo.com "Discord")
* [![LinkedIn](/assets/icones/social/linkedin.png "LinkedIn")](https://www.linkedin.com/in/romainbentz/ "LinkedIn")
* [![Shell](/assets/icones/social/shell.png "Shell")](https://sh.hackndo.com "Shell")
* [![RSS](/assets/icones/social/rss.png "RSS")](/feed.xml "RSS")
* [![Ko-Fi](/assets/icones/social/kofi.gif "Ko-Fi")](https://ko-fi.com/hackndo "Ko-Fi")

© 2024. All rights reserved.

[![french flag](/assets/icones/fr.png)](https://beta.hackndo.com/ethereum/)

![Ethereum](/assets/uploads/2023/06/ethereum_banner.jpg "Ethereum")

# Ethereum

10 Jul 2023 · 13 min

Author : **[Pixis](https://twitter.com/HackAndDo)**

[Blockchain](/archives/#blockchain)

Unlike blockchains such as Bitcoin, which essentially allow Bitcoin cryptocurrency transactions to be sent, Ethereum also has something quite extraordinary: **decentralized** code execution.

Yes, decentralized. This means that we can write a program, code that is, and have it run not on one server, but on thousands of servers, or **nodes**. And the output of our program is also recorded in a decentralized way. I don’t know about you, but I think it’s incredible, and it really made me want to dig a little deeper into the subject.

So Ethereum is just another blockchain. There’s no shortage of blockchains today, but to date, Ethereum is the best-known and most widely used, at least in terms of blockchains that allow you to execute code. It does have its drawbacks, which other blockchains have addressed (albeit often to the detriment of other aspects), but that’s not really the point.

Let’s take a look at how Ethereum works, covering the notions of EOA accounts, contracts, states and transactions.

## Ethereum 101

We discussed how blockchains work in general in the article [Blockchain 101](/blockchain/). Ethereum operates in a similar way, with the consensus mechanism being the Proof of Stake. Ethereum’s own cryptocurrency is Ether (or ETH). Like Bitcoin and all other blockchains, Ethers can be sent to other users via transactions. Each user has his own address.

What Ethereum brings is that, in addition to regular users who send transactions, it is possible to create small programs, **smart contracts**, which also live on the blockchain. They all have addresses, just like users, but they also have code, stored on the blockchain.

To distinguish these two types of accounts, we call classic human users **EOA** (Externally Owned Accounts), which we distinguish from contract accounts, which we’ll simply refer to as **contracts**.

## EOA vs Contrats

Human-created accounts, or **EOAs**, are accounts with an address, a public key and a private key. They can initiate transactions by signing them, send Ethers and receive them. These transactions can be sent to other EOAs, allowing Ethers to be sent, but also to contracts.

**Contracts** also have an address, but no private key. **They cannot initiate transactions**. They can only react to transactions initiated by EOAs, or to messages sent by other contracts. Indeed, once called by an EOA, a contract can send messages to other contracts. The notion of *message* is discussed at the end of this article.

[![EOA vs Contract](/assets/uploads/2023/06/eoa_contract.png)](/assets/uploads/2023/06/eoa_contract.png)

## Data organization

Before we dive into why and how a contract account can execute code within the Ethereum ecosystem, let’s zoom in on the various data managed and used by Ethereum. Indeed, in this ecosystem, a **global state** of addresses must be kept up to date (with account balances, for example), the list of **transactions** must be stored and verifiable, the messages emitted in the various transactions must be accessible, and the permanent storage of each smart contract must, by definition, also be stored somewhere.

All this data **is not stored in the blocks of the blockchain**. Surprising as it may seem (at least to me at first sight), this information is stored in databases, **outside the blocks**, in the form of trees that follow a specific format: these are **Merkle Patricia Tries**, which enable a list of keys/values to be stored in an optimized way.

> There’s no typo, it’s `Trie`, not `Tree`, in reference to the word Re**trie**ve. We’ll probably see the Merkle Patricia Tries in detail in a dedicated article.

These data are therefore stored in the following trees:

* **State trie**, or **world state**, which itself contains links to **storage tries**.
  **Transactions tries**
* Receipt tries\*\*

In blocks, only the hash of the root of each of these trees is stored.

[![Ethereum Blocks](/assets/uploads/2023/06/ethereum_blocks.png)](/assets/uploads/2023/06/ethereum_blocks.png)

It’s up to each client to know how to store the contents of the trees and manage queries based on the root node hash (not all clients use the same database solutions, by the way).

This enables lightweight devices (mobile, IoT) to synchronize quickly and easily with the blockchain without having to download huge volumes of data, so that they only know the root nodes hashes for each block. With this information, they can query *full nodes*, i.e. nodes that have stored the blockchain, and also all the data in the databases, to send them the few pieces of information they need to validate any given data.

> Note that even an Ethereum full node only requires around 1TB of disk space. It’s accessible to everyone, which is why so many people participate in the decentralized network. There are also **archive nodes**. Unlike **full nodes**, which only synchronize with the last 128 blocks, archive nodes store the **entire** blockchain. For more information, please read [this article](https://www.quicknode.com/guides/infrastructure/node-setup/ethereum-full-node-vs-archive-node).

Let’s see what these different data trees correspond to.

## World State

Let’s start with the **State Trie**, or **World State**. We can point out that, while we were comparing a blockchain to a decentralized database, Ethereum is more complex and comprehensive than that. Instead, we could describe Ethereum as **a decentralized state machine**.

So, the general state of Ethereum is called **World State**. In this world state, there are all active user addresses (i.e. addresses present in at least one transaction), and each address has an associated **account state**.

[![World State](/assets/uploads/2023/06/world_state_basic.png)](/assets/uploads/2023/06/world_state_basic.png)

## Account State

The status of each account is therefore recorded in the **world state** containing the following 4 fields:

* `balance`: the account’s Ether balance
* `nonce`: A number that increments with each transaction for an EOA, and with each contract creation for a contract.
* `codeHash` : A hash that can be used to retrieve the smart contract’s code (the hash of an empty character string for an EOA).
* `storageRoot`: The root node hash of the Merkle Patricia Trie of **account storage**, or **storage trie**. It is used to retrieve the state of the contract, such as the value of permanently stored variables. This field is empty for an EOA account.

[![Account State](/assets/uploads/2023/06/world_state.png)](/assets/uploads/2023/06/world_state.png)

Each time...