---
title: The cryptography behind electronic passports
url: https://blog.trailofbits.com/2025/10/31/the-cryptography-behind-electronic-passports/
source: The Trail of Bits Blog
date: 2025-10-31
fetch_date: 2025-11-01T03:11:16.370473
---

# The cryptography behind electronic passports

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The cryptography behind electronic passports

Joop van de Pol

October 31, 2025

[cryptography](/categories/cryptography/), [zero-knowledge](/categories/zero-knowledge/), [threat-modeling](/categories/threat-modeling/)

Page content

* [Electronic passport basics](#electronic-passport-basics)
  + [How the eMRTD application works](#how-the-emrtd-application-works)
* [Digging into the threat model](#digging-into-the-threat-model)
* [Cryptographic mechanisms](#cryptographic-mechanisms)
  + [Legacy cryptography](#legacy-cryptography)
  + [Modern enhancements](#modern-enhancements)
* [Gaps in the threat model: Why you shouldn’t give your passport to just anyone](#gaps-in-the-threat-model-why-you-shouldnt-give-your-passport-to-just-anyone)
* [Security and privacy implications of zero-knowledge identity proofs](#security-and-privacy-implications-of-zero-knowledge-identity-proofs)

Did you know that most modern passports are actually embedded devices containing an entire filesystem, access controls, and support for several cryptographic protocols? Such passports display a small symbol indicating an electronic machine-readable travel document (eMRTD), which digitally stores the same personal data printed in traditional passport booklets in its embedded filesystem. Beyond allowing travelers in some countries to skip a chat at border control, these documents use cryptography to prevent unauthorized reading, eavesdropping, forgery, and copying.

![Image showing the Chip Inside symbol](/img/passports_figure_1.png)

Figure 1: Chip Inside symbol (ICAO Doc 9303 Part 9)

This blog post describes how electronic passports work, the threats within their threat model, and how they protect against those threats using cryptography. It also discusses the implications of using electronic passports for novel applications, such as zero-knowledge identity proofs. Like many widely used electronic devices with long lifetimes, electronic passports and the systems interacting with them support insecure, legacy protocols that put passport holders at risk for both standard and novel use cases.

## Electronic passport basics

A passport serves as official identity documentation, primarily for international travel. The International Civil Aviation Organization (ICAO) defines the standards for electronic passports, which (as suggested by the “Chip Inside” symbol) contain a contactless integrated circuit (IC) storing digital information. Essentially, the chip contains a filesystem with some access control to protect unauthorized reading of data. The full technical details of electronic passports are specified in [ICAO Doc 9303](https://www.icao.int/publications/doc-series/doc-9303); this blog post will mostly focus on part 10, which specifies the logical data structure (LDS), and part 11, which specifies the security mechanisms.

![Flowchart showning electronic passport logical data structure](/img/passports_figure_2.png)

Figure 2: Electronic passport logical data structure (ICAO Doc 9303 Part 10)

The filesystem architecture is straightforward, comprising three file types: master files (MFs) serving as the root directory; dedicated files (DFs) functioning as subdirectories or applications; and elementary files (EFs) containing actual binary data. As shown in the above figure, some files are mandatory, whereas others are optional. This blog post will focus on the eMRTD application. The other applications are part of LDS 2.0, which would allow the digital storage of travel records (digital stamps!), electronic visas, and additional biometrics (so you can just update your picture instead of getting a whole new passport!).

### How the eMRTD application works

The following figure shows the types of files the eMRTD contains:

![Image showing the contents of the eMRTD application](/img/passports_figure_3.png)

Figure 3: Contents of the eMRTD application (ICAO Doc 9303 Part 10)

There are generic files containing common or security-related data; all other files are so-called data groups (DGs), which primarily contain personal information (most of which is also printed on your passport) and some additional security data that will become important later. All electronic passports must contain DGs 1 and 2, whereas the rest is optional.

![Image showing DGs in the LDS](/img/passports_figure_4.png)

Figure 4: DGs in the LDS (ICAO Doc 9303 Part 10, seventh edition)

Comparing the contents of DG1 and DG2 to the main passport page shows that most of the written data is stored in DG1 and the photo is stored in DG2. Additionally, there are two lines of characters at the bottom of the page called the machine readable zone (MRZ), which contains another copy of the DG1 data with some check digits, as shown in the following picture.

![Image showing an example passport with MRZ](/img/passports_figure_5.png)

Figure 5: Example passport with MRZ (ICAO Doc 9303 Part 3)

## Digging into the threat model

Electronic passports operate under a straightforward threat model that categorizes attackers based on physical access: those who hold a passport versus those who don’t. If you are near a passport but you do not hold it in your possession, you should not be able to do any of the following:

* Read any personal information from that passport
* Eavesdrop on communication that the passport has with legitimate terminals
* Figure out whether it is a specific passport so you can trace its movements[1](#fn:1)

Even if you do hold one or more passports, you should not be able to do the following:

* Forge a new passport with inauthentic data
* Make a digital copy of the passport
* Read the fingerprint (DG3) or iris (DG4) information[2](#fn:2)

Electronic passports use short-range RFID for communication (ISO 14443). You can communicate with a passport within a distance of 10–15 centimeters, but eavesdropping is possible at distances of several meters[3](#fn:3). Because electronic passports are embedded devices, they need to be able to withstand attacks where the attacker has physical access to the device, such as elaborate side-channel and fault injection attacks. As a result, they are often certified (e.g., under Common Criteria).

We focus here on the threats against the electronic components of the passport. Passports have many physical countermeasures, such as visual effects that become visible under certain types of light. Even if someone can break the electronic security that prevents copying passports, they would still have to defeat these physical measures to make a full copy of the passport. That said, some systems (such as online systems) only interact digitally with the passport, so they do not perform any physical checks at all.

## Cryptographic mechanisms

The earliest electronic passports lacked most cryptographic mechanisms. Malaysia issued the first electronic passport in 1998, which predates the first ICAO eMRTD specifications from 2003. Belgium subsequently issued the first ICAO-compliant eMRTD in 2004, which in turn predates the first cryptographic mechanism for confidentiality specified in 2005.

While we could focus solely on the most advanced cryptographic implementations, electronic passports remain in circulation for extended periods (typically 5–10 years), meaning legacy systems continue operating alongside modern solutions. This means that there are typically many old passports floating around that do not support the latest and greatest access control mechanisms[4](#fn:4). Similarly, not all inspection systems/terminals support all of the protocols, which means passports potentially need to support multiple protocols. All protocols discussed in the following are described in more detail in ICAO Doc 9303 Part 11.

### Legacy cryptography

Legacy protection mechanisms for electronic passports provide better security than what they were replacing (nothing), eve...