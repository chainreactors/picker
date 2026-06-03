---
title: Security of Third-Party Keyboard Apps on Mobile Devices
url: https://zeltser.com/third-party-keyboards-security
source: Lenny Zeltser
date: 2026-06-02
fetch_date: 2026-06-03T06:46:53.749726
---

# Security of Third-Party Keyboard Apps on Mobile Devices

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Security of Third-Party Keyboard Apps on Mobile Devices

Keyboard apps offer better predictions, voice transcription, and AI-powered writing, all requiring users to send what they type to remote servers. Mobile OS vendors set the rules but can't enforce what developers do with that data.

![Security of Third-Party Keyboard Apps on Mobile Devices - illustration](/assets/third-party-keyboards-security.DJzgcojl_1qec3b.webp)

A third-party keyboard app with network access effectively becomes a keylogger that the user has authorized. The safeguards depend almost entirely on what the developer chooses to do with the data once it leaves the mobile device.

iOS and Android have supported third-party keyboards for over a decade, and the underlying trust questions have only gotten harder as more keyboards send what you type to remote servers for AI-powered features. Let’s explore how access works on each platform, where data can leak, and the trade-off AI keyboards introduce.

## How Third-Party Keyboards Get Network Access

Keyboard apps can transmit keystrokes to developer servers for features such as next-word prediction, cross-device sync, and analytics of typing patterns. The very ability that draws users to these keyboards is the primary security concern.

Network access for a third-party keyboard on iOS requires two things:

* The developer must declare the [RequestsOpenAccess](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/requestsopenaccess) key in the keyboard extension. Apple describes that key as “a Boolean value indicating whether a custom keyboard uses a shared container and accesses the network.”
* The user must also toggle Allow Full Access on in Settings. An iOS warning spells out the consequences when the user toggles that setting on.

On iOS, some third-party keyboards can function without users granting them full access, though that mode usually disables the features that drew users to the app.

Android handles this differently. The access decision on Android requires two things:

* The developer adds [INTERNET permission](https://developer.android.com/develop/connectivity/network-ops/connecting) to the manifest. Android grants the declared permission automatically when the user installs the app, without prompting the user to approve network access.
* The user must also enable the keyboard in Settings and select it as the [active Input Method Editor](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method) (IME). This step triggers a [system warning](https://android.googlesource.com/platform/frameworks/base/%2B/refs/heads/master/packages/SettingsLib/res/values/strings.xml) telling the user that the IME “may be able to collect all the text you type, including personal data like passwords and credit card numbers.”

Once selected, the IME receives every character typed across every app. Android does not add a separate “full access” toggle afterward.

Credentials are the one exception to what the keyboard sees. A password manager fills the login field without sending data through the keyboard. Android does this through the [Autofill framework](https://developer.android.com/identity/autofill) and [Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). iOS does the same through [AutoFill](https://support.apple.com/guide/security/credential-provider-extensions-sec6319ac7b9/web).

## Guidelines for Keyboard Apps

Both platforms publish keyboard developer guidance:

* Apple’s [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/CustomKeyboard.html) is now archived, but it told developers, “Your first consideration when creating a custom keyboard must be how you will establish and maintain user trust.” Apple now points keyboard developers to the [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), which covers keyboard extensions and data use.
* Google’s [Privacy](https://developer.android.com/privacy-and-security/about) and [Security](https://developer.android.com/privacy-and-security/security-tips) checklists call for minimizing data collection, encrypting transit, and keeping personal data out of logs. The [Android IME developers](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method) page extends some of these expectations to keyboard apps.

Both platforms expose user-facing privacy declarations:

* On iOS, every keyboard’s App Store listing includes a [Privacy Nutrition Label](https://www.apple.com/privacy/labels/). The label categorizes what data the developer says they collect and whether it’s linked to the user. Developers must also ship a [Privacy Manifest](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) declaring tracking domains and use of [required-reason APIs](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).
* On Android, every keyboard on Google Play must complete a [Data Safety section](https://support.google.com/googleplay/android-developer/answer/10787469). The section shows users what data the app collects, shares, and whether it’s encrypted in transit.

Filing these declarations is mandatory, but the accuracy of the claims is the developer’s responsibility.

Customers have to decide whether to trust each keyboard developer based on what the developer publishes about its security practices and its track record. Apple’s app review process presumably catches blatant violations. However, once a keyboard transmits user data off the device, neither Apple nor Google can enforce developers’ server-side security practices.

## Potential for Data Leakage

Keystroke data can leak from a third-party keyboard in several ways. A malicious developer might build the app to exfiltrate what users type. Attackers might compromise an otherwise legitimate keyboard through a supply chain attack. And a developer might leak data through weak security engineering or poor vulnerability management, even without malicious intent.

The Citizen Lab’s report [The Not-So-Silent Type](https://citizenlab.ca/research/vulnerabilities-across-keyboard-apps-reveal-keystrokes-to-network-eavesdroppers/) examined cloud-based keyboard apps from nine vendors of Chinese-market Pinyin keyboards. The apps transmitted keystrokes with homegrown encryption that even passive eavesdroppers could exploit. The researchers reported that “eight of the nine apps identified contained vulnerabilities that could be exploited to completely reveal the contents of users’ keystrokes in transit.”

Data can leak from insecure storage as readily as from insecure transit. The [ai.type breach](https://haveibeenpwned.com/breach/AIType), cataloged by Have I Been Pwned, exposed the breadth of what one third-party keyboard collected and then left in an unsecured database:

* Names, email addresses, phone numbers, dates of birth, and genders
* IP addresses, geographic locations, and cellular network names
* Device information, IMEI numbers, and IMSI numbers
* Address book contacts and lists of apps installed on devices
* Social media profiles and profile photos

## The Rise of AI-Powered Keyboards

Keyboard apps increasingly rely on off-device processing to deliver AI features. Microsoft and Google have added cloud AI features to their long-standing keyboards, SwiftKey and Gboard. Other keyboards depend on cloud language models from the start. For these apps, sending the user’s data to the cloud is essential to deliver their AI features. For example:

* [Grammarly Keyboard](https://www.grammarly.com/keyboard): When [granted full access on iOS](https://support.grammarly.com/hc/en-us/articles/115000730091-Why-Grammarly-Need...