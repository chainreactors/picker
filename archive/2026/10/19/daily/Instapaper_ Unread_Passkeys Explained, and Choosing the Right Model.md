---
title: Passkeys Explained, and Choosing the Right Model
url: https://www.darkoperator.com/blog/2026/10/18/passkeys-explained-and-choosing-the-right-model
source: Instapaper: Unread
date: 2026-10-19
fetch_date: 2026-10-20T06:53:46.899857
---

# Passkeys Explained, and Choosing the Right Model

# [Shell is Only the Beginning](/ "Shell is Only the Beginning")

When getting shell is only the start of the journey.

* [Blog](/)
* [Infosec Tactico Podcast](/infosec-tactico-podcast)
* [Search](/searchpage)
* Blog Series

  + [PowerShell Basics](/powershellbasics)
* MSF Installation Guides

  + [Installing Metasploit in Ubuntu and Debian](/installing-metasploit-in-ubunt)
  + [Installing Metasploit Framework in OS X](/installing-metasploit-framewor)
* [Projects](https://github.com/darkoperator)
* [About Me](/about-me)

Navigation
Blog
Infosec Tactico Podcast
Search
Blog Series
PowerShell Basics
MSF Installation Guides
Installing Metasploit in Ubuntu and Debian
Installing Metasploit Framework in OS X
Projects
About Me

# [Passkeys Explained, and Choosing the Right Model](/blog/2026/10/18/passkeys-explained-and-choosing-the-right-model)

[October 19, 2026](/blog/2026/10/18/passkeys-explained-and-choosing-the-right-model)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)
in [Blue Team](/blog/category/Blue%2BTeam), [PowerShell](/blog/category/PowerShell)

### How WebAuthn defeats phishing, and how to match device-bound and synced passkeys to your workforce with passkey profiles

*MFA to Passkeys in Microsoft Entra ID series · Part 2 of 7*

In part 1 went over how an adversary-in-the-middle proxy relays a traditional MFA challenge and walks away with the session, something I have to admit I see often, almot always in the BEC (Bussiness Email Compromise) I see. This part answers the next two questions: **what makes a passkey different**, and **which kind of passkey should each of your users have?**

The second question used to be simple: buy security keys like the ones provided by Yubikey. In 2026 the answer is richer, and more nuanced. Entra ID now supports:

* **device-bound passkeys:** FIDO2 security keys, Microsoft Authenticator, Microsoft Entra passkeys on Windows, and Windows Hello for Business;
* **synced passkeys:** Apple Passwords/iCloud Keychain, Google Password Manager, and third-party managers such as 1Password and Bitwarden;
* **passkey profiles**, which let you allow different kinds of passkeys for different groups.

If you choose right model and you can move most of the workforce to phishing-resistant sign-in with no hardware budget, while holding administrators to a much higher standard.

## A passkey is a key pair, not a secret

Lets go over one of th biggest missunderstandings I see. A passkey is a FIDO2/WebAuthn credential. At **registration**:

1. Entra ID (the *relying party*) sends a challenge and its identifier (`login.microsoft.com`).
2. The authenticator generates a **new key pair unique to that relying party and that account**.
3. The **public key** goes to Entra ID. The **private key** stays with the authenticator (device-bound) or in the user's end-to-end encrypted passkey provider (synced).

At **sign-in**:

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/1b7ae89e-6663-43a8-84c7-d2a3dd24d6d6/Passkey+Registration.png)

Three properties stand out in this design:

* **Origin binding (step 2).** The *browser* supplies the origin, not the user. If the page is `login-micros0ft.example`, the authenticator never finds a credential for it. There is nothing for a proxy to relay.
* **No shared secret.** Entra ID stores only a public key. A database breach yields nothing reusable.
* **Two factors in one gesture.** Possession of the authenticator plus local user verification (PIN or biometric) satisfies MFA. The biometric never leaves the device.

> **What passkeys don't solve:** device code phishing (the user is on the real site), stolen session cookies after sign-in, and a help desk that registers an attacker's passkey on request. Parts 3–5 handle those cases.

