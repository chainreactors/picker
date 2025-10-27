---
title: Passkeys—Microsoft, Apple, and Google’s password killer—are finally here
url: https://arstechnica.com/information-technology/2022/10/passkeys-microsoft-apple-and-googles-password-killer-are-finally-here/
source: Instapaper: Unread
date: 2022-10-27
fetch_date: 2025-10-03T21:03:46.522448
---

# Passkeys—Microsoft, Apple, and Google’s password killer—are finally here

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

WHAT TOOK YOU SO LONG?

# Passkeys—Microsoft, Apple, and Google’s password killer—are *finally* here

It only took 50 years, but there's finally a replacement that's safer and easier to use.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Oct 25, 2022 9:25 am
| [530](https://arstechnica.com/information-technology/2022/10/passkeys-microsoft-apple-and-googles-password-killer-are-finally-here/#comments "530 comments")

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/10/GettyImages-1295580690.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2022/10/GettyImages-1295580690.jpg)

Credit:
Gertty Images

Credit:
Gertty Images

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

For years, Big Tech has insisted that the death of the password is right around the corner. For years, those assurances have been little more than empty promises. The password alternatives—such as pushes, OAUTH single-sign ons, and trusted platform modules—introduced as many usability and security problems as they solved. But now, we’re finally on the cusp of a password alternative that’s actually going to work.

The new alternative is known as passkeys. Generically, passkeys refer to various schemes for storing authenticating information in hardware, a concept that has existed for more than a decade. What’s different now is that Microsoft, Apple, Google, and a consortium of other companies have unified around a single [passkey standard](https://fidoalliance.org/passkeys/) shepherded by the FIDO Alliance. Not only are passkeys easier for most people to use than passwords; they are also completely resistant to credential phishing, credential stuffing, and similar account takeover attacks.

On Monday, PayPal [said](https://newsroom.paypal-corp.com/2022-10-24-PayPal-Introduces-More-Secure-Payments-with-Passkeys) US-based users would soon have the option of logging in using FIDO-based passkeys, joining Kayak, eBay, Best Buy, CardPointers, and WordPress as online services that will offer the password alternative. In recent months, Microsoft, Apple, and Google have all updated their operating systems and apps to enable passkeys. Passkey support is still spotty. Passkeys stored on iOS or macOS will work on Windows, for instance, but the reverse isn’t yet available. In the coming months, all of that should be ironed out, though.

## What, exactly, *are* passkeys?

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/10/fido-illustration01.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2022/10/fido-illustration01.jpg)

Credit:
FIDO Alliance

Credit:
FIDO Alliance

Passkeys work almost identically to the FIDO authenticators that allow us to use our phones, laptops, computers, and Yubico or Feitian security keys for multi-factor authentication. Just like the FIDO authenticators stored on these MFA devices, passkeys are invisible and integrate with Face ID, Windows Hello, or other biometric readers offered by device makers. There’s no way to retrieve the cryptographic secrets stored in the authenticators short of physically dismantling the device or subjecting it to a jailbreak or rooting attack.

Even if an adversary was able to extract the cryptographic secret, they still would have to supply the fingerprint, facial scan, or—in the absence of biometric capabilities—the PIN that’s associated with the token. What’s more, hardware tokens use FIDO’s Cross-Device Authentication flow, or CTAP, which relies on Bluetooth Low Energy to verify the authenticating device is in close physical proximity to the device trying to log in.

Until now, FIDO-based security keys have been used mainly to provide MFA, short for multi-factor authentication, which requires someone to present a separate factor of authentication in addition to the correct password. The additional factors offered by FIDO typically come in the form of something the user has—a smartphone or computer containing the hardware token—and something the user is—a fingerprint, facial scan, or other biometric that never leaves the device.

So far, attacks against FIDO-compliant MFA have been in short supply. An advanced credential phishing campaign that recently breached Twilio and other top-tier security companies, for instance, failed against Cloudflare for one reason: Unlike the other targets, Cloudflare [used FIDO-compliant hardware tokens](https://arstechnica.com/information-technology/2022/08/phishers-breach-twilio-and-target-cloudflare-using-workers-home-numbers/) that were immune to the phishing technique the attackers used. The victims who were breached all relied on weaker forms of MFA.

But whereas hardware tokens can provide one or more factors of authentication in addition to a password, passkeys rely on no password at all. Instead, passkeys roll multiple authentication factors—typically the phone or laptop and the facial scan or fingerprint of the user—into a single package. Passkeys are managed by the device OS. At the user’s option, they can also be synced through end-to-end encryption with a user’s other devices using a cloud service provided by Apple, Microsoft, Google, or another provider.

Passkeys are “discoverable,” meaning an enrolled device can automatically push one through an encrypted tunnel to another enrolled device that’s trying to sign in to one of the user’s site accounts or apps. When signing in, the user authenticates themselves using the same biometric or on-device password or PIN for unlocking their device. This mechanism completely replaces the traditional username and password and provides a much easier user experience.

“Users no longer need to enroll each device for each service, which has long been the case for FIDO (and for any public key cryptography)," said Andrew Shikiar, FIDO's executive director and chief marketing officer. "By enabling the private key to be securely synced across an OS cloud, the user needs to only enroll once for a service, and then is essentially pre-enrolled for that service on all of their other devices. This brings better usability for the end-user and—very significantly—allows the service provider to start retiring passwords as a means of account recovery and re-enrollment.”

Ars Review Editor Ron Amadeo [summed things up well](https://arstechnica.com/gadgets/2022/10/google-rolls-out-beta-passkey-support-for-chrome-and-android/) last ...