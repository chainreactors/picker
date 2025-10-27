---
title: Hardware investigation of wireless keyloggers
url: https://synacktiv.com/en/publications/hardware-investigation-of-wireless-keyloggers
source: Instapaper: Unread
date: 2023-03-08
fetch_date: 2025-10-04T08:57:44.812523
---

# Hardware investigation of wireless keyloggers

[Skip to main content](hardware-investigation-of-wireless-keyloggers#main-content)

[Search](../../search)

Switch Language

EnglishToggle Dropdown

* English
* [French](../../publications/hardware-investigation-of-wireless-keyloggers)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

[![Home](/sites/default/files/logo_synacktiv_blanc.webp)](../../en "Home")

* [Our offer](../our-offer)
  + [Penetration Test / Red Team](../features/penetration-test-red-team)
  + [Incident response](../features/incident-response)
  + [Reverse-engineering](../features/reverse-engineering)
  + [Development](../our-team/development)
  + [Products](../products/kraqozorus)
  + [CSIRT](../csirt)
* [Trainings](../offers/trainings)
* [Join us](../join-us)
* [Publications](../our-publications)
  + [Posts](../publications)
  + [Advisories](../advisories)
  + [Resources](../ressources)
* [The company](../the-company)
* [Contact](../contact)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

# Hardware investigation of wireless keyloggers

Written by
Antoine Cervoise
- 03/03/2023 - in
CSIRT
, Hardware

- [Download](hardware-investigation-of-wireless-keyloggers)

When a hardware keylogger is found on a computer, you can assume the user account and its secrets are compromised. In this article, we will present how to get access to the data stored on both a basic keylogger and a more advanced model with Wi-Fi access.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings).

