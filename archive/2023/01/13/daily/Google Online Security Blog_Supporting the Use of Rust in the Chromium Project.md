---
title: Supporting the Use of Rust in the Chromium Project
url: http://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html
source: Google Online Security Blog
date: 2023-01-13
fetch_date: 2025-10-04T03:44:16.993894
---

# Supporting the Use of Rust in the Chromium Project

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Supporting the Use of Rust in the Chromium Project](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html "Supporting the Use of Rust in the Chromium Project")

January 12, 2023

Posted by Dana Jansens (she/her), Chrome Security Team

We are pleased to announce that moving forward, the Chromium project is going to support the use of third-party Rust libraries from C++ in Chromium. To do so, we are now actively pursuing adding a [production Rust toolchain](https://bugs.chromium.org/p/chromium/issues/detail?id=1292038) to our build system. This will enable us to include Rust code in the Chrome binary within the next year. We’re starting slow and setting clear expectations on [what libraries we will consider](https://chromium.googlesource.com/chromium/src/%2B/main/docs/adding_to_third_party.md#Rust) once we’re ready.

In this blog post, we will discuss how we arrived at the decision to support third-party Rust libraries at this time, and not broader usage of Rust in Chromium.

**Why We Chose to Bring Rust into Chromium**

Our goal in bringing Rust into Chromium is to **provide a simpler** (no IPC) and **safer** (less complex C++ overall, no memory safety bugs in a sandbox either) **way to satisfy [the rule of two](https://chromium.googlesource.com/chromium/src/%2B/master/docs/security/rule-of-2.md), in order to speed up development** (less code to write, less design docs, less security review) **and improve the security** (increasing the number of lines of code without memory safety bugs, decreasing the bug density of code) **of Chrome**. And we believe that we can use third-party Rust libraries to work toward this goal.

Rust was developed by Mozilla specifically for use in writing a browser, so it’s very fitting that Chromium would finally begin to rely on this technology too. Thank you Mozilla for your huge contribution to the systems software industry. Rust has been an incredible proof that we should be able to expect a language to provide safety while also being performant.

We know that C++ and Rust can play together nicely, through tools like [cxx](https://github.com/dtolnay/cxx), [autocxx](https://github.com/google/autocxx) [bindgen](https://rust-lang.github.io/rust-bindgen/), [cbindgen](https://github.com/eqrion/cbindgen), [diplomat](https://github.com/rust-diplomat/diplomat), and (experimental) [crubit](https://github.com/google/crubit). However there are also limitations. We can expect that the shape of these limitations will change in time through new or improved tools, but the decisions and descriptions here are based on the current state of technology.

**How Chromium Will Support the Use of Rust**

The Chrome Security team has been investing time into researching how we should approach using Rust alongside our C++ code. Understanding the implications of incrementally moving to writing Rust instead of C++, even in the middle of our software stack. What [the limits](https://bugs.chromium.org/p/chromium/issues/detail?id=1296314) of safe, simple, and reliable interop might be.

Based on our research, we landed on two outcomes for Chromium.

1. We will support interop in only a single direction, from C++ to Rust, for now. Chromium is written in C++, and the majority of stack frames are in C++ code, right from main() until exit(), which is why we chose this direction. By limiting interop to a single direction, we control the shape of the dependency tree. Rust can not depend on C++ so it cannot know about C++ types and functions, except through dependency injection. In this way, Rust can not land in arbitrary C++ code, only in functions passed through the API from C++.- We will only support third-party libraries for now. Third-party libraries are written as standalone components, they don’t hold implicit knowledge about the implementation of Chromium. This means they have APIs that are simpler and focused on their single task. Or, put another way, they typically have a narrow interface, without complex pointer graphs and shared ownership. We will be reviewing libraries that we bring in for C++ use to ensure they fit this expectation.

**The Interop Between Rust and C++ in Chromium**

We have observed that most successful C/C++ and Rust interop stories to date have been built around interop through narrow APIs (e.g. libraries for [QUIC](https://github.com/cloudflare/quiche#calling-quiche-from-cc) or [bluetooth](https://cs.android.com/android/platform/superproject/%2B/master%3Apackages/modules/Bluetooth/system/gd/rust/shim/src/bridge.rs), Linux drivers) or through clearly isolated components (e.g. IDLs, IPCs). Chrome is built on foundational but [really wide C++ APIs](https://source.chromium.org/chromium/chromium/src/%2B/main%3Acontent/public/browser/web_contents_observer.h), such as the //content/public layer. We examined what it would mean for us to build Rust components against these types of APIs. At a high level what we found was that because C++ and Rust play by different rules, things can go sideways very easily.

For example, Rust guarantees temporal memory safety with static analysis that relies on two inputs: [lifetimes](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html) ([inferred](https://doc.rust-lang.org/reference/lifetime-elision.html) or explicitly written) and [exclusive mutability](https://doc.rust-lang.org/rust-by-example/scope/borrow/alias.html). The latter is incompatible with how the majority of Chromium’s C++ is written. We hold redundant mutable pointers throughout the system, and pointers that provide multiple paths to reach mutable pointers. We have [cyclical](https://source.chromium.org/chromium/chromium/src/%2B/main%3Acontent/browser/renderer_host/frame_tree_node.h;l=667;drc=1e6c1a39cbbc1dcad6e7828661d74d76463465ed) [mutable](https://source.chromium.org/chromium/chromium/src/%2B/main%3Acontent/browser/renderer_host/render_frame_host_impl.h;l=3714;drc=1e6c1a39cbbc1dcad6e7828661d74d76463465ed) data structures. This is especially true in our browser process, which contains a giant interconnected system of (mutable) pointers. If these C++ pointers were also used as Rust references in a complex or long-lived way, it would require our C++ authors to understand the aliasing rules of Rust and prevent the possibility of violating them, such as by:

* Returning the same mutable pointer from a function twice, where the first may still be held.* Passing overlapping pointers where one is mutable into Rust, in a way that they may be held as references at the same time.* Mutating state that is visible to Rust through a shared or mutable reference.

Without interop tools providing support via the compiler and the type system, developers would need to understand all of the assumptions being made by Rust compiler, in order to not violate them from C++. In this framing, C++ is much like unsafe Rust. And while unsafe Rust is very costly to a project, its cost is managed by keeping it [encapsulated and to the minimum possible](https://chromium.googlesource.com/chromium/src/%2B/master/docs/security/rule-of-2.md#unsafe-code-in-safe-languages). In the same way, the full complexity of C++ would need to be encapsulated from safe Rust. Narrow APIs designed for interop can provide similar encapsulation, and we hope that interop tools can provide encapsulation in other ways that allow wider APIs between the languages.

The high-level summary is that without additional interop tooling support:

* Passing pointers/references across languages is risky.* Narrow interfaces between the languages is critical to make it feasible to write code correctly.

Any cross-language interop between arbitrary code ...