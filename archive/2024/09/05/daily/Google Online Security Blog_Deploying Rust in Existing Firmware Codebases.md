---
title: Deploying Rust in Existing Firmware Codebases
url: http://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html
source: Google Online Security Blog
date: 2024-09-05
fetch_date: 2025-10-06T18:23:55.387351
---

# Deploying Rust in Existing Firmware Codebases

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Deploying Rust in Existing Firmware Codebases](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html "Deploying Rust in Existing Firmware Codebases")

September 4, 2024

Posted by Ivan Lozano and Dominik Maier, Android Team

Android's use of safe-by-design principles drives our adoption of memory-safe languages like Rust, making exploitation of the OS increasingly difficult with every release. To provide a secure foundation, we’re extending hardening and the use of [memory-safe languages to low-level firmware](https://security.googleblog.com/2023/10/bare-metal-rust-in-android.html) (including in [Trusty apps](https://cs.android.com/android/platform/superproject/main/%2B/main%3Atrusty/user/app/keymint/lib.rs;drc=4176f2465d7dc81c398730cb579c0a4949a9a832)).

In this blog post, we'll show you how to gradually introduce [Rust into your existing firmware](https://security.googleblog.com/2021/04/rust-in-android-platform.html#:~:text=But%20what%20about%20all%20that%20existing%20C%2B%2B%3F), prioritizing new code and the most security-critical code. You'll see how easy it is to boost security with drop-in Rust replacements, and we'll even demonstrate how the Rust toolchain can handle specialized bare-metal targets.

Drop-in Rust replacements for C code are not a novel idea and have been used in other cases, such as [librsvg’s adoption of Rust](https://mail.gnome.org/archives/desktop-devel-list/2017-January/msg00001.html) which involved [replacing C functions with Rust functions](https://web.archive.org/web/20170928062853/https%3A//people.gnome.org/~federico/blog/docs/fmq-porting-c-to-rust.pdf) in-place. We seek to demonstrate that this approach is viable for firmware, providing a path to memory-safety in an efficient and effective manner.

# Memory Safety for Firmware

Firmware serves as the interface between hardware and higher-level software. Due to the lack of software security mechanisms that are standard in higher-level software, vulnerabilities in firmware code can be dangerously exploited by malicious actors. Modern phones contain many coprocessors responsible for handling various operations, and each of these run their own firmware. Often, firmware consists of large legacy code bases written in memory-unsafe languages such as C or C++. Memory unsafety is the leading cause of vulnerabilities in [Android](https://source.android.com/docs/security/test/memory-safety), [Chrome](https://www.chromium.org/Home/chromium-security/memory-safety/), and many other code bases.

Rust provides a memory-safe alternative to C and C++ with comparable performance and code size. Additionally it supports interoperability with C with no overhead. The Android team has discussed [Rust for bare-metal firmware previously](https://security.googleblog.com/2023/10/bare-metal-rust-in-android.html), and has [developed training specifically for this domain](https://google.github.io/comprehensive-rust/bare-metal.html).

# Incremental Rust Adoption

Our incremental approach focusing on replacing new and highest risk existing code (for example, code which processes external untrusted input) can provide maximum security benefits with the least amount of effort. Simply writing any new code in Rust reduces the number of new vulnerabilities and over time can lead to a reduction in [the number of outstanding vulnerabilities](https://security.googleblog.com/2021/04/rust-in-android-platform.html).

You can replace existing C functionality by writing a thin Rust shim that translates between an existing Rust API and the C API the codebase expects. The C API is replicated and exported by the shim for the existing codebase to link against. The shim serves as [a wrapper](https://doc.rust-lang.org/nomicon/ffi.html#calling-rust-code-from-c) around the Rust library API, bridging the existing C API and the Rust API. This is a common approach when rewriting or replacing existing libraries with a Rust alternative.

# Challenges and Considerations

There are several challenges you need to consider before introducing Rust to your firmware codebase. In the following section we address the general state of no\_std Rust (that is, bare-metal Rust code), how to find the right off-the-shelf crate (a rust library), porting an std crate to no\_std, using Bindgen to produce FFI bindings, how to approach allocators and panics, and how to set up your toolchain.

## The Rust Standard Library and Bare-Metal Environments

Rust's standard library consists of three crates: [core](https://doc.rust-lang.org/core/), [alloc](https://doc.rust-lang.org/alloc/), and [std](https://doc.rust-lang.org/std/). The core crate is always available. The alloc crate requires an allocator for its functionality. The std crate assumes a full-blown operating system and is commonly not supported in bare-metal environments. A third-party crate indicates it doesn’t rely on std through the crate-level #![no\_std] attribute. This crate is said to be no\_std compatible. The rest of the blog will focus on these.

## Choosing a Component to Replace

When choosing a component to replace, focus on self-contained components with robust testing. Ideally, the components functionality can be provided by an open-source implementation readily available which supports bare-metal environments.

Parsers which handle standard and commonly used data formats or protocols (such as, XML or DNS) are good initial candidates. This ensures the initial effort focuses on the challenges of integrating Rust with the existing code base and build system rather than the particulars of a complex component and simplifies testing. This approach eases introducing more Rust later on.

## Choosing a Pre-Existing Crate (Rust Library)

Picking the right open-source crate (Rust library) to replace the chosen component is crucial. Things to consider are:

* Is the crate well maintained, for example, are open issues being addressed and does it use recent crate versions?
* How widely used is the crate? This may be used as a quality signal, but also important to consider in the context of using crates later on which may depend on it.
* Does the crate have acceptable documentation?
* Does it have acceptable test coverage?

Additionally, the crate should ideally be no\_std compatible, meaning the standard library is either unused or can be disabled. While a wide range of no\_std compatible crates exist, others do not yet support this mode of operation – in those cases, see the next section on converting a std library to no\_std.

By convention, crates which optionally support no\_std will provide an std feature to indicate whether the standard library should be used. Similarly, the alloc feature usually indicates using an allocator is optional.

|  |  |
| --- | --- |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPgBmsZj6ZTOto6Frw_NToC18UKVimJ8SHuCerE7W01D83L3qeJ-Qop83lTf1pvDshgc4CW3pap9aXpzVpSQZtG9EVZDzIQKD5x3vZ4yiEGDxMODTUTNZtlGMVy3Sh-I1i4x-QY8RzBAaqOSap6rGuC9WYg4pdhUO5vY_-OqUCcPssnZAYmUKb-FnV5Ainemg?key=NlrS0k5AvJIpHEA9_mIwTQ) | Note: Even when a library declares #![no\_std] in its source, there is no guarantee that its dependencies don’t depend on std. We recommend looking through the dependency tree to ensure that all dependencies support no\_std, or test whether the library compiles for a no\_std target. The only way to know is currently by trying to compile the crate for a bare-metal target. |

For example, one approach is to run cargo check with a bare-metal toolchain provided through rustup:

$ rustup target add aarch64-unknown-none

$ cargo check --target aarch64-unknown-none --no-default-features

## Porting a std Library to no\_...