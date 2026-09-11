---
title: uac v3.4.0
url: https://kitploit.com/en/posts/github-tclahr-uac-v340
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:42.376283
---

# uac v3.4.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4174/0ae4961254882e04ca26ce38468c4526703cff9d76d6242b52af6cf4cff8146c.gif)

New releaseSep 10, 2026

# uac v3.4.0

Portable, dependency-free incident response tool that automates forensic artifact collection from Unix-like systems, including memory acquisition, process hashing, and bodyfile creation via customizable YAML profiles.

Share

![logo](https://raw.githubusercontent.com/tclahr/uac/HEAD/logo/uac-dark.svg)

## Unix-like Artifacts Collector (UAC)

[![shellcheck_badge](https://github.com/tclahr/uac/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tclahr/uac/actions/workflows/shellcheck.yaml)
[![bestpractices_badge](https://bestpractices.coreinfrastructure.org/projects/5640/badge)](https://bestpractices.coreinfrastructure.org/projects/5640)
[![release_badge](https://img.shields.io/github/v/release/tclahr/uac?include_prereleases&style=flat-square)](https://github.com/tclahr/uac/releases)
[![license_badge](https://img.shields.io/github/license/tclahr/uac?style=flat-square)](https://github.com/tclahr/uac/LICENSE)

[About](#-about-uac)
•
[Documentation](#-documentation)
•
[Main Features](#-main-features)
•
[Supported Operating Systems](#-supported-operating-systems)
•
[Usage](#-usage)
•
[Contributing](#-contributing)
•
[Support](#-support)
•
[License](#-license)

## 🔎 About UAC

**UAC (Unix-like Artifacts Collector)** is a powerful and extensible incident response tool designed for forensic investigators, security analysts, and IT professionals. It automates the collection of artifacts from a wide range of Unix-like systems, including AIX, ESXi, FreeBSD, Linux, macOS, NetBSD, NetScaler, OpenBSD and Solaris.

Whether you're handling an intrusion, conducting forensic investigations, or performing compliance checks, UAC simplifies and accelerates data collection while minimizing reliance on external support during critical incidents.

### Key Highlights

* 📂 Fully customizable via YAML profiles for tailored data collection.
* ⚡ Lightweight, portable, and requires no installation or dependencies.
* 🔒 Adheres to the order of volatility to ensure reliable data acquisition.
* 🛠 Designed for diverse environments, including IoT devices and NAS systems.

![UAC in Action](https://assets.kitploit.com/production/public/readmes/4174/0ae4961254882e04ca26ce38468c4526703cff9d76d6242b52af6cf4cff8146c.gif)

## 📘 Documentation

Full documentation is available at the [project documentation page](https://tclahr.github.io/uac-docs).

## 🌟 Main Features

* Run everywhere with no dependencies (no installation required).
* Customizable and extensible collections and artifacts.
* Respect the order of volatility during artifact collection.
* Collect information about current running processes (including processes without a binary on disk).
* Hash running processes and executable files.
* Extract files and directories status to create a bodyfile.
* Collect system and user-specific data, configuration files, and logs.
* Acquire volatile memory from Linux systems using different methods and tools.
* Support to write output to various cloud platforms.

## 💾 Supported Operating Systems

UAC runs on any Unix-like system, regardless of the processor architecture. All UAC needs is shell :)

[![AIX](https://img.shields.io/static/v1?label=&message=AIX&color=brightgreen&style=for-the-badge)](#-supported-operating-systems)
[![ESXi](https://img.shields.io/static/v1?label=&message=ESXi&color=blue&style=for-the-badge)](#-supported-operating-systems)
[![FreeBSD](https://img.shields.io/static/v1?label=&message=FreeBSD&color=red&style=for-the-badge)](#-supported-operating-systems)
[![Linux](https://img.shields.io/static/v1?label=&message=Linux&color=lightgray&style=for-the-badge)](#-supported-operating-systems)
[![macOS](https://img.shields.io/static/v1?label=&message=macOS&color=blueviolet&style=for-the-badge)](#-supported-operating-systems)
[![NetBSD](https://img.shields.io/static/v1?label=&message=NetBSD&color=orange&style=for-the-badge)](#-supported-operating-systems)
[![NetScaler](https://img.shields.io/static/v1?label=&message=NetScaler&color=blue&style=for-the-badge)](#-supported-operating-systems)
[![OpenBSD](https://img.shields.io/static/v1?label=&message=OpenBSD&color=yellow&style=for-the-badge)](#-supported-operating-systems)
[![Solaris](https://img.shields.io/static/v1?label=&message=Solaris&color=lightblue&style=for-the-badge)](#-supported-operating-systems)

*Note: UAC even runs on systems like Network Attached Storage (NAS) devices, Network devices such as OpenWrt, and IoT devices.*

## 🚀 Usage

UAC does not need to be installed on the target system. Simply download the latest version from the [releases page](https://github.com/tclahr/uac/releases), uncompress it, and launch. It's that simple!

### 🛠 Getting Started

1. Download the latest release from the [Releases page](https://github.com/tclahr/uac/releases).
2. Uncompress the archive.
3. Execute the tool directly from the terminal.

### Examples

Click to view usage examples

**Collect all artifacts based on the ir\_triage profile:**

root@kitploit:~

```
./uac -p ir_triage /tmp
```

**Collect memory dump and all artifacts based on the full profile:**

root@kitploit:~

```
./uac -a ./artifacts/memory_dump/avml.yaml -p full /tmp
```

**Collect all artifacts excluding a specific one:**

root@kitploit:~

```
./uac -p full -a \!artifacts/bodyfile/bodyfile.yaml .
```

**Collect all artifacts based on the ir\_triage profile, along with all artifacts located in the /my\_custom\_artifacts directory:**

root@kitploit:~

```
./uac -p ir_triage -a /my_custom_artifacts/\* /mnt/sda1
```

**Collect all artifacts based on a custom profile:**

root@kitploit:~

```
./uac -p /my_custom_uac_data/my_custom_uac_profile.yaml /tmp
```

## 💙 Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Have you created any artifacts? Please share them with us!

You can contribute with new artifacts, profiles, bug fixes, or propose new features. Please read our [Contributing Guide](https://github.com/tclahr/uac/blob/main/CONTRIBUTING.md) before submitting a Pull Request to the project.

## 👨‍💻 Support

For general help using UAC, please refer to the [project documentation page](https://tclahr.github.io/uac-docs). For additional help, you can use one of the following channels:

* [Discord](https://discord.com/invite/digitalforensics) (For live discussion with the community and UAC team)
* [GitHub](https://github.com/tclahr/uac/issues) (Bug reports and contributions)
* [Twitter](https://twitter.com/tclahr) (Get the news fast)

## ⭐ Support the Project

If you find UAC helpful, please give us a ⭐ on [GitHub](https://github.com/tclahr/uac)! This helps others discover the project and motivates us to improve it further.

## 📜 License

The UAC project uses the [Apache License Version 2.0](https://github.com/tclahr/uac/blob/main/LICENSE) software license.

[Read more](/en/tools/github/tclahr/uac?expand=1)

## Categories

[Memory Forensics](/en/categories/memory-forensics)[Forensics](/en/categories/forensics)[Information Gathering](/en/categories/information-gathering)[Digital Forensics](/en/categories/digital-forensics)[Utilities & Frameworks](/en/categories/utilities-frameworks)[Incident Response](/en/categories/incident-response)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a dire...