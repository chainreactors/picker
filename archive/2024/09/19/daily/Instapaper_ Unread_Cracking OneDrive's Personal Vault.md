---
title: Cracking OneDrive's Personal Vault
url: https://malwaremaloney.blogspot.com/2024/09/cracking-onedrives-personal-vault.html
source: Instapaper: Unread
date: 2024-09-19
fetch_date: 2025-10-06T18:28:16.171046
---

# Cracking OneDrive's Personal Vault

[![MALoney (It's in the name)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFONMYzjaTaf0PMebgsLM2EgUZ1tLRqAAASIGtbHMoC0Lg8n676906qdGcFww5mXGQRtu3Cg4j3a8uB5oYQMljPSjjopnUdxLDQFxeSdleqk_TvvwAk1rBaBd-UfxK-W5caERP14HExgw/s1600/9-30-2016+6-41-54+AM.png)](https://malwaremaloney.blogspot.com/)

## Pages

* [Home](https://malwaremaloney.blogspot.com/)
* [All Things Symantec](https://malwaremaloney.blogspot.com/p/all-things-symantec.html)
* [All Things OneDrive](https://malwaremaloney.blogspot.com/p/all-things-onedrive.html)
* [Tools](https://malwaremaloney.blogspot.com/p/tools.html)

## Thursday, September 5, 2024

### Cracking OneDrive's Personal Vault

Sometimes in digital forensics there is a need to gain access to encrypted data sources. This can come in many forms including zip files, TrueCrypt/VeraCrypt, KeePass and BitLocker. OneDrive's Personal Vault is no exception. It is important to gain access to these encrypted containers because they can contain information that is important to our investigation.

## What is Personal Vault?

According to Microsoft, "Personal Vault is a protected area in OneDrive where you can store your most important or sensitive files and photos without sacrificing the convenience of anywhere access." Personal Vault adds an extra layer of security by using Two-Factor Authentication (2FA). When accessed form the Windows client, Personal Vault is stored on the system in a BitLocker encrypted vhdx. It should be noted that Personal Vault is only available for OneDrive Personal.

## Digging Deeper

What had caught my eye was that Microsoft is storing the data on a Windows device in a BitLocker encrypted vhdx. So where is this file located? The vhdx file is stored in a hidden folder at the root of the system drive. `c:\OneDriveTemp\<SID>\<GUID>.vhdx`

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVfY2njSAo_t841bNHu15gOm1oxNdDvD0Q7hXpl1J95lzKJL1eGNdv4d3JdT1xs_ZePufdjj6Udf8hF88EDCKFeaSsgPwuOhG7RsrhH3KPk35wWlRwpRK6fijGjKNDHFy3a2inPIRp6L8heBPUSDsYf8wInd9N8RoyH6TYFC9rWNJqYg2VfEY6FFncNTU/s600/odt.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVfY2njSAo_t841bNHu15gOm1oxNdDvD0Q7hXpl1J95lzKJL1eGNdv4d3JdT1xs_ZePufdjj6Udf8hF88EDCKFeaSsgPwuOhG7RsrhH3KPk35wWlRwpRK6fijGjKNDHFy3a2inPIRp6L8heBPUSDsYf8wInd9N8RoyH6TYFC9rWNJqYg2VfEY6FFncNTU/s537/odt.png)

So now that we found the vhdx file, what can we do with it? We know it's protected by BitLocker so let's see what we can find out. The first thing I did was mount the vhdx and assign it a drive letter. This way, I could work with manage-bde to find out more information about the disk.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW8A6LgZErExmfTJgGqSo4PEyYBwKt56Zxn0QjAJ_omy3skDMry-CErerYJXhAtp6LsOWtZJ18UevSLY6uPhX6yy5wLB3dKG5CRvGwiIgmhdfmJC5wJq608vRvngPBfp5eVQEvHG6_I1uJkvdakA76fd875bpf6VCuE8Hk5s_KBjoLMX8P9P5L5PbYE2I/s600/locked.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW8A6LgZErExmfTJgGqSo4PEyYBwKt56Zxn0QjAJ_omy3skDMry-CErerYJXhAtp6LsOWtZJ18UevSLY6uPhX6yy5wLB3dKG5CRvGwiIgmhdfmJC5wJq608vRvngPBfp5eVQEvHG6_I1uJkvdakA76fd875bpf6VCuE8Hk5s_KBjoLMX8P9P5L5PbYE2I/s608/locked.png)

Now we can open up an administrative command prompt and start investigating the drive. The first command I used was `manage-bde -status`. This command provides information about BitLocker-capable volumes. This is the information for our Personal Vault.

```
Volume F: [Label Unknown]
[Data Volume]

    Size:                 Unknown GB
    BitLocker Version:    2.0
    Conversion Status:    Unknown
    Percentage Encrypted: Unknown%
    Encryption Method:    XTS-AES 128
    Protection Status:    Unknown
    Lock Status:          Locked
    Identification Field: Unknown
    Automatic Unlock:     Disabled
    Key Protectors:
        External Key
```

Interesting! So, it appears the volume is protected by an external key. Let's take a closer look at this with the following command `manage-bde -protectors -get f:`. And our results look like this:

```
BitLocker Drive Encryption: Configuration Tool version 10.0.19041
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

Volume F: [Label Unknown]
All Key Protectors

   External Key:
     ID: {08F750D7-0483-4F0E-847B-174119BD2896}
     External Key File Name:
       08F750D7-0483-4F0E-847B-174119BD2896.BEK
```

Let's see if we can get this external key.

```
manage-bde -protectors -get f: -sek d:\Projects\PersonalVaultBEK
BitLocker Drive Encryption: Configuration Tool version 10.0.19041
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

ERROR: The operation cannot be performed because the volume is locked.
```

Seems we hit a road block. We cannot save the key because the volume is locked.

## Looking at it from an Unlocked Perspective

The next thing we will try is to unassign the drive letter, dismount and unlock the Personal Vault with OneDrive.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKdMN6OaFQKLg8ZRTQAb_kA_h4Y32xofTc2xPF9g9vSvEV1DN5NXfNXwUZvbJBukoCMhcj1e7P335R2S-ZagVlXdKKKMgOYI28JUa44Es2jbDCp4Xx2k37dfORqLWIO2gnZh8ajvzSvglQlkAzBlqpqeFmNux1GUNZJ721JTqWKfwuz5Sm7658b-5tD44/s400/unlock_vault.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKdMN6OaFQKLg8ZRTQAb_kA_h4Y32xofTc2xPF9g9vSvEV1DN5NXfNXwUZvbJBukoCMhcj1e7P335R2S-ZagVlXdKKKMgOYI28JUa44Es2jbDCp4Xx2k37dfORqLWIO2gnZh8ajvzSvglQlkAzBlqpqeFmNux1GUNZJ721JTqWKfwuz5Sm7658b-5tD44/s353/unlock_vault.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5bAgBuak-ozrD6XHWE0_ktvzgRLmeSIQFfkH9hA9R6U_Npv0G02lqbKUf4m0SzWwuB0UFEJoKlsZL1Dbh4W_E0OalOuDYlp8FybbaFUFVgl1OGAlkI_gTvlyfa0X9Z-l8MsrxzpZ9wej7aKm1TSrgJKlGo15Sg21xKPJ85PCwerZo_dNsVLL6EMFJWU4/s400/2fa.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5bAgBuak-ozrD6XHWE0_ktvzgRLmeSIQFfkH9hA9R6U_Npv0G02lqbKUf4m0SzWwuB0UFEJoKlsZL1Dbh4W_E0OalOuDYlp8FybbaFUFVgl1OGAlkI_gTvlyfa0X9Z-l8MsrxzpZ9wej7aKm1TSrgJKlGo15Sg21xKPJ85PCwerZo_dNsVLL6EMFJWU4/s478/2fa.png)

So now the Personal Vault is unlocked. What's interesting is that there is not a drive letter associated with the Personal Vault. Inside our OneDrive folder, there is a Personal Vault.lnk file. When the vault is locked, double clicking it will run through the steps of unlocking the vault. After the vault is unlocked, double clicking it will bring us to the vault. We'll take a look at the lnk file to see how the vhdx is being referenced.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsODxEmOFBdHYxEjtFyA1pAYX79Z5H9lJ0r7uXqyraddkwqo3rIeRhRFi3agSyxMugDNkARP6RC60o-YkI-43opC-m7K3_fHYg3EHVrHV2c49SPo85s64hxynjYsG9pFad3uDKC3ps4-9_IjxC85Yz2lH2qJDU0BtgAPEd-ERY7mPKlYgmB02T7uMCvEM/s600/dir.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsODxEmOFBdHYxEjtFyA1pAYX79Z5H9lJ0r7uXqyraddkwqo3rIeRhRFi3agSyxMugDNkARP6RC60o-YkI-43opC-m7K3_fHYg3EHVrHV2c49SPo85s64hxynjYsG9pFad3uDKC3ps4-9_IjxC85Yz2lH2qJDU0BtgAPEd-ERY7mPKlYgmB02T7uMCvEM/s598/dir.png)

Here is the output from LECmd.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8s-wPqXQz-yQupvqKgRLFYn84aYeH6sv3awckENa_JoWPFYd8GDQHH5VEi7plZBg5B31rpdj11liYJ0XBBbsQZqrfZqHCoqf3NJGCWe8C0i0GdnfOqcgXrSWshbAaZZkQcU2DXBNnZWg7Oa0QzlOKNkNppv4b1hEAlEuzfRE-G40BS4a3Xe0AN40FFJU/s600/lecmd2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8s-wPqXQz-yQupvqKgRLFYn84aYeH6sv3awckENa_JoWPFYd8GDQHH5VEi7plZBg5B31rpdj11liYJ0XBBbsQZqrfZqHCoqf3NJGCWe8C0i0GdnfOqcgXrSWshbAaZZkQcU2DXBNnZWg7Oa0QzlOKNkNppv4b1hEAlEuzfRE-G40BS4a3Xe0AN40FFJU/s511/lecmd2.png)

The lnk file is pointing to a Personal Vault folder in my OneDrive. When I ran a directory listing this folder was not present. This is because the folder is hidden. If we run dir again, looking for hidden files/folders, we can see that the folder is actually a junction.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjivjV2Q-dvOg0a-mXmM9Vnq3jI1orOLVgCbJN65qV9ypet65GqwWFx2hy0QMpSikzjGipEhSq5LeOedF0m08hvnhi3iOP5oFIq5L9xY3EG_T8FC8EYb...