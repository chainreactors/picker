---
title: isms-builder v1.37.5.3
url: https://kitploit.com/en/posts/github-coolstartnow-isms-builder-v13753
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:43.214894
---

# isms-builder v1.37.5.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12462/053332b35c995bc3a672be7bfd193ca3789f3245e7cdffaa456833fabdec309e.png)

New releaseAug 26, 2026

# isms-builder v1.37.5.3

Self-hosted Information Security Management System — ISO 27001, NIS2, GDPR/DSGVO, BSI IT-Grundschutz

Share

![ISMS Builder Banner](https://assets.kitploit.com/production/public/readmes/12462/26d3b00b65a4f94cc34514132f1ee5f5c9036e45516880da99fb9501dd79bead.png)

# ISMS Builder

**Self-hosted Information Security Management System — open source, no cloud required**

[![CI](https://github.com/coolstartnow/isms-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/coolstartnow/isms-builder/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-423%20passing-brightgreen)](https://github.com/coolstartnow/isms-builder/actions)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=white)](https://nodejs.org)
[![Version](https://raw.githubusercontent.com/coolstartnow/isms-builder/HEAD/docs/badges/version.svg)](CHANGELOG.md)

---

> ## ⚠️ Security Warning: Fake repositories and copies distributing malware
>
> ISMS Builder has **no packaged "releases", installers, or downloadable ZIP files** — the only
> legitimate source is this repository, cloned or downloaded directly from GitHub as plain
> source code. We are aware of at least one **malicious repository impersonating this project**
> (fake README, fake "Download" button linking to a ZIP disguised as a screenshot, containing a
> Windows malware loader — `.cmd` → `.exe` → Lua-DLL payload chain). **Do not download or run any
> "isms\_builder" ZIP/installer/exe from anywhere other than this repository.**
> If you find a suspicious repo or site impersonating this project, please open an
> [issue](https://github.com/coolstartnow/isms-builder/issues) or a
> [discussion](https://github.com/coolstartnow/isms-builder/discussions) so we can flag it.

---

> **Status: Active development — not yet a finished product.**
> The core modules are functional and in use, but some features are incomplete
> and the platform is still growing. Contributions, feedback and real-world
> testing are very welcome — that is exactly why this was open-sourced.

---

## What is ISMS Builder?

ISMS Builder is a **self-hosted web platform** for managing an Information Security Management System (ISMS).
It covers the full compliance lifecycle — from policy authoring to audit evidence — for ISO 27001:2022, NIS2, GDPR/DSGVO, BSI IT-Grundschutz and other frameworks.

**No cloud. No SaaS fees. Your data stays on your server.**

> Designed for SMEs, IT teams, and consultants who need a real ISMS tool without a five-figure vendor contract.

---

## Intended Use and Scope

This project began as a working tool for a single ISMS practitioner and grew from there. It is
open source because the work may be useful to others — not because it is a commercial product in
disguise. Being explicit about that helps you decide whether it fits your situation.

**What it is built for.** A small ISMS team — often one person, sometimes a handful — that
authors and maintains the documentation of a management system: policies, risks, assets,
controls, evidence. The number of people who *need an account* is expected to stay small.
Reaching a large audience works without accounts: policy acknowledgements are sent as
token-based links, so recipients read and confirm a document without ever logging in, and
without appearing in any user list.

**What it expects of you.** ISMS Builder is self-hosted, and everything that follows from that
is yours: deployment, TLS, hardening, backups, updates, access control, and the data protection
obligations for whatever you store in it. The project ships a reasonable default configuration,
not a managed service.

**What it is not.** There is no hosted SaaS offering, no commercial support contract, and no
service-level agreement. It is not a multi-tenant hosting product. It does not certify you
against any standard, and it is not legal advice — it helps you organise and evidence the work,
but the assessment remains yours and your auditor's.

**Who maintains it.** One person, alongside a full-time job. Issues and discussions are read and
answered, usually within days; security reports are prioritised. Feature requests are welcome and
genuinely shape the roadmap, but they compete for limited evenings. If your organisation depends
on a fixed timeline or guaranteed response, a commercial vendor is the honest recommendation —
and that is not a reason to avoid the project, only a reason to plan realistically.

---

## Screenshots

| Login | Dashboard |
| --- | --- |
| ![Login](https://assets.kitploit.com/production/public/readmes/12462/dad90b27558016928f149aa956d5b5ecef78f7639fe00117fa6e7b6b9c610884.png) | ![Dashboard](https://assets.kitploit.com/production/public/readmes/12462/ad427999a2d247f7b486faff089572c213b6bf809d64946438305c1519e54566.png) |

| Statement of Applicability | Risk Management |
| --- | --- |
| ![SoA](https://assets.kitploit.com/production/public/readmes/12462/19133912a32d643c4db93e977047aa6f93cc85889555a63dc29b986f5290d196.png) | ![Risks](https://assets.kitploit.com/production/public/readmes/12462/19133912a32d643c4db93e977047aa6f93cc85889555a63dc29b986f5290d196.png) |

| GDPR & Datenschutz | Asset Management |
| --- | --- |
| ![GDPR](https://assets.kitploit.com/production/public/readmes/12462/453b4e84b6c08241d87e8edd96d803a68b5d56565aee2b317444f30db8d9ffb5.png) | ![Assets](https://assets.kitploit.com/production/public/readmes/12462/053332b35c995bc3a672be7bfd193ca3789f3245e7cdffaa456833fabdec309e.png) |

| Guidance & Dokumentation | Reports |
| --- | --- |
| ![Guidance](https://assets.kitploit.com/production/public/readmes/12462/2eb44e0df23e8eba8d70e09a14a18028d1d9dc37e8e734d0c837f2b7fe6ec787.png) | ![Reports](https://assets.kitploit.com/production/public/readmes/12462/765395a2a3cf39ec72a00ad53df464bc79d54a69ca34738bdeb775ff7e1584f3.png) |

> Run `npm start` and open `https://localhost:3000` to explore the full demo dataset locally.

---

## Feature Overview

| Module | Description | Standards |
| --- | --- | --- |
| **Policy Management** | Template CRUD, versioning, lifecycle (draft → review → approved → archived), space hierarchy, attachments | ISO 27001 §5 |
| **Statement of Applicability** | 313 controls across 8 frameworks, inline editing, gap analysis, cross-mapping | ISO 27001 A / BSI / NIS2 / EUCS / EUAI / ISO 9001 / CRA |
| **Risk Management** | Risk register, treatment plans, auditor role | ISO 27001 §6.1 |
| **Security Goals** | KPI tracking with progress bars, calendar integration | ISO 27001 §6.2 |
| **GDPR & Privacy** | VVT, AV-contracts, DSFA, TOMs, DSAR queue, 72h-timer, deletion log with email alerts | DSGVO Art. 13–35 |
| **Asset Management** | Asset register, editable asset types, protection goals (CIA + authenticity) with dependency inheritance, classification levels, EoL tracking | ISO 27001 A.5.9–5.12 |
| **BCM / BCP** | Business Impact Analysis, continuity plans, exercises | ISO 27001 A.5.29–5.30 / NIS2 |
| **Training Records** | Training catalogue, completion tracking, certificate upload | ISO 27001 A.6.3 |
| **Supplier Management** | Vendor register, audit scheduling, risk assessment | ISO 27001 A.5.19–5.22 |
| **Legal & Contracts** | Contracts, NDAs, privacy policies, expiry calendar |  |
| **Incident Inbox** | CISO inbox + **public reporting form** (no login required) | NIS2 / BSI |
| **Governance** | Management reviews, action tracking...