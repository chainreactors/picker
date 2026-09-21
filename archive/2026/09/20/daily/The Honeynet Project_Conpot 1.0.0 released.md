---
title: Conpot 1.0.0 released
url: https://honeynet.org/2026/09/20/conpot-1.0.0/
source: The Honeynet Project
date: 2026-09-20
fetch_date: 2026-09-21T07:27:40.949144
---

# Conpot 1.0.0 released

[![The Honeynet Project Logo](/logo-text.svg)](/)

* About
  + [The Project](/about/)
  + [Code of Conduct](/about/code-of-conduct/)
  + [Funding](/about/funding/)
  + [Papers](/papers/)
* [Projects](/projects/)
* GSoC
  + [Google Summer of Code](/gsoc/)
  + [GSoC 2026](/gsoc/gsoc-2026/)
  + [GSoC 2025](/gsoc/gsoc-2025/)
  + [GSoC 2024](/gsoc/gsoc-2024/)
  + [GSoC 2023](/gsoc/gsoc-2023/)
  + [GSoC 2022](/gsoc/gsoc-2022/)
  + [GSoC 2021](/gsoc/gsoc-2021/)
  + [GSoC 2020](/gsoc/gsoc-2020/)
  + [GSoC 2018](/gsoc/gsoc-2018/)
  + [GSoC 2017](/gsoc/gsoc-2017/)
  + [GSoC 2016](/gsoc/gsoc-2016/)
  + [GSoC 2015](/gsoc/gsoc-2015/)
  + [GSoC 2014](/gsoc/gsoc-2014/)
  + [GSoC 2013](/gsoc/gsoc-2013/)
  + [GSoC 2012](/gsoc/gsoc-2012/)
  + [GSoC 2011](/gsoc/gsoc-2011/)
  + [GSoC 2010](/gsoc/gsoc-2010/)
  + [GSoC 2009](/gsoc/gsoc-2009/)
* [Workshops](/workshops/)
* [Challenges](/challenges/)
* [Blog](/blog/)
* [FAQ](/faq/)

# Conpot 1.0.0 released

###### 20 Sep 2026 [Lukas Rist](https://honeynet.org/authors/lukas-rist/) [conpot](https://honeynet.org/tags/conpot/) [honeypot](https://honeynet.org/tags/honeypot/) [ics](https://honeynet.org/tags/ics/) [scada](https://honeynet.org/tags/scada/)

The [Conpot](https://github.com/mushorg/conpot) team is proud to announce [version 1.0.0](https://github.com/mushorg/conpot/releases/tag/v1.0.0). This is a platform rewrite, not a point release. The honeypot still emulates ICS/SCADA services so you can collect attacker intelligence, but the runtime, templates, logging sinks, and several protocol libraries are new.

Treat this as a **breaking upgrade**: migrate templates and log consumers, then re-validate Docker ports and deployment scripts.

[Conpot](https://github.com/mushorg/conpot) is a low-interaction ICS/SCADA honeypot. You configure device templates and protocol servers so scanners and operators see a plausible industrial system, while sessions and attacks land in structured logs. 1.0.0 keeps that mission and replaces the stack underneath it.

## Runtime and packaging

The gevent stack is gone. Protocol servers now run on **asyncio**. The CLI is a normal asyncio entrypoint: `python -m conpot` / `conpot.cli`.

Startup is less rigid: fewer hard restrictions at launch, and clearer operator UX. MAC-address spoofing was **removed**.

## Templates and databus (breaking)

Templates moved from **XML to TOML**, with a flatter layout: `templates/<name>/template.toml` (metadata + databus) plus per-protocol `*.toml`. Auxiliary files stay in subdirectories only when needed (for example HTTP `htdocs`).

The databus is decoupled from `SessionManager`. `get_value()` evaluates a mapping once. Random/generated value functions, extra SNMP-oriented emulators, and a simulated PLC-style emulator sit on that bus.

## Protocol changes

Protocol work in this release is mostly correctness, library upgrades, and crash/DoS hardening rather than brand-new industrial dialects:

* **S7:** parameter-length calculation, read/write, PLC-stop.
* **Modbus:** pymodbus, recv-path fixes, and a DoS fix for unbounded byte-at-a-time oversized reads.
* **IEC 104:** IOA and float endianness, types 100–103, friendlier I-frame logs.
* **ENIP/CIP:** exception/crash fixes, device-info handling, **cm-ethernetip**.
* **BACnet:** bacpypes3 plus BACnet/IP encode/decode.
* **HTTP:** aiohttp; template substitution no longer uses `HTMLParser`.
* **SNMP:** richer emulators, default listen port **16100**, no custom MIB compile path.
* **FTP / IPMI / TFTP:** FTP handler exception-loop fix, RFC 959 greeting expectations, IPMI IPv6/test and JSON logging fixes, FakeSession timeout before pyghmi init, TFTP test cleanup.

## Logging and sessions (breaking for sinks)

Attack logging is structured (schema version 1) across JSON, SQLite, syslog, HPFriends, and TAXII. Events carry `event_time` distinct from session start. Remote **IP and port**, and destination from the socket, are first-class fields. Syslog gets attack JSON explicitly.

HPFriends/JSON payloads use `session_id` / `protocol` / flat endpoints instead of the old `id` / `data_type` / remote tuples. Sessions can be deleted.

If you ingest Conpot into a SIEM, HPFriends, or a homegrown parser, update field mappings before you cut over.

## Get it, run it, contribute

Release notes and the full changelog live on GitHub: [Conpot 1.0.0](https://github.com/mushorg/conpot/releases/tag/v1.0.0).

Thanks to everyone who contributed since the last line of the 0.6-era tree, including first-time contributors who landed protocol, packaging, and test work over a long stretch of PRs. If you are running ICS honeypots, please try 1.0.0, file issues when templates or sinks surprise you, and consider sharing anonymized attack data with the community.

We are looking for operators and developers who care about industrial protocols. Issues and pull requests are welcome on [mushorg/conpot](https://github.com/mushorg/conpot).

The Honeynet Project 1999–2026