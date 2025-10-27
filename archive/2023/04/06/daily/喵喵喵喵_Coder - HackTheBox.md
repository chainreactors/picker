---
title: Coder - HackTheBox
url: https://darkwing.moe/2023/04/05/Coder-HackTheBox/
source: 喵喵喵喵
date: 2023-04-06
fetch_date: 2025-10-04T11:29:03.968062
---

# Coder - HackTheBox

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

Coder - HackTheBox

# Coder - HackTheBox

##### 2023-04-05

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80/443](#80-443)
   2. [2.2. 445](#445)
3. [3. SMB](#SMB)
   1. [3.1. Development](#Development)
4. [4. Encrypter.exe](#Encrypter-exe)
   1. [4.1. keepass](#keepass)
   2. [4.2. Decrypt.cs](#Decrypt-cs)
   3. [4.3. Authenticator backup codes](#Authenticator-backup-codes)
5. [5. teamcity OTP](#teamcity-OTP)
   1. [5.1. 非预期 爆破OTP](#非预期-爆破OTP)
   2. [5.2. brute.py](#brute-py)
   3. [5.3. 预期方法](#预期方法)
6. [6. teamcity getshell](#teamcity-getshell)
7. [7. e.black 信息](#e-black-信息)
   1. [7.1. enc.txt](#enc-txt)
8. [8. user flag](#user-flag)
9. [9. 提权信息](#提权信息)
   1. [9.1. ADCS](#ADCS)
10. [10. 提权 & root flag](#提权-amp-root-flag)
    1. [10.1. root flag](#root-flag)
11. [11. 参考资料](#参考资料)

# Coder - HackTheBox

2023-04-05

# 基本信息

* <https://app.hackthebox.com/machines/Coder>
* 10.10.11.207

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040401.jpg)

# 端口扫描

80，443和常规域端口：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.207 Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-04 14:41 CST Nmap scan report for 10.10.11.207 Host is up (0.083s latency). Not shown: 987 closed tcp ports (conn-refused) PORT     STATE SERVICE       VERSION 53/tcp   open  domain        Simple DNS Plus 80/tcp   open  http          Microsoft IIS httpd 10.0 | http-methods: |_  Potentially risky methods: TRACE |_http-server-header: Microsoft-IIS/10.0 |_http-title: IIS Windows Server 88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-04-04 08:44:05Z) 135/tcp  open  msrpc         Microsoft Windows RPC 139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn 389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: coder.htb0., Site: Default-First-Site-Name) |_ssl-date: 2023-04-04T08:44:50+00:00; +2h01m50s from scanner time. | ssl-cert: Subject: commonName=dc01.coder.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc01.coder.htb | Not valid before: 2022-06-30T04:24:26 |_Not valid after:  2023-06-30T04:24:26 443/tcp  open  ssl/http      Microsoft IIS httpd 10.0 |_ssl-date: 2023-04-04T08:44:50+00:00; +2h01m50s from scanner time. | tls-alpn: |_  http/1.1 |_http-server-header: Microsoft-IIS/10.0 |_http-title: IIS Windows Server | http-methods: |_  Potentially risky methods: TRACE | ssl-cert: Subject: commonName=default-ssl/organizationName=HTB/stateOrProvinceName=CA/countryName=US | Not valid before: 2022-11-04T17:25:43 |_Not valid after:  2032-11-01T17:25:43 445/tcp  open  microsoft-ds? 464/tcp  open  kpasswd5? 593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0 636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: coder.htb0., Site: Default-First-Site-Name) |_ssl-date: 2023-04-04T08:44:50+00:00; +2h01m50s from scanner time. | ssl-cert: Subject: commonName=dc01.coder.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc01.coder.htb | Not valid before: 2022-06-30T04:24:26 |_Not valid after:  2023-06-30T04:24:26 3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: coder.htb0., Site: Default-First-Site-Name) |_ssl-date: 2023-04-04T08:44:50+00:00; +2h01m50s from scanner time. | ssl-cert: Subject: commonName=dc01.coder.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc01.coder.htb | Not valid before: 2022-06-30T04:24:26 |_Not valid after:  2023-06-30T04:24:26 3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: coder.htb0., Site: Default-First-Site-Name) |_ssl-date: 2023-04-04T08:44:50+00:00; +2h01m50s from scanner time. | ssl-cert: Subject: commonName=dc01.coder.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc01.coder.htb | Not valid before: 2022-06-30T04:24:26 |_Not valid after:  2023-06-30T04:24:26 Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows  Host script results: | smb2-security-mode: |   311: |_    Message signing enabled and required | smb2-time: |   date: 2023-04-04T08:44:43 |_  start_date: N/A |_clock-skew: mean: 2h01m49s, deviation: 0s, median: 2h01m49s  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 75.53 seconds ``` |

## 80/443

直接访问是IIS默认页面：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040402.jpg)

## 445

smb可以匿名访问：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040403.jpg)

# SMB

## Development

Development里发现一个加密文件和对应的加密程序，还发现有adcs相关内容：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040404.jpg)

下载下来分析：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` smb: \Temporary Projects\> mask "" smb: \Temporary Projects\> recurse ON smb: \Temporary Projects\> prompt OFF smb: \Temporary Projects\> cd .. smb: \> mget * ``` |

# Encrypter.exe

.net程序，直接反编译分析代码,根据代码可以知道是根据时间戳作为随机数种子生成key和iv，使用AES进行加密：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040405.jpg)

所以直接根据文件时间得到当时加密的时间戳(注意时差)，对应编写解密程序,解密得到一个7z压缩包：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040406.jpg)

## keepass

解压得到一个key和一个keepass密码库，直接使用key解密即可得到保存的一些信息：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` Authenticator backup codes xxx Teamcity s.blade veh5nUSZFFoqz9CrrhSeuwhA https://teamcity-dev.coder.htb O365 s.blade@coder.htb AmcwNO60Zg3vca3o0HDrTC6D ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040407.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023040408.jpg)

## Decrypt.cs

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` | ``` using System.IO; using System; using System.Security.Cryptography;  public class HelloWorld {     public static void Main(string[] args)     {         FileInfo fileInfo = new FileInfo("s.blade.enc");         string destFile = Path.ChangeExtension(fileInfo.Name, ".dec");         long value = 1668205028;         Random random = new Random(Convert.ToInt32(value));         byte[] array = new byte[16];         random.NextBytes(array);         byte[] array2 = new byte[32];         random.NextBytes(array2);         byte[] array3 = DecryptFile(fileInfo.Name, destFile, array2, array);     }     private static byte[] DecryptFile(string sourceFile, string destFile, byte[] Key, byte[] IV)     {         using (RijndaelManaged rijndaelManaged = new RijndaelManaged())         {             FileStream stream = new FileStream(sourceFile, FileMode.Open);             ICryptoTransform transform = rijndaelManaged.CreateDecryptor(Key, IV);             CryptoStream cryptoStream = new CryptoStream(stream, transform, CryptoStreamMode.Read);             FileStream fileStream = new FileStream(destFile, FileMode.Create);             byte[] array = new byte[1024];             int count;             while ((count = cryptoStream.Read(array, 0, array.Length)) != 0)             {                 fileStream.Write(array, 0, count);             }         }         return null;     } } ``` |

## Authenticator backup codes

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` {   "6132e897-44a2-4d14-92d2-12954724e83f": {     "encrypted": true,     "hash": "6132e897-44a2-4d14-92d2-12954724e83f",     "index": 1,     "type": "totp",     "secret": "U2FsdGVk...