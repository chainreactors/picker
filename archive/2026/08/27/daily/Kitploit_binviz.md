---
title: binviz
url: https://kitploit.com/en/tools/github/karankantaria/binviz
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:41.209030
---

# binviz

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/karankantaria/binviz

![](https://assets.kitploit.com/production/public/tools/53209/d77df4e6a92791a7b4577f9bfad1ff5b8691e6a2f5b6758b7bf756630f96441e-display-v1.webp)

[Static Analysis](/en/categories/static-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Forensics](/en/categories/forensics)[Fuzzing](/en/categories/fuzzing)[Malware Analysis](/en/categories/malware-analysis)[Binary Analysis](/en/categories/binary-analysis)[Learning & Education](/en/categories/education)

![GitHub](/providers/github.png)karankantaria/binviz

# binviz

Binary visualiser and triage tool — entropy, byte-class and Hilbert surfaces, dot plots and control-flow graphs over one shared address-space model.

[View Repository](https://github.com/karankantaria/binviz)

3391 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

[Website](https://pypi.org/project/binviz/)

Share

# binviz

Binary visualiser & triage tool: linked interactive views (entropy, histograms,
image/dot-plot surfaces, control-flow graphs) over a single shared
address-space model.

root@kitploit:~

```
pipx install binviz && binviz serve
```

## What it does

Open a file and every view is looking at the same address space. Select a range
in one and the rest follow — the point is to answer "what is this region" by
looking at it several ways at once.

* **Map it.** `binviz model` parses ELF/PE/Mach-O through LIEF into regions,
  symbols and an offset↔virtual-address mapping, materialising gaps and
  overlays. Malformed input falls back to a raw model rather than failing.
* **Find the parts worth looking at.** Windowed entropy and other named
  signals, byte-class and Hilbert surfaces, and window classification against
  thresholds *measured* from a ground-truth corpus rather than picked
  (ARCHITECTURE.md §2.1). Packed, encrypted, code and padding do not look alike.
* **Identify an encoding.** Bigram and sparse-trigram histograms, a dot plot
  for repeats and self-similarity, and an image view over 15 packed pixel
  formats and 24 Bayer modes — with a stride suggester, because the wrong row
  stride turns a photograph into diagonal noise and you conclude there is no
  photograph.
* **Read the code.** Capstone decode by linear sweep and recursive descent
  (differentially tested against objdump), a five-tier function-discovery
  cascade including jump tables, and control-flow graphs laid out in a worker
  — with the uncertainty of a recovered boundary drawn rather than hidden.
* **Get a verdict.** `binviz triage` says what the file looks like and why;
  in the UI each finding clicks through to the bytes it was derived from.

The UI is five workspaces — Overview, Bytes, Patterns, Code, and All — over the
same selection. Static analysis only: samples are parsed, never executed.

## Screenshots

![Overview workspace](https://assets.kitploit.com/production/public/readmes/53209/82650cf844dfc5bdda1164361e1639af4e602a4e056fb43d4a372f0cc820f084/c0854eab0cd6606e14e7b7d822c8764bf47ccf6d7f6a56be94384abcf3ffbd3b-display-v1.webp)

![Bytes workspace](https://assets.kitploit.com/production/public/readmes/53209/d77df4e6a92791a7b4577f9bfad1ff5b8691e6a2f5b6758b7bf756630f96441e/ae5bff8983eaf5983d41b43e59de4ad7bc8ab2df8fd015e467af3b67414674b2-display-v1.webp)

![Patterns workspace](https://assets.kitploit.com/production/public/readmes/53209/98d7b8a36dabbc202c1a7f8e677b9ffc53709ac33694e61cb0dca4f2e719c44e/2ea21e6e721c88a2e2f2bee7f019383d94e1b0aa51b997afe19da24f80b11c97-display-v1.webp)

![Code workspace](https://assets.kitploit.com/production/public/readmes/53209/ed3aa34cf73f42ff013a7bb3b98fb8f08bf3905535176b967c0284d998ee5a03/9852f0d23f3d9d0a6fd196993ade2ae8e05809809c4a9f227b99f6cf0a891356-display-v1.webp)

### Plates

Rendered by the same code the UI draws with, straight from the CLI —
regenerate with `python docs/make_plates.py`.

| A static binary | The same program, UPX-packed |
| --- | --- |
| ![Hilbert byte-class, static](https://assets.kitploit.com/production/public/readmes/53209/01793ccc54240281f686c0aa60a65efcdaacffa92224c55ad090335b29994433/fcffcdd6974ae6161a33bf9ce733c81cab4b3bdc71338f20007daa458a6c6045-display-v1.webp) | ![Hilbert byte-class, packed](https://assets.kitploit.com/production/public/readmes/53209/cf318fe294bf138390cfd76b453329a7603d7430381882914989ec105ce330cc/13d8aecc2a0085da09283359ad5cc4f1eb5445cea98c3b4fb5adb7727bfa72bd-display-v1.webp) |
| Code, strings and padding separate into visible territories. | Structure collapses into uniform noise — the signature of packing. |
| ![Entropy, static](https://assets.kitploit.com/production/public/readmes/53209/4f0909ffd3d1fe99df6f7d404a2e57eb23845b0ca31af48051dc2dad18d62bdd/ec8d24c6685a99396b2bb80e9f0b49c135284e888b624babde5b4cd8e57e957a-display-v1.webp) | ![Entropy, packed](https://assets.kitploit.com/production/public/readmes/53209/dcbe97d72485a37f55d41f8ee6c756017ead91891ca0aee85fe1026b81e754c8/0495c16c7b3cc4304ffe4d6e10fd757a728ac90825a02e3f8985a9c3aed0c428-display-v1.webp) |
| Windowed entropy stays banded and low. | Flat and high, right up to the unpacking stub. |

| Right row stride | Wrong row stride |
| --- | --- |
| ![RGB bars, correct stride](https://assets.kitploit.com/production/public/readmes/53209/27272d4212ef36d06258d3eef55c32ba8dcdb893b9f0199d408c0a74bf49752c/df719532a884cb35b54140afd96a4a391ddf26c52dd52aaf1033baa2a5e9d6fe-display-v1.webp) | ![RGB bars, wrong stride](https://assets.kitploit.com/production/public/readmes/53209/1d7fd3b7de4bb77b828fa63ab2cb1c2e5e51b8dca771847b509d8d862148b373/1142bcc0412ae00796383ed64d98dac04ab2d5839583052cadf6f321680de413-display-v1.webp) |

Same bytes, one number different. That is why the stride suggester exists: the
wrong row stride turns a photograph into diagonal noise, and you conclude there
is no photograph.

`ARCHITECTURE.md` is how it is put together: what ships, the branding every
surface inherits, the conventions a new screen must follow, and the
limitations that are deliberate. `SECURITY.md` is the security posture.

## Quickstart

root@kitploit:~

```
python -m venv .venv
# -c pins to the exact versions the suite is green against; pyproject.toml
# publishes ranges, so without it you get whatever resolves today
.venv/Scripts/pip install -e ".[dev]" -c constraints-dev.txt   # POSIX: .venv/bin/pip

# build the ground-truth corpus (uses zig cc from the ziglang pip package;
# needs UPX on PATH, in $UPX, or unzipped into corpus/tools/upx-*/)
make -C corpus                            # or: python corpus/build.py

# thresholds are measured, never hardcoded (see ARCHITECTURE.md §2.1)
python corpus/calibrate.py                # writes corpus/calibration.json

pytest                                    # functional suite
pytest -m perf -s                         # 100 MB performance targets

binviz probe  corpus/out/hello_O2
binviz model  corpus/out/hello_upx
binviz signal corpus/out/hello_upx --name entropy_4096 --png out.png
binviz hist   corpus/out/ramp16.bin --n 2 --dtype u16le --png bigram.png
...