---
title: mvt v2026.9.7
url: https://kitploit.com/en/posts/github-mvt-project-mvt-v202697
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:15.439719
---

# mvt v2026.9.7

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50793/1605f162836af7a174773d88d2ceb5d657380572ff859d347f6e94a916cc2598-display-v1.webp)

New releaseSep 8, 2026

# mvt v2026.9.7

Forensic collection and analysis toolkit for Android and iOS devices to identify potential compromise by known spyware using public and private indicators of compromise.

Share

![](https://assets.kitploit.com/production/public/readmes/50793/aeb46226919236e8db29c8ad66f256a5ee8d41a6f7a971b5ccc4dcec0bd5c7e3/49deb9c44bd813e596fed4b35334f0b8ff6f633b14238c927dce7137c1bd71d9-display-v1.webp)

# Mobile Verification Toolkit

> [!IMPORTANT]
> We recently merged the "v3" branch. This introduced breaking changes. If you relied on mvt output in other scripts They might have broken. More details: <https://github.com/mvt-project/mvt/issues/757>

[![](https://img.shields.io/pypi/v/mvt)](https://pypi.org/project/mvt/)
[![Documentation Status](https://readthedocs.org/projects/mvt/badge/?version=latest)](https://docs.mvt.re/en/latest/?badge=latest)
[![CI](https://github.com/mvt-project/mvt/actions/workflows/tests.yml/badge.svg)](https://github.com/mvt-project/mvt/actions/workflows/tests.yml)
[![Downloads](https://pepy.tech/badge/mvt)](https://pepy.tech/project/mvt)

Mobile Verification Toolkit (MVT) is a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices.

It has been developed and released by the [Amnesty International Security Lab](https://securitylab.amnesty.org) in July 2021 in the context of the [Pegasus Project](https://forbiddenstories.org/about-the-pegasus-project/) along with [a technical forensic methodology](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/). It continues to be maintained by Amnesty International and other contributors.

> **Note**
> MVT is a forensic research tool intended for technologists and investigators. It requires understanding digital forensics and using command-line tools. This is not intended for end-user self-assessment. If you are concerned with the security of your device please seek reputable expert assistance.

### Indicators of Compromise

MVT supports using public [indicators of compromise (IOCs)](https://github.com/mvt-project/mvt-indicators) to scan mobile devices for potential traces of targeting or infection by known spyware campaigns. This includes IOCs published by [Amnesty International](https://github.com/AmnestyTech/investigations/) and other research groups.

> **Warning**
> Public indicators of compromise are insufficient to determine that a device is "clean", and not targeted with a particular spyware tool. Reliance on public indicators alone can miss recent forensic traces and give a false sense of security.
>
> Reliable and comprehensive digital forensic support and triage requires access to non-public indicators, research and threat intelligence.
>
> Such support is available to civil society through [Amnesty International's Security Lab](https://securitylab.amnesty.org/get-help/?c=mvt_docs) or through our forensic partnership with [Access Now’s Digital Security Helpline](https://www.accessnow.org/help/).

More information about using indicators of compromise with MVT is available in the [documentation](https://docs.mvt.re/en/latest/iocs/).

## Installation

MVT can be installed from sources or from [PyPI](https://pypi.org/project/mvt/) (you will need some dependencies, check the [documentation](https://docs.mvt.re/en/latest/install/)):

root@kitploit:~

```
pip3 install mvt
```

You can also install MVT from PyPI with [uv](https://docs.astral.sh/uv/). First, install uv:

root@kitploit:~

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install MVT as a command-line tool:

root@kitploit:~

```
uv tool install mvt
```

For alternative installation options and known issues, please refer to the [documentation](https://docs.mvt.re/en/latest/install/) as well as [GitHub Issues](https://github.com/mvt-project/mvt/issues).

## Usage

MVT provides three commands: `mvt-ios` and `mvt-android` analyse acquisitions from devices of that platform, and `mvt` hosts what belongs to neither: `version`, `completion`, `plugins` and `download-iocs` (`version` and `download-iocs` remain available on the platform commands for now). Running `mvt` on its own shows the installed version, update notices and the available commands. [Check out the documentation to learn how to use them!](https://docs.mvt.re/)

Pass `--verbose` to any of the three commands, before the command name (`mvt-ios --verbose check-backup ...`), for debug output. The `--verbose` option the `check-*` commands accept after their name still works but is kept for compatibility only and will be removed in a future release.

### Shell completion

MVT can generate a shell completion script for Bash, Zsh, and Fish which covers `mvt`, `mvt-ios` and `mvt-android`:

root@kitploit:~

```
mvt completion
```

The command prints setup instructions by default. To generate the completion script directly, pass the shell name:

root@kitploit:~

```
mvt completion bash
```

MVT only writes completion files or shell configuration when `--install` is passed. See the [command completion documentation](https://docs.mvt.re/en/latest/command_completion/) for details.

Plugin packages extend MVT with additional forensic modules, which run inside
the `check-*` commands, and with top-level commands on `mvt`, `mvt-ios` and
`mvt-android`. See the
[development documentation](https://docs.mvt.re/en/latest/development/) for
writing and installing them, and the
[custom CLI command documentation](https://docs.mvt.re/en/latest/development/custom_commands/)
for the entry points a package registers commands in.

## License

The purpose of MVT is to facilitate the ***consensual forensic analysis*** of devices of those who might be targets of sophisticated mobile spyware attacks, especially members of civil society and marginalized communities. We do not want MVT to enable privacy violations of non-consenting individuals. In order to achieve this, MVT is released under its own license. [Read more here.](https://docs.mvt.re/en/latest/license/)

[Read more](/en/tools/github/mvt-project/mvt?expand=1)

## Categories

[Android Security](/en/categories/android-security)[Disk Forensics](/en/categories/disk-forensics)[Indicator of Compromise (IOC) Management](/en/categories/ioc-management)[iOS Security](/en/categories/ios-security)[Forensics](/en/categories/forensics)[Mobile Forensics](/en/categories/mobile-forensics)[Digital Forensics](/en/categories/digital-forensics)[Mobile Security](/en/categories/mobile-security)[Threat Intelligence](/en/categories/threat-intelligence)[Incident Response](/en/categories/incident-response)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories