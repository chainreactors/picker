---
title: When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax
url: https://blog.doyensec.com/2026/05/19/cfitsio-weaponized-filenames.html
source: Over Security
date: 2026-05-19
fetch_date: 2026-05-20T06:05:10.990419
---

# When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax

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

# When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax

19 May 2026 - Posted by Adrian Denkiewicz

This research was recently presented at [BSides Luxembourg 2026](https://pretalx.com/bsidesluxembourg-2026/talk/WDFHHV/). This blogpost documents our findings presented during the talk. The BSides slides are posted [here](https://www.doyensec.com/resources/BSides-Luxembourg-2026-CFITSIO-EFS.pdf). Today, weâre also releasing the Docker-based playground utilized for the demos so anyone interested can reproduce the findings locally: [doyensec/cfitsio-efs-playground](https://github.com/doyensec/cfitsio-efs-playground).

In our [previous post](https://blog.doyensec.com/2026/04/20/cfitsio-fuzzing.html) on CFITSIO, we wrote about the AI-assisted fuzzing pipeline and the memory corruption issues found in its Extended Filename Syntax (EFS). This was only half of the story. We kept thinking that even without memory issues, EFS seems like a pretty powerful and rather risky feature. The EFS page is full of very interesting [use cases](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/filters.html). To quote some of them (emphasis mine):

> ârawfile.dat[i512,512]â: reads raw binary data array (a 512x512 short integer array in this case) and *converts it on the fly* into a temporary FITS image in memory which is *then opened* by the application program.

> âftp://heasarc.gsfc.nasa.gov/test/vela.fitsâ: FITS files in any *ftp archive site on the internet* may be opened with read-only access. Files with *HTTP addresses* may be opened in the same way.

> âmyfile.fits[EVENTS][PHA > 5]â: *creates and opens a temporary FITS files* that is identical to âmyfile.fitsâ except that the EVENTS table will only contain the rows that have values of the PHA column greater than 5. In general, any *arbitrary boolean expression using a C or Fortran-like syntax*, which mayâ¦

That surely looks promising, right?

Therefore, this post is about the next batch of findings. This time, there are no heap overflows or stack corruptions to discuss. Weâll focus on perfectly documented features, useful during file processing, but chained together to achieve some unexpected offensive primitives.

This article is not meant to criticize CFITSIOâs authors or its code. I actively use tools that depend on CFITSIO and appreciate the work behind them. What interests me here is how perfectly reasonable legacy features can become real security problems once the surrounding software and threat model change.

## Extended Filename Syntax

As demonstrated, EFS is more than a mere filename parser. It is a mini-language hidden inside a filename parameter, capable of doing very interesting stuff. To understand how it works, we have to look into the source code.

When an EFS-enabled method is used, the input string eventually reaches CFITSIOâs internal [`ffopen()` routine](https://github.com/HEASARC/cfitsio/blob/2d1b464a399ed5d7b9364a40d9b02c3d1073dfcc/cfileio.c), which runs it through EFS parsing logic before the actual file is opened. At that stage, parts of the string may be reinterpreted as a protocol, outfile clause, extension selector, or filter expression.

The implementation is *driver-based*. CFITSIO keeps a table of registered backends through [`fits_register_driver`](https://github.com/HEASARC/cfitsio/blob/2d1b464a399ed5d7b9364a40d9b02c3d1073dfcc/cfileio.c#L5331), each associated with a prefix and a set of handler functions such as `checkfile`, `open`, `create`, `seek`, `read`, and `write`. Besides standard files, CFITSIO registers handlers for things like `mem://`, `shmem://`, `http://`, `ftps://`, and even exotic variants like `ftpsmem://`, `ftpfile://`, or `ftpscompress://`.

This is why EFS can seamlessly jump between local files, memory-backed files, compressed variants, and network protocols without the caller doing anything special.

Some of those drivers may implement `write`, `create` or `seek` methods, some may not.

```
 status = fits_register_driver("ftpscompress://",
            NULL,
            mem_shutdown,
            mem_setoptions,
            mem_getoptions,
            mem_getversion,
            NULL,            /* checkfile not needed */
            ftps_compress_open,
            0,            /* create function not required */
            mem_truncate,
            mem_close_free,
            0,            /* remove function not required */
            mem_size,
            0,            /* flush function not required */
            mem_seek,
            mem_read,
            mem_write);
```

To achieve interesting primitives, we need to carefully review whatâs available and whatâs not.

## A Tiny Lab Environment

To simplify testing and demonstrating while ensuring reproducibility, we built a minimal Docker playground around CFITSIO. The container includes a tiny helper program called `fits-sample-opener`. In the insecure mode, it just calls [`fits_open_file`](https://github.com/HEASARC/cfitsio/blob/2d1b464a399ed5d7b9364a40d9b02c3d1073dfcc/cfileio.c), performs one harmless metadata query, and exits. The helper does almost nothing on purpose. If opening a file causes a network request, a local file copy, or outbound exfiltration, that behavior comes from CFITSIO itself.

That additional metadata query is there for a reason: some EFS behaviors do not fully materialize on the initial open alone. We wanted the sample application to stay minimal while still triggering side effects like a real caller that actually inspects the file it just opened.

The full environment, including the helper program, building instructions, and the fake `root://` server used later in this post, is available [here](https://github.com/doyensec/cfitsio-efs-playground).

Make sure to target the right git tag/release as EFS handling might change in the future.

## Primitive 1: Arbitrary File Copy

The first surprising behavior comes from the outfile clause. EFS supports the following formula:

```
input.fits(output.fits)
```

The meaning is roughly: work on `input.fits`, but first save a separate copy as `output.fits`.

Now, letâs use our EFS playground and replace `input.fits` with `/etc/passwd`:

```
docker run --rm -v "$(pwd)":/workspace cfitsio:4.6.3 \
  fits-sample-opener '/etc/passwd(/workspace/foo)'
```

Even though `/etc/passwd` is not a FITS file, the copy happens *before* validation fails. This is an arbitrary file copy primitive. Depending on the target environment, the attack might be followed by copying sensitive files into a web-accessible or otherwise attacker-readable location, or just breaking something to achieve denial-of-service. Of course, standard OS permissions still apply.

## Primitive 2: Forced Downloads and SSRF

If the filename starts with `http://`, `https://`, `ftp://`, or `ftps://`, CFITSIO will reach out to the remote resource and fetch it. The plain `http://` and `ftp://` paths are handled by raw socket code that has been in the tree for nearly 30 years. There was no concept of Server-Side Request Forgery back then. The TLS variants delegate to libcurl, where the request line is built by the library and is not directly attacker controlled. Either way, the same outfile clause still applies, which is what makes this interesting.

```
docker run --rm -v "$(pwd)":/workspace cfitsio:4.6.3 \
  fits-sample-opener 'https://example.com/anyfile(/workspace/grabbed.file...