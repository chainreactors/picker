---
title: How Sui Move rethinks flash loan security
url: https://blog.trailofbits.com/2025/09/10/how-sui-move-rethinks-flash-loan-security/
source: The Trail of Bits Blog
date: 2025-09-11
fetch_date: 2025-10-02T19:58:13.175644
---

# How Sui Move rethinks flash loan security

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How Sui Move rethinks flash loan security

Nicolas Donboly

September 10, 2025

[blockchain](/categories/blockchain/)

Page content

* [The Solidity approach: Callbacks and runtime checks](#the-solidity-approach-callbacks-and-runtime-checks)
* [The Sui Move approach: Composable safety](#the-sui-move-approach-composable-safety)
  + [Sui’s object model and Move’s abilities](#suis-object-model-and-moves-abilities)
  + [How PTBs work](#how-ptbs-work)
  + [Move bytecode verifier](#move-bytecode-verifier)
* [The hot potato pattern in action: DeepBookV3](#the-hot-potato-pattern-in-action-deepbookv3)
  + [How the hot potato pattern ensures repayment](#how-the-hot-potato-pattern-ensures-repayment)
* [Implementing safety by design](#implementing-safety-by-design)

Flash loans, a fundamental DeFi primitive that enables collateral-free borrowing as long as repayment occurs within the same transaction, have historically been a double-edged sword. While they allow honest borrowers to perform arbitrage and debt refinancing, they have also enabled attackers to amplify the impact of their exploits and increase the amount of funds stolen. We found that Sui’s Move language significantly improves flash loan security by replacing Solidity’s reliance on callbacks and runtime checks with a “hot potato” model that enforces repayment at the language level. This shift makes flash loan security a language guarantee rather than a developer responsibility.

This post analyzes the flash loan implementation from [DeepBookV3](https://docs.sui.io/standards/deepbook), Sui’s native order book DEX. We compare Sui’s implementation to common Solidity patterns and show how Move’s design philosophy of making security the default rather than the developer’s responsibility provides stronger safety guarantees while simplifying the developer experience.

## The Solidity approach: Callbacks and runtime checks

Solidity flash loan protocols traditionally rely on a callback pattern, which provides maximum flexibility but places the entire security burden on developers. The process requires the lending protocol to temporarily trust the borrower before it can validate repayment.

The typical flow involves these steps:

1. A borrower contract calls `flashLoan` on the lending protocol.
2. The protocol transfers the tokens to the borrower contract.
3. The protocol then calls an `onFlashLoan` function on the borrower contract.
4. The borrower contract performs its logic with the borrowed tokens.
5. The borrower contract repays the loan.
6. The original lending protocol checks its balance to confirm repayment and reverts the entire transaction if the funds haven’t been returned.

![Flowchart showing the standard callback flow for a flash loan in Solidity](/img/sui_move_figure_1.png)

Figure 1: The standard callback flow for a flash loan in Solidity

This callback-based model places security responsibilities on the lending protocol developer, who must implement a balance check at the end of the function to ensure the safety of the loan (figure 2). Because the protocol makes an external call to the borrower’s contract, developers must carefully manage the state to prevent reentrancy risks. The Fei Protocol developers [learned this lesson at a cost of $80M in 2022](https://rekt.news/fei-rari-rekt) when a hacker exploited a flaw in the system (in particular, that it did not follow the [check-effect-interaction](https://docs.soliditylang.org/en/v0.6.11/security-considerations.html#use-the-checks-effects-interactions-pattern) (CEI) pattern) to borrow funds and then withdraw their collateral before the borrow was recorded Even the borrower can be at risk if the access control on their receiver contract isn’t properly implemented.

```
function flashLoan(uint256 amount, address borrowerContract) external {
    uint256 balanceBefore = token.balanceOf(address(this));

    token.transfer(borrowerContract, amount);
    borrowerContract.onFlashloan();

    if (token.balanceOf(address(this)) < balanceBefore) {
        revert RepayFailed();
    }
}
```

Figure 2: A pseudo-Solidity implementation of a flash loan

Additionally, the lack of a standard interface initially caused fragmentation. Although [EIP-3156](https://eips.ethereum.org/EIPS/eip-3156) later proposed a standard for single-asset flash loans, where the lender [pulls the funds back from the borrower](https://eips.ethereum.org/EIPS/eip-3156#flash-loan-reference-implementation) instead of expecting the funds to be sent by the borrower, it has yet to be adopted by all major DeFi protocols and comes with its own set of [security challenges](https://rareskills.io/post/erc-3156).

## The Sui Move approach: Composable safety

Sui’s implementation of flash loans is fundamentally different. It leverages three core features of the platform—a unique object model, Programmable Transaction Blocks (PTBs), and the bytecode verifier—to provide flash loan security at the language level.

### Sui’s object model and Move’s abilities

To understand Move’s safety guarantees, one must first understand Sui’s object model. In Ethereum’s account-based model, a token balance is just a number in a ledger (the [ERC20](https://eips.ethereum.org/EIPS/eip-20) contract) that keeps track of who owns what. A user’s wallet doesn’t hold the tokens directly, but instead holds a key that allows it to ask the central contract what its balance is.

![Image depicting how users’ balances are entries within a central contract’s storage](/img/sui_move_figure_3.png)

Figure 3: In Ethereum, users' balances are entries within a central contract's storage.

In contrast, Sui’s object-centric model treats every asset (a token, an NFT, admin rights, or a liquidity pool position) as a distinct, independent object. In Sui, everything is an object, carrying properties, ownership rights, and the ability to be transferred or modified. A user’s account directly owns these objects. There is no central contract ledger; ownership is a direct relationship between the account and the object itself.

![Image depicting how in Sui, users directly own a collection of independent objects](/img/sui_move_figure_4.png)

Figure 4: In Sui, users directly own a collection of independent objects.

This object-centric approach (which is specific to Sui, not the Move language itself) is what enables [parallel transaction processing](https://blog.sui.io/parallelization-explained/) and allows objects to be passed directly as arguments to functions. This is where Move’s **abilities system** comes into play. Abilities are compile-time attributes that define how an object can be used.

There are four key abilities:

* `key`: Allows the object to be used as a key in a storage.
* `store`: Allows the object to be stored in objects that have the key ability.
* `copy`: Allows the object to be copied.
* `drop`: Allows the object to be discarded or ignored at the end of a transaction.

In the case of our flash loan, the key advantage comes from *omitting* abilities. An object with no abilities cannot be stored, copied, or dropped. It becomes a “hot potato”: a temporary proof or receipt that **must** be consumed by another function within the same transaction. In Move, “consuming” an object means passing it to a function that takes ownership and destroys it, removing it from circulation. If it isn’t, the transaction is invalid and will not execute. While Move’s abilities system provides the safety mechanism for flash loans, Sui’s PTBs enable the composability that makes them practical.

### How PTBs work

In Ethereum, until [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) (account abstraction) becomes the norm, interactions with DeFi protocols require multiple, separate transactions (e.g., one for token approval and another for the swap). This creates friction and potential failure points.

Sui’s PTBs solv...