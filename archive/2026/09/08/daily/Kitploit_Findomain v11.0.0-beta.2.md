---
title: Findomain v11.0.0-beta.2
url: https://kitploit.com/en/posts/github-findomain-findomain-1100-beta2
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:05.335631
---

# Findomain v11.0.0-beta.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/3889/e0a9df21a9e68ffbbd2f765c95be6af793acd31efff88e8d21f805cc2cf52068.png)

New releaseSep 8, 2026

# Findomain v11.0.0-beta.2

The fastest and complete solution for domain recognition. Supports screenshoting, port scan, HTTP check, data import from other tools, subdomain monitoring, alerts via Discord, Slack and Telegram, multiple API Keys for sources and much more.

Share

[![Follow on Twitter](https://img.shields.io/twitter/follow/edu4rdshl.svg?logo=twitter)](https://twitter.com/edu4rdshl)
[![Follow on Twitter](https://img.shields.io/twitter/follow/FindomainApp.svg?logo=twitter)](https://twitter.com/FindomainApp)

[![Travis CI Status](https://travis-ci.org/edu4rdshl/findomain.svg?branch=master)](https://travis-ci.org/edu4rdshl/findomain)
[![Appveyor CI Status](https://ci.appveyor.com/api/projects/status/github/edu4rdshl/findomain?branch=master&svg=true)](https://ci.appveyor.com/project/edu4rdshl/findomain)
[![Build status](https://github.com/Edu4rdSHL/findomain/workflows/Github%20Actions/badge.svg)](https://github.com/Edu4rdSHL/findomain/actions)

# Findomain

![Findomain](https://assets.kitploit.com/production/public/readmes/3889/c56d4f9f4cadd83cf99a297dd8745ed4df4c129cb0ba9604029396417a57f224.png)

The complete solution for domain recognition. Supports screenshotting, port scanning, importing data from other tools, subdomain monitoring, and more. Be alerted on your findings through services such as Discord, Slack, and Telegram. Multiple API Keys for sources and much more.

## Chat with us

[![Chat on Discord](https://img.shields.io/discord/697050821057183777.svg?logo=discord)](https://discord.gg/y5JaRbX)

# What Can Findomain Do?

The following table demonstrates features that are available in the premium version (but not the free version) of Findomain. It aims to gives you an idea of why you should use Findomain and what it can do for you. The domain used for the test was aol.com. The details of the [BlackArch](https://blackarch.org) virtual machine used in the test are outlined below:

root@kitploit:~

```
Host: KVM/QEMU (Standard PC (i440FX + PIIX, 1996) pc-i440fx-3.1)
Kernel: 5.2.6-arch1-1-ARCH
CPU: Intel (Skylake, IBRS) (4) @ 2.904GHz
Memory: 139MiB / 3943MiB
```

The tool used to calculate the time was Linux's `time` command.

| Enumeration Tool | Search Time | Total Subdomains Found | CPU Usage | RAM Usage |
| --- | --- | --- | --- | --- |
| Findomain | real 0m5.515s | 84110 | Very Low | Very Low |

**Summary:** 84110 subdomains in 5.5 seconds.

# Features

* Subdomains monitoring: put data to Discord, Slack or Telegram webhooks. See [Subdomains Monitoring](https://github.com/findomain/findomain/blob/master/README.md#subdomains-monitoring) for more information.
* Multi-thread support for API querying, it makes that the maximun time that Findomain will take to search subdomains for any target is 15 seconds (in case of API's timeout).
* Parallel support for subdomains resolution, in good network conditions can resolv about 3.5k of subdomains per minute.
* DNS over TLS support.
* Specific IPv4 or IPv6 query support.
* Discover subdomains without brute-force, it tool uses Certificate Transparency Logs and APIs.
* Discover only resolved subdomains.
* Discover subdomains IP for data analysis.
* Read target from user argument (-t) or file (-f).
* Write to one unique output file specified by the user all or only resolved subdomains.
* Write results to automatically named TXT output file(s).
* Hability to query directly the Findomain database created with [Subdomains Monitoring](https://github.com/findomain/findomain/blob/master/docs/INSTALLATION.md#subdomains-monitoring) for previous discovered subdomains.
* Hability to import and work data discovered by other tools. See [Working with other tools](https://github.com/findomain/findomain/blob/master/README.md#working-with-other-tools).
* Quiet mode to run it silently.
* Cross platform support: Any platform, it's written in Rust and Rust is multiplatform. See [the documentation](https://github.com/findomain/findomain/blob/master/docs/INSTALLATION.md#build-for-32-bits-or-another-platform) for instructions.
* Multiple API support.
* Possibility to use as subdomain resolver.
* Subdomain wildcard detection for accurate results.
* Support for subdomain discover using bruteforce method.
* Support for configuration file in TOML, JSON, INI or YAML format.
* Custom DNS IP addresses for fast subdomains resolving (more than 60 per second by default, adjustable using the `--threads` option.

# Findomain in Depth

See [Subdomains Enumeration: what is, how to do it, monitoring automation using webhooks and centralizing your findings](https://medium.com/%40edu4rdshl/subdomains-enumeration-what-is-how-to-do-it-monitoring-automation-using-webhooks-and-5e0a0c6d9127) for a detailed guide, including real-world examples, of how to get the most out of the tool.

# How Does It Work?

Findomain uses Certificate Transparency logs and well-tested APIs to find subdomains. This method makes the tool much faster and more reliable than alternatives. If you want to know more about Certificate Transparency logs, read <https://www.certificate-transparency.org/>

Findomain queries 54 passive sources. Every one of them parses a documented
data format, JSON in almost every case: there is no HTML scraping anywhere, so a
redesigned web page can never quietly turn results into noise. Paginated APIs are
walked to the last page.

* [360 PassiveDNS](https://passivedns.cn) `**`
* [Ahrefs](https://ahrefs.com/api) `**`
* [AlienVault OTX](https://otx.alienvault.com) `**`
* [AnubisDB](https://jldc.me/anubis/)
* [Arquivo.pt](https://arquivo.pt/api)
* [BeVigil](https://bevigil.com/osint-api) `**`
* [BinaryEdge](https://binaryedge.io) `**`
* [BufferOver (free)](https://tls.bufferover.run) `**`
* [BufferOver (paid)](https://rapidapi.com/bufferover/api/bufferover-run-tls) `**`
* [BuiltWith](https://api.builtwith.com) `**`
* [C99](https://api.c99.nl) `**`
* [Censys](https://search.censys.io) `**`
* [CertSpotter](https://sslmate.com/certspotter/) `*`
* [Chaos](https://chaos.projectdiscovery.io) `**`
* [CIRCL PassiveDNS](https://www.circl.lu/services/passive-dns/) `**`
* [CommonCrawl](https://commoncrawl.org)
* [Crt.sh (database mirror)](https://crt.sh)
* [Deepinfo](https://deepinfo.com) `**`
* [Detectify](https://detectify.com) `**`
* [DigiCert CertCentral](https://daas.digicert.com) `**`
* [DNSlytics](https://dnslytics.com) `**`
* [DNSRepo](https://dnsrepo.noc.org) `**`
* [Facebook CT](https://developers.facebook.com/docs/certificate-transparency) `**`
* [Farsight DNSDB](https://www.domaintools.com/products/farsight-dnsdb/) `**`
* [FOFA](https://fofa.info) `**`
* [FullHunt](https://fullhunt.io) `**`
* [HackerTarget](https://hackertarget.com) `*`
* [Hunter.io](https://hunter.io/api-documentation) `**`
* [IntelX](https://intelx.io) `**`
* [LeakIX](https://leakix.net) `**`
* [Maltiverse](https://maltiverse.com)
* [Mnemonic PassiveDNS](https://docs.mnemonic.no/display/public/API/PassiveDNS%2BOverview)
* [Netlas](https://netlas.io) `**`
* [ONYPHE](https://www.onyphe.io) `**`
* [PassiveTotal](https://community.riskiq.com) `**`
* [Pentest-Tools](https://pentest-tools.com) `**`
* [PublicWWW](https://publicwww.com) `**`
* [Pulsedive](https://pulsedive.com) `**`
* [Quake](https://quake.360.cn) `**`
* [SecurityTrails](https://docs.securitytrails.com/docs) `**`
* [Shodan](https://www.shodan.io) `**`
* [SOCRadar](https://socradar.io) `**`
* [Spamhaus PassiveDNS](https://www.spamhaus.com) `**`
* [Subdomain Center](https://www.subdomain.center)
* [Sublist3r](https://api...