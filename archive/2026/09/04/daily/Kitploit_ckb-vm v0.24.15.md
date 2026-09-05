---
title: ckb-vm v0.24.15
url: https://kitploit.com/en/posts/github-nervosnetwork-ckb-vm-v02415
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:08.356288
---

# ckb-vm v0.24.15

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7153/0e20dae38e25426be05276a7208996479a5cef7fcfa598b9e778d816a7e41be1.png)

New releaseSep 4, 2026

# ckb-vm v0.24.15

CKB's vm, based on open source RISC-V ISA

Share

# [Nervos CKB](https://nervos.org) VM

[![Build Status](https://dev.azure.com/nervosnetwork/ckb-vm/_apis/build/status/nervosnetwork.ckb-vm?branchName=develop)](https://dev.azure.com/nervosnetwork/ckb-vm/_build/latest?definitionId=10&branchName=develop)
[![codecov](https://codecov.io/gh/nervosnetwork/ckb-vm/branch/develop/graph/badge.svg)](https://codecov.io/gh/nervosnetwork/ckb-vm)

---

## About CKB VM

CKB VM is a pure software implementation of the [RISC-V](https://riscv.org/) instruction set used as scripting VM in CKB. Right now it implements full IMCB instructions for both 32-bit and 64-bit register size support. In the future we might also implement V extensions to enable better crypto implementations.

## License

Nervos CKB is released under the terms of the MIT license. See [COPYING](https://github.com/nervosnetwork/ckb-vm/blob/develop/COPYING) for more information or see <https://opensource.org/licenses/MIT>.

## Development Process

This is now deployed and used in production CKB mainnet.

The `develop` branch is regularly built and tested, but is not guaranteed to be completely stable. CKB will use released versions of CKB VM which are tested and more stable.

The contribution workflow is described in [CONTRIBUTING.md](https://github.com/nervosnetwork/ckb-vm/blob/develop/CONTRIBUTING.md), and security policy is described in [SECURITY.md](https://github.com/nervosnetwork/ckb-vm/blob/develop/SECURITY.md). To propose new protocol or standard for Nervos, see [Nervos RFC](https://github.com/nervosnetwork/rfcs).

---

## How to build

CKB VM is currently tested mainly with `stable` Rust version on 64-bit Linux, macOS, and Windows.

root@kitploit:~

```
# download CKB VM
$ git clone https://github.com/nervosnetwork/ckb-vm
$ cd ckb-vm
$ cargo build
```

You can also run the tests:

root@kitploit:~

```
make test
```

CKB VM has already included RISC-V binaries used in tests, so you don't need a RISC-V compiler to build binaries. However if you do want to play with your own binaries, a RISC-V compiler might be needed. [riscv-tools](https://github.com/riscv/riscv-tools) can be a good starting point here, or if you are an expert on GNU toolchain, you might also compile upstream GCC from source with RISC-V support, [here](https://github.com/nervosnetwork/ckb-vm/blob/develop/examples/is13.rs) is an example. CKB VM is using standard RISC-V instructions and ELF binary format, so theoretically any RISC-V compatible compilers are able to produce contracts used in CKB VM(tho bug reports are very welcome if you find breakage).

## Notes on Different Modes

Right now CKB VM has 2 different modes:

* Rust interpreter mode
* Assembly based interpreter mode(ASM mode)

For consistent behavior, you should only use ASM mode. The Rust mode is developed more to assist development, and never used in production by us. In case of bugs, there might be inconsistent behaviors between Rust mode and ASM mode.

[Read more](/en/tools/github/nervosnetwork/ckb-vm?expand=1)

## Categories

[Embedded Systems Security](/en/categories/embedded-systems-security)[Cryptography](/en/categories/cryptography)[Hardware Security](/en/categories/hardware-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories