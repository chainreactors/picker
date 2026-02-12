---
title: Breaking Down ZeroDayRAT - New Spyware Targeting Android and iOS
url: https://iverify.io/blog/breaking-down-zerodayrat---new-spyware-targeting-android-and-ios
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:22:51.134259
---

# Breaking Down ZeroDayRAT - New Spyware Targeting Android and iOS

Products

Solutions

Partners

Resources

Company

[###### Request Demo](../contact)

Products

Solutions

Partners

Resources

Company

[###### Request Demo](../contact)

###### [The Attack Surface in Your Pocketâand How Scattered Spider Socially Engineers Their Way Inside](./the-attack-surface-in-your-pocket-and-how-scattered-spider-socially-engineers-their-way-inside)

###### The Attack Surface in Your Pocketâand How Scattered Spider Socially Engineers Their Way Inside

[Blog](../blog)

# Breaking Down ZeroDayRAT - New Spyware Targeting Android and iOS

By Daniel Kelley, Threat Researcher

Feb 10, 2026

![](https://framerusercontent.com/images/spbGHiv0gqdBjUiq7quU9n6UWE.jpg?width=1456&height=816)

![](https://framerusercontent.com/images/spbGHiv0gqdBjUiq7quU9n6UWE.jpg?width=1456&height=816)

We recently identified a new mobile spyware platform called ZeroDayRAT being sold openly via Telegram (with activity first observed February 2nd). The developer runs dedicated channels for sales, customer support, and regular updates, giving buyers a single point of access to a fully operational spyware panel.

From that panel, an operator gains full remote control over a userâs Android or iOS device, with support spanning Android 5 through 16 and iOS up to 26, including the iPhone 17 Pro. No technical expertise is required. The platform goes beyond typical data collection into real-time surveillance and direct financial theft.

![](https://framerusercontent.com/images/PCKvKC1wCo0b89ox0zJiO6vnr4.png)

*Image 1: ZeroDayRAT's dashboard with two devices, one in India and the US.*

To infect a device, an operator needs to get a malicious binary onto it, an APK for Android or a payload for iOS. The most common way that happens is smishing: the victim gets a text with a link, downloads what looks like a legitimate app, and installs it. Phishing emails, fake app stores, and links shared over WhatsApp or Telegram all work too.

### Device Overview and User Profiling

Once a device is infected, the overview tab is the first thing an operator sees. Device model, OS, battery, country, lock status, SIM and carrier info, dual SIM phone numbers, app usage broken down by time, a live activity timeline, and a preview of recent SMS messages are all displayed on a single screen.

![](https://framerusercontent.com/images/638oc8q6MmgdXZGNdMbeaBkO9Gk.png)

*Image 2: The overview tab for a compromised Android device.*

This screen is enough to profile the infected user: who they talk to, what apps they use most, when they're active, and what network they're on. Scrolling down reveals intercepted messages from banking services, carriers, and personal contacts. But the overview is just a starting point. The rest of the panel breaks the device open further.

![](https://framerusercontent.com/images/NrpSmwXNIssc1Q21rGSWaylpvg.png)

*Image 3: Intercepted SMS messages visible in the overview tab.*

### Location, Notifications, and Account Access

Beyond the overview, each data stream gets its own tab. GPS coordinates are pulled and plotted on an embedded Google Maps view with location history, so an operator can track not just where the infected user is now but where they've been.

![](https://framerusercontent.com/images/X3vQ7BteMSq5aUem0X5KTUvCHk.png)

*Image 4: Real-time GPS tracking of a compromised device in Bengaluru.*

Notifications are captured separately: app name, title, content, and timestamp. WhatsApp messages, Instagram notifications, missed calls, Telegram updates, YouTube alerts, system events. Without opening a single app, an attacker has passive visibility into nearly everything happening on the phone.

![](https://framerusercontent.com/images/tQHQJNQQ56ZUCm6Tiqd1EAE7CzE.png)

*Image 5: Real-time notification capture across all apps.*

One of the more problematic panels is the accounts tab. Every account registered on the device is enumerated: Google, WhatsApp, Instagram, Facebook, Telegram, Amazon, Flipkart, PhonePe, Paytm, Spotify, and more, each with its associated username or email. This is basically everything an attacker needs to attempt account takeover or launch targeted social engineering.

![](https://framerusercontent.com/images/Slxgspl86fsUlISHYLDk3NF6Ks.png)

*Image 6: Every account registered on the compromised device.*

SMS access rounds out the data collection: full inbox search, the ability to send messages from the phoneâs number, and visibility into incoming OTP codes from banks and platforms. SMS-based two-factor authentication is effectively bypassed.

### Live Surveillance and Keylogging

Everything above is passive data collection. The surveillance tab crosses into real-time physical access: live camera streaming (front or back), screen recording, and a microphone feed. Combined with GPS tracking, an operator can watch, listen to, and locate a target simultaneously.

![](https://framerusercontent.com/images/WEkz9GvsVzLcKtGmJVmFE76C50.png)

*Image 7: Live camera, screen recording, and microphone access from a single panel.*

Alongside the surveillance tools, a keylogger captures every input with app context and millisecond timestamps: biometric unlocks, gestures, keystrokes, app launches. A live screen preview runs on the right side of the panel, so the attacker sees what the target is doing and what they're typing at the same time.

![](https://framerusercontent.com/images/tePXVIyIwLFv5uzpy7V605X2U.png)

*Image 8: Keylogger output alongside a live screen preview.*

### Banking and Cryptocurrency Theft

With all of that access in place, the stealer tab moves into direct financial theft. The crypto stealer scans for wallet apps like MetaMask, Trust Wallet, Binance, and Coinbase, logging wallet IDs and balances. It also performs clipboard address injection, silently replacing copied wallet addresses with the attacker's so outgoing transfers get redirected.

![](https://framerusercontent.com/images/NeolDPBviWCBMWBh0nnHe1MZE.png)

*Image 9: The crypto stealer detecting wallets and injecting clipboard addresses.*

A separate bank stealer module targets online banking apps, UPI platforms like PhonePe and Google Pay, and services like Apple Pay and PayPal, capturing credentials via overlay attacks. Between the two modules, an operator can go after both traditional financial accounts and cryptocurrency from the same panel.

![](https://framerusercontent.com/images/E45Jgr20hOumuocWPg9ifEO6BQ.png)

*Image 10: Android and iOS devices reporting in from different countries.*

### A Problem That Isn't Going Away

Taken together, this is a complete mobile compromise toolkit, the kind that used to require nation-state investment or bespoke exploit development, now sold on Telegram. A single buyer gets full access to a targetâs location, messages, finances, camera, microphone, and keystrokes from a browser tab. Cross-platform support and active development make it a growing threat to both individuals and organizations.

For enterprises, a compromised employee device is a vector for credential theft, account takeover, and data exfiltration. For individuals, it means total loss of privacy and direct financial exposure. Mobile device security needs to be treated with the same urgency as endpoint and email security.

Detecting threats like ZeroDayRAT requires mobile EDR that goes beyond traditional device management. iVerify combines on-device threat detection, mobile forensics, and automated response to identify spyware, malware, and indicators of compromise across both BYOD and managed fleets. To learn more, visit [iverify.io](../).

### More Blogs

[![](https://framerusercontent.com/images/Vj0x3uOt8v2HfO6k1iAcNF3Ce4.png?width=1456&height=816)

![](https://framerusercontent.com/images/Vj0x3uOt8v2HfO6k1iAcNF3Ce4.png?width=1456&height=816)

Feb 4, 2026

#### How Attackers Run Smishing Campaigns (And Why They Work)](./how-attackers-run-smishing-campaigns-%28and-why-they-work%29)[![](https://framerusercontent.com/images/GUV0Q2t227Qof79m7Cw5UF9clc.png?width=384...