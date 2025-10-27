---
title: Fuzztruction - Prototype Of A Fuzzer That Does Not Directly Mutate Inputs (As Most Fuzzers Do) But Instead Uses A So-Called Generator Application To Produce An Input For Our Fuzzing Target
url: https://buaq.net/go-162052.html
source: unSafe.sh - 不安全
date: 2023-05-07
fetch_date: 2025-10-04T11:37:46.726719
---

# Fuzztruction - Prototype Of A Fuzzer That Does Not Directly Mutate Inputs (As Most Fuzzers Do) But Instead Uses A So-Called Generator Application To Produce An Input For Our Fuzzing Target

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

![](https://8aqnet.cdn.bcebos.com/ca31c763f25a10ba9fd7d33e1f0e3699.jpg)

Fuzztruction - Prototype Of A Fuzzer That Does Not Directly Mutate Inputs (As Most Fuzzers Do) But Instead Uses A So-Called Generator Application To Produce An Input For Our Fuzzing Target

Fuzztruction is an academic prototype of a fuzzer that does not directly mutate inputs (as m
*2023-5-6 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-162052.htm)
阅读量:39
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiAXVhE8X5YwwJvuQbSTRrAv7KxPNPI2EfOMHwh5JWkafSVxfY2A51v2wyWTuwi8D0rM4jd5Cz7vFkcw3MhUOF8QGWMmkCQDx4NOmKXXjI8xyyDKITzoIIINxuBBKxg81756EXBfGz0DuPHarmTLkXLRpmWU2j4VCQ8f0ZKzSV2mFjhl1tqZnJaRNGXMw=w502-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEiAXVhE8X5YwwJvuQbSTRrAv7KxPNPI2EfOMHwh5JWkafSVxfY2A51v2wyWTuwi8D0rM4jd5Cz7vFkcw3MhUOF8QGWMmkCQDx4NOmKXXjI8xyyDKITzoIIINxuBBKxg81756EXBfGz0DuPHarmTLkXLRpmWU2j4VCQ8f0ZKzSV2mFjhl1tqZnJaRNGXMw)

