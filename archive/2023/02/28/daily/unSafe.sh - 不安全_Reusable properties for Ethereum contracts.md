---
title: Reusable properties for Ethereum contracts
url: https://buaq.net/go-151241.html
source: unSafe.sh - 不安全
date: 2023-02-28
fetch_date: 2025-10-04T08:13:51.492615
---

# Reusable properties for Ethereum contracts

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

![]()

Reusable properties for Ethereum contracts

As smart contract security constantly evolves, property-based fuzzing has become
*2023-2-27 21:0:54
Author: [blog.trailofbits.com(查看原文)](/jump-151241.htm)
阅读量:27
收藏*

---

As smart contract security constantly evolves, property-based fuzzing has become a go-to technique for developers and security engineers. This technique relies on the creation of code properties – often called invariants – which describe what the code is supposed to do. To help the community define properties, we are releasing a set of [168 pre-built properties](https://github.com/crytic/properties) that can be used to guide Echidna, our smart contract fuzzing tool, or directly through unit tests. Properties covered include compliance with the most common ERC token interfaces, generically testable security properties, and properties for testing fixed point math operations.

Since mastering these tools takes time and practice, we will be holding two livestreams on our [Twitch](https://www.twitch.tv/trailofbits) and [YouTube channels](https://www.youtube.com/trailofbits) that will provide hands-on experience with these invariants:

* March 7 – ERC20 properties, example usage, and Echidna cheat codes (Guillermo Larregay)
* March 14 – ERC4626 properties, example usage, and tips on fuzzing effectively ([Benjamin Samuels](https://twitter.com/thebensams))

## Why should I use this?

The [repository](https://github.com/crytic/properties/blob/main/PROPERTIES.md#erc20) and related workshops will demonstrate how fuzzing can provide a much higher level of security assurance than unit tests alone. This collection of properties is simple to integrate with projects that use well-known standards or commonly-used libraries. This release contains tests for the [ABDKMath64x64 library](https://github.com/abdk-consulting/abdk-libraries-solidity), [ERC-20 token standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/), and [ERC-4626 tokenized vaults standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-4626/):

**ERC20**

* Properties for standard interface functions
* Inferred sanity properties (ex: no user balance should be greater than token supply)
* Properties for extensions such as burnable, mintable, and pausable tokens.

**ERC4626**

* Properties that verify rounding directions are compliant with spec
* Reversion properties for functions that must never revert
* Differential testing properties (ex: `deposit()` must match functionality predicted by `previewDeposit()`)
* Functionality properties (ex: `redeem()` deducts shares from the correct account)
* Non-spec security properties (share inflation attack, token approval checks, etc.)

**ABDKMath64x64**

* Communicative, associative, distributive, and identity properties for relevant functions
* Differential testing properties (ex: `2^(-x) == 1/2^(x)`)
* Reversion properties for functions which should revert for certain ranges of input
* Negative reversion properties for functions that should not revert for certain ranges of input
* Interval properties (ex: `min(x,y) <= avg(x,y) <= max(x,y)`)

The goal of these properties is to detect vulnerabilities or deviations from expected results, ensure adherence to standards, and provide guidance to developers writing invariants. By following this workshop, developers will be able to identify complex security issues that cannot be detected with conventional unit and parameterized tests. Furthermore, using this repository will enable developers to focus on deeper systemic issues instead of wasting time on low-hanging fruit.

As a bonus, while creating and testing these properties, we found a bug in the ABDKMath64x64 library: for a specific range of inputs to the divuu function, an assertion could be triggered in the library. More information about the bug, from one of the library's authors, can be found here.

## Do It Yourself!

If you don’t want to wait for the livestream, you can get started right now. Here’s how to add the properties to your own repo:

* Install [Echidna](https://github.com/crytic/echidna#installation).
* Import the properties into to your project:
  + In case of using Hardhat, use: `npm install <https://github.com/crytic/properties.git>` or `yarn add <https://github.com/crytic/properties.git>`
* Create a test contract according [to the documentation](https://github.com/crytic/properties/blob/main/README.md).

Let’s say you want to create a new ERC20 contract called `YetAnotherCashEquivalentToken`, and check that it is compliant with the standard. Following the previous steps, you create the following test contract for performing an external test:

```
pragma solidity ^0.8.0;
import "./path/to/YetAnotherCashEquivalentToken.sol";
import {ICryticTokenMock} from "@crytic/properties/contracts/ERC20/external/util/ITokenMock.sol";
import {CryticERC20ExternalBasicProperties} from "@crytic/properties/contracts/ERC20/external/properties/ERC20ExternalBasicProperties.sol";
import {PropertiesConstants} from "@crytic/properties/contracts/util/PropertiesConstants.sol";

contract CryticERC20ExternalHarness is CryticERC20ExternalBasicProperties {
    constructor() {
        // Deploy ERC20
        token = ICryticTokenMock(address(new CryticTokenMock()));
    }
}

contract CryticTokenMock is YetAnotherCashEquivalentToken, PropertiesConstants {

    bool public isMintableOrBurnable;
    uint256 public initialSupply;
    constructor () {
        _mint(USER1, INITIAL_BALANCE);
        _mint(USER2, INITIAL_BALANCE);
        _mint(USER3, INITIAL_BALANCE);
        _mint(msg.sender, INITIAL_BALANCE);

        initialSupply = totalSupply();
        isMintableOrBurnable = false;
    }
}
```

Then, a configuration file is needed to set the fuzzing parameters to run in Echidna:

```
corpusDir: "tests/crytic/erc20/echidna-corpus-internal"
testMode: assertion
testLimit: 100000
deployer: "0x10000"
sender: ["0x10000", "0x20000", "0x30000"]
multi-abi: true
```

Finally, run Echidna on the test contract:

```
echidna-test . --contract CryticERC20ExternalHarness --config tests/echidna-external.yaml
```

Furthermore, this effort is fluid. Some ideas for future work include:

* Test more of the widely-used mathematical libraries with our properties, such as PRBMath ([properties/issues/2](https://github.com/crytic/properties/issues/2)).
* Add tests for more ERC standards ([properties/issues/5](https://github.com/crytic/properties/issues/5)).
* Create a corpus of tests for other commonly used functions or contracts that are not standards, such as AMMs or liquidity pools ([properties/issues/4](https://github.com/crytic/properties/issues/4)).

文章来源: https://blog.trailofbits.com/2023/02/27/reusable-properties-ethereum-contracts-echidna/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)