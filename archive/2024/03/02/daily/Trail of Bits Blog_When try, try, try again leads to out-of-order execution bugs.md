---
title: When try, try, try again leads to out-of-order execution bugs
url: https://blog.trailofbits.com/2024/03/01/when-try-try-try-again-leads-to-out-of-order-execution-bugs/
source: Trail of Bits Blog
date: 2024-03-02
fetch_date: 2025-10-04T12:10:36.977934
---

# When try, try, try again leads to out-of-order execution bugs

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# When try, try, try again leads to out-of-order execution bugs

Troy Sargent

March 01, 2024

[blockchain](/categories/blockchain/), [slither](/categories/slither/)

Have you ever wondered how a rollup and its base chain—the chain that the rollup commits state checkpoints to—communicate and interact? How can a user with funds only on the base chain interact with contracts on the rollup?

In Arbitrum Nitro, one way to call a method on a contract deployed on the rollup from the base chain is by using retryable transactions (a.k.a. [retryable tickets](https://docs.arbitrum.io/arbos/l1-to-l2-messaging)). While this feature enables these interactions, it does not come without its pitfalls. During our reviews of Arbitrum and contracts integrating with it, we identified footguns in the use of retryable tickets that are not widely known and should be considered when creating such transactions. In this post, we’ll share how using retryable tickets may allow unexpected race conditions and result in out-of-order execution bugs. What’s more, we’ve created a new [Slither detector](https://github.com/crytic/slither/releases/tag/0.10.1) for this issue. Now you’ll be able to not only recognize these footguns in your code, but test for them too.

## Retryable tickets

In Arbitrum Nitro, retryable tickets facilitate communication between the Ethereum mainnet, or Layer 1 (L1), and the Arbitrum Nitro rollup, or Layer 2 (L2). To create retryable tickets, users can call `createRetryableTicket` on the L1 `Inbox` contract of the Arbitrum rollup, as shown in the code snippet below. When retryable tickets are created and queued, ArbOS will attempt to automatically “redeem” them by executing them one after another on L2.

```
/**
 * @notice Put a message in the L2 inbox that can be reexecuted for some fixed amount of time if it reverts
 * @dev all msg.value will deposited to callValueRefundAddress on L2
 * @dev Gas limit and maxFeePerGas should not be set to 1 as that is used to trigger the RetryableData error
 * @param to destination L2 contract address
 * @param l2CallValue call value for retryable L2 message
 * @param maxSubmissionCost Max gas deducted from user's L2 balance to cover base submission fee
 * @param excessFeeRefundAddress gasLimit x maxFeePerGas - execution cost gets credited here on L2 balance
 * @param callValueRefundAddress l2Callvalue gets credited here on L2 if retryable txn times out or gets cancelled
 * @param gasLimit Max gas deducted from user's L2 balance to cover L2 execution. Should not be set to 1 (magic value used to trigger the RetryableData error)
 * @param maxFeePerGas price bid for L2 execution. Should not be set to 1 (magic value used to trigger the RetryableData error)
 * @param data ABI encoded data of L2 message
 * @return unique message number of the retryable transaction
 */
function createRetryableTicket(
    address to,
    uint256 l2CallValue,
    uint256 maxSubmissionCost,
    address excessFeeRefundAddress,
    address callValueRefundAddress,
    uint256 gasLimit,
    uint256 maxFeePerGas,
    bytes calldata data
) external payable returns (uint256);
```

The createRetryableTicket function interface

Assuming the gas costs are covered by the sender and no failures occur, the transactions will be executed sequentially, and the final state results from applying transaction B immediately following transaction A.

![](/img/wpdump/5d973004c0cf625cf3cb521d7373e7e8.png)

Figure 1: The happy path is when the transactions are all executed in order.

## Wait, what does “retryable” mean?

Because any transaction may fail (e.g., the L2 gas price rises significantly following the creation of a transaction, and the user has insufficient gas to cover the new cost), Arbitrum created these types of transactions so that users can “retry” them by supplying additional gas. Failing retryable tickets will be persisted in memory and may be re-executed by *any user* who manually calls the `redeem` method of the `[ArbRetryableTx](https://docs.arbitrum.io/for-devs/dev-tools-and-resources/precompiles#arbretryabletx)` precompiled contract, sponsoring the gas costs. A retryable ticket that fails is different from a normal transaction that reverts, in that it does not require a new transaction to be signed to be executed again.

Additionally, retryable tickets in memory can be redeemed up to one week after they are created. A retryable ticket’s lifetime can be extended for another week by paying an additional fee for storing it; otherwise, it will be discarded after its expiration date.

## Where things go wrong

While these types of transactions are useful—in that they facilitate L2-to-L1 communication and allow users to retry their transactions if failures occur—they come with pitfalls, risks that users and developers may not be aware of. Specifically, retryable tickets are expected to execute in the order they are submitted, but this is not always guaranteed to happen.

In scenario 1, both transactions A and B fail and enter the memory region. The state of the application is left unchanged.

Consider the three scenarios below in which two retryable tickets are created within the same transaction.

![](/img/wpdump/466398e4008762993f4d402291439e30.png)

Figure 2: Two retryable tickets are created in the same transaction, but both fail and enter the memory region.

However, anyone can manually redeem transaction B before transaction A, which means that the transactions will be executed out of order unexpectedly.

![](/img/wpdump/3042857e85e242fcd9bf261af68f9179.png)

Figure 3: Anyone can manually redeem transactions in the memory region out of order.

In scenario 2, transaction A fails and enters the memory region, but transaction B succeeds. Once again, the transactions are executed out of order (i.e., transaction A is not executed at all), and the final state is not what was expected.

![](/img/wpdump/aafbd9fed19d775391332e9493e8a4f7.png)

Figure 4: Only transaction B is included in the final state.

In scenario 3, transaction A succeeds, but transaction B does not. That means transaction B must be re-executed manually. Transactions can be created more than once, which means that a second set of transactions A and B could be submitted before the first transaction B is re-executed. If developers of a protocol using the Arbitrum rollup system don’t account for the possibility that the protocol could receive a second transaction A prior to transaction B’s success, the protocol may not handle this case correctly.

![](/img/wpdump/838f3d52df5189a6c6f03d532065b6b3.png)

Figure 5: Only transaction A is included in the final state.

## The out-of-order execution vulnerability

In light of these scenarios, developers should consider that transactions may execute out of order. For instance, if the second transaction in a queue relies on completion of the first, but it executes before the first executes due to an insufficient gas failure, it may revert or not work correctly. It’s important that the callee, or message recipient, on the rollup can robustly handle situations such as the receipt of transactions in a different order than they were created and smaller subsets of transactions due to failures. If a protocol does not anticipate cases of reorderings and failures of retryable tickets, the protocol could break or be hacked.

Let’s consider the following L2 contract, which users can call to claim rewards based on some staked tokens. When they decide to unstake their tokens, any rewards that they haven’t yet claimed are lost:

```
function claim_rewards(address user) public onlyFromL1 {
    // rewards is computed based on balance and staking period
    uint unclaimed_rewards = _compute_and_update_rewards(user);
    token.safeTransfer(user, unclaimed_rewards);
}

// Call claim_rewards before unstaking, otherwise you lose your rewards...