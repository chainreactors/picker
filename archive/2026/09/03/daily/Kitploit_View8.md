---
title: View8
url: https://kitploit.com/en/tools/github/suleram/view8
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:33.407325
---

# View8

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

View8 — Decompiles serialized V8 bytecode (JSC files) into high-level readable JavaScript-like code, with support for multiple V8 versions, tree output, and deterministic function naming for malware analysis. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/suleram/view8

![](https://assets.kitploit.com/production/public/tools/53912/586141eb6cf6f5518895313967cef892f13121dd116e51aa4bf4c3650d4d2b78-display-v1.webp)

[Static Analysis](/en/categories/static-analysis)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Malware Analysis](/en/categories/malware-analysis)[Binary Analysis](/en/categories/binary-analysis)

![GitHub](/providers/github.png)suleram/view8

# View8

Decompiles serialized V8 bytecode (JSC files) into high-level readable JavaScript-like code, with support for multiple V8 versions, tree output, and deterministic function naming for malware analysis.

[View Repository](https://github.com/suleram/view8)

37560231 month ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# View8

`View8` is a static analysis tool designed to decompile serialized V8 bytecode objects (JSC files) into high-level readable code. To parse and disassemble these serialized objects, View8 utilizes a patched compiled V8 binary. As a result, View8 produces a textual output similar to JavaScript.

## Requirements

* Python 3.x
* Disassembler binary. Available versions:

+ V8 Version `9.4.146.24` (Used in Node V16.x)
+ V8 Version `10.2.154.26` (Used in Node V18.x)
+ V8 Version `11.3.244.8` (Used in Node V20.x)

For compiled versions, visit the [releases page](https://github.com/suleram/View8/releases).

## Usage

### Command-Line Arguments

* `--inp`, : The input file name.

`-i`

- `--out`, `-o`: Path to the output. Depending on the selected options, the output may be a single file or a directory tree.

- `--input_format`, `-f`: Specify the input format. Options are:
  * `raw`: the input is a raw JSC file.
  * `disassembled`: the input file is already disassembled.
  * `serialized`: the input is already decompiled and stored in a serialized format. The current serialized format is Python `pickle`; use trusted input only.

- `--export_format`, `-e`: Specify the export format(s). Options are `v8_opcode`, `translated`, `decompiled`, and `serialized`. Multiple options can be combined. Default: `decompiled`.

- `--path`, `-p`: Path to the disassembler binary. Required if the input is in the raw format and View8 cannot automatically locate the matching disassembler.

- `--scope`: Propagate scope arguments. Default: `1`.

- `--normalize`: Replace address-derived function identifiers with deterministic names based on parse order.

- `--normalize-map [CSV]`: While using `--normalize`, write a CSV mapping every original function name to its normalized name. When the path is omitted, View8 derives `<output>.name_map.csv` from `--out`, or from `--inp` when no output path is set.

- `--tree`, `-t`: Split output into a tree structure rather than storing all functions in one file. Specify the function that will be used as the tree root. To start from the default main function, use `start`.

- `--split_mode`: Tree splitting mode. Options are `declarers`, `calls`, and `references`. Default: `declarers`.

- `--inline_depth`, `-d`: In `calls` and `references` modes, include functions reachable from the selected tree root up to depth N in the main tree file. Depth `0` means only the selected root; depth `1` includes direct callees/references; depth `2` includes their children. Not used with `declarers`.

- `--inline_branch_limit`, `-l`: In tree mode, inline complete child branches with at most N functions into the main tree file when child branches are included by `--inline_depth`. Larger branches are saved separately.

- `--split_depth`: In `calls` and `references` modes, limit how deep exported usage branches are traversed. Default: `4`.

- `--include`, `-n`: File containing functions to include in the output.

- `--exclude`, `-x`: File containing functions to exclude from the output.

- `--func`: Display a selected function.

- `--show_all`: In function display mode, also show lines marked as hidden.

- `--verbosity`, `-v`: Verbosity level. Accepted range: `0` to `3`.

### Basic Usage

To decompile a V8 bytecode file and export the decompiled code:

root@kitploit:~

```
python view8.py -i input_file -o output_file
```

### Disassembler Path

By default, `View8` detects the V8 bytecode version of the input file using `VersionDetector.exe` and automatically searches for a compatible disassembler binary in the `Bin` folder. This can be changed by specifying a different disassembler binary with the `--path` or `-p` option:

root@kitploit:~

```
python view8.py -i input_file -o output_file --path /path/to/disassembler
```

### Processing Disassembled Files

To skip the disassembling process and provide an already disassembled file as the input, use the `--input_format disassembled` or `-f disassembled` option:

root@kitploit:~

```
python view8.py -i input_file -o output_file -f disassembled
```

### Deterministic Function Names and Mapping CSV

Use `--normalize` to replace address-derived function names with deterministic identifiers. To preserve the relationship between the original and normalized names, add `--normalize-map`:

root@kitploit:~

```
python view8.py \
  --input_format disassembled \
  --inp sample.jsc.disasm.txt \
  --normalize \
  --normalize-map \
  --out decompiled/sample.dec.txt \
  --export_format decompiled serialized
```

This writes `decompiled/sample.dec.name_map.csv` with the following columns:

root@kitploit:~

```
original_name,normalized_name
func_start_0x268514e9dcd9,func_start_0x100000000
func_rne_0x268514eb0779,func_rne_0x100000001
```

An explicit CSV path can also be provided:

root@kitploit:~

```
python view8.py \
  --input_format disassembled \
  --inp sample.jsc.disasm.txt \
  --normalize \
  --normalize-map mappings/sample.names.csv \
  --out decompiled/sample.dec.txt
```

### Creating and Processing Serialized Files

Sometimes it is useful to decompile the file into a serialized format that preserves the parsed objects and structures. This type of output may be easier to post-process than a text format, for example during further deobfuscation. To create a serialized output, use the `serialized` export format:

root@kitploit:~

```
python view8.py -i input_file -o output_file -e serialized
```

**Security warning:** the current serialized format is a Python `pickle` file (`.pkl`). Unpickling data from untrusted sources can execute arbitrary code. Only load serialized files that you generated yourself.

To load a serialized output back and export it in another format, use `--input_format serialized` or `-f serialized`:

root@kitploit:~

```
python view8.py -i input_file -o output_file -f serialized
```

### Export Formats

Specify the export format(s) using the `--export_format` or `-e` option. You can combine mult...