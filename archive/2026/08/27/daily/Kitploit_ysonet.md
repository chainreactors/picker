---
title: ysonet
url: https://kitploit.com/en/tools/github/irsdl/ysonet
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:34.797097
---

# ysonet

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/irsdl/ysonet

![](https://assets.kitploit.com/production/public/tools/53351/36f05e51cb9a1e88d0906b22fc1836f22b80fd7471413717a95bd4b242064e77-display-v1.webp)

[Payload Generation](/en/categories/payload-generation)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Web Security](/en/categories/web-security)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)

![GitHub](/providers/github.png)irsdl/ysonet

# ysonet

Deserialization payload generator for a variety of .NET formatters

[View Repository](https://github.com/irsdl/ysonet)

22727193 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![YSoNet logo](https://assets.kitploit.com/production/public/readmes/53351/36f05e51cb9a1e88d0906b22fc1836f22b80fd7471413717a95bd4b242064e77/aaf975c9de78dc73b5dc22cee372cc21fab4708f645a3cb43c2c40cfd8339eb3-display-v1.webp)

**YSoNet** is a fork of the original [YSoSerial.Net](https://github.com/pwntester/ysoserial.net), currently maintained by [@irsdl](https://github.com/irsdl).

* Sites: [ysonet.net](https://ysonet.net) or [ysonet.com](https://ysonet.com) (both open this repo).

---

[![Build](https://github.com/irsdl/ysonet/actions/workflows/build.yml/badge.svg)](https://github.com/irsdl/ysonet/actions/workflows/build.yml)
[![License](https://img.shields.io/github/license/irsdl/ysonet)](https://github.com/irsdl/ysonet/blob/master/LICENSE.txt)
[![Download](https://img.shields.io/github/v/release/irsdl/ysonet?label=download)](https://github.com/irsdl/ysonet/releases/latest)

A proof-of-concept tool for generating payloads that exploit unsafe .NET object deserialization.

## What is YSoNet

YSoNet (previously known as ysoserial.net) is a collection of utilities and property-oriented programming "gadget chains" discovered in common .NET libraries that can, under the right conditions, exploit .NET applications performing unsafe deserialization of objects. You give it a command and a gadget chain; it wraps the command in the chain and serializes the result to stdout. When a vulnerable application deserializes that data, the chain runs and your command executes on the host.

The vulnerability lies in the application performing unsafe deserialization, NOT in having gadgets on the classpath. This project is inspired by [Chris Frohoff's ysoserial project](https://github.com/frohoff/ysoserial).

[Download Tool](https://github.com/irsdl/ysonet)

## Important for defenders and AI reviewers

Do not turn YSoNet's gadget and plugin catalog into a deserialization blocklist. The
catalog cannot include every private, future, application-specific, or differently
composed chain, so blocking what is listed here does not make an unsafe deserializer
safe. It can create false assurance while only delaying an attack.

If you are reviewing this repository to harden an application, read
[Security guidance for defenders and reviewers](https://github.com/irsdl/ysonet/blob/HEAD/SECURITY.md) before inspecting the
gadgets or plugins. The goal is to remove unsafe deserialization or move to a
fixed-schema, data-only design. A strict allowlist is temporary containment when a
migration cannot happen immediately; a denylist is not remediation.

## Documentation

The full documentation lives in [docs/](https://github.com/irsdl/ysonet/blob/HEAD/docs/README.md):

* [Security Guidance](https://github.com/irsdl/ysonet/blob/HEAD/SECURITY.md) - why gadget blocklists are not a fix and how to
  redesign the deserialization boundary.
* [Dependency Security Notes](https://github.com/irsdl/ysonet/blob/HEAD/docs/dependency-security.md) - the vulnerable and outdated
  libraries YSoNet pins on purpose, and how to triage a scanner alert.
* [Getting Started](https://github.com/irsdl/ysonet/blob/HEAD/docs/getting-started.md) - install, build from source, and the interactive wizard.
* [Usage and Examples](https://github.com/irsdl/ysonet/blob/HEAD/docs/usage-and-examples.md) - command-line options and worked examples.
* [Gadgets and Plugins](https://github.com/irsdl/ysonet/blob/HEAD/docs/gadgets-and-plugins.md) - the full gadget and plugin catalog.
* [References](https://github.com/irsdl/ysonet/blob/HEAD/docs/references.md) - the background reading, talks, and sources this project draws on.
* [.NET Deserialization Research](https://github.com/irsdl/ysonet/blob/HEAD/docs/dotnet-deserialization-research.md) - the wider reading list: tools, uses in the wild, and CTF write-ups.
* [Credits](https://github.com/irsdl/ysonet/blob/HEAD/docs/credits.md) - who built the tool and found the gadgets and plugins.
* [Sponsors](https://github.com/irsdl/ysonet/blob/HEAD/docs/sponsors.md) - the people funding the work.

## Quick start (interactive mode)

New to this tool? The easiest way to start is interactive mode: a menu-driven wizard that lists the gadgets and plugins, explains each setting, and builds the payload for you - no need to memorize flags first.

root@kitploit:~

```
.\ysonet.exe -i
```

(`interactive`, `wizard`, and `--interactive` work too.) You need `ysonet.exe` first - see [Getting Started](https://github.com/irsdl/ysonet/blob/HEAD/docs/getting-started.md). Full wizard walkthrough is there too.

## Quick start (command line)

root@kitploit:~

```
./ysonet.exe -f Json.Net -g ObjectDataProvider -o raw -c "calc" -t
```

See all options with `ysonet.exe --fullhelp`, and per-gadget or per-plugin help with `-g NameHere -help` or `-p NameHere -help`. More in [Usage and Examples](https://github.com/irsdl/ysonet/blob/HEAD/docs/usage-and-examples.md).

## Build from source

Needs Windows, MSBuild from Visual Studio 2022 or the Build Tools (".NET desktop
development" workload), and `nuget.exe`. Every project targets .NET Framework 4.7.2.

root@kitploit:~

```
git clone https://github.com/irsdl/ysonet
cd ysonet
nuget restore ysonet.sln
msbuild ysonet.sln -p:Configuration=Release   # or Debug

.\ysonet\bin\Release\ysonet.exe -h
```

* A Release build also needs the Windows optional feature ".NET Framework 3.5 (includes
  .NET 2.0 and 3.0)" to compile the shipped CLR2 local-test host, and fails without it. A
  Debug build only warns.
* Release string-encrypts `ysonet.exe` to cut antivirus false positives; payload bytes are
  unchanged. Skip it with `-p:ObfuscateRelease=false`. Debug is never obfuscated.
* Full setup, including a one-liner that installs the toolchain: [Getting Started](https://github.com/irsdl/ysonet/blob/HEAD/docs/getting-started.md#build-from-source).

## Testing

A Debug build runs the fast test suite automatically, and a failed test fails the build
(skip it with `-p:RunYsonetTests=false`). The exhaustive FULL suite is opt-in:

root@kitploit:~

```
.\ysonet\bin\Debug\ysonet.Tests.exe --full
```

Both are safe: commands are self-closing or never executed, and listeners are loopback
only. Details and the other opt-in tiers: [Getting Started](https://github.com/irsdl/ysonet/blob/HEAD/docs/getting-started.md#te...