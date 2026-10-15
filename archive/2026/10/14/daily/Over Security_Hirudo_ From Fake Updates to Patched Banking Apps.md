---
title: Hirudo: From Fake Updates to Patched Banking Apps
url: https://www.threatfabric.com/blogs/hirudo-from-fake-updates-to-patched-banking-apps
source: Over Security
date: 2026-10-14
fetch_date: 2026-10-15T06:45:17.067213
---

# Hirudo: From Fake Updates to Patched Banking Apps

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* REGIONS
  + [Europe](https://www.threatfabric.com/regions/europe)
  + [Asia Pacific](https://www.threatfabric.com/regions/apac)
  + [Middle East & North Africa](https://www.threatfabric.com/regions/mena)
  + [Americas](https://www.threatfabric.com/regions/americas)
* USE CASES
  + [Social Engineering & Scams](https://www.threatfabric.com/usecases/social-engineering-scams)
  + [Account Takeover (ATO)](https://www.threatfabric.com/usecases/ato)
  + [Device Takeover (DTO)](https://www.threatfabric.com/usecases/dto)
  + [Hybrid Fraud](https://www.threatfabric.com/usecases/hybrid-fraud)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [WEBINARS](https://www.threatfabric.com/webinars)
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
  + [FUSION FIRESIDE](https://www.threatfabric.com/fusion-fireside)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research
Europe
MENA
Americas
APAC

## Hirudo: From Fake Updates to Patched Banking Apps

14 October 2026

![](https://www.threatfabric.com/hubfs/MTI_Hirudo3.jpg)

### Jump to

ThreatFabric's Mobile Threat Intelligence team has identified a new Android banking remote access trojan we track as Hirudo. Hirudo combines on-device credential theft with live remote control of the same phone, and it is delivered by shopping and entertainment apps that carry the trojan as a separate installation package. On their own, those traits place Hirudo alongside the current generation of Accessibility-driven Android bankers. What sets it apart is the lengths its operators go to once a bank is in their sights: rather than overlaying a fake screen on top of the genuine banking app, Hirudo attempts to replace the banking app itself with a modified copy that quietly disables the bank's own security checks from the inside.

In this article we focus on four things: how the banking apps are patched, how the campaign is distributed, who it targets, and the fraud it is built to commit.

## Key takeaways

* **A new Android banking RAT, Hirudo**, blends credential phishing, device takeover, screen and camera capture and SMS theft, tying every stolen value to a device and a target app.
* **It replaces banking apps with patched copies.** Eight Indonesian banking apps, covering seven banks, have purpose-built replacements that embed a hooking engine to blind signature, Accessibility, screen-capture and Play Integrity checks from within the app.
* **A two-app design.** A branded lure (shopping, adult video or short drama) carries the RAT as a separate APK and drops it behind a fake in-app "update."
* **Distributed with real ad infrastructure.** Lures are served from Amazon CloudFront and tied to campaigns through OpenInstall attribution and Meta Pixel IDs; some download routes were still live in October 2026.
* **Targeting reaches well beyond Indonesia.** Credential targets named in code span Indonesia, China, India, Mexico, Morocco and Thailand, and the bundled fake checkout carries Malaysian bank and wallet branding.
* **A mature back office.** Backend data captured in August 2026 exposed thousands of credential and device records, lock-screen history and financial profiles.

## A two-stage design: dropper and payload

Hirudo ships in two parts. The app the victim installs first is a **dropper**, wrapped in a convincing lure: a shopping app (Shopora), an adult-video app (1V1 X), or a short-drama app (ZoyaTV / KoiShort). The lure is functional, loading real content in a WebView, a storefront, a video catalogue or short dramas, so the experience looks legitimate. Behind that content the dropper runs a fixed startup routine: it collects promotion-tracking data, fetches its campaign configuration, and checks whether the **payload**, the Hirudo RAT, is already installed with its Accessibility service and notification access enabled.

If the payload is absent, the dropper displays a fake in-app "update" prompt and offers the bundled payload APK for installation. The payload is installed as a second app and must be granted its own permissions before any of Hirudo's collection or control features can run. One analysed shopping dropper goes further and raises a blackhole VPN during installation, cutting the device's IPv4 traffic while the payload is installed. [This approach](/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat) is currently observed in multiple families active on the threat landscape.

![fig1_fraud_chain-png-1](https://www.threatfabric.com/hs-fs/hubfs/fig1_fraud_chain-png-1.png?width=3333&height=1667&name=fig1_fraud_chain-png-1.png)

*Figure 1. The Hirudo fraud chain. A branded dropper installs a separate payload behind a fake update; once running, the payload drives several theft and control surfaces that report to the operator backend.*

Once the payload is running, the fraud surfaces open up. When the dropper's content triggers a payment, it passes the order details to the payload through an Android intent, and the payload renders a **fake checkout page** in a transparent WebView positioned over the dropper's order screen. The page is branded with the bank or wallet the dropper supplies and localised into eight languages. The victim types a payment PIN, the payload uploads it as appPayPwd, and returns a forged payment-success result to the dropper so the transaction appears to complete.

![](https://www.threatfabric.com/hs-fs/hubfs/shot_fake_checkout-png.png?width=538&height=685&name=shot_fake_checkout-png.png)

*Figure 2. The bundled fake-checkout page, here with Maybank branding and example order details. The transparent background places the PIN pad over the dropper's own order page.*

Separate from checkout, the payload uses bank- and wallet-specific prompts to request login passwords, uploaded as appPwd, and it reads the genuine app's screen to reflect the right user ID or amount back to the victim. It also targets **device-unlock secrets**: a full-screen fake pattern overlay captures the first pattern drawn and, in one build, the payload reads PIN, password and pattern input directly from the phone's real lock screen through Accessibility. Rounding out the payload's toolkit are live screen viewing over WebRTC, front- and rear-camera sessions, and SMS collection with a 90-day initial scan and a configured list of bank and wallet senders.

## Rewriting the bank: how Hirudo patches a banking app

Hirudo keeps a registry of 42 financial apps, but only eight Indonesian apps, across seven banks, have dedicated replacement downloads. For these, the RAT detects the installed banking app through Accessibility, checks its signing certificate against a stored reference, then shows a fake "update" prompt. It opens Android's uninstaller for the genuine app without waiting for the user to tap, and downloads the bank-specific replacement in parallel.

![shot_replacement_flow-png](https://www.threatfabric.com/hs-fs/hubfs/shot_replacement_flow-png.png?width=3456&height=1935&name=shot_replacement_flow-png.png)

*Figure 3. The replacement path. The RAT detects the bank app, removes the genuine copy, downloads the patched APK and drives the in...