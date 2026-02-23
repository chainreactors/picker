---
title: Bit-field layout
url: https://maskray.me/blog/2026-02-22-bit-field-layout
source: MaskRay
date: 2026-02-22
fetch_date: 2026-02-23T04:19:47.900851
---

# Bit-field layout

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-02-22](/blog/2026-02-22-bit-field-layout)

# Bit-field layout

The C and C++ standards leave nearly every detail to the
implementation. C23 Â§6.7.3.2:

> An implementation may allocate any addressable storage unit large
> enough to hold a bit-field. If enough space remains, a bit-field that
> immediately follows another bit-field in a structure shall be packed
> into adjacent bits of the same unit. If insufficient space remains,
> whether a bit-field that does not fit is put into the next unit or
> overlaps adjacent units is implementation-defined. The order of
> allocation of bit-fields within a unit (high-order to low-order or
> low-order to high-order) is implementation-defined. The alignment of the
> addressable storage unit is unspecified

C++ is also terse â `[class.bit]p1`:

> Allocation of bit-fields within a class object is
> implementation-defined. Alignment of bit-fields is
> implementation-defined. Bit-fields are packed into some addressable
> allocation unit.

The actual rules come from the platform ABI:

* **Itanium ABI** â used on Linux, macOS, BSD, and most
  non-Windows platforms. The Itanium C++ ABI ([section
  2.4](https://itanium-cxx-abi.github.io/cxx-abi/abi.html#class-types)) defers bit-field placement to "the base C ABI" but adds its own
  constraints (notably: bit-fields are never placed in the tail padding of
  a base class).
* System V ABI Processor Supplement. The x86-64 psABI says little
  about bit-fields, while the [AArch64
  AAPCS](https://github.com/ARM-software/abi-aa/blob/main/aapcs64/aapcs64.rst#id115) has a more detailed description.
* **Microsoft ABI** â used on Windows (MSVC). In GCC and
  Clang, structs with the `ms_struct` attribute also mimics
  this ABI.

Clang implements both ABIs in
`clang/lib/AST/RecordLayoutBuilder.cpp`. It processes
bit-fields in **two distinct phases**:

1. **Layout** (storage units) â assign a bit offset to
   every bit-field. This is ABI-specified and determines
   `sizeof` and `alignof`.
2. **Codegen** (access units) â choose what LLVM IR loads
   and stores to emit. This is a compiler optimization that affects
   generated code but not the ABI.

Understanding these separately is the key to understanding
bit-fields. This article focuses on Itanium (the default on most
platforms), with a section on how the Microsoft ABI differs.

## Phase 1: Storage Units

In `clang/lib/AST/RecordLayoutBuilder.cpp`,
`ItaniumRecordLayoutBuilder::LayoutFields` lays out fields of
a `RecordDecl`. For each bit field, it calls
`LayoutBitField` to determine the storage unit and bit
offset.

A **storage unit** is a region of `sizeof(T)`
bytes, by default aligned to `alignof(T)`. For an
`int` bit-field, that's a 4-byte region at a 4-byte-aligned
offset. The alignment can be reduced by the `packed`
attribute and `#pragma pack`.

* `StorageUnitSize = sizeof(T) * 8` â the unit's size in
  bits
* `FieldAlign = alignof(T)` in bits â the unit's alignment
  (before modifiers)
* `FieldOffset` â the first bit after the last
  bit-field

### Core Rule

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` if (FieldSize == 0 ||     (AllowPadding &&      (FieldOffset & (FieldAlign-1)) + FieldSize > StorageUnitSize))   FieldOffset = alignTo(FieldOffset, FieldAlign); ``` |

Compute where `FieldOffset` falls within its aligned
storage unit. If the remaining space is less than
`FieldSize`, round up to the next aligned boundary.
Otherwise, pack the bit-field at the current position.

### Declared Type Matters

Consider two structs that store the same total number of bits (7 + 7
+ 2 = 16) but use different declared types:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` struct U8  { uint8_t  a:7, b:7, c:2; };   // sizeof = 3 struct U16 { uint16_t a:7, b:7, c:2; };   // sizeof = 2  struct S1 { int a:14; int b:10; int c:30; };   // sizeof = 8 ``` |

**Walk-through for `U8`** (all fields have
StorageUnitSize = 8, FieldAlign = 8):

* `a` at bit 0. Position = 0, 0 + 7 = 7 <= 8. Fits.
  **Offset = 0.**
* `b` at bit 7. Position = 7, 7 + 7 = 14 > 8. Doesn't
  fit. New unit at bit 8. **Offset = 8.**
* `c` at bit 15. Position = 15 - 8 = 7, 7 + 2 = 9 > 8.
  Doesn't fit. New unit at bit 16. **Offset = 16.**

Three 1-byte storage units. `sizeof(U8) = 3`. Eight
padding bits wasted.

**Walk-through for `U16`** (all fields have
StorageUnitSize = 16, FieldAlign = 16):

* `a` at bit 0. Position = 0, 0 + 7 = 7 <= 16. Fits.
  **Offset = 0.**
* `b` at bit 7. Position = 7, 7 + 7 = 14 <= 16. Fits.
  **Offset = 7.**
* `c` at bit 14. Position = 14, 14 + 2 = 16 <= 16. Fits.
  **Offset = 14.**

One 2-byte storage unit. `sizeof(U16) = 2`. No waste.

**Walk-through for `S1`** (all fields have
StorageUnitSize = 32, FieldAlign = 32):

* `a` at bit 0. Position = 0, 14 fits in 32. **Offset
  = 0.**
* `b` at bit 14. Position = 14, 14 + 10 = 24 <= 32.
  Fits. **Offset = 14.** Bits 24â31 are padding (unfilled
  tail of the first storage unit).
* `c` at bit 24. Position = 24, 24 + 30 = 54 > 32.
  Doesn't fit. New unit at bit 32. **Offset = 32.** Bits
  62â63 are padding (unfilled tail of the second storage unit).

`sizeof(S1) = 8`, `alignof(S1) = 4`.

Note: Phase 1 uses two `int` storage units, but Phase 2 is
free to merge `a`, `b`, and `c` into a
single `i64` access unit (since there are no non-bitfield
barriers and 8 bytes fits in a register). On x86\_64, the LLVM type ends
up as `{ i64 }`.

### Mixed Types

When bit-fields have different declared types, the storage unit size
changes:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` struct S2 { int a:24; short b:8; };   // sizeof = 4 ``` |

* `a` is `int` (StorageUnitSize = 32). Placed at
  bit 0.
* `b` is `short` (StorageUnitSize = 16,
  FieldAlign = 16). Current offset = 24. Position within a 16-bit aligned
  unit: 24 % 16 = 8. 8 + 8 = 16 <= 16. Fits. **Offset =
  24.**

`sizeof(S2) = 4`. The `short` bit-field
overlaps into the `int`'s storage unit. Under Itanium,
storage units of different types *can* share bytes.

The `short` can also reuse space left by a smaller
bit-field:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` struct S2b { int a:16; short b:8; };   // sizeof = 4 ``` |

* `a` is `int` (StorageUnitSize = 32). Placed at
  bit 0.
* `b` is `short` (StorageUnitSize = 16,
  FieldAlign = 16). Current offset = 16. Position within a 16-bit aligned
  unit: 16 % 16 = 0. 0 + 8 = 8 <= 16. Fits. **Offset =
  16.**

Here `b`'s 16-bit storage unit (bits 16â31) falls entirely
within `a`'s 32-bit storage unit.

> Under Microsoft ABI, `sizeof` is 8: the type size change
> from `int` to `short` forces a new storage
> unit.

This overlapping extends to non-bit-field members too. A
non-bit-field can be allocated within the unfilled bytes of a preceding
bit-field's storage unit:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` struct S2c { uint16_t first:8; uint8_t second; };   // sizeof = 2 ``` |

* `first` is `uint16_t:8`. Placed at bit 0. Uses
  8 bits of a 16-bit storage unit (bytes 0â1).
* `second` is a non-bit-field `uint8_t`. The
  bitfield state resets, but DataSize is only 1 byte. `second`
  (alignment 1) goes at **byte 1** (bit 8) â inside
  `first`'s storage unit.

Note that this overlapping means a write to `first` via
its access unit could touch byte 1 where `second` lives.
Phase 2 must ensure the access units don't clobber each other (see [Hard constraints](#itanium-merging-algorithm)).

> Under Microsoft ABI, `sizeof` is 4: `first`
> gets a full `uint16_t` unit (2 bytes), and
> `second` starts at byte 2 instead of byte 1.

### Non-bitfield After Bitfield

When a non-bitfield field cannot fit within the remaining bytes, it
resets the bitfield state and unfilled bits become padding:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` struct ...