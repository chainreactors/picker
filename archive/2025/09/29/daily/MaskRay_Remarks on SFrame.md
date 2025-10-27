---
title: Remarks on SFrame
url: https://maskray.me/blog/2025-09-28-remarks-on-sframe
source: MaskRay
date: 2025-09-29
fetch_date: 2025-10-02T20:50:14.577160
---

# Remarks on SFrame

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-09-28](/blog/2025-09-28-remarks-on-sframe)

# Remarks on SFrame

The `.sframe` format is a lightweight alternative to
`.eh_frame` and `.eh_frame_hdr` designed for
efficient [stack
unwinding](/blog/2020-11-08-stack-unwinding). By trading some functionality and flexibility for
compactness, SFrame achieves significantly smaller size while
maintaining the essential unwinding capabilities needed by
profilers.

SFrame focuses on three fundamental elements for each function:

* Canonical Frame Address (CFA): The base address for stack frame
  calculations
* Return address
* Frame pointer

An `.sframe` section follows a straightforward layout:

* Header: Contains metadata and offset information
* Auxiliary header (optional): Reserved for future extensions
* Function Descriptor Entries (FDEs): Array describing each
  function
* Frame Row Entries (FREs): Arrays of unwinding information per
  function

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` struct [[gnu::packed]] sframe_header {   struct {     uint16_t sfp_magic;     uint8_t sfp_version;     uint8_t sfp_flags;   } sfh_preamble;   uint8_t sfh_abi_arch;   int8_t sfh_cfa_fixed_fp_offset;   // Used by x86-64 to define the return address slot relative to CFA   int8_t sfh_cfa_fixed_ra_offset;   // Size in bytes of the auxiliary header, allowing extensibility   uint8_t sfh_auxhdr_len;   // Numbers of FDEs and FREs   uint32_t sfh_num_fdes;   uint32_t sfh_num_fres;   // Size in bytes of FREs   uint32_t sfh_fre_len;   // Offsets in bytes of FDEs and FREs   uint32_t sfh_fdeoff;   uint32_t sfh_freoff; }; ``` |

While magic is popular choices for file formats, they deviate from
established ELF conventions, which simplifies utilizes the section type
for distinction.

The version field resembles the similar uses within DWARF section
headers. SFrame will likely evolve over time, unlike ELF's more stable
control structures. This means we'll probably need to keep producers and
consumers evolving in lockstep, which creates a stronger case for
internal versioning. An internal version field would allow linkers to
upgrade or ignore unsupported low-version input pieces, providing more
flexibility in handling version mismatches.

## Data structures

### Function Descriptor Entries (FDEs)

Function Descriptor Entries serve as the bridge between functions and
their unwinding information. Each FDE describes a function's location
and provides a direct link to its corresponding Frame Row Entries
(FREs), which contain the actual unwinding data.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` struct [[gnu::packed]] sframe_func_desc_entry {   int32_t sfde_func_start_address;   uint32_t sfde_func_size;   uint32_t sfde_func_start_fre_off;   uint32_t sfde_func_num_fres;   // bits 0-3 fretype: sfre_start_address type   // bit 4 fdetype: SFRAME_FDE_TYPE_PCINC or SFRAME_FDE_TYPE_PCMASK   // bit 5 pauth_key: (AArch64 only) the signing key for the return address   uint8_t sfde_func_info;   // The size of the repetitive code block for SFRAME_FDE_TYPE_PCMASK; used by .plt   uint8_t sfde_func_rep_size;   uint16_t sfde_func_padding2; }; ``` |

The current design has room for optimization. The
`sfde_func_num_fres` field uses a full 32 bits, which is
wasteful for most functions. We could use `uint16_t` instead,
requiring exceptionally large functions to be split across multiple
FDEs.

It's important to note that SFrame's function concept represents code
ranges rather than logical program functions. This distinction becomes
particularly relevant with compiler optimizations like hot-cold
splitting, where a single logical function may span multiple
non-contiguous code ranges, each requiring its own FDE.

