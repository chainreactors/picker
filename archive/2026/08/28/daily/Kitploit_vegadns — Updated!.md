---
title: vegadns — Updated!
url: https://kitploit.com/en/posts/gitlab-wattocyber-vegadns-98175e161febf6e04d7c4b61b68bc9608c60f9fa9e5abdb057fa68608fda59b3
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:05.607519
---

# vegadns — Updated!

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50586/71769671d314f5e8976b2ebbce2e1f94ffd16a2e044b747463db338ee3c4e648-display-v1.webp)

UpdatedAug 28, 2026

# vegadns — Updated!

Rust-based DNS enumeration and subdomain discovery tool for reconnaissance and penetration testing security assessments.

Share

![vegadns - subdomain enum and path discovery](https://assets.kitploit.com/production/public/readmes/50586/71769671d314f5e8976b2ebbce2e1f94ffd16a2e044b747463db338ee3c4e648.jpg)

[![license](https://img.shields.io/badge/license-MIT-2d6a4f)](LICENSE) [![gitlab](https://img.shields.io/badge/gitlab-WattoCyber-fc6d26)](https://gitlab.com/WattoCyber/vegadns)

# vegadns

High-concurrency **subdomain enum**, **passive OSINT**, **HTTP path discovery**, and **Java / hidden endpoint extract** in one **Rust** binary.

Sanskrit *vega* = impetus / velocity. Also the star.

## The problem this solves

Subdomain and content-discovery tools split into two camps: slow-but-clean
passive OSINT and fast-but-junk-prone DNS brute. vegadns does both in one
binary, and it filters the noise (wildcard DNS, soft-404s) that buries massdns
and gobuster users in false positives. It is built and benchmarked against
massdns, puredns, dnsx, subfinder, altdns, and ZDNS on planted-answer lab
suites (see below).

## Quick start

root@kitploit:~

```
git clone [email protected]:WattoCyber/vegadns.git
cd vegadns
cargo build --release
./target/release/vegadns --help
```

Requires Rust stable. Full CLI reference in the README below or `--help`.

The shipped product is `vegadns` from `src/` (`cargo build --release`). There is
no Python on the scan path. `scripts/*.py` are optional peer-bench drivers
(massdns / ffuf / subfinder H2H on the same mock) and are excluded from
language statistics - see [scripts/README.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/scripts/README.md).

| Lane | Command | What it does |
| --- | --- | --- |
| Offline | `wordlist` / `expand` / `permute` | Depth packs, FQDN expand, altdns-class mutate (no network) |
| Lab DNS | `mock-serve` | Fixture zone over UDP for peer H2H |
| Passive OSINT | `passive` | Public CT / datasets / APIs → in-scope names (no DNS brute) |
| DNS | `enum` | Wordlist expand → concurrent UDP resolve → wildcard filter → emit |
| Live HTTP | `probe` | Host list → concurrent GET → live URLs (httpx-class) |
| Archives | `harvest` | Wayback CDX → in-scope hosts + subdirectory prefixes |
| Surface | `map` | Passive → recurse/permute → resolve → harvest → probe |
| HTTP paths | `paths` | Concurrent path scan + soft-404 fingerprint filter |
| Endpoints | `endpoints` | Java / source / hidden seed + HTML/JS/robots/sitemap extract |

Research pass covered massdns, puredns/shuffledns, dnsx, subfinder, alterx/gotator/altdns, and ZDNS. See [docs/RESEARCH.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/RESEARCH.md).

## How to read the numbers

We plant a fixed set of **real** answers (oracle). Every tool gets the same wordlist and the same mock server.

| Column | Plain English |
| --- | --- |
| Time | Seconds until the tool finishes (lower is faster) |
| Real found | How many planted answers it recovered (higher is better; max = oracle size) |
| Reported | How many names/URLs it printed as hits |
| Junk | Reported − Real found (noise you still have to triage) |
| Clean hit rate | Real found / Reported. **100%** means every printed hit was real |

**Faster is not always better.** A tool can finish first and still bury you in junk. We care about **all real answers, almost no junk**, then speed.

These are private lab / gym suites plus one public OSINT domain (`hackerone.com`). Not “fastest on the public internet.”
Full raw tables: **[docs/BENCHMARKS.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/BENCHMARKS.md)**.
This-revision vegadns-only clocks: **[docs/feature\_timing\_cloud.json](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/feature_timing_cloud.json)** (`python scripts/feature_timing.py`).

## Benchmarks at a glance

### 1. DNS lab - find subdomains, ignore wildcard noise

**Setup:** 500 real subdomains planted. Zone also answers random junk labels (wildcard). Wordlist: 8000 labels. Host: Kali.

| tool | Time | Real found (of 500) | Reported | Junk | Clean hit rate |
| --- | --- | --- | --- | --- | --- |
| **vegadns** | **0.18s** | **500** | **500** | **0** | **100%** |
| massdns | 0.43s | 500 | 721 | 221 | 69% |
| gobuster-dns | 161s | 0 | 0 | 0 | - |

**Takeaway:** vegadns and massdns both found every real name. massdns also printed **221 wildcard lies**. vegadns filtered those and finished faster on this suite.

### 2. DNS stress gym - flaky resolver (latency + packet loss)

**Setup:** 800 real names. Mock DNS adds 10 ms delay, 5% SERVFAIL, 2% drop. Wordlist: 2000. Host: Kali.

| tool | Time | Real found (of 800) | Reported | Junk | Clean hit rate |
| --- | --- | --- | --- | --- | --- |
| **vegadns** | **0.14s** | **800** | **800** | **0** | **100%** |
| massdns | 0.55s | 800 | 1700 | ~900 | 47% |

**Takeaway:** vegadns wins wall **and** clean output on this suite. massdns still dumps ~half junk.

### 3. Same tool, before vs after hot-path work

**Setup:** Windows gym-stress, 3000 candidates, same 800 oracle. No peer race. We only compare vegadns to itself.

| build | Time | Real found | Clean hit rate | Names checked / sec |
| --- | --- | --- | --- | --- |
| before | 0.59s | 800 / 800 | 100% | 5,047 |
| **after (best)** | **0.40s** | 800 / 800 | 100% | **7,583** |

**Takeaway:** ~**33%** faster, ~**50%** more names per second, still zero junk. Detail: [docs/OPTIMIZATION\_BREAKTHROUGHS.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/OPTIMIZATION_BREAKTHROUGHS.md). Later ceiling work (UDP buffers, `poll` instead of spin, no silent concurrency clamps) is in [docs/OPTIMIZATION\_CEILING.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/OPTIMIZATION_CEILING.md).

### 4. HTTP paths - server lies with “200 OK” on missing pages

**Setup:** 24 real paths planted (`/admin`, `/api`, …). **Soft-404:** missing paths still return HTTP **200** with a fixed “not found” body. Status-only tools treat those as hits. Wordlist mixes real paths + bait. Same process-wall clock for every tool.

| tool | Time | Real found (of 24) | Reported | Junk | Clean hit rate |
| --- | --- | --- | --- | --- | --- |
| **vegadns paths** | **0.032s** | **24** | **24** | **0** | **100%** |
| feroxbuster | 1.03s | 24 | 61 | **37** | 39% |

**What this means**

1. Every timed tool found all 24 real paths.
2. ferox also reported **37 fake pages** (soft-404 200s).
3. vegadns fingerprints the lie, drops fakes, prints **exactly the 24 real URLs**, and finishes **faster**.

**Takeaway:** vegadns wins clean output **and** wall on this fixed Kali suite (body drain + keep-alive reuse; process-wall H2H).

### 5. Same suites, re-run on Linux cloud host (2026-08-20)

Real adjacent binaries on PATH (massdns, dnsx, puredns, shuffledns, gobuster, ffuf, ferox). Single measured run. Full tables: [docs/PEER\_BENCH\_CLOUD\_2026-08-20.md](https://gitlab.com/wattocyber/vegadns/-/blob/main/docs/PEER_BENCH_CLOUD_2026-08-20.md).

**DNS gym-stress** (800 planted, 2000 labels, 10 ms / 5% SERVFAIL / 2% drop):

| tool | Time | vs vegadns | Real found (of 800) | Junk | Clean hit rate | F1 |
| --- | --- | --- | --- | --- | --- | --- |
| **vegadns** | **0.164s** | **1.0×** | **800** | **0** | **100%** | **1.000** |
| massdns | 0.515s | 3.1× | 800 | 900 | 47% | 0.640 |
| puredns | 1.211s | 7.4× | 800 | 900 | 47% | 0.640 |
| shuffledns | 1.435s | 8.7× | 800 | 900 | 47% | 0.640 |
| dnsx | 6.673s | 41× | 795 | 895 |...