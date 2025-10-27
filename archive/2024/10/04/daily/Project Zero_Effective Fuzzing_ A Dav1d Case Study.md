---
title: Effective Fuzzing: A Dav1d Case Study
url: https://googleprojectzero.blogspot.com/2024/10/effective-fuzzing-dav1d-case-study.html
source: Project Zero
date: 2024-10-04
fetch_date: 2025-10-06T18:50:50.700632
---

# Effective Fuzzing: A Dav1d Case Study

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, October 3, 2024

### Effective Fuzzing: A Dav1d Case Study

Guest post by Nick Galloway, Senior Security Engineer, 20% time on Project Zero

Late in 2023, while working on a 20% project with Project Zero, I found an integer overflow in the [dav1d](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d&sa=D&source=editors&ust=1727869833018829&usg=AOvVaw0OeT8v646Gvjwd0m7jBsCT) AV1 video decoder. That integer overflow leads to an out-of-bounds write to memory. Dav1d 1.4.0 [patched](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/commit/2b475307dc11be9a1c3cc4358102c76a7f386a51&sa=D&source=editors&ust=1727869833019194&usg=AOvVaw3804XIY0C7CGB-UUn5NwNA) this, and it was assigned [CVE-2024-1580](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2502&sa=D&source=editors&ust=1727869833019361&usg=AOvVaw2q-_2_XpPz6efrZdkggxY_). After the disclosure, I received some questions about how this issue was discovered, since dav1d is already being fuzzed by at least [oss-fuzz](https://www.google.com/url?q=https://github.com/google/oss-fuzz&sa=D&source=editors&ust=1727869833019505&usg=AOvVaw1deHOW6xxNlIZyxGlGjMct). This blog post explains what happened. It’s a useful case study in how to construct fuzzers to exercise as much code as possible. But first, some background...

# Background

## Dav1d

[Dav1d](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d&sa=D&source=editors&ust=1727869833020012&usg=AOvVaw1NMeiqpYWceoZIYBeSFatd) is a highly-optimized AV1 decoder. [AV1](https://www.google.com/url?q=https://en.wikipedia.org/wiki/AV1&sa=D&source=editors&ust=1727869833020113&usg=AOvVaw1ETEEXIx_hheFr4FUEaMVU) is a royalty-free video coding format developed by the Alliance for Open Media, and achieves improved data compression compared to older formats. AV1 is [widely supported](https://www.google.com/url?q=https://caniuse.com/av1&sa=D&source=editors&ust=1727869833020194&usg=AOvVaw3h5W2dCTCZKbFY_sl8V3t0) by web browsers, and a significant parsing vulnerability in AV1 decoders could be used as part of an attack to gain remote code execution. In the right context, where AV1 is parsed in a received message, this could allow a 0-click exploit. Testing some popular messaging clients by sending AV1 videos and AVIF images (which uses the AV1 codec) yielded the following results:

* AVIF images are displayed in iMessage
* AVIF images are NOT displayed in Android Messages when sent as an MMS
* AVIF images are displayed in Google Chat
* AV1 videos are not immediately displayed in Google Chat, but can be downloaded by the receiver and eventually can be played after being downscaled

Dav1d is written primarily in C and notably has different code paths for different architectures. There are x86, x86-64, ppc, riscv, arm32, and arm64 code paths in the repository, most of these containing optimized assembly. As noted in their roadmap, support for some of these is ongoing work, but at least ARMv7, ARMv8, and x86-64 have been thoroughly tested in the field. Based on this being a library written in C and assembly, as well as dav1d’s ubiquitous support in web browsers, I might expect it already has excellent fuzzing coverage from multiple sources.

## The integer overflow

The full details, including two proof-of-concepts that can be used to reproduce the vulnerability, are available from the [project zero bug tracker](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2502&sa=D&source=editors&ust=1727869833021191&usg=AOvVaw2827Z5-pyHnolJPIQLVAmh). The short explanation is that when multiple decoding threads are used, a signed 32-bit integer overflow can occur when calculating the values to put in the tile start offset array. In the excerpt below, the addition overflows:

|  |
| --- |
| f->frame\_thread.tile\_start\_off[tile\_idx++] = row\_off + b\_diff \*    f->frame\_hdr->tiling.col\_start\_sb[tile\_col] \* f->sb\_step \* 4; |

These overflowed values in tile\_start\_off are then passed to setup\_tile():

|  |
| --- |
| setup\_tile(&f->ts[j], f, data, tile\_sz, tile\_row, tile\_col++,                         c->n\_fc > 1 ? f->frame\_thread.tile\_start\_off[j] : 0); |

The tile\_start\_off parameter to setup\_tile() is from f->frame\_thread.tile\_start\_off[j] above, and used to calculate values for several pointers. (Note that pal\_idx, cbi, and cf are pointers in the frame\_thread struct, [as can be seen in internal.h](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/1.3.0/src/internal.h?ref_type%3Dtags%23L283&sa=D&source=editors&ust=1727869833024329&usg=AOvVaw3zyAYRiEcvv-Yy85_lc6L9).

|  |
| --- |
| static void setup\_tile(Dav1dTileState \*const ts,                         const Dav1dFrameContext \*const f,                         const uint8\_t \*const data, const size\_t sz,                         const int tile\_row, const int tile\_col,                         const int tile\_start\_off)  ...         ts->frame\_thread[p].pal\_idx = f->frame\_thread.pal\_idx ?              &f->frame\_thread.pal\_idx[(size\_t)tile\_start\_off \* size\_mul[1] / 8] :              NULL;          ts->frame\_thread[p].cbi = f->frame\_thread.cbi ?              &f->frame\_thread.cbi[(size\_t)tile\_start\_off \* size\_mul[0] / 64] :              NULL;          ts->frame\_thread[p].cf = f->frame\_thread.cf ?              (uint8\_t\*)f->frame\_thread.cf +                  (((size\_t)tile\_start\_off \* size\_mul[0]) >> !f->seq\_hdr->hbd) :              NULL; |

Those pointers are later written to, resulting in an out of bounds write to memory. Two test cases are provided with the bug, the first of which (poc1.obu) will result in an address which is outside the valid range of addresses, and so might not be exploitable. The other test case (poc2.obu) enables high bit depth mode and so has higher memory requirements, but results in pointers that are within the normal range of addresses, and so is more likely to be useful in an exploit.

## Fuzzing Space Definition

A fuzzer’s success is typically measured by “coverage”, where the fuzz target's execution is traced to examine which lines of assembly code have been covered. When I talk about the “fuzzing space”, I specifically mean space in the sense of a [mathematical space](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Space_(mathematics)&sa=D&source=editors&ust=1727869833031893&usg=AOvVaw0_mQO6SzJFsxVzIRqaI_Ph), where the set of lines of code that are executed by a given set of test cases is something we would like to maximize. In other words, a good fuzzer will execute as many lines of code as possible with the smallest possible set of test cases. To fully define the space we would also consider the fuzzing engine that generates test cases, the initial seed corpus, and the various configurations and architectures supported by the code to be fuzzed.

# Modified Dav1d Fuzzer

The dav1d fuzzer in oss-fuzz at the time I was looking at dav1d is [visible on GitHub](https://www.google.com/url?q=https://github.com/google/oss-fuzz/tree/dc543015c47f5efe6a23fa9d555a10c20ec531bf/projects/dav1d&sa=D&source=editors&ust=1727869833032315&usg=AOvVaw1rCRY6jwO3dC0odT9NmnTM). This contains build instructions and a dockerfile for oss-fuzz to run this at scale. The fuzzer implementation is in the dav1d source repository. The [meson.build file](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/8ddb28e5a726f185186c7bbd749ca3499c639c15/tests/libfuzzer/meson.build&sa=D&source=editors&ust=1727869833032482&usg=AOvVaw2JbV-f3E9v_VebU3Loe3dI) shows a couple of configurations, one for building dav1d\_fuzzer and the other for building dav1d\_fuzzer\_mt, which additionally defines DAV1D\_MT\_FUZZING.

The fuzzing code is written in C, found in [dav1d\_fuzzer.c](https://www.goo...