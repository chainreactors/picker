---
title: efiSeek
url: https://kitploit.com/en/tools/github/dsecurity/efiseek
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:35.658830
---

# efiSeek

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

efiSeek — Ghidra plugin that automates UEFI firmware analysis by identifying known GUIDs, protocols, SMI handlers, and interrupt functions, with headless module sorting. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/dsecurity/efiseek

![](https://assets.kitploit.com/production/public/tools/54268/106501d5a6fa3831cb3450b8e5a084648b43e08385229d00b0aa71190907fa4d-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Reverse Engineering](/en/categories/reverse-engineering)[Hardware Security](/en/categories/hardware-security)[Hardware & IoT Security](/en/categories/hardware-iot-security)[Binary Analysis](/en/categories/binary-analysis)[Firmware Analysis](/en/categories/firmware-analysis)

![GitHub](/providers/github.png)dsecurity/efiseek

# efiSeek

Ghidra plugin that automates UEFI firmware analysis by identifying known GUIDs, protocols, SMI handlers, and interrupt functions, with headless module sorting.

[View Repository](https://github.com/dsecurity/efiseek)

40640232 years ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# ***efiSeek for Ghidra***

## About

The analyzer automates the process of researching EFI files, helps to discover and analyze well-known protocols, smi handlers, etc.

## Features

### Finds known EFI GUID's

![guids](https://assets.kitploit.com/production/public/readmes/54268/f55455cbfed89cdff5b359ba76faef086168bbc283157c671e29eda1206b7e9c/6cdb4232666f0a7d7475afcec217679a67869b3195a70b988efb9508888361e0-display-v1.webp)

### Identifies protocols located with `LOCATE_PROTOCOL` function

![locateProtocols](https://assets.kitploit.com/production/public/readmes/54268/03aa8b8a861583afa6621f5c695ab2ea4d9f61735d48c1c272eaf7684f69d23e/8a721f3a30be84a52c6018425b8937d34ef28644c5e1f3f2872002b7e27b849a-display-v1.webp)

### Identifies functions used as the `NOTIFY` function

![notify](https://assets.kitploit.com/production/public/readmes/54268/6d643d7dd201f5206d1e2b32bbb0b34a3f0b1753e6d6c4af78277b3fce14f19e/91646e84f1caaeb58df62a8224ebf0e1cb5558781bf031422a1032dd74acdcbb-display-v1.webp)

### Identifies protocols installed in the module through `INSTALL_PROTOCOL_INTERFACE`

![install](https://assets.kitploit.com/production/public/readmes/54268/805109cb0e1b37b32fe8644d74df847dfce0a02fe2bd0134306316e7aa822c18/67257852ab43c770d4d2629774c36e546cfb6c0dbcefc093d8131d6c3cc2dcb5-display-v1.webp)

### Identifies functions used as an interrupt function (like some hardware, software/child interrupt)

![ioTrap](https://assets.kitploit.com/production/public/readmes/54268/9c925c097e8daf1da54d9548e46293ec8d44102df5b009805a5988b984cef803/adeb12afae48d0d1b275cd9e14eee82b48d58424414b51c7a027ba922218b2d1-display-v1.webp)

![sx](https://assets.kitploit.com/production/public/readmes/54268/1067c246cc6fb51fb5a428730c543b7b5bf43eb2a87f41dacc2b163417a06a70/a405543603037ac919fcad1b9468762c70b2dbea9de1a10234bd4ab0b8bc4418-display-v1.webp)

![child](https://assets.kitploit.com/production/public/readmes/54268/87cd61486b5cc01c5a91ac19453dfba7e6fac8c648bdd68807ae7549f909eb9a/697cc22d6d8879bfec22f2a098b31883056f9dce37880186a40d4980dc89980e-display-v1.webp)

![sw](https://assets.kitploit.com/production/public/readmes/54268/dd5b93e2cdaf760aaa82c2bfcbb48f5cb7d253d138d9c7f52ddda5aedc925a36/7e106c65b38f96bec27de7bbfbd93aa7b060208d67c0cbe52c08c59df4499ade-display-v1.webp)

### Script for loading efi modules to relevant directories in `Headless mode`

Sorting smm modules relying on meta information into next folders:

* SwInterrupts
* ChildInterrupts
* HwInterrupts
* UnknownInterrupts

![sort](https://assets.kitploit.com/production/public/readmes/54268/5ea86ae4a5ee20cc460b21579dabebd760e67f701405d34a665e397a5763aaf2/48af87f792b58176499954ea48237df6a3502a5ab698327a4cc3789a3aef877e-display-v1.webp)

## Installation

Set `GHIDRA_INSTALL_DIR` environment variable to ghidra path.

Start `gradlew.bat`, after the completion of building a copy archive from the `dist` directory to `GHIDRA_HOME_DIR/Extensions/Ghidra/`.
And turn on this extention in your ghidra.

## Usage

After installation you are free to use this analyzer. If you open a EFI file, the analyzer appears selected automatically.
To start the analyzer, press `A` or `Analysis/Auto Analyze` and press `Analyze`.

## References

* <https://github.com/al3xtjames/ghidra-firmware-utils>
* <https://github.com/danse-macabre/ida-efitools/>

[Download Tool](https://github.com/dsecurity/efiseek)