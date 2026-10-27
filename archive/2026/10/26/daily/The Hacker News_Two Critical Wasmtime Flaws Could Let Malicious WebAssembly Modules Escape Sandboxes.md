---
title: Two Critical Wasmtime Flaws Could Let Malicious WebAssembly Modules Escape Sandboxes
url: https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:43.877749
---

# Two Critical Wasmtime Flaws Could Let Malicious WebAssembly Modules Escape Sandboxes

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Two Critical Wasmtime Flaws Could Let Malicious WebAssembly Modules Escape Sandboxes](https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html)

**Swati Khandelwal**Oct 26, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5xq9w5oCep_lu7UpdVExPO7yRQ1tMz0YkxljYR_LmwG3WKowZ2CtLPh4F6kASJ7Xu0xJKy4uVzlwj7fPEO3fgKUELS4BqUtDZvGh1P-iqRslXNCLdkcJMCBGSKvJeqrrkeZdfPO9Wmv_v2VqdYEZVavTHw-QHUhli9QYGVhASuSRt3DETy8JMBz1D-kE/s1700-nu-rw-lo-l85-e365/wasm.jpg)

Two critical flaws in [Wasmtime](https://docs.wasmtime.dev/introduction.html), a WebAssembly runtime that can be built into other software, could allow a malicious WebAssembly module to escape the sandbox intended to contain it, the project's maintainers say.

An attacker would first need a vulnerable Wasmtime build to compile a module they control, and one of the flaws affects only ARM64 systems. Fixed versions were released on October 19 and 20, and the maintainers have not reported any attacks.

Wasmtime runs WebAssembly code outside web browsers. Both bugs are in Cranelift, the compiler it uses by default to turn WebAssembly into machine code. Wasmtime's maintainers at the Bytecode Alliance rated each flaw 9.9 out of 10 on the CVSS scale in advisories published on October 19.

* [CVE-2026-115889](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-897f-g5gm-fmxm) affects Wasmtime across all processor architectures.
* [CVE-2026-115893](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-mghf-wjfp-p5xm) affects only ARM64, also called aarch64.

The sandbox is meant to keep a module inside set limits. A module can only use its own memory and the host functions it is given, and its code can only jump to checked locations.

Because both flaws need a module the attacker controls, the risk is highest for services that compile modules written by other people. Fastly, for example, [says its Compute platform runs customer code using Wasmtime](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/). The advisories do not name any affected services or specify what an attacker could access after escaping the sandbox.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

Neither flaw was in the Known Exploited Vulnerabilities catalog kept by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) as of October 26.

### Which Versions Are Affected

The two flaws were fixed at different times, so whether your version is affected depends on your release line and, for one flaw, your processor architecture.

| Wasmtime version | CVE-2026-115889 (any architecture) | CVE-2026-115893 (ARM64 only) | What to do |
| --- | --- | --- | --- |
| Before 36.0.19 (includes 24.x) | Affected | Affected | Update to 36.0.19, or move to 48.0.7, 49.0.4 or 50.0.0 |
| 36.0.19 | Fixed | Fixed | None needed for these flaws |
| 37.0.0 through 42.x | Affected | Affected | Move to 48.0.7, 49.0.4 or 50.0.0 |
| 43.0.0 through 47.x | Not affected | Affected | Move to 48.0.7, 49.0.4 or 50.0.0 |
| 48.0.0 through 48.0.6 | Not affected | Affected | Update to 48.0.7 |
| 48.0.7 | Not affected | Fixed | None needed for these flaws |
| 49.0.0 through 49.0.3 | Not affected | Affected | Update to 49.0.4 |
| 49.0.4, and 50.0.0 or later | Not affected | Fixed | None needed for these flaws |

Wasmtime [supports long-term support (LTS) releases](https://docs.wasmtime.dev/stability-release.html), which are numbered in multiples of 12, for two years. Other releases get two months. Security fixes are guaranteed for supported releases.

Only the 36, 48, 49, and 50 release lines are still supported. Every other line, including the 24.x LTS line whose support ended on August 20, 2026, got no fix.

ARM64 hosts that updated to 36.0.7, 42.0.2, or 43.0.1 in April to fix an [earlier Cranelift sandbox escape on ARM64](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-jhxm-h53p-jm7w) are still affected by CVE-2026-115893.

### What to Do

Update to the fixed release for your line: [36.0.19](https://github.com/bytecodealliance/wasmtime/releases/tag/v36.0.19), [48.0.7](https://github.com/bytecodealliance/wasmtime/releases/tag/v48.0.7), or [49.0.4](https://github.com/bytecodealliance/wasmtime/releases/tag/v49.0.4). Wasmtime 50.0.0, released on October 20, is fixed for both flaws. Hosts on an unsupported line need to move to one of these releases.

Wasmtime can be built into other programs as a library, so updating the command-line tool does not fix them. Each program that includes Wasmtime needs to be rebuilt with a fixed version.

Neither advisory lists a workaround. Until a host is updated, the risk comes from any module an outsider can supply.

Both flaws are listed in RustSec, the database the [cargo-audit](https://rustsec.org/) tool uses to check Cargo.lock files, as [RUSTSEC-2026-0380](https://rustsec.org/advisories/RUSTSEC-2026-0380.html) and [RUSTSEC-2026-0379](https://rustsec.org/advisories/RUSTSEC-2026-0379.html).

As of October 26, [GitHub's advisory database](https://github.com/github/advisory-database) had a reviewed entry for CVE-2026-115889 but none for CVE-2026-115893. GitHub says [only reviewed entries trigger Dependabot alerts](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependabot-alerts), so Dependabot users should not expect an alert for the ARM64 flaw.

Spin, an open-source tool for building serverless WebAssembly apps that runs on Wasmtime, [moved to Wasmtime 50.0.0 in version 4.2.4](https://github.com/spinframework/spin/blob/v4.2.4/Cargo.lock) on October 21.

### How the Two Flaws Work

CVE-2026-115889 comes from how Cranelift stored the numbers it uses to track values inside a function. Before version 43, it packed these numbers into 24-bit fields, and in release builds, a number too large for its field overflowed without any error.

Crane...