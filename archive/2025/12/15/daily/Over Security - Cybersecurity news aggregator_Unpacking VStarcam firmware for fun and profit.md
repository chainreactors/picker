---
title: Unpacking VStarcam firmware for fun and profit
url: https://palant.info/2025/12/15/unpacking-vstarcam-firmware-for-fun-and-profit/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-15
fetch_date: 2025-12-16T03:24:16.613506
---

# Unpacking VStarcam firmware for fun and profit

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Unpacking VStarcam firmware for fun and profit

2025-12-15
 [Security](/categories/security/)/[IoT](/categories/iot/)
 11 mins
 [0 comments](/2025/12/15/unpacking-vstarcam-firmware-for-fun-and-profit/#comments)

One important player in the [PPPP protocol business](/2025/11/05/an-overview-of-the-pppp-protocol-for-iot-cameras/) is VStarcam. At the very least theyâve already accumulated an impressive portfolio of security issues. Like [exposing system configuration including access password unprotected in the Web UI](https://github.com/Retr0-code/auth-traversal) (discovered by multiple people independently from the look of it). Or the [open telnet port accepting hardcoded credentials](https://brownfinesecurity.com/blog/vstarcam-cb73-hardcoded-root-password) (definitely discovered by lots of people independently). In fact, these cameras have been [seen used as part of a botnet](https://www.carson-saint.com/vstarcam-vulnerability-saint-blocks-eleven11bot-ddos-attacks/), likely thanks to some documented vulnerabilities in their user interface.

Is that a thing of the past? Are there updates fixing these issues? Which devices can be updated? These questions are surprisingly hard to answer. I found zero information on VStarcam firmware versions, available updates or security fixes. In fact, it doesnât look like they ever even acknowledged learning about the existence of these vulnerabilities.

No way around downloading these firmware updates and having a look for myself. With surprising results. First of all: there are *lots* of firmware updates. It seems that VStarcam accumulated a huge number of firmware branches. And even though not all of them even have an active or downloadable update, the number of currently available updates goes into hundreds.

And the other aspect: the variety of update formats is staggering, and often enough standard tools like binwalk arenât too useful. It took some time figuring out how to unpack some of the more obscure variants, so Iâm documenting it all here.

*Warning*: Lots of quick-and-dirty Python code ahead. Minimal error checking, use at your own risk!

#### Contents

* [ZIP-packed incremental updates](#zip-packed-incremental-updates)
* [VStarcam pack system](#vstarcam-pack-system)
* [VeePai updates](#veepai-updates)
* [Ingenic updates](#ingenic-updates)
  + [LZO-compressed partitions](#lzo-compressed-partitions)
  + [Ingenicâs jzlzma compression](#ingenic-s-jzlzma-compression)
  + [Exotic Ingenic update](#exotic-ingenic-update)
* [But what about these security issues?](#but-what-about-these-security-issues)

## ZIP-packed incremental updates

These incremental updates donât contain an image of the entire system, only the files that need updating. They always contain the main application however, which is what matters.

Recognizing this format is easy, the files start with the 32 bytes `www.object-camera.com.by.hongzx.` or `www.veepai.com/design.rock-peng.` (the old and the new variant respectively). The files end with the same string in reverse order. Everything in between is a sequence of ZIP files, with each file packed in its own ZIP file.

Each ZIP file is preceded by a 140 byte header: 64 byte directory name, 64 byte file name, 4 byte ZIP file size, 4 byte timestamp of some kind and 4 zero bytes. While `binwalk` can handle this format, having each file extracted into a separate directory structure isnât optimal. A simple Python script can do better:

```
#!/usr/bin/env python3
import datetime
import io
import struct
import os
import sys
import zipfile

def unpack_zip_stream(input: io.BytesIO, targetdir: str) -> None:
    targetdir = os.path.normpath(targetdir)
    while True:
        header = input.read(0x8c)
        if len(header) < 0x8c:
            break

        _, _, size, _, _ = struct.unpack('<64s64sLLL', header)
        data = input.read(size)

        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for member in archive.infolist():
                path = os.path.normpath(
                    os.path.join(targetdir, member.filename)
                )
                if os.path.commonprefix((path, targetdir)) != targetdir:
                    raise Exception('Invalid target path', path)

                try:
                    os.makedirs(os.path.dirname(path))
                except FileExistsError:
                    pass

                with archive.open(member) as member_input:
                    data = member_input.read()
                with open(path, 'wb') as output:
                    output.write(data)

                time = datetime.datetime(*member.date_time).timestamp()
                os.utime(path, (time, time))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} in-file target-dir', file=sys.stderr)
        sys.exit(1)

    if os.path.exists(sys.argv[2]):
        raise Exception('Target directory exists')

    with open(sys.argv[1], 'rb') as input:
        header = input.read(32)
        if (header != b'www.object-camera.com.by.hongzx.' and
                header != b'www.veepai.com/design.rock-peng.'):
            raise Exception('Wrong file format')
        unpack_zip_stream(input, sys.argv[2])
```

## VStarcam pack system

This format is pretty simple. There is an identical section starting with `VSTARCAM_PACK_SYSTEM_HEAD` and ending with `VSTARCAM_PACK_SYSTEM_TAIL` at the start and at the end of the file. This section seems to contain a payload size and its MD5 hash.

There are two types of payload here. One is a raw SquashFS image starting with `hsqs`. These seem to be updates to the base system: they contain an entire Linux root filesystem and the Web UI root but not the actual application. The matching application lives on a different partition and is likely delivered via incremental updates.

The other variant seems to be used for hardware running LiteOS rather than Linux. The payload here starts with a 16 byte header: compressed size, uncompressed size and an 8 byte identification of the compression algorithm. The latter is usually `gziphead`, meaning standard gzip compression. After uncompressing you get a single executable binary containing the entire operating system, drivers, and the actual application.

So far binwalk can handle all these files just fine. I found exactly one exception, [firmware version 48.60.30.22](http://doraemon-hangzhou.eye4.cn/firmware_48.60.30.22_1577170721.bin). It seems to be another LiteOS-based update but the compression algorithm field is all zeroes. The actual compressed stream has some distinct features that make it look like none of the common compression algorithms.

![Screenshot of a hexdump showing the first 160 and the last 128 bytes of a large file. The file starts with the bytes 30 c0 fb 54 and looks random except for two sequences of 14 identical bytes: ef at offset 0x24 and fb at offset 0x43. The file ending also looks random except for the closing sequence: ff ff 0f 00 00.](/2025/12/15/unpacking-vstarcam-firmware-for-fun-and-profit/mystery_compression.png)

Well, I had to move on here, so thatâs the one update file I havenât managed to unpack.

## VeePai updates

This is a format that seems to be used by newer VStarcam hardware. At offset 8 these files contain a firmware version like `www.veepai.com-10.201.120.54`. Offsets of the payload vary but it is a SquashFS image, so binwalk can be used to find and unpack it.

Normally these are updates for the partition where the VStarcam application resides in. In a few cases these are updating the Linux base system however, no application-specific files from what I could tell.

## Ingenic updates

This format seems to be specific to the Ingenic hardware platform, and Iâve seen other hardware vendors use it as well. One noticeable feature here is the presence of a `tag` partition conta...