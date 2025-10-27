---
title: Manticore GUIs made easy
url: https://blog.trailofbits.com/2022/12/13/manticore-gui-plugin-binary-ninja-ghidra/
source: Trail of Bits Blog
date: 2022-12-14
fetch_date: 2025-10-04T01:23:20.324823
---

# Manticore GUIs made easy

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Manticore GUIs made easy

Wong Kok Rui, National University of Singapore

December 13, 2022

[binary-ninja](/categories/binary-ninja/), [manticore](/categories/manticore/), [internship-projects](/categories/internship-projects/)

Trail of Bits maintains Manticore, a symbolic execution engine that can analyze smart contracts and native binaries. While symbolic execution is a powerful technique that can augment the vulnerability discovery process, it requires some base domain knowledge and thus has its own learning curve. Given the plethora of ways in which a user can interact with such an engine and the need for frequent context switching between a disassembler and one’s terminal or script editor, integrating symbolic execution into one’s workflow can be daunting for a beginner.

One of the ways Trail of Bits has sought to ease this process is by making graphical user interfaces (GUIs) for Manticore that are embedded in popular interactive disassemblers. Last summer, former intern Alan Chang worked on the first such interface, [the Manticore User Interface (MUI) plugin for Binary Ninja](https://blog.trailofbits.com/2021/11/17/mui-visualizing-symbolic-execution-with-manticore-and-binary-ninja/). We found that pairing Manticore directly with an interactive disassembler provides vulnerability researchers with a more convenient way to actually use (and benefit from) symbolic execution. Therefore, during my winter and summer internships at Trail of Bits, my goal was to help grow the MUI ecosystem by making a MUI plugin for Ghidra and building infrastructure to make these plugins easier to use, maintain, and develop.

[![](/img/wpdump/613c53fc94634f3842c7136bf1ee1e07.png)](/img/wpdump/613c53fc94634f3842c7136bf1ee1e07.png)

The gRPC server–based architecture that MUI plugins use.

## The Ghidra Plugin

We figured that the most direct way to encourage more people to use MUI plugins would be to simply develop MUI plugins for a greater variety of disassemblers! Thus, I spent my winternship developing a Ghidra version of the MUI plugin; I chose Ghidra chiefly because it is popular and, unlike the commercial tool Binary Ninja, free and open source. Additionally, a few internal projects at Trail of Bits were already using Ghidra, so I would have ample opportunity to explore Ghidra plugin development. Finally, by developing a Ghidra plugin (one written in Java instead of Python), we could develop a solution that wouldn’t be tied to a single programming language, gaining insight that could guide the development of future plugins.

This initial Ghidra plugin mimicked the existing Binary Ninja plugin as closely as possible. While it took a bit of time to become familiar with Java Swing and Ghidra’s widgets, simply mimicking the existing visual components and user interface was a fairly trivial task once I got going.

[![](/img/wpdump/dbcb24986ffeccfb429d5e4d33ac46aa.png)](/img/wpdump/dbcb24986ffeccfb429d5e4d33ac46aa.png)

A side-by-side comparison of the run dialogs of Binary Ninja and Ghidra.

However, because the Ghidra plugin would be written in Java, it could not depend on the Manticore Python package or directly call Manticore’s Python API. Our solution to that challenge was to use a tool called [shiv](https://github.com/linkedin/shiv) to seamlessly bundle the Manticore library and all of its dependencies into a [Python zipapp](https://peps.python.org/pep-0441/). That way, we could create a “batteries-included” Manticore binary and then translate the Binary Ninja plugin’s interactions with the Manticore API into the appropriate command-line arguments. We then placed this binary in the relevant platform-specific subdirectories of Ghidra’s `os` directory, which facilitates cross-platform support.

By the end of the winternship, I was able to add extra features to the Ghidra plugin, such as the ability to specify arbitrary Manticore arguments in addition to those with dedicated input fields and support for multiple Manticore instances in the same Ghidra session. This, however, brought to light an additional problem.

## Feature parity and cross-disassembler development

It quickly became apparent that our approach to plugin development would not be sustainable if we aspired to expand the MUI project to support even more disassemblers. For each new MUI feature, we would first have to determine how to implement the feature, accounting for the way that the plugin interacts with Manticore (e.g., through direct calls to the Manticore API or through Manticore’s command-line interface options). Furthermore, certain front-end information shared across plugins (e.g., fixed description strings or sensible default options) would have to be repeated and standardized in each implementation.

To address this problem, over the summer I developed a centralized remote procedure call (RPC) server binary for MUI. This server handles all interactions with the full-featured Manticore Python API and handles MUI functionality through individual RPCs defined in a [protocol buffer](https://developers.google.com/protocol-buffers). We chose to use [gRPC](https://grpc.io/) as our RPC framework because of its performance, wide adoption, and strong support for code generation across many programming languages. As a result, MUI plugins of the future can easily contain and depend on their own gRPC-generated code.

The server is written in Python, providing it access to the full functionality of Manticore’s Python API, but is bundled into a shiv binary that can be called in any language. This facilitates a new client-server architecture that allows developers to implement any back-end Manticore functionality and tests just once. Developers of the front-end disassembler plugins can make RPC requests to the server with just a few lines of trivial code, which means that their work on individual plugins can focus almost entirely on front-end/UI changes.

To alleviate the “chore” of handling fixed strings and other front-end information that will be identical across plugins, we can store such data in JSON files that are packaged with MUI plugin releases and loaded on startup. In this way, we can standardize data such as the fields, field descriptors, and default values of the run dialogs used to start Manticore’s execution.

[![](/img/wpdump/8d70b0153b5f68c1463716b665b5b9f2.png)](/img/wpdump/8d70b0153b5f68c1463716b665b5b9f2.png)

Fixed data can be stored in plugin-agnostic JSON files.

## Demo: Developing a Feature for MUI

Let’s take a look at the process of developing a feature for MUI. Suppose that we want to enable manual state management during the runtime of a Manticore instance. Specifically, we want the ability to do the following:

* **Pause** a state and **resume** it at a later time, which will be useful if we implement capabilities like execution tracing in the future.
* **Kill** a state at our discretion. That way, if a state bypasses an `avoid` hook or becomes stuck in an infinite loop, we will be able to abandon it.First, we will define a new RPC and the RPC’s message formats in our protocol buffer file. The server will receive the state’s numeric ID, the Manticore instance that we’re working with, and a `StateAction` enum indicating whether it should resume, pause, or kill the state.

[![](/img/wpdump/4a0b58e0538753e4c54036b114c3acd7.png)](/img/wpdump/4a0b58e0538753e4c54036b114c3acd7.png)

Details of the new RPC and its message formats are defined in the protocol buffer.

We’ll also need to update an existing message—`ManticoreStateList`. MUI plugins have state lists that display all states and the status of each state; these lists are updated via a `GetStateList` RPC. Because it’d be beneficial for users to see “paused” states as distinct from preexisting state statuses, we’ll add a new `paused_states` field to the RPC’s response message, which will c...