The padding field `sfde_func_padding2` represents
unnecessary overhead in modern architectures where unaligned memory
access performs efficiently, making the alignment benefits
negligible.

To enable binary search on `sfde_func_start_address`, FDEs
must maintain a fixed size, which precludes the use of variable-length
integer encodings like PrefixVarInt.

### Frame Row Entries (FREs)

Frame Row Entries contain the actual unwinding information for
specific program counter ranges within a function. The template design
allows for different address sizes based on the function's
characteristics.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` template <class AddrType> struct [[gnu::packed]] sframe_frame_row_entry {   // If the fdetype is SFRAME_FDE_TYPE_PCINC, this is an offset relative to sfde_func_start_address   AddrType sfre_start_address;   // bit 0 fre_cfa_base_reg_id: define BASE_REG as either FP or SP   // bits 1-4 fre_offset_count: typically 1 to 3, describing CFA, FP, and RA   // bits 5-6 fre_offset_size: byte size of offset entries (1, 2, or 4 bytes)   sframe_fre_info sfre_info; }; ``` |

Each FRE contains variable-length stack offsets stored as trailing
data. The `fre_offset_size` field determines whether offsets
use 1, 2, or 4 bytes (`uint8_t`, `uint16_t`, or
`uint32_t`), allowing optimal space usage based on stack
frame sizes.

## Architecture-specific stack offsets

SFrame adapts to different processor architectures by varying its
offset encoding to match their respective calling conventions and
architectural constraints.

### x86-64

The x86-64 implementation takes advantage of the architecture's
predictable stack layout:

* First offset: Encodes CFA as `BASE_REG + offset`
* Second offset (if present): Encodes FP as
  `CFA + offset`
* Return address: Computed implicitly as
  `CFA + sfh_cfa_fixed_ra_offset` (using the header field)

### AArch64

AArch64's more flexible calling conventions require explicit return
address tracking:

* First offset: Encodes CFA as `BASE_REG + offset`
* Second offset: Encodes return address as
  `CFA + offset`
* Third offset (if present): Encodes FP as
  `CFA + offset`

The explicit return address encoding accommodates AArch64's variable
stack layouts and link register usage patterns.

### s390x

TODO

## `.eh_frame` and `.sframe`

SFrame reduces size compared to `.eh_frame` plus
`.eh_frame_hdr` by:

* Eliminating `.eh_frame_hdr` through sorted
  `sfde_func_start_address` fields
* Replacing CIE pointers with direct FDE-to-FRE references
* Using variable-width `sfre_start_address` fields (1 or 2
  bytes) for small functions
* Storing start addresses instead of address ranges.
  `.eh_frame` address ranges
* Start addresses in a small function use 1 or 2 byte fields, more
  efficient than `.eh_frame` initial\_location, which needs at
  least 4 bytes (`DW_EH_PE_sdata4`).
* Hard-coding stack offsets rather than using flexible register
  specifications

However, the bytecode design of `.eh_frame` can sometimes
be more efficient than `.sframe`, as demonstrated on
x86-64.

---

SFrame serves as a specialized complement to `.eh_frame`
rather than a complement replacement. The current version does not
include personality routines, Language Specific Data Area (LSDA)
information, or the ability to encode extra callee-saved registers.
While these constraints make SFrame ideal for profilers and debuggers,
they prevent it from supporting C++ exception handling, where
libstdc++/libc++abi requires the full `.eh_frame` feature
set.

In practice, executables and shared objects will likely contain all
three sections:

* `.eh_frame`: Complete unwinding information for exception
  handling
* `.eh_frame_hdr`: Fast lookup table for
  `.eh_frame`
* `.sframe`: Compact unwinding information for
  profilers

The auxiliary header, currently unused, provides a pathway for future
enhancements. It could potentially accommodate `.eh_frame`
augmentation data such as personality routines, ...