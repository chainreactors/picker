---
title: Secure Enclaves for Offensive Operations (Part II)
url: https://www.outflank.nl/blog/2025/06/16/secure-enclaves-for-offensive-operations-part-ii/
source: Publications | Outflank
date: 2025-06-17
fetch_date: 2025-10-06T22:54:09.681041
---

# Secure Enclaves for Offensive Operations (Part II)

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Secure Enclaves for Offensive Operations (Part II)](https://www.outflank.nl/blog/2025/06/16/secure-enclaves-for-offensive-operations-part-ii/ "Secure Enclaves for Offensive Operations (Part II)")

[Cedric Van Bockhaven](https://www.outflank.nl/blog/author/cedric/ "Posts by Cedric Van Bockhaven")
 |
June 16, 2025

This blog post is the second part in a series about using Secure Enclaves for Offensive Operations. [The first part](https://www.outflank.nl/blog/2025/02/03/secure-enclaves-for-offensive-operations-part-i/) discussed the basics of how enclaves work, provided some ideas on how to develop your own enclave, as well as analyze and debug existing enclaves. We also hinted at how enclaves could potentially be used for offensive purposes. *Remember: VTL0 is where the normal kernel lives, VTL1 is where the secure kernel operates (and our enclaves).*

In this follow-up post, we will share what we discovered while digging into enclave internals. It’s been a hands-on journey filled with many (failed) experiments. We’ll walk you through some of the practical techniques we used to exploit a read-write primitive in a vulnerable enclave DLL, and how we managed to turn that into VTL1 code execution.

![](https://www.outflank.nl/wp-content/uploads/2025/06/image-12.png)

The outcome of this research has been integrated into Outflank C2 (part of our [OST offering](https://www.outflank.nl/products/outflank-security-tooling/)) for implant sleepmasking. As a result, when the implant is dormant, its memory remains completely hidden. Even from VTL0 ring0 (this is where an EDR typically lives), it’s not possible to inspect the implant’s memory or view the call stack of the VTL1 thread. We also added a sleepmask to Beacon Booster for Cobalt Strike. It handles sleep masking by storing the key material used to encrypt beacon memory in VTL1, while the implant data itself is stored in VTL0.

To make this work, we had to jump through several hoops. In this post, we’ll walk through how we got there and what we had to deal with along the way. This research was presented during Insomni’Hack 2025 in Lausanne, make sure to check out the [video of our talk](https://www.youtube.com/watch?v=t4VLLobgDoM).

![](https://www.outflank.nl/wp-content/uploads/2025/06/enclave-sleepmask.png)

## Crossing the Trust Boundary

In [Part I](https://www.outflank.nl/blog/2025/02/03/secure-enclaves-for-offensive-operations-part-i/), we discussed how to find enclave DLLs and how to debug them. Microsoft SQL server also ships with several enclave DLLs, let’s take a brief look at one of them.

As part of the [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17) feature in SQL server, secure enclave attestation is supported. The attestation process ensures that only trusted code is running inside the enclave before sensitive data is processed by establishing trust between the database client and server. The component responsible for handling this attestation is AzureAttest.dll.

In AzureAttest.dll (and several other enclave-related DLLs), you’ll find typical pointer validation checks that determine whether a buffer resides inside or outside the enclave.

![](https://www.outflank.nl/wp-content/uploads/2025/06/image-6.png)

Why is that important? If the enclave were to read from or write to an arbitrary user-supplied pointer without validation, it could result in leaking or overwriting sensitive enclave memory. This could expose cryptographic key material or even allow tampering with code running in VTL1.

Josh Watson (Microsoft) has recently written a blog post about the necessity of performing these kinds of checks to prevent enclave vulnerabilities: [Everything Old Is New Again: Hardening the Trust Boundary of VBS Enclaves](https://techcommunity.microsoft.com/blog/microsoft-security-blog/everything-old-is-new-again-hardening-the-trust-boundary-of-vbs-enclaves/4386961). Basically, as we’re passing data between VTL0 and VTL1, we are crossing a trust boundary. VTL1 shouldn’t trust the data it receives from VTL0.

> The most important thing to remember is that while the host process cannot read or write in the enclave’s memory region, the converse does not hold true – an enclave *can* read and write the memory of its host VTL0 process. This can create tricky situations when the enclave operates on pointers passed from the host process to the enclave.

So these pointer validations are there for a good reason. Beyond that, the blog post also explores other types of vulnerabilities, such as time-of-check/time-of-use (TOCTOU) issues. These can occur when a function is called and the pointers it relies on are updated in between, creating a race condition. You can address this by copying the structure data into the enclave function itself, so it can’t be modified externally once the check has passed.

Unfortunately, implementing checks that can prevent these vulnerabilities are left as an exercise to the enclave developer, and we’ve seen them being implemented in different ways. Ideally, Microsoft would offer convenience functions as part of its API that perform these validations.

## Microsoft Edge Preferences Enclave

Microsoft Edge bundles an enclave DLL, prefs\_enclave\_x64.dll, presumably for storing preferences securely. It’s present by default on newer systems at `%WINDIR%/System32/Microsoft-Edge-WebView/prefs_enclave_x64.dll`. It has three exported functions, one for initialization (`Init`), one for sealing (`SealSettings`) and one for unsealing settings (`UnsealSettings`).

![](https://www.outflank.nl/wp-content/uploads/2025/06/image-11.png)

Despite what the name might suggest, this DLL can be used to seal and unseal any kind of data, not just configuration settings. For example, we can use it to encrypt our implant shellcode through the enclave. The enclave DLL does not restrict what kind of information is sealed. It’s important to note that while the key material resides in VTL1, the encrypted data is still stored in VTL0. The enclave is merely used as a secure processing environment in which the data is sealed/unsealed. The implant memory is still accessible as it resides in VTL0, and the sleep function is performed in VTL0 too.

This technique is implemented in our [Beacon Booster](https://www.outflank.nl/videos/beacon-booster/) tool and allows sealing a Cobalt Strike beacon via this enclave DLL during sleep. Furthermore, a PoC for sealing arbitrary shellcode that capitalizes on this idea was weaponized by Ori David (Akamai) and explained in their blog post: [Ab...