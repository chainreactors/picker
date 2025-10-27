---
title: Fuzzable - Framework For Automating Fuzzable Target Discovery With Static Analysis
url: https://buaq.net/go-145538.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:55:52.271317
---

# Fuzzable - Framework For Automating Fuzzable Target Discovery With Static Analysis

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

![](https://8aqnet.cdn.bcebos.com/37a69e456e27166bc9800317873769f8.jpg)

Fuzzable - Framework For Automating Fuzzable Target Discovery With Static Analysis

Framework for Automating Fuzzable Target Discovery with Static Analysis. Introduction Vu
*2023-1-14 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-145538.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg-AG5V_YW0RBzUL1zyrYr9VoTYs89wRcU-16gcn2Vwci03UyrdR7Pz_vokULyeqNF9aquJCi4J03wY6a21VYx0XeHZPtkw8L5F68NnFLOgiEm11LHJbCKp0hQXK5dXaqhRFjMMGFFlBxrOPSVcByaM5j-COMvm0B1SN1qzFT02ItA89FfnpEnv1dcGSQ=w640-h198)](https://blogger.googleusercontent.com/img/a/AVvXsEg-AG5V_YW0RBzUL1zyrYr9VoTYs89wRcU-16gcn2Vwci03UyrdR7Pz_vokULyeqNF9aquJCi4J03wY6a21VYx0XeHZPtkw8L5F68NnFLOgiEm11LHJbCKp0hQXK5dXaqhRFjMMGFFlBxrOPSVcByaM5j-COMvm0B1SN1qzFT02ItA89FfnpEnv1dcGSQ)

Framework for Automating *Fuzzable* Target Discovery with Static Analysis.

## Introduction

Vulnerability researchers conducting security assessments on software will often harness the capabilities of coverage-guided fuzzing through powerful tools like AFL++ and libFuzzer. This is important as it automates the [bughunting](https://www.kitploit.com/search/label/Bughunting "bughunting") process and reveals exploitable conditions in targets quickly. However, when encountering large and complex codebases or closed-source binaries, researchers have to painstakingly dedicate time to manually audit and [reverse engineer](https://www.kitploit.com/search/label/Reverse%20Engineer "reverse engineer") them to identify functions where fuzzing-based exploration can be useful.

**Fuzzable** is a framework that integrates both with C/C++ source code and binaries to assist [vulnerability](https://www.kitploit.com/search/label/Vulnerability "vulnerability") researchers in identifying function targets that are viable for fuzzing. This is done by applying several static analysis-based heuristics to pinpoint risky behaviors in the software and the functions that executes them. Researchers can then utilize the framework to generate basic harness templates, which can then be used to hunt for vulnerabilities, or to be integrated as part of a continuous fuzzing pipeline, such as Google's [oss-fuzz](https://github.com/google/oss-fuzz "oss-fuzz") project.

In addition to running as a standalone tool, Fuzzable is also integrated as a plugin for the [Binary Ninja](https://binary.ninja "Binary Ninja")  disassembler, with support for other disassembly backends being developed.

Check out the original blog post detailing the tool [here](https://codemuch.tech/2021/06/07/fuzzabble/ "here"), which highlights the technical specifications of the [static analysis](https://www.kitploit.com/search/label/Static%20Analysis "static analysis") heuristics and how this tool came about. This tool is also featured at [Black Hat Arsenal USA 2022](https://www.blackhat.com/us-22/arsenal/schedule/index.html#automating-fuzzable-target-discovery-with-static-analysis-26726 "Black Hat Arsenal USA 2022").

## Features

* Supports analyzing **binaries** (with [Angr](https://angr.io "Angr") and [Binary Ninja](https://binary.ninja "Binary Ninja")) and **source code** artifacts (with [tree-sitter](https://tree-sitter.github.io/tree-sitter/ "tree-sitter")).
* Run static analysis both as a **standalone CLI tool** or a **Binary Ninja plugin**.
* **Harness generation** to ramp up on creating fuzzing campaigns quickly.

## Installation

Some binary targets may require some sanitizing (ie. signature matching, or identifying functions from inlining), and therefore **fuzzable** primarily uses Binary Ninja as a disassembly backend because of it's ability to effectively solve these problems. Therefore, it can be utilized both as a standalone tool and plugin.

Since Binary Ninja isn't accessible to all and there may be a demand to utilize for security assessments and potentially scaling up in the cloud, an [angr](https://github.com/angr/angr "angr") *fallback* backend is also supported. I anticipate to incorporate other disassemblers down the road as well (priority: Ghidra).

### Command Line (Standalone)

If you have Binary Ninja Commercial, be sure to install the API for standalone headless usage:

```
$ python3 /Applications/Binary\ Ninja.app/Contents/Resources/scripts/install_api.py
```

Install with `pip`:

### Manual/Development Build

We use [poetry](https://python-poetry.org "poetry") for dependency management and building. To do a manual build, clone the repository with the third-party modules:

```
$ git clone --recursive https://github.com/ex0dus-0x/fuzzable
```

To install manually:

```
$ cd fuzzable/

# without poetry
$ pip install .

# with poetry
$ poetry install

# with poetry for a development virtualenv
$ poetry shell
```

You can now analyze binaries and/or source code with the tool!

```
# analyzing a single shared object library binary
$ fuzzable analyze examples/binaries/libbasic.so

# analyzing a single C source file
$ fuzzable analyze examples/source/libbasic.c

# analyzing a workspace with multiple C/C++ files and headers
$ fuzzable analyze examples/source/source_bundle/
```

### Binary Ninja Plugin

**fuzzable** can be easily installed through the Binary Ninja plugin marketplace by going to `Binary Ninja > Manage Plugins` and searching for it. Here is an example of the **fuzzable** plugin running, accuracy identifying targets for fuzzing and further vulnerability assessment:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgnDH0VyJjvXC_Bb4MuEQTvNf5c27YtMLBN-yab0FuIr4ycjZwkbqzIlIiVE0MiOfhcO5-pRPadMDlH9mjZZaSeve2-4nL9RXPVFtNlk4Vh71pnXP9mgirsNR2MG9f7U9Tx4zs5_8C2jS_zZwboniUkiJ5dH2xuSSBzv-cwFGnkQXoOBwwBWh-wRtcaUQ=w640-h258)](https://blogger.googleusercontent.com/img/a/AVvXsEgnDH0VyJjvXC_Bb4MuEQTvNf5c27YtMLBN-yab0FuIr4ycjZwkbqzIlIiVE0MiOfhcO5-pRPadMDlH9mjZZaSeve2-4nL9RXPVFtNlk4Vh71pnXP9mgirsNR2MG9f7U9Tx4zs5_8C2jS_zZwboniUkiJ5dH2xuSSBzv-cwFGnkQXoOBwwBWh-wRtcaUQ)

## Usage

**fuzzable** comes with various options to help better tune your analysis. More will be supported in future plans and any feature requests made.

### Static Analysis Heuristics

To determine fuzzability, **fuzzable** utilize several heuristics to determine which targets are the most viable to target for dynamic analysis. These heuristics are all weighted differently using the [scikit-criteria](https://scikit-criteria.quatrope.org/en/latest/tutorial/quickstart.html "scikit-criteria") library, which utilizes *multi-criteria decision analysis* to determine the best candidates. These metrics and are there weights can be seen here:

| Heuristic | Description | Weight |
| --- | --- | --- |
| Fuzz Friendly Name | Symbol name implies behavior that ingests file/buffer input | 0.3 |
| Risky Sinks | Arguments that flow into risky calls (ie memcpy) | 0.3 |
| Natural Loops | Number of loops detected with the dominance frontier | 0.05 |
| Cyclomatic Complexity | Complexity of function target based on edges + nodes | 0.05 |
| Coverage Depth | Number of callees the target traverses into | 0.3 |

> As mentioned, check out the [technical blog post](https://codemuch.tech/2021/06/07/fuzzabble/ "technical blog post") for a more in-depth look into why and how these metrics are utilized.

Many metrics were largely inspired by [Vincenzo Iozzo's original work in 0-knowledge fuzzing](https://resources.sei.cmu.edu/asset_files/WhitePaper/2010_019_001_53555.pdf "Vincenzo Iozzo's original work in 0-knowledge fuzzing").

Every targets you want to analyze is diverse, and **fuzzable** will not be able to account for every edge case behavior in the program target. Thus, it may be important during ...