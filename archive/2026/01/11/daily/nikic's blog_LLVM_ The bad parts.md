---
title: LLVM: The bad parts
url: https://www.npopov.com/2026/01/11/LLVM-The-bad-parts.html
source: nikic's blog
date: 2026-01-11
fetch_date: 2026-01-12T03:37:32.277940
---

# LLVM: The bad parts

Blog by **nikic**.
Find me on [GitHub](https://github.com/nikic),
[StackOverflow](https://stackoverflow.com/users/385378/nikic),
[Twitter](http://twitter.com/nikita_ppv) and
[Mastodon](https://mastodon.social/%40nikic).
Learn more [about me](/aboutMe.html).

[« Back to article overview.](/)

# LLVM: The bad parts

11. January 2026

A few years ago, I wrote a blog post on [design issues in LLVM IR](https://www.npopov.com/2021/06/02/Design-issues-in-LLVM-IR.html). Since then, one of these issues has been fixed fully (opaque pointers migration), one has been mostly fixed (constant expression removal), and one is well on the way towards being fixed (ptradd migration).

This time I’m going to be more ambitious and not stop at three issues. Of course, not all of these issues are of equal importance, and how important they are depends on who you ask. In the interest of brevity, I will mostly just explain what the problem is, and not discuss what possible solutions would be.

Finally, I should probably point out that this is written from my perspective as the lead maintainer of the LLVM project: This is not a list of reasons to not use LLVM, it’s a list of opportunities to improve LLVM.

## High level issues

### Review capacity

Unlike many other open-source projects, LLVM certainly [does not suffer](https://insights.linuxfoundation.org/project/llvm-llvm-project) from a lack of contributors. There are *thousands* of contributors and the distribution is relatively flat (that is, it’s not the case that a small handful of people is responsible for the majority of contributions.)

What LLVM does suffer from is insufficient review capacity. There are a lot more people writing code than reviewing it. This is somewhat unsurprising, as code review requires more expertise than writing code, and may not provide immediate value[1](#fn:review_value) to the person reviewing (or their employer).

Lack of review capacity makes for a bad contributor experience, and can also result in bad changes making their way into the codebase. The way this usually works out is that someone puts up a PR, then fails to get a qualified review for a long period of time, and then one of their coworkers (who is not a qualified reviewer for that area) ends up rubberstamping the PR.

A related problem is that LLVM has a somewhat peculiar contribution model where it’s the responsibility of the PR author to request reviewers. This is especially problematic for new contributors, who don’t know whom to request. Often relevant reviewers will become aware of the PR thanks to a label-based notification system, but this is not apparent from the UI, and it’s easy for PRs to fall through the cracks.

A potential improvement here would be a Rust-style [PR assignment system](https://forge.rust-lang.org/triagebot/pr-assignment.html).

### Churn

Both the LLVM C++ API and LLVM IR are not stable and undergo frequent changes. This is simultaneously a great strength and weakness of LLVM. It’s a strength because LLVM does not stagnate and is willing to address past mistakes even at significant cost. It’s a weakness because churn imposes costs on users of LLVM.

Frontends are *somewhat* insulated from this because they can use the largely stable C API. However, it does not cover everything, and most major frontends will have additional bindings that use the unstable C++ API.

Users that integrate with LLVM more tightly (for example downstream backends) don’t have that option, and have to keep up with all API changes.

This is part of LLVM’s general development philosophy, which I’ll express somewhat pointedly as “upstream or GTFO”. LLVM is liberally licensed and does not require you to contribute changes upstream. However, if you do not upstream your code, then it will also not factor into upstream decision-making.

This point is somewhat unlike the rest, in that I’m not sure it’s possible to make things “strictly better” here. It’s possible that LLVM’s current point on the stability scale is not optimal, but moving it somewhere else would come with significant externalities. Making major changes in LLVM is already extremely hard due to the sheer scale of the project, without adding additional stability constraints on top.

### Build time

LLVM is a huge project. LLVM itself is >2.5 million lines of C++ and the entire monorepo is something like 9 million. C++ is not exactly known for fast build times, and compiling all that code takes time. This is bearable if you either have fast hardware or access to a build farm, but trying to build LLVM on a low-spec laptop is not going to be fun.

An additional complication is building with debug info (which I always recommend against), in which case you’ll add the extra gotchas of slow link times, high risk of OOM and massive disk usage. There are ways to avoid that (using shared libs or dylib build, using split dwarf, using lld), but it takes some expertise.

Promising changes in this area are the [use of pre-compiled headers](https://discourse.llvm.org/t/rfc-use-pre-compiled-headers-to-speed-up-llvm-build-by-1-5-2x/89345?u=nikic) (which significantly improves build time), and changing to use a [dylib build by default](https://discourse.llvm.org/t/rfc-llvm-link-llvm-dylib-should-default-to-on-on-posix-platforms/85908?u=nikic) (which reduces disk usage and link time, esp. for debuginfo builds). Another is to [reduce test performance](https://discourse.llvm.org/t/rfc-reducing-process-creation-overhead-in-llvm-regression-tests/88612?u=nikic) using daemonization (not strictly part of the “build time”, but relevant for the development cycle).

### CI stability

LLVM CI consists of over 200 post-commit buildbots that test LLVM in lots of different configurations on lots of different hardware. Commits that turn a buildbot from green to red result in an email to the commit author.

Unfortunately, this CI is never fully green, and flaky on top. This is in part due to flaky tests (typically in lldb or openmp), but can also be due to buildbot-specific issues. The end result is that it’s “normal” to get buildbot failure notifications for any given commit, even if it is perfectly harmless. This dilutes the signal, and makes it easier to miss the real failures.

The introduction of pre-merge testing on PRs did significantly improve the overall CI situation, but not the buildbot problem as such. I think we need to start taking flaky tests/buildbots more seriously before we can really make progress here.

Because someone is definitely going to mention how this [is not rocket science](https://graydon2.dreamwidth.org/1597.html), and we just need to start using bors / merge queues to guarantee an always-green build: It’s a problem of scale. There are >150 commits on a typical workday, which would be more than one commit every 10 minutes even if they were uniformly distributed. Many buildbots have multi-hour runs. This is hard to reconcile.[2](#fn:bors)

### End-to-end testing

In some respects, LLVM has very thorough test coverage. We’re quite pedantic about making sure that new optimizations have good coverage of both positive and negative tests. However, these tests are essentially unit tests for a single optimization pass or analysis.

We have only a small amount of coverage for the entire optimization pipeline (phase ordering tests), so optimizations sometimes regress due to pass interactions. Tests for the combination of the middle-end and backend pipelines are essentially nonexistent. There is likely room for improvement here, though it comes with tradeoffs.

However, what actually concerns me are end-to-end executable tests. LLVM’s test suite proper does not feature these at all. Executable tests are located in a separate [llvm-test-suite](https://github.com/llvm/llvm-test-suite) repo, which is typically not used during routine development, but run by buildbots. It contains a lot of different code ranging from benchmarks to unit tests.

However, llvm-test-suite has quite few tests ...