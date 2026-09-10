---
title: Empire v7.0.2
url: https://kitploit.com/en/posts/github-bc-security-empire-v702
source: Kitploit
date: 2026-09-09
fetch_date: 2026-09-10T06:47:22.605680
---

# Empire v7.0.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/47525/729a4216e2c21f980b772126f5f14edcf49062a6a3802549c8e8f613aef8958c.png)

New releaseSep 9, 2026

# Empire v7.0.2

Empire is a post-exploitation and adversary emulation framework that is used to aid Red Teams and Penetration Testers.

Share

![Empire](https://assets.kitploit.com/production/public/readmes/47525/866d49f2602585d03ce30af4c3dec36745ce2099e4ac2a1f6bc0a3aa8d60cf01.jpg)
[![Donate](https://img.shields.io/badge/Donate-Sponsor-blue?style=plastic&logo=github)](https://github.com/sponsors/BC-SECURITY)
[![Docs](https://img.shields.io/badge/Wiki-Docs-green?style=plastic&logo=wikipedia)](https://bc-security.gitbook.io/empire-wiki/)
[![Discord](https://img.shields.io/discord/716165691383873536?style=plastic&logo=discord)](https://discord.gg/P8PZPyf)
[![Blog](https://img.shields.io/badge/Blog-Read%20me-orange?style=plastic&logo=wordpress)](https://www.bc-security.org/blog)
[![Twitter URL](https://img.shields.io/twitter/follow/BCSecurity?style=plastic&logo=twitter)](https://twitter.com/BCSecurity)
[![Twitter URL](https://img.shields.io/twitter/follow/EmpireC2Project?style=plastic&logo=twitter)](https://twitter.com/EmpireC2Project)
[![YouTube URL](https://img.shields.io/youtube/channel/views/UCIV4xSntF1h1bvFt8SUfzZg?style=plastic&logo=youtube)](https://www.youtube.com/channel/UCIV4xSntF1h1bvFt8SUfzZg)
[![LinkedIn](https://img.shields.io/badge/Linkedin-blue?style=plastic&logo=linkedin&logoColor=#0A66C2)](https://www.linkedin.com/company/bc-security/)

# Empire

Empire is a post-exploitation and adversary emulation framework that is used to aid Red Teams and Penetration Testers. The Empire server is written in Python 3 and is modular to allow operator flexibility. Empire comes built-in with a client that can be used remotely to access the server. There is also a GUI available for remotely accessing the Empire server, [Starkiller](https://github.com/BC-SECURITY/Starkiller).

### Features

* Server/Client Architecture for Multiplayer Support
* Fully encrypted communications
* HTTP/S, Malleable HTTP, Foreign, Hop, SMB, and Port Forward Pivot Listeners
* Massive library (400+) of supported tools in PowerShell, C#, & Python
* Donut Integration for shellcode generation
* Modular plugin interface for custom server features
* Flexible module interface for adding new tools
* Integrated obfuscation using [ConfuserEx 2](https://github.com/mkaring/ConfuserEx) & [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)
* In-memory .NET assembly execution
* Customizable Bypasses
* JA3/S and JARM Evasion
* MITRE ATT&CK Integration
* Integrated Roslyn compiler (Thanks to [Covenant](https://github.com/cobbr/Covenant))
* Docker, Kali, ParrotOS, Ubuntu 22.04/24.04, and Debian 12/13 Install Support

### Agents

* PowerShell
* Python 3
* C#
* IronPython 3
* Go

### Modules

* [Assembly Execution](https://github.com/BC-SECURITY/Empire/blob/main/empire/server/data/module_source/code_execution/Invoke-Assembly.ps1)
* [BOF Execution](https://github.com/airbus-cert/Invoke-Bof)
* [Mimikatz](https://github.com/gentilkiwi/mimikatz)
* [Seatbelt](https://github.com/GhostPack/Seatbelt)
* [Rubeus](https://github.com/GhostPack/Rubeus)
* [SharpSploit](https://github.com/cobbr/SharpSploit)
* [Certify](https://github.com/GhostPack/Certify)
* [ProcessInjection](https://github.com/3xpl01tc0d3r/ProcessInjection)
* And Many More

## Sponsors

[![](https://assets.kitploit.com/production/public/readmes/47525/b81df4883f8973d8fbda22924a9ce0966337b619548cfe6616a5d7d0c0bc1a15.png)](https://www.route4me.com//)

[![](https://assets.kitploit.com/production/public/readmes/47525/a071203172031edfaf05bba03ffe1e032d8b680ab55a99a823935653cf2e9e87.png)](https://www.instagram.com/purpl3_cult/)

## Release Notes

Please see our [Releases](https://github.com/BC-SECURITY/Empire/releases) or [Changelog](https://github.com/bc-security/empire/blob/main/CHANGELOG.md) page for detailed release notes.

### Quickstart

root@kitploit:~

```
git clone https://github.com/BC-SECURITY/Empire.git
```

Check out the [Installation Page](https://bc-security.gitbook.io/empire-wiki/quickstart/installation) for install instructions.

Note: The `main` branch is a reflection of the latest changes and may not always be stable.
After cloning the repo, you can checkout the latest stable release by running the `setup/checkout-latest-tag.sh` script.

root@kitploit:~

```
git clone https://github.com/BC-SECURITY/Empire.git
cd Empire
./setup/checkout-latest-tag.sh
./ps-empire install -y
```

If you are using the sponsors version of Empire, it will pull the sponsors version of Starkiller.
Because these are private repositories, you need to have ssh credentials configured for GitHub.
Instructions can be found [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

#### Server

root@kitploit:~

```
# Start Server
./ps-empire server

# Help
./ps-empire server -h
```

Check out the [Empire Docs](https://bc-security.gitbook.io/empire-wiki/) for more instructions on installing and using with Empire.
For a complete list of changes, see the [changelog](https://github.com/bc-security/empire/blob/main/changelog).

## Starkiller

![](https://assets.kitploit.com/production/public/readmes/47525/7a5c4e790a7456ffb0f2821192901a6430f294848108d2ba5177754821ba14b6.png)

[Starkiller](https://github.com/BC-SECURITY/Starkiller) is a web application GUI for PowerShell Empire that interfaces remotely with Empire via its API.
Starkiller can be ran as a replacement for the Empire client or in a mixed environment with Starkiller and Empire clients.
As of 5.0, Starkiller is packaged with Empire and doesn't require any additional setup.

## Contribution Rules

See [Contributing](https://github.com/bc-security/empire/blob/main/.github/CONTRIBUTING.md)

## Contributors

A special thanks to the following contributors for their help with Empire:

[@harmj0y](https://twitter.com/harmj0y)
[@sixdub](https://twitter.com/sixdub)
[@enigma0x3](https://twitter.com/enigma0x3)
[@rvrsh3ll](https://twitter.com/424f424f)
[@killswitch\_gui](https://twitter.com/killswitch_gui)
[@xorrior](https://twitter.com/xorrior)
[@Cx01N](https://twitter.com/Cx01N_)
[@Hubbl3](https://twitter.com/_Hubbl3)
[@Vinnybod](https://twitter.com/_vinnybod)

## Official Discord Channel

Join us in [our Discord](https://discord.gg/P8PZPyf) with any comments, questions, concerns, or problems!

[![](https://assets.kitploit.com/production/public/readmes/47525/b9c6c1a93ec9d835eb9eb82daf478a061771665c6abee00b3f94fa98e3e3a5f9.png)](https://discord.gg/P8PZPyf)

[Read more](/en/tools/github/bc-security/empire?expand=1)

## Categories

[Penetration Testing Frameworks](/en/categories/penetration-testing-frameworks)[Exploit Frameworks](/en/categories/exploit-frameworks)[Payload Generation](/en/categories/payload-generation)[Persistence Mechanisms](/en/categories/persistence-mechanisms)[Exploitation](/en/categories/exploitation)[IDS/IPS Evasion](/en/categories/ids-ips-evasion)[Lateral Movement](/en/categories/lateral-movement)[Scripting & Automation](/en/categories/scripting-automation)[Shellcode](/en/categories/shellcode)[Data Exfiltration](/en/categories/data-exfiltration)[Post-Exploitation](/en/categories/post-exploitation)[Penetration Testing](/en/categories/penetration-testing)[Command and Control](/en/categories/command-and-control)[Red Teaming](/en/categories/red-teaming)[Remote Access Tool](/en/categories/remote-access-tool)[Shellcode Generation](/en/categories/shellcode-generation)[Payload Development](/en/categories/payload-development)[Remote Access Trojan](/en...