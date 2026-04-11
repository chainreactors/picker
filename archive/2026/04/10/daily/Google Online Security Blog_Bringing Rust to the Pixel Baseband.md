---
title: Bringing Rust to the Pixel Baseband
url: http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html
source: Google Online Security Blog
date: 2026-04-10
fetch_date: 2026-04-11T04:20:39.654743
---

# Bringing Rust to the Pixel Baseband

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Bringing Rust to the Pixel Baseband](https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html "Bringing Rust to the Pixel Baseband")

April 10, 2026

Posted by Jiacheng Lu, Software Engineer, Google Pixel Team

Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. [Recognizing the risks](https://security.googleblog.com/2023/12/hardening-cellular-basebands-in-android.html) associated within the complex modem firmware, Pixel 9 shipped with [mitigations](https://security.googleblog.com/2024/10/pixel-proactive-security-cellular-modems.html) against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its proactive security measures further. Following our previous discussion on ["Deploying Rust in Existing Firmware Codebases"](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html), this post shares a concrete application: integrating a memory-safe Rust DNS(Domain Name System) parser into the modem firmware. The new Rust-based DNS parser significantly reduces our security risk by mitigating an entire class of vulnerabilities in a risky area, while also laying the foundation for broader adoption of memory-safe code in other areas.

Here we share our experience of working on it, and hope it can inspire the use of more memory safe languages in low-level environments.

### Why Modem Memory Safety Can’t Wait

In recent years, we have seen increasing interest in the cellular modem from attackers and security researchers. For example, Google's Project Zero [gained remote code execution](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html) on Pixel modems over the Internet. Pixel modem has tens of Megabytes of executable code. Given the complexity and remote attack surface of the modem, other critical memory safety vulnerabilities may remain in the predominantly memory-unsafe firmware code.

### Why DNS?

The DNS protocol is most commonly known in the context of browsers finding websites. With the evolution of cellular technology, modern cellular communications have migrated to digital data networks; consequently, even basic operations such as call forwarding rely on DNS services.

DNS is a complex protocol and requires parsing of untrusted data, which can lead to vulnerabilities, particularly when implemented in a memory-unsafe language (example: [CVE-2024-27227](https://nvd.nist.gov/vuln/detail/cve-2024-27227)). Implementing the DNS parser in Rust offers value by decreasing the attack surfaces associated with memory unsafety.

### Picking a DNS library

DNS already has a level of support in the open-source Rust community. We evaluated multiple open source crates that implement DNS. Based on [criteria shared in earlier posts](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html#:~:text=Existing%20Crate), we identified [hickory-proto](https://crates.io/crates/hickory-proto) as the best candidate. It has excellent maintenance, over 75% test coverage, and widespread adoption in the Rust community. Its pervasiveness shows its potential as the de-facto DNS choice and long term support. Although hickory-proto initially lacked `no_std` support, which is needed for Bare-metal environments (see our [previous post](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html#:~:text=Bare%2Dmetal%20Environments) on this topic), we were able to add support to it and its dependencies.

## Adding `no_std` support

The work to enable `no_std` for hickory-proto is mostly mechanical. We shared the process [in a previous post](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html#:~:text=Porting%20a%20std%20Library%20to%20no_std). We undertook modifications to hickory\_proto and its dependencies to enable `no_std` support. The upstream `no_std` work also results in a `no_std` URL parser, beneficial to other projects.

* <https://github.com/hickory-dns/hickory-dns/pull/2104>
* <https://github.com/servo/rust-url/pull/831>
* <https://github.com/krisprice/ipnet/pull/58>

The above PRs are great examples of how to extend `no_std` support to existing std-only crates.

## Code size study

Code size is the one of the factors that we evaluated when picking the DNS library to use.

|  |  |  |
| --- | --- | --- |
| Code size by category | Rust implemented Shim that calls Hickory-proto on receiving a DNS response | 4KB |
| core, alloc, compiler\_builtins (reusable, one-time cost) | 17KB |
| Hickory-proto library and dependencies | 350KB |

---

|  |  |  |
| --- | --- | --- |
| Sum |  | 371KB |

We built prototypes and measured size with [size-optimized settings](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html#:~:text=Build%20Optimizations). Expectedly, `hickory_proto` is not designed with embedded use in mind, and is not optimized for size. As the Pixel modem is not tightly memory constrained, we prioritized community support and code quality, leaving code size optimizations as future work.

However, the additional code size may be a blocker for other embedded systems. This could be addressed in the future by adding additional feature flags to conditionally compile only required functionality. Implementing this modularity would be a valuable future work.

### Hook-up Rust to modem firmware

Before building the Rust DNS library, we defined several Rust unit tests to cover basic arithmetic, dynamic allocations, and [`FFI`](https://doc.rust-lang.org/nomicon/ffi.html) to verify the integration of Rust with the existing modem firmware code base.

## Compile Rust code to staticlib

While using `cargo` is the default choice for compilation in the Rust ecosystem, it [presents challenges](https://security.googleblog.com/2021/05/integrating-rust-into-android-open.html#:~:text=No%20nested%20build%20systems) when integrating it into existing build systems. We evaluated two options:

1. Using `cargo` to build a [`staticlib`](https://doc.rust-lang.org/beta/rustc/command-line-arguments.html#--crate-type-a-list-of-types-of-crates-for-the-compiler-to-emit) before the modem builds. Then add the produced staticlib into the linking step.
2. Directly work with `rustc` and integrate the Rust compilation steps into the existing modem build system.

Option #1 does not scale if we are going to add more Rust components in the future, as linking multiple staticlibs may cause [duplicated symbol errors](https://github.com/rust-lang/rust/issues/44322). We chose option #2 as it scales more easily and allows tighter integration into our existing build system. Our existing C/C++ codebase uses [Pigweed](https://pigweed.dev/) to drive the primary build system. Pigweed supports Rust targets ([example](https://cs.opensource.google/pigweed/pigweed/%2B/main%3Apw_build/rust_library.gni;drc=87f7abc323e345dd2729d5039a7ee0ee49c2fd56)) with direct calls to [`rustc`](https://cs.opensource.google/pigweed/pigweed/%2B/main%3Apw_toolchain/generate_toolchain.gni;l=415;drc=e194c83f1d063833745f49da8f85b583be9774bb) through [`rust tools` defined in `GN`](https://gn.googlesource.com/gn/%2B/main/docs/reference.md#buildfile-functions-tool_specify-arguments-to-a-toolchain-tool_back-to-top-usage).

We compiled all the Rust crates, including hickory-proto, its dependencies, and core, compiler\_builtin, alloc, to [`rlib`](https://doc.rust-lang.org/reference/linkage.html#r-link.rlib). Then, we created a `staticlib` target with a single lib.rs file which references all the [`rlib`](https://doc.rust-lang.org/reference/linkage.htm...