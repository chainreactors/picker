---
title: The Architects of Evasion: a Crypters Threat Landscape
url: https://blog.sekoia.io/the-architects-of-evasion-a-crypters-threat-landscape/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-09
fetch_date: 2025-10-04T12:12:17.736986
---

# The Architects of Evasion: a Crypters Threat Landscape

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# The Architects of Evasion: a Crypters Threat Landscape

In this report, we introduce key concepts and analyse the different crypter-related activities and the lucrative ecosystem of threat groups leveraging them in malicious campaigns.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR and Livia Tibirna](#molongui-disabled-link)
March 7 2024

0

13 minutes reading

As of today, a **large majority of intrusion sets** and threat actors **leverage crypters** prior to delivering and executing malicious payloads on a target system. They use it to **build malware capable of avoiding security solutions**. In their campaigns, malicious actors can rely on an **open-source**, a **commercially available** or a **custom** crypter.

While a crypter software is not malicious per se, it is **intended to hide known malicious code** such as ransomware, infostealers or RATs and to **facilitate malware delivery**. Therefore, understanding the functioning of the crypters ecosystem is essential to having a more accurate view of the broader cybercrime landscape.

In this report, we introduce key concepts and analyse the different **crypter-related activities** and the **lucrative ecosystem of threat groups** leveraging them in malicious campaigns. Our analysis is based on the Sekoia Threat Detection & Research (TDR) team investigation results, insights from open-source reporting, and extensive monitoring of different cybercrime platforms.

While it has been reported that APT groups also [leverage](https://flashpoint.io/wp-content/uploads/Flashpoint_RUS-UA_2023-FINAL.pdf) crypters, often sourced from third-party services mentioned in this report, our analysis centres on **financially-motivated** activities.

## Definitions and Background

### Crypters

**Crypters** (“криптер” in Russian)are software programs capable of **encrypting, obfuscating, and manipulating malware to bypass detection mechanisms**, while keeping the malware’s functionalities intact. This is made by leveraging different **obfuscation techniques**, notably code transformations.

Of note, some sources use the terms “packer”, “cryptor” and “loader” interchangeably when referring to crypters.

Crypters are most commonly used to **deliver Remote Administration Tools (RATs), infostealers and ransomware**. This is notably the case for malware families distributed on a large scale. As the final payload is typically chosen by the crypter user individually, **the same crypter is often used for disparate final payloads** and campaigns. Therefore, clustering crypter-related activities (notably the “as-a-service” activities) is challenging from a defender point of view.

### Scantime and runtime crypters

Depending on the anti-detection routine used, there are scantime and runtime crypters. On the one hand, **scantime crypters** are known for their capability of obfuscatingmalware before execution. This is effective during a scan of files stored on a disk but is potentially susceptible to detection during the malware execution, as the file should be decrypted before running.

On the other hand, **runtime crypters** are designed to bypass detection during the execution process by loading decrypted portions into memory as separate processes. After the malware is launched, the stub code re-encrypts it. This allows the malware to be loaded and executed before security systems can respond to any malicious behaviour.

![The classification of crypter software depending on the type of stub used.](data:image/svg+xml...)![The classification of crypter software depending on the type of stub used.](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/03/Scantime-and-Runtime-Crypters-1024x723.png)

### (Crypter) Stub

A crypter software typically encrypts or obfuscates a binary and modifies it to decrypt itself during runtime. The part of the modified program **responsible for decrypting the main payload** is called the **stub** (“стаб” in Russian). The following are different types of stubs:

* **Public** (**shared**) stubs are commonly available, widely used and shared among multiple users. While they do not require any financial effort, public stubs are more easily detected by security systems.
* **Private** stubs are unique to each user or a smaller group of users. They are updated regularly, usually daily, to stay ahead of antivirus (AV) signatures. While they are more expensive on the cybercrime market, private stubs generally ensure a longer FUD (Fully UnDetectable) time for the related crypter (*e.g.* [FUDcrypter/Data-Encoder](https://blog.bushidotoken.net/2023/03/tips-for-investigating-cybercrime.html)).
* **Melt** stubs are designed to be self-destructive. After it has served its purpose of decrypting and executing the main payload, it deletes itself.

Depending on the type of stubused, **crypters can be classified as static or polymorphic**. While static crypters use the same stub across different encrypted files, polymorphic ones leverage a dynamic stub. For example, AceCryptor launches numerous System calls to standard libraries (*e.g.* Kernel32, WS\_32) to masquerade as legitimate software. Techniques to detect the environment or to detect debugging processes are concealed in the API calls to prevent full execution of the crypter. So, polymorphic crypters  constantly change their signature while retaining functionality (*e.g.* shuffling blocks of code while preserving a malicious file’s ability to run, inserting garbage code, *etc.*), making it more difficult to detect.

![The classification of crypter software depending on the anti-detection routine used.](data:image/svg+xml...)![The classification of crypter software depending on the anti-detection routine used.](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/03/Static-and-Polymorphic-Crypt...