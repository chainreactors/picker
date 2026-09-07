---
title: ublockdnsclient v0.3.1
url: https://kitploit.com/en/posts/github-ugzv-ublockdnsclient-v031
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:48.037435
---

# ublockdnsclient v0.3.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12864/c996a096cfcbdaba72a03bdf14d818ab0d4b5b9ba319661d0798f651cae475b9.png)

New releaseSep 6, 2026

# ublockdnsclient v0.3.1

Cross-platform system DNS client for uBlockDNS with device wide ad and tracker blocking and real time filter updates.

Share

# uBlockDNS Client

uBlockDNS Client is an independent project and is **not affiliated with, endorsed by, or related to uBlock Origin or its maintainer**.

uBlockDNS Client brings DNS-level ad and tracker blocking to your entire device. It uses community-maintained filter lists such as EasyList and EasyPrivacy, applied at the DNS layer so apps, browsers, and background services are covered without per-browser extensions.

**Website:** [ublockdns.com](https://ublockdns.com)

uBlockDNS Client is intended for desktop and server environments where you want one install point, system-wide protection, and remote configuration through the uBlockDNS dashboard.

## Highlights

* System-wide DNS filtering for browsers, apps, and background traffic
* Encrypted upstream DNS-over-HTTPS connection to the uBlockDNS service
* Real-time filter and custom rule updates from your dashboard
* Local service model with status checks and service management commands
* Cross-platform support for macOS, Linux, Windows 10+, and FreeBSD

## Install

Create a free account at [ublockdns.com](https://ublockdns.com), then follow the setup guide in your dashboard. The guide covers all supported platforms with copy-paste commands and step-by-step instructions.

Quick install for macOS and Linux:

root@kitploit:~

```
curl -sSfL https://ublockdns.com/install.sh | sh -s -- <profile-id>
```

Use `-L` so curl follows Cloudflare redirects on the hosted install script.

During installation, you may be prompted for your Mac or Linux administrator password to update system DNS settings.

Verify installer script checksum (Linux):

root@kitploit:~

```
curl -sSfLO https://ublockdns.com/install.sh
curl -sSfLO https://github.com/ugzv/ublockdnsclient/releases/latest/download/SCRIPT_SHA256SUMS
grep " install.sh$" SCRIPT_SHA256SUMS | sha256sum -c -
sh install.sh <profile-id>
```

Windows 10 or later (PowerShell as Administrator):

root@kitploit:~

```
irm https://ublockdns.com/install?id=<profile-id> | iex
```

The dashboard uses this bootstrap flow. It downloads the installer from `/install-script`, which avoids Cloudflare redirect issues that can break direct `/install.ps1` downloads.

Published Windows installers and binaries require Windows 10 or later. Windows 7, Windows 8, and Windows 8.1 are not supported.

Verify installer script checksum (PowerShell):

root@kitploit:~

```
iwr https://ublockdns.com/install-script -OutFile install.ps1
iwr https://github.com/ugzv/ublockdnsclient/releases/latest/download/SCRIPT_SHA256SUMS -OutFile SCRIPT_SHA256SUMS
$expected = (Select-String -Path .\SCRIPT_SHA256SUMS -Pattern " install.ps1$").Line.Split()[0].ToLower()
$actual = (Get-FileHash .\install.ps1 -Algorithm SHA256).Hash.ToLower()
if ($actual -ne $expected) { throw "install.ps1 checksum mismatch" }
powershell -ExecutionPolicy Bypass -File .\install.ps1 -ProfileId <profile-id>
```

A Windows GUI installer (.exe) is also available on the [releases page](https://github.com/ugzv/ublockdnsclient/releases).

### Updating

The service updates itself daily; releases are verified against the uBlockDNS signing key before being applied. Set `UBLOCKDNS_NO_AUTOUPDATE=1` in the service environment to opt out, or update manually with `sudo ublockdns upgrade`.

Automatic updates apply on macOS, Windows, and Linux. On FreeBSD, `rc.d` does not restart a service that exits, so the client does not update itself there; use `sudo ublockdns upgrade`. The client logs which mode it is in at startup.

Older versions without the `upgrade` command: re-run the install command once and automatic updates take over.

### Uninstalling

macOS and Linux:

root@kitploit:~

```
sudo ublockdns uninstall
```

Windows (PowerShell as Administrator):

root@kitploit:~

```
& "$env:ProgramFiles\uBlockDNS\ublockdns.exe" uninstall
```

The leading `&` is required. Without it PowerShell treats the quoted path as a plain string and reports `Unexpected token 'uninstall'`.

Uninstalling stops the service and restores your previous DNS settings. The binary stays on disk; delete it manually if you no longer want it. Run `ublockdns status` afterwards to confirm system DNS no longer points at `127.0.0.1`.

### Other platforms

The dashboard setup guide also covers Chrome, Firefox, iOS, Android, and routers. These use DNS-over-HTTPS directly and don't require this client.

### Supported architectures

linux/amd64, linux/arm64, linux/armv7, darwin/amd64, darwin/arm64, windows/amd64, windows/arm64, freebsd/amd64

## Usage

root@kitploit:~

```
ublockdns install   -profile <profile-id>   Install as system service
ublockdns uninstall                          Remove service and restore DNS
ublockdns start                              Start the service
ublockdns stop                               Stop the service
ublockdns status                             Show service state and readiness details
ublockdns status -json                       Show machine-readable status with ready_code and probe_error
ublockdns wait-ready -timeout 45s            Wait until service and DNS are active
ublockdns wait-ready -timeout 45s -json      Emit machine-readable readiness state for automation
ublockdns upgrade                            Update to the latest release and restart the service
ublockdns version                            Print version
```

Manage your filter lists, custom rules, and query log from the [dashboard](https://ublockdns.com). The CLI is intentionally narrow: install the local service, verify it is healthy, and let the dashboard handle policy changes.

## How it works

The client runs a local DNS proxy on `127.0.0.1:53` and, when IPv6 is available, `[::1]:53`. It forwards all queries to the uBlockDNS service over encrypted DNS-over-HTTPS. The service evaluates each query against the filter lists and custom rules enabled for your profile, then returns either the normal DNS answer or a block response.

When you update filter lists or custom rules in the dashboard, the client receives those changes in real time and flushes the local DNS cache automatically so new decisions take effect quickly.

## Build from source

Requires Go 1.25 or later.

root@kitploit:~

```
go build -o ublockdns .
sudo ./ublockdns install -profile <profile-id>
```

## Feedback and issues

Found a bug or have a suggestion? [Open an issue](https://github.com/ugzv/ublockdnsclient/issues/new/choose).

For blocking problems (ads getting through or a site wrongly blocked), check which filter lists you have enabled in your [dashboard](https://ublockdns.com) first. uBlockDNS uses community-maintained lists and does not control their contents.

## Security

Report security vulnerabilities privately through [GitHub Security Advisories](https://github.com/ugzv/ublockdnsclient/security/advisories/new). Do not open public issues for security problems.

For trust model details, development transparency, and current audit status, see [SECURITY.md](https://github.com/ugzv/ublockdnsclient/blob/main/SECURITY.md).

## License

MIT

[Read more](/en/tools/github/ugzv/ublockdnsclient?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Network Security](/en/categories/network-security)[Privacy](/en/categories/privacy)[Utilities & Frameworks](/en/categories/utilities-f...