---
title: Building checksec without boundaries with Checksec Anywhere
url: https://blog.trailofbits.com/2025/11/13/building-checksec-without-boundaries-with-checksec-anywhere/
source: The Trail of Bits Blog
date: 2025-11-13
fetch_date: 2025-11-14T03:12:39.696143
---

# Building checksec without boundaries with Checksec Anywhere

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Building checksec without boundaries with Checksec Anywhere

Gabe Sherman

November 13, 2025

[tool-release](/categories/tool-release/), [internship-projects](/categories/internship-projects/), [open-source](/categories/open-source/), [binary-analysis](/categories/binary-analysis/), [capture-the-flag](/categories/capture-the-flag/)

Page content

* [Using Checksec Anywhere](#using-checksec-anywhere)
* [Key features of Checksec Anywhere](#key-features-of-checksec-anywhere)
  + [Multi-format analysis](#multi-format-analysis)
  + [Privacy-first](#privacy-first)
  + [Performance by design](#performance-by-design)
  + [Enhanced accessibility](#enhanced-accessibility)
  + [Technical architecture](#technical-architecture)
* [Future work](#future-work)
  + [Additional formats](#additional-formats)
  + [Additional security properties](#additional-security-properties)
* [Try it out](#try-it-out)

Since its original release in 2009, [checksec](https://www.trapkit.de/tools/checksec/) has become widely used in the software security community, proving useful in CTF challenges, security posturing, and general binary analysis. The tool inspects executables to determine which exploit mitigations (e.g., ASLR, DEP, stack canaries, etc.) are enabled, rapidly gauging a program’s defensive hardening. This success inspired numerous spinoffs: a [contemporary Go implementation](https://github.com/slimm609/checksec), Trail of Bits’ [Winchecksec](https://github.com/trailofbits/winchecksec) for PE binaries, and various scripts targeting Apple’s Mach-O binary format. However, this created an unwieldy ecosystem where security professionals must juggle multiple tools, each with different interfaces, dependencies, and feature sets.

During my summer internship at Trail of Bits, I built [Checksec Anywhere](https://checksec-anywhere.com/) to consolidate this fragmented ecosystem into a consistent and accessible platform. Checksec Anywhere brings ELF, PE, and Mach-O analysis directly to your browser. It runs completely locally: no accounts, no uploads, no downloads. It is fast (analyzes thousands of binaries in seconds) and private, and lets you share results with a simple URL.

## Using Checksec Anywhere

To use Checksec Anywhere, just drag and drop a file or folder directly into the browser. Results are instantly displayed with color-coded messages reflecting finding severity. All processing happens locally in your browser; at no point is data sent to Trail of Bits or anyone else.

![Figure 1: Uploading 746 files from /usr/bin to Checksec Anywhere](/img/checksec-anywhere/checksec-anywhere-1.gif)

Figure 1: Uploading 746 files from /usr/bin to Checksec Anywhere

## Key features of Checksec Anywhere

### Multi-format analysis

Checksec Anywhere performs comprehensive binary analysis across ELF, PE, and Mach-O formats from a single interface, providing analysis tailored to each platform’s unique security mechanisms. This includes traditional checks like stack canaries and PIE for ELF binaries, GS cookies and Control Flow Guard for PE files, and ARC and code signing for Mach-O executables. For users familiar with the traditional checksec family of tools, Checksec Anywhere reports maintain consistency with prior reporting nomenclature.

### Privacy-first

Unlike many browser-accessible tools that simply provide a web interface to server-side processing, Checksec Anywhere ensures that your binaries never leave your machine by performing all analysis directly in the browser. Report generation also happens locally, and shareable links do not reveal binary content.

### Performance by design

From browser upload to complete security report, Checksec Anywhere is designed to rapidly process multiple files. Since Checksec Anywhere runs locally, the exact performance depends on your machine… but it’s fast. On a modern MacBook Pro it can analyze thousands of files in mere seconds.

### Enhanced accessibility

Checksec Anywhere eliminates installation barriers by offering an entirely browser-based interface and features designed to provide accessibility:

* **Shareable results**: Generate static URLs for any report view, enabling secure collaboration without exposing binaries.
* **SARIF export**: Generate reports in SARIF format for integration with CI/CD pipelines and other security tools. These reports are also generated entirely on your local machine.
* **Simple batch processing**: Drag and drop entire directories for simple bulk analysis.
* **Tabbed interface**: Manage multiple analyses simultaneously with an intuitive UI.

  ![Figure 2: Tabbed interface for managing multiple analyses](/img/checksec-anywhere/checksec-anywhere-2.png)

  Figure 2: Tabbed interface for managing multiple analyses

### Technical architecture

Checksec Anywhere leverages modern web technologies to deliver native-tool performance in the browser:

* **Rust core**: Checksec Anywhere is built on the [checksec.rs](https://github.com/etke/checksec.rs) foundation, using well-established crates like Goblin for binary parsing and iced\_x86 for disassembly.
* **WebAssembly bridge**: The Rust code is compiled to Wasm using wasm-pack, exposing low-level functionality through a clean JavaScript API.
* **Extensible design**: Per-format processing architecture allows easy addition of new binary types and security checks.
* **Advanced analysis**: Checksec Anywhere performs disassembly to enable deeper introspection (like to detect stack protection in PE binaries).

See the [open-source codebase](https://github.com/trailofbits/checksec-anywhere) to dig further into its architecture.

## Future work

With an established infrastructure for cross-platform binary analysis and reporting, we can easily add new features and extensions. If you have pull requests, we’d love to review and merge them.

### Additional formats

A current major blind spot is lack of support for mobile binary formats like Android APK and iOS IPA. Adding analysis for these formats would address the expanding mobile threat landscape. Similarly, specialized handling of firmware binaries and bootloaders would extend coverage to critical system-level components in mobile and embedded devices.

### Additional security properties

Checksec Anywhere is designed to add new checks as researchers discover new attack methods. For example, recent research has uncovered multiple mechanisms by which compiler optimizations violate constant-time execution guarantees, prompting significant discussion within the compiler community (see [this LLVM discourse thread](https://discourse.llvm.org/t/rfc-constant-time-execution-guarantees-in-llvm/86700), for example). As these issues are addressed, constant-time security checks can be integrated into Checksec Anywhere, providing immediate feedback on whether a given binary is resistant to timing attacks.

## Try it out

Checksec Anywhere eliminates the overhead of managing format-specific security analysis tools while providing immediate access to comprehensive binary security reports. No installation, no dependencies, no compromises on privacy or performance. Visit [checksec-anywhere.com](http://checksec-anywhere.com) and try it now!

I’d like to extend a special thank you to my mentors William Woodruff and Bradley Swain for their guidance and support throughout my summer here at Trail of Bits!

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [Using Checksec Anywhere](#using-checksec-anywhere)
* [Key features of Checksec Anywhere](#key-features-of-checksec-anywhere)
  + [Multi-format analysis...