Hardware keyloggers can be bought online for a couple of dollars and are very appreciated due to their discretion because they cannot be discovered by endpoint security software. The only condition for attackers is the usage of an external keyboard. We can assume they are used for espionage, while no public communication exists for such usage apart from a few articles[1](hardware-investigation-of-wireless-keyloggers#footnote1_xfsr3j6 "https://www.bleepingcomputer.com/news/security/student-expelled-for-usiâ¦")[2](hardware-investigation-of-wireless-keyloggers#footnote2_yryu69q "https://cybersecuritynews.com/agarwal-hardware-key-logger/")[3](hardware-investigation-of-wireless-keyloggers#footnote3_5p0jii8 "https://www.dailymail.co.uk/news/article-3281805/Three-students-chargedâ¦"). They can be bought on many websites, even Amazon, making them commonly used in private life, for example during a divorce[4](hardware-investigation-of-wireless-keyloggers#footnote4_cta9wqf "https://www.rosen.com/divorce/divorcearticles/keylogger-nc-divorce/"). Many vendors also highlight their usage for monitoring employees. These vendors also sell other kind of recording devices, such as video (recording VGA, HDMI or DVI), RS232 and even Ethernet loggers. For all these tools, the price varies according to storage capacity and features (time keeping, Wi-Fi access...). Additionally, backdoored keyboards or small PCBs to insert in existing ones can also easily be bought online.

![KeyGrabber Forensic Keylogger Cable / Module](/sites/default/files/inline-images/keylogger.webp)
> It is the smallest hardware keylogger available on the market, making it a professional surveillance and security tool. - <https://www.keelog.com/>

> The parent or employer does not need to be familiar with operating a complicated software to monitor the activities of children or employees. - <https://www.detective-store.com/>

## Targets

In this article, we will focus on the analysis of two hardware keyloggers:

* KeyDemon TimeKeeper
* Airdrive Keylogger

![Analyzed keyloggers.](/sites/default/files/inline-images/keyloggers.webp)

### KeyDemon TimeKeeper

The TimeKeeper is a classic keylogger. It can be configured for a specific layout and a time can be set if the attacker knows in advance the exact time when the keylogger will be plugged. For accessing the data, a three key combination must be pressed, which will mount the keylogger as a USB drive. This combination can also be configured in the config file. The main inconvenient for an attacker is the need of two physical accesses, a first one to drop the keylogger and a second one to get it back.

![TimeKeeper manual](/sites/default/files/inline-images/timekeeper-config.webp)

TimeKeeper manual.

The configuration file is in the same folder as the logged keystrokes:

```
$ cat config.txt
Password=KBS
LogSpecialKeys=Full
DisableLogging=No
DisableLayout=No
Encryption=No
Timestamping=Yes
$ head LOG.TXT
[2016/2/23 18:24:00][Time set]
[2016/2/23 18:25:23][Pwr][Sh]Helo ld [Sh]0[Ent]
[Sh]Hello [Sh]World [Sh]1[Ent]
[Sh]Hllo [Sh]World [Sh]2[Ent]
[Sh]Hello [Sh]World [Ent]
[Sh]Hello [Sh]World [Sh]4[Ent]
[Sh]Hello [Sh]World
[2016/2/23 18:25:33] [Sh]5[Sh]Hello [Sh]World [Sh]6[Sh]Hello [Sh]Wold [Ent]
```

Investigating this kind of device is pretty simple. You can simply brute force all the magic combination using an Arduino/Teensy/Rubber ducky/Flipper zero.

Code for Teensy:

```
void setup() {}

void loop() {
  delay(1000);
  for (int i = 4 ; i < 30 ; i++) {
    for (int j = 4 ; j < 30 ; j++) {
      for (int k = 4 ; k < 30 ; k++) {
        if ((i != j) and (j != k) and ( i != k)) {
          Keyboard.press(i | 0xF000);
          Keyboard.press(j | 0xF000);
          Keyboard.press(k | 0xF000);
          delay(150);
          Keyboard.releaseAll();
        }
      }
    }
  }
  delay(1000);
  while(1) {}
}
```

Code for Arduino:

```
void setup() {
  Keyboard.begin();
}

void loop() {
  delay(1000);
  for (int i = 97 ; i < 123 ; i++) {
    for (int j = 97 ; j < 123 ; j++) {
      for (int k = 97 ; k < 123 ; k++) {
        Keyboard.press(char(i));
        Keyboard.press(char(j));
        Keyboard.press(char(k));
        delay(150);
        Keyboard.releaseAll();
      }
    }
  }
  delay(1000);
  while(1) {}
}
```

## Airdrive Keylogger

The Airdrive Keylogger is a keylogger with a Wi-Fi hotspot which can be used to configure it and remotely dump the captured keystrokes.

![Keylogger configuration.](/sites/default/files/inline-images/configs_small.webp)

Keylogger configuration.

Â

![Keylogger logs.](/sites/default/files/inline-images/logs.webp)

Keylogger logs.

To access the device, our first attempts focused the Wi-Fi interface. By default, the keylogger is providing an access point with the *AIR\_XXXXXX* name pattern (the SSID can be changed and/or hidden). However, because no client is connected on the device and the Wi-Fi chip is not vulnerable to the PMKID attack[5](hardware-investigation-of-wireless-keyloggers#footnote5_khybcwr "https://hashcat.net/forum/thread-7717.html"), the only remaining method was to brute force the PSK online, which is pretty slow and rarely successful.

### ESP8266 inside

Our approach was therefore to open the device, which revealed a simple layout with all the interesting hardware on the same side:

![Keylogger components.](/sites/default/files/inline-images/keylogger_open.webp)

Keylogger components.

- A 5M160Z chip.
- An ESP8266 chip, used for the Wi-Fi interface.
- A Winbond Flash used for storage.

#### Flash dump

The Winbond Flash canÂ easily be identified by reading the reference from its shield: 25Q128JVSQ. Performing a dump of such chips is common and well documented on the Internet, and an Hydrabus was used to do so[6](hardware-investigation-of-wireless-keyloggers#footnote6_s4163i5 "https://github.com/hydrabus/hydrafw/wiki/HydraFW-SPI-guide#flashrom-usaâ¦") with a clip. However, trying to read the flash will not work due to VCC being connected to the master component on the device. As we are powering the flash during the dump, the main chip is powered up and also tries to access it.

An easy solution is to unsolder the Winbond Flash and read it offline. Another way would have been to put ...