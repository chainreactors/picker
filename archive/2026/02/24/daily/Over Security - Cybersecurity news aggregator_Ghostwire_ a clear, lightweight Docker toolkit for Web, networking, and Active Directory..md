---
title: Ghostwire: a clear, lightweight Docker toolkit for Web, networking, and Active Directory.
url: https://www.hacktivesecurity.com/blog/2025/11/19/ghostwire-a-clear-lightweight-docker-toolkit-for-web-networking-and-active-directory/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-24
fetch_date: 2026-02-25T04:15:00.185250
---

# Ghostwire: a clear, lightweight Docker toolkit for Web, networking, and Active Directory.

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [R/D](https://www.hacktivesecurity.com/blog/category/r-d/)
* Ghostwire: a clear, lightweight Docker toolkit for Web, networking, and Active Directory.

[R/D](https://www.hacktivesecurity.com/blog/category/r-d/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2025/11/Ghostwire.png)

\_ [November 19, 2025](https://www.hacktivesecurity.com/blog/2025/11/19/ghostwire-a-clear-lightweight-docker-toolkit-for-web-networking-and-active-directory/)\_ [Noel Duma](https://www.hacktivesecurity.com/blog/author/noel/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2025/11/19/ghostwire-a-clear-lightweight-docker-toolkit-for-web-networking-and-active-directory/#respond)

### Ghostwire: a clear, lightweight Docker toolkit for Web, networking, and Active Directory.

TL;DR <https://github.com/hacktivesec/ghostwire>

Traditional pentesting distributions (and the Docker versions as well) have become heavy, hard to maintain, and inconsistent across different environments. Ghostwire was created to offer a simpler alternative: a minimal, repeatable, and transparent Docker toolkit with an essential set of tools for web, network, Active Directory, mobile, and post-compromise analysis.

The project is based on a single multi-stage Dockerfile, `Dockerfile.total`, from which other specialized Dockerfiles (web, net, ad, wifi, mobile, total) are derived. This approach keeps the structure clear, reduces complexity, and avoids duplication.

The image uses Ubuntu 24.04, runs as a non-root user (`ghost`), and mounts two directories: `/work` for project files and `/shared` for persistent output. SecLists is already included under `/opt/seclists`.

The tool stack is intentionally minimal:

* **Web:** gobuster, sqlmap, ffuf, nuclei, wpscan, joomscan, whatweb, wafw00f
* **Network:** nmap, tcpdump, socat, netcat-openbsd, snmp, ike-scan, patator
* **Active Directory:** impacket, ldap-utils, smbclient, ldapdomaindump, bloodhound (venv), smbmap, enum4linux, NetExec
* **Cracking:** hashcat (CPU OpenCL via POCL), John, Hydra
* **Forensics and reverse engineering:** bulk\_extractor, steghide, exiftool, binwalk, foremost, apktool, jadx
* **Cloud:** Trivy, AWS CLI v2

The Python tools live in a dedicated venv that hosts components such as ldapdomaindump, bloodhound, smbmap, pypykatz, arjun, commix, objection, frida-tools. NetExec uses a separate venv to avoid conflicts.
The Go utilities (ffuf v2, nuclei, jaeles, amass v4, subfinder, httpx, dnsx, katana, waybackurls, anew, unfurl, s3scanner, kerbrute, gitleaks) are compiled at build time, and the Go toolchain is removed afterwards.

Ghostwire integrates a SOCKS pivot system via `px`, which dynamically generates a `proxychains4` configuration to route individual commands. `pxcurl`, `pxwget`, and support for standard environment variables (ALL\_PROXY, HTTP\_PROXY, HTTPS\_PROXY) are also available. Operations based on raw sockets remain outside the tunnel, as expected.

Essential scripts and utilities are included: `savehere`, `out`, `session-log`, `gw-wifi-capture`, `gw-usb-capture`, `gw-gpu-check`. Heavier frameworks such as PowerSploit, Empire, CloudMapper, and MobSF are optional and can be enabled only via build args.

Usage is straightforward: clone the repository, build the required stage via Docker Compose, and work inside the container with `/work` and `/shared` mounted. The `ghost` user has sudo inside the container, while keeping the environment isolated from the host.

An important point is that many GUI tools once considered “mandatory inside the distro” — such as Burp Suite, Wireshark, Ghidra, IDA Free, CyberChef desktop — are now available and work perfectly on both Windows and macOS. Ghostwire therefore focuses on CLI tools, leaving GUIs on the host, where they integrate better, reduce complexity, and do not bloat the Docker image.

The project is available under the Hacktive Security organization, `ghostwire` repository on GitHub.

Ghostwire aims to remain a clear, stable, and easily maintainable toolkit. To achieve this goal, user contributions are essential: reports, suggestions, optimizations, tests, and documentation improvements all help keep the project lean without introducing unnecessary components.

[♥95](https://www.hacktivesecurity.com/wp-admin/admin-ajax.php?action=process_simple_like&post_id=6309&nonce=f52252030b&is_comment=0&disabled=true "Like")

![](https://secure.gravatar.com/avatar/a7a53b02b148c6f0f61c236743901eeb3fb...