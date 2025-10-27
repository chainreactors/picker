---
title: 2024-09-19 UNC1860 Iran APT -  Temple of Oats ( OATBOAT,  TEMPLEDOOR, SASHEYAWAY,  OBFUSLAY,  WINTAPIX,  CRYPTOSLAY) Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-19-unc1860-iran-apt-temple-of.html
source: contagio
date: 2024-09-21
fetch_date: 2025-10-06T18:31:39.510154
---

# 2024-09-19 UNC1860 Iran APT -  Temple of Oats ( OATBOAT,  TEMPLEDOOR, SASHEYAWAY,  OBFUSLAY,  WINTAPIX,  CRYPTOSLAY) Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Thursday, September 19, 2024

### [2024-09-19 UNC1860 Iran APT - Temple of Oats ( OATBOAT, TEMPLEDOOR, SASHEYAWAY, OBFUSLAY, WINTAPIX, CRYPTOSLAY) Samples](https://contagiodump.blogspot.com/2024/09/2024-09-19-unc1860-iran-apt-temple-of.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeREVzdywWNCwvJWqVuNg63iMRy1ooPd_aQluMq1rs1HlJ1BO1YI48wE7kX32ib8LBpl2pnn-OIMDsfOC-UU4jLbxtCF7UzAhr7i14rSv52nNOB_o1-S-zIWOSCsRS_s8y8NIne2qwNgDJYbpRMp8wrB7bCjuHK8HOR1w5bOLs01e9CKwOHEZshnnrFe4/w252-h247/Discord%202024-09-19%2023.25.17.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeREVzdywWNCwvJWqVuNg63iMRy1ooPd_aQluMq1rs1HlJ1BO1YI48wE7kX32ib8LBpl2pnn-OIMDsfOC-UU4jLbxtCF7UzAhr7i14rSv52nNOB_o1-S-zIWOSCsRS_s8y8NIne2qwNgDJYbpRMp8wrB7bCjuHK8HOR1w5bOLs01e9CKwOHEZshnnrFe4/s387/Discord%202024-09-19%2023.25.17.png)

 [2024-09-19 Mandiant: UNC1860 and the Temple of Oats: Iran’s Hidden Hand in Middle Eastern Networks](https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks/)

UNC1860 is an Iranian state-sponsored threat actor, likely affiliated with the Ministry of Intelligence and Security (MOIS), known for its persistent and stealthy operations. It employs a variety of specialized tools, passive backdoors, and custom utilities to target high-priority networks, such as government and telecommunications entities in the Middle East.

**Passive Implants:** UNC1860 relies on custom-made passive backdoors like TOFULOAD and WINTAPIX, which leverage undocumented Input/Output Control (IOCTL) commands for communication, bypassing standard detection mechanisms used by EDR systems. These implants operate without initiating outbound traffic, making them difficult to detect through traditional network monitoring tools.

**Windows Kernel Driver:** UNC1860 repurposed a legitimate Iranian antivirus kernel mode driver, Sheed AV, for stealthy persistence. This driver is used in TEMPLEDROP, a passive backdoor that protects its own files and other malware it deploys, preventing modification and enhancing its evasion capabilities.

**Obfuscation and Encryption**: The group implements custom XOR encryption and Base64 encoding/decoding libraries to avoid detection. For example, XORO, a rolling encryption module (MD5: 57cd8e220465aa8030755d4009d0117c), is used in several utilities such as TANKSHELL and TEMPLEPLAY. These encryption methods, although simple, are tailored to evade standard detection signatures.

TEMPLEPLAY and VIROGREEN Controllers: These GUI-operated malware controllers allow UNC1860 or third-party actors to manage compromised systems easily. They provide features such as:

**Command execution** via the Command Prompt Tab.

**File transfer** through Upload and Download Tabs.

Using infected systems as middleboxes through the Http Proxy Tab, facilitating RDP connections even in restricted environments.

**Web Shells and Droppers:** Web shells like STAYSHANTE and SASHEYAWAY are frequently deployed after initial access is achieved. These shells enable further persistence by deploying full passive backdoors, such as TEMPLEDOOR and FACEFACE, which can execute commands, transfer files, and interact with system services.

**Multi-stage Implants:** UNC1860 maintains a suite of "main-stage" implants with advanced capabilities, reserved for high-value targets. These implants, such as TOFULOAD and TEMPLEDROP, demonstrate the group's deep understanding of Windows kernel components and its ability to bypass security measures like kernel protections.

**Reverse Engineering and Evasion:** UNC1860 exhibits strong reverse engineering skills, especially evident in their repurposing of legitimate software like Windows file system filter drivers. This allows the group to manipulate system components for stealthy operations, using advanced evasion techniques like terminating Windows Event Log service threads and restarting them as needed.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/APT/Iran/UNC1860%2BIran%2BAPT%2BSamples.zip)