## The passkey landscape in Entra ID

| Credential | Type | Where the private key lives | Attestation possible | Typical fit |
| --- | --- | --- | --- | --- |
| FIDO2 security key (USB/NFC) | Device-bound | Secure element on the key | Yes | Admins, shared/kiosk devices, no-phone users |
| Passkey in **Microsoft Authenticator** (iOS 17+ / Android 14+) | Device-bound | Phone's secure hardware, inside Authenticator | Yes (App Attest / Play Integrity) | Mobile-first workforce, cross-device sign-in |
| **Microsoft Entra passkey on Windows** | Device-bound | Windows Hello container on that PC | No (profile can't enforce attestation) | Unmanaged or personal Windows PCs, multiple Entra accounts per PC |
| **Windows Hello for Business** | Device-bound | TPM on an Entra/hybrid-joined PC | n/a (managed by Intune/GPO) | Corporate Windows devices, including device sign-in |
| **Platform SSO** (macOS) | Device-bound | Secure Enclave | n/a | Corporate Macs |
| **Synced passkey** (iCloud Keychain, Google Password Manager, 1Password, Bitwarden…) | Synced | User's passkey provider, end-to-end encrypted, on all their devices | No, never | General workforce |

Microsoft's own numbers for synced passkeys are compelling. From [Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-synced-passkeys): **99%** of users successfully register them, sign-in is **14× faster** than password + traditional MFA (3 seconds instead of 69), and sign-in success is **95% vs. 30%**.

### Device-bound vs. synced: the real trade-off

| Question | Device-bound | Synced |
| --- | --- | --- |
| Can the organization verify the make/model? | Yes, with attestation enforced | **No.** Synced passkeys don't support attestation |
| What happens when a device is lost? | Need a second credential or a recovery process (Part 4) | Provider restores the passkey to a new device |
| Who controls recovery? | You (help desk + TAP) | The provider account (Apple ID, Google account…) and its recovery |
| Deployment cost | Hardware and logistics (security keys) or app rollout (Authenticator) | Nearly zero |
| Phishing-resistant? | Yes | Yes |

The key sentence from Microsoft's FIDO2 guidance: *"Treat synced passkeys as phishing-resistant credentials but with the same security posture as other unattested authenticators."* Synced passkeys fully defeat AiTM phishing. What you give up is **provenance**: you can't prove the private key isn't also sitting in a personal account on a family iPad.

### Attestation and AAGUIDs: know what you are really enforcing

Every authenticator model has an **AAGUID**, a 128-bit make-and-model identifier. Passkey profiles and authentication strengths can allow or block AAGUIDs. Read this carefully, though:

> *"If enforce attestation is set to No, Microsoft Entra ID can't guarantee any attribute about a passkey, including if it's synced or device-bound."* ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2))

Without attestation, the AAGUID is a claim the authenticator makes about itself. Microsoft calls AAGUID lists a "policy guide rather than a strict security control" in that case. Two more caveats:

* Attestation is checked **at registration only**. Turning it on later doesn't evict passkeys registered without it.
* Removing an AAGUID from an allow list **does** stop existing passkeys of that model from signing in. Useful, but easy to trigger by accident.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/a3385d76-8052-424e-ba7d-ce6b6c15961f/how-to-enable-passkey-fido2_security-key-aaguid-details.png)

Screenshot: Microsoft Learn. A user's passkey details in the admin center include the AAGUID.

Useful AAGUIDs published by Microsoft:

| Authenticator | AAGUID |
| --- | --- |
| Microsoft Authenticator (Android) | `de1e552d-db1d-4423-a619-566b625cdc84` |
| Microsoft Authenticator (iOS) | `90a3ccdf-635c-4729-a248-9b709135078f` |
| Windows Hello (hardware) | `08987058-cadc-4b81-b6e1-30de50dcbe96` |
| Windows Hello (VBS hardware) | `9ddd1817-af5a-4672-a2b9-3e3dd95000a9` |
| Windows Hello (software) | `6028b017-b1d4-4c02-b4b3-afcdafc96bb2` |

Security-key vendors...