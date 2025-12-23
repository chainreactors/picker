---
title: Advent Of Configuration Extraction – Part 4: Turning capa Into A Configuration Extractor For TinyShell variant
url: https://blog.sekoia.io/advent-of-configuration-extraction-part-4-turning-capa-into-a-configuration-extractor-for-tinyshell-variant/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-22
fetch_date: 2025-12-23T03:25:32.745919
---

# Advent Of Configuration Extraction – Part 4: Turning capa Into A Configuration Extractor For TinyShell variant

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Advent Of Configuration Extraction – Part 4: Turning capa Into A Configuration Extractor For TinyShell variant

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Pierre Le Bourhis, Jeremy Scion and Sekoia TDR](#molongui-disabled-link)
December 22 2025

0

8 minutes reading

In the third part of our series ‘Advent of Configuration Extraction’, we dissect a lightweight **Linux backdoor**, that is derived from an open-source backdoor called *[TinySHell](https://github.com/creaktive/tsh/tree/master)*. It is designed to provide silent, persistent remote access to compromised servers. The malware consists of a **stripped ELF binary** that hides most identifying metadata, a **networking component** that connects to its command-and-control server using a custom authentication protocol, and a **backdoor module** capable of executing commands or spawning a remote shell. Its simplicity, minimal footprint, and removal of recognizable strings make it highly stealthy and effective for long-term espionage activities.

The sample [8e07beb854f77e90c174829bd4e01e86779d596710ad161dbc0e02a219d6227f](https://bazaar.abuse.ch/sample/8e07beb854f77e90c174829bd4e01e86779d596710ad161dbc0e02a219d6227f/) available on Malware Bazaar is used to highlight the configuration extraction development process.

# capa Overview

Before digging into the main topic of this report, this section makes a rapid tour of **[capa](https://mandiant.github.io/capa/)**, in order to understand the central piece of the configuration extractor.

**FLARE capa** is an open-source capability detection tool for malware analysis that identifies what a binary does rather than how it is implemented. It can work standalone or integrate with disassembly frameworks like IDA or Ghidra. capa statically analyzes executables (PE, ELF, Mach-O, shellcode), extracts features such as API calls, strings, instructions, control flow patterns, and embedded data, and matches them against human-readable YAML rules describing high-level behaviors (e.g., process injection, keylogging, persistence). Rules are evaluated hierarchically across multiple scopes (instruction, basic block, function, file), producing a concise list of detected capabilities.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/12/image-6.png)

*Figure 1. capa standalone cli output on the backdoor sample*

Each rule explicitly defines the scope at which it applies, meaning all required features must be present within the same instruction, basic block, function, or the entire file. This scoping model prevents unrelated features from being incorrectly combined across different parts of the binary and enables precise behavioral attribution (e.g., identifying a specific function responsible for injection). Rules express feature requirements using declarative logic constructs (AND, OR, NOT), quantifiers (e.g., “N or more occurrences”), and optional conditions. capa also supports rule dependencies, allowing complex capabilities to be composed from simpler ones by referencing other rules. During analysis, capa extracts features once, then evaluates rules bottom-up from lower to higher scopes, caching matches and resolving dependencies to produce explainable results with clear evidence linking each detected capability to the underlying code locations.

# Malware Extractor Overview

The backdoor obfuscates its string using RC4 encryption. This routine is invoked multiple times throughout the binary to retrieve various pieces of information, such as Linux file path, Command-and-Control (C2) configuration data and feature activation flags. As mentioned earlier, the malware binary is stripped, meaning that no symbols are available to help identify functions of interest during the configuration extraction process.

The extractor approach differs from those presented in the previous articles [[Part-1](https://blog.sekoia.io/advent-of-configuration-extraction-part-1-pipeline-overview-first-steps-with-kaiji-configuration-unboxing/), [Part 2](https://blog.sekoia.io/advent-of-configuration-extraction-part-2-unwrapping-quasarrats-configuration/)]. Since the string containing the C2 is obfuscated using RC4, the primary strategy consists of locating the corresponding decryption function within the binary. To achieve this, the extractor relies on **capa**. Then, the extractor leverages [Capstone](https://www.capstone-engine.org/) to manipulate the instructions to retrieve the decryption key and finally it uses [LIEF](https://lief.re/) to extract the encrypted strings.

## Locate RC4 function

As a first step, the standalone **capa** tool can be used, or alternatively its plugin version in a decompiler, to understand what to look for and in which context the targeted function operated. By inspecting the FLARE-capa view in IDA, the tool matches one of its rules named “**encrypted data using RC4 PRGA**” and returns the address of the corresponding function (in this sample, 0x402c81).

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/12/image-4.png)

*Figure 2. Flare capa plugin output on the backdoor sample*

Based on the plugin results, it is possible to clearly determine where and how the RC4 function is used. This is achieved by identifying cross-references to the function and analyzing its callers to determine the arguments, how they are supplied, and where the corresponding data are stored within the binary.

## CAPA Instrumentation

To locate the RC4 function, the extractor relies on the Python package **[flare-capa](https://pypi.org/project/flare-capa/)**. In order to keep the pipeline lightweight and maintainable, not all default capa rules are loaded. However, to obtain a functional flare-capa setup in Python, the extractor requires a minimal...