Fuzztruction is an academic prototype of a fuzzer that does not directly mutate inputs (as most fuzzers do) but instead uses a so-called generator application to produce an input for our fuzzing target. As programs generating data usually produce the correct representation, our fuzzer *mutates* the generator program (by injecting faults), such that the data produced is *almost* valid. Optimally, the produced data passes the parsing stages in our fuzzing target, called *consumer*, but triggers unexpected behavior in deeper program logic. This allows to even fuzz targets that utilize [cryptography](https://www.kitploit.com/search/label/Cryptography "cryptography") primitives such as [encryption](https://www.kitploit.com/search/label/Encryption "encryption") or message integrity codes. The main advantage of our approach is that it generates complex data without requiring heavyweight program analysis techniques, grammar approximations, or human intervention.

For instructions on how to reproduce the experiments from the paper, please read the [`fuzztruction-experiments`](https://github.com/fuzztruction/fuzztruction-experiments "$ (5)") submodule documentation *after* reading this document.

> **Compatibility:** While we try to make sure that our prototype is as [platform independent](https://www.kitploit.com/search/label/Platform%20Independent "platform independent") as possible, we are not able to test it on all platforms. Thus, if you run into issues, please use Ubuntu 22.04.1, which was used during development as the host system.

## Quickstart

```
# Clone the repository
```

## Components

Fuzztruction contains the following core components:

### ****Scheduler****

The scheduler orchestrates the interaction of the generator and the consumer. It governs the fuzzing campaign, and its main task is to organize the fuzzing loop. In addition, it also maintains a queue containing queue entries. Each entry consists of the seed input passed to the generator (if any) and all mutations applied to the generator. Each such queue entry represents a single test case. In traditional fuzzing, such a test case would be represented as a single file. The implementation of the scheduler is located in the [`scheduler`](https://github.com/fuzztruction/fuzztruction/blob/main/scheduler "$ (7)") directory.

### ****Generator****

The generator can be considered a seed generator for producing inputs tailored to the fuzzing target, the consumer. While common fuzzing approaches mutate inputs on the fly through bit-level mutations, we mutate inputs indirectly by injecting faults into the generator program. More precisely, we identify and mutate data operations the generator uses to produce its output. To facilitate our approach, we require a program that generates outputs that match the input format the fuzzing target expects.

The implementation of the generator can be found in the [`generator`](https://github.com/fuzztruction/fuzztruction/blob/main/generator "$ (8)") directory. It consists of two components that are explained in the following.

#### ****Compiler Pass****

The compiler pass ([`generator/pass`](https://github.com/fuzztruction/fuzztruction/blob/main/generator/pass "$ (9)")) instruments the target using so-called [patch points](https://llvm.org/docs/StackMaps.html "patch points"). Since the current (tested on LLVM12 and below) implementation of this feature is unstable, we patch LLVM to enable them for our approach. The patches can be found in the [`llvm`](https://github.com/fuzztruction/fuzztruction-llvm "$ (11)") repository (included here as submodule). Please note that the patches are experimental and not intended for use in production.

The locations of the patch points are recorded in a separate section inside the compiled binary. The code related to parsing this section can be found at [`lib/llvm-stackmap-rs`](https://github.com/fuzztruction/llvm-stackmap-rs "$ (12)"), which we also published on [crates.io](https://crates.io/crates/llvm_stackmap "crates.io").

During fuzzing, the scheduler chooses a target from the set of patch points and passes its decision down to the agent (described below) responsible for applying the desired mutation for the given patch point.

#### **Agent**

The agent, implemented in [`generator/agent`](https://github.com/fuzztruction/fuzztruction/blob/main/generator/agent "$ (14)") is running in the context of the generator application that was compiled with the custom compiler pass. Its main tasks are the implementation of a forkserver and communicating with the scheduler. Based on the instruction passed from the scheduler via shared memory and a message queue, the agent uses a JIT engine to mutate the generator.

### ****Consumer****

The generator's counterpart is the consumer: It is the target we are fuzzing that consumes the inputs generated by the generator. For Fuzztruction, it is sufficient to compile the consumer application with AFL++'s compiler pass, which we use to record the coverage feedback. This feedback guides our mutations of the generator.

Before using Fuzztruction, the runtime environment that comes as a Docker image is required. This image can be obtained by building it yourself locally or pulling a pre-built version. Both ways are described in the following. Before preparing the runtime environment, this repository, and all sub repositories, must be cloned:

```
git clone --recurse-submodules https://github.com/fuzztruction/fuzztruction.git
```

### ****Local Build****

The Fuzztruction runtime environment can be built by executing [`env/build.sh`](https://github.com/fuzztruction/fuzztruction/blob/main/env/build.sh "$ (15)"). This builds a Docker image containing a complete runtime environment for Fuzztruction locally. By default, a [pre-built version](https://hub.docker.com/repository/docker/nbars/fuzztruction-llvm_debug "pre-built version") of our patched LLVM version is used and pulled from Docker Hub. If you want to use a locally built LLVM version, check the [`llvm`](https://github.com/fuzztruction/fuzztruction-llvm "$ (17)") directory.

### ****Pre-built****

In most cases, there is no particular reason for using the pre-built environment -- except if you want to reproduce the exact experiments conducted in the paper. The pre-built image provides everything, including the pre-built evaluation targets and all dependencies. The image can be retrieved by executing [`env/pull-prebuilt.sh`](https://github.com/fuzztruction/fuzztruction/blob/main/env/pull-prebuilt.sh "$ (18)").

The following section documents how to spawn a runtime environment based on either a locally built image or the prebuilt one. Details regarding the reproduction of the ...