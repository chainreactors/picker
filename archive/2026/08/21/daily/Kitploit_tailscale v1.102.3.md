---
title: tailscale v1.102.3
url: https://kitploit.com/en/posts/github-tailscale-tailscale-v11023
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:04.979187
---

# tailscale v1.102.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4601/3bbcaf0e7ca41f9038af61ca63251d745afaeb4b1edbca055b7f14d5815dcb25.png)

New releaseAug 21, 2026

# tailscale v1.102.3

The easiest, most secure way to use WireGuard and 2FA.

Share

# Tailscale

<https://tailscale.com>

Private WireGuard® networks made easy

## Overview

This repository contains the majority of Tailscale's open source code.
Notably, it includes the `tailscaled` daemon and
the `tailscale` CLI tool. The `tailscaled` daemon runs on Linux, Windows,
[macOS](https://tailscale.com/kb/1065/macos-variants/), and to varying degrees
on FreeBSD and OpenBSD. The Tailscale iOS and Android apps use this repo's
code, but this repo doesn't contain the mobile GUI code.

Other [Tailscale repos](https://github.com/orgs/tailscale/repositories) of note:

* the Android app is at <https://github.com/tailscale/tailscale-android>
* the Synology package is at <https://github.com/tailscale/tailscale-synology>
* the QNAP package is at <https://github.com/tailscale/tailscale-qpkg>
* the Chocolatey packaging is at <https://github.com/tailscale/tailscale-chocolatey>

For background on which parts of Tailscale are open source and why,
see <https://tailscale.com/opensource/>.

## Using

We serve packages for a variety of distros and platforms at
[https://pkgs.tailscale.com](https://pkgs.tailscale.com/).

## Other clients

The [macOS, iOS, and Windows clients](https://tailscale.com/download)
use the code in this repository but additionally include small GUI
wrappers. The GUI wrappers on non-open source platforms are themselves
not open source.

## Building

We always require the latest Go release, currently Go 1.26. (While we build
releases with our [Go fork](https://github.com/tailscale/go/), its use is not
required.)

root@kitploit:~

```
go install tailscale.com/cmd/tailscale{,d}
```

If you're packaging Tailscale for distribution, use `build_dist.sh`
instead, to burn commit IDs and version info into the binaries:

root@kitploit:~

```
./build_dist.sh tailscale.com/cmd/tailscale
./build_dist.sh tailscale.com/cmd/tailscaled
```

If your distro has conventions that preclude the use of
`build_dist.sh`, please do the equivalent of what it does in your
distro's way, so that bug reports contain useful version information.

## Bugs

Please file any issues about this code or the hosted service on
[the issue tracker](https://github.com/tailscale/tailscale/issues).

## Contributing

PRs welcome! But please file bugs. Commit messages should [reference
bugs](https://docs.github.com/en/github/writing-on-github/autolinked-references-and-urls).

We require [Developer Certificate of
Origin](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin)
`Signed-off-by` lines in commits.

See [commit-messages.md](https://github.com/tailscale/tailscale/blob/HEAD/docs/commit-messages.md) (or skim `git log`) for our commit message style.

## About Us

[Tailscale](https://tailscale.com/) is primarily developed by the
people at <https://github.com/orgs/tailscale/people>. For other contributors,
see:

* <https://github.com/tailscale/tailscale/graphs/contributors>
* <https://github.com/tailscale/tailscale-android/graphs/contributors>

## Legal

WireGuard is a registered trademark of Jason A. Donenfeld.

[Read more](/en/tools/github/tailscale/tailscale?expand=1)

## Categories

[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Network Security](/en/categories/network-security)[Authentication](/en/categories/authentication)

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