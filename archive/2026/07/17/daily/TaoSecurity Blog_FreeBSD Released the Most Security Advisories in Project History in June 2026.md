---
title: FreeBSD Released the Most Security Advisories in Project History in June 2026
url: https://taosecurity.blogspot.com/2026/07/freebsd-released-most-security.html
source: TaoSecurity Blog
date: 2026-07-17
fetch_date: 2026-07-18T04:46:38.231378
---

# FreeBSD Released the Most Security Advisories in Project History in June 2026

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### FreeBSD Released the Most Security Advisories in Project History in June 2026

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[July 16, 2026](https://taosecurity.blogspot.com/2026/07/freebsd-released-most-security.html "permanent link")

On average, the FreeBSD security team releases about 2 security advisories per month. AI has changed this.

In April, the project released 8 advisories, [with 6 powered by AI](https://www.reddit.com/r/freebsd/comments/1t0ei6o/ai_found_6_out_of_8_freebsd_security_advisories/).  In May, the count decreased slightly to 7.

Today I took a look at the [FreeBSD Security Advisory](https://www.freebsd.org/security/advisories/) page to check the latest advisory count.

June saw the most number of advisories ever published in project history: 25.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXCtOGgN23DN0aQXhw-6X5iKxsGy1VTmfao5_Y-s0XjtXS0WQJuy-7CzL1HXqGO6hBkUtJJm78h8EqJNsRnH_ZMk56viiKx9RpMw6T0T1v-ak82oV25lXZr16On78oDaAHkt0G_pEJ1C8pyVUFOaVW7AO_OH3zR73i6zxzVSCHOdegJgGNxrqx/w640-h274/FreeBSD%20Security%20Vulns%20by%20month.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXCtOGgN23DN0aQXhw-6X5iKxsGy1VTmfao5_Y-s0XjtXS0WQJuy-7CzL1HXqGO6hBkUtJJm78h8EqJNsRnH_ZMk56viiKx9RpMw6T0T1v-ak82oV25lXZr16On78oDaAHkt0G_pEJ1C8pyVUFOaVW7AO_OH3zR73i6zxzVSCHOdegJgGNxrqx/s1600/FreeBSD%20Security%20Vulns%20by%20month.png)

This blows away the previous record of 18 from January 2001. The other big spike was 11 in January 2016.

AI apaprently discovered at least 9 of the June 2026 FreeBSD vulnerabilities.

On 15 June the FreeBSD Foundation announced the [FreeBSD AI-assisted Vulnerability Discovery Project](https://freebsdfoundation.org/blog/freebsd-ai-assisted-vulnerability-discovery-project-launch/):

"The 6-month project is being funded by a grant from the Alpha Omega project.

The funds will be used to engage FreeBSD Security Team members under fixed-term contracts to find and patch vulnerabilities.

The Security Team’s access to publicly available AI models and tokens will be provided free of charge. AI will be used for vulnerability discovery and analysis only, all patches will be manually created."

Yes, 25 vulnerabilities is far lower than the 570 associated with Patch Tuesday this week. However, it's important to see the effects of AI-powered vulnerability discovery everywhere. It's not hype. It is real.

I am hopeful that developers will continue to use AI to discover and fix vulnerabilities in old code, and also prevent new code from shipping with vulnerabilities.

Addendum:

I asked Gemini to explain the large number of advisories in 2001-2002. It said:

"The
pronounced security advisory spike between August 2000 and January 2001
represents one of the most concentrated periods of security patching in
FreeBSD's history, totaling 66 advisories in a six-month window.

A
closer look at the specific advisories reveals that this spike was
primarily driven by a massive wave of vulnerabilities discovered in
popular third-party software (the "Ports" collection) along with
critical auditing of core networking daemons.

1. Vulnerabilities in Popular Third-Party Software (Ports)

During
this era, many open-source projects were grappling with newly pervasive
exploitation techniques like buffer overflows and format string
vulnerabilities. The dataset shows a massive batch of updates for staple
utilities of the early-2000s internet:

Internet
& Chat Clients: Multiple advisories were issued for communication
tools, including the `pine` mail client, `xchat`, `gaim` (instant
messaging), `bitchx` (IRC client), and the `netscape` web browser.

Web
& Content Servers: Security flaws were patched in web servers and
frameworks like `php`, `zope`, `thttpd`, and the `boa` web server.

Development
& System Tools: Popular utilities like `curl`, `gnupg`, `cvsweb`,
`ethereal` (now Wireshark), `syslog-ng`, and even alternative
shells/editors like `bash1` and `joe` required immediate security
patches.

2. Core System & Network Infrastructure Patches

Alongside
user-facing applications, the core FreeBSD development team had to
address architectural and networking vulnerabilities in the base system:

Routing
& Firewalls: Critical flaws were patched in basic networking
security logic, notably `ipfw` (the firewall tool) and `ppp-nat`
(Network Address Translation).

Core
Network Daemons: High-risk vulnerabilities struck standard network
entry points, resulting in patches for `bind` (DNS server), `telnetd`,
`dhclient`, and the newly adopted `openssh`.

Protocol
& Kernel Level: Security advisories were issued for low-level
system components like `tcp-iss` (Initial Sequence Number generation,
crucial for preventing TCP hijacking) and filesystem-level wrappers like
`procfs`.

3. The Climax: January 2001

The
spike peaked dramatically in January 2001 alone with 18 advisories.
This was largely an administrative and security "housecleaning" event.
Rather than a single massive system failure, it reflects a coordinated
effort by the FreeBSD Security Officer team to bundle and ship security
patches for dozens of utilities simultaneously—including `crontab`,
`inetd`, `mysql`, and `xfree86`—ensuring systems were hardened as the
platform matured."

[ai](https://taosecurity.blogspot.com/search/label/ai)
[freebsd](https://taosecurity.blogspot.com/search/label/freebsd)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/1263808485469068541)

### Popular posts from this blog

### [Zeek in Action Videos](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

[July 29, 2021](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcWFyS3aGQrT6UiiiBbLkOiUs5W_Y9cYMLeH2Z7KkzzqINSWjFIEG8inSUNbYNGTjF7dcEUOOOkK7DzHQXcNMY3Nhl1PIFsdZZeJOH7bzRzpQMUdez5M7_g3t_xyygra49FBKK/w640-h360/capture_001_29072021_143006.jpg)](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

This is a quick note to point blog readers to my Zeek in Action YouTube video series for the Zeek network security monitoring project .  Each video addresses a topic that I think might be of interest to people trying to understand their network using Zeek and adjacent tools and approaches, like Suricata, Wireshark, and so on.  I am especially pleased with Video 6 on monitoring wireless networks . It took me several weeks to research material for this video. I had to buy new hardware and experiment with a Linux distro that I had not used before -- Parrot .  Please like and subscribe, and let me know if there is a topic you think might make a good video.

[Read more](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "Zeek in Action Videos")

### [MITRE ATT&CK Tactics Are Not Tactics](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

[October 23, 2020](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh8UtkHOxII5KLGuTgeVk3iVj3KMfkoFLyDb11MrasYGQ9J2Q5NPBgNUX4-Dk5YKF_26s2quTQ_ve4bEh4yIF1H97CJeNqoGqlpAATJPzThQ_IGALsANV3MZLlF_zogZNHM-LI/s320/on+tactics.jpg)](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

Just what are "tactics"? Introduction MITRE ATT&CK  is a great resource, but something about it has bothered me since I first heard about it several years ago. It's a minor point, but I wanted to document it in case it confuses anyone else. The MITRE ATT&CK Design and Philosophy document from March 2020 says the following: At a high-level, ATT&CK is a behavioral model that consists o...