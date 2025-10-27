---
title: Looking for Missed Alarm Bugs in a Formal Verification Tool
url: https://blog.regehr.org/archives/2124
source: Embedded in Academia
date: 2024-09-05
fetch_date: 2025-10-06T18:26:30.765797
---

# Looking for Missed Alarm Bugs in a Formal Verification Tool

# [Embedded in Academia](https://blog.regehr.org)

# Looking for Missed Alarm Bugs in a Formal Verification Tool

---

[This piece is co-authored with Vsevolod Livinskii.]

Formal verification isn’t some sort of magic pixie dust that we sprinkle over a computer system to make it better. Real formal verification involves a lot of the same kind of difficult, nasty, grungy engineering work that any other systems-level job involves. Furthermore, the verification tools themselves are very difficult to get right. They are subject to many kinds of defects, and they are if anything more difficult to debug than other software. They need to be rigorously tested if we’re going to trust them.

[Alive2 is a translation validation tool](https://users.cs.utah.edu/~regehr/alive2-pldi21.pdf): given two versions of a function in LLVM IR–usually these correspond to some code before and after an optimization has been performed on it–Alive2 tries to either prove that the optimization was correct, or prove that it was incorrect. Alive2 is used in practice by compiler engineers: [more than 600 LLVM issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue+alive2.llvm.org) link to our [online Alive2 instance](https://alive2.llvm.org/ce/).

Ignoring crashes and such, we can broadly categorize defects in Alive2 as:

* a false alarm: Alive2 signals an error when none was present
* a missed alarm: Alive2 fails to signal an error when one was present

The first kind of error, false alarms, are not too difficult to test for: we simply ask Alive2 to verify a large number of optimizations, and we look closely at the errors that it signals. Every such error is the result of either a bug in LLVM or in Alive2. The second kind of error, the ones in the bottom left quadrant, are much more difficult to test for:

![](https://blog.regehr.org/wp-content/uploads/2021/10/Screen-Shot-2021-10-20-at-12.16.35-PM-1280x817.png)

The thing we’re missing is test cases that might trigger a missed-alarm bug: each such test requires a pair of functions in LLVM IR that have the same signatures, but which provably behave differently for at least one choice of inputs. We can’t rely on compiler bugs to create these test cases because LLVM is not a very buggy compiler! The vast majority of optimizations it performs are correct.

To find missed-alarm bugs, we tried two different ideas. In the rest of this piece we’ll describe both of them.

First, we started with [YARPGen](https://github.com/intel/yarpgen), a random program generator that has been used to find a large number of compiler bugs. The key guarantee that YARPGen provides is that the C or C++ function it generates is free of undefined behavior. Without this guarantee, we can’t really do randomized differential testing, since different compilers will tend to exploit undefined behaviors differently. However, this guarantee isn’t a sufficient basis for finding missed alarm bugs, so we modified YARPGen to suit our purposes. Our modified version generates a random function, as usual, and then it does something new: it randomly mutates this function slightly, while maintaining the guarantee that the new function is also free of undefined behavior.

Now we have two functions, very similar to each other, both guaranteed to be free of undefined behavior. Is this a basis for finding missed alarm bugs? Not quite–we still need to make sure that these functions produce different results when executed, for at least one set of inputs. To do this, we simply compile and run the pairs of functions, throwing away any pairs where our mutation happens to not change the observable behavior. Finally, we compile the pair of functions into LLVM IR and then ask Alive2 to see if one of them refines the other. By construction, this check must fail–if Alive2 does not signal an error, then we have found the kind of missed alarm bug in Alive2 that we were originally looking for.

The other method that we have for seeking out missed alarm bugs is one that we arrived at by accident. We realized that Zhengyang Liu’s LLVM superoptimizer, Minotaur, is basically passively looking for missed alarm bug every time that we use it. Here’s the [Minotaur](https://github.com/minotaur-toolkit/minotaur) source code and here’s [a paper about it](https://users.cs.utah.edu/~regehr/minotaur.pdf).

For every LLVM instruction in the program being optimized, Minotaur tries to find a cheaper way to compute it. It does this by extracting that instruction, and some of its backwards data, control, and memory dependencies into a new LLVM function that returns the value computed by the target instruction. This new function serves as the *specification* for a program synthesis problem, where the goal is to find a cheaper way to compute the specification. Minotaur uses Alive2 to ensure that the new function refines the old one, and it uses [llvm-mca](https://llvm.org/docs/CommandGuide/llvm-mca.html) to ensure that the new function is cheaper to compute than the old one.

Synthesis works by enumerating a large number of *partially symbolic* candidates, where instructions are represented concretely, but literal constants are represented symbolically. Zhengyang modified Alive2 in such a way that when a candidate contains at least one symbolic constant, it emits an exists-forall solver query, which asks the solver: “Do there exist values for the symbolic constants in the candidate, such that the candidate refines the specification?”

The details of Minotaur’s synthesis procedure don’t matter too much; the important point is that since there are a huge number of candidates, the vast majority of which do not refine the specification, we end up giving Alive2 many opportunities to miss an alarm.

But, if Alive2 misses an alarm when it is invoked by Minotaur, how will we know? Well, keep in mind that missing an alarm means that Alive2 claimed that a candidate refined the specification when in fact no refinement relation exists. Since refinement is the correctness criterion for an optimizer, these failures, by definition, lead to miscompilations. Since we routinely use Minotaur to compile large open source programs and then we run their test suites, we should have a decent chance of finding any miscompilations that it introduces.

We’ve looked at two different ways, one using randomized search and the other using a small-scale exhaustive search, to look for missed alarm bugs in Alive2. What have we found so far? Not much! It does not look like Alive2 and Z3 are in the habit of missing alarms. This means that it is fulfilling its top-level design goal, which is good, since people actually rely on Alive2 in practice.

So is this the end of the story? Are we now certain that Alive2 doesn’t miss alarms? Alas, no, we’re not sure. My suspicion is that if we really wanted to find missed alarm bugs, we would look at Alive2’s support for function attributes and similar constructs that neither YARPGen nor Minotaur stress in interesting ways.

September 4, 2024

regehr

[Uncategorized](https://blog.regehr.org/archives/category/uncategorized)

---

### One response to “Looking for Missed Alarm Bugs in a Formal Verification Tool”

1. **BCS** says:

   [September 11, 2024 at 9:44 am](https://blog.regehr.org/archives/2124#comment-20751)

   Has much work been done on characterizing how much of the full state space things like YARPGen and collections of “large open source programs” actually explore?

   —

   I don’t even know how I would characterize the full extent of the state space, but at a guess most any single approach would miss close to “almost all” (in the math sense) of it.

   that said, as long as the parts that are actually used in practice get covered, it might be a better ROI to use resource to tackle a new approach rather than expand the coverage for existing one.

[Embedded in Academia](https://blog.regehr.org)

Proudly powered by [WordPress](https://wordpress.org)