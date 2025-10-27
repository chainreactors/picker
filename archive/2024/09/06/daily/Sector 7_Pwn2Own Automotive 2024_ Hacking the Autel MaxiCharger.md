---
title: Pwn2Own Automotive 2024: Hacking the Autel MaxiCharger
url: https://sector7.computest.nl/post/2024-08-pwn2own-automotive-autel-maxicharger/
source: Sector 7
date: 2024-09-06
fetch_date: 2025-10-06T18:37:34.429968
---

# Pwn2Own Automotive 2024: Hacking the Autel MaxiCharger

[![](/images/logo.png)](/)

* [Research](/)
* [About](/about/)
* [Contact](/contact/)
* [Computest](https://computest.nl/)

* [Mastodon](https://infosec.exchange/%40sector7)
* [Bluesky](https://bsky.app/profile/sector7-nl.bsky.social)
* [LinkedIn](https://www.linkedin.com/company/computest)
* [GitHub](https://github.com/sector7-nl)
* [RSS](/index.xml)

September 5, 2024

# Pwn2Own Automotive 2024: Hacking the Autel MaxiCharger

![](/post/2024-08-pwn2own-automotive-autel-maxicharger/header.jpg)

During Pwn2Own Automotive 2024 in Tokyo, we demonstrated exploits against three different EV chargers: the Autel MaxiCharger (MAXI US AC W12-L-4G), the [ChargePoint Home Flex](https://sector7.computest.nl/post/2024-08-pwn2own-automotive-chargepoint-home-flex/) and the [JuiceBox 40 Smart EV Charging Station with WiFi](https://sector7.computest.nl/post/2024-08-pwn2own-automotive-juicebox-40/). This is our writeup of the research we performed on the Autel MaxiCharger, the bugs we found (CVE-2024-23958, CVE-2024-23959 and CVE-2024-23967) and the exploits we developed. During the competition, we were able to execute arbitrary code on this charger with no other prerequisites than being in range of Bluetooth.

# Background

Of the chargers we looked at, the Autel MaxiCharger had by far the most extensive hardware feature set. Just from the outside, we could already see:

* WiFi
* Ethernet port
* Bluetooth
* 4G LTE connection (with a SIM card slot)
* RFID reader
* LCD touch screen
* RS485
* Undocumented USB-C port next to the SIM card slot

The app also shows a lot of features we didn’t see on the other chargers. For example, users can specify the OCPP URL the charger will connect to. It even allows users to set a charger up as a *public* charger, which means the charger accepts arbitrary RFID charging cards and the owner gets reimbursed for the energy used. This is a very interesting feature to keep in mind.

![Home Charger Sharing.](home.png#center)

Inside the charger, we found a lot of nicely labelled test points, including multiple UARTs. We even found some unused internal micro-USB headers on the PCBs, although we didn’t try them, so we don’t know what data they may carry.

The hardware we did identify includes:

* A GigaDevices GD32F407 as the Charge Control Module (ECC).
* An ESP32-WROOM-32D running the AT firmware, used exclusively for WiFi and Bluetooth.
* An ST Micro STM32F407ZGT6 as the Power Control Module (ECP).
* A Quectel EC25-AFX (4G LTE).
* An LCD controller for which we had firmware (an LCD Control Module, LCD Information Unit, LCD Resources Unit and LCD Languages Unit), but no information on what type of chip.

We are not totally sure all of this is correct: the charger has a lot of functionality, split out over a lot of different components. Many of those were not relevant to our research. For example, we are unsure of the use of the Barrot BR8051A01 chip, identified [by ZDI as a bluetooth radio](https://www.zerodayinitiative.com/blog/2023/11/28/a-detailed-look-at-pwn2own-automotive-ev-charger-hardware), as everything we’ve seen suggests the ESP32 handles both WiFi and Bluetooth.

# Obtaining the firmware

Obtaining the firmware was by far the hardest part of hacking this charger.

The first time we turned it on, we paired a phone over Bluetooth and connected the charger to a WiFi network that was capturing all traffic with tcpdump. We initiated a firmware update that was available, but later on we saw that the packet capture had obtained nothing relevant. Apparently, the phone was downloading the update and sending it over Bluetooth to the charger.

We tried again while intercepting the network traffic of the phone with Burp. We determined that the update process works like this:

* The app requests the versions of all firmware components from the main controller of the charger over BLE.
* The app submits this information to Autel’s server.
* At any later point, the app can ask the server if there are any updates for that charger.
* If there are any, the server sends back an URL for each component for which an update is available.
* The app downloads the files from those URLs and sends them over BLE to the charger.
* The main controller of the charger sends the update to the right component.

We tried to replicate this, but the URLs we got back were obfuscated. To deobfuscate them, we tried decompiling it or hooking into the app. This turned out way harder than we expected: the code of the mobile apps is obfuscated and the app contains anti-debugging tricks.

Eventually, we gave up with the app and looked a bit more closely at the obfuscated URLs we had gotten back, and noticed that they do look quite close to being base64 encoded. If we base64 decode them, we don’t get back readable text, but we can see that some bytes line up with a (pre-signed) Amazon S3 URL:

![Base 64 decoded obfuscated URL.](url.png#center)

By guessing some characters (like the “https://” at the start) and comparing the base64 encoded version of the guessed URL with the actual data, we could work out (step by step) that all they did was applying a simple substitution before base64 decoding:

* A ➔ a
* a ➔ A
* B ➔ b
* b ➔ B
* C ➔ c
* c ➔ C
* D ➔ d
* d ➔ D
* E ➔ e
* e ➔ E
* F ➔ f
* f ➔ F
* G ➔ g
* g ➔ G
* 7 ➔ y
* y ➔ 7

With that figured out, we could download the firmware files. To get all the URLs of the firmware for each component, we had to ask the server. As our charger was now on the latest version, it would not reply with any URLs until the next update was available.

For most of the components of the charger, we found we could just submit a lower version number as the current version by subtracting 1 from the minor version to get back the URL for the current version. For one of the components, this didn’t work: it was on version 0.00 and we could not submit anything lower. But we had the firmware of the main controller, which was the target we were most interested in.

## Decrypting the firmware

These files were again obfuscated, but also not very well. We could observe a pattern that was repeating every 256 bytes:

![Repeating pattern in a firmware file.](firmware.png#center)

This suggests it could be a XOR with a 256 byte key. We made some guesses of what this key could be: we first looked for each offset in the 256-byte blocks which byte value was most common, and then we looked at which 256-block in its entirety was most common. Firmware files quite often contain sections that are filled with just NUL bytes, this way we hoped to determine the XOR value of a NUL byte (at each offset in the key). Both of these methods resulted in almost the same key. XORing the entire file with these keys did not result in a readable file.

Then we tried using subtraction instead of a XOR, which also did not produce a readable file. But there were tiny fragments that were correct, small bits of readable text, or line endings that line up correctly to the end of a string. But when we tried to start from those and guess the characters before or after it, we found that this would corrupt a small fragment a block at a different place in the file. So, it clearly wasn’t just adding/subtracting either.

![File after subtracting the value that is most common at that offset in a 256-byte block.](subtracted.png#center)

Our next guess was a combination of a addition/subtraction and a XOR. This would mean we were looking for two 256-byte keys. The small correctly decrypted fragments are actually logical for this obfuscation method.

### Mathematical background

We can explain the occurrence of correctly decrypted bytes for our subtraction attempt mathematically, but feel free to skip this section if you are not interested in that.

Suppose the encryption is applied as (all of this per byte, so modulo 256):

```
ciphertext = (plaintext ^ b) + a
```

Then the ciphertext for a zero byte is just `(b ^ 0) + a = b + a`. When we subtract this value, we end up with:

```
subtracted = (plaintext ^...