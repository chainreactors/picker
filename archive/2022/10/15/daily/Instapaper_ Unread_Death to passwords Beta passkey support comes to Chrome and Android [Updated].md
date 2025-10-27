---
title: Death to passwords Beta passkey support comes to Chrome and Android [Updated]
url: https://arstechnica.com/gadgets/2022/10/google-rolls-out-beta-passkey-support-for-chrome-and-android/
source: Instapaper: Unread
date: 2022-10-15
fetch_date: 2025-10-03T20:00:31.496425
---

# Death to passwords Beta passkey support comes to Chrome and Android [Updated]

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

You can't make me use a QR code

# Death to passwords: Beta passkey support comes to Chrome and Android [Updated]

Big Tech's cross-platform password replacement arrives in the Google ecosystem.

[Ron Amadeo](https://arstechnica.com/author/ronamadeo/)
–

Oct 12, 2022 1:38 pm
| [186](https://arstechnica.com/gadgets/2022/10/google-rolls-out-beta-passkey-support-for-chrome-and-android/#comments "186 comments")

[![](https://cdn.arstechnica.net/wp-content/uploads/2021/01/passwords.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2021/01/passwords.jpg)

Please don't do this.
Credit:
Getty Images

Please don't do this.
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

Big Tech wants to kill the password, with "passkeys" being the hot, new password replacement standard on the block. Passkeys are [backed by](https://arstechnica.com/gadgets/2022/05/apple-google-and-microsoft-want-bluetooth-proximity-to-replace-the-password/) Google, Apple, Microsoft, and the FIDO Alliance, so expect to see them everywhere soon. iOS [picked up](https://arstechnica.com/gadgets/2022/09/ios-16-review-customization-unlocked/4/) the standard in version 16, and now Google is [launching passkey betas](https://android-developers.googleblog.com/2022/10/bringing-passkeys-to-android-and-chrome.html) on Chrome and Android.

The passkey argument is that passwords are old and insecure. Computer passwords were originally conceived as an easy-to-remember secret for humans to type into a text box. As the need for greater security arose, password managers arrived, making it easy to save and recall your passwords. Now, instead of some human-memorable phrase, the ideal way to use a password is to have a computer generate some wild string of characters and never reuse that password anywhere else. The password manager revolution is all a hack, though, built on top of that original text box. We don't really need the text box anymore, and that's where the passkeys come in.

Passkeys just trade [WebAuthn](https://webauthn.guide/) cryptographic keys with the website directly. There's no need for a human to tell a password manager to generate, store, and recall a secret—that will all happen automatically, with way better secrets than what the old text box supported, and with uniqueness enforced. The downside is that, while every browser in the world supports showing that old text box, passkey support will need to be added to every web browser, every password manager, and every website. It's going to be a long journey.

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/10/34.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2022/10/34-1440x1022.jpg)

The passkey process works a lot like autofill.

Credit:
Ron Amadeo

The passkey process works a lot like autofill.
Credit:
Ron Amadeo

The one weird choice Big Tech made with passkeys is that the thing that authenticates your access to a website is *your phone*, not the password manager on whatever device you are currently using. This communication between phone and client also isn't done over the Internet like two-factor authentication—the device you are using needs to have Bluetooth so your phone can talk to it locally. Bluetooth is used to make sure your phone is in proximity to the device and to start a (more secure than Bluetooth) network session. Keeping the communication local ensures that random people on the Internet can't log in to your accounts, but it's also going to lock out some desktop computers.

Google says its passkey efforts have reached "a major milestone" today. If you sign up for the Play Services beta, you can now create and use passkeys on Android devices, and Chrome Canary now supports passkeys for websites. Google says stable implementations for Chrome and Android will be out later this year, but it wants developers to start developing right now.

Google also shared a few details of how this is going to work. Google's solution has your passkeys stored in the Google Password Manager. A pop-up on your phone will first have you pick an account, then authenticate with some kind of biometric, like fingerprint unlock. The phone will communicate with the client over Bluetooth, the browser unlocks your passkey and then sends that to the website. (If the client is your phone, then this all gets a lot simpler.)

![](https://cdn.arstechnica.net/wp-content/uploads/2022/10/image2.png)

You start off with a QR Code? This must just be a hack for the beta.
Credit:
Google

For some reason, Google's example involves kicking off the whole process with a QR Code. I assume this is just a quick hack for the beta, but to get the passkey pop-up to first appear on your phone, Google has the computer show a QR code, and then the phone scans it. Just like for the Google Prompt or other forms of 2FA, in the future, the initial passkey pop-up will hopefully open automatically via the Internet.

Besides stable releases for Android and Chrome, next up for Google is an API for native Android apps and an Android API for third-party password managers to plug into this. Google's getting its house in order right now, but in the future this should work across ecosystems, so an iPhone could send a passkey to Chrome, or an Android phone could send a passkey to Safari.

#### Update: A correction and more details

We made a few tweaks to this after talking to a Microsoft rep. One big correction is that passkeys are stored on your client device, not transferred from your phone. Your phone is used to authenticate your access to that passkey, though. There's concern in the comments about Bluetooth security, but Bluetooth communication is for proximity. Passkeys don't rely on Bluetooth security to be secure. Like 2FA, it's expected that authenticating with your phone won't need to happen for every single login.

Related Stories

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/05/User-Experiences-with-Multi-device-FIDO-Credentials-150x150.jpg)](https://arstechnica.com/gadgets/2022/05/apple-google-and-microsoft-want-bluetooth-proximity-to-replace-the-password/)

[Apple, Google, and Microsoft want to kill the password with “Passkey” standard](https://arstechnica.com/gadgets/2022/05/apple-google-and-microsoft-want-bluetooth-proximity-to-replace-the-password/)

Instead of a password, devices could look for your phone over B...