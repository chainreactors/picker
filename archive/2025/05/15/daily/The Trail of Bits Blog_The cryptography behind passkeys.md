---
title: The cryptography behind passkeys
url: https://blog.trailofbits.com/2025/05/14/the-cryptography-behind-passkeys/
source: The Trail of Bits Blog
date: 2025-05-15
fetch_date: 2025-10-06T22:26:52.698326
---

# The cryptography behind passkeys

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The cryptography behind passkeys

Joop van de Pol

May 14, 2025

[cryptography](/categories/cryptography/)

When most people think of cryptography, the first thing they typically think of is encryption: keeping information confidential. But just as important (if not more) is authenticity: ensuring that information is really coming from an authentic source. When you visit a website, the server typically proves its identity through a Transport Layer Security (TLS) certificate authenticated by the Web Public Key Infrastructure (PKI). Passwords are the traditional solution for user authentication, but they suffer from phishing attacks and data breaches. This is where passkeys come in.

Instead of explaining what passkeys are and why they are better than passwords—[something](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html) [many](https://www.eff.org/deeplinks/2023/10/what-passkey) [other](https://fidoalliance.org/passkeys/) [resources](https://passkeys.dev/) have already covered—this post will examine the cryptography behind passkeys, the guarantees they do or do not give, and interesting cryptographic things you can do with them, such as generating cryptographic keys and storing certificates. You need to understand the cryptography behind passkeys to implement secure authentication correctly. We’ll also discuss the main passkey specification, WebAuthn, and show you how to use extensions of passkey mechanisms to build a more intricate system with different capabilities.

## Passkey cryptography basics

At their core, passkeys are just key pairs used to produce digital signatures. When registering a passkey, the website saves the public key and an identifier. When authenticating a user via a passkey, the website provides a challenge and waits for a signed response including this challenge (and some other metadata, such as the identifier). The identifier is used to look up the public key, which is used to verify the signature.

From a cryptographic perspective, this is quite straightforward. The private key authenticates the user, but no sensitive information useful to an attacker is communicated to the server. If the server challenge is properly generated—e.g., as a uniformly random sequence of 32 bytes—then it will prevent replay attacks. Since the server holds only a public key and the user does not send it sensitive information, there is nothing to be leaked in case of a hack.

But digital signatures alone aren’t enough to solve the phishing problem. If we stopped here with just the cryptographic primitives, users would still be vulnerable. For instance, without additional safeguards, an attacker might trick users into signing challenges for the wrong website or reusing the same key pair across multiple sites.

This is why passkeys are built on the [W3C’s WebAuthn](https://w3c.github.io/webauthn/) specification, which adds crucial security properties beyond the basic cryptography. Let’s look at how WebAuthn transforms these simple cryptographic primitives into a phishing-resistant authentication system.

## WebAuthn

WebAuthn is the main specification behind passkeys. In simple terms, users access a **website** (relying party) through their **browser** (WebAuthn user agent) on a **device** such as a laptop, phone, or PC (client device). The browser interacts with an **authenticator**, a piece of hardware or software that generates the passkey key pair, and creates digital signatures using this key pair.

![Simplified view of a passkey authentication flow](/img/cryptography_behind_passkeys_image1.png)

Figure 1: Simplified view of a passkey authentication flow.

In the diagram above, you can see how a passkey authentication works:

1. The website requests authentication through the browser.
2. The browser communicates with the authenticator.
3. The authenticator checks credentials and user presence.
4. The authenticator returns a signed response.
5. The browser forwards this response to the website for verification.

(This interaction between browser and authenticator is described in more detail in another specification: the FIDO Alliance’s [Client to Authenticator Protocol](https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-errata-20220621.html) (CTAP).) This is a simplified description; the WebAuthn specification allows for a larger variety of use cases (e.g., everything could work via a mobile application instead of a website/browser). However, those specifics are not relevant to understanding how passkeys work with cryptography.

## Anti-phishing protections

WebAuthn solves the phishing problem through origin binding. The specification requires browsers to provide the **origin** of the request (i.e., the website domain) to the authenticator. The authenticator in turn uses passkeys only when the website making the request matches the website that created the passkey.

This means that if you create a passkey for bank.com, a phishing site at fake-bank.com simply cannot use it—your authenticator will refuse the request. Each website also gets its own unique key pair, eliminating the password reuse problem entirely.

Additionally, the specification allows only origins that use HTTPS, which means that the request comes from a server that has a valid certificate for the corresponding origin.

## Types of authenticators

Generally, authenticators are “something you have.” All authenticators can check whether a user is actually present when authenticating. Some authenticators can additionally verify the user according to “something they know,” such as a PIN, or “something they are,” such as their biometrics.

There are two main types of authenticators you’ll encounter:

* **Platform authenticators**: These live inside the user device itself.
  + Examples: iCloud Keychain, Google Password Manager, Windows Hello, 1Password
  + Pros: Convenient, often include cloud backup capabilities
  + Cons: Vulnerable if the device itself is compromised
* **Roaming authenticators**: These are separate dedicated hardware devices
  + Examples: YubiKeys, Titan Security Keys, Feitian keys
  + Pros: Higher security isolation, not affected by device compromise
  + Cons: Can be lost or damaged, typically no backup mechanism

If a platform can do cross-platform communication (such as Bluetooth), its platform authenticators can also be used as roaming authenticators by communicating with another device (e.g., a smartphone[1](#fn:1)). For maximum security in high-value applications, we recommend using dedicated hardware security keys as your authenticators.

Some authenticators show the user details of the request that it is producing a digital signature for. For authenticators that cannot do this, the browser will display these details instead. Always verify these details before approving an authentication request.

When a user registers a passkey on a website, the authenticator generates a passkey and an identifier (credential ID). The website stores the public key and the identifier and ties them to the user account. The website can then use this identifier to tell authenticators which passkey they want to access. Some authenticators have a lot of storage, and they store all user passkeys themselves. Other authenticators do not, so they instead encrypt the passkey and provide the encrypted passkey to the website as the identifier during registration. When the website wants to authenticate a user, it provides the identifier to the browser, which in turn provides it to the authenticator, which decrypts it and uses the passkey. Essentially, the website is storing the passkey, but since it is encrypted it is of limited value if the website gets hacked.

In theory, you can just store a cryptographic key pair in a file, write some software around it that uses this key pair for cryptogr...