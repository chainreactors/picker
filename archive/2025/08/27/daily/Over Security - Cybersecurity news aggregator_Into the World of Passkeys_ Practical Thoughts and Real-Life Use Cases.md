---
title: Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases
url: https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:49:36.190427
---

# Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/ "Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases")

[August 26, 2025](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/ "Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases")
 /
[Cyrill Brunschwiler](https://blog.compass-security.com/author/cbrunsch/ "Posts by Cyrill Brunschwiler")
 /
[1 Comment](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/#comments)

In a [previous blog post](https://blog.compass-security.com/2025/02/passkeys/), we explored the technical side of **passkeys** (also known as **discoverable credentials** or **resident keys**), what they are, how they work, and why they’re a strong alternative to passwords. If you’re a curious techie, check that out first.

But today, we’re taking a more hands-on approach. We’ll show how passkeys are used in the real world – by everyday users and security professionals alike. First, let’s quickly revisit the basics.

Why passkeys are a better way to sign-in:

* They protect you from phishing.
* They’re extremely hard – essentially impossible – to guess.
* You do not have to memorize them.
* Each service (like a website or app) automatically gets its own unique passkey.
* Passkeys can’t be stolen in data breaches.
* They’re stored securely, either on your device or in the cloud.

There are two main types:

* **Device-bound passkeys**: Stored on a specific device like a security key or your phone.
* **Synced passkeys**: Stored in your credential manager of choice and shared across your devices (like with Apple iCloud Keychain or Google Password Manager).

## Disclaimer: On Language and Precision

The terminology around passkeys is still evolving – and not always consistently used in the wild. While we strive to be accurate, we’ll occasionally trade formal precision for clarity. So, to all the RFC enthusiasts and standard purists out there: this post tries to walk the fine line between being correct and being readable. Please don’t shoot the messenger, I only mean well.

For those unfamiliar with the terminology of passkeys and authentication, there’s a glossary of key terms at the end of this post to help you out.

## So… Are Passkeys Perfect?

After hearing about all these advantages, you might be thinking: “Okay, this sounds almost too good to be true. What’s the catch?”

And you’re right to ask. Passkeys are a big leap forward – but they aren’t magic. As with any security technology, they come with trade-offs. Let’s look at some of the realistic challenges you might face when adopting passkeys in your everyday life.

### Synced Passkeys

One of the big promises of passkeys is improved usability. The FIDO Alliance – the group behind the standard – emphasizes that passkeys are not just more secure than passwords, but also easier to use. This is especially true when using Synced Passkeys, which are stored in your cloud-based credential manager and shared across your devices. Some widely known examples include:

* Apple’s iCloud Keychain
* Google’s Password Manager
* Third-party tools like 1Password, Keeper, or LastPass

Sounds great, right? It is – but it also comes with some caveats:

* If your credential manager is accessible on a shared device (say, a family iPad), everyone with access to that device might, in certain scenarios, be able to use your passkeys.
* Some platforms allow easy sharing of passkeys (e.g. on Apple via Airdrop). If a passkey is shared with another person, they receive unrestricted access to the corresponding service.
* Each credential manager handles passkeys slightly differently, which can affect how recovery, sharing, and syncing work in practice.

In other words, while synced passkeys improve convenience, they also bring some familiar challenges – particularly around managing device access and trust. It’s a classic case of balancing security and usability.

### Device-Bound Passkeys

If you use a dedicated hardware device (**hardware authenticator**) to store your passkeys, they are referred to as device-bound passkeys. Examples for this could be a USB key, your smartphone or your laptop. These passkeys are not synced or backed up anywhere. This brings stronger control and isolation, but also the disadvantages are obvious:

* You must have the device with you to log in.
* The passkeys can no longer be synchronized between different devices
* If you lose your **authenticator**, all the passkeys stored on it are also lost. In extreme cases, this can lead to you being locked out of your account for good.

Device-bound passkeys are more secure in some ways, but less forgiving. If your only passkey lives on a lost or damaged authenticator, you might be in trouble.

### Recovering Access

So, how do I regain access to my account after losing my device-bound passkey? Well, if this is the only authentication option you have configured, the answer is simple – in most cases, not at all. While some larger providers may offer limited account recovery options, relying on those is risky and not guaranteed. Therefore, it is paramount to configure a second, additional authentication option. I recommend the following setup:

* Primary login with a device-bound passkey
* Secondary backup login, consisting of:
  + A strong and unique password stored securely in a password manager
  + An additional second factor, such as an authenticator app on your mobile phone

The secondary backup login should only ever be used for recovery purposes. Additionally, those of you who want to be super safe can also have a second hardware authenticator stored in a secure location.

### Stolen Authenticator: What Now?

But what if a stranger comes into possession of your hardware authenticator? Can they log in as you? Ideally, no. That’s where the so-called **user verification** feature comes into play. Before creating your first passkey on an authenticator, you can protect it with an additional layer of security. Depending on the model, this could mean:

* Entering a PIN.
* Scanning a fingerprint.
* Using Face ID.

If the service provider has implemented passkeys according to today’s standard and best practices, every use of a passkey must be verified by the user through one of these mechanisms. That means even if a thief steals your USB key or phone, they still can’t use your passkeys without passing the verification check.

As you might have noticed, some devices fall back to a PIN – which raises the questions: “Aren’t we now protecting our wonderful passkeys with one of those previously decried passwords again? Does this mean that we are reintroducing all the password-specific problems that we wanted to solve with passkeys in the first place?”

And as is the case with almost every closed question, the best answer to this one is: It depends. While it is true that with certain models, we must remember a PIN to use the passkeys, most current authenticators offer additional protection mechanisms to prevent unauthorized use such as:

* The hardware itself may include secure elements that resist tampering.
* Biometric authentication can be used which is tied to the user.
* The dev...