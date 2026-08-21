---
title: fnprint
url: https://kitploit.com/en/tools/github/1rhino2/fnprint
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:02:58.397493
---

# fnprint

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

fnprint — match functions in binaries by what they do, not what their bytes look like. behavioral function fingerprinting via microexecution. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/1rhino2/fnprint

![](https://assets.kitploit.com/production/public/tools/50575/5e79e003590825868a0bb3b199f3c2fe2f78ed03d0889a82de17df08afb27874.png)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Dynamic Code Analysis (DAST)](/en/categories/dynamic-code-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Malware Analysis](/en/categories/malware-analysis)[Binary Analysis](/en/categories/binary-analysis)[Firmware Analysis](/en/categories/firmware-analysis)

![GitHub](/providers/github.png)1rhino2/fnprint

# fnprint

match functions in binaries by what they do, not what their bytes look like. behavioral function fingerprinting via microexecution.

[View Repository](https://github.com/1rhino2/fnprint)

2021520h 16m ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![fnprint](https://raw.githubusercontent.com/1rhino2/fnprint/HEAD/assets/wordmark.svg)

fnprint matches functions in binaries by what they *do*, not by what their bytes
or control-flow graphs look like. it runs each function in a tiny emulator with
made-up inputs, records the side effects it produces, and hashes that behavior
into a fingerprint. two functions that behave the same get similar fingerprints,
even if they were built by a different compiler or at a different optimization
level.

the point of doing it this way: byte signatures (FLIRT, FunctionID) break the
moment code is recompiled, and CFG matchers (BinDiff, Diaphora) get shaky across
`-O0` vs `-O3`. behavior survives both a lot better.

x86-64 ELF only for now. see [limits](#what-it-is-bad-at) before you trust it.

## show me

point it at a stripped binary and a corpus of things you already have names for:

root@kitploit:~

```
$ strip --strip-all mystery.so
$ nm mystery.so
nm: mystery.so: no symbols

$ fnprint index libz.so -o corpus.db          # a build you have symbols for
$ fnprint query mystery.so --corpus corpus.db
named 9 function(s):
  0x000022f9  100.0%  adler32_z
  0x00002a8d  100.0%  compress2
  0x0000ad5d  100.0%  inflateBackEnd
  0x0000adc4   86.7%  inflate_fast
  0x00002e67   80.5%  crc32_z
  ...
```

that run is a fully stripped `-O0` build named from an `-O2` corpus. different
optimization level, zero symbols left, and the names come back right. it names
what it is confident about and stays quiet about the rest.

the other thing it does is diff two builds and tell you which functions changed
behavior, which is handy when a vendor ships a new firmware and you want to know
what actually moved:

root@kitploit:~

```
$ fnprint match old.so new.so
compared 84 functions present in both
  unchanged:  53
  changed:    1
  low-signal: 31 (too small to judge)

changed behavior (lowest similarity first):
   61.7%  deflate_stored
```

for actual n-day work there is `triage`. build one corpus from the known
vulnerable version of a function and one from the patched version, then rank an
unknown build against both. a function close to the vulnerable side and clearly
separated from the patched side is what you want in front of a human, not just a
single match score you have to interpret:

root@kitploit:~

```
$ fnprint index vuln.so    -o vuln.db
$ fnprint index patched.so -o patched.db
$ fnprint triage mystery.so --vuln vuln.db --patched patched.db
43 functions triaged: 1 look vulnerable, 0 patched, 42 inconclusive

review queue (vuln-leaning, strongest first):
   addr         vuln%  patched%  margin  matches
   0x000022f9  100.0     27.3   +72.7  adler32_z vs crc32_z
```

the 42 functions that are identical in both versions come back inconclusive on
purpose, they can't be pinned to either side and shouldn't be flagged. `--margin`
and `--min-sim` control how hard the two sides have to separate before it commits.

## how it works

for each function:

* map the binary and jump to the function with junk in the argument registers.
* any read from memory we did not set up returns a deterministic value and the
  page gets mapped on the fly. wild pointers never crash the run, and the same
  input always gives the same trace. this is Godefroid's microexecution trick.
* calls to other functions get stubbed (recorded, then skipped) so we never
  dive into libc and the run stays about *this* function.
* we log an arch-neutral stream of effects: which argument buffers and struct
  fields it reads and writes, what value classes it writes (a copy of an input,
  a small constant, a pointer), calls it makes, branches it takes, what it
  returns. absolute addresses are thrown away, only offsets and shapes are kept.
* that stream gets turned into shingles and a minhash signature. similarity is
  the fraction of matching minhash slots, which estimates how much two functions'
  behavior overlaps. an LSH band index keeps queries from comparing everything
  against everything.

no training data, no model. the same idea shows up in the literature as
Blanket Execution (Egele et al, USENIX Security 2014); fnprint is a practical,
maintained take on it with a CLI you can actually use.

## install

needs a rust toolchain and the unicorn + capstone libraries.

root@kitploit:~

```
# debian/ubuntu/kali
sudo apt install libunicorn-dev libcapstone-dev

cargo install --path cli
# or just
cargo build --release   # binary at target/release/fnprint
```

## usage

root@kitploit:~

```
fnprint index <binary> [-o out.db]      fingerprint every function, optionally to a db
fnprint match <a> <b>                   diff two binaries (or .db files) by behavior
fnprint query <target> --corpus <db>    name unknown functions from a corpus
fnprint triage <t> --vuln <db> --patched <db>   rank a build against vuln vs patched corpora
fnprint eval <a> <b>                     accuracy metrics using symbol names as truth
fnprint dump <binary> <func>            print the recorded effect trace (debugging)
```

`match` and `query` take either an ELF or a `.db` you built with `index`, so you
can fingerprint a corpus once and reuse it.

## accuracy

rank-1 accuracy is: for a function in build A, rank every function in build B by
similarity, is the top hit the right one. that is exactly the stripped-naming
task. measured on zlib 1.3.1 (84 functions), reproducible with `bench/run.sh`:

full table plus a second library (lua) in [bench/NUMBERS.md](https://github.com/1rhino2/fnprint/blob/HEAD/bench/NUMBERS.md).

`eval` also reports recall@3 / recall@5 and an abstention rate, since rank-1
alone hides a lot. on gcc O0 -> O2 the top hit is right 93% of the time but the
correct function is in the top 5 96.6% of the time, so a small review budget
closes most of the gap. it also abstains (declines a confident "same" call)
on the pairs it isn't sure about instead of guessing, which is why precision
stays high while recall at the same threshold is low.

the honest read: when at least one side has some behavioral...