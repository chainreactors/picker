---
title: fluxion v6.32
url: https://kitploit.com/en/posts/github-fluxionnetwork-fluxion-v632
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:28.060623
---

# fluxion v6.32

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2077/d964d855d88983a040b11400f8a9d33e0055879314db569623495b470c7875c1.jpg)

New releaseSep 12, 2026

# fluxion v6.32

Automated WPA/WPA2 phishing tool that captures handshakes, spawns a rogue access point, and lures users to a captive portal to harvest credentials via social engineering.

Share

![Fuxion logo](https://raw.githubusercontent.com/FluxionNetwork/fluxion/master/logos/logo.jpg)

# Fluxion is the future of MITM WPA attacks

Fluxion is a security auditing and social-engineering research tool. It is a remake of linset by vk496 with (hopefully) fewer bugs and more functionality. The script attempts to retrieve the WPA/WPA2 key from a target access point by means of a social engineering (phishing) attack. It's compatible with the latest release of Kali (rolling). Fluxion's attacks' setup is mostly manual, but experimental auto-mode handles some of the attacks' setup parameters. Read the [FAQ](https://github.com/FluxionNetwork/fluxion/wiki/FAQ) before requesting issues.

If you need quick help, you can talk with us on [Discord](https://discord.gg/G43gptk).

## Installation

**Download the latest revision**

root@kitploit:~

```
git clone https://github.com/FluxionNetwork/fluxion.git
```

**Switch to tool's directory**

root@kitploit:~

```
cd fluxion
```

**Run fluxion (it will check dependencies and prompt to install any that are missing)**

root@kitploit:~

```
./fluxion.sh
```

**To install/check dependencies only without running attacks**

root@kitploit:~

```
./fluxion.sh -i
```

**Fluxion is also available in arch**

root@kitploit:~

```
cd bin/arch
makepkg
```

or using the blackarch repo

root@kitploit:~

```
pacman -S fluxion
```

## 📜 Changelog

Fluxion is actively maintained with new features, improvements, and bugfixes.
Be sure to check out the [changelog here](https://github.com/FluxionNetwork/fluxion/commits/master).

## ![Octocat](https://assets.kitploit.com/production/public/readmes/2077/45bebdb2ae403a054b2b9bc3f689f5db2d4e1047c85bfcbe8f556880813e7745.png "Octocat") How to contribute

All contributions are welcome! Code, documentation, graphics, or even design suggestions are welcome; use GitHub to its fullest. Submit pull requests, contribute tutorials or other wiki content -- whatever you have to offer, it'll be appreciated but please follow the [style guide](https://github.com/FluxionNetwork/fluxion/wiki/Code-style-guide).

## 📖 How it works

* Scan for a target wireless network.
* Launch the `Handshake Snooper` attack.
* Capture a handshake (necessary for password verification).
* Launch `Captive Portal` attack.
* Spawns a rogue (fake) AP, imitating the original access point.
* Spawns a DNS server, redirecting all requests to the attacker's host running the captive portal.
* Spawns a web server, serving the captive portal which prompts users for their WPA/WPA2 key.
* Spawns a jammer, deauthenticating all clients from original AP and luring them to the rogue AP.
* All authentication attempts at the captive portal are checked against the handshake file captured earlier.
* The attack will automatically terminate once a correct key has been submitted.
* The key will be logged and clients will be allowed to reconnect to the target access point.
* For a guide to the `Captive Portal` attack, read the [Captive Portal attack guide](https://github.com/FluxionNetwork/fluxion/wiki/Captive-Portal-Attack)

## ❗ Requirements

A Linux-based operating system. We recommend Kali Linux 2025.4. An external wifi card is recommended.

## ![Octocat](https://assets.kitploit.com/production/public/readmes/2077/45bebdb2ae403a054b2b9bc3f689f5db2d4e1047c85bfcbe8f556880813e7745.png "Octocat") Credits

1. l3op - contributor
2. dlinkproto - contributor
3. vk496 - developer of linset
4. Derv82 - @Wifite/2
5. Princeofguilty - @webpages and @buteforce
6. Ons Ali @wallpaper
7. PappleTec @sites
8. MPX4132 - Fluxion V3
9. usama7628674 - contributor
10. cjb900 - moderator

## Disclaimer

* Authors do not own the logos under the `/attacks/Captive Portal/sites/` directory. Copyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, and research.
* The usage of Fluxion for attacking infrastructures without prior mutual consent could be considered an illegal activity and is highly discouraged by its authors/developers. It is the end user's responsibility to obey all applicable local, state and federal laws. Authors assume no liability and are not responsible for any misuse or damage caused by this program.

## Note

* Beware of sites pretending to be related with the Fluxion Project. These may be delivering malware.
* For WN722n V2/V3 VISIT - <https://github.com/aircrack-ng/rtl8188eus>
* Fluxion **DOES NOT WORK** on Windows Subsystem for Linux (WSL/WSL2), because the subsystem doesn't allow access to wireless network interfaces. Any issues regarding WSL will be **Closed Immediately**

## Links

**Fluxion website:** <https://fluxionnetwork.github.io/fluxion/>
**Discord:** <https://discord.gg/G43gptk>

[Read more](/en/tools/github/fluxionnetwork/fluxion?expand=1)

## Categories

[Wi-Fi Auditing](/en/categories/wi-fi-auditing)[Phishing](/en/categories/phishing)[Wireless Security](/en/categories/wireless-security)[Penetration Testing](/en/categories/penetration-testing)[Social Engineering](/en/categories/social-engineering)[Red Teaming](/en/categories/red-teaming)

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