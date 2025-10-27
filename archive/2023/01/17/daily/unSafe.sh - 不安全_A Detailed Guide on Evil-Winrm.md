---
title: A Detailed Guide on Evil-Winrm
url: https://buaq.net/go-145808.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:01:57.987483
---

# A Detailed Guide on Evil-Winrm

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2e53578ef3ccb1a22fa82ef9badce801.jpg)

A Detailed Guide on Evil-Winrm

BackgroundEvil-winrm tool is originally written by the team Hackplayers. The purpo
*2023-1-16 23:39:59
Author: [www.hackingarticles.in(查看原文)](/jump-145808.htm)
阅读量:36
收藏*

---

### Background

Evil-winrm tool is originally written by the team Hackplayers. The purpose of this tool is to make penetration testing easy as possible especially in the Microsoft Windows environment. Evil-winrm works with PowerShell remoting protocol (PSRP). System and network administrators often use Windows Remote Management protocol to upload, edit and upload. WinRM is a SOAP-based, and firewall-friendly protocol that works with HTTP transport over the default HTTP port 5985. For more information about PowerShell remoting, consider visiting Microsoft’s official site.

**<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.3>**

### Table of Content

* Introduction to Evil-winrm
* Winrm Service Discovery
* Evil-winrm Help – List Available Features
* Login With Plain Texted Password
* Login with Plain Texted Password – SSL Enabled
* Login with NTLM Hash -Pass The Hash Attack
* Load Powershell Script
* Store logs with Evil-winrm
* Disable Remote Path Completion
* Disable Coloured Interface
* Run Executables File
* Service Enumeration with Evil-winrm
* File Transfer with Evil-winrm
* Use Evil-winrm From Docker
* Login with the key using Evil-winrm
* Conclusion

### Introduction to Evil-winrm

Evil-winrm open-sourced tool written in ruby language making post exploitation easy as possible. This tool comes with many cool features which include remote login with plain texted password, SSL encrypted login, login with NTLM hash, login with keys, file transfer, logs store etc. The authors of the tool keep updating this tool and adding many new features which made Internal assessment easier. Using evil-winrm, we get a PowerShell session of the remote host. This tool comes with all modern Kali Linux but if you wish to download then you can download it from its official git repository.

Download Link: **<https://github.com/Hackplayers/evil-winrm>**

### Winrm Service Discovery

As we have discussed earlier that the evil-winrm tool is used if the Winrm service is enabled in the remote host. To confirm, we can look for the two default winrm service ports 5895 and 5896 open or not using nmap. From the nmap result, we found that winrm service is enabled so we can use evil-winrm to log in and perform other tasks which we are going to explore in the lateral phases.

```
nmap -p 5985,5986 192.168.1.19
```

### ![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX4BH15fcVaS2fdbUP9yAHYbe3eXmcq9k3TbJKV2a5wxi7UoVhBauzHA4jytwcDp8Uon-C8N3LY_vwUF3HPvAxWq_R6Z6dzeLpIlCaLDrNyxE8U8u_x1LjgU_jyUKyGmXNWppSe26DTMj6eDZG9AgeVYC2i1H93WXvs7VcmYAjaT4S9kuy0FoxzK04lg/s16000/1.png?w=640&ssl=1)

### Evil-winrm Help – List Available Features

Many penetration testers and the CTF players have used this tool quite often during internal assessments but still many of us are unaware of the tool’s extra features which can make our assessment much easier than ever.  To list the all-available cool features of the evil-winrm, we can simply use **-h** flag and that will list all the help commands with descriptions.  We are going to cover as much as possible in this article and encourage everyone to play with other features as well.

