---
title: Fake crypto-wallet downloads used to deploy ScreenConnect remote access software
url: https://bartblaze.blogspot.com/2026/11/crypto-hardware-wallet-users-under.html
source: Blaze's Security Blog
date: 2026-11-17
fetch_date: 2026-11-18T09:24:27.546808
---

# Fake crypto-wallet downloads used to deploy ScreenConnect remote access software

# [Blaze's Security Blog](https://bartblaze.blogspot.com/)

Personal blog about internet & malware threats.

## Search this Blog

|  |  |
| --- | --- |
|  |  |

* [Home](https://bartblaze.blogspot.com/)
* [Ransomware Prevention](https://bartblaze.blogspot.com/p/ransomware-prevention.html)
* [The purpose of ransomware](https://bartblaze.blogspot.com/p/the-purpose-of-ransomware.html)
* [About Me & Disclaimer](https://bartblaze.blogspot.com/p/about.html)

## Tuesday, November 17, 2026

### Fake crypto-wallet downloads used to deploy ScreenConnect remote access software

## Introduction

A new attack campaign targeting users of cryptocurrency and specifically those using hardware wallets, is doing the rounds.

The attacker's end goal is to install ConnectWise's [ScreenConnect](https://en.wikipedia.org/wiki/ScreenConnect), which is a legitimate remote-support application. **ScreenConnect enables these attackers to take remote control of the device**, execute commands, and steal any information they may find interesting.

**⚠ What if you downloaded or ran one of these files?**

If you downloaded one of the ZIP files and executed the BAT file inside, your system may be compromised.

[Read the detection and remediation instructions →](#detection-remediation)

A simple visual representation of the attack flow can be observed in Figure 1.

|  |
| --- |
| ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj51PhDfazoSTvdNC6wXk9eT0Murbd27l1DGYKuGkHvcpJ0xjxOG5xf8Xbh1WzRXsywdoydcOQ36BG9MyXAw-SlHQ7hqxQJ2bwWRjcfxLDC7n3Z9y0NjU7AvoiGd7DfK6s1FX9VsmTq51eVrJzQg3qaTGY_2CPpSuOfaLwUGKZvoC9IutIbrE931I5SyyCL/w400-h266/image.png) |
| Figure 1 - Attack flow |

## Technical analysis

The following lure names and domains have been observed in this campaign:

| Targeted service / brand | Filename / artifact | SHA-256 | Associated domain / infrastructure |
| --- | --- | --- | --- |
| Coldcard | `v1.5.3Q-q1-coldcard.bat` | 13a340968f98b27eb4e39dd61f0b75822d68c8fbc35fa7f0ef791b65f87a8997 | `coldcard[.]pro` |
| Coldcard | `v1.5.3Q-q1-coldcard.zip` | 190702a08dbb3b2c2b07b75876b6b88eec04f827070514b9ef387990fcce8b2b | `coldcard[.]pro` |
| Ledger | `Ledger-wallet-Transition-Transcript.bat` | a6e49e8686488acbe8938da3726f8510ec58e638ee804b55fda43600c4f741a2 | `ledger-wallet[.]net` `ledgeradvisorinfo[.]app` |
| Ledger | `Ledger-wallet-Transition-Transcript.zip` | 52d7d663bb916e4cbf09fe0f3317d7ec379bf64cfa326b64e52cf75c0c71dd6e | `ledger-wallet[.]net` `ledgeradvisorinfo[.]app` |
| Pera Algorand Wallet | `Pera_Algorand_Wallet_v2.1.2.35.zip` | 1166831bf6ea477cf093b0f404b4a970c253062a91cfccef96c774522a7afa91 | `peraalgowallet[.]app` |
| Pera Algorand Wallet | `Pera_Algorand_Wallet_v2.1.2.35.bat` | f7f646ce988f9af34075792805b786aea16a53d67c5cda5cbbe484f37b2fa1af | `peraalgowallet[.]app` |
| Revolut | `revolut-taxfile.zip` | 633aec4539c4608fbb6cd19e596bc463c709761b04150cce8a4b0995702d51fa | N/A |
| Revolut | `Revolut-taxfile.bat` | f7f646ce988f9af34075792805b786aea16a53d67c5cda5cbbe484f37b2fa1af | N/A |
| ScreenConnect | `screenconnect.msi` | b3418cfb2a5b36682429b10443cd5333d19346fee83e8b85d7f6947b4ad3fa4a | `fjksdjfdtitive[.]net` Remote-access server |
| ScreenConnect | `screenconnect.exe` | 99f35301f179919706ce7c82379c37631d2d1cdab28a0b63cfa5044b20c06cad | `fjksdjfdtitive[.]net` Remote-access server |
| Xaman | `xamantaxfile.zip` | a311a02a982acf1a8bd61b87b79c9ac98e54827892f1caf126e09aba586dfabc | N/A |
| ScreenConnect | N/A | ec874726bb4f58823a95674ceca60cb23cfa8546489b9b9d0382ae64bf2892f1 | `fjksdjfdtitive[.]net` Remote-access server |

In this attack campaign, the ScreenConnect client service is configured to connect to fjksdjfdtitive[.]net on TCP port 8041. In addition, it also features the following connection parameters:

* `h=` Remote host
* `s=` Session identifier
* `e=Access`
* `y=Guest`

The login page behind fjksdjfdtitive[.]net allows the attacker to login and remote control any impacted device as seen in Figure 2 below.

|  |
| --- |
| ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1D1waLVFw9nl3Pev8YWzL2K-ktxRigElRUbWjkdrdufVtgo3lvHi5a7K3VOeLopEzaf4wDGXI4Pdu-E1zEXORQgbmKGtSdJC7NIFGpHSjV1IvNYQZKPgCqJMkqxzz_dN-i6XZn0Bl-0Uqd5hLCJguvh9nr8X22nuS2kar3GAtI2Ug4YMgfIElajWLKuXr/w320-h162/image.png) |
| Figure 2 - ScreenConnect login page |

## Detection and Remediation

If you downloaded any of the ZIP files, and ran the BAT file inside, it is highly likely you have been affected by this campaign. Follow the steps below to verify if you have been infected and to remove ScreenConnect.

### 1. Isolate first

* Disconnect the device from Wi-Fi and/or Ethernet.
* Avoid using the affected device for cryptocurrency wallets, banking, email, or anything else for the time being.

### 2. Block ScreenConnect domain and/or IP

If you have a firewall, or use any DNS filtering or software, or perhaps a proxy, block fjksdjfdtitive[.]net first and foremost from accessing the internet. Do the same for the IP  191.96.101[.]224. *Note*: remove the square brackets [].

You should block both the domain and IP address on the network level if possible, so all your devices are protected.

### 3. Review if impacted

Review Installed Apps or Programs and Features (installed software) for:

`ScreenConnect Client (abb21f5ccc9bd236)`

`Note: the numbering may differ per ScreenConnect installation. U`**`nless you actually use the software, consider a``ny presence of ScreenConnect is a sign of compromise!`**

Investigate the associated Windows service and installation directory.

Relevant paths include:

`C:\Program Files (x86)\ScreenConnect Client (abb21f5ccc9bd236)\`

Associated executables:

* `ScreenConnect.ClientService.exe`
* `ScreenConnect.WindowsClient.exe`
* `ScreenConnect.WindowsBackstageShell.exe`

Review also if a service has been installed by opening **services.msc** and verifying if a **ScreenConnect Client** service has been installed. If so, stop and disable this service first before removing the above files and folder.

If none of the above are found, ensure to also review the %TEMP% folder for presence of any batch files (.bat) or a folder starting with the name sc\_installer\_.

**If you do find any of the artifacts above, I highly recommend to reinstall Windows** to ensure any traces are completely gone. Read how to do that here: <https://support.microsoft.com/en-us/windows/experience/backup-recovery/reset-your-pc>

If you cannot identify any of the above, then you are likely not impacted. However, if you did open / run a suspicious ZIP and/or BAT (batch) file and you do not want to or cannot reinstall, then at the least, perform a full system scan with your installed antivirus/antimalware, as well as another one, for example [MalwareBytes](https://www.malwarebytes.com/).

### 4. Reset credentials

If impacted, from a separate and clean device do the following**, in parallel with Step 3 above**:

* Reset email credentials.
* Change password-manager credentials.
* Reset cryptocurrency exchange passwords.
* Revoke any active sessions and potentially API keys (after resetting passwords and logging in from a known clean / safe device).

  In addition, review and revoke suspicious token approvals.

Any locally stored wallet data may also have been exposed, as well as other sensitive data.

### 5. Additional precautions

Since it's always better to be safe than sorry, the following general advice may assist if you suspect a cryptocurrency wallet has been exposed:

1. Stop using the compromised computer for wallet operations.
2. If a recovery phrase or private key may have been exposed, treat the wallet as compromised.
3. Generate a new wallet using a clean device and a new recovery phrase.
4. Move remaining assets to the new wallet. Note this may incur a cost.
5. Verify destination addresses directly on the hardware-wallet display.
6. Review and revoke suspicious token approvals. If the wallet interacted with a suspicious *dApp* or signed an unknown approval, revoke allowances on...