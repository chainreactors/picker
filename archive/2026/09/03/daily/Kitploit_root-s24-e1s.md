---
title: root-s24-e1s
url: https://kitploit.com/en/tools/github/everyoneexe/root-s24-e1s
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:33.722282
---

# root-s24-e1s

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

root-s24-e1s — Galaxy S24 SM-S921B S921BXXSDCZB2 RAM-only KernelSU Next + Root S24 app | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/everyoneexe/root-s24-e1s

![](https://assets.kitploit.com/production/public/tools/53920/fb78e01e41b96a30524613a1077288631941788b9997f49ad009661c4da42e77-display-v1.webp)

[Android Security](/en/categories/android-security)[Privilege Escalation](/en/categories/privilege-escalation)[Exploit Frameworks](/en/categories/exploit-frameworks)[Exploitation](/en/categories/exploitation)[Mobile Security](/en/categories/mobile-security)[Payload Development](/en/categories/payload-development)

![GitHub](/providers/github.png)everyoneexe/root-s24-e1s

# root-s24-e1s

Galaxy S24 SM-S921B S921BXXSDCZB2 RAM-only KernelSU Next + Root S24 app

[View Repository](https://github.com/everyoneexe/root-s24-e1s)

192 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Root S24 (e1s / S921BXXSDCZB2)

Per-boot local root on **Galaxy S24 SM-S921B** firmware `S921BXXSDCZB2`
(kernel `6.1.138-android14-11`), then late-load **KernelSU Next** so
`com.rifsxd.ksunext` reports Working LKM.

Not affiliated with [Root My Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy).
No GitHub payload feed, no multi-device catalog. One firmware, bundled
payload. Use a device you own.

## Download

Install the APK from **[Releases](https://github.com/everyoneexe/root-s24-e1s/releases)**.

KernelSU Next manager (required):
[v3.3.0](https://github.com/KernelSU-Next/KernelSU-Next/releases/download/v3.3.0/KernelSU_Next_v3.3.0_33214-release.apk)

## Device

|  |  |
| --- | --- |
| Model | SM-S921B |
| Codename | e1s |
| Firmware | S921BXXSDCZB2 |
| Kernel | 6.1.138-android14-11 |
| Bug | CVE-2026-43499 (futex PI UAF) |
| Root | RAM-only; reboot drops it |
| Manager | KernelSU Next v3.3.0 |

## Layout

root@kitploit:~

```
src/                 exploit + UMH helper (this target only)
src/targets/e1s-S921BXXSDCZB2/
docs/                this firmware + Next LKM notes
kernelsu/            Next-compat .ko + ksud, GPL module source
app/                 Root S24 (Kotlin), bundled DCZB2 payload
```

## App

Settings matches Root My Galaxy (theme, language menu, Shizuku). Shizuku is
the reliable transport on this phone (uid 2000). Without it, app UID can
SIGKILL the helper (exit 137).

Keep the screen on during install. Do not kill leftover
`cve-2026-43499-root` keepers after a write.

## Build from source

root@kitploit:~

```
export ANDROID_NDK_HOME=/path/to/android-ndk
make

cd app
./gradlew :app:assembleDebug
```

KernelSU rebuild: DDK `ghcr.io/ylarod/ddk-min:android14-6.1-20260313`,
vermagic `6.1.138-android14-11`. See [docs/kernelsu-next.md](https://github.com/everyoneexe/root-s24-e1s/blob/main/docs/kernelsu-next.md).

adb (clean boot), same payload the app bundles:

root@kitploit:~

```
export EXPLOIT_ATTEMPTS=1 P0_ATTEMPT_TIMEOUT_SEC=300 EXPLOIT_ATTEMPT_TIMEOUT_SEC=420
/data/local/tmp/cve-2026-43499-root --run-payload \
  /data/local/tmp/cve-2026-43499-app.so \
  /data/local/tmp/cve-2026-43499-root \
  /data/local/tmp/dczb2.log
```

## License

Exploit/helper: Apache-2.0 (see LICENSE and NOTICE).
`kernelsu/kernel`: GPL-2.0.

[Download Tool](https://github.com/everyoneexe/root-s24-e1s)