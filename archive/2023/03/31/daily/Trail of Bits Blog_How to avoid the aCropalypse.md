---
title: How to avoid the aCropalypse
url: https://blog.trailofbits.com/2023/03/30/acropalypse-polytracker-blind-spots/
source: Trail of Bits Blog
date: 2023-03-31
fetch_date: 2025-10-04T11:13:57.566232
---

# How to avoid the aCropalypse

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How to avoid the aCropalypse

Henrik Brodin

March 30, 2023

[program-analysis](/categories/program-analysis/), [research-practice](/categories/research-practice/)

## The aCropalypse is upon us!

Last week, news about CVE-2023-21036, nicknamed the “[aCropalypse](https://www.da.vidbuchanan.co.uk/blog/exploiting-acropalypse.html),” spread across [Twitter](https://twitter.com/ItsSimonTime/status/1636857478263750656) and other media, and I quickly realized that the underlying flaw could be detected by our tool, [PolyTracker](https://github.com/trailofbits/polytracker). I’ll explain how PolyTracker can detect files affected by the vulnerability even without specific file format knowledge, which parts of a file can become subject to recovery using [acropalypse.app](https://acropalypse.app/), and how Google and Microsoft could have caught this bug by using our tools. Coincidentally, my colleagues, Evan Sultanik and Marek Surovič, and I [wrote a paper](https://arxiv.org/abs/2301.08700) that describes this class of bugs, defines a novel approach for detecting them, and introduces our implementation and tooling. It will appear at this year’s workshop on Language-Theoretic Security ([LangSec](https://langsec.org/spw23/)) at the IEEE Security and Privacy Symposium.

We use PolyTracker to instrument the image parser, `libpng`. (Any parser will do, not just aCropalyptic ones.) The PolyTracker instrumentation tells us which portions of the input file are completely ignored by the parser, which we call *blind spots*. Blind spots are almost always indicators of design flaws in the file format, malformation in the input file, and/or a bug in the parser. Normal images should have almost no blind spots, but parsing malformed aCropalyptic images through `libpng` reveals the cropped data in a large blind spot. The aCropalypse bugs could have been caught if the vulnerable products had been instrumented with PolyTracker and their output tested for blind spots.

[![](/img/wpdump/646f5cdf68158456ebd6beb5c4a96dfd.png)](/img/wpdump/646f5cdf68158456ebd6beb5c4a96dfd.png)

```
# parse the screenshot with an instrumented version of pngtest
$ ./pngtest.instrumented re3eot.png.png out_re3eot.png.png
# ask polytracker to identify any blindspots in the file
$ polytracker cavities polytracker.tdag
Re3eot.png,697120,1044358
# found a blind spot starting at offset 697120 (size ~300KiB), it is ignored and contains the cropped out image data that could be retrieved
```

## Understanding the aCropalypse

According to [this tweet](https://twitter.com/ItsSimonTime/status/1636857478263750656), it is possible to recover parts of an original image from a cropped or redacted screenshot. The TL;DR is that when the Google Pixel built-in screenshot editing tool, Markup, is used to crop or resize an image, it overwrites the original image, but only up to the offset where the new image ends. Any data from the original image after that offset is left intact in the file. David Buchanan devised an algorithm to recover the original image data still left in the file; you can read more about the specifics on [his blog](https://www.da.vidbuchanan.co.uk/blog/exploiting-acropalypse.html).

[![](/img/wpdump/0c62c614297e4dcabd39207441eabae1.png)](/img/wpdump/0c62c614297e4dcabd39207441eabae1.png)

More recently, Chris Blume identified a similar vulnerability for the Windows Snipping Tool. The methodology we describe here for the Markup tool can be used on images produced by the Windows Snipping Tool.

PolyTracker has a feature we introduced a couple of years ago called *blind spot detection*. We define *blind spots* as the set of input bytes whose data flow never influences either the control flow that leads to an output or an output itself. Or, in layman’s terms, *unused file data that can be altered to have any content without affecting the output*. The cropped-out regions of an aCropalypse image are, by definition, blind spots, so PolyTracker should be able to detect them!

One of the challenges of tracking input bytes and detecting blind spots for real-world inputs like PNG images or PDF documents is *taint explosion*. The PNG file format contains compressed chunks of image data. Compression is especially keen on contributing to taint explosion as input bytes combine in many ways to produce output bytes. PolyTracker’s unique representation of the taint structure allows us to track 2^31 unique taint labels, which is necessary for analyzing taints propagated during [zlib](https://zlib.net/)-decompression of image data.

## aCropalyptic files will have Blind Spots when processed

To understand why the aCropalypse vulnerability produces blind spots, we need to combine our knowledge of the vulnerability with the description of blind spots. When parsing a PNG file with a PNG parser, the parser will interpret the header data and consume chunks according to the PNG specification. In particular, it will end at a chunk with type IEND, even if that is not at the actual end of the file.

We use PolyTracker to [instrument a tool](https://github.com/trailofbits/polytracker/blob/acropalypse/examples/Dockerfile-acropalypse.demo) (pngtest from the [libpng](https://libpng.sourceforge.io/) project) that reads PNG files and writes them to disk again. This will produce an additional output file, called `polytracker.tdag`, that captures the data flow from the runtime trace. Using that file and PolyTracker’s blind spot detection feature, we can enumerate the input bytes that do not affect the resulting image. Remember, these are the bytes of the input file that neither affect any control flow, nor end up (potentially mixed with other data) in the output file. They have no actual meaning in interpreting the format for the given parser.

## Show me!

Using the PolyTracker-instrumented `pngtest` application, we load, parse, and then store the below image to disk again. During this processing, we track all input bytes through PNG and zlib processing until they eventually reach the output file in some form.

[![](/img/wpdump/646f5cdf68158456ebd6beb5c4a96dfd.png)](/img/wpdump/646f5cdf68158456ebd6beb5c4a96dfd.png)

We use a [Docker image](https://github.com/trailofbits/polytracker/blob/acropalypse/examples/Dockerfile-acropalypse.demo) containing the PolyTracker instrumented pngtest application.

```
$ docker run -ti --rm -v $(pwd):/workdir acropalypse
$ cd /workdir
$ /polytracker/acropalypse/libpng-1.6.39/pngtest.instrumented re3eot.png.png out_re3eot.png.png
```

The `re3eot.png` image is 1044358 bytes in size, whereas the `out_re3eot.png` is 697,182 bytes. Although this indicates a fairly large reduction in size, at this point we can’t tell why; it could, for example, be the result of different compression settings.

Next, let’s find the blind spots from this process:

```
$ polytracker cavities polytracker.tdag

100%|███████████████████| 1048576/1048576 [00:01<00:00, 684922.43it/s]
re3eot.png,697120,1044358
out_re3eot.png,37,697182
```

The output we are interested in is:

```
re3eot.png,697120,1044358
```

This tells us that the data starting from offset 697,120 to the end of the file was ignored when producing the output image. We have found a blind spot! The additional 347,238 bytes of unused data could be left from an original image—an indication of the aCropalypse vulnerability. Let’s use the [acropalypse.app](https://acropalypse.app/) web page to see if we can recover it.

[![](/img/wpdump/9178517825282e8a56caee6a1ee351d8.png)](/img/wpdump/9178517825282e8a56caee6a1ee351d8.png)

This indicates that the file was in fact produced by the vulnerable application. At this point, we know that the image contains data from the original image at the end, as that is the core of the vulnerability. We also know the exact location and extent of that data (according to the blind spot’s starting offset and size...