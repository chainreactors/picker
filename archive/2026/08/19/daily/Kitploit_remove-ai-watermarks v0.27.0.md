---
title: remove-ai-watermarks v0.27.0
url: https://kitploit.com/en/posts/github-wiltodelta-remove-ai-watermarks-v0270
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:30.595289
---

# remove-ai-watermarks v0.27.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F7369%2F52f57016c303fee2abf64a36db9550333e29b342701c1bf3c7f2e464e61c8df9.png&w=3840&q=75)

New releaseAug 19, 2026

# remove-ai-watermarks v0.27.0

Remove visible and invisible AI watermarks and provenance metadata from images and video. Python library and CLI for SynthID, C2PA, EXIF, IPTC, XMP, and common generative-AI marks.

Share

# Remove AI Watermarks

Remove AI provenance marks from images and video you generated yourself:

* known visible labels such as the Gemini sparkle and vendor text marks;
* invisible pixel watermarks through diffusion regeneration;
* C2PA, EXIF, XMP, IPTC, and related AI metadata.

Video support covers provenance identification, complete visible-plus-metadata
cleaning, directory batches, visible Sora, Veo, Seedance, Dola, Hailuo, and
Kling mark removal, and oracle-certified VAE regeneration for video SynthID
removal.

> Try it online at [raiw.cc](https://raiw.cc) if you do not want to install Python
> or run diffusion models locally.

[![PyPI](https://img.shields.io/pypi/v/remove-ai-watermarks?logo=pypi&logoColor=white)](https://pypi.org/project/remove-ai-watermarks/)
[![Python](https://img.shields.io/pypi/pyversions/remove-ai-watermarks?logo=python&logoColor=white)](https://pypi.org/project/remove-ai-watermarks/)
[![Downloads](https://static.pepy.tech/badge/remove-ai-watermarks/month)](https://pepy.tech/project/remove-ai-watermarks)
[![License](https://img.shields.io/pypi/l/remove-ai-watermarks?color=blue)](LICENSE)
[![Tests](https://github.com/wiltodelta/remove-ai-watermarks/actions/workflows/test.yml/badge.svg)](https://github.com/wiltodelta/remove-ai-watermarks/actions/workflows/test.yml)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/wiltodelta)

> This project is for lawful use on content you own. It does not target stock
> agency previews or other watermarks that protect third party paid content.
> See [scope, safety, and legal notes](https://github.com/wiltodelta/remove-ai-watermarks/blob/HEAD/docs/legal-and-safety.md).

## Choose what you want to do

| Goal | Command | GPU |
| --- | --- | --- |
| Find provenance signals and watermarks | `identify` | No |
| Remove known visible AI marks | `visible` | No |
| Erase a region you select | `erase` | No |
| Strip AI metadata | `metadata` | No |
| Identify supported video provenance | `video identify` | No |
| Remove visible marks and AI metadata from video | `video all` | No |
| Strip AI metadata from video | `video metadata` | No |
| Remove a registered visible AI mark from video | `video visible` | No |
| Process a directory of videos | `video batch` | Depends on mode |
| Remove video SynthID with the certified VAE profile | `video invisible` | Recommended |
| Regenerate an image to disrupt invisible watermarks | `invisible` | Required (CUDA) |
| Run visible, invisible, and metadata removal | `all` | Recommended |
| Process a directory | `batch` | Depends on mode |

## Installation modes

| Need | Install |
| --- | --- |
| Metadata inspection and stripping | `remove-ai-watermarks` |
| Visible detection and removal | `remove-ai-watermarks[visible]` |
| Visible video processing | `remove-ai-watermarks[video]` |
| Video SynthID removal | `remove-ai-watermarks[video,diffusion]` |
| Torch-free DWT-DCT detection | `remove-ai-watermarks[detect]` |
| Invisible image removal (needs CUDA) | `remove-ai-watermarks[qwen-zimage]` |
| Every production feature | `remove-ai-watermarks[all]` |

Lower-level and specialized extras include `pixels`, `heif`, `trustmark`,
`migan`, `lama`, and `diffusion`. The
[installation guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/HEAD/docs/installation.md#feature-extras) documents their exact
dependency composition and model requirements.

## Quick start

Install the metadata-focused default CLI:

root@kitploit:~

```
uv tool install remove-ai-watermarks
```

Inspect an image:

root@kitploit:~

```
remove-ai-watermarks identify image.png
```

For visible watermark removal, install the pixel dependencies:

root@kitploit:~

```
uv tool install --force "remove-ai-watermarks[visible]"
```

Then remove a known visible mark and AI metadata:

root@kitploit:~

```
remove-ai-watermarks visible image.png -o clean.png
```

Strip metadata without running visible inpainting or diffusion:

root@kitploit:~

```
remove-ai-watermarks metadata image.png --remove -o clean.png
```

Without `-o` this command overwrites the source in place.

Inspect or remove AI metadata from an MP4, MOV, M4V, WebM, MKV, AVI, or FLV
file:

root@kitploit:~

```
remove-ai-watermarks video metadata input.mp4 --check
remove-ai-watermarks video metadata input.mp4 --remove -o clean.mp4
```

The `video metadata` command does not transcode video or audio streams. Unlike
the image command above, when `-o` is omitted it writes `<source>_clean` and
preserves the original. MP4 and MOV
inspection includes the native TC260 `AIGC` tag in
`moov.udta.meta.keys/ilst`, including a `moov` placed after the media payload.
MKV and WebM inspection reads the normative
`Segment.Tags.Tag.SimpleTag` placement. AVI uses `LIST/INFO/AIGC`, while FLV
uses `script.onMetaData.AIGC`. The non-ISOBMFF formats are remuxed with stream
copy for removal.

Use the product-oriented video path to identify or clean a file:

root@kitploit:~

```
uv tool install --force "remove-ai-watermarks[video]"
remove-ai-watermarks video identify input.mp4
remove-ai-watermarks video all input.mp4 -o clean.mp4
```

`video all` removes a stable registered visible mark when present and always
strips verified AI metadata. If neither signal is found, it still writes a
same-container passthrough, so application callers get one predictable output
contract. Proprietary invisible-video removal is excluded by default.
`--invisible` opts into the lossy, oracle-certified video SynthID profile.

Process a directory with the same contract:

root@kitploit:~

```
remove-ai-watermarks video batch ./videos --mode all
```

Remove a supported visible video mark:

root@kitploit:~

```
remove-ai-watermarks video visible input.mp4 -o clean.mp4
remove-ai-watermarks video visible veo.mp4 --mark veo -o veo_clean.mp4
remove-ai-watermarks video visible seedance.mp4 --mark seedance -o seedance_clean.mp4
remove-ai-watermarks video visible dola.mp4 --mark dola -o dola_clean.mp4
remove-ai-watermarks video visible hailuo.mp4 --mark hailuo -o hailuo_clean.mp4
remove-ai-watermarks video visible kling.mp4 --mark kling -o kling_clean.mp4
```

This path scans the complete sequence before changing pixels. It accepts only a
mark that repeats at a stable position across adjacent frames, then reuses the
same OpenCV, MI-GAN, or LaMa fill backends as image removal. Audio is copied
without re-encoding and is allowed to reach its natural end; the video stream
is transcoded because its pixels change. By default, a guarded optical-flow
pass motion-aligns the preceding accepted fill and blends it only when the
nearby source context agrees; use `--no-temporal-consistency` to disable it.
The encoder preserves supported
8-bit source chroma sampling, color tags, and MP4/MOV track timescale instead
of relying on ffmpeg's implicit raw-BGR defaults. Variable frame intervals are
preserved through a timestamped in-memory NUT bridge instead of being flattened
to the average frame rate. Non-zero source start timestamps are retained
together with the copied audio offset. The default `--mark auto`
scans all providers in one decode pass and selects the first stable match in
the specifi...