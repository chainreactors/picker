---
title: Android Trojan that intercepts voice calls to banks just got more stealthy
url: https://arstechnica.com/information-technology/2024/10/android-trojan-that-intercepts-voice-calls-to-banks-just-got-more-stealthy/
source: Instapaper: Unread
date: 2024-11-01
fetch_date: 2025-10-06T19:22:01.553022
---

# Android Trojan that intercepts voice calls to banks just got more stealthy

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

HELLO, CUSTOMER SUPPORT?

# Android Trojan that intercepts voice calls to banks just got more stealthy

FakeCall malware can reroute calls intended for banks to attacker-controlled numbers.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Oct 30, 2024 3:59 pm
| [35](https://arstechnica.com/information-technology/2024/10/android-trojan-that-intercepts-voice-calls-to-banks-just-got-more-stealthy/#comments "35 comments")

[![Security concept: smartphone with text Virus](https://cdn.arstechnica.net/wp-content/uploads/2024/10/infected-phone-300x204.jpg)
![Security concept: smartphone with text Virus](https://cdn.arstechnica.net/wp-content/uploads/2024/10/infected-phone-1000x648.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2024/10/infected-phone.jpg)

Credit:
Getty Images

Credit:
Getty Images

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Researchers have found new versions of a sophisticated Android financial-fraud Trojan that’s notable for its ability to intercept calls a victim tries to place to customer-support personnel of their banks.

FakeCall first came to public attention in 2022, when researchers from security firm Kaspersky [reported](https://www.kaspersky.com/blog/fakecalls-banking-trojan/44072/) that the malicious app wasn’t your average banking Trojan. Besides containing the usual capabilities for stealing account credentials, FakeCall could reroute voice calls to numbers controlled by the attackers.

## A strategic evolution

The malware, available on websites masquerading as Google Play, could also simulate incoming calls from bank employees. The intention of the novel feature was to provide reassurances to victims that nothing was amiss and to more effectively trick them into divulging account credentials by having the social-engineering come from a live human.

The interception was possible when victims followed instructions during installation to grant permission for the app to become the default call handler on the Android device. From then on, FakeCall could detect calls to a bank’s legitimate customer-support number and reroute them to an attacker-controlled number. To better hide the sleight-of-hand, the Trojan can display its own screen over the system's.

[![](https://cdn.arstechnica.net/wp-content/uploads/2024/10/fakecalls-call-rerouting-overview.webp)](https://cdn.arstechnica.net/wp-content/uploads/2024/10/fakecalls-call-rerouting-overview.webp)

An overview of how FakeCall can intercept voice calls.

Credit:
Zimperium

An overview of how FakeCall can intercept voice calls.
Credit:
Zimperium

On Wednesday, a researcher at mobile security firm Zimperium [reported](https://www.zimperium.com/blog/mishing-in-motion-uncovering-the-evolving-functionality-of-fakecall-malware/) finding 13 new variants of the malware. The continued development of the already-sophisticated Trojan indicates the attackers behind it continue to ramp up investment in it.

“The newly discovered variants of this malware are heavily obfuscated but remain consistent with the characteristics of earlier versions,” Zimperium malware researcher Fernando Ortega [wrote](https://www.zimperium.com/blog/mishing-in-motion-uncovering-the-evolving-functionality-of-fakecall-malware/). Ortega continued: “This suggested a strategic evolution—some malicious functionality had been partially migrated to native code, making detection more challenging.”

Much of the new obfuscation is the result of hiding malicious code in a dynamically decrypted and loaded .dex file of the apps. As a result, Zimperium initially believed the malicious apps they were analyzing were part of a previously unknown malware family. Then the researchers dumped the .dex file from an infected device’s memory and performed static analysis on it.

“As we delved deeper, a pattern emerged,” Ortega wrote. “The services, receivers, and activities closely resembled those from an older malware variant with the package name com.secure.assistant.” That package allowed the researchers to link it to the FakeCall Trojan.

Many of the new features don’t appear to be fully implemented yet. Besides the obfuscation, other new capabilities include:

> ### Bluetooth Receiver
>
> This receiver functions primarily as a listener, monitoring Bluetooth status and changes. Notably, there is no immediate evidence of malicious behavior in the source code, raising questions about whether it serves as a placeholder for future functionality.
>
> ### Screen Receiver
>
> Similar to the Bluetooth receiver, this component only monitors the screen’s state (on/off) without revealing any malicious activity in the source code.
>
> ### Accessibility Service
>
> The malware incorporates a new service inherited from the Android Accessibility Service, granting it significant control over the user interface and the ability to capture information displayed on the screen. The decompiled code shows methods such as *onAccessibilityEvent() and onCreate()* implemented in native code, obscuring their specific malicious intent.
>
> While the provided code snippet focuses on the service’s lifecycle methods implemented in native code, earlier versions of the malware give us clues about possible functionality:
>
> * **Monitoring Dialer Activity**: The service appears to monitor events from the **com.skt.prod.dialer** package (the stock dialer app), potentially allowing it to detect when the user is attempting to make calls using apps other than the malware itself.
> * **Automatic Permission Granting**: The service seems capable of detecting permission prompts from the **com.google.android.permissioncontroller** (system permission manager) and **com.android.systemui** (system UI). Upon detecting specific events (e.g., **TYPE\_WINDOW\_STATE\_CHANGED**), it can automatically grant permissions for the malware, bypassing user consent.
> * **Remote Control**: The malware enables remote attackers to take full control of the victim’s device UI, allowing them to simulate user interactions, such as clicks, gestures, and navigation across apps. This capability enables the attacker to manipulate the device with precision.
>
> ### Phone Listener Service
>
> This service acts as a conduit between the malware and its **Command and Control (C2) server**, allowing the attacker to issue commands and execute actions on the infected device. Lik...