**File Information**

* ├── ALL\_LISTED
* │   └──
* │       ├── 0969f7f5556e3babd7050308a29fa2987dce01b3c94959724c9cd49bce052d80
* │       ├── 1146b1f38e420936b7c5f6b22212f3aa93515f3738c861f499ed1047865549cb
* │       ├── 1485c0ed3e875cbdfc6786a5bd26d18ea9d31727deb8df290a1c00c780419a4e
* │       ├── 159eecbba87a7397a5b84a21c289ae66ec776a3fd3b41bf11549fb621afebc0a
* │       ├── 1786916c1e3b16ce654497861fe43bb595ea0f0fa0fad4cd62f3edc82f9a27d4
* │       ├── 1c57b1ed990a8946e86d69da2a047fa15525d883b86e93cb6444a4065dbad362
* │       ├── 2097320e71990865f04b9484858d279875cf5c66a5f6d12c819a34e2385da838
* │       ├── 23a9abed7c4a76a5cacf1e984ecf3cce91c3c1bbf4424c4b2ee141b4154c3703
* │       ├── 2538767f13218503bccf31fccb74e7531994b69a36a3780b53ba5020d938af20
* │       ├── 269d7faed3a01b5ff9181df32e3fdbf7f7f193cc53e4f28aa21290343e69f3cd
* │       ├── 3269de107e436a75a8308377709dc49b4893cfd137a3fc5b92d0f0590af4cb12
* │       ├── 359d826ff025c5e4971d90be0d7dfebe10fc125f6dcaa2f0e9869e9f6bec4432
* │       ├── 36b61f94bdfc86e736a4ee30718e0b1ee1c07279db079d48d3fe78b1578dbf03
* │       ├── 3875ed58c0d42e05c83843b32ed33d6ba5e94e18ffe8fb1bf34fd7dedf3f82a7
* │       ├── 58cb1ef132fbdd1855f75c2886666275d1bb75a9fb3fed88d05feee4230afd32
* │       ├── 59463257c3f2425109fd097f814b6468663df947de8178c8cd7b7c5e94d3375c
* │       ├── 596b2a90c1590eaf704295a2d95aae5d2fec136e9613e059fd37de4b02fd03bb
* │       ├── 5cb88ec4eca35c41dbf32218c0f031e75e4c24a17cabe9eea2aa06efa5982967
* │       ├── 67560e05383e38b2fcc30df84f0792ad095d5594838087076b214d849cde9542
* │       ├── 6f0a38c9eb9171cd323b0f599b74ee571620bc3f34aa07435e7c5822663de605
* │       ├── 6f938caeefa0aea3b8301e07bf918a49408cd319187d05ac519b20a00f460469
* │       ├── 71106875c37bf5b92ef25c7bc1d607ae349aa85bbb2e92a39165a8a8f8f6eb0e
* │       ├── 7495c1ea421063845eb8f4599a1c17c105f700ca0671ca874c5aa5aef3764c1c
* │       ├── 786298c0d98aaf35777738a43a41546c6c8b1972b9bd601fb6cccf2c8f539ae4
* │       ├── 7a1fee8d879bc16e63d05c79c5419bd19ee308c54831d7ee196cfa8281498a06
* │       ├── 8578bff36e3b02cc71495b647db88c67c3c5ca710b5a2bd539148550595d0330
* │       ├── 8e4f7a19b09e118ebda79726bf17e9d37ff4b66f4143762dd97ca80340388963
* │       ├── 8fdd00243ba68cadd175af0cbaf860218e08f42e715a998d6183d7c7462a3b5b
* │       ├── 90b3f7fefe8e11b8eacaba09a3c14ed6aa66a4c8d798440d912d0a663917a265
* │       ├── 9117bd328e37be121fb497596a2d0619a0eaca44752a1854523b8af46a5b0ceb
* │       ├── 9483f5eb9133c353cef636ef9fcc29e2c7bf658881574211ee142c93c523efaf
* │       ├── a052413e65e025cbefdddff6eeae91161de17ffec16d3a741dd9b7c33d392435
* │       ├── a2598161e1efff623de6128ad8aafba9da0300b6f86e8c951e616bd19f0a572b
* │       ├── a375f98aa21377ed0c59b4c7121ac93763157e39d8235fb5ce77f88dee0e2ee4
* │       ├── a650a90c1b505989b7e81bfb310d7e2013a380ab26f99622de158c58b1d0fbbf
* │       ├── ac7b01e01de0dc289cd649aa5072243f2036bd8d2d0152b6d9874c2ccaaf1e5d
* │       ├── b65bcba449d74e4395421aeb4012c9e509acb5e8153ff3dc9f01fd97a5cc2711
* │       ├── b66919a18322aa4ce2ad47d149b7fe38063cd3cfa2e4062cd1a01ad6b3e...