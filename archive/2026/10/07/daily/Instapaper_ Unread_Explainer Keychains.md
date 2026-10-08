---
title: Explainer Keychains
url: https://eclecticlight.co/2026/10/07/explainer-keychains/
source: Instapaper: Unread
date: 2026-10-07
fetch_date: 2026-10-08T08:08:22.731005
---

# Explainer Keychains

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [All Macs](https://eclecticlight.co/mac-problem-solving-2-2/)
* [M1-M5 Macs](https://eclecticlight.co/m1-macs-2/)
* [Troubleshooting](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Painting](https://eclecticlight.co/painting-topics-2-2/)
* [Mac Front Page](https://eclecticlight.co/category/macs/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[October 7, 2026](https://eclecticlight.co/2026/10/07/explainer-keychains/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Explainer:** Keychains

Keychains are specialised database files used by every Mac since the introduction of Mac OS X to store and protect passwords, security certificates and other secrets. Even if you use a third-party password manager, your Mac still has at least two personal keychains for use by apps, and two more for the system. As a result of their history, keychains come in two types, and earlier this year Apple added a new variant.

#### File-based keychains

Those ultimately derived from ancestors in Classic Mac OS are file-based keychains including the login keychain, whose password is that user’s login password to enable it to be unlocked following login. Until those were changed to a new variant in macOS 26.4, like all file-based keychains they were self-contained and fully mobile between systems and Macs. Since Mac OS X 10.2 Jaguar in 2002, these have been accessed using the SecKeychain API (and more recently the SecItem API as well), and maintained using the Keychain Access app, now hidden away in /System/Library/CoreServices/Applications.

In addition to login keychains, all Macs contain at least two other essential file-based keychains:

* in /System/Library/Keychains, in the SSV, are SystemRootCertificates.keychain and others providing the set of root security certificates specific to that version of macOS;
* in /Library/Keychains are System.keychain and others providing certificates and passwords required for all users, including those to gain access to that Mac’s Wi-Fi connections.

##### login keychain

The login keychain located in ~/Library/Keychains/login.keychain-db is each user’s default personal file-based SecKeychain. It’s here that each user can still store passwords, certificates, secure notes, etc. for general use on that Mac, but not passkeys.

Although kept unlocked, readable and writeable while the user is logged in, that doesn’t guarantee access to its contents. If an app makes a call to the macOS security system to retrieve a stored secret for its use, that determines whether the app is trusted to access that information, and whether that keychain is locked. Assuming the secret is stored there, the app is trusted, and the keychain is unlocked, then the secret is retrieved and passed back to the app. If the app isn’t trusted or the keychain is locked, then the security system, not the app, displays a distinctive standard dialog asking for the password to that keychain to authenticate before it will provide the secret to the app.

Access to secrets is determined by the security system, the specific access it grants to an app, and to individual items in that user’s keychain. At its most restrictive, the system can limit all other apps from accessing a particular secret in the keychain, but specific secrets can also be shared across several different apps.

##### Custom keychains

Users and apps can create multiple custom file-based keychains. Although those could be stored almost anywhere, most are conventionally kept in the ~/Library/Keychains folder. These aren’t unlocked automatically after login, and you may be prompted by a dialog to open them when access is required. Those created for third-party apps can of course have their passwords set by the app that uses them, and they may be opened for their app to access their contents. Currently, together with login keychains from macOS prior to 26.4, these are the least-protected, and commercial apps can often break into them in a matter of seconds.

##### Entropy-secured login keychains

Starting with macOS 26.4, login keychains have been made more secure by the addition of an entropy file as a requirement for their encryption and decryption. Entropy files are stored in the SIP-protected and locked folder at /var/db/SystemKeys, and can be identified for keychains that can be unlocked, using the command
`security show-keychain-info -s path`
where `path` is the full path to the keychain, typically ~/Library/Keychains/login.keychain-db for a login keychain. That returns the name of the entropy file as `salt`, which can then be used to identify and copy it when required. Further details [are here](https://eclecticlight.co/2026/10/02/how-to-copy-login-keychains-that-can-be-unlocked/).

Thus, a login keychain copied to another boot Data volume or another Mac can’t be unlocked unless the entropy file has also been transferred. Entropy files are backed up by all good backup utilities, and can be restored using Migration Assistant.

#### Data Protection keychain

Since OS X 10.9 Mavericks, Macs have also had one and only one Data Protection keychain for each user, accessed using the SecItem API. Its origins go back to the introduction of iOS, which has never used file-based keychains. If you share your keychain in iCloud, this is the local copy of that shared keychain and is known as *iCloud Keychain;* if you don’t share it in iCloud, then it’s known as *Local Items* instead. The local copy of this is normally stored in ~/Library/Keychains/[UUID]/keychain-2.db, where the UUID is that assigned to that Mac.

This Data Protection keychain stores most standard types of secret, including internet and other passwords, certificates, keys and passkeys. Prior to macOS 11, it only synchronised internet passwords using iCloud, but from Big Sur onwards it synchronises all its contents, including passkeys, which have now become first class citizens. One limitation of the Data Protection keychain is that it can’t be targeted by code running outside a user context, such as a `launchd` daemon, which can only target file-based keychains such as the login keychain.

Unlike file-based keychains, secrets in the Data Protection keychain can be protected by the Secure Enclave in Macs equipped with T2 or Apple silicon chips, and can therefore be protected by biometrics including Touch ID, and Face ID in iOS and iPadOS. Hence they’re required for passkeys, which can’t be supported by traditional file-based keychains.

Although passwords stored in the Data Protection keychain can be listed in Keychain Access, the Passwords app is intended for use with it.

#### Utilities

Passwords, bundled in /Applications, for the Data Protection keychain
Keychain Access, bundled in /System/Library/CoreServices/Applications, for file-based keychains
Mints, free from [its Product Page](https://eclecticlight.co/mints-a-multifunction-utility/), lists details of open keychains from its Keychain button, in the Information section, although this relies on deprecated API calls which could be removed at short notice.

#### References

[Apple TN3137](https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains): On Mac keychain APIs and implementations
[Apple Keychain Services](https://developer.apple.com/documentation/security/keychain-services)

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/10/07/explainer-keychains/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/10/07/explainer-keychai...