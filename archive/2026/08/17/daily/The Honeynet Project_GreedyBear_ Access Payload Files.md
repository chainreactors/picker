---
title: GreedyBear: Access Payload Files
url: https://honeynet.org/2026/08/17/17/
source: The Honeynet Project
date: 2026-08-17
fetch_date: 2026-08-18T02:53:54.434101
---

# GreedyBear: Access Payload Files

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

# GreedyBear: Access Payload Files

###### 17 Aug 2026 [Krishna Awasthi](https://honeynet.org/authors/krishna-awasthi/) [gsoc](https://honeynet.org/tags/gsoc/) [greedybear](https://honeynet.org/tags/greedybear/) [threatintel](https://honeynet.org/tags/threatintel/) [malware](https://honeynet.org/tags/malware/)

Our [GSoC](https://summerofcode.withgoogle.com/) student **[Krishna Awasthi](https://github.com/opbot-xd)** spent three months working under the supervision of **[Tim Leonhard](https://github.com/regulartim)** on [**GreedyBear**](https://github.com/GreedyBear-Project/GreedyBear) and a new companion project, [**tpot-payload-server**](https://github.com/GreedyBear-Project/tpot-payload-server), building a complete pipeline to capture, quarantine, and share the malware payload files that T-Pot honeypots collect from live attackers.

Read on for an overview of the project, the technical decisions behind it, and what shipped.

**Student:** Krishna Awasthi ([opbot-xd](https://github.com/opbot-xd))

**Mentors:** Tim Leonhard

**Organization:** The Honeynet Project

**Project:** [GreedyBear](https://github.com/GreedyBear-Project/GreedyBear) · [tpot-payload-server](https://github.com/GreedyBear-Project/tpot-payload-server)

## The Problem

GreedyBear already harvests threat intelligence from T-Pot’s Elasticsearch stack: attack IPs, ports, credentials, and signatures. However, one critical layer of evidence was entirely absent: the **actual malware payload files** that honeypots like Dionaea, Cowrie, Honeytrap, and ADBHoney capture from live attackers.

These binaries, scripts, and exploit payloads live unindexed on T-Pot’s local filesystem under its data directory with no API, no index, and no way for downstream tools to access them. The goal of this GSoC project [**GreedyBear: Access payload files**](https://summerofcode.withgoogle.com/programs/2026/projects/gm6UndtK) was to build a **complete, production-grade pipeline** that bridges T-Pot payload captures with GreedyBear’s threat intelligence platform and the broader security research community.

## Architecture

The solution spans two codebases connected by a secured API channel, implemented in three phases:

1. **T-Pot side:** A stateless FastAPI microservice that scans honeypot payload directories on demand and serves file metadata and downloads over an API-key-authenticated endpoint.
2. **GreedyBear side:** A Django Q2 scheduled task that fetches new payloads, deduplicates by SHA256, and quarantines them safely with `.vir` extensions.
3. **Distribution:** An RBAC-protected DRF API for researchers, plus automated submission of new samples to MalwareBazaar.

![End-to-end architecture: T-Pot payload server through GreedyBear ingestion to researcher access](/2026/08/17/17/architecture.svg)

## GSoC Tasks and Deliverables

### 1. T-Pot Payload Server (New Repository)

The first phase of the project was building [tpot-payload-server](https://github.com/GreedyBear-Project/tpot-payload-server), a new standalone microservice designed to run as a Docker sidecar alongside T-Pot.

The server mounts honeypot capture directories (Dionaea binaries, Cowrie downloads, Honeytrap downloads, ADBHoney downloads) as **read-only** volumes and exposes two core endpoints:

* `GET /api/v1/payloads/recent?start_ts=...&end_ts=...` - Scans directories for files modified within a time window and returns metadata (MD5, SHA1, SHA256 hashes, MIME type, size, source honeypot) computed on-the-fly.
* `GET /api/v1/payloads/download/{locator}` - Streams the raw binary payload for ingestion.

A key design decision was making the service **completely stateless**. There is no background daemon watching directories. The server only consumes CPU during the brief window when GreedyBear actively makes a request, and sits idle the rest of the time. All file analysis (hashing, MIME detection via `python-magic`) happens through streaming reads; no sample is ever executed.

Security was a central concern throughout. The container runs with a read-only filesystem, `no-new-privileges`, and as a non-root user. The download endpoint includes multi-layer path traversal guards: exact directory allowlisting against configured honeypot paths, regex-validated filenames, and `is_relative_to` checks against symlink escapes.

An automated `install.sh` script handles deployment: it detects the T-Pot installation, generates a secure API key, configures an NGINX HTTPS reverse proxy using T-Pot’s existing TLS certificates, and brings up the container stack.

Key pull requests on **tpot-payload-server**:

* [Initial repository setup - #12](https://github.com/GreedyBear-Project/tpot-payload-server/pull/12)
* [Payload metadata extraction engine - #15](https://github.com/GreedyBear-Project/tpot-payload-server/pull/15)
* [FastAPI endpoints and containerization - #19](https://github.com/GreedyBear-Project/tpot-payload-server/pull/19)
* [Environment configuration and port conflict fix - #47](https://github.com/GreedyBear-Project/tpot-payload-server/pull/47)
* [Comprehensive README and documentation - #49](https://github.com/GreedyBear-Project/tpot-payload-server/pull/49)
* [Automated deployment with NGINX proxy and TLS - #52](https://github.com/GreedyBear-Project/tpot-payload-server/pull/52)
* [Release workflow - #53](https://github.com/GreedyBear-Project/tpot-payload-server/pull/53)

### 2. HoneypotPayload Model and Quarantine Storage

On the GreedyBear side, I introduced the `HoneypotPayload` Django model to persist payload metadata: SHA256, MD5, SHA1 hashes, MIME type, file size, and source information. The model includes `ManyToManyField` relationships to `Honeypot`, `IOC` (attacker IPs), and `CowrieSession` for threat intelligence correlation. A `unique` constraint on SHA256 (case-insensitive) ensures deduplication at the database level.

Downloaded samples are stored through a custom `QuarantineStorage` backend that restricts all file saves to the `media/quarantine/` directory and enforces a `.vir` extension on every filename, preventing accidental execution on any operating system.

* [HoneypotPayload model with quarantine storage - #1422](https://github.com/GreedyBear-Project/GreedyBear/pull/1422)

### 3. Payload Extraction Task

The core ingestion pipeline is a Django Q2 scheduled task (`PayloadExtractionJob`) that runs alongside GreedyBear’s existing extraction jobs after every extraction interval.

Each run:

1. Queries the `tpot-payload-server` for payloads modified in the last extraction window.
2. Performs **bulk deduplication**: collects all incoming SHA256 hashes, queries PostgreSQL for existing records, and filters the diff before downloading anything.
3. Checks quarantine disk usage against `MAX_QUARANTINE_SIZE_GB` before each download. Once the cap is reached, new samples are tracked in the database by metadata only and remain retrievable on-demand from T-Pot.
4. Downloads new payload files via the authenticated download endpoint, appends `.vir`, and saves through `QuarantineStorage`.

The task uses a shared `HttpClient` wrapper with configur...