---
title: Use mutation testing to find the bugs your tests don't catch
url: https://blog.trailofbits.com/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/
source: The Trail of Bits Blog
date: 2025-09-19
fetch_date: 2025-10-02T20:22:08.050695
---

# Use mutation testing to find the bugs your tests don't catch

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Use mutation testing to find the bugs your tests don't catch

Guillermo Larregay

September 18, 2025

[blockchain](/categories/blockchain/), [mutation-testing](/categories/mutation-testing/)

Page content

* [How tests improve security](#how-tests-improve-security)
* [How to measure test suite effectiveness](#how-to-measure-test-suite-effectiveness)
* [Mutation testing](#mutation-testing)
* [Automated mutation testing](#automated-mutation-testing)
* [Case study](#case-study)
* [Use mutation testing in your projects](#use-mutation-testing-in-your-projects)

Test coverage is a flawed metric; coverage metrics tell you whether code was executed during testing, not whether it was actually tested for correctness. Even test suites that achieve 100% code coverage can miss critical vulnerabilities. In blockchain, where bugs can lead to multimillion-dollar losses, the false sense of security given by “high test coverage” can be catastrophic. When millions or billions of dollars are at stake, “good enough” testing isn’t good enough.

Instead of simply measuring your coverage, you should actually *test your tests*. This is where mutation testing comes in, a technique that reveals the blind spots in your test suite by systematically introducing bugs and checking if your tests catch them. At Trail of Bits, we’ve been using mutation testing extensively in our audits, and it’s proven invaluable. In this post, we’ll show you how mutation testing uncovered a high-severity vulnerability in the Arkis protocol that was missed by traditional testing and would have allowed attackers to drain funds. More importantly, we’ll show you how to use this technique to find similar hidden vulnerabilities in your own code before attackers do.

## How tests improve security

Testing is a critical part of the blockchain development process: it can show whether individual functions and user flows are implemented correctly, verify the robustness of access controls, verify how contracts perform in adversarial situations, and prevent changes to contracts from causing regressions.

The following are three of the recommended testing methodologies available for blockchain projects:

* Unit testing: This is the most basic testing setup for a project, testing the smallest functional units of code. A unit testing suite includes test cases for individual functions’ behavior and checks for specific input values or values that can trigger edge cases. A functional and robust unit test suite makes code refactoring easier and serves as a solid foundation for integration testing.
* Integration testing: An integration testing suite includes test cases for interactions between functions and contracts and end-to-end testing of user interactions, administrative operations, and other kinds of operational flows. These cases perform similarly to how the contracts will behave once deployed and can help detect issues related to data validation, access controls, and contract interactions.
* Fuzz testing: These tests generate random sequences of interactions with contracts or functions, with randomized data in each call, and evaluate the resulting system state after the transactions are executed. The resulting state must comply with a certain set of invariant conditions defined in the test suite in order for the test to succeed. Fuzz testing is useful for individual functions or for end-to-end testing of operational flows; it can detect issues like domain and range errors in mathematical functions, faulty encoding and decoding of data, and incorrect data persistence.

## How to measure test suite effectiveness

If you’re developing a blockchain protocol in 2025, the minimum level of testing should involve all three methodologies. However, just because you’re using all three methodologies, that doesn’t mean you’re using them in an effective way that actually catches bugs.

The most common metric for a test suite’s effectiveness is known as “coverage.” Coverage measures how much of your code is “touched” by your test suite. Common sense indicates that, for a test suite to be any good, it should cover 100% of your code—that is, 100% of all lines/branches are touched by tests.

Usually, achieving 100% code coverage is difficult and resource-consuming. Most software engineering projects consider 80% coverage to be “good enough,” but considering the inherent risks and financial incentives in blockchain, it is definitely *not* good enough for contracts.

And even then, assuming your test suite covers all your code, can you rest assured that your system is safe? You probably already know the answer—it’s “no.” One of the biggest drawbacks of using coverage to assess your test suite is that 100% coverage doesn’t mean that all legitimate and malicious use cases are being tested.

Let’s play with a very simple toy example to show how coverage metrics can be deceiving. Below we have a `verifyMinimumDeposit()` function that returns `true` if the amount deposited is at least 1 ether, and `false` otherwise:

```
function verifyMinimumDeposit(uint256 deposit) public returns (bool) {
    if (deposit >= 1 ether) {
        return true;
    } else {
        return false;
    }
}
```

The developer created two unit tests for the function to test for `true` and `false` return values:

```
// A 2 ether deposit is ok
function test_DepositGreaterThanOneEther_ReturnsTrue() public {
    assertTrue(toyContract.verifyMinimumDeposit(2 ether));
}

// Minimum deposit is 1 ether, 100 gwei is not ok
function test_DepositLessThanOneEther_ReturnsFalse() public {
    assertFalse(toyContract.verifyMinimumDeposit(100 gwei));
}
```

Test coverage for the `verifyMinimumDeposit()` function is 100%, as all of its lines and branches are covered. The developer is happy with the metric and calls it a day. However, the tests are flawed: there are no test cases that check for edge case values. For example, if a code refactor mistakenly changes the condition to `deposit >= 2 ether`, the tests will still pass, but basic protocol functionality will be broken. The test suite failed to detect the incorrect value, and depending on other factors, the new code could even pose a security risk.

So you can see that coverage is not the best metric for assessing a test suite’s effectiveness. A better approach is to use mutation testing, a technique for finding test suite coverage gaps that are not related to actual line or branch coverage.

## Mutation testing

At a high level, a mutation testing campaign makes minor systematic changes to the codebase and runs the existing test suite against the modified code. Each modified version of the codebase is called a “mutant.”

After the test suite is run against a mutant, two results can happen: if the test suite fails, the mutant is “caught” or “killed,” meaning that there are checks in the test suite for that particular change. However, if the test suite finishes correctly, the mutant was not caught (it “survived”), revealing a coverage gap in the test suite.

The goal of a mutation testing campaign is to generate as many mutants as possible and validate that the test suite can catch all of them. A useful metric for assessing the test suite’s effectiveness is the percentage of caught mutants over all mutants generated. Ideally, this value should be 100%, meaning that the test suite could kill all generated mutants.

The following are some common mutations that can be performed on a codebase:

* Replace unary or binary operators; for example, replace an addition with a subtraction
* Replace assignment operators; for example, replace `+=` with `=`
* Replace constant literal values; for example, replace any nonzero constant with `0`
* Negate or replace conditions in `if` statements or loops
* Comment out whole lines of code
* Replace lines with the revert instruction
* Replace data types; for ex...