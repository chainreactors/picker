---
title: Circomspect has more passes!
url: https://blog.trailofbits.com/2023/03/21/circomspect-static-analyzer-circom-more-passes/
source: Trail of Bits Blog
date: 2023-03-22
fetch_date: 2025-10-04T10:15:20.537187
---

# Circomspect has more passes!

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Circomspect has more passes!

Fredrik Dahlgren

March 21, 2023

[blockchain](/categories/blockchain/), [cryptography](/categories/cryptography/), [crytic](/categories/crytic/), [products](/categories/products/)

***TL;DR:*** We have released version 0.8.0 of [Circomspect](https://github.com/trailofbits/circomspect), our static analyzer and linter for [Circom](https://docs.circom.io/). Since our initial release of Circomspect in September 2022, we have added five new analysis passes, support for tags, tuples, and anonymous components, links to in-depth descriptions of each identified issue, and squashed a number of bugs. Please download the new version and tell us what you think!

## New analysis passes

The new analysis passes, added to the tool’s initial nine, check for a range of issues that could occur in Circom code:

1. Failure to properly constrain intermediate signals
2. Failure to constrain output signals in instantiated templates
3. Failure to constrain divisors in division operations to nonzero values
4. Use of BN254-specific templates from Circomlib with a different curve
5. Failure to properly constrain inputs to Circomlib’s `LessThan` circuit

Apart from finding the issue related to the Circomlib LessThan circuit discussed below, these analysis passes would also have caught the “[million dollar ZK bug](https://medium.com/veridise/circom-pairing-a-million-dollar-zk-bug-caught-early-c5624b278f25)” recently identified by Veridise in the [`circom-pairing`](https://github.com/yi-sun/circom-pairing) library.

To understand the types of issues that Circomspect can identify, let’s dig into the final example in this list. This analysis pass identifies an issue related to the `LessThan` circuit implemented by [Circomlib](https://github.com/iden3/circomlib), the de facto standard library for Circom. To fully understand the issue, we first need to take a step back and understand how signed values are represented by Circom.

## Signed arithmetic in GF(p)

Circom programs operate on variables called signals, which represent elements in the finite field `GF(p)` of integers modulo a prime number `p`. It is common to identify the elements in `GF(p)` with the unsigned integers in the half-open interval `[0, p)`. However, it is sometimes convenient to use field elements to represent signed quantities in the same way that we may use the elements in `[0, 232)` to represent signed 32-bit integers. Mirroring the definition for two’s complement used to represent signed integer values, we define `val(x)` as follows:

[![](/img/wpdump/7d5317c5832a360b71d16fb104f2017c.png)](/img/wpdump/7d5317c5832a360b71d16fb104f2017c.png)

We then say that *a is less than b* in `GF(p)` if `val(a) < val(b)` as signed integers. This means that `q = floor(p/2)` is the greatest signed value representable in `GF(p)`, and that `-q = q + 1` is the least signed value representable in `GF(p)`. It also means, perhaps somewhat surprisingly, that `q + 1` is actually less than `q`. This is also how the comparison operator `<` [is implemented by the Circom compiler](https://github.com/iden3/circom/blob/ca3345681549c859af1f3f42128e53e3e43fe5e2/circom_algebra/src/modular_arithmetic.rs#L154-L161).

As usual, we say that `a` *is positive* if `a > 0` and *negative* if `a < 0`. One way to ensure that a value a is nonnegative is to restrict the size (in bits) of the binary representation of `a`. In particular, if the size of a is strictly less than `log(p) - 1` bits, then `a` must be less than or equal to `q` and, therefore, nonnegative.

## Circomlib’s ‘LessThan’ template

With this out of the way, let’s turn our attention to the LessThan template defined by Circomlib. This template can be used to constrain two input signals `a` and `b` to ensure that `a < b`, and is implemented as follows:

[![](/img/wpdump/6aae737f794332c67c93f95a3bb88c2f.png)](/img/wpdump/6aae737f794332c67c93f95a3bb88c2f.png)

The LessThan template defined by [Circomlib](https://github.com/iden3/circomlib/blob/v2.0.5/circuits/comparators.circom)

Looking at the implementation, we see that it takes an input parameter n and two input signals `in[0]` and `in[1]`, and it defines a single output signal out. Additionally, the template uses the `Num2Bits` template from Circomlib to constrain the output signal out.

The `Num2Bits` template from Circomlib takes a single parameter `n` and can be used to convert a field element to its n-bit binary representation, which is given by the array out of size `n`. Since the size of the binary representation is bounded by the parameter n, the input to `Num2Bits` is also implicitly constrained to `n` bits. In the implementation of `LessThan` above, the expression `(1 << n) + in[0] - in[1]` is passed as input to `Num2Bits`, which constrains the absolute value `|in[0] - in[1]|` to `n` bits.

To understand the subtleties of the implementation of the `LessThan` template, let’s first consider the expected use case when both inputs to `LessThan` are at most `n` bits, where `n` is small enough to ensure that both inputs are nonnegative.

We have two cases to consider. If `in[0] < in[1]`, then `in[0] - in[1]` is a negative `n-`bit value, and `(1 << n) + in[0] - in[1]` is a positive n-bit value. It follows that bit `n` in the binary representation of the input to `Num2Bits` is `0`, and thus out must be equal to `1 - 0 = 1`.

On the other hand, if `in[0] ≥ in[1]`, then `in[0] - in[1]` is a nonnegative n-bit value (since both inputs are positive), and `(1 << n) + in[0] - in[1]` is a positive `(n + 1)`-bit value with the most significant bit equal to `1`, It follows that bit `n` in the binary representation of the input to `Num2Bits` is `1`, and out must be given by `1 - 1 = 0`.

This all makes sense and gives us some confidence if we want to use `LessThan` for range proofs in our own circuits. However, things become more complicated if we forget to constrain the size of the inputs passed to `LessThan`.

## Using signals to represent unsigned quantities

To describe the first type of issue that may affect circuits defined using `LessThan`, consider the case in which signals are used to represent unsigned values like monetary amounts. Say that we want to allow users to withdraw funds from our system without revealing sensitive information, like the total balance belonging to a single user or the amounts withdrawn by users. We could use `LessThan` to implement the part of the circuit that validates the withdrawn amount against the total balance as follows:

[![](/img/wpdump/200fc3102b4e4ce9c21a1d7ec2c9661d.png)](/img/wpdump/200fc3102b4e4ce9c21a1d7ec2c9661d.png)

The ValidateWithdrawal template should ensure that users cannot withdraw more than their total balance.

Now, suppose that a malicious user with a zero balance decides to withdraw `p - 1` tokens from the system, where `p` is the size of the underlying prime field. Clearly, this should not be allowed since `p - 1` is a ridiculously large number and, in any case, the user has no tokens available for withdrawal. However, looking at the implementation of `LessThan`, we see that in this case, the input to `Num2Bits` will be given by `(1 << 64) + (p - 1) - (0 + 1) = (1 << 64) - 2` (as all arithmetic is done modulo `p`). It follows that bit 64 of the binary representation of the input will be `0`, and the output from `LessThan` will be `1 - n2b.out[64] = 1 - 0 = 1`. This also means that `ValidateWithdrawal` will identify the withdrawal as valid.

The problem here is that `p - 1` also represents the signed quantity –`1` in `GF(p)`. Clearly, `-1` is less than `1`, and we have not constrained the withdrawn amount to be nonnegative. Adding a constraint restricting the size of the amount to be less than `log(p) - 1` bits would ensure that the amount must be positive, which would prevent this issue.

More generally, since the input ...