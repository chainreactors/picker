---
title: CFITSIO Fuzzing: Memory Corruptions and a Codex-Assisted Pipeline
url: https://blog.doyensec.com/2026/04/20/cfitsio-fuzzing.html
source: Over Security - Cybersecurity news aggregator
date: 2026-04-19
fetch_date: 2026-04-20T04:56:13.540365
---

# CFITSIO Fuzzing: Memory Corruptions and a Codex-Assisted Pipeline

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# CFITSIO Fuzzing: Memory Corruptions and a Codex-Assisted Pipeline

20 Apr 2026 - Posted by Adrian Denkiewicz

Have you ever wondered how those amazing space photos are taken? Are they exclusive to the big telescopes floating in space or can you take one from your backyard? What does it take to extract hydrogen colors out of a seemingly black sky?

![Andromeda Galaxy / M31](../../../public/images/m31.jpg)

Those are great questions, but you wonât learn it from here.

Instead, Iâll show how I set up and performed fuzzing of the [CFITSIO](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/fitsio.html) library which is how those space photos are usually processed. Iâll show how the bugs were triaged at scale, and how Codex was used to unblock the fuzzing and to develop the initial security fixes.

Note: the work described in this blogpost used the GPT-5-Codex, which was the latest model I had access to at the time.

## FITS Format

The Flexible Image Transport System (FITS) is a data standard created in the late 1970s by NASA, ESA, and the broader astronomy community. It started as a way to exchange telescope imagery across heterogeneous systems, but it evolved into a container for complex datasets: primary images, binary/ASCII tables, compressed tiles, world coordinate metadata, and instrument-specific headers. Today, most observatories, satellite missions, and even backyard observatories output FITS directly, so the ecosystem of tools is rich. Under the hood, FITS is far more than a simple image file - it routinely carries gigabyte-scale mosaics, time-series cubes, and calibration tables. The current FITS standard lives in a dense [spec](https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf) and most of it addresses astronomy beyond typical astrophotography - radio, infrared, X-ray, time-series, and polarization data with all their metadata are first-class in the spec, while backyard imaging uses only a small slice. Once telescopes and CCD cameras got cheap enough for hobbyists, the community needed tooling that already worked, so adopting FITS was the obvious shortcut. The format was battle-tested and carried all the metadata serious imaging needed. Ultimately, hobbyists inherited a rather complex data format that rarely changes because backward compatibility with old files is still mandatory.

There are several different libraries that claim to support the FITS format. Usually though, that only means some subset of the spec. CFITSIO is the most complete implementation and the library is used by [numerous great pieces of astronomy software](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/major_users.html), therefore it piqued my interest.

For my fuzzing corpus, Iâve used some of my own astrophotos along with several [public samples](https://fits.gsfc.nasa.gov/fits_samples.html). Iâm sure the coverage could be vastly improved with the right set of specialized data.

## First Round: Generic Fuzzing

Initially, I began fuzzing using the standard AFL++ workflow. Harness code, testing corpus, some optimizations, with several sessions running over two weeks. This resulted in a [security advisory](https://www.doyensec.com/resources/Doyensec_Advisory_CFITSIO_Q22025.pdf) consisting of six different bugs.

It was a quick experiment to see how fruitful the fuzzing could be and how the communication with the NASA team works. Fortunately, the cooperation was great and issues were quickly addressed by the HEASARC team.

## Second Round: EFS

Having the setup ready to go, I decided to give it another shot. Testing was performed against cfitsio-4.6.3 which included fixes to previously reported issues. This time, I focused exclusively on the [Extended Filename Syntax (EFS)](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/filters.html) which got my interest earlier. Itâs a set of filters, enclosed in square brackets, that can be used to modify the raw file in various ways before it is opened and read by the application. Although EFS looks like a filename parser on the surface, itâs effectively a mini-language: image slicing, histogram generation, filters, pixel expressions, region filtering, arithmetic expressions, and the entire parser stack behind them.

An example FITS filename can look like this: `myfile.fits[EVENTS][col Rad = sqrt(X**2 + Y**2)]`

This opens a FITS file, selects the EVENTS extension, and creates a new column computed from existing data. The library does all of that before the application sees a single byte. The filename alone triggers extension lookup, column arithmetic, and a temporary file copy. Each bracket pair activates a different parser subsystem inside CFITSIO.

This represents a very interesting attack surface and itâs exposed in more places than people might think. Many applications accept filenames directly from external callers without realizing that CFITSIO will interpret them through EFS if only the `fits_open_file` or similar method is called (a non-EFS alternative: `fits_open_diskfile` also exists). If those filenames come from untrusted input, the attack path is open.

This time, as I didnât have too much dedicated time, Iâve strongly relied on help from the GPT/Codex. First, it generated the harness code and some helpful cleanup utilities. The harness itself is minimal: it reads a filename string from a file, passes it to `fits_open_file` in read-only mode, then exits. Thatâs enough to exercise the entire EFS parsing and evaluation pipeline (or most of it, as I learned later), without needing complex application logic.

Early fuzzing cycles not only resulted in a lot of crashes, but also unexpected files created all over the filesystem and with the input FITS file being repeatedly destroyed. This wasnât hard to fix though. I then asked GPT to look at the spec and the code and create a dictionary tailored to EFS tokens.

Within hours I had some clean crashes. This was nothing surprising given how much logic CFITSIO runs before it ever opens a file. Some days later, I ran [AFLtriage](https://github.com/quic/AFLTriage) and observed that there are just three different bugs responsible for all crashes I was seeing. The fuzzer couldnât move on any further and coverage also barely moved. Even relatively simple code paths were unreachable with random mutations constantly hitting the same shallow error paths.

To keep going, I had to automate more of the workflow. Thatâs when I brought in Codex again.

## Workflow Improvements

I loaded the CFITSIO/harness sources into Codex and fed it the crash reports along with the input files. Within seconds, it identified the root cause of each issue. It also gave me correct functions, correct offsets, correct control flow, and assumptions that failed. It pointed to actual logic errors, such as operator-precedence mistakes, unchecked token lengths or unbounded concatenations. I was surprised how fast and accurate the analysis was.

The next step involved asking for the patch and applying it. This completely unblocked my fuzzing. I restarted the process using the old output directory with a new harness build andâ¦ left it running.

Two weeks later, I had to stop the fuzzing and started investigating. AFLtriage again was very useful to quickly identify unique crashes. Learning from past experience, I went with Codex as my assistant again. After a few manual experiments I automated the following pipeline:

...