```
evil-winrm -h
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ-4N3NZHMJBIWWT0L_lVGyFOo_DiW7Nr3Ls6pFNVxAraW_jB6xVTZdLGhj1xBtEE-9ewTcxXjIg6Lfmznte1mCgqIqY7QsBF4Cmg7ySzMhBlygKghOKBFsDXja-lCfbMOGoYZVmuyQoeAJ0JclL4_9pbCkieAKhKXs-fbHV-t1yfkytreQgAfCkHNnA/s16000/2.png?w=640&ssl=1)

### Login With Plain Texted Password

Suppose we have obtained a plain texted password during the enumeration phase, and we noticed that winrm service is enabled in the remote host. Then we can take a remote session on the target system using evil-winrm by issuing the IP address of the remote host with **-i** flag, username with **-u** flag and the password with **-p** flag. In the below picture, we can see that it has established a remote PowerShell session.

```
evil-winrm -i 192.168.1.19 -u administrator -p [email protected]
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe_SzAv7Joh2me4Vdofre2DZPcSfjJo-DNbmszEL9vXdasM2jfdHpSirMRmlulEYgc4epMngwA0k5lIjIXGkrMIprSC6rDyrvLHEAMXR95lmpY9ny3D1uYITo-0j-R1q-lrR4ikpfMaIw6khGe1-SXuZNFAn3kghszaGNMjK6FkWWYnkyd7thuzBmaGw/s16000/4.png?w=640&ssl=1)

### Login with Plain Texted Password – SSL Enabled

As we have mentioned earlier that the winrm service transports traffic over the HTTP protocol then we can use Secure Socket Layer (SSL) feature to make the connection secure. Once we enable the SSL feature then our data will be delivered over an encrypted secure socket layer. With evil-winrm, we can achieve the objective using **-S** flag along with our previous command that we used to establish a connection to the remote host.

```
evil-winrm -i 192.168.1.19 -u administrator -p [email protected] -S
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOAfaCC9m4qMV4FjurV12Qfo3U3OHMA7ngvltegNDXW2tBLZYfh7CwNm3FwGjgpEgYBpPR1hFkx5RWNeIndABKy6Ze6HVZkli-InYrgIQy2y1668xASOnJIXqkltEY51pU9C9ym41NZHI-AaG9PPSEOUCD1pieoKzprAHvmiHAF4u3F4ME2Nfk7-0xFQ/s16000/5.png?w=640&ssl=1)

### Login with NTLM Hash -Pass The Hash Attack

During the internal assessment or solving any CTF related to windows privilege escalation and Active Directory exploitation, we often get NTLM hash by using our exploits and the attacks. If we are in the windows environment, we can utilise evil-winrm to establish a PowerShell session by performing pass the hash attack where we issue hash as a password instead of using a plain texted password. Apart from that, this attack also supports other protocols as well. We can pass the hash using **-H** flag along with the command we used earlier replacing the password section with the hash. More detailed guide about the pass-the-hash attack is available in the below link:

**<https://www.hackingarticles.in/lateral-movement-pass-the-hash-attack/>**

```
evil-winrm -i 192.168.1.19 -u administrator -H 32196B56FFE6F45E294117B91A83BF38
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUT9NJqZ1mSnsVg7Fh8R1r_9t0PP5nZPzTf1ya17cXkZJKVTjgk4a9ixFLVKHkH9yfNnCcrpgS1aGk1S7Om46RPCpiGKqd2CjRtorV3Uiwyk0TYfj4MvKDS2hu0_qYOszrP7cfcwxmDOJFF5hy-1_n33pQ6weSm4HAAkanY6navDEYprIoZH8MSVghug/s16000/6.png?w=640&ssl=1)

### Load Powershell Script

Evil-winrm also comes up with a feature which allows us to use scripts from our base machine. We can directly load scripts directly into the memory using **-s** flag along with the script file path where we have stored scripts I our local machine. Furthermore, it also comes up with AMSI feature which we often require before importing any script. In the below example, we are bypassing AMSI then directly calling Invoke-Mimiktz.ps1 script from our system to the target machine and loading it into the memory. After that, we can use any mimikatz command. For demonstration purpose, here we have dumped credentials from the cache. After dumping credentials, we can perform pass the hash attack with obtained NTLM hash again. Follow the steps below to reproduce the attack with evil-winrm.

**<https://github.com/clymb3r/PowerShell/blob/master/Invoke-Mimikatz/Invoke-Mimikatz.ps1>**

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/...