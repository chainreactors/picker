---
title: Forget Linux, This 24 KB Bare Metal LLM OS Runs AI Faster
url: https://www.blackmoreops.com/bare-metal-llm-assembly-os-qwen3/
source: blackMORE Ops
date: 2026-11-26
fetch_date: 2026-11-27T10:17:28.544956
---

# Forget Linux, This 24 KB Bare Metal LLM OS Runs AI Faster

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Friday, November 27, 2026

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

* [Linux](https://www.blackmoreops.com/category/systems/linux/)
* [Security](https://www.blackmoreops.com/category/security/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

[Home](https://www.blackmoreops.com) > [Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/) > Forget Linux, This 24 KB Bare Metal LLM OS Runs AI Faster

[Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)[Linux](https://www.blackmoreops.com/category/systems/linux/)

# Forget Linux, This 24 KB Bare Metal LLM OS Runs AI Faster

## Run Qwen3 Without Linux on Bare Metal x86 Assembly vs llama.cpp Benchmark

9 hours ago

*13*

A developer has thrown out the operating system entirely and built a bare metal LLM that boots in under 100 milliseconds.

[![Bare metal LLM OS of 24 KB running Qwen3-0.6B at 134.9 tokens per second with no Linux](data:image/svg+xml...)](https://www.blackmoreops.com/wp-content/uploads/2026/11/bare-metal-llm-24kb-os-featured.webp)

asm-llm-os, a 24 KB bare metal LLM operating system

Alexey Fateev’s [llm.asm](https://github.com/alesha-pro/llm.asm) project packs a complete x86-64 operating system into 24,252 bytes of hand written assembly. Its only job is to run Alibaba’s Qwen3-0.6B language model. There is no Linux, no Windows, no C, no Rust and no libc. On an AMD EPYC 7642 server, Fateev’s own benchmarks show it generating text up to 54% faster than llama.cpp running on a normal Linux install.

[![Bare metal LLM decode benchmark of llm.asm against llama.cpp running Qwen3-0.6B on an AMD EPYC 7642](data:image/svg+xml...)](https://www.blackmoreops.com/wp-content/uploads/2026/11/bare-metal-llm-benchmark.webp)

Decode speed for Qwen3-0.6B Q8\_0 at 1 to 16 threads, from the llm.asm benchmark tables

Fateev announced the release [on X](https://x.com/superalesha/status/2125682626056839259) this week with the line “I deleted Linux completely”. The code, a bootable ISO builder and a Proxmox setup guide are on GitHub under the MIT licence.

Table of Contents

* [A 24 KB bare metal LLM that boots straight to a chat prompt](#penci-A_24_KB_bare_metal_LLM_that_boots_straight_to_a_chat_prompt "A 24 KB bare metal LLM that boots straight to a chat prompt")
* [The benchmark claims against llama.cpp](#penci-The_benchmark_claims_against_llamacpp "The benchmark claims against llama.cpp")
* [Bit-exact with PyTorch](#penci-Bit-exact_with_PyTorch "Bit-exact with PyTorch")
* [Running on a diskless Proxmox VM](#penci-Running_on_a_diskless_Proxmox_VM "Running on a diskless Proxmox VM")
* [The fine print](#penci-The_fine_print "The fine print")
* [What it means for local AI](#penci-What_it_means_for_local_AI "What it means for local AI")
* [Sources](#penci-Sources "Sources")

## A 24 KB bare metal LLM that boots straight to a chat prompt

The kernel, called asm-llm-os, is smaller than a typical web page. GRUB or QEMU loads it as a Multiboot kernel and drops the 614 MiB model file into memory beside it. From there the assembly code takes over. It switches the processor into 64-bit long mode, maps memory with 2 MiB huge pages, checks the CPU for AVX2, FMA and F16C, then reads the ACPI tables and wakes every core through the APIC.

Between 74 and 94 milliseconds after the kernel starts, the user is looking at an `asm-llm>` prompt. It is a working multi-turn chat. The KV cache is kept between turns, Qwen3’s reasoning mode can be turned on with `/think`, and a `/bench` command runs a speed test on the spot. Input comes from a PS/2 keyboard and output goes to the VGA text screen, with everything mirrored over a serial port.

In this bare metal LLM design the weights are never copied. The transformer reads them directly from the physical address where the bootloader left them. That is possible only because there is no kernel underneath demanding virtual memory, file systems or permission checks.

## The benchmark claims against llama.cpp

Fateev compared three builds on the same AMD EPYC 7642: llama.cpp running CPU only with `-ngl 0`, his 14.7 KB static Linux binary, and the bootable bare metal LLM OS running under QEMU with KVM. All three used Q8\_0 weights, a 34 token prompt and 64 generated tokens, averaged over three runs.

* 1 thread: 23.67 tok/s for the bare met...