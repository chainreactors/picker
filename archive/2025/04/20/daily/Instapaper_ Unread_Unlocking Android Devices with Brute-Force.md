---
title: Unlocking Android Devices with Brute-Force
url: https://belkasoft.com/unlocking-android-devices-with-brute-force
source: Instapaper: Unread
date: 2025-04-20
fetch_date: 2025-10-06T22:04:18.136010
---

# Unlocking Android Devices with Brute-Force

* +1 (650) 272-0384
* [Sign in](/signin)

* Solutions

  [For Business

  Boost cyber incident response, eDiscovery and forensics capacity of your organization.](/corporate)
  [For Law Enforcement

  Acquire, examine and report digital evidence in a forensically sound way.](/law-enforcement)
  [For Academia

  Learn the art of digital forensics and cyber incident response with Belkasoft's training.](/academic)
* Products

  [Belkasoft X Forensic

  For law enforcement: Acquire, examine and analyze evidence from mobile, computer, drones, cars and cloud
  sources.](/x)
  [Belkasoft X Corporate

  For corporate customers: Carry out forensic examinations, conduct investigations into cyber incidents, and provide incident response.](/corporate)
  [Belkasoft Remote Acquisition

  A part of Belkasoft X Corporate for remotely acquiring data and evidence from computers and mobile devices
  around the world.](/r)
  [Belkasoft Incident Investigations

  A part of Belkasoft X Corporate for identifying infiltration points of malicious code and originating attack
  vectors to harden your cybersecurity.](/n)
  [Belkasoft Triage

  Instantly perform effective triage analysis of Windows devices in the
  field on scene.](/t)

  [Belkasoft Live RAM Capturer

  A tiny free forensic tool that allows to reliably extract the entire
  contents of computer’s volatile memory.](/ram-capturer)
* [Training](/training)
* Resources

  [Blog](/articles#blog)
  [Articles](/articles#article)
  [Whitepapers](/whitepapers)
  [Webinars](/webinar)
  [BelkaTalk](/belkatalk)
  [Tutorials](/tutorials)
  [Newsroom](/news)
  [Product Releases](/new)
  [Testimonials](/testimonials)
  [Case Studies](/case_studies)
  [BelkaCTF](/ctf)
  [User Guide](/help)
* Company

  [About](/company)
  [News](/news)
  [Customers](/customers)
  [Partners](/partners)
  [Contact Us](/contact)
* [![Get started](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/73846a5e-e69a-4352-8c78-bd41126272e8.png)](https://hubspot-cta-redirect-eu1-prod.s3.amazonaws.com/cta/redirect/26836331/73846a5e-e69a-4352-8c78-bd41126272e8)

[#blog](/articles#blog)

# Unlocking Android Devices with Brute-Force

### Table of Contents

* [Android lock screen brute‑force in a nutshell](#nutshell)
* [Unisoc brute‑force specifics](#unisoc)
* [MediaTek (MTK) brute‑force specifics](#mtk)
* [Kirin brute‑force specifics](#kirin)
* [Final thoughts: Do not give up on locked evidence!](#final)
* [See also](#see-also)

![](/images/blog/android-device-passcode-brute-force-cover.jpg)

Even non-DFIR people nowadays know that manually guessing an unknown passcode is the fastest way to permanently lose access to a device—and its data. Device manufacturers and software developers have done an impressive job protecting user data. And even if there are no login attempt limits, doing Android pin brute-force by hand with thousands and millions of possible combinations? Clearly not an option.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-250061186275.png)](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLIQb%2FQS%2F3jD3V9jXofUV85pZzAGaN6O4ghz2AOSSSEMIX%2FMocV079KeLn0Nm7T8F8CoLVV3ik9SAMJ7MqG8EJv9Gi2NaCT6Ml4QkU5D70IVgpq4ZXUt0HhvCMqObSObTvQoFEZFZTpu9VAHu0pbrgJfvzYyK1RoA54l8D9%2FtA%3D%3D&webInteractiveContentId=250061186275&portalId=26836331)

![A locked Android phone with a passcode timeout](/images/articles/unlocking-android-devices-with-brute-force/unlock-android-01-locked-android.jpg)

So, how to unlock an Android device for forensic purposes? Find a vulnerability that lets you break into the system, bypass restrictions (at least, part of them), and launch an automated brute-force attack.

Easier said than done.

Android devices are incredibly diverse. While they share common security features, there is no one-size-fits-all approach. The available solutions target specific groups of chipset models, that is why each Android password brute-force method in [Belkasoft X](/x) comes with its own workflow—depending on whether you are dealing with a MediaTek, Kirin, or Unisoc-based device.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-250061186275.png)](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLIQb%2FQS%2F3jD3V9jXofUV85pZzAGaN6O4ghz2AOSSSEMIX%2FMocV079KeLn0Nm7T8F8CoLVV3ik9SAMJ7MqG8EJv9Gi2NaCT6Ml4QkU5D70IVgpq4ZXUt0HhvCMqObSObTvQoFEZFZTpu9VAHu0pbrgJfvzYyK1RoA54l8D9%2FtA%3D%3D&webInteractiveContentId=250061186275&portalId=26836331)

## Android lock screen brute-force in a nutshell

Most Android devices that end up in forensic labs nowadays have user data encrypted. The encryption keys used to secure it are derived in the Trusted Execution Environment (TEE) after the device is booted and the user supplies their passcode. They are based on **device-specific keys** and the keys derived from **the user’s lock screen passcode**.

Forensic brute-force attacks leverage chipset-specific vulnerabilities, exploiting weaknesses in the boot process like insecure boot ROMs or debug modes. In particular, Belkasoft X can interrupt the secure boot chain, obtain code execution at a low level, and extract the keys needed to **brute-force the passcode** from TEE. **It runs the brute-force attack offline**—avoiding Android’s normal throttling (delays or attempt limits). The passcode guessing speed depends on the complexity of the key derivation function and on the computing capacity of the digital forensic workstation.

This process does not interact with user data dumped from the device, that is why it is unlikely to alter information or cause data loss.

![The Belkasoft X screen displaying a prompt whether the uses wants to brute-force mobile passcode](/images/articles/unlocking-android-devices-with-brute-force/unlock-android-02-would-you-brute-force.jpg)

## Unisoc brute-force specifics

Unisoc’s low-cost processors (formerly Spreadtrum) are found in many budget Android devices. Some of these SoC models include vulnerabilities that allow code execution in the BootROM simply via USB when the device is booted into Spreadtrum Download Mode (SPD). Belkasoft X exploits them to run its own code at the earliest boot stages, dump encryption key material, and brute-force the passcode offline. BootROM flaws are not patchable via software update (they are in read-only memory), so affected SoCs remain vulnerable.

This brute-force method is part of the Spreadtum acquisition workflow, and it is easy and relatively fast to run. You just need to install a couple of drivers, put the Unicoc device into the SPD mode, and begin the process.

## MediaTek (MTK) brute-force specifics

MediaTek SoCs power a variety of Android devices (especially mid-range phones by Xiaomi, Vivo, Oppo, and the like). Many of these devices lack a dedicated secure element and rely solely on the TEE for protection—and critically, **MTK’s BootROM has known vulnerabilities that open the door to brute-force attacks**. In particular, it allows uploading and executing unsigned code before secure boot enforcement.

Belkasoft X provides an acquisition workflow that can break into the booting process of devices based on a number of MTK chipsets. Just like with Unisoc-based devices, it downloads the physical device image and encryption key material to run the brute-force process offline.

To successfully perform MTK brute-force, you will need to install drivers for low-level communication with MTK and then put the device into BootROM mode (or Preloader mode, for some devices). The whole process requires a few more prerequisite steps and more attention than the Unisoc brute-force one, but it is still relatively easy to run, and it works quite fast.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-250061186275.png...