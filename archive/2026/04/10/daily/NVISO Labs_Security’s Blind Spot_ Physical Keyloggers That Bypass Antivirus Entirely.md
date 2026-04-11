---
title: Security’s Blind Spot: Physical Keyloggers That Bypass Antivirus Entirely
url: https://blog.nviso.eu/2026/04/10/securitys-blind-spot-physical-keyloggers-that-bypass-antivirus-entirely/
source: NVISO Labs
date: 2026-04-10
fetch_date: 2026-04-11T04:21:09.398646
---

# Security’s Blind Spot: Physical Keyloggers That Bypass Antivirus Entirely

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [AI Security](https://blog.nviso.eu/category/ai-security/)
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Security’s Blind Spot: Physical Keyloggers That Bypass Antivirus Entirely

[Carina Schwabe](https://blog.nviso.eu/author/carina-schwabe/ "Posts by Carina Schwabe")

[Blue Team](https://blog.nviso.eu/category/blue-team/)

April 10, 2026April 10, 2026
11 Minutes

## Keyloggers: A Persistent Threat

Nowadays, virtually all digital services rely on logins and authentication, from email inboxes to help desks. These involve login credentials to prove identity, typically at least a username and a password. Initially, this information is confidential from a potential attacker. While a username can be relatively easy to guess in a world of SSO and email addresses as usernames, an attacker has to reach deeper into their bag of tricks to uncover a password.

One way to do this is through keyloggers. Keyloggers are tools that covertly record all keystrokes and transmit them to an attacker. Broadly, there are two types: software-based keyloggers and physical keyloggers. Malware keyloggers are often a secondary feature of so‑called stealer malware, which actively collects stored browser passwords, session cookies, tokens, and other secrets from the infected system and sends them to the attacker. Live keystroke recording is mostly an add‑on to modern stealer malware. However, kernel‑mode or user‑mode native keyloggers are much rarer but still exist as standalone malware in targeted attacks. Physical keyloggers, on the other hand, are hardware components—usually a cable or an inline device—physically connected to the system or a peripheral like the keyboard. However, there are also variants that are built directly into a keyboard, making them even less conspicuous. The captured data is then either stored on the device for later physical retrieval or accessed by the attacker wirelessly.

While stealer malware can theoretically be detected by an EDR system through anomaly detection, this isn’t possible with physical keyloggers. Stealer malware always leaves traces—processes, API calls, and data exfiltration from the system. Even though modern stealer malware can hide well using various evasion and obfuscation techniques, these traces still offer detection opportunities, especially when there are implementation flaws. Also, some EDRs can flag low‑level keyboard hook abuse (`SetWindowsHookEx`, `GetAsyncKeyState` patterns) despite obfuscation. The physical keylogger used for the following testing, by contrast, doesn’t spawn processes, change settings, or exfiltrate data via the system itself. It leaves no traces in the operating system since it is a USB HID (Human Interface Device) passthrough device and isn’t part of the system. Instead, it sits between the keyboard and the victim system, presenting itself to the OS as the legitimate peripheral. HIDs (Human Interface Devices) are peripherals like keyboards, mice, and game controllers that communicate user input to a computer using standardized protocols for plug‑and‑play operation. From the OS perspective, there’s no sign of an unusual driver, file, or memory artifact. Also, keystrokes appear exactly like legitimate user input. However, it should be noted that there are keyloggers in the wild that identify as a peripheral or mass storage device with their own VID/PID.

While EDRs may have USB control policies or monitor for new USB devices being attached, they analyze traditional artifacts (primarily processes, memory, APIs, registry, as well as file and network activity) for detection. Thus, once installed, the physical keylogger remains invisible. Without any interaction at the OS level, the EDR sees no suspicious activity. In effect, a physical keylogger operates like an external observer looking over the user’s shoulder and recording every keystroke. With this mode of operation, a physical keylogger undermines the principles that modern security mechanisms rely on—namely OS interactions, logging, and software artifacts for anomaly detection. The question isn’t which malicious process was started or when a network connection was made, but rather who had physical access to the devices to install a piece of hardware. Instead of searching through logs and software artifacts, the focus suddenly shifts to access control records, camera footage, and hardware replacement cycles—data points that, in standard incidents, play a secondary role at best.

The investigation of a physical keylogger therefore pursues several objectives: understanding how it works, identifying potential detection approaches, and—where possible—deriving practical defense and prevention measures.

---

## AirDrive Forensic: One Cable to Uncover All Your Secrets

To take a closer look at a device, we selected the AirDrive Forensic Keylogger Cable Pro from the vendor Keelog[1](#edc5ce02-fe75-4836-b2c1-5074de7428cd) as we encountered it during an DFIR engagement. Since every keylogger can potentially work differently, the following statements apply exclusively to this model. Keelog describes the keylogger as an “ultra-compact USB keylogger hidden inside a USB extension cable. Externally, the USB cable is indistinguishable from standard cables and does not attract attention.”

![A black USB cable with a standard USB connector on one end and a smaller connector on the other end.](https://blog.nviso.eu/wp-content/uploads/2026/02/image.png)

AirDrive Forensic Keylogger Cable Pro

In the Pro version, the AirDrive not only records keystrokes but also supports accessing the log data via Wi‑Fi. To do this, the device creates its own network with the default SSID `AIR_XXYYZZ`. In our tests, the AirDrive operated exclusively as a Soft AP (access point) on 2.4 GHz, broadcasting its own SSID and serving a local admin page at 192.168.4.1. After connecting to the Wi‑Fi hotspot broadcasted by the keylogger and navigating to the IP address 192.168.4.1, you can view and download the recorded data (as can be seen in the screenshot below). It also offers a range of configuration options—from keyboard layout to network settings—where you can define a custom SSID and password.

![Screenshot of an AirDrive data log interface displaying various entries, commands, and test results.](https://blog.nviso.eu/wp-content/uploads/2026/01/image-24.png)

Log provided by the keylogger via WiFi

While we did observe the keylogg...