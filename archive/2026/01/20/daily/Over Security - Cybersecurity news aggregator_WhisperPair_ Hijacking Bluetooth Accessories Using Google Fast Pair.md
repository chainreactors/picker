---
title: WhisperPair: Hijacking Bluetooth Accessories Using Google Fast Pair
url: https://whisperpair.eu/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-20
fetch_date: 2026-01-21T03:33:08.020251
---

# WhisperPair: Hijacking Bluetooth Accessories Using Google Fast Pair

# WhisperPair

Hijacking Bluetooth Accessories Using Google Fast Pair

[Is my device vulnerable?](/vulnerable-devices)

[About](/#about)  Cite   [Watch the video](https://www.youtube.com/watch?v=-j45ShJINtc)

Bluetooth hijacking

Many Bluetooth accessories do not implement Google Fast Pair correctly, enabling an attacker to forcefully pair with a vulnerable accessory.

 [Learn more](#bluetooth-hijacking)

Location tracking

If an accessory has never been paired with an Android device, an attacker may be able to track its location using Google's Find Hub Network.

 [Learn more](#location-tracking)

Cross-ecosystem impact

Since the Fast Pair functionality of an accessory cannot be disabled, users outside the Android ecosystem are also vulnerable to WhisperPair.

 [Learn more](#impact)

## About

[Google Fast Pair](https://www.android.com/better-together/fast-pair/) enables one-tap pairing and account synchronisation across supported Bluetooth accessories. While
Fast Pair has been adopted by many popular consumer brands, we discovered that many flagship products
have not implemented Fast Pair correctly, introducing a flaw that allows an attacker to hijack devices
and track victims using [Google's Find Hub](https://www.android.com/learn-find-hub/) network.

We introduce WhisperPair, a family of practical attacks that
leverages a flaw in the Fast Pair implementation on flagship audio accessories. Our findings
show how a small usability 'add-on' can introduce large-scale security and privacy risks for
hundreds of millions of users.

### Hijacking Fast Pair Accessories

WhisperPair enables attackers to forcibly pair a vulnerable Fast Pair accessory (e.g.,
wireless headphones or earbuds) with an attacker-controlled device (e.g., a laptop) without
user consent. This gives an attacker complete control over the accessory, allowing them to
play audio at high volumes or record conversations using the microphone. This attack succeeds
within seconds (a median of 10 seconds) at realistic ranges (tested up to 14 metres) and does
not require physical access to the vulnerable device.

The flaw stems from many accessories failing to enforce a critical step in the pairing
process. To start the Fast Pair procedure, a Seeker (a phone)
sends a message to the Provider (an accessory) indicating that it wants
to pair. The Fast Pair specification states that if the accessory is not in pairing mode, it should
disregard such messages. However, many devices fail to enforce this check in practice, allowing
unauthorised devices to start the pairing process. After receiving a reply from the vulnerable device,
an attacker can finish the Fast Pair procedure by establishing a regular Bluetooth pairing.

### Tracking Victims Using Google's Find Hub Network

Some devices also support Google's Find Hub network. This enables users to find their lost
accessories using crowdsourced location reports from other Android devices. However, if an
accessory has never been paired with an Android device, an attacker can add the accessory
using their own Google account. This allows the attacker to track the user via the compromised
accessory. The victim may see an unwanted tracking notification after several hours or days,
but this notification will show their own device. This may lead users to dismiss the warning
as a bug, enabling an attacker to keep tracking the victim for an extended period.

![A screenshot of the Find Hub app showing the location of a pair of Pixel Buds Pro 2 on the map. The app indicates that an estimated location from the Find Hub network is used.](/_app/immutable/assets/findhub-attacker.Bwm6z3Vn.png)

Figure 1: Attacker's dashboard with location from the Find Hub network.

 ![A screenshot showing an unwanted tracking notification indicating that a pair of Pixel Buds Pro 2 has been detected. A map displays the locations where the earbuds were detected near the device.](/_app/immutable/assets/findhub-victim.BOUzwvZL.png)

Figure 2: Unwanted tracking notification showing the victim's own device.

This attack exploits the fact that non-Android devices do not perform the Fast Pair procedure
when they connect to an accessory. Android devices write an Account Key to the accessory after the pairing has completed. This
key is used to establish ownership of the device, as the first key written to a device is
marked as the Owner Account Key. Therefore, if the victim has
never connected their accessory to an Android device, the attacker will be marked as the owner
after writing their account key.

## Impact

WhisperPair is not an isolated issue. Our study shows that multiple devices, vendors, and
chipsets are affected. These vulnerable devices passed both the manufacturers' quality
assurance tests and Google's certification process, demonstrating a systemic failure rather
than an individual developer error. While there is a certification process that devices must
undergo before the Fast Pair functionality is activated, insecure implementations still
reached the market at scale. This shows a chain of compliance failures in Google Fast Pair, as
the vulnerability failed to be detected on all three levels: implementation, validation, and
certification.

The consequences of WhisperPair are severe, allowing an attacker to pair with a vulnerable
device in seconds. The attack can be performed using commodity hardware and does not require
user interaction. In some scenarios, an attacker may also be able to add the accessory to the
Find Hub Network using a malicious account.

### Responsible disclosure & mitigation

We reported our findings to Google in August 2025, who classified the issue as critical [(CVE-2025-36911)](https://www.cve.org/CVERecord?id=CVE-2025-36911). We agreed on a 150-day disclosure window, during which Google could work with their
ecosystem partners to release security patches. Google awarded us the maximum possible bounty
of $15,000 for this issue. We would like to thank the Android Security Team for their
responsiveness and collaboration throughout the disclosure process.

The only way to fix this vulnerability is by installing a software update issued by the
manufacturer of the accessory. Although many manufacturers have released patches for their
impacted devices, software updates may not yet be available for every vulnerable device. We
encourage researchers and users to verify patch availability directly with the manufacturer.

## Questions and Answers

Who conducted this research?

This research was conducted by researchers at the [COSIC](https://www.esat.kuleuven.be/cosic) group of KU Leuven.

COSIC:

* [Sayon Duttagupta](https://www.esat.kuleuven.be/cosic/people/person/?u=u0129899)\* [(Contact)](https://www.kuleuven.be/wieiswie/en/person/00129899)
* [Nikola Antonijević](https://www.esat.kuleuven.be/cosic/people/person/?u=u0148369) [(Contact)](https://www.kuleuven.be/wieiswie/en/person/00148369)
* [Bart Preneel](https://homes.esat.kuleuven.be/~preneel/%20) [(Contact)](https://www.kuleuven.be/wieiswie/en/person/00003308)

DistriNet - Group T (work performed while at COSIC):

* [Seppe Wyns](https://seppe.io)\* [(Contact)](https://www.kuleuven.be/wieiswie/en/person/00179829)
* [Dave Singelée](https://sites.google.com/site/davesingelee) [(Contact)](https://www.kuleuven.be/wieiswie/en/person/00041052)

\* Primary authors

Is my device vulnerable?

If you have a Bluetooth accessory that supports Google Fast Pair (like wireless earbuds,
headphones, or speakers), you might be affected. You can [look up your device](/vulnerable-devices) to check whether it is vulnerable.

Regardless of whether your device is vulnerable, we recommend keeping your device up to
date.

How can I protect myself against this attack?

Because Google Fast Pair cannot be disabled, the only way to prevent WhisperPair attacks
is by performing a software update.

Please consult your accessory's manual for instructions on how to install a software
update.

Can a vulnerability like WhisperPair be prevented ...