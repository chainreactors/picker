---
title: A Day in the Life of a Prolific Voice Phishing Crew
url: https://krebsonsecurity.com/2025/01/a-day-in-the-life-of-a-prolific-voice-phishing-crew/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-09
fetch_date: 2025-10-06T20:13:14.148794
---

# A Day in the Life of a Prolific Voice Phishing Crew

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# A Day in the Life of a Prolific Voice Phishing Crew

January 7, 2025

[39 Comments](https://krebsonsecurity.com/2025/01/a-day-in-the-life-of-a-prolific-voice-phishing-crew/#comments)

Besieged by scammers seeking to phish user accounts over the telephone, **Apple** and **Google** frequently caution that they will never reach out unbidden to users this way. However, new details about the internal operations of a prolific voice phishing gang show the group routinely abuses legitimate services at Apple and Google to force a variety of outbound communications to their users, including emails, automated phone calls and system-level messages sent to all signed-in devices.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/thumb-mobile.png)

KrebsOnSecurity recently told the saga of a cryptocurrency investor named **Tony** who was robbed of more than $4.7 million in [an elaborate voice phishing attack](https://krebsonsecurity.com/2024/12/how-to-lose-a-fortune-with-just-one-bad-click/). In Tony’s ordeal, the crooks appear to have initially contacted him via **Google Assistant**, an AI-based service that can engage in two-way conversations. The phishers also abused legitimate Google services to send Tony an email from google.com, and to send a Google account recovery prompt to all of his signed-in devices.

Today’s story pivots off of Tony’s heist and new details shared by a scammer to explain how these voice phishing groups are abusing a legitimate Apple telephone support line to generate “account confirmation” message prompts from Apple to their customers.

Before we get to the Apple scam in detail, we need to revisit Tony’s case. The phishing domain used to steal roughly $4.7 million in cryptocurrencies from Tony was **verify-trezor[.]io**. This domain was featured in [a writeup from February 2024](https://www.lookout.com/threat-intelligence/article/cryptochameleon-fcc-phishing-kit) by the security firm **Lookout**, which found it was one of dozens being used by a prolific and audacious voice phishing group it dubbed “**Crypto Chameleon**.”

Crypto Chameleon was brazenly trying to voice phish employees at the **U.S. Federal Communications Commission** (FCC), as well as those working at the cryptocurrency exchanges **Coinbase** and **Binance**. Lookout researchers discovered multiple voice phishing groups were using a new phishing kit that closely mimicked the single sign-on pages for **Okta** and other authentication providers.

As we’ll see in a moment, that phishing kit is operated and rented out by a cybercriminal known as “**Perm**” a.k.a. “**Annie**.” Perm is the current administrator of **Star Fraud**, one of the more consequential cybercrime communities on Telegram and one that has emerged as a foundry of innovation in voice phishing attacks.

A review of the many messages that Perm posted to Star Fraud and other Telegram channels showed they worked closely with another cybercriminal who went by the handles “**Aristotle**” and just “**Stotle**.”

It is not clear what caused the rift, but at some point last year Stotle decided to turn on his erstwhile business partner Perm, sharing extremely detailed videos, tutorials and secrets that shed new light on how these phishing panels operate.

Stotle explained that the division of spoils from each robbery is decided in advance by all participants. Some co-conspirators will be paid a set fee for each call, while others are promised a percentage of any overall amount stolen. The person in charge of managing or renting out the phishing panel to others will generally take a percentage of each theft, which in Perm’s case is 10 percent.

When the phishing group settles on a target of interest, the scammers will create and join a new **Discord** channel. This allows each logged on member to share what is currently on their screen, and these screens are tiled in a series of boxes so that everyone can see all other call participant screens at once.

Each participant in the call has a specific role, including:

-The Caller: The person speaking and trying to social engineer the target.
-The Operator: The individual managing the phishing panel, silently moving the victim from page to page.
-The Drainer: The person who logs into compromised accounts to drain the victim’s funds.
-The Owner: The phishing panel owner, who will frequently listen in on and participate in scam calls.

## ‘OKAY, SO THIS REALLY IS APPLE’

In one video of a live voice phishing attack shared by Stotle, scammers using Perm’s panel targeted a musician in California. Throughout the video, we can see Perm monitoring the conversation and operating the phishing panel in the upper right corner of the screen.

﻿

In the first step of the attack, they [peppered the target’s Apple device with notifications from Apple](https://krebsonsecurity.com/2024/03/recent-mfa-bombing-attacks-targeting-apple-users/) by attempting to reset his password. Then a “**Michael Keen**” called him, spoofing Apple’s phone number and saying they were with Apple’s account recovery team.

The target told Michael that someone was trying to change his password, which Michael calmly explained they would investigate. Michael said he was going to send a prompt to the man’s device, and proceeded to place a call to an automated line that answered as Apple support saying, “I’d like to send a consent notification to your Apple devices. Do I have permission to do that?”

In this segment of the video, we can see the operator of the panel is calling the real Apple customer support phone number **800-275-2273**, but they are doing so by spoofing the target’s phone number (the victim’s number is redacted in the video above). That’s because calling this support number from a phone number tied to an Apple account and selecting “1” for “yes” will then send an alert from Apple that displays the following message on all associated devices:

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/appleconfirmation.png)

Calling the Apple support number 800-275-2273 from a phone number tied to an Apple account will cause a prompt similar to this one to appear on all connected Apple devices.

KrebsOnSecurity asked two different security firms to test this using the caller ID spoofing service shown in Perm’s video, and sure enough calling that 800 number for Apple by spoofing my phone number as the source caused the Apple Account Confirmation to pop up on all of my signed-in Apple devices.

In essence, the voice phishers are using an automated Apple phone support line to send notifications from Apple and to trick people into thinking they’re really talking with Apple. The phishing panel video leaked by Stotle shows this technique fooled the target, who felt completely at ease that he was talking to Apple after receiving the support prompt on his iPhone.

“Okay, so this really is Apple,” the man said after receiving the alert from Apple. “Yeah, that’s definitely not me trying to reset my password.”

“Not a problem, we can go ahead and take care of this today,” Michael replied. “I’ll go ahead and prompt your device with the steps to close out this ticket. Before I do that, I do highly suggest that you change your password in the settings app of your device.”

The target said they weren’t sure exactly how to d...