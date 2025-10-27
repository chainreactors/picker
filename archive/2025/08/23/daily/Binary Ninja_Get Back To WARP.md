---
title: Get Back To WARP
url: https://binary.ninja/2025/08/22/warp.html
source: Binary Ninja
date: 2025-08-23
fetch_date: 2025-10-07T00:48:04.241268
---

# Get Back To WARP

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Get Back To WARP

* [Mason Reed](https://github.com/emesare)
* 2025-08-22
* [reversing](/tag/reversing), [warp](/tag/warp), [plugin](/tag/plugin)

Since [Binary Ninja 4.2](https://binary.ninja/2024/11/20/4.2-frogstar.html#warp-advanced-function-matching-algorithm-alpha), users have been able to enable WARP, and now with [Binary Ninja 5.1](https://binary.ninja/2025/07/24/5.1-helion.html) we are finally enabling it by default! WARP has received many features users have been asking for, and a healthy amount of polish on top of that as well. In this blog weâll describe what WARP is, hot it works, and how you can use it to improve your reverse engineering experience.

## WARP Is This?

WARP (and similarly [SigKit](https://binary.ninja/2020/03/11/signature-libraries.html)) was designed to identify known functions in unknown binaries, increasing the ability to reason about what a binary does (or doesnât) do. An addition goal of WARP is to provide the groundwork for function similarity lookups (fuzzy matching) and a format that can be used to transfer analysis information passively.

Because of the statically linked nature of many modern binaries (especially Rust and Go) we often end up with quantities of library code far exceeding that of âuserâ code. It is the job of WARP to provide the facilities for you as a user to create signatures of these common functions to match and apply information automatically.

WARP works by first creating a GUID for each unique basic block in a given function, from which a âFunction GUIDâ is derived. This GUID is then used to look up possible matching functions. The GUID itself is stable and should be identical for the same function in any given binary. This poses some challenges given that a function might be referencing data or code at a different address. To address this we zero out âvariantâ instructions before generating the basic block GUID. A more detailed description is available over on the [WARP GitHub repository](https://github.com/Vector35/warp?tab=readme-ov-file#creating-a-function-guid).

WARP works directly on the raw bytes of the file, and we use our [BNIL representations](https://docs.binary.ninja/dev/bnil-overview.html) to identify the instructions to mask off. This means that all architectures that are supported by Binary Ninja will work, including custom ones. Additionally, where other reverse engineering tools have similar capabilities, they can also generate compatible GUIDs, allowing cross-tool information sharing!

### What Can I Expect?

When you open a new binary in 5.1, after function analysis finishes, we will then take all functions and their respective GUID and attempt to automatically match against relevant WARP data, applying matched information. As part of applying information we will tag the function. This makes it easy for you as a user to know when WARP information has been applied.

![Unmatched](/blog/images/warp/unmatched-small.png)
![Matched](/blog/images/warp/matched-small.png)

After the function is matched, the following information will be transferred (if available):

* function symbol
* function type
* calling convention
* comments and variables

![Unmatched](/blog/images/warp/unmatched-big.png)
![Matched](/blog/images/warp/matched-big.png)

## Stats for Nerds

For those who like numbers (I do not) we compared a few different binaries and use cases from both the previous development version of WARP and the 5.1 release. This way we can prove weâve made improvements withâ¦ science?

For each binary we simply open it up in Binary Ninja (either 5.0 or 5.1) and observe the number of tagged WARP functions. The below chart details a few binaries, while the information is self-evident, the data we are matching on is not, so I will detail that below:

* Binary A-D: The binaries are matching against our bundled MSVC signatures.
* Binary E: This binary is testing our ability to transfer functions from a separate version of the same application, specifically version A to version E.
* Binary F: This binary is testing our ability to match on RISC like architectures, this showcases improvements to our variant instruction detection, as we are generating signatures from one binary with symbols and applying them to another binary of the same microcontroller.

![Statistics](/blog/images/warp/stats.svg)

The keen-eyed among you will notice a small dip in matched functions for `Binary B`. This brings up an important point about accuracy: the reason we are matching fewer functions in that binary is because our dataset of functions was increased, causing some collisions on functions which previously had none. While the local result might seem worse, this is a good thing!

The functions were all named âConcurrency::*X*â. If youâve reversed windows binaries, you likely already know that these are bogus names that often show up in some function matchers. Itâs common when analyzing C++ binaries to see your tool mark up some small constructors with the aforementioned names. This can easily cause confusion and provide no value during reverse engineering.

The premise of WARP is that we do not need to hand hold the creation of signatures or prematurely prune problematic signatures, which is a big problem with SigKit and other similar tools. For example, previously with SigKit, Binary Ninja would consistently annotate `operator new()` in place of `operator delete()` (see the below images), and this was happening automatically with little feedback to the user that the source was SigKit.

![Incorrect Function](/blog/images/warp/bad-match-0.png)

![Incorrect Function Proof](/blog/images/warp/bad-match-1.png)

Knowing this, we consider the dip in matched functions for `Binary B` to be an improvement. As we add more data to the bundled signatures, incorrect matches on signatures will continue to go down.

## New UI and API

One of the major improvements of this release was the addition of an interactive UI, giving you control over what information is applied and access to additional information such as the list of possible functions for any given function.

![New UI](/blog/images/warp/ui.png)

![New UI Animated](/blog/images/warp/ui-anim.gif)

This new UI is [written in C++](https://github.com/Vector35/binaryninja-api/tree/dev/plugins/warp/ui) as a separate bundled plugin which of course means we had to add an API to WARP. With 5.1 you can now write scripts to create, query and apply function information. For anyone wanting to know more, we include a section detailing the API and an example python script [in the user documentation](https://dev-docs.binary.ninja/guide/warp.html#api).

## Improved Signature Creation

While the process for consuming WARP information has been streamlined with the UI, we still needed to improve the workflow for producing the WARP information. While processing headlessly is still supported with the API, headless is not required. Previously, SigKit required the headless API for creating signatures of library files.

To start with, we overhauled the processing of individual files. From the UI you can now process [static libraries](https://en.wikipedia.org/wiki/Static_libr...