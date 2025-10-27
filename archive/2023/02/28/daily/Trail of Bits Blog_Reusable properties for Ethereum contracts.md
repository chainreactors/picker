---
title: Reusable properties for Ethereum contracts
url: https://blog.trailofbits.com/2023/02/27/reusable-properties-ethereum-contracts-echidna/
source: Trail of Bits Blog
date: 2023-02-28
fetch_date: 2025-10-04T08:14:33.640741
---

# Reusable properties for Ethereum contracts

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Reusable properties for Ethereum contracts

Trail of Bits

February 27, 2023

[blockchain](/categories/blockchain/), [education](/categories/education/), [guides](/categories/guides/)

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
  + In case of using Hardhat, use: `npm install https://github.com/crytic/properties.git` or `yarn add https://github.com/crytic/properties.git`
    In case of using Foundry, use: `forge install crytic/properties`
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

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.