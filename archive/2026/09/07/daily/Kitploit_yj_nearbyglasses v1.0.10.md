---
title: yj_nearbyglasses v1.0.10
url: https://kitploit.com/en/posts/github-yjeanrenaud-yj_nearbyglasses-v1010
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:40:55.641016
---

# yj_nearbyglasses v1.0.10

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12083/29c66ac6f3e7327f73700e7241c0ca93860a8f5cc3efdfdc619b8ee91873473a.png)

New releaseSep 7, 2026

# yj\_nearbyglasses v1.0.10

attempting to detect smart glasses nearby and warn you

Share

# yj\_nearbyglasses

attempting to detect smart glasses nearby and warn you.

# ⚠ WARNING! ⚠

## *nearby-glasses-alert.pages.dev* is NOT RELATED TO MY PROJECT. Many apps in Play Store and App Store look or are even called very similar to *Nearby Glasses*. They seem to hijack the name and try to make a quick profit from it. they do not adhere to the AGPL license, give no whatsoever. I do not endorse this.

![Screenshot Nearby Glasses classic](https://assets.kitploit.com/production/public/readmes/12083/e76b27744afcd0893efe1992c440e28c6606e742fa390f1b2c9a79a34e5600d1.png)
![Screenshot Nearby Glasses canary mode](https://assets.kitploit.com/production/public/readmes/12083/29c66ac6f3e7327f73700e7241c0ca93860a8f5cc3efdfdc619b8ee91873473a.png)

# ⚠ WARNING! ⚠

## **HARASSING someone because you think they are wearing a covert surveillance device can be a criminal offence. It may even be a more serious offence than using such a device. Please seek legal advice regarding your local laws on this matter.**

## ⚠ DO NOT HARASS ANYONE AT ALL ⚠

---

# Nearby Glasses

The app, called *Nearby Glasses*, has one sole purpose: Look for smart glasses nearby and warn you.

[![Get It On Google Play](https://assets.kitploit.com/production/public/readmes/12083/a7dbeba4623dd255798dd1159e543cdbeeb9e43faa6db7f859b0f9ed3699932c.png)](https://play.google.com/store/apps/details?id=ch.pocketpc.nearbyglasses) [![Get it at IzzyOnDroid](https://assets.kitploit.com/production/public/readmes/12083/75659b864e0f38bedce979c2097721b9beae838a06434eaacb0e93815468735a.png)](https://apt.izzysoft.de/packages/ch.pocketpc.nearbyglasses) [![Get it on Obtainium](https://assets.kitploit.com/production/public/readmes/12083/33e5685bdfff51e02830f2a18b5df5df986e73c2c8ae0f7cf031ebc791e5f771.png)](https://apps.obtainium.imranr.dev/redirect.html?r=obtainium://add/https://github.com/yjeanrenaud/yj_nearbyglasses/) [![Download on the App Store](https://assets.kitploit.com/production/public/readmes/12083/a6fa504b048d52b4e9f5108021dce33af0d96b8b78c34095072971f4a34471fa.png)](https://apps.apple.com/us/app/nearby-glasses-original/id6761056896)

# Table of contents

* [Nearby Glasses](#Nearby-Glasses)
* [Why?](#why)
* [How?](#how)
* [Features](#features)
  + [What's RSSI?](#whats-rssi)
* [iOS and Android](#ios-and-android)
* [Usage](#usage)
* [ToDos](#todos)
* [Tech-Solutionism?](#tech-solutionism)
* [Build from Source](#build-from-source)
* [Shoutouts](#shoutouts)
* [License and Credits](#license-and-credits)

This app notifies you when smart glasses are nearby. It uses company identificators in the Bluetooth data sent out by these. Therefore, there likely are false positives (e.g. from VR headsets). Hence, please proceed with caution when approaching a person nearby wearing glasses. They might just be regular glasses, despite this app’s warning.

The app’s author [Yves Jeanrenaud](https://yves.app) takes no liability whatsoever for this app nor it’s functionality. Use at your own risk. By technical design, detecting Bluetooth LE devices might sometimes just not work as expected. I am no graduated developer. This is all written in my free time and with knowledge I taught myself.
**False positives are likely.** This means, the app *Nearby Glasses* may notify you of smart glasses nearby when there might be in fact a VR headset of the same manufacturer or another product of that company’s breed. It may also miss smart glasses nearby. Again: I am no pro developer.
However, this app is **free and open source**, you may review the code, change it and re-use it (under the [license](https://github.com/yjeanrenaud/yj_nearbyglasses/blob/main/LICENSE)).
The app *Nearby Glasses* does not store any details about you or collects any information about you or your phone. There are no telemetry, no ads, and no other nuisance. If you install the app via Play Store, Google may know something about you and collect some stats. But the app itself does not.
If you choose to store (export) the logfile, that is completely up to you and your liability where this data go to. The logs are recorded only locally and not automatically shared with anyone. They do contain little sensitive data; in fact, only the manufacturer ID codes of BLE devices encountered.

**Use with extreme caution!** As stated before: There is no guarantee that detected smart glasses are really nearby. It might be another device looking technically (on the BLE adv level) similar to smart glasses.
Please do not act rashly. **Think before you act upon any messages** (not only from this app).

## Why?

* Because I consider smart glasses an intolerable intrusion, consent neglecting, horrible piece of tech that is already used for making various and tons of equally truely disgusting 'content'. [1](https://www.404media.co/border-patrol-agent-recorded-raid-with-metas-ray-ban-smart-glasses/), [2](https://www.404media.co/metas-ray-ban-glasses-users-film-and-harass-massage-parlor-workers/)
* Some smart glasses feature small LED signifying a recording is going on. But this is easily disabled, whilst manufacturers claim to prevent that and take no responsibility at all (tech tends to do that for decades now). [3](https://www.404media.co/how-to-disable-meta-rayban-led-light/)
* Smart glasses have been used for instant facial recognition before [4](https://www.404media.co/someone-put-facial-recognition-tech-onto-metas-smart-glasses-to-instantly-dox-strangers/) and reportedly will be out of the box [5](https://www.nytimes.com/2026/02/13/technology/meta-facial-recognition-smart-glasses.html). This puts a lot of people in danger.
* They data is used to train AI, which means, people will screen the recordings and see, liekly, most intimate, insights [6](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)
* I hope this app is useful for someone.

## How?

* It's a simple rather heuristic approach. Because BLE uses randomised MAC and the OSSID are not stable, nor the UUID of the service announcements, you can't just scan for the bluetooth beacons. And, to make thinks even more dire, some like Meta, for instance, use proprietary Bluetooth services and UUIDs are not persistent, ~~we can only rely on the communicated device names for now~~.
* The currently **most viable approach** comes from the [Bluetooth SIG assigned numbers repo](https://www.bluetooth.com/specifications/assigned-numbers/). Following this, the manufacturer company's name shows up as number codes in the packet advertising header (ADV) of BLE beacons.
* this is what BLE advertising frames look like:

root@kitploit:~

```
Frame 1: Advertising (ADV_IND)
Time:  0.591232 s
Address: C4:7C:8D:1E:2B:3F (Random Static)
RSSI: -58 dBm

Flags:
  02 01 06
    Flags: LE General Discoverable Mode, BR/EDR Not Supported

Manufacturer Specific Data:
  Length: 0x1A
  Type:   Manufacturer Specific Data (0xFF)
  Company ID: 0x058E (Meta Platforms Technologies, LLC)
  Data: 4D 45 54 41 5F 52 42 5F 47 4C 41 53 53

Service UUIDs:
  Complete List of 16-bit Service UUIDs
  0xFEAA
```

* According to the [Bluetooth SIG assigned numbers repo](https://github.com/yjeanrenaud/yj_nearbyglasses/blob/main/www.bluetooth.com/specifications/assigned-numbers), we may use these company IDs:
  + `0x01AB` for `Meta Platforms, Inc. (formerly Facebook)`
  + `0x058E` for `Meta Platforms Technologies, LLC`
  + `0x0D53` for `Luxo...