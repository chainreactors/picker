---
title: Windows Account Passwords: Why and How to Break NTLM Credentials
url: https://buaq.net/go-140313.html
source: unSafe.sh - 不安全
date: 2022-12-17
fetch_date: 2025-10-04T01:46:28.565623
---

# Windows Account Passwords: Why and How to Break NTLM Credentials

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

![](https://8aqnet.cdn.bcebos.com/565d11fe69b1f66d376fdcc502186b5d.jpg)

Windows Account Passwords: Why and How to Break NTLM Credentials

Windows account passwords, or NTLM passwords, are a
*2022-12-16 19:56:45
Author: [blog.elcomsoft.com(查看原文)](/jump-140313.htm)
阅读量:43
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

Windows account passwords, or NTLM passwords, are among the easiest to recover due to their relatively low cryptographic strength. At the same time, NTLM passwords can be used to unlock DPAPI-protected data such as the user’s passwords stored in Web browsers, encrypted chats, EFS-protected files and folders, and a lot more. In this article we argue about prioritizing the recovery of NTLM hashes over any other types of encrypted data.

## What are NTLM hashes?

In Windows, NTLM hashes are used to verify passwords when users sign in to their Windows accounts. Microsoft still uses the NTLM mechanism to store passwords in modern versions of Windows. These passwords are stored in the SAM database, or in the NTDS database on the domain controller. Interestingly, NTLM hashes are faster to break than the much older LM hashes due to the way the algorithm is implemented.

NTLM hashes protect local Windows accounts as well as the newer types of accounts introduced in Windows 8: the [Microsoft Account](https://blog.elcomsoft.com/2016/03/breaking-into-microsoft-account-its-no-google-but-getting-close/) sign-in. Windows caches the password hash and stores it locally on the computer. This allows users to log in to their computer while using it offline. On another hand, this also allows extracting the cached hash file and running an offline attack to recover the original password. The hashed Microsoft Account passwords are stored locally in the SAM database along with the rest of NTLM hashes. Technically, the locally cached Microsoft Accounts passwords are protected with the same NTLM mechanism as other types of cached credentials, which makes them just as easy and as fast to attack as local Windows passwords.

> *In layman’s terms, breaking an NTLM hash reveals the user’s plain-text Windows account or Microsoft account password, allowing the expert to sign in to that user’s computer and extract DPAPI-protected ata.*

**NTLM hashes are poorly salted**. Microsoft uses cryptographic salt to protect LM and NTLM password hashes ([what’s the difference?](https://blog.elcomsoft.com/2022/08/breaking-windows-passwords-lm-ntlm-dcc-and-windows-hello-pin-compared/)). However, the same salt is used to protect all LM and all NTLM passwords, which allows attacking all user accounts that present on a certain computer simultaneously. This only changed in Windows Hello PINs.

The NTLM hashes are among the weakest and fastest to attack. A CPU-only attack already demonstrates very impressive speeds, while employing a mid-range NVIDIA RTX 2070 board allows trying up to 23 billion password combinations per second. Such a speed allows breaking 8-character passwords that consist of an **extended character set** (small and capital letters, numbers, and special characters) in **under 87 hours**. A more typical 8-character password containing only small and capital English letters and numbers (no special characters) can be broken in **under 3 hours**. A more powerful GPU, multiple GPUs, or several computers in a distributed attack can be used to speed up the recovery.

[![](https://blog.elcomsoft.com/wp-content/uploads/2022/08/EDPR_compare_16082022.png)](https://blog.elcomsoft.com/wp-content/uploads/2022/08/EDPR_compare_16082022.png)

## What is DPAPI, and how is it related to NTLM?

Windows uses Data Protection Application Programming Interface (DPAPI) as a transparent way to access encryption keys protecting various system resources. Examples of such DPAPI-protected resources are online forms and authentication credentials (passwords) stored in Microsoft Edge and Google Chrome, EFS (Encrypted File System, or NTFS file encryption) keys, passwords to network shares and FTP resources, and a lot more.

DPAPI transparently protects sensitive information stored in each user’s Windows account. For example, if the user enables file encryption by ticking the “Encrypt contents to secure data” box in the Advanced Properties of a file or folder, the encrypted files will be transparently accessible to the authenticated user, but cannot be accessed when analyzing a disk image.

[![](https://blog.elcomsoft.com/wp-content/uploads/2022/12/efs.png)](https://blog.elcomsoft.com/wp-content/uploads/2022/12/efs.png)

In addition, DPAPI protects authentication credentials cached in Microsoft Edge and Google Chrome browsers. This protection is also transparent; the user does not need to enter any additional password to access these authentication credentials, but such credentials cannot be extracted when analyzing a disk image without an authenticated Windows session.

[![](https://blog.elcomsoft.com/wp-content/uploads/2022/12/edge.png)](https://blog.elcomsoft.com/wp-content/uploads/2022/12/edge.png)

## The “NTLM first” strategy

This strategy prioritizes easily accessible data that can be used to break other passwords or to decrypt data, disregarding its potential value as evidence. In particular, this strategy prioritizes stored passwords (e.g. Web browser password storage, keychain, DPAPI-protected data etc.)

So why do we need the NTML password after all? It’s because of the other things that are protected with it. The users’ passwords stored in Windows Web browsers such as Microsoft Edge and Google Chrome are encrypted with a key protected with Windows DPAPI. Decrypting the key (and accessing stored passwords) requires a Windows account unlock, which in turn means we’ll need to break the NTLM password to sign into the user’s Windows account. NTLM passwords are notoriously fast to recover, which makes them the perfect target.

You’ll need to take several steps to make the best use of the strategy.

1. Analyze unencrypted data for any passwords that can be accessed.
2. Create or update the custom dictionary.
3. Use the custom dictionary to attack the NTLM password.
4. Access DPAPI-protected data (such as browser passwords, SMB passwords etc.) e.g. with [Elcomsoft Internet Password Breaker](https://www.elcomsoft.com/einpb.html)[![](https://blog.elcomsoft.com/wp-content/uploads/2021/06/einpb.png)](https://blog.elcomsoft.com/wp-content/uploads/2021/06/einpb.png)
5. Update custom dictionary.
6. Analyze the dictionary of the user’s passwords. Any repeatable patterns? Shared passwords? Common templates? What kind of mutations would fit the user’s profile?
7. Update custom dictionary with “cleaned”, pattern-based passwords (e.g. for entries such as “Password123” use “password” and medium strength of “Digit” mutations).
8. When attacking files and documents, place the fastest/easiest to break files at the top of the queue. NTLM passwords are among the weakest, and should always make it to the top of the queue.

## Additional information

If you are interested in unlocking DPAPI-protected data, check out the following presentation first:

* [DPAPI exploitation during pentest and password cracking](https://www.synacktiv.com/ressources/univershell_2017_dpapi.pdf)

In addition, we recommend the following articles:

* [DPAPI – Extracting Passwords – HackTricks – Boitatech](https://hacktricks.boitatech.com.br/windows/windows-local-privilege-escalation/dpapi-extracting-passwords)

We offer a tool for extracting DPAPI-protected passwords from all major Web browsers:

* [Elcomsoft Internet Password Breaker | Elcomsof...