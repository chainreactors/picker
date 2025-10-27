---
title: Web Browser Stored Credentials
url: https://pentestlab.blog/2024/08/20/web-browser-stored-credentials/
source: Penetration Testing Lab
date: 2024-08-21
fetch_date: 2025-10-06T18:02:32.032977
---

# Web Browser Stored Credentials

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [August 20, 2024August 19, 2024](https://pentestlab.blog/2024/08/20/web-browser-stored-credentials/)

# Web Browser Stored Credentials

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Credential Access](https://pentestlab.blog/category/red-team/credential-access/).[Leave a Comment on Web Browser Stored Credentials](https://pentestlab.blog/2024/08/20/web-browser-stored-credentials/#respond)

Microsoft introduced Data Protection Application Programming Interface (DPAPI) in Windows environments as a method to encrypt and decrypt sensitive data such as credentials using the *CryptProtectData* and *CryptUnprotectData* functions. Browsers such as Chrome and Edge utilize DPAPI to encrypt credentials prior to storage. The master key is stored locally and can be decrypted with the password of the user, which then is used to decrypt DPAPI data blobs.

In the world of red team operations, locations which credentials are stored are always a target as it will allow access to other applications or lateral movement. Organizations which are utilizing Microsoft Edge or Google Chrome for storage the credentials of their users are vulnerable due to the abuse of CryptUnprotectData API ([T1555.003](https://attack.mitre.org/techniques/T1555/003/)). It should be noted that reading credentials stored in browsers doesn’t require any form of elevation and it is challenging for defensive teams to detect due to the high volume of events which are generated in case of monitoring.

Master keys are located in the following path and by default are not visible as these are classified as protected operating system files.

```
C:\users\<user>\appdata\roaming\microsoft\protect\<SID>\<MasterKey>
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-master-keys.png?w=939)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-master-keys.png)

User Master Keys

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-master-keys-unhide.png?w=993)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-master-keys-unhide.png)

Mimikatz was the first tool that interacted with DPAPI, and has specific modules to perform decryption operations. However, the Mimikatz encrypted key parser is broken and therefore it can no longer be used to decrypt DPAPI blobs as it fails with a message of *No Alg and/or key handle*. Instead of using Mimikatz, it is feasible to harvest the encrypted key from “*Local State*” by executing the following command from a PowerShell console:

```
(gc "$env:LOCALAPPDATA\Google\Chrome\User Data\Local State" | ConvertFrom-Json).os_crypt.encrypted_key
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-local-state-encrypted-key.png?w=838)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-local-state-encrypted-key.png)

Local State – Encrypted Key

The encrypted key can be ingested in the Mimikatz *dpapi::chrome* module to decrypt the contents of “*Login Data*“.

```
dpapi::chrome /in:"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data" /encryptedkey:[EncryptedKey] /unprotect
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-dpapi-decrypt.png?w=963)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-dpapi-decrypt.png)

Mimikatz – DPAPI Decrypt

[SharpDPAPI](https://github.com/GhostPack/SharpDPAPI) is a C# port of the Mimikatz DPAPI functionality which enables in-memory based execution. Master keys can be retrieved by executing the following command:

```
dotnet inline-execute SharpDPAPI.exe masterkeys /rpc
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-sharpdpapi-user-master-keys.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-sharpdpapi-user-master-keys.png)

ShaprDPAPI – User Master Keys

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-guid-identifier-and-decryption-keys.png?w=959)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-guid-identifier-and-decryption-keys.png)

SharpDPAPI – GUID & Decryption Keys

[SharpChrome](https://github.com/GhostPack/SharpDPAPI/) is part of the SharpDPAPI and targets sensitive information stored in Chromium based browsers such as Chrome, Edge and Brave. The tool will attempt to read and decrypt the AES key from the “*Local State*” file using the cryptographic function BCrypt. The API *CryptUnprotectData()* is used to decrypt passwords stored in browsers.

```
dotnet inline-execute SharpChrome logins
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-sharpchrome.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-sharpchrome.png)

SharpChrome – DPAPI

An alternative tool called [CredentialKatz](https://github.com/Meckazin/ChromeKatz) implements a different method as credentials are dumped directly from the credential manager of Chrome or Edge. This method is more evasive as it attempts to inject into an existing browser process and read credentials and doesn’t utilize DPAPI for decryption. Offline parsing of credentials is also supported via a minidump file. CredentialKatz harvest passwords from credential manager in plain-text by using the *PasswordReuseDetectorImpl* class.

```
CredentialKatz.exe
```

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-credentialkatz.png?w=808)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-credentialkatz.png)

CredentialKatz

## Domain Backup Key

In the event that domain administrator access has been achieved the DPAPI backup key can be retrieved from the domain controller to decrypt master keys from any user in the domain. The backup key is stored in the following Active Directory location:

[![](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-dpapi-backupkey.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/08/web-browser-stored-credentials-dpapi-backupkey.png)

DPAPI – Backup Key

Mimikatz support remote dumping of the backup key by executing the following command:

```
lsadump::backupkeys /system:dc.red.lab /export
```

[![](https://pentestlab.blog/wp-content/uploads/2...