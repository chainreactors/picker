---
title: [Tool] starshield-forensics v0.3.7: Offline Chromium LevelDB .log carver (Python stdlib, MIT)
url: https://seclists.org/fulldisclosure/2026/Nov/39
source: Full Disclosure
date: 2026-11-17
fetch_date: 2026-11-18T09:22:47.464997
---

# [Tool] starshield-forensics v0.3.7: Offline Chromium LevelDB .log carver (Python stdlib, MIT)

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

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [Tool] starshield-forensics v0.3.7: Offline Chromium LevelDB .log carver (Python stdlib, MIT)

---

*From*: Ziqi Xiao <ziqixiao () gmail com>
*Date*: Fri, 13 Nov 2026 11:12:19 +0800

---

```
Tool: starshield-forensics v0.3.7 & StarShield-Bench-24
Category: Digital Forensics / Incident Response (DFIR) & AI Security
License: MIT (Open Source, Python >= 3.10 standard library only)
Author: Ziqi Xiao (@Ziqi)
Repository: https://github.com/Ziqi/starshield-forensics
Release Tag:
https://github.com/Ziqi/starshield-forensics/releases/tag/v0.3.7
Documentation: https://ziqi.github.io/starshield/
Zenodo DOI: https://doi.org/10.5281/zenodo.24145804 (v0.3.7:
10.5281/zenodo.24156262)
Supply Chain: OpenSSF Best Practices Silver (#16602) | Scorecard 7.1/10
               https://www.bestpractices.dev/projects/16602

1. Summary & Threat Context
---------------------------
During Business Email Compromise (BEC), supplier invoice diversion, and
Authorized Push Payment (APP) fraud investigations, browser-based messaging
and invoicing apps frequently propagate UI retractions or post-transfer
edits as soft-delete updates while uncompacted Chromium IndexedDB / Local
Storage LevelDB write-ahead logs (.log) still retain earlier UTF-8 or
UTF-16LE JSON records or text fragments on disk.

At the same time, piping untrusted adversary chat exports directly into LLM
summarizers exposes incident responders to indirect prompt injection (OWASP
LLM01) and fabricated payment routing identifiers.

starshield-forensics v0.3.7 is a deterministic, offline Python 3.10+
standard-library CLI utility (zero external PyPI dependencies) packaged as
a reproducible single-file .pyz zipapp for restricted lab and triage hosts.

2. Technical Capabilities (v0.3.7)
----------------------------------
- Redacted Storage Feasibility Check (`precheck`):
  Scans read-only copies of Chromium IndexedDB / Local Storage directories
  offline, distinguishing uncompacted `.log` WAL segments from Snappy
  `.ldb` SSTables (footer magic `0xdb4775248b80fb57`) and Blink `0xFF`
  envelopes (`GO` / `PARTIAL` / `NO_GO_COMPACTED_OR_UNSUPPORTED`) using
  aggregate counts only without emitting raw message plaintext or paths.

- Cross-Block 32 KiB LevelDB `.log` Carver (`parse-leveldb-log`):
  Parses physical 32,768-byte WAL blocks, verifies masked Castagnoli CRC32C
  (`(((crc >> 15) | (crc << 17)) + 0xA282EAD8) mod 2^32`), reassembles
  `FULL`, `FIRST`, `MIDDLE`, and `LAST` fragments across `0x8000` block
  boundaries, and carves soft-deleted / edited JSON records
  (`--schema auto|chatsvc|generic-json`) anchored to exact physical byte
  offsets (`leveldb_batch_byte_offset`).

- Exported JSON Triage & Container Provenance (`triage-json`,
`inspect-image`):
  Enumerates `deletetime` / `edittime` records in JSON exports and performs
  neutral structural verification of RFC 2083 PNG chunks
(`IHDR`/`iCCP`/`IDAT`)
  and multi-segment ISO 10918 JPEG `APP2` ICC (`acsp`) + `APP13` (`8BIM`)
  markers, paired with explicit OS-screenshot caveats to prevent
overclaiming.

- Payment Identifier Checksums & Keyed Pseudonymization:
  Validates ISO/IEC 7812 Luhn card numbers, 89-country ISO-13616 IBAN
  Mod-97 checksums, intra-message UK Sort Code + 8-digit account pairs,
  and ISO-9362 SWIFT/BIC syntax (250 ISO-3166 country codes). Suppresses
  filenames, byte counts, and stderr snippets while pseudonymising matched
  identifiers by default via per-run keyed HMAC-SHA256 tokens
  (`--hmac-digest {sha256,sha384,blake2b}`).

- `StarShield-Bench-24` Synthetic Evaluation Corpus:
  24 seeded synthetic test cases (`SSB24-01`..`SSB24-24`) scoring WAL
  recovery, byte-offset citation accuracy, malformed-container rejection,
  and bilingual indirect prompt-injection resilience; paired with 12
  companion financial-triage cases (`TC-0456`..`TC-0467`) submitted
  upstream in OWASP GenAI Data Security Initiative PR #119.

3. Reproducible Build & Cryptographic Verification
--------------------------------------------------
Single-file reproducible `starshield.pyz` SHA-256 (`v0.3.7`):
  e6603ef083b20a5460bf56818f63a3a94b856deb377a5b6330be2394e0e21232

Maintainer OpenSSH Ed25519 Signing Key (`KEYS.pub` in repository):
  2196305+Ziqi () users noreply github com namespaces="file,git" ssh-ed25519
AAAAC3NzaC1lZDI1NTE5AAAAIKz9qGDNELwOsoNnmZIpLKQ+5HOqdE4ilZaTRA/1LR7a

Verification commands (OpenSSH >= 8.2p1, zero external packages):
  ssh-keygen -Y verify -f KEYS.pub \
    -I "2196305+Ziqi () users noreply github com" \
    -n file -s SHA256SUMS.sig < SHA256SUMS
  shasum -a 256 -c SHA256SUMS
  python3 scripts/build_reproducible.py --verify

Bug reports, edge-case Chromium WAL test vectors, and technical critiques
are welcome via GitHub Issues: https://github.com/Ziqi/starshield-forensics

--
Ziqi Xiao
Independent Security Architect & Digital Forensics Researcher
https://ziqi.github.io/starshield/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **[Tool] starshield-forensics v0.3.7: Offline Chromium LevelDB .log carver (Python stdlib, MIT)** *Ziqi Xiao (Nov 17)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")