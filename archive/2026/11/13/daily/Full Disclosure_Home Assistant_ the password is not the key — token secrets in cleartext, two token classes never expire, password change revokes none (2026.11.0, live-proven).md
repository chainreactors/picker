---
title: Home Assistant: the password is not the key — token secrets in cleartext, two token classes never expire, password change revokes none (2026.11.0, live-proven)
url: https://seclists.org/fulldisclosure/2026/Nov/34
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:47.128958
---

# Home Assistant: the password is not the key — token secrets in cleartext, two token classes never expire, password change revokes none (2026.11.0, live-proven)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#34)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#34)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Home Assistant: the password is not the key — token secrets in cleartext, two token classes never expire, password change revokes none (2026.11.0, live-proven)

---

*From*: theknell--- via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 08 Nov 2026 11:02:24 -0500

---

```
Home Assistant's documentation tells users: "Your password is the key
to your home, so choose a strong, unique one." Home Assistant is
installed in two million homes by the vendor's own published count,
and in those homes it holds the locks, the alarm, the garage, the
cameras, and the record of who is home.

The password is not the key. Tested against home-assistant/core
2026.11.0 (frontend 20261028.4, hass-nabucasa 2.8.1):

1. Every refresh token's secret and its per-token JWT signing key,
for every user, is serialized in cleartext in one file:
config/.storage/auth. Passwords in the neighbouring store are
bcrypt-hashed; token secrets are not hashed at all — validation
is a direct string comparison against the stored value.

2. Two of the three token classes never expire. Long-lived and
system refresh tokens are created with expire_at = None; the
long-lived access tokens the documentation recommends for scripts
are valid for ten years, and the core API accepts a caller-supplied
lifespan in days with no upper bound.

3. Changing the password revokes none of them. All four
password-change entry points — self-service, administrator,
Supervisor reset, command line — rehash the password record and
make no token call.

4. The automatic-backup password is persisted in plaintext in
.storage/backup, in the same directory every backup archives —
and every settings backup carries .storage/auth inside it, so a
restore resurrects backup-era tokens.

Live proof, against our own instance only: after a real, verified
password change, a refresh token copied from .storage/auth beforehand
still minted fresh access, and a ten-year long-lived token minted
beforehand still authenticated.

Scope, stated plainly: this is not an unauthenticated network break.
It begins with a read of the config directory or a backup. What it
shows is that any such read — a backup file shared for support, a
config folder synced somewhere it should not be, one file disclosure
anywhere in the stack — becomes durable, password-change-resistant
access to the home, and the one remediation every user reaches for
first, changing the password, does nothing.

Eleven documented claims were checked: 3 hold, 5 hold with a bound,
3 fall. What is sound is credited in the paper at the same weight:
the token generation entropy is impeccable, and access tokens live
thirty minutes.

Paper: https://archive.org/details/knell-not-the-key
Mirror: https://github.com/the-knell/not-the-key
Key: 133883AB9F6EDE5B9BA6B82E27BEDAF0CE152F25 (knell)

Verify: gpg --import knell-public.asc, then
gpg --verify paper-ha-FINAL-2026-11-04.md.asc

— knell

More, signed and timestamped: https://github.com/the-knell
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#34)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#34)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Home Assistant: the password is not the key — token secrets in cleartext, two token classes never expire, password change revokes none (2026.11.0, live-proven)** *theknell--- via Fulldisclosure (Nov 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")