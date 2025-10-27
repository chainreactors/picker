---
title: Password Recovery and Data Decryption: Getting Around and About
url: https://buaq.net/go-150566.html
source: unSafe.sh - 不安全
date: 2023-02-23
fetch_date: 2025-10-04T07:49:16.160825
---

# Password Recovery and Data Decryption: Getting Around and About

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Password Recovery and Data Decryption: Getting Around and About

Access to encrypted information can be gained throu
*2023-2-22 19:42:46
Author: [blog.elcomsoft.com(查看原文)](/jump-150566.htm)
阅读量:26
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

Access to encrypted information can be gained through various methods, including live system analysis ([1](https://blog.elcomsoft.com/2022/05/live-system-analysis-extracting-bitlocker-keys/) and [2](https://blog.elcomsoft.com/2020/07/live-system-analysis-discovering-encrypted-disk-volumes/)), using [bootable forensic tools](https://blog.elcomsoft.com/2022/03/simplifying-digital-triage-with-bootable-forensic-tools/), analysis of [sleep/hibernation files](https://blog.elcomsoft.com/2021/09/forensic-implications-of-sleep-hybrid-sleep-hibernation-and-fast-startup-in-windows-10/), and exploiting [TPM vulnerabilities](https://blog.elcomsoft.com/2021/01/understanding-bitlocker-tpm-protection/), with password recovery being the last option on the list. Each method has different resource requirements and should be used in order of least resource-intensive to most time-consuming, with password recovery as the last resort. Familiarize yourself with the different [encryption recovery strategies](https://blog.elcomsoft.com/2019/11/what-is-password-recovery-and-how-it-is-different-from-password-cracking/) and learn about data formats with weak protection or known vulnerabilities.

## Why password recovery is your last resort

When presented encrypted evidence, one’s immediate thought is “I need to break a bunch of passwords”. However, decrypting protected information by recovering the original plain-text password is the most straightforward approach, but also the least efficient one. Since most encryption formats are designed to withstand password attacks with hundreds thousands rounds of hashing, the time required to break even a simple password could be days, months, or years. In real life, the chance of successfully breaking encryption by attacking passwords is low. For example, the authors of [When Encryption Baffles the Police: A Collection of Cases](https://scienceblogs.de/klausis-krypto-kolumne/when-encryption-baffles-the-police-a-collection-of-cases/) describe as many as 55 criminal cases that involved data encryption. In 17 cases, encryption was fully or partially broken, which results in an approximately 30% success rate.

You may be able to improve this success rate by employing alternative techniques to decrypt information other than attacking plain-text passwords. If access to encrypted digital evidence takes precedence over retrieving the plain-text password (which is not always the case, e.g. [Windows Account Passwords: Why and How to Break NTLM Credentials](https://blog.elcomsoft.com/2022/12/windows-account-passwords-why-and-how-to-break-ntlm-credentials/)), a number of more efficient solutions may be available. The recovery methods for accessing protected pose very different resource requirements such as the time spent by the expert to set up the attack, and the time required to carry out the attack. We recommend trying the least resource-intensive methods first and only resorting to more time-consuming methods (such as brute force) when all other options have been exhausted. The following are our preferred recovery methods:

1. Encrypted disks and virtual machines: Live system analysis. This method, if available, enables the retrieval of binary encryption keys and/or imaging of the file system of a mounted disk without the need for lengthy brute-force attacks.
2. Live system analysis: If you have access to an authenticated user session, make the most of it before shutting down the computer. Even if full-disk encryption is not used, some data (such as DPAPI-protected items) will only be accessible when the user signs in with their password. DPAPI-protected items include passwords saved in web browsers (Chrome, Edge, etc.), passwords for network shares, keys, tokens, and certificates.
3. Computer in sleep/hibernation: Analyze page/hibernation files for disk encryption keys (using [Elcomsoft Forensic Disk Decryptor](https://www.elcomsoft.com/efdd.html)). Keep in mind that volatile virtual machine images may also be stored in RAM.
4. Consider using [bootable forensic tools](https://blog.elcomsoft.com/2022/03/simplifying-digital-triage-with-bootable-forensic-tools/) (such as [Elcomsoft System Recovery](https://www.elcomsoft.com/esr.html)) to quickly image built-in storage media and [extract encryption metadata](https://blog.elcomsoft.com/2020/11/elcomsoft-system-recovery-a-swiss-army-knife-of-desktop-forensics/).
5. BitLocker disks: Consider using [TPM vulnerabilities](https://blog.elcomsoft.com/2021/01/understanding-bitlocker-tpm-protection/) to unlock the BitLocker boot drive before removing storage media for imaging.
6. Encrypted disks: Analyze hibernation and page files with Elcomsoft Forensic Disk Decryptor (searching for encryption keys). An authenticated user session is not necessary for this analysis.
7. Some data formats have weak protection or known vulnerabilities. Familiarize yourself with these formats (such as [Microsoft Office](https://blog.elcomsoft.com/2019/10/microsoft-office-encryption-evolution-from-office-97-to-office-2019/) documents saved in legacy formats like .doc/.xls instead of .docx/.xlsx); e.g. [Decrypting Password-Protected DOC and XLS Files in Minutes](https://blog.elcomsoft.com/2022/04/decrypting-password-protected-doc-and-xls-files-in-minutes/).
8. Use the “low hanging fruit” strategy and prioritize files with weak protection.
9. Password recovery. This should only be used as a last resort, but you may have options such as a smart attack and/or custom dictionaries made up of the user’s other passwords (for example, extracted from the keychain/web browsers).

More information:

* [What is Password Recovery and How It Is Different from Password Cracking](https://blog.elcomsoft.com/2019/11/what-is-password-recovery-and-how-it-is-different-from-password-cracking/)
* [A Bootable Flash Drive to Extract Encrypted Volume Keys, Break Full-Disk Encryption](https://blog.elcomsoft.com/2019/04/a-bootable-flash-drive-to-extract-encrypted-volume-keys-break-full-disk-encryption/)
* [How Long Does It Take to Crack Your Password?](https://blog.elcomsoft.com/2017/04/how-long-does-it-take-to-crack-your-password/)
* [How to Break 70% of Passwords in Minutes](https://blog.elcomsoft.com/2017/02/how-to-break-70-of-passwords-in-minutes/)

#### REFERENCES:

![](https://www.elcomsoft.com/images/bicons/edpr.gif)

### Elcomsoft Distributed Password Recovery

Build high-performance clusters for breaking passwords faster. Elcomsoft Distributed Password Recovery offers zero-overhead scalability and supports GPU acceleration for faster recovery. Serving forensic experts and government agencies, data recovery services and corporations, Elcomsoft Distributed Password Recovery is here to break the most complex passwords and strong encryption keys within realistic timeframes.

[Elcomsoft Distributed Password Recovery official web page & downloads »](https://www.elcomsoft.com/edpr.html)

---

文章来源: https://blog.elcomsoft.com/2023/02/password-recovery-and-data-decryption-getting-around-and-about/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)