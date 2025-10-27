---
title: Emergency Accounts: Last Call!
url: https://blog.nviso.eu/2024/09/17/emergency-accounts-last-call/
source: NVISO Labs
date: 2024-09-18
fetch_date: 2025-10-06T18:24:37.420677
---

# Emergency Accounts: Last Call!

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

# Emergency Accounts: Last Call!

[Victor Turegano](https://blog.nviso.eu/author/victor-turegano/ "Posts by Victor Turegano")

[Azure](https://blog.nviso.eu/category/cloud-security/azure/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/), [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)

September 17, 2024September 17, 2024
6 Minutes

## Update your emergency accounts before October 15th.

Even if you have been out of office for the last couple of months, you should be aware that starting October 15th you will need to provide Multi Factor Authentication (MFA) to logon to Azure portal, Entra admin center and Intune admin center. This will be enforced to all users accessing these resources regardless of their role or permission level.

Microsoft article: [Mandatory MFA for Azure and other administration portals.](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication)

Two types of accounts are notably affected by this enforcement:

* Emergency “Break the Glass” accounts.
* Non-personal accounts (NPA). Meaning regular user accounts used by services or applications.

The latter will most likely be affected beginning of 2025. That is why this article will focus on Emergency accounts.

### What are emergency accounts?

Microsoft recommends that you set up one or two directly assigned emergency accounts in case you lose access to your tenant for whatever reason. In general, these are the characteristics of emergency accounts:

* Cloud-only accounts which do not have dependencies on on-premises services. It is customary to use the \*.onmicrosoft.com domain for these accounts.
* Directly assigned to the Global Administrator role.
* Excluded from almost all conditional access policies.\*
* Not assigned to one individual.
* With minimal number of dependencies, including MFA service.

In practice, this was most times achieved by creating an account with a long password which was then split into pieces and given to different people in the organisation and no MFA was configured or required for these accounts.

With Microsoft’s new MFA enforcement, you need a different approach for emergency accounts.

\* We recommend creating specific conditional access policies for emergency accounts to compensate for the exclusions.

## You need to enable MFA for emergency accounts by October 15th

![October 15th](https://blog.nviso.eu/wp-content/uploads/2024/09/Deadline.jpg)

In practice, you can choose any MFA method supported by Entra ID for your emergency accounts. But now that you are forced to do it, why not pick a long-term solution?

[Phishing-resistant MFA methods](https://www.sans.org/blog/what-is-phishing-resistant-mfa/) are the best solution for securing your emergency accounts and still being able to use them in case of an (ahem) emergency. Other than eliminating MFA methods one by one, I will appeal to the risk-based approach: if you will have an account with direct Global Administrator access, you should protect it accordingly.

From the three phishing-resistant methods currently supported by Entra ID we recommend FIDO2 compliant keys. The reasons of this recommendation:

* Microsoft Authenticator (as sign-in method) and Windows Hello for Business are linked to a specific device which will need to be maintained, updated, and (even if they fit in a safe) how will they remain charged?
* Certificate authentication needs an infrastructure for the trust chain which represents an additional dependency.
* FIDO2 hardware keys are the most cost-efficient solution to protect your emergency accounts.

While you are at it, why not deploy FIDO2 keys for all your administrators? 😊

There are plenty of [supported FIDO2 compliant keys](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-fido2-hardware-vendor#fido2-security-keys-eligible-for-attestation-with-microsoft-entra-id) available that you can use with Entra ID. Some of them require a PIN or passphrase to activate the cryptographic functions, some are unlocked by Biometrics. This is referred to as “a gesture” that activates the key, and it varies from one vendor to another.

You must be aware that, even if Entra ID now supports device-bound FIDO2 passkeys, this approach is similar to using a smartphone or Windows device which you will need to maintain and keep updated to be used for emergency access when required and, thus, not recommended.

## Suggested approach

In the times when a long shared password was used, there was a group of people within the organization, the Quorum, who held the pieces of the password. This Quorum was normally composed by members of the C-Suite, IT and security management. A sub-group of these members was required to get access to the emergency accounts to mitigate the possibility of misuse.

Today, we would leverage the possibility to register multiple FIDO2 keys for one emergency account. These keys should be kept securely (in a safe, for example) and in such a way that prevents one individual from accessing them alone.

There are two viable options:

* Two individuals split the combination to one physical safe that holds one FIDO2 key. Both (or even a third person) hold the “gesture” to activate the key.
* One individual knows the combination of the physical safe and another knows the PIN for the FIDO2 key or has the fingerprint to activate it.

Either option will provide *separation of duties*. There are many possible deviations from those options, but keep in mind not to place all the responsibility in one person only.

Replicating the setup in another geography or region, will also provide redundancy in case of localized emergency. (i.e. physical safe being inaccessible, faulty FIDO2 key, etc.)

You can decide if you prefer to create only one emergency account with several FIDO2 keys assigned to it, or creating separate accounts for each location.

Ensure you register more than one FIDO2 key to each emergency account you create. It is even better to use different hardware providers to be prepared in situations like the one related to Yubikey’s recently discovered [vulnerability](https://www.yubico.com/support/security-advisories/ysa-2024-03/).

### Pros and Cons

The most obvious inconvenience for the suggested approach is the dependence on a physical key for emergency access. But you should registe...