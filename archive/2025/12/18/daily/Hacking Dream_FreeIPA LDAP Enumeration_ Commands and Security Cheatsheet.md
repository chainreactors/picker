---
title: FreeIPA LDAP Enumeration: Commands and Security Cheatsheet
url: https://www.hackingdream.net/2025/12/freeipa-ldap-enumeration-commands-and-cheatsheet.html
source: Hacking Dream
date: 2025-12-18
fetch_date: 2025-12-19T03:22:14.901689
---

# FreeIPA LDAP Enumeration: Commands and Security Cheatsheet

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### FreeIPA LDAP Enumeration: Commands and Security Cheatsheet

[December 18, 2025](https://www.hackingdream.net/2025/12/freeipa-ldap-enumeration-commands-and-cheatsheet.html "permanent link")

FreeIPA LDAP Enumeration: Commands and Security Cheatsheet

# FreeIPA LDAP Enumeration: Commands and Security Cheatsheet

*Updated on December 18, 2025*

Table of Contents

* [1. Privileged Accounts & Groups](#priority-1)
* [2. SUDO Rules (Critical for Privilege Escalation)](#priority-2)
* [3. HBAC Policies (Access Control Rules)](#priority-3)
* [4. Hosts & Services](#priority-4)
* [5. SSH Public Keys (Lateral Movement)](#priority-5)
* [6. Password & Kerberos Policies](#priority-6)
* [7. Certificate Authority & Profiles](#priority-7)
* [8. DNS Records](#priority-8)
* [9. Active Directory Trusts](#priority-9)
* [10. Topology & Replication](#priority-10)
* [11. Automation & Vaults](#priority-11)
* [12. Automated Full Dump](#automated-dump)
* [13. Post-Extraction Analysis](#post-analysis)

Understanding **FreeIPA LDAP enumeration** is critical for both penetration testers and system administrators to identify severe security misconfigurations.

## Priority 1: Privileged Accounts & Groups

Identifying administrative groups is the first step in mapping the privilege hierarchy within a FreeIPA environment.

```
# 1. Dump all groups with memberships (identify admin groups)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=groups,cn=accounts,dc=corp,dc=com" "(objectClass=posixGroup)" cn gidNumber member memberUid description > groups.ldif

# 2. Find admin-level accounts (admins group)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=admins,cn=groups,cn=accounts,dc=corp,dc=com" "(objectClass=*)" member memberUid

# 3. Extract trust admins (if AD trust exists)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=trust admins,cn=groups,cn=accounts,dc=corp,dc=com" "(objectClass=*)" member

# 4. Enumerate users with elevated privileges
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=users,cn=accounts,dc=corp,dc=com" "(memberOf=cn=admins,cn=groups,cn=accounts,dc=corp,dc=com)" uid uidNumber memberOf
```

**MITRE ATT&CK:** `T1069.002` (Permission Groups Discovery: Domain Groups)

## Priority 2: SUDO Rules (Critical for Privilege Escalation)

Leveraging **FreeIPA LDAP enumeration** to find SUDO rules often reveals direct paths to root access on enrolled hosts.

```
# 5. Extract ALL sudo rules
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=sudorules,cn=sudo,dc=corp,dc=com" "(objectClass=ipaSudoRule)" cn ipaEnabledFlag memberHost memberUser sudoCommand sudoRunAsUser sudoRunAsGroup sudoOption > sudo_rules.ldif

# 6. Find wildcard sudo rules (ALL commands)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=sudorules,cn=sudo,dc=corp,dc=com" "(sudoCommand=*ALL*)" cn memberHost memberUser

# 7. Identify NOPASSWD sudo rules (instant privilege escalation)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=sudorules,cn=sudo,dc=corp,dc=com" "(sudoOption=*NOPASSWD*)" cn memberHost memberUser sudoCommand
```

**MITRE ATT&CK:** `T1548.003` (Abuse Elevation Control Mechanism: Sudo and Sudo Caching)

## Priority 3: HBAC Policies (Access Control Rules)

Host-Based Access Control (HBAC) defines which users can access specific services on specific hosts.

```
# 8. Dump all Host-Based Access Control rules
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=hbac,dc=corp,dc=com" "(objectClass=ipaHBACRule)" cn ipaEnabledFlag memberUser memberHost memberService serviceCategory hostCategory userCategory > hbac_rules.ldif

# 9. Find permissive HBAC rules (allow all users/hosts)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=hbac,dc=corp,dc=com" "(&(objectClass=ipaHBACRule)(|(userCategory=all)(hostCategory=all)))" cn memberService

# 10. Extract HBAC services (SSH, login, gdm, etc.)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=hbacservices,cn=hbac,dc=corp,dc=com" "(objectClass=ipaHBACService)" cn description
```

**MITRE ATT&CK:** `T1078.002` (Valid Accounts: Domain Accounts)

## Priority 4: Hosts & Services

Enumerating hosts and service principals helps identify targets for lateral movement and Kerberoasting.

```
# 11. Enumerate all enrolled hosts (servers/workstations)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=computers,cn=accounts,dc=corp,dc=com" "(objectClass=ipaHost)" fqdn description macAddress managedBy enrolledBy ipaClientVersion > hosts.ldif

# 12. Extract service principals (Kerberos services - Kerberoasting targets)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=services,cn=accounts,dc=corp,dc=com" "(krbPrincipalName=*)" krbPrincipalName krbCanonicalName managedBy description > services.ldif

# 13. Find HTTP service principals (web applications)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=services,cn=accounts,dc=corp,dc=com" "(krbPrincipalName=HTTP/*)" krbPrincipalName managedBy

# 14. Dump hostgroups (server groupings)
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=hostgroups,cn=accounts,dc=corp,dc=com" "(objectClass=ipaHostGroup)" cn member memberHost description
```

**MITRE ATT&CK:** `T1087.002` (Account Discovery: Domain Account), `T1558.003` (Steal or Forge Kerberos Tickets: Kerberoasting)

## Priority 5: SSH Public Keys (Lateral Movement)

Public keys stored in LDAP can be used to identify users who likely have active SSH access across the domain.

```
# 15. Extract SSH public keys from all user accounts
LDAPTLS_REQCERT=never ldapsearch -LLL -x -H ldaps://ipa-server.com:636 -b "cn=users,cn=accounts,dc=corp,dc=com" "(ipaSSHPubKey=*)" uid ipaSSHPubKey mail > ssh_keys.ldif

# 16. Parse and save SSH keys for offline analysis
grep -A 1 "ipaSSHPubKey:" ssh_keys.ldif | grep -v "^--$" | sed 'N;s/\n/ /' > extracted_ssh_keys.txt
```

**MITRE ATT&CK:** `T1552.004` (Unsecured Credentials: Private Keys)

## Priority 6: Password & Kerberos Policies

Analyzing policies allows attackers to understand lockout thresholds and identify AS-REP Roastable accounts.

```
# 17. Extract password policies (lockout thresholds, complexity)
LDAPTLS_REQCERT=never ...