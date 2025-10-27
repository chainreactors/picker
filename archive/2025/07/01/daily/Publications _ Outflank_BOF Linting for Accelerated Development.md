---
title: BOF Linting for Accelerated Development
url: https://www.outflank.nl/blog/2025/06/30/bof-linting-for-accelerated-development/
source: Publications | Outflank
date: 2025-07-01
fetch_date: 2025-10-06T23:55:47.217903
---

# BOF Linting for Accelerated Development

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [BOF Linting for Accelerated Development](https://www.outflank.nl/blog/2025/06/30/bof-linting-for-accelerated-development/ "BOF Linting for Accelerated Development")

[Cedric Van Bockhaven](https://www.outflank.nl/blog/author/cedric/ "Posts by Cedric Van Bockhaven")
 |
June 30, 2025

Creating Beacon Object Files (BOFs) allows operators to extend the functionality of a C2 framework, though their development may sometimes involve hidden complexities that only become apparent after the BOF is executed. Today, we introduce a BOF linting tool to address some of the common pitfalls.

BOFs are lightweight, in-memory modules used in **[Cobalt Strike](https://www.outflank.nl/products/cobalt-strike/)** and other post-exploitation/C2 frameworks such as [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/) and [Core Impact](https://www.coresecurity.com/products/core-impact).  They are object files produced by a C compiler ([COFF](https://en.wikipedia.org/wiki/COFF)). Cobalt Strike parses this file and acts as a linker and loader for its contents. This approach allows you to write code for use in Beacon, without tedious gymnastics to manage strings and dynamically call Win32 APIs.

BOFs are powerful and flexible, but their minimalistic design inherently comes with strict constraints. For example, a lot of common functions (e.g., `strlen, strcmp`, etc.) are not directly available to you via a BOF as the library these functions are defined in is not linked against. Instead, the BOF standard allows you to call external functions via Dynamic Function Resolution (DFR).

The Cobalt Strike team has published excellent documentation materials and support tools: [BOF](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm) [manual](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm), [BOF-](https://github.com/Cobalt-Strike/bof_template)[template](https://github.com/Cobalt-Strike/bof_template), and, most recently, [BOF-VS](https://www.cobaltstrike.com/blog/simplifying-bof-development). BOFs are usable in all frameworks with a BOF loader.

Within the OST offering, we provide various tools via BOF. We want BOFs to work across different frameworks, which means we need compatibility with the various available BOF loaders. Loaders might differ in implementation each with their own limitations.

If you have developed a BOF before, you might have encountered that BOF development can have subtle pitfalls. Furthermore, some issues can often only be noticed at runtime, instead of during development.

Inspired by the excellent primers like [BOFs for Script Kiddies](https://trustedsec.com/blog/bofs-for-script-kiddies) and [A Developer’s Introduction to Beacon Object Files](https://trustedsec.com/blog/a-developers-introduction-to-beacon-object-files), **we’ve built `boflint`: a tool designed to make the BOF development lifecycle smoother and less error-prone.**

## **BOF Limitations and Loader Limitations**

BOFs impose inherent limitations, and compiler quirks (gcc vs. MSVC) along with loader differences can further affect the proper functioning of your BOF.

When the BOF loader parses the COFF file, it performs section handling, symbol handling, and relocation handling. Issues can arise during any of these stages:

* **Section handling:**
  + E.g. not all loaders correctly parse sections like `.bss` (used for zero-initialized/unitialized globals). This might require [workarounds](https://github.com/CCob/BOF.NET/blob/main/bofs/bofnet_execute.cpp#L39-L42) in your code.
* **Symbol handling:**
  + E.g. references to unresolved symbols (for example, usage of `printf` instead of `BeaconPrintf`). This might also happen transparently when the compiler adds in references to `memset/memmove` when using struct initializers. Similarly, when you attempt to use STL functions, the compiler will automatically add symbol references.
  + Every function or symbol used in a BOF must be explicitly resolvable by the loader. Undefined or unresolvable imports may cause the BOF to fail at runtime.
* **Relocation handling:**
  + E.g. most loaders only implement a subset of relocation types.

By reviewing the section, symbol and relocation information in a BOF after compilation, we can identify potential issues early – before running the BOF.

## **Enter BOF Linting**

**To help identify potential BOF issues we developed `boflint`: a post-compilation linter for BOF files. `boflint` analyzes your BOF for common errors before running it in an implant, preventing worst-case scenarios such as crashing the implant.**

`boflint` identifies several key issues:

* **Relocation types**: Ensures only supported relocation types are used.
* **Entry point validation**: Verifies the presence of the mandatory `go` or `sleep_mask` function.
* **Import resolution**: Flags undefined or unresolvable imports.
* **Large stack variables**: Detects large stack variable usage that results in an unresolvable import for stack probing.
* **Exception handling**: Warns against the use of exception handling, which is unsupported in BOFs.

Several common issues can be detected by the linter by verifying the section, symbol and relocation information in the BOF. Different BOF loaders handle edge cases differently. `boflint` currently supports validation for BOFs targeting Cobalt Strike, OC2 and Core Impact.

## **Using `boflint` in Your Workflow**

In 2023, the Cobalt Strike team released a [Visual Studio BOF template](https://github.com/Cobalt-Strike/bof-vs/) (BOF-VS), which was aimed at [simplifying BOF development](https://www.cobaltstrike.com/blog/simplifying-bof-development) and resolving many of the common issues that arise in BOF development.

We have worked closely with the Cobalt Strike team to incorporate `boflint` directly into BOF-VS’s workflow. Now when building a BOF in Visual Studio, the linter will automatically check your BOF for known issues, such as unresolved import symbols, as highlighted in the screenshot below.

![](https://www.outflank.nl/wp-content/uploads/2025/02/image-1.png)

*Screenshot showing the build output of BOF-VS with `boflint` highlighting a unresolved imported symbol error.*

If you compile BOFs in other environments, integrating `boflint` into your workflow is simple. The idea is to run `boflint` after compiling your BOF, so you could add it to your Makefile.

For example, a Makefile might look like this:

`bof`:
`x86_64-w64-mingw32-gcc -o example.o example.c`
`boflint.py example.o`

## **Get** **S****tarted with** **L****inting**

...