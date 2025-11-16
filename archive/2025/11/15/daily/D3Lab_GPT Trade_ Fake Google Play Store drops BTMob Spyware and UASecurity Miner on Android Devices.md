---
title: GPT Trade: Fake Google Play Store drops BTMob Spyware and UASecurity Miner on Android Devices
url: https://www.d3lab.net/gpt-trade-fake-google-play-store-drops-btmob-spyware-and-uasecurity-miner-on-android-devices/
source: D3Lab
date: 2025-11-15
fetch_date: 2025-11-16T03:19:23.570812
---

# GPT Trade: Fake Google Play Store drops BTMob Spyware and UASecurity Miner on Android Devices

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# GPT Trade: Fake Google Play Store drops BTMob Spyware and UASecurity Miner on Android Devices

[Malware](https://www.d3lab.net/category/malware/)

[![Fake Google Play Store](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Screenshot-2025-11-14-alle-15.54.01-1.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Screenshot-2025-11-14-alle-15.54.01-1.png?fit=1030%2C782&ssl=1 "Screenshot 2025-11-14 alle 15.54.01")

During D3Lab’s continuous monitoring of newly registered domains through our **Brand Monitor** service, we identified a domain crafted to impersonate the Google Play Store.

![Fake Google Play Store](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Screenshot-2025-11-14-alle-15.54.01-1.png?resize=1030%2C782&ssl=1)

The site advertises a supposed application called **“GPT Trade”**, presented as an AI-powered trading assistant and visually styled to resemble official ChatGPT / OpenAI branding. Unsuspecting users are encouraged to download an APK directly from the page: `https://playgoogle-gpttrade[.]com/GPT%20Trade.apk`

Our investigation revealed that **GPT Trade is not a legitimate application**, but a sophisticated **Android dropper** engineered to generate, prepare, and install multiple secondary malware payloads, including:

* **BTMob** – a powerful spyware family
* **UASecurity Miner** – a persistence-oriented component tied to a suspicious Android packing service

The overall structure of the attack shows a modern, modular approach where threat actors rely on packer-as-a-service platforms, Telegram bots, and impersonation techniques to distribute malware effectively.

---

## **From Fake App Store to Infection: How the GPT Trade Dropper Works**

![Captcha Request](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Screenshot-2025-11-14-alle-15.55.58-1.png?resize=648%2C580&ssl=1)

Once installed and opened, the GPT Trade application displays a **fake captcha screen**. To the user, this appears to be a benign verification step. In the background, however, the application immediately begins its real activity.

During this stage, the dropper:

1. Creates multiple directories inside its private storage
2. Unpacks or decrypts several embedded components
3. Generates new APK files in “processed” form
4. Prepares two distinct malicious packages

Two XML preference files reveal the dropper’s behavior clearly:

```
/shared_prefs/SplitApkInstallerminer.xml
/shared_prefs/SplitApkInstalleruser.xml
```

These files contain paths to dynamically created payloads, confirming that GPT Trade acts as a **multi-stage dropper**, not a standalone app.

Once the captcha is completed, the app triggers several dex2oat32 processes to finalize the generated APKs and silently installs both malware packages:

* **mooz.balkcigol.rotinom** (BTMob spyware)
* **com.xenlyqw.jkkcyubcust** (UASecurity Miner)

Finally, it opens **chatgpt.com** in the system browser — a social engineering technique intended to reinforce user trust and mask the compromise.

---

## **Malicious Component #1: UASecurity Miner**

**Package:** com.xenlyqw.jkkcyubcust

**SHA256:** 918f002a41f9551d48ece999ccba504fcf7596017d9566c07c5335fe0081effe

This component communicates with:

* 147[.]93[.]153[.]119 (multiple ports: 50904, 50912, 50916, 50920)
* https://aptabase[.]fud2026[.]xyz:8443/api/v0/event

Notably, the domain *aptabase[.]fud2026[.]xyz* resolves to the same IP, indicating a dedicated C2 server.

The manifest shows services designed for **continuous persistence**, including:

* Foreground services
* Boot receivers
* Firebase messaging services
* Keep-alive modules

Combined, these elements suggest a component dedicated to maintaining remote control and telemetry collection.

---

## **Malicious Component #2: BTMob Spyware**

**Package:** mooz.balkcigol.rotinom

**SHA256:** 7f005c10f80372311e9c038526d81d931672d15c644fef2a77eefd67c6235917

BTMob is a well-known and highly invasive Android spyware family. In this case, the sample contacts:

* http://95[.]164[.]53[.]100/private/yarsap\_80541[.]php
* http://95[.]164[.]53[.]100:8080/

The manifest includes an **extremely broad set of permissions**, such as:

* SMS read/send
* Contact list access
* Screen recording and media projection
* Accessibility service binding
* Camera and microphone access
* Overlay windows
* Exact alarm scheduling
* App installation/uninstallation
* File system read/write
* Location data (GPS, network, background)

This extensive set enables complete device takeover: credential theft, overlay attacks, keylogging, call or screen interception, and persistent surveillance.

---

## **Infrastructure Links: The Role of UASecurity Tools**

![APK Protection by UASecurity Tools](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Screenshot-2025-11-14-alle-16.01.47-1.png?resize=1030%2C494&ssl=1)

Before installing the secondary malware, the GPT Trade dropper contacts: `timeserver[.]uasecurity[.]org (207[.]90[.]195[.]25) – port 2000`

This domain is part of **UASecurity Tools**, a service that has been active since **August 2025** and offers Android APK “protection” through a website and a Telegram bot.

### **OSINT confirmed the existence of:**

* Website: **https://access[.]uasecurity[.]org/**
* Telegram bot: **@android\_protect\_bot**
* Official channel: **t.me/protect\_bot\_official**
* [YouTube video](https://www.youtube.com/watch?v=k93hRiFL6vs) promoting an Android C2 tool

[](https://www.d3lab.net/wp-content/uploads/2025/11/uasecurity_tools-k93hRiFL6vs.mkv-1.mp4)

The UASecurity platform provides APK packing and obfuscation services. Despite presenting itself as a legitimate “intellectual property protection” tool, its packer is clearly being abused by malware developers.

The behavior of GPT Trade — generating “original” and “processed” directories, producing installers dynamically, and using a captcha trigger — strongly matches installers created by this packer.

There is **no evidence** that UASecurity Tools directly distributes malware. However, the misuse of their service within this campaign highlights how “developer tools” can be co-opted to support malicious operations.

---

## **Conclusion**

The GPT Trade campaign demonstrates a mature and modular Android attack chain:

* **Social engineering** through a fake Google Play interface
* **A dropper acting as an APK generator**
* **Installation of two independent malware families**
* **Use of a third-party APK packer to evade detection**
* **Multiple C2 endpoints tied to distinct functionalities**

This approach reflects a growing trend in the Android threat landscape: attackers increasingly rely on outsourced infrastructure, Telegram-based distribution systems, and packer-as-a-service tools to streamline and scale their operations.

D3Lab will continue to monitor the evolution of these techniques and their associated infrastructures.

---

## **Disclaimer**

Installing applications from untrusted sources poses significant security risks.

**Always download mobile applications exclusively from official and verified app stores**, and avoid APK files distributed through webs...