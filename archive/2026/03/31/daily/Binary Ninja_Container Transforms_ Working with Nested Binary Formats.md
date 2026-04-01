---
title: Container Transforms: Working with Nested Binary Formats
url: https://binary.ninja/2026/03/31/container-transforms.html
source: Binary Ninja
date: 2026-03-31
fetch_date: 2026-04-01T04:45:23.265552
---

# Container Transforms: Working with Nested Binary Formats

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Portal](https://portal.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## Container Transforms: Working with Nested Binary Formats

* [Brian Potchik](https://github.com/bpotchik)
* 2026-03-31
* [reversing](/tag/reversing), [announcements](/tag/announcements)

![Container Transforms >](/blog/images/container/container.png)

Firmware analysis, malware triage, and embedded systems reverse engineering often require extracting files from nested container formats: TAR archives inside GZIP files, encrypted firmware wrapped in multiple compression layers, or password-protected ZIPs containing âinfectedâ malware.

Manually peeling each layer with separate tools gets old fast.

Binary Ninjaâs Container Transform system automates this workflow, handling detection, extraction, password management, and multi-layer nesting while preserving the structure and provenance of each stage.

## The Nested Binary Challenge

Consider analyzing an Apple firmware update:

```
firmware.img4 (IMG4 container)
  ââ LZFSE compressed payload
      ââ Mach-O kernel
```

Traditionally you would:

1. Recognize the IMG4 format
2. Extract the payload
3. Identify and decompress LZFSE
4. Finally load the Mach-O

With Container Transforms, this entire chain resolves automatically during file load. Hereâs the end result of this feature in action:

![Opening a Mach-O kernel from an IMG4 firmware container](/blog/images/container/machokernel.gif)

## The Real Problem: Representation

This system began with a narrower feature: *support for memory regions that store decoded data*.

The initial impetus for this was performance-related ([GitHub issue #7234](https://github.com/Vector35/binaryninja-api/issues/7234)). Decoded data flowing through the Undo buffer caused regressions because that system was designed for small user-driven edits, not large, derived byte streams.

But the deeper issue was not performance. It was representation itself.

Decoded data has:

* **Provenance**: how it was produced
* **Structure**: which container or encoding it came from
* **Multiplicity**: one input may produce many outputs

Flattening derived data into a linear memory view discards that information.

What was missing was a proper way to model derived artifacts: data that exists because it was decoded, decompressed, or extracted from something else, possibly across multiple stages.

The Container Transform system models each step as a contextual transformation instead of mutating data in place. The result is a navigable tree of derived artifacts that preserves structure, metadata, and history without special cases.

## Architectural Direction

We considered several ways this could have been implemented:

* A completely new subsystem for extracted data
* Representing each stage as a [`BinaryView`](https://api.binary.ninja/binaryninja.binaryview-module.html#binaryninja.binaryview.BinaryView)
* Extending the existing Transform system

Building a parallel subsystem could add unnecessary complexity. Modeling each stage as a `BinaryView` would have blurred the line between representation and analysis. A `BinaryView` implies analyzable program state, lifecycle semantics, and ownership that do not apply to intermediate decoding stages.

Instead, we leveraged our existing [`Transform`](https://api.binary.ninja/binaryninja.transform-module.html#binaryninja.transform.Transform) system and extended it with explicit contextual representation. Transforms now produce *context*, not just bytes. That distinction enables nested containers, multi-output transforms, automatic and interactive workflows, and a clean separation between extraction and analysis.

## What Are Container Transforms?

Container transforms are specialized transforms that decode structured formats. Unlike simple encodings (Base64, Hex), container transforms can:

1. **Auto-detect** formats using magic bytes or other signatures
2. **Extract multiple outputs** from a single input
3. **Handle passwords and encryption**
4. **Chain** across nested formats
5. **Preserve provenance** information

### Mental Model: Trees, Not Pipelines

```
graph TD
    A["archive.tar.gz"] -->|Gzip| B["archive.tar"]
    B -->|Tar| C["README.md"]
    B -->|Tar| D["firmware.img4"]
    B -->|Tar| E["config.json"]
    D -->|IMG4| F["LZFSE payload"]
    F -->|LZFSE| G["Mach-O kernel"]
```

Container extraction forms a tree rather than a linear pipeline. Each node represents a transformation step; children represent derived artifacts. You can inspect intermediate layers instead of interacting only with a flattened final result.

Binary Ninja ships with detection-enabled transforms for:

* **Compression**: Gzip, Zlib, Bzip2, LZMA, LZ4 (Frame), Zstd, XZ, LZFSE
* **Archives**: Zip, Tar, CPIO, AR, CaRT
* **Binary Containers**: IMG4, Universal (Fat Mach-O)
* **Firmware Containers**: UImage, FIT, TRX
* **Disk Images**: DMG
* **Text Encodings**: IntelHex, SRec, TiTxt

```
>>> [x.name for x in Transform if getattr(x, "supports_detection", False)]
['Gzip', 'Zlib', 'Bzip2', 'LZMA', 'LZ4Frame', 'Zstd', 'XZ', 'Zip', 'CaRT', 'Tar', 'AR', 'CPIO', 'DMG', 'UImage', 'FIT', 'TRX', 'IntelHex', 'SRec', 'TiTxt', 'IMG4', 'LZFSE', 'Universal']
```

### Other Transforms

The transforms listed above support **automatic detection**, meaning Binary Ninja can recognize the format and incorporate it into the container resolution tree during file loading.

Binary Ninja also provides many additional transforms that are **not detection-enabled**. These transforms can still be applied manually but are not automatically considered during container discovery.

Common examples include:

* **Raw compression primitives** (e.g., `Deflate`, `LZ4Block`, `LZF`)
* **Encodings** (`Base64`, `HexDump`, `RawHex`)
* **Text / language representations** (`CArray`, `RustArray`, `IntList`)
* **Cryptographic transforms** (`AES`, `DES`, `RC4`, etc.)
* **Simple reversible transforms** (`XOR`, `ROL`, arithmetic transforms)

These transforms typically require parameters, lack reliable file signatures, or would otherwise produce too many false positives if attempted automatically.

They remain accessible through the Transform system and can be applied programmatically:

```
Transform["Base64"].decode(data)
Transform["Deflate"].decode(data)
Transform["XOR"].decode(data, {"key": b"\x42"})
```

This design keeps automatic container discovery reliable while still exposing the full transform toolkit for manual analysis workflows.

## Invocation Model

Container transforms participate directly in the standard file loading pipeline, both in the UI and through the [`load()`](https://api.binary.ninja/#binaryninja.load) API. When a file is opened, Binary Ninja evaluates whether the input represents a container and recursively resolves any nested transforms.

The process consists of four stages:

1. **Detection** identifies container formats applicable to the input.
2. **Transform Resolution** applies matching transforms and recursively evaluates their outputs.
3. **Context Tree Construction** builds a transformation context tree representing all discovered extraction paths.
4. **Context Selection** chooses a final derived artifact for analysis.

This model allows Binary Ninja to transparently...