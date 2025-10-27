---
title: The End of Passwords? Embrace the Future with Passkeys.
url: https://blog.nviso.eu/2024/07/02/the-end-of-passwords-embrace-the-future-with-passkeys/
source: NVISO Labs
date: 2024-07-03
fetch_date: 2025-10-06T17:41:47.216572
---

# The End of Passwords? Embrace the Future with Passkeys.

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# The End of Passwords? Embrace the Future with Passkeys.

[NVISO](https://blog.nviso.eu/author/nviso/ "Posts by NVISO")

[Tools](https://blog.nviso.eu/category/tools/), [Passwords](https://blog.nviso.eu/category/passwords/), [Cyberculture](https://blog.nviso.eu/category/cyberculture/), [Awareness](https://blog.nviso.eu/category/awareness/)

July 2, 2024July 2, 2024
5 Minutes

Yesterday, unexpectedly, my personal Google account suggested using Passkeys for login. This is amazing, as Passkeys is the game-changer for cyber security because it could imply the solution to one of the biggest headaches in cyber security: password use.

![decorative image showing a hand holding a smartphone with a lock and a secret from which multiple paths are starting](https://blog.nviso.eu/wp-content/uploads/2024/06/Picture1-2.png)

## The problem with passwords.

For decades, we have struggled with passwords as an authentication tool. They constitute a conceptually very weak solution for digital security. Using passwords is much more prone to abuse than most people realize. The intense use of digital applications caused users to juggle hundreds or thousands of passwords. Human behaviour led to poor practices: password re-use increased the risk of broad access breaches in case criminals stole a password. Increasing password length and complexity was circumvented by people keeping a paper list of passwords. The universal use of authentication to access a wide array of personal or business applications has created a situation where, to stay secure, a password manager and multi-factor authentication (MFA) are indispensable for critical services.
According to Google Cloud’s 2023 Threat Horizons Report, 86% of security breaches involve stolen credentials. IBM estimates the global average cost of a security breach was $4.45 million in 2023.
So how can we, in a structural way, eliminate the dangers associated with single password authentication per service and trust something more resilient, for both our private and personal digital life?

## Why passkeys are a game-changer.

After its creation in 2013, the FIDO (Fast IDentity Online) alliance paved the way in 2018 for the introduction of FIDO2 keys. The size of USB sticks, they safely store a certificate, allowing authentication on any kind of device (laptops, smartphones, etc.) These are also known as YubiKeys (the most famous product leveraging this technology). These products have a good reputation and a reasonable adoption among users and institutions aware of the dangers of using passwords.
But while this key offers one of the best protections available on the market, the need to buy and manage a separate token is a showstopper for many individuals, although the daily use of passwords is ubiquitous. Passkeys offer a much better alternative.
So, why am I so enthusiastic about passkeys? Because they solve all the issues associated with passwords for both security professionals and everyday users.

Here’s how passkeys shine:

* Enhanced Security: Passkeys are resistant to phishing and brute-force attacks. They are complex in structure and length and cannot be guessed.
* Privacy: The private key never leaves the user’s device, reducing the risk of theft.
* Convenience: No need to remember complex passwords.

## What exactly are passkeys?

Do not confuse passkeys with passphrases. Passphrases, like passwords, are secrets you need to remember and enter manually. They are just longer passwords. Passkeys, however, are fundamentally different.
Passkeys rely on asymmetric cryptography, meaning they consist of:

* A Private Key: Securely stored on the user’s device.
* A Public Key: Shared with the server to verify the user’s identity.
* A Challenge-Response Mechanism: Used to authenticate the user without exposing the private key.

Here is a simplified description of the logon process.

![The passkeys logon process. ](https://blog.nviso.eu/wp-content/uploads/2024/06/image-3-544x1024.png)

Source: Bitwarden.com.

The private key is the crucial element to secure, often stored in a password vault or, even better, in the TPM chip of your computer. Any modern smartphone or computer offers a way to securely store a private key, making it straightforward to use passkeys. As a fallback, password managers offer a reliable storage solution.

## Built on open standards.

Passkeys are based on open standards developed by the FIDO Alliance. Security keys like YubiKey are also based on those standards. However, earlier versions required buying a physical key and were often complicated to initialize. For companies, the cost of buying and managing large numbers of physical keys was also a barrier.
Modern passkeys no longer require a token but can be installed as software. Together with the widespread adoption of MFA, they offer a truly passwordless solution, compatible with state-of-the-art devices, and therefore easy to obtain and install.

## For both personal and corporate use.

Tech giants like Google, Microsoft, Apple, Amazon, and Meta are now adopting passkeys. For users, logging in will be as simple as validating the connection on their phone, using a PIN or biometric authentication.
For companies, passkeys and FIDO standards represent an opportunity to enhance security by reducing risks associated with traditional password use and implementing a passwordless strategy. Passkeys are easy to use, easy to deploy, cost-effective, and robust. All major cloud vendors provide guidance on implementing passkeys or any other passwordless based on FIDO standards, and Microsoft is providing guidance on Active Directory implementation.
One more thing remains, where to keep your secrets?
When you use passkeys, keeping your certificates safe is crucial. You might be wondering where to put that secret, right? After all, you don’t want anyone else getting their hands on your private key. The good thing is that you have plenty of options! The not so good thing is that they all have their pros and cons. As always, you will have to balance security and convenience.

The table below shows your alternatives for storing your passkeys:

| **Store your passkeys in:** | **PROS** | **CONS** |
| --- | --- | --- |
| TPM chip of your computer | High security, protection against hardware and software attacks with the integrated TPM Chip | Less flexible for multi-device access |
| Smartphone | Conveni...