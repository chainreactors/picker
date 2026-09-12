---
title: BEAR-C2
url: https://kitploit.com/en/tools/github/s3n4t0r-0x0/bear-c2
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:05.586922
---

# BEAR-C2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/s3n4t0r-0x0/bear-c2

![](https://assets.kitploit.com/production/public/tools/54775/6dbf3b3b9d78cd298f8a845712ad9f08d7b5c021b95369f620c2e7fd3749d6db-display-v1.webp)

[Penetration Testing Frameworks](/en/categories/penetration-testing-frameworks)[Exploit Frameworks](/en/categories/exploit-frameworks)[Persistence Mechanisms](/en/categories/persistence-mechanisms)[Data Exfiltration](/en/categories/data-exfiltration)[Post-Exploitation](/en/categories/post-exploitation)[Security Virtualization](/en/categories/security-virtualization)[Phishing](/en/categories/phishing)[Command and Control](/en/categories/command-and-control)[Red Teaming](/en/categories/red-teaming)[Payload Development](/en/categories/payload-development)[Adversarial Attack](/en/categories/adversarial-attack)

![GitHub](/providers/github.png)s3n4t0r-0x0/bear-c2

# BEAR-C2

The exploit server for out-of-band findings. Point a target at a domain you own. Every HTTP request and every email it sends back lands in a dashboard you control, and it gets whatever response you choose in return.

[View Repository](https://github.com/s3n4t0r-0x0/bear-c2)[Website](https://x.com/S3N4T0R_0X0)

583125321 day ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# BEAR-C2 Adversary Simulation Framework

---

![Project Status](https://img.shields.io/badge/Status-BETA-yellow?style=flat-square) [![verigen: 2.0](https://img.shields.io/badge/verigen-2.0-green?style=flat-square)](https://img.shields.io/badge/verigen-2.0-green?style=flat-square) ![Adversary Simulation](https://img.shields.io/badge/Adversary-Simulation-purple?style=flat-square) ![TTPs](https://img.shields.io/badge/TTPs-Emulation-blue?style=flat-square) ![APT Simulation](https://img.shields.io/badge/Red-Team-darkred?style=flat-square) ![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT&CK-orange?style=flat-square) [![Linux](https://img.shields.io/badge/Platform-Linux-black?style=flat-square)](https://img.shields.io/badge/Platform-Linux-black?style=flat-square)

BEAR-C2 is an adversary simulation and emulation framework built around real world TTPs inspired by `Russian, Chinese, North Korean, and Iranian APT groups.` It provides a flexible environment for diverse engagement scenarios and delivers a realistic foundation for red team operations and adversary emulation drawing from related simulation research in the [APT Attack Simulation Repository](https://github.com/S3N4T0R-0X0/APT-Attack-Simulation). It supports defense evasion techniques and multiple encryption options for accurate representation of real world intrusion scenarios.

---

![image psd(1)](https://assets.kitploit.com/production/public/readmes/54775/73e92140567d4515531b07a8a874017631d26d5b938823cfafbea1d8a6842cc7/8bb96e1108c0b44e532d8f43eba18f3d72500d788ddb48f5fe630d2c8b114125-display-v1.webp)
> [!CAUTION]
> It's essential to note that this project is for educational and research purposes only, and any unauthorized use of it could lead to legal consequences.

## 🏗 Install dependencies and Usage:

root@kitploit:~

```
git clone https://github.com/S3N4T0R-0X0/BEAR-C2.git && cd BEAR-C2

chmod +x requirements.sh && ./requirements.sh

./BEAR-C2
```

---

## 🧠 The Challenge with Adversary Simulation:

Accurately replicating **APT techniques** requires a `flexible environment capable of mimicking connection protocols, encryption methods, exfiltration techniques, and C2 Channels/Profiles` used in modern intrusions. However, achieving this level of precision has always been a challenge.

![main ](https://assets.kitploit.com/production/public/readmes/54775/8af4474bf61f52114745ec8403b4ea6d01d26a57f85913f1f01b4bba559a1eb7/59654a7b465df184554d5c31ee49293c1f5d9da71a1e6ef81aa0a2fa5b88b8ea-display-v1.webp)

Every time an operator needs to test a specific **encryption scheme** with a particular **exfiltration profile**, a separate **C2 script** `must be built to match the attack scenario.` For example, one simulation might require **AES encryption** with **OneDrive exfiltration**, while another might need **a different encryption method** combined with **Dropbox exfiltration** to reflect the techniques observed in real world attacks. This lack of flexibility makes the process inefficient and time consuming.

![Screenshot From 2026-09-01 05-54-48](https://assets.kitploit.com/production/public/readmes/54775/c106129e53832b08e6575610090337721e4e5892eade10bee395fae638326cc2/299229b4ffae9286d368a6e9243c4528d469f5395f166d9b67fa0020beaf5d8a-display-v1.webp)

This is why **BEAR C2** was developed to provide **adversary simulation** with full customization through the new listener, allowing seamless configuration of `connection protocols, encryption, exfiltration,` and automated loading techniques. This ensures that simulations can accurately reflect real **APT intrusions** without the need to build custom scripts for every scenario.

## Reaper Node Payload Samples

Reaper Node provides C++ payload samples `/Stagers-Loaders/Reaper Node Samples/` that can be used as customizable templates for environments where a pre-generated payload is not required. The samples contain the core configuration fields required to establish communication with the corresponding Reaper Node instance.

Before compiling the payload, the required connection and transport parameters must be configured to match the Reaper Node configuration.

### Payload Configuration

The payload configuration should provide input fields for the following parameters:

* **Authentication ID**
  The identifier used to associate the payload with the configured Reaper Node instance.
* **Server Host**
  The IP address or hostname of the Reaper Node endpoint.
* **Server Port**
  The network port exposed by the Reaper Node for the selected communication protocol.
* **Encryption Key**
  Required when the selected transport uses encryption. The value must match the encryption configuration used by the Reaper Node. If encryption is disabled, this field is not required.
* **User-Agent**
  The HTTP client identification value used when establishing the initial HTTP/HTTPS communication. The payload should use a User-Agent supported by the corresponding Reaper Node configuration.

The User-Agent does not need to be identical across different Reaper Node configurations. A payload can use any User-Agent defined as supported by the selected Reaper Node profile, as long as the resulting configuration is compatible with the server-side transport settings.

### Example Configuration

The following example shows a sample HTTPS transport configuration with authentication, server addressing, encryption, and User-Agent parameters:

root@kitploit:~

```
const string AUTH_ID = "YOUR_AUTH_ID";
const string SERVER_HOST = "YOUR_SERVER_HOST";
const int SERVER_PORT = YOUR_SERVER_PORT;
const string KEY = "YOUR_ENCRYPTION_KEY";
const string DEFAULT_USER_AGENT = "YOUR_USER_AGENT";
bool VERIFY_SSL = true;
```

This configuration represents an HTTPS transport with encryption enabled. Th...