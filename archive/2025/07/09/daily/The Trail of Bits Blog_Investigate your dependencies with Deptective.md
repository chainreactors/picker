---
title: Investigate your dependencies with Deptective
url: https://blog.trailofbits.com/2025/07/08/investigate-your-dependencies-with-deptective/
source: The Trail of Bits Blog
date: 2025-07-09
fetch_date: 2025-10-06T23:38:56.376656
---

# Investigate your dependencies with Deptective

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Investigate your dependencies with Deptective

Evan Sultanik, Andrew Pan

July 08, 2025

[tool-release](/categories/tool-release/), [research-practice](/categories/research-practice/), [supply-chain](/categories/supply-chain/)

Page content

* [Wait, isn’t there already a tool for that?](#wait-isnt-there-already-a-tool-for-that)
* [How does it work?](#how-does-it-work)
  + [Tracing](#tracing)
  + [Finding the right packages to install](#finding-the-right-packages-to-install)
  + [Installing potential dependencies](#installing-potential-dependencies)
* [Try it out](#try-it-out)

Have you ever tried compiling a piece of open-source software, only to discover that you neglected to install one of its native dependencies? Or maybe a binary “fell off the back of a truck” and you want to try running it but have no idea what shared libraries it needs. Or maybe you need to use a poorly packaged piece of software whose maintainers neglected to list a native dependency.

[Deptective](https://github.com/trailofbits/deptective), our new open-source tool, solves these problems. You can give it any program, script, or command, and it will find a set of packages sufficient to run the software successfully.

Here’s Deptective automatically finding all of [`jq`](https://jqlang.org)’s build-time dependencies:

## Wait, isn’t there already a tool for that?

There are many existing tools that automatically find software dependencies. For example, Trail of Bits created and maintains [it-depends](https://blog.trailofbits.com/2021/12/16/it-depends/), which uses package specifications to enumerate dependencies and their vulnerabilities. But that’s not the problem Deptective is intended to solve. Deptective detects dependencies *not* based upon the software’s self-reported requirements, but instead by *observing* what the software needs at runtime.

Deptective can work on any Linux process: native binaries, shell scripts, or even build systems. For example, simply run `deptective ./configure` or `deptective cmake ..` in an open-source repo, and it will automatically determine the native packages necessary to install to get the software to build!

Deptective is spiritually similar to [nix-autobahn](https://github.com/Lassulus/nix-autobahn), but Deptective is not tied to Nix and can also enumerate arbitrary runtime dependencies.

## How does it work?

There are more details below, but in short, Deptective **traces** the software to record files that the software tried to read but are missing from the environment; **finds a package** that provides the missing files; **installs** the package; then repeats the process for further missing packages, backtracking as necessary.

![Deptective’s dependency exploration and backtracking strategy](/img/deptective_figure_1.png)

Figure 1: Deptective’s dependency exploration and backtracking strategy

### Tracing

At their core, packages are groups of files; installing a package puts its constituent files onto your local system. Programs attempt to access their dependencies’ files, failing when they don’t exist. Deptective runs the target program while tracing its system calls using `strace`. Deptective analyzes the resulting system call trace to record all failed file accesses. If the program fails to execute (i.e., returns a nonzero exit code), Deptective proceeds to find the packages that contain the missing files.

### Finding the right packages to install

Once we know the missing files the program failed to load, how do we determine the packages that provide them? Luckily, most Linux distributions provide an index that maps files to their corresponding packages. Deptective searches the selected distribution’s index to find packages that contain the desired files. Once it selects a candidate package, it creates a new container snapshot, installs the package, and re-traces the target program in the environment with the package installed. We employ a simple heuristic to determine if the installed package was correct: if the trace is identical to the previous trace, the package is irrelevant and can be removed from consideration. If the presence of the new package produces a unique trace from the target program, the package is relevant. Deptective proceeds to install candidate packages until either there are no more to try or the software completes with exit code zero.

### Installing potential dependencies

Sometimes there are multiple packages in the index that can satisfy a dependency. In that case, Deptective tries every candidate until it finds one that produces a distinct program trace. It traces the program in a Docker container that matches the system’s distribution and version. Deptective installs each candidate in a separate container and deletes the ones that don’t pass our heuristic. Once Deptective determines that a package is relevant, it snapshots the Docker container, using it as a base for future installations. Using Docker provides a “clean” starting environment and does not pollute the host operating system’s packages. It also means that Deptective can run not only on Linux, but also macOS and Windows.

## Try it out

As with all of our open-source tools, you can find Deptective on our [GitHub](https://github.com/trailofbits/deptective). Follow the instructions written in the README to get it up and running.

Deptective is just one of many custom tools that Trail of Bits has developed to gain insight into software supply chains. Please [drop us a line](https://www.trailofbits.com/contact/) if this interests you or your organization!

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [Wait, isn’t there already a tool for that?](#wait-isnt-there-already-a-tool-for-that)
* [How does it work?](#how-does-it-work)
  + [Tracing](#tracing)
  + [Finding the right packages to install](#finding-the-right-packages-to-install)
  + [Installing potential dependencies](#installing-potential-dependencies)
* [Try it out](#try-it-out)

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.