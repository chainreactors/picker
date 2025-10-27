---
title: Blockchain 101
url: https://en.hackndo.com/blockchain/
source: hackndo
date: 2023-07-04
fetch_date: 2025-10-04T11:50:59.732704
---

# Blockchain 101

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

[![french flag](/assets/icones/fr.png)](https://beta.hackndo.com/blockchain/)

![Blockchain 101](/assets/uploads/2023/06/blockchain_banner.png "Blockchain 101")

# Blockchain 101

03 Jul 2023 · 10 min

Author : **[Pixis](https://twitter.com/HackAndDo)**

[Blockchain](/archives/#blockchain)

For several years now, I’ve been interested in a subject you’ve probably heard of: **blockchains**. I find it fascinating that a technology allows thousands of people to agree on so many subjects **without the need for an intermediary**. Decentralization is a subject that I believe has a lot of potential, and we’ll see in the long term whether this technology will endure or not. In any case, as it stands, it’s a hot topic! More recently, I’ve become interested in the **Ethereum** blockchain, **smart contracts**, and the **security of smart contracts**. We’re going to talk about all that here, here we go.

Before diving into the security of smart contracts, it’s important to recap some **key concepts about blockchains**. What is it, how does it work, who are the actors involved, we’ll look at all this in this introduction article. The idea is not to go into all the details, but to get an **overview** of how blockchains work in general. As the technical specifics vary greatly from one blockchain to another, we’ll cover them in due course in future articles.

## Definition

There are hundreds of definitions for the term **blockchain**. What I think is important to understand is that it represents a decentralized registry (or database). There is no central entity deciding whether a transaction is valid or not, but rather thousands of people or machines working to verify and validate these transactions, all driven by mathematical rules and concepts.

In a nutshell, we can simplify a blockchain by imagining it as a huge Excel spreadsheet in which you can add rows one after the other. It is also possible to read the entire Excel file, from the moment it was created. However, it is not possible to modify a line that has already been written and validated. It’s *append only*.

Of course, this is a simplification, as blockchains such as Ethereum include, in addition to classic transactions, a virtual machine with its own storage space and so on. We’ll talk about this in the next article.

## Transactions

What are these transactions? They are simply transfers of coins from one account to another. If Alice wants to send 1 coin to Bob, that’s a transaction.

> A **coin** is the cryptocurrency of the blockchain. For the Bitcoin blockchain, it’s Bitcoin, for the Ethereum blockchain it’s Ether, for Solana it’s Sol, and so on.

To find out if Alice has enough *coins*, all you have to do is read the transaction history. **The whole** history. If one day she received `3` *coins*, spent `2` of them, then received `4`, we can know, at the current time, that Alice has `3-2+4`, i.e. `5` *coins*. She is then entitled to spend 1 coin, so everything’s fine.

[![Alice balance](/assets/uploads/2023/06/alice_balance.png)](/assets/uploads/2023/06/alice_balance.png)

> Note that this is how Bitcoin works, but for other blockchains, the balance of each account is sometimes kept up to date (in the blockchain or not) to avoid having to recompute users’ balances for each transaction.

Here’s what a classic blockchain contains. A record of all users’ spending since the blockchain was created.

## User

To be a blockchain user, you need to have a pair of asymmetric keys: a public key and a private key. The private key, obviously carefully stored by each user, is used to sign all transactions. This is how, when Alice claims to be sending `1` coin to some address, it is possible to verify that it was Alice who initiated the transaction. She has **signed** it with her **private key**, and anyone can check that this signature is valid with her public key.

This means that in a blockchain, we don’t know that the user is **Alice**. Rather, a user is defined by an address (derived from the public key). So when Alice wants to execute a transaction, from the blockchain’s point of view, her **address** is the source of the transaction.

Furthermore, to communicate with the blockchain, the user will use a **client**. This is nothing more than a program that knows how to generate transactions, communicate with the network and so on. The user could code everything himself, but that’s not practical. It’s a bit like using a web browser to go online. It’s more practical than writing code to make HTTP requests.

## Validation

That’s all very well, but who validates these transactions? Who does the math to verify that Alice has at least `1` coin to send to someone? And checks that it’s really Alice who’s doing the transaction?

This is where the concepts of **blocks** and **validators** come in. For a blockchain to work properly, several people need to get to work validating transactions. They create so-called **nodes**, which will be able to broadcast themselves to the network and become part of it, retrieving past transactions and those awaiting validation. It’s a true **peer-to-peer** network. As soon as a user wants to send a transaction (**1**), the client he is using to send his transaction will notify another node (via [NewPooledTransactionHashes](https://eips.ethereum.org/EIPS/eip-2464)) that a new transaction has been sent (**2**). The transaction will be **verified** (signature verification, funds available, etc.) (**3**), but it is not yet **validated**. It will join the waiting list of transactions that have been sent but not yet validated, called the **mempool**. This node will also notify other nodes by broadcasting this transaction (**4**), and these new nodes will do the verification work themselves (**6**) and add this transaction to their mempool, and so on.

[![Tx Propagation](/assets/uploads/2023/06/tx_propagation.png)](/assets/uploads/2023/06/tx_propagation.png)

So there’s a whole bunch of transactions waiting to be validated, and that’s where the magic of the blockchain comes in. Transactions have to be validated, and all the nodes in the network will need to agree on which transactions should be validated, and the order in which they should be validated.

Each node then creates a block, the size of which is limited (and differs from one blockchain to another) by selecting pending transactions in the mempool. Once this block has been created, all the nodes compete to make its block the new reference block. The winner’s block becomes the last block in the chain. It is added to the previously validated blocks, the underlying transactions are no longer in the mempool, since they have been validated, and all nodes must therefore rebuild a new block with the transactions that have not yet been validated to try, once again, to win this competition.

[![New...