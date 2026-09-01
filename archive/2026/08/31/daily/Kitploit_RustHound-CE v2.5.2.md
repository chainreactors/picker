---
title: RustHound-CE v2.5.2
url: https://kitploit.com/en/posts/github-g0h4n-rusthound-ce-v252
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:39.539363
---

# RustHound-CE v2.5.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/48915/0e79b9ebb3db303d092efd513e08bde5bbe77cc8d07ce5ed740df75de6ecd08a.png)

New releaseAug 31, 2026

# RustHound-CE v2.5.2

Active Directory data ingestor for BloodHound Community Edition written in Rust. 🦀

Share

![rusthound-ce logo](https://raw.githubusercontent.com/g0h4n/RustHound-CE/main/img/rusthoundce-transparent-dark-theme.png)

---

RustHound-CE is a cross-platform and cross-compiled BloodHound collector tool written in Rust, making it compatible with Linux, Windows, and macOS. It therefore generates all the JSON files that can be analyzed by BloodHound Community Edition. This version is only compatible with [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound). The version compatible with [BloodHound Legacy](https://github.com/BloodHoundAD/BloodHound) can be found on [NeverHack's github](https://github.com/NH-RED-TEAM/RustHound).

RustHound was created during my years as a pentester at Armature Technologies, renamed later Opencyber then NeverHack. I would like to thanks NeverHack for giving me time to research and develop the original RustHound project, which is still available on their github. We've decided to continue working together to contribute to both versions. This one will remain compatible with the community edition, and the NeverHack version with the Legacy version of BloodHound.

* [HELP.md](https://github.com/g0h4n/rusthound-ce/blob/HEAD/HELP.md) - How to compile it? How to install it? How to use it?
* [CHANGELOG.md](https://github.com/g0h4n/rusthound-ce/blob/HEAD/CHANGELOG.md) - A record of all significant version changes
* [ROADMAP.md](https://github.com/g0h4n/rusthound-ce/blob/HEAD/ROADMAP.md) - List of planned evolutions
* [CONTRIBUTING.md](https://github.com/g0h4n/rusthound-ce/blob/HEAD/CONTRIBUTING.md) - How to contribute to the project
* [LINKS.md](https://github.com/g0h4n/rusthound-ce/blob/HEAD/LINKS.md) - Useful resources

# Quick usage

## Compilation

This project can be compiled directly from `make` command like:

root@kitploit:~

```
# Compile it for your current system
make release
# Compile it for Windows
make windows
```

Or using `docker` like below:

root@kitploit:~

```
docker build --rm -t rusthound-ce .

# Then
docker run --rm -v $PWD:/usr/src/rusthound-ce rusthound-ce help
docker run --rm -v $PWD:/usr/src/rusthound-ce rusthound-ce release
docker run --rm -v $PWD:/usr/src/rusthound-ce rusthound-ce windows
docker run --rm -v $PWD:/usr/src/rusthound-ce rusthound-ce linux
```

## Installation

[![Crates.io Version](https://img.shields.io/crates/v/rusthound-ce) ![Crates.io Total Downloads](https://img.shields.io/crates/d/rusthound-ce?color=f74c00)](https://crates.io/crates/rusthound-ce)

Make sure the [required dependencies](https://github.com/g0h4n/RustHound-CE/blob/main/HELP.md#required-dependencies) are installed.

root@kitploit:~

```
# Install and/or update RustHound-CE from cargo command
cargo install rusthound-ce
```

## Usage

Here's an example of a command to collect domain objects and obtain the zip archive containing the json files to be imported into BloodHound CE:

root@kitploit:~

```
rusthound-ce -d DOMAIN.LOCAL -u [email protected] -z
```

More information and examples with how to compile RustHound-CE or how to use RustHound-CE can be found directly on the [help page](https://github.com/g0h4n/rusthound-ce/blob/HEAD/HELP.md).

# Special thanks to

[![](https://assets.kitploit.com/production/public/readmes/48915/a4fb07446a6c535550e346a5861e95ff65f7f64e6c5cc382ba961b5e9ee647d9.png)](https://github.com/NH-RED-TEAM)
[![](https://assets.kitploit.com/production/public/readmes/48915/46ccd1662da9ff4a628384791c5ca49be2f4d8d53aa832eebfa1de573add15a1.png)](https://github.com/f3rn0s)
[![](https://assets.kitploit.com/production/public/readmes/48915/e82fa8d71e18140f167eaa37b9e30b7658fd74fe3a922042e6c8694869f8227a.jpg)](https://github.com/barney0)
[![](https://assets.kitploit.com/production/public/readmes/48915/4dd366a7364331d88b1e0281730c81e0c14bd26662280c2d9f1cbca3ae4e23fd.png)](https://github.com/Mayfly277)
[![](https://assets.kitploit.com/production/public/readmes/48915/6978f83f61d98e35508f6e57bb976c98b0c38c394a02d0d65c932eba95d4d91a.png)](https://github.com/spyr0-sec)
[![](https://assets.kitploit.com/production/public/readmes/48915/3bec552750ca5b5e3cef35bfb769cce6ac4a06ab1ced9fd7f637778108b75b8b.jpg)](https://github.com/z-jxy)
[![](https://assets.kitploit.com/production/public/readmes/48915/956514f8f8952c4d1022be7e06b08d81cc3aed1f3cf7ba029d80baa1e60ef692.png)](https://github.com/0xdf223)
[![IppSec](https://assets.kitploit.com/production/public/readmes/48915/feb22a8e03c0bdebf1ada17bc39287c147e07af84ad3f3eeb010470152ac835e.jpg)](https://github.com/IppSec)
[![](https://assets.kitploit.com/production/public/readmes/48915/307436356e9dcf0c5f3fb41a01ae8a93d60ac339a040db5afb9694892f628cb8.jpg)](https://github.com/aancw)
[![](https://assets.kitploit.com/production/public/readmes/48915/47396838366fc6be21f7692d3aa962cc7589c991e748cd8c9f652973583adb65.png)](https://github.com/karanabe)
[![](https://github.com/AlexLinov.png?size=50)](https://github.com/AlexLinov)
[![](https://github.com/devdudumuniz.png?size=50)](https://github.com/devdudumuniz)
[![](https://github.com/luckystars0612.png?size=50)](https://github.com/luckystars0612)

[Read more](/en/tools/github/g0h4n/rusthound-ce?expand=1)

## Categories

[Reconnaissance](/en/categories/reconnaissance)[Information Gathering](/en/categories/information-gathering)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)

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