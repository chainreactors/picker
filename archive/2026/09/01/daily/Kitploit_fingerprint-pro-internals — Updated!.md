---
title: fingerprint-pro-internals — Updated!
url: https://kitploit.com/en/posts/github-proofofbots-fingerprint-pro-internals-74483b09060e477a91793ded91dbd68d5d5709468078a636a47f7465bed72913
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:11.462907
---

# fingerprint-pro-internals — Updated!

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50179/db97a6edd521bccc78a634b24f194b129ea07aeb4c6f93238bf8c7229a272cfb.png)

UpdatedSep 1, 2026

# fingerprint-pro-internals — Updated!

Documenting the internals of Fingerprint Pro's commercial agent, not the open-source FingerprintJS library

Share

![Fingerprint Pro Internals](https://raw.githubusercontent.com/proofofbots/fingerprint-pro-internals/HEAD/docs/logo.svg)

### Fingerprint Pro v4, deobfuscated and documented

**143 signals named. The bundle unpacked. The wire format decoded.**

**[Run it on your browser](https://proofofbots.github.io/fingerprint-pro-internals/explorer.html)** ·
**[Read the docs](https://proofofbots.github.io/fingerprint-pro-internals/)** ·
[Signal map](https://proofofbots.github.io/fingerprint-pro-internals/reference/signals.html) ·
[Collector sources](https://proofofbots.github.io/fingerprint-pro-internals/slices/)

---

|  |  |
| --- | --- |
| [**143 signals, one row each**](https://proofofbots.github.io/fingerprint-pro-internals/reference/signals.html) | surfaces touched, status codes, constants compared, value shape |
| [**The agent, readable**](https://proofofbots.github.io/fingerprint-pro-internals/repo/agent.html) | CRC32 names resolved, tables decrypted, wrappers folded, bindings renamed, hash-pinned |
| [**Every collector as its own file**](https://proofofbots.github.io/fingerprint-pro-internals/slices/) | one signal plus only the helpers it reaches, instead of a 200 KB bundle |
| [**The collectors, runnable**](https://proofofbots.github.io/fingerprint-pro-internals/repo/collector.html) | `collect`, `buildPayload`, `frame`, `send` from a console. No agent, no network |
| [**Wire format, end to end**](https://proofofbots.github.io/fingerprint-pro-internals/03-wire-format.html) | JSON to bytes, deflate-raw over 1024, sealed with a key that ships inside the frame |
| [**What `visitor_id` is a function of**](https://proofofbots.github.io/fingerprint-pro-internals/06-identity.html) | 7 fields break a match alone, `s56` is a bearer token, not a fingerprint |

[![The signal explorer running the 143 collectors in-browser](https://assets.kitploit.com/production/public/readmes/50179/db97a6edd521bccc78a634b24f194b129ea07aeb4c6f93238bf8c7229a272cfb.png)](https://proofofbots.github.io/fingerprint-pro-internals/explorer.html)

# Akamai solver + other tools

For Akamai, and other solvers, check out this repo: <https://github.com/proofofbots/web-re-toolkit>

## The site

The whole repository is published at
[proofofbots.github.io/fingerprint-pro-internals](https://proofofbots.github.io/fingerprint-pro-internals/):
the guide, every generated map as a filterable table, all 143 collector sources syntax highlighted,
and the live explorer. `npm run site` builds it into [`docs/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/docs/), which is what GitHub Pages
serves from `main`. Open `docs/index.html` over HTTP to preview a build locally.

## Quickstart

root@kitploit:~

```
npm install
npm run fetch      # download the pinned bundle, verify its hash
npm run all        # deobfuscate, verify, regenerate every map
npm run site       # rebuild the documentation site into docs/
npm run capture    # serve the capture page, open it once per browser
```

To read rather than run, start at
[the signal map](https://proofofbots.github.io/fingerprint-pro-internals/reference/signals.html) for
the inventory and
[the collector sources](https://proofofbots.github.io/fingerprint-pro-internals/slices/) for the code
behind any single signal.

To watch the agent on a live site, paste [`spy/fpspy.js`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/spy/fpspy.js) into DevTools.

To run the collectors with no agent and no network, open
[the explorer](https://proofofbots.github.io/fingerprint-pro-internals/explorer.html), or serve the
repository and open [`collector/index.html`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/collector/index.html) for the raw table.

Everything here describes one pinned build: `jsl/4.0.0`, sha256 `250c7dfe…`, fetched 2026-08-07. The
tenant ships new builds and the paths rotate. `npm run fetch` checks the pin and `npm run diff` says
what changed.

## Layout

| directory | what is in it |
| --- | --- |
| [`docs/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/docs/) | the writeup, plus the generated site GitHub Pages serves |
| [`agent/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/agent/) | the deobfuscated bundle and worker, the decrypted string tables, the pin |
| [`reference/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/reference/) | generated maps: signals, slices, schema, envelope, codes, endpoints, observed |
| [`collector/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/collector/) | `fp-collect.js`, the collectors and codec as one plain module |
| [`site/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/site/) | source of the generated site |
| [`spy/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/spy/) | the DevTools instrumentation script |
| [`captures/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/captures/) | three browser captures of the pinned build |
| [`profiles/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/profiles/) | a device profile that compiles to a payload |
| [`evidence/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/evidence/) | raw rows behind the identity and attribution findings |
| [`tools/`](https://github.com/proofofbots/fingerprint-pro-internals/blob/HEAD/tools/) | the toolchain, one job per file |
| `artifacts/` | everything generated that is not committed |

## What the analysis found

* Both protection layers come apart offline. Property names are CRC32 constants over DOM
  identifiers, which a dictionary resolves; the four string tables that key off live browser state
  key off property *names*, which the same dictionary already recovers.
  [02-obfuscation](https://proofofbots.github.io/fingerprint-pro-internals/02-obfuscation.html)
* The agent names its own signals. Each module registers a `sources` table mapping the wire id to the
  collector, so the map is the agent's labels, not assigned ones. 143 ids, 4 of them scheduled first
  because they are slow.
  [01-architecture](https://proofofbots.github.io/fingerprint-pro-internals/01-architecture.html),
  [04-collection](https://proofofbots.github.io/fingerprint-pro-internals/04-collection.html)
* The wire format is JSON over bytes, deflate-raw over 1024 bytes, then framed with a key that ships
  inside the frame.
  [03-wire-format](https://proofofbots.github.io/fingerprint-pro-internals/03-wire-format.html)
* `s56`, the blob the server issues over the GET leg and the client replays, is a bearer token. Any
  payload carrying a bound one answers as that visitor whatever the device reports. With it empty,
  seven fields break the identity match on their own, and the rest hold until six groups of them move
  at once. [06-identity](https://proofofbots.github.io/fingerprint-pro-internals/06-identity.html)
* Across Chrome, Firefox and Safari on one machine, 58 of the 143 signals report a different value
  and the remaining 85 are identical. The static read and the captures disagree nowhere.
  [04-collection](https://proofofbots.github.io/fingerprint-pro-internals/04-collection.html)

## Docs

1. [Architecture](https://proofofbots.github.io/fingerprint-pro-internals/01-architecture.html) — modu...