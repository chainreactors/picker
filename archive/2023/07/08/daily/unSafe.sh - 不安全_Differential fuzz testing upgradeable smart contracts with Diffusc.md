---
title: Differential fuzz testing upgradeable smart contracts with Diffusc
url: https://buaq.net/go-171488.html
source: unSafe.sh - 不安全
date: 2023-07-08
fetch_date: 2025-10-04T11:52:24.456844
---

# Differential fuzz testing upgradeable smart contracts with Diffusc

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

![](https://8aqnet.cdn.bcebos.com/bffb728110bd3908c02d32a05f85df25.jpg)

Differential fuzz testing upgradeable smart contracts with Diffusc

By William E Bodell III (@WEBthe3rd)On March 28, 2023, SafeMoon, a self-styled “
*2023-7-7 19:0:33
Author: [blog.trailofbits.com(查看原文)](/jump-171488.htm)
阅读量:26
收藏*

---

***By William E Bodell III (@WEBthe3rd)***

On March 28, 2023, SafeMoon, a self-styled “community-focused DeFi token” on Binance Smart Chain, lost the equivalent of $8.9 million in Binance Coin BNB to an exploit in a liquidity pool. The exploit leveraged a simple error introduced in an upgrade to SafeMoon’s SFM token contract, allowing the attacker to burn tokens held in the liquidity pool and artificially inflate their price before selling enough previously acquired tokens to completely drain the pool of wrapped BNB.

Smart contract upgrades are meant to fix bugs, but examples like this highlight how upgradeability can go terribly wrong. Thankfully, such bugs can be avoided with the right testing practices. To that end, it is my pleasure to introduce a new tool to your smart contract security toolbox, [Diffusc](https://github.com/crytic/diffusc), which I have been working on since February as an associate at Trail of Bits.

Diffusc combines static analysis with differential fuzz testing to compare two upgradeable smart contract (USC) implementations, which can uncover unexpected differences in behavior before an upgrade is performed on-chain. Built on top of Slither and Echidna, Diffusc performs differential taint analysis, uses the results to generate differential fuzz testing contracts in Solidity, and then feeds them into Echidna for fuzzing. It is, to my knowledge, the first implementation of differential fuzzing for smart contracts and should be used in combination with other auditing tools before performing an upgrade.

If you want to play with the tool right now, head on over to the [repo](https://github.com/crytic/diffusc#setup-1), follow the setup instructions in the README, and test it out on some real-world examples like Compound and Safemoon.

### Upgradeable smart contracts

While there are other ways of designing smart contracts for upgradeability, the most common USC pattern by far is the `delegatecall`-based proxy pattern. In this pattern, a proxy contract stores the address of an implementation contract, which can be changed by the contract owner or admin. There are many sub-patterns, but the key feature is the use of `delegatecall` in the proxy’s fallback function, which catches all calls to functions not defined in the proxy itself.

Crucially, `delegatecall` differs from the typical call opcode because it fetches the function code from the target contract but executes it in the context of the proxy, so the proxy’s storage is used for all business logic. This allows the implementation to be swapped out without the need for migrating the state to a new contract. For an in-depth survey of USC proxy patterns, see [Proxy Hunting: Understanding and Characterizing Proxy-based Upgradeable Smart Contracts in Blockchains](https://www.usenix.org/conference/usenixsecurity23/presentation/bodell) and our [Trail of Bits blog posts on upgradeability](https://secure-contracts.com/resources/tob_blogposts.html#upgradeability).

### Differential fuzzing

Fuzz testing is a security analysis technique in which randomly generated inputs are fed into the software under test while the fuzzer monitors its execution for errors. There are a variety of flavors, one of which is differential fuzzing, in which two similar implementations are fed the same inputs, with the fuzzer looking for any differences in execution between the two.

There are several fuzzers designed to test smart contracts specifically, of which Echidna is the most mature and feature rich. While fuzzers outside the realm of smart contracts often monitor the software under test for crashes, smart contract fuzzing typically looks for invariant violations. Invariants can be inserted into the contract under test itself (i.e., internal testing) or written in test functions that call into the contract under test from an external contract (i.e., external testing—for more detail see our [introduction to common testing approaches](https://secure-contracts.com/program-analysis/echidna/basic/common-testing-approaches.html)).

Differential fuzzing for smart contracts uses external testing, with test functions that take some random input and feed it into matching functions in both implementations and then compare the results of the two calls, asserting that they should be equal.

## Diffusc implementation

Diffusc is a human-assisted tool that aims to ease the validation of smart contract upgrades:

1. It leverages Slither’s static analysis to identify all functions that are impacted by the upgrade.
2. It generates wrappers to deploy and interact with the contracts. Wrapper contracts come in two flavors: standard mode and fork mode.
3. The user should review the wrappers for errors, add information that Diffusc could not infer automatically, and add additional invariants and preconditions where appropriate.
4. Finally, Diffusc leverages Echidna to perform differential fuzzing and to try to find issues with the upgrade. Some failing tests may require additional manual review.

*[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/07/image1.png?resize=690%2C290&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/07/image1.png?ssl=1)Figure 1. Diffusc architecture at a high level*

### Using Slither to diff upgrade versions

The first component of Diffusc is a pair of utility extensions in Slither, which will be included in an upcoming release of the static analysis tool. The upgradeability utility primarily does two things:

1. Compares two USC implementations to generate a diff, augmented by taint analysis to identify unmodified code that can be affected by changes made elsewhere
2. Identifies the storage slot in which a proxy stores its implementation address

The difficult part is in the implementation comparison and finding code that is affected by the changes.

#### Finding new and modified functions

To find new functions and variables, we compare the list of function signatures and variables for the two USCs. Missing or modified variables can be found the same way. To find modified functions, we rely on the intermediate representation (IR) of the function (through [SlithIR](https://github.com/crytic/slither/wiki/SlithIR)), and we traverse the control flow graph to see if the functions match. This allows us to look for semantic change and not be impacted by changes such as the addition of inline code comments or code formatting.

As an example, consider a somewhat simplified version of the Compound upgrade that introduced a token distribution bug.

In late September to October of 2021, a bug introduced in an upgrade to the [Compound protocol’s `Comptroller` contract](https://etherscan.io/address/0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b) caused tens of millions of dollars in COMP tokens to be erroneously distributed to users. After begging—and even threatening—users to return the funds, the Compound community ultimately lost about $40 million in reward tokens, diluting the positions of existing token holders.

One of the new functions, `_upgradeSplitCompRewards()`, initialized any existing markets that had not accrued any rewards with a new `index` value in the market’s corresponding `supplyState` struct. This new function was called by the modified `_become()` function, which is called as part of the upgrade pro...