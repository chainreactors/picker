---
title: A Brief Review of Bitcoin Locking Scripts and Ordinals
url: https://buaq.net/go-167923.html
source: unSafe.sh - 不安全
date: 2023-06-09
fetch_date: 2025-10-04T11:45:55.888152
---

# A Brief Review of Bitcoin Locking Scripts and Ordinals

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

![](https://8aqnet.cdn.bcebos.com/ff9d0ef5287a5932ec45aa3098694e77.jpg)

A Brief Review of Bitcoin Locking Scripts and Ordinals

This article is an attempt at cataloging all the types of bitcoin transacti
*2023-6-8 23:16:54
Author: [research.nccgroup.com(查看原文)](/jump-167923.htm)
阅读量:73
收藏*

---

This article is an attempt at cataloging all the types of bitcoin transaction locking scripts, their prevalence and their security implications. The data presented in this article was lifted directly from the bitcoin blockchain, which required custom code to quickly iterate over the entire blockchain (over 450 GB at the time of writing). The tool is available on Github <https://github.com/nccgroup/FastBTCParser>.

Note: in the rest of this article, Bitcoin and Satoshi will be used interchangeably to refer to an amount of currency in a transaction (1 Bitcoin = 100,000,000 Satoshis).

## Anatomy of a Bitcoin Block

Bitcoin relies on the trust-less dissemination of a ledger called the Bitcoin blockchain, which holds a record of all transactions since the inception of Bitcoin. Each block on the chain contains a transaction made of:

* one or multiple input transactions (prior transaction outputs): all Bitcoins “spent” in a transaction, except for coinbase transactions, are one of the outputs of a prior transaction.
* Unlocking scripts (sometimes referred as `ScriptSig`): each input transaction’s output needs a valid unlocking script to authorize the spending of all the proceeds of that prior transaction.
* A list of transaction outputs: each transaction output receives an arbitrary amount from the total of input transactions proceeds, and each of these outputs needs a locking script (sometimes referred as `ScriptPubKey`).

Here is an example of a simple transaction data taken from the blockchain:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | 010000000151f36afbb502ff5dd7507845c79cb07e44edc86add4ffd068b3e7b |
|  | 4017bd290b000000008a4730440220591e3186aa579cd299eb27584a8f929eac |
|  | d8b4f810ba402b80f33a153fa8f3c1022024e0c4bc4710294a56ccf9e43c2714 |
|  | 88139e73ae1dbcd22bf4e6c2194b489a2e014104bd117a74f353dfc60809c1c8 |
|  | f7d57ddbb2bae869fb8bc3d863cb3e8ecab5af6816729494fb0687b298e67be8 |
|  | 75bafb5da82966394805611d0b1ef0f947025c1cffffffff02fe8ed485050000 |
|  | 001976a9147549ddbffcab3fbbb07c52adbe9476351c42f2b188ac001bb70000 |
|  | 0000001976a91465ed94fa5782ef897878140a2890babbf000853688ac000000 |
|  | 00 |

And here is that same transaction cut into its individual fields:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | 01000000 ] Transaction format version number |
|  | 01 ] Number of inputs |
|  | ———INPUTS———- |
|  | 51f36afbb502ff5dd7507845c79cb07e ┐ TXID (bytes reversed) |
|  | 44edc86add4ffd068b3e7b4017bd290b ┘ |
|  | 00000000 ] TXID Output number |
|  | 8a ] ScriptSig size (138 bytes) |
|  | 4730440220591e3186aa579cd299eb27 ┐ ScriptSig |
|  | 584a8f929eacd8b4f810ba402b80f33a | |
|  | 153fa8f3c1022024e0c4bc4710294a56 | |
|  | ccf9e43c271488139e73ae1dbcd22bf4 | |
|  | e6c2194b489a2e014104bd117a74f353 | |
|  | dfc60809c1c8f7d57ddbb2bae869fb8b | |
|  | c3d863cb3e8ecab5af6816729494fb06 | |
|  | 87b298e67be875bafb5da82966394805 | |
|  | 611d0b1ef0f947025c1c ┘ |
|  | ffffffff ] Sequence Number |
|  | ——END OF INPUTS—— |
|  | 02 ] Number of outputs |
|  | ———OUTPUTS——— |
|  | —OUTPUT 1— |
|  | fe8ed48505000000 ] Amount in Satoshis ~237 bitcoins (bytes reversed) |
|  | 19 ] ScriptPubKey size (25 bytes) |
|  | 76a9147549ddbffcab3fbbb07c52adbe ┐ ScriptPubKey |
|  | 9476351c42f2b188ac ┘ |
|  | —OUTPUT 2— |
|  | 001bb70000000000 ] Amount in Satoshis 12,000,000 (bytes reversed) |
|  | 19 ] ScriptPubKey size (25 bytes) |
|  | 76a91465ed94fa5782ef897878140a28 ┐ ScriptPubKey |
|  | 90babbf000853688ac ┘ |
|  | ——END OF OUTPUTS—– |
|  | 00000000 ] Lock time |

* `TXID` is the 32-byte ID of a prior transaction from which one of the outputs is going to be spent.
* `ScriptPubKey` is considered as a locking script. Each transaction output locks an arbitrary amount of Satoshis with such a script. Those Satoshis can then be used in a future transaction by unlocking them.
* `ScriptSig` is considered as an unlocking script. As such it needs to provide the adequate data and commands to satisfy the input transaction’s output locking script conditions to unlock its funds so that they can be spent in the current transaction.

## Bitcoin Scripting Language

In any Bitcoin transaction, the `ScriptSig` and `ScriptPubKey` are scripts written in a simple language with a limited amount of commands. The scripting language is not Turing-complete and each command is stored in a single byte. The language provides the ability to store fixed or variable length data blocks inlined within the script, and uses a stack to process that data.

In effect `ScriptSig` from the current transaction and `ScriptPubKey` from the input (prior) transaction are concatenated (referred to as “the script”) and executed to unlock the funds. The execution is successful, funds unlocked and spent, if:

* The script is valid
* The script is entirely executed
* A single non-zero value item remains on the stack

A complete description of the scripting language and commands can be found here: <https://en.bitcoin.it/wiki/Script>

The first output locking script or `ScriptPubKey` of the sample transaction above decodes to the following:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

This is a `P2PKH` type locking script and is described in the [Pay To Public Key Hash](#p2pkh-pay-to-public-key-hash) section.

## Locking scripts

Using the tool associated with this article ([see here](#somewhat-fast-bitcoin-blockchain-parser-tool)), we can now obtain a list of all existing locking script fingerprints, along with their prevalence. The fingerprinting process ignores any part of the script that’s data and replaces it with a `<data>` tag (but accounts for the data’s length if it is specified by the previous script op-code).

For brevity, only scripts with over 100 occurrences will be shown below. A complete unedited list can be found through the ([accompanying tool’s github page](#somewhat-fast-bitcoin-blockchain-parser-tool)). The complete list contains 156 unique script fingerprints.

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | #OCCURRENCES ITEM |
|  | 155 OP\_1 OP\_DATA\_65 <data> OP\_DATA\_65 <data> OP\_2 OP\_CHECKMULTISIG |
|  | 182 OP\_IFDUP OP\_IF OP\_2SWAP OP\_VERIFY OP\_2OVER OP\_DEPTH |
|  | 336 OP\_DATA\_36 <data> |
|  | 753 OP\_1 OP\_DATA\_65 <data> OP\_1 OP\_CHECKMULTISIG |
|  | 986 OP\_DATA\_32 <data> |
|  | 1693 OP\_1 OP\_DATA\_33 <data> OP\_1 OP\_CHECKMULTISIG |
|...