---
title: Fuzzing on-chain contracts with Echidna
url: https://buaq.net/go-172663.html
source: unSafe.sh - 不安全
date: 2023-07-22
fetch_date: 2025-10-04T11:52:30.188291
---

# Fuzzing on-chain contracts with Echidna

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

![](https://8aqnet.cdn.bcebos.com/5987e8a588b8b1a98b7ad2c71ef06edc.jpg)

Fuzzing on-chain contracts with Echidna

By Guillermo Larregay and Elvis SkozdopoljWith the release of version 2.1.0 of E
*2023-7-21 19:0:31
Author: [blog.trailofbits.com(查看原文)](/jump-172663.htm)
阅读量:32
收藏*

---

*By Guillermo Larregay and Elvis Skozdopolj*

With the release of version 2.1.0 of [Echidna](https://github.com/crytic/echidna), our fuzzing tool for Ethereum smart contracts, we’ve introduced new features for direct retrieval of on-chain data, such as contract code and storage slot values. This data can be used to fuzz deployed contracts in their on-chain state or to test how new code integrates with existing contracts.

Echidna now has the capability to recreate real-world hacks by fuzzing contract interfaces and on-chain code. In this blog post, we’ll demonstrate how the 2022 [Stax Finance](https://medium.com/neptune-mutual/decoding-stax-finances-vulnerability-4e9a7abac82c) hack was reproduced using only Echidna to find and exploit the vulnerability. This incident involved a missing validation check in the `[StaxLPStaking](https://etherscan.io/address/0xd2869042e12a3506100af1d192b5b04d65137941#code)` contract, which led to the theft of 321,154 xLP tokens, worth approximately $2.3 million at the time of the attack.

Echidna’s “optimization mode” will automatically discover transaction sequences that maximize or minimize the outcome of a custom function. In this case, we’ll simply ask it to maximize an attacker’s balance and let it do the rest of the work.

## Recreating the Stax Finance exploit

To reproduce the Stax Finance exploit using Echidna, we need:

* A contract to be fuzzed by Echidna that wraps the target Stax contract and related contracts (figure 1)
* An Echidna configuration file that contains the block number from before the attack took place and an RPC provider to get on-chain information (figure 2)

Figure 1 shows a simplified version of the fuzzing contract contract, and figure 2 shows the configuration file. You can find the full contract and configuration file [here](https://gist.github.com/tuturu-tech/efbba5a57465c9e75f0ed0050bbc49ed).

```
contract StaxExploit {

    IStaxLP StaxLP = IStaxLP(0xBcB8b7FC9197fEDa75C101fA69d3211b5a30dCD9);
    IStaxLPStaking StaxLPStaking =
        IStaxLPStaking(0xd2869042E12a3506100af1D192b5b04D65137941);

    ...

    constructor() {
        // Using HEVM to set the block.number and block.timestamp
        hevm.warp(1665493703);
        hevm.roll(15725066);

        // setting up initial balances
        ...
    }

    function getBalance() internal returns (uint256) {
        return StaxLP.balanceOf(address(this));
    }

    function stake(uint256 _amount) public {
        _amount = (_amount % getBalance()) + 1;
        StaxLPStaking.stake(_amount);
    }

    // Other functions wrappers ...

    function migrateStake(
        address oldStaking,
        uint256 amount
    ) public {
        StaxLPStaking.migrateStake(oldStaking, amount);
    }

    function migrateWithdraw(
        address staker,
        uint256 amount
    ) public {
        StaxLPStaking.migrateWithdraw(staker, amount);
    }

    fallback() external payable {}

    // The optimization function
    function echidna_optimize_extracted_profit() public returns (int256) {
        return (int256(StaxLP.balanceOf(address(this))) -
            int256(initialAmount));
    }
}
```

Figure 1: The attacker contract

In the fuzzing contract, we added a function called `echidna_optimize_extracted_profit()`, allowing Echidna to monitor the profit for the current transaction sequence and identify the most profitable one.

```
testMode: optimization
testLimit: 1000000
corpusDir: corpus-stax
rpcUrl: https://.../
rpcBlock: 15725066
```

Figure 2: The Echidna configuration file

As shown in the configuration file, we set Echidna to run in optimization mode to maximize the profit function.

Next, we ran Echidna on the fuzzing contract using the command in figure 3.

```
$ echidna ./StaxExploit.sol --config echidna-config.yaml
```

Figure 3: The command used to execute Echidna

Echidna’s optimizer generates random sequences of function calls with varying arguments, calculating the return value of the `echidna_optimize_extracted_profit()` function for each sequence. At the end of the run, it discards any unnecessary or reverting calls from the sequence of transactions, leaving only those calls that maximize the profit.

Thus, with our fuzzing contract and the profit function, Echidna can swiftly discover the correct sequence of transactions to reproduce the hack, without needing prior knowledge of the actual contract exploit.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/07/Echidna-run.png?resize=690%2C329&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/07/Echidna-run.png?ssl=1)

Figure 4: An Echidna run using the code in this post

### Nitty-gritty details

Now that we’ve given a high-level overview of how Echidna can recreate the exploit, let’s dive into some technical details for readers interested in trying this out on their own.

To set up the fuzzing contract, we used [Slither’s code generation utilities](https://github.com/crytic/slither/blob/master/slither/utils/code_generation.py). This let us get the target contract’s interface and deployment address, in addition to other necessary interfaces and addresses (e.g., ERC-20 tokens, other contracts, and user-defined data types), from Etherscan. We also created wrappers for Echidna to call the contract functions, and we added our `echidna_optimize_extracted_profit()` function.

We took advantage of Echidna’s ability to use [hevm](https://hevm.dev/controlling-the-unit-testing-environment.html#cheat-codes) cheat codes for manipulating the execution environment. This involved setting the block number and block timestamp to a point in time just prior to the actual exploit. To streamline the use of [hevm cheat codes](https://github.com/crytic/properties#hevm-cheat-codes-support), we used helpers from our [`properties` repository](https://github.com/crytic/properties) and imported the [`HEVM.sol` helper](https://github.com/crytic/properties/blob/main/contracts/util/Hevm.sol).

In setting up the configuration file, we configured `testMode` to `optimization`. We also assigned the RPC provider and block number (indicated by `rpcUrl` and `rpcBlock` parameters, respectively) for Echidna to fetch the on-chain information. To prevent an indefinite runtime in case Echidna doesn’t find the exploit, we set an upper limit of one million test runs through the `testLimit` parameter. The resulting corpus was stored in the `corpus-stax` directory, as specified in the `corpusDir` parameter.

## Limitations and challenges

While Echidna is a powerful tool, it’s not without limitations and challenges:

1. Echidna might not find all vulnerabilities. Since fuzz testing can’t guarantee complete coverage, it’s crucial to augment Echidna with other security testing methods like static analysis, formal verification, and even unit testing (e.g., 100% branch coverage, testing for edge cases, positive and negative tests, etc.), for a comprehensive analysis.
2. Complex contracts may require more time. Depending on the complexity of the smart contract, it might take Echidna longer to discover vulnerabilities.
3. Fetching contracts and slots from the network can be slow. API rate limits can hinder the process of acquiring on-chain information for contracts using numerous storage slots. There are ongoing discussions on how to mitigate this issue.
4. Custo...