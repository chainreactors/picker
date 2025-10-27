---
title: How could someone steal your keychain’s secrets
url: https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/
source: Instapaper: Unread
date: 2023-08-26
fetch_date: 2025-10-04T12:02:18.250184
---

# How could someone steal your keychain’s secrets

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [M-series Macs](https://eclecticlight.co/m1-macs/)
* [Mac Problems](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Mac articles](https://eclecticlight.co/mac-problem-solving/)
* [Macs](https://eclecticlight.co/category/macs/)
* [Art](https://eclecticlight.co/painting-topics/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[August 25, 2023](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# How could someone steal your keychain’s secrets?

Putting all your Mac’s secrets in just a couple of places makes those prime targets for attack. Given that your Mac’s keychains can’t be locked away in hidden vaults, otherwise they couldn’t do their job, how might someone steal your secrets from within them?

Recall that your Mac has [two different types](https://eclecticlight.co/2023/08/07/an-introduction-to-keychains-and-how-theyve-changed/) of keychain:

* file-based keychains, including most significantly your login keychain, which aren’t shared,
* one Data Protection keychain, normally that shared in iCloud, or stored on your Mac as Local Items when it’s not shared.

Both types are stored locally in your Mac’s several Library/Keychains folders, and the local copy of the Data Protection keychain is synced via iCloud when that feature is enabled. Although /Library/Keychains will contain some attractive secrets, main targets are the login and Data Protection keychains held in ~/Library/Keychains.

#### How to tell whether a password is stored in the right keychain

Given the better protection provided by the Data Protection keychain, it’s good to have confidence that the apps you use that keep secrets do so using that, rather than a file-based keychain. Background processes and helpers that are run by `launchd` can only use file-based keychains, but an app with a GUI should be free to use either.

The simplest test is to enter a new secret into the app, see whether that appears in the list in Password settings, and syncs to other Macs and devices sharing the same keychain in iCloud. As not all secrets are visibly shared, if you can’t see the synced password, watch the Modified timestamp on the keychain-2.db file in the ~/Library/Keychains/UUID folder, where the UUID is that Mac’s Hardware UUID shown in System Information. If the password is saved instead to the login keychain, then the Modified timestamp on ~/Library/Keychains/login.keychain-db should update instead.

#### Searching unencrypted keychains

The simplest way for an attacker to try to obtain data from a keychain is to look through for contents stored without being encrypted. As file-based keychains remain in their traditional format, some of the metadata, but none of the secrets, may appear in plain text. In the past, before the use of Data Protection keychains to store website and other passwords, these could have been useful to an attacker, but are of limited value now. In contrast, Data Protection keychains appear to encrypt their entire contents, making this approach worthless with them.

#### Stealing the keychain password

By far the easiest way for an attacker to obtain your login keychain password is to ask you for it, by displaying a fake dialog prompting you to enter it. Without checking such dialogs carefully before giving them a password, many users fall for this simple trick. If you’re in any doubt, don’t enter anything into the dialog and click on the **Deny** button every time.

This trick is most effective in attacks against the login keychain, which lacks the more advanced protections of the Data Protection keychain. Those limit access to secrets according to app entitlements, for example, making it impossible for an app without a specific entitlement to gain access to many of its secrets. Other secrets may not even be stored in the Data Protection keychain, but kept in the [Secure Enclave](https://eclecticlight.co/2023/08/21/how-the-secure-enclave-protects-your-mac/).

#### Stealing the keychain

If an attacker can’t trick you into giving away the password to a keychain, then they could try to brute-force the password instead. That requires ‘exfiltrating’ (copying) the keychain from your Mac to a remote system where they can run software to guess the password. While your Mac’s Secure Enclave can impose limits on the number of times passwords can be tried, there’s no way to impose such limits on the keychain when it’s on another system, so their software will run many millions of attempts to guess the right password if necessary.

The same approach can be used if an attacker gains physical access to a device sharing the same passwords, in which case they’ll prefer to try this from the least-protected device, such as an old Mac or device that’s sharing the same iCloud keychain.

Forcing a password takes computer power, suitable software, and time. One popular means of accelerating the process is to run as much as possible on a GPU, but that’s only effective for certain types of password. Forcing is normally only feasible when individuals are being targeted, rather than as part of a general campaign of attacks. Different types of password and vault/keychain require different approaches, and some can be faster to force than others. Among the most difficult to force at present are those used by LastPass, while macOS file-based keychains are among the quicker to force. But, given the right tool and sufficient time, all vaults/keychains can be broken into.

#### To protect your keychain:

* Never give your password to anything that might not be completely legitimate. Know [how to tell](https://eclecticlight.co/2023/08/09/when-should-you-provide-a-keychain-or-admin-password/) genuine password requests from forgeries.
* Ensure your Mac is well-protected against malware, and never takes chances that might download it onto your Mac.
* Use the macOS password manager, or a reputable third-party equivalent.
* If you’re at additional risk of attack, consider using a software firewall to monitor attempts at exfiltration.
* Wherever possible, use apps that save their secrets to the Data Protection keychain.
* Consider removing old devices from iCloud keychain, as they could prove its most vulnerable point.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2023/08/25/how-could-someone-steal-your-keychains-secrets/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://ecle...