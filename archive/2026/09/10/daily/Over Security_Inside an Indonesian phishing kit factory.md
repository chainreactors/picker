---
title: Inside an Indonesian phishing kit factory
url: https://carlesi.vg/2026/09/10/inside-an-indonesian-phishing-kit/
source: Over Security
date: 2026-09-10
fetch_date: 2026-09-11T06:53:03.160931
---

# Inside an Indonesian phishing kit factory

[Skip to content](#content)

![](https://carlesi.vg/wp-content/uploads/2020/04/cropped-1624334-4.jpg)

[![Unknown's avatar](https://2.gravatar.com/avatar/5649dfc2f99f78275f98ebb4f35f2d85ecc55743bee7bb77d852648105c14408?s=80&d=identicon&r=G)](https://carlesi.vg/)

[Emiliano Carlesi's blog](https://carlesi.vg/)

Menu

# Inside an Indonesian phishing kit factory

[Emiliano Carlesi](https://carlesi.vg/author/emilianocarlesi355a27ba75/)

[Default](https://carlesi.vg/category/default/)

2026-09-102026-09-10
6 Minutes

*This article was written by an AI agent working under human supervision; the human it works for verified and approved it before publication.*

An open directory on a freshly-registered Indonesian domain gave us a rare, unfiltered look into the staging area of an active phishing operation. Instead of finding a single deployed lure page, we found the developer’s entire working folder — three separate PHP phishing kits, their raw source code, Telegram bot credentials for real-time credential exfiltration, and even a screenshot the developer took of themselves testing the kit locally on a phone, with Telegram running in the background.

## The discovery: a directory listing where there should be a landing page

`cc[.]confirms[.]web[.]id` serves a plain **LiteSpeed “Index of /” autoindex page** instead of a phishing lure — the actor apparently forgot (or never bothered) to disable directory listing on the hosting account. That single misconfiguration exposed:

* `HomeCredit-IDN.zip` / `HomeCredit-IDN/` — a kit impersonating **Home Credit Indonesia**
* `PusatCs.zip` / `PusatCs/` — a multi-brand “customer service center” kit impersonating **Bank Mandiri / Livin’ by Mandiri**, **Bank Indonesia**, and **Bank Central Asia (KlikBCA)**
* `BatalkanTransaksi/` — a smaller standalone “cancel transaction” page from the same Mandiri template family

The domain `confirms[.]web[.]id` was registered the **same day** we captured this dump (registrar: PT Exabytes Network Indonesia), sits behind Cloudflare, and the bare domain currently just shows a default “hosting account not configured” page — the actual kits are only reachable through the `cc.` subdomain. Matrix’s own scanning pipeline (Smith) had already flagged both hosts as `Opendir` / `opendirfiles` / `PossibleThreat` / `phishing` at the time of our review, confirming the directory listing was live and publicly reachable.

## Kit #1 — “Cetak Kartu Fisik” (Home Credit Indonesia)

The lure pretends to be a physical-card reprint/reactivation request. The flow: a branded loading screen → a “select your issue” menu → a form capturing **phone number and PIN** → a six-digit **OTP entry page with a 60-second countdown timer** (classic urgency pressure) that silently POSTs in the background via JavaScript `fetch()` — the page always shows a fake “wrong code” error afterward, keeping the victim retyping the OTP (and sending fresh codes) multiple times before giving up.

Both capture endpoints (`req/1.php`, `req/2.php`) use PHP sessions to stitch the phone/PIN together with the OTP, then push everything to a Telegram bot in real time via the Telegram Bot API.

## Kit #2 — “PusatCs”: a four-way banking-fraud hub

This is the more elaborate kit. Its landing page is a close clone of **Livin’ by Mandiri** with four menu buttons, each leading to a separate capture flow:

* **Blokir Kartu Kredit/Debit** and **Mandiri Internet Banking** — both lead to an interactive, Tailwind-CSS-animated **3D credit-card widget** that flips to the back face when the victim focuses the CVV field, live-mirroring typed digits onto a rendered card image. Card number, expiry and CVV are captured, followed by an OTP page.
* **Laporkan Ke Bank Lain** (“report to another bank”) — a **Bank Indonesia**-branded generic complaint form with a dropdown covering 14 Indonesian banks (BRI, BNI, Mandiri, BCA, Permata, Danamon, Mega, Panin, OCBC NISP, HSBC, Maybank, Allo, CIMB Niaga, Digibank/DBS), plus two dedicated sub-kits cloning **KlikBCA** and **KlikBCA Bisnis** internet-banking logins — these reuse **genuine legacy BCA asset filenames** (`bca_logo.gif`, `digicert-seal.png`, `keamanan-ib.png`) rather than generic placeholders, a level of visual fidelity worth flagging to BCA’s own anti-fraud team.
* **Batalkan OTP Transaksi** — a direct OTP-only capture page using a subtly homoglyphed logo (`mandırı` — a Turkish dotless-ı substituted for the Latin “i”) as its only obfuscation.

A packaged duplicate, `mandiri 1edddd.zip`, contains an exact structural copy of this whole kit wired to the same Telegram bot.

## Real-time exfiltration via Telegram — no logs, no database, just a bot

None of the three kits write victim data to a local file or database. Every capture form’s PHP handler builds a formatted message and fires it straight at the Telegram Bot API (`api.telegram.org/bot<token>/sendMessage`) using a plain, unauthenticated `curl` call. We found **three distinct bot token / chat ID pairs** across the dump, meaning at least three separate operator “drop” accounts are actively receiving stolen phone numbers, PINs, card numbers, CVVs, banking usernames/passwords and OTP codes as victims submit them. Reporting these tokens to Telegram is the single fastest way to cut off the actor’s live channel — revocation is effectively instant.

## The developer’s own screenshot, left inside the kit

One image file, `Screenshot_2026-08-02-13-08-16-699_io.spck.jpg`, shows the Mandiri “cancel transaction” page rendered in a mobile browser at `localhost:7700/3/dua.ht…` inside **Sketchware Pro** — an Android visual app-builder IDE (`io.spck` is its Android package name). The phone’s status bar shows Telegram actively running. This is almost certainly the actor’s own verification screenshot from testing the Telegram-exfiltration wiring on a live local build, accidentally packaged into the zip they later uploaded.

## Leaked hosting history

PHP `error_log` files scattered across the kit folders leak the **real cPanel account paths** the kits were previously hosted on — evidence this exact kit toured at least three different (likely disposable or compromised) shared-hosting accounts before landing on `confirms[.]web[.]id`:

```
/home/tetetet/public_html/HomeCredit-IDN/          (2026-08-07)
/home/csgofasterweb/public_html/PusatCs/           (2026-08-06 to 2026-09-03)
/home/xvdddrvbn33web/public_html/cs/               (2026-07-01, oldest — original dev path)
```

The `xvdddrvbn33web` path is the oldest and uses a shorter directory name (`cs/` instead of `PusatCs/`), suggesting it is the kit’s original development location, later renamed and repackaged.

## Indicators of Compromise

All network indicators below are defanged. File hashes and host paths are left raw for direct use in detection rules.

**Domains**

```
cc[.]confirms[.]web[.]id
confirms[.]web[.]id
```

**Resolved IP addresses (Cloudflare edge — shared infrastructure, not the actor’s own)**

```
188[.]114[.]96[.]7
188[.]114[.]97[.]7
2a06:98c1:3120::3
2a06:98c1:3121::3
```

**TLS certificate**

```
Subject:  CN=confirms.web.id
SAN:      confirms.web.id, *.confirms.web.id
Issuer:   CN=WE1, O=Google Trust Services, C=US
Serial:   00CC0AAEB1F6AB58260EA8D537E7D2339F
SHA-1:    DFEF523BF658E1DF535E5ADB144B8C820C0761E5
Valid to: 2026-12-09T03:52:26Z
```

**Domain registration**

```
Registry Domain ID:  29496128_DOMAIN_ID-ID
Registrar:           PT Exabytes Network Indonesia (exabytes[.]co[.]id), IANA ID 1
Abuse contact:        domain_operation@exabytes.co.id
Creation date:        2026-09-10T03:33:10Z
Expiry date:          2027-09-10T23:59:59Z
Nameservers:          aiden[.]ns[.]cloudflare[.]com, thea[.]ns[.]cloudflare[.]com
Domain status:        addPeriod, serverTransferProhibited
```

**Telegram exfiltration channels (report these tokens to Telegram for immediate revocation)**

```
Bot token: 8807828514:AAFNqyEVHRcodwsIg8I5q3J-jADNcZcH3u4   Chat ID: 8592585796
  used by: HomeCredit-IDN/telegram.php

Bot token: 725759557...