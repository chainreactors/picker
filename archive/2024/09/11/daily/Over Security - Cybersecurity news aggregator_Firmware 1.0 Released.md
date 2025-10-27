---
title: Firmware 1.0 Released
url: https://blog.flipper.net/released-firmware-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-11
fetch_date: 2025-10-06T18:32:42.795589
---

# Firmware 1.0 Released

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipperzero.one/)
* [Shop](https://shop.flipperzero.one/)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipperzero.one/downloads)
* [Community](https://flipperzero.one/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

# Firmware 1.0 Released

* [![Ruslan Nadyrshin](/content/images/size/w100/2024/03/007.jpg)](/author/ruslan/)
* [![Alexey Zakharov](/content/images/size/w100/2024/08/IMG_7628.jpeg)](/author/alexey/)

#### [Ruslan Nadyrshin](/author/ruslan/), [Alexey Zakharov](/author/alexey/)

Sep 10, 2024

![Firmware 1.0 Released](/content/images/size/w2000/2024/09/Flipper_Zero_Firmware_1.0_main_illustration_compressed-1.jpg)

Meet the first major release of Flipper Zero firmware — version 1.0. In this release, we have completed work on many features that have been in development for 3 years and are now stable. In this post, we’ll show you what’s new in Firmware 1.0 and the challenges we faced during development.

## What’s new in Firmware 1.0

![upload in progress, 0](https://blog.flipper.net/content/images/2024/09/Flipper_Zero_Firmware_1.0_whats_new_02--1-.png)

— Mom, look! We can draw just like Apple®!

* **3rd-party apps:** We’ve introduced dynamic app loading support. Now you can install hundreds of community-developed apps from the Apps Catalog, and the number of apps continues to grow.
* **New NFC subsystem:** Completely rewritten from scratch, resulting in a significant increase in card reading speed. New NFC card types support and a new plugin system for user card parsers.
* **JavaScript support:** You can now develop apps for Flipper Zero using JavaScript.
* **General system improvements:** Battery life reaches 1 month in standby. Bluetooth data transfer speed with Android devices increased by up to 2x. Firmware updates now upload via Bluetooth 40% faster.

# Apps on Flipper Zero

![upload in progress, 0](https://blog.flipper.net/content/images/2024/07/Flipper_Zero_apps_installation.jpg)

Initially, all features in Flipper Zero were implemented as part of the firmware. Every new feature or fix required a full firmware update. It was a pain on both ends: we had to compile and make a new release, and users then had to install it. One more problem was the system flash memory limit, which we had reached a long time ago. At some point, we could no longer add new features to our Flipper Zero firmware.

## Dynamic app loading subsystem

To continue adding new features, we developed something unusual for embedded hardware: **dynamic application loading**. Thanks to it, Flipper Zero is now able to run applications right from FAP files on the microSD card (FAP stands for Flipper Application Package, our special format of compiled application files). A new firmware component named **app loader** handles loading and launching FAPs. This way, we could finally continue adding new features and store them outside the firmware, saving space on system flash memory.

![upload in progress, 0](https://blog.flipper.net/content/images/2024/08/Flipper_Zero_dynamic_app_loading_from_microSD_card.jpg)

Developers loved this idea and have created hundreds of applications! However, these were scattered across different communities and forums, making it difficult for users to find them. That’s why we created the Apps Catalog, where apps made by the community are available in one place. We are especially proud that all apps in our catalog are **open source**, and we’re grateful to our community’s enthusiasts for developing and maintaining them. [Learn how to submit your app to the Apps Catalog.](https://github.com/flipperdevices/flipper-application-catalog/blob/main/documentation/Contributing.md)

## How to install Apps on Flipper Zero

You can install apps on your Flipper Zero from the Apps Catalog, which is available via [Flipper Mobile App](https://flpr.app/?ref=blog.flipper.net) and [Flipper Lab](https://lab.flipper.net/apps). Installing apps on Flipper Zero is now as easy as on your phone:

[![](https://img.spacergif.org/v1/1920x1080/0a/spacer.png)](https://blog.flipper.net/content/media/2024/08/flipperzero-app-install-4.mp4)

0:00

/0:21

1×

[Video] Community apps can be installed on Flipper Zero from the Apps Catalog

For convenience, apps in the Apps Catalog are grouped into categories based on their features: Sub-GHz, NFC, RFID, Games, Media, Tools, and others.

# JavaScript on Flipper Zero

We’ve added a scripting engine to the firmware, allowing you to run apps written in JavaScript, one of the most common programming languages. This also **makes development much easier** compared to using C/C++, as you don’t need to set up a development environment on your computer and learn the Flipper Zero firmware SDK.

![upload in progress, 0](https://blog.flipper.net/content/images/2024/09/Flipper_Zero_JavaScript_support_new.png)

Add JS files to Flipper Zero via qFlipper or Flipper Lab

To run a script on your Flipper Zero, add the JS file to the `SD Card/apps/Scripts` folder (via qFlipper or Flipper Lab) and run it from the `Apps → Scripts` menu. There is no need to compile JS scripts on a PC.

We included example scripts in the firmware for you to start learning JavaScript on Flipper Zero. These examples are located at `SD Card/apps/Scripts`. They will help you learn the language syntax and understand how to use JavaScript modules. For more information on the scripting engine’s capabilities and limitations, please refer to [our documentation](https://developer.flipper.net/flipperzero/doxygen/js.html).

JavaScript support is based on the [mJS scripting engine](https://github.com/cesanta/mjs). Originally designed for microcontrollers, mJS utilizes system resources efficiently and operates relatively quickly. It requires less than **50k of flash space** and **2k of RAM**.

# New NFC subsystem

![upload in progress, 0](https://blog.flipper.net/content/images/2024/08/Flipper_Zero_new_NFC_subsystem.png)

NFC is one of the largest subsystems in Flipper Zero’s firmware and hardware. Previously, to work with NFC, we used the [RFAL library](https://www.st.com/en/embedded-software/stsw-st25rfal002.html) by STMicroelectronics, the manufacturer of the NFC chip inside Flipper Zero. However, this library was poorly optimized for RTOS, consumed a lot of memory, and slowed down our NFC subsystem.

To address this, we’ve **completely redesigned** our NFC subsystem from scratch, significantly improving its speed and making it easier to support new NFC card protocols.

## What’s new in the NFC subsystem

* **FreeRTOS friendly:** The old RFAL library required polling to get events from the NFC subsystem. The new library uses an event-driven approach, which is efficient when using RTOS. This simplified the code and eliminated unnecessary delays in the NFC subsystem. [See the code on GitHub.](https://github.com/flipperdevices/flipperzero-firmware/blob/7c88a4a8f1062063b74277c03617fb9e083e538b/targets/f7/furi_hal/furi_hal_nfc_event.c#L47)
* **Improved architecture:** In the RFAL library, several protocols can be implemented within one huge file of thousands of lines, and a single protocol can be scattered throughout the library. This made it difficult to add and support NFC protocols. To address this issue, we restructured the library and strictly divided the protocols based on stack layers. [See the protocols on GitHub.](https://github.com/flipperdevices/flipperzero-firmware/tree/dev/lib/nfc/protocols)
* **Parsers are now dynamic:** Initially, card data parsers were integrated into the NFC app and loaded into RAM along with it, which occasionally caused a lack of RAM. Now, parsers are FALs (Flipper App Library) that can be loaded one by one. Community members can add support for their card types by creating parsers by implementing a simple interface. [See the code on GitHub.](https://g...