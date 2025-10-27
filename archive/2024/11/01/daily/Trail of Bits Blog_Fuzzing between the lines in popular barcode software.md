---
title: Fuzzing between the lines in popular barcode software
url: https://blog.trailofbits.com/2024/10/31/fuzzing-between-the-lines-in-popular-barcode-software/
source: Trail of Bits Blog
date: 2024-11-01
fetch_date: 2025-10-06T19:17:07.635791
---

# Fuzzing between the lines in popular barcode software

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Fuzzing between the lines in popular barcode software

Artur Cygan

October 31, 2024

[application-security](/categories/application-security/), [fuzzing](/categories/fuzzing/)

Page content

* [Assessing the project’s fuzzing state](#assessing-the-projects-fuzzing-state)
* [Instrumenting the build](#instrumenting-the-build)
* [How to identify the target](#how-to-identify-the-target)
  + [Diagnosing crashes](#diagnosing-crashes)
  + [Putting it all together](#putting-it-all-together)
* [Lessons learned](#lessons-learned)

Fuzzing—one of the most successful techniques for finding security bugs, consistently featured in articles and industry conferences—has become so popular that you may think most important software has already been extensively fuzzed. But that’s not always the case. In this blog post, we show how we fuzzed the ZBar barcode scanning library and why, despite our limited time budget, we found serious bugs: an out-of-bounds stack buffer write that can lead to arbitrary code execution with a malicious barcode, and a memory leak that can be used to perform a denial-of-service attack.

ZBar is an open-source library for reading barcodes written in C. It supports an impressive number of barcode formats, including QR codes. One of our clients used it, so we wanted to quickly assess its security. Given the extensive amount of code, manual review was not an option. Since we noticed no public mention of fuzzing, we decided to give it a shot.

## Assessing the project’s fuzzing state

You might ask: how do you know whether or not software has been fuzzed? Although there’s no definitive answer to this question, it’s possible to make some educated guesses. First, we can check the repository for any mention of fuzzing, including searching issues, pull requests, and the code itself. For instance, [this issue](https://github.com/mchehab/zbar/issues/233) proposes a fuzzing harness, but it was likely never run. Second, we can check [the oss-fuzz projects](https://github.com/google/oss-fuzz/tree/master/projects). If the project is fuzzed with oss-fuzz, it’s worth checking if the fuzzing harnesses are targeting the functionality we’re interested in and whether the project actually works. We observed cases where project builds were failing for months and were not actively fuzzed. Similarly to the project’s repository, oss-fuzz issues and pull requests can contain interesting information. Developers expressed [some interest](https://github.com/google/oss-fuzz/issues/3863) in bringing ZBar to oss-fuzz, but this was ultimately abandoned.

By this point we knew two things about ZBar: it was barely fuzzed (or not fuzzed at all), and we identified starting points for creating our own fuzzing campaign.

## Instrumenting the build

To fuzz ZBar, it has to be built with sanitizer and fuzzer instrumentation. Building an unfamiliar project can be a time-consuming challenge on its own, and adding instrumentation for fuzzing often makes this task even more difficult. For that reason, it’s useful to take an existing build and tweak it. Fortunately, ZBar is already [packaged in Nixpkgs](https://github.com/NixOS/nixpkgs/blob/011567f35433879aae5024fc6ec53f2a0568a6c4/pkgs/tools/graphics/zbar/default.nix), so we could quickly modify the build:

```
zbar-instrumented = with pkgs; (zbar.override {
  stdenv = clang16Stdenv;
}).overrideAttrs (orig: {
  buildInputs = orig.buildInputs ++ [ llvmPackages_16.openmp ];
  dontStrip = true;
  doCheck = false; # tests started failing with sanitizers
  CFLAGS = "-g -fsanitize=address,fuzzer-no-link";
  LDFLAGS = "-g -fsanitize=address,fuzzer-no-link";
});
```

Figure 1: Instrumenting ZBar for fuzzing

Nix packages are described with the Nix programming language and can be easily manipulated in various ways. In the case above, we use override to modify [inputs](https://github.com/NixOS/nixpkgs/blob/011567f35433879aae5024fc6ec53f2a0568a6c4/pkgs/tools/graphics/zbar/default.nix#L1-L30) defined by the package where we set the package’s compiler to Clang (otherwise, GCC is used by default). The following `overrideAttrs` function is a free-form override that allows us to modify anything we want. With `overrideAttrs`, we add the missing `openmp` dependency, disable stripping so that debug build works properly, and disable the tests. Finally, we add the instrumentation compiler and linker flags for AddressSanitizer and libFuzzer. If you’re unfamiliar with the instrumentation flags, our [AppSec Testing Handbook](https://appsec.guide/) has excellent [guidance](https://appsec.guide/docs/fuzzing/c-cpp/libfuzzer/).

Obviously, Nix is not the only answer to this problem. Depending on the software and packaging, tweaking existing packages might be more difficult. However, we highly recommend trying it out, as we found it to be often the quickest way to achieve the goal.

## How to identify the target

After preparing the instrumentation, we need to identify the fuzzing target. This part heavily depends on the project and can be non-trivial. Luckily, in ZBar the target was quite obvious: the function that takes an image and decodes barcode data from it. At this point there are a few questions to answer. How big should the image be? By default, ZBar tries to read all the known code types. Should we configure the scanner to specific codes or just try them all at once? We think it’s important not to overthink this and start with *something* to see how it performs. We started with the following harness, based on [the official example](https://github.com/ZBar/ZBar/blob/854a5d97059e395807091ac4d80c53f7968abb8f/examples/scan_image.c#L65-L104):

```
#include <stdio.h>
#include <stdlib.h>
#include <zbar.h>

using namespace zbar;

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, uint32_t size) {
  int width = 16, height = 16;
  if (size != width*height) return 1;

  zbar_image_t *image = zbar_image_create();
  if(!image)
    return 0;

  zbar_image_set_size(image, width, height);
  zbar_image_set_format(image, zbar_fourcc('Y', '8', '0', '0'));
  zbar_image_set_data(image, data, size, NULL);

  /* create a reader */
  zbar_image_scanner_t *scanner = zbar_image_scanner_create();

  /* configure the reader */
  zbar_image_scanner_set_config(scanner, (zbar_symbol_type_t)0, ZBAR_CFG_ENABLE, 1);
  zbar_scan_image(scanner, image);

  /* clean up */
  zbar_image_destroy(image);
  zbar_image_scanner_destroy(scanner);
  return 0;
}
```

Figure 2: Initial testing harness

In this harness, we essentially modified the sample to take the input image from the fuzzer and locked it down to a 16-by-16 pixel square
(8 bits per pixel). Running this harness resulted in one `LeakSanitizer` crash reporting a memory leak. Because
`libFuzzer` stops at the first crash, we disabled the memory leak detection with `-detect_leaks=0` and continued
fuzzing. After a while, the coverage gains appeared to stall, so we decided to enlarge the input image to 32-by-32 pixels. Surprisingly, libFuzzer struggled to figure out that input should be of size 1024 and couldn’t start fuzzing. Even tweaking the `max_len` and `len_control` options didn’t help. we managed to kickstart fuzzing by manually passing a seed input of the right size:

```
head -c 1024 /dev/zero > seed
./result/bin/zbar-fuzz -detect_leaks=0 -seed_inputs=seed
```

Figure 3: Manually passing the seed input

After this, the fuzzer was able to quickly find another crash from AddressSanitizer caused by a stack buffer overflow. If you paid attention to the ZBar instrumentation code, we mentioned in the comment that its tests are disabled due to sanitizer failure. It turned out the failure during tests wasn’t a false positive and concerned the same bug the fuzzer discovered.

Even with this simple approach, we managed to find some bugs in the library. However, with more time, we could have made a numb...