---
title: facai安全管理工具，发财发财都发财！
url: https://mp.weixin.qq.com/s/cNcx4SYsNop9axXTI_rtXA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:49:10.100242
---

# facai安全管理工具，发财发财都发财！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6ODVwZLx6y24IC5tYDBn9qjWFIgaG3VqTkB9xxg0dF81E1dmxLN8TAiaNb8kfCCCiaWIicDraEuUJvqrVpJAOMkkU12Z0eAtULw3I/0?wx_fmt=jpeg)

# facai安全管理工具，发财发财都发财！

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 发财网安工具，都发财，谁用谁发财，你只负责点点点，其他都交给它。

### 介绍

### github: https://github.com/guimaizi/facai

首先周知现在是ai时代了，为什么做这玩意，ai时代传统安全已经死了，这也是个事实，但是，如之前我公众号文章所写。

在当前地球文明中我们要服务两个客户:

1. 人类
2. AI

因为现在就这两种客户在用，所以我们做软件，要人类和AI都能看得懂，用的了。

Json是个很好的格式，无论是人类还是ai都能读懂，也符合当下AI-Agent的标准。

所以该工具就是基于HTTP请求，并且是json格式的HTTP请求:

```
{  "url": "https://a.molun.com/auth/getAuthCodeInfoByCode",  "headers": {    "accept": "application/json, text/plain, */*",    "content-type": "application/x-www-form-urlencoded",    "user-agent": "Mozilla/5.0...",    "cookie": "auth_sid=20000"  },  "method": "POST",  "body": "code=1&client_id=65407",  "time": "2025-11-14 17:20:26",  "website": "http://a.molun.com/",  "status": 0,  "scaner_status":0,  "source": 0  // 0=流量捕捉, 1=url生成}
```

一切以处理HTTP请求为标准，也就是说通过获取HTTP请求，来分离出，website站点、subdomain子域名，再得到子域名解析记录，再得到HTTP响应，包括html\js\各类响应信息等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MlDb4sb1b3x0iaQf6QXsy43V2RCibsLNo4KCubd5LFxecdp9gyy0JY5dOjug2kAHcqngzcic1pWlAwqWs3camicck91kukH8bib77E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6OmFiaBnuyxZMYlGYlfV7KpLlglUHDdruS2tCQpfNQAz7CLJjZTbdEia6jhdlfSRctkhOEbIqOvZTBKgib4W8ibSPib1PnL4zz83WjU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PhggBMsiaBTZBqQiaZ5nMqESMGibLQDRs3iaVyW8z07BOO7EG9yDC3B3hxrZtpKZWxKG8tia57wS4BAYRFRUdq4FscjXibf6SkOvX2A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PHmVyIEkKzsqcvG3kyzyqRzcY7CoAtsvMN8BCtp6px8VWuzAFdyHau39hTaB8ticTP0ME0Xia5KBHOxWIadnhXJOuCOIs4sr7GA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OyEayBULpw4ybXk7B4Yp8tiaH1FQdfiblNGOS4RxcDE5FfEkPdA1ulsfEeKcPibrMNh0bibO6S4u7uk1JicBjMdMSj5gIEbbpt5sMs/640?wx_fmt=png&from=appmsg)

支持对http请求进行处理分离，并且处理读取html，还会对http进行漏洞扫描，并且扫描是无害化，不打任何payload，虽然有不少误报，但将就能用。

1. 资产管理工具
2. 被动漏洞扫描器

### 使用方式

**需要环境**

1. Windows系统
2. mongodb数据库
3. python3+

**安装依赖**

`pip install -r requirements.txt`

**配置文件**config.json

```
{    "flask_port":5001,    "chrome_path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",    "burp_path": "D:\\hack_tools\\burp\\",    "chrome_cdp_port": 19227,    "chrome_spider_cdp_port": 19228,    "mitmproxy_port": 18081,    "burp_port":8080,    "mongodb": {        "ip": "127.0.0.1",        "port": 27017,        "dbname": "facai",        "username": "",        "password": ""    },    "AI_model":{        "model_name":"",        "API":"",        "API_KEY": ""    }}
```

这里的burp\_path有个前提，我burp是破解版的，如果你不是，你可以不用填写，burp\_path、burp\_port。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6NA79RPe3nWm3WUCzLHrKKEEM72TowkxQuDEQmtOdS1PCgsNWqkGdBqkQ7kGprSn4Gib3MqQTHmiaokDW8IG871tZQxajHzK0jFQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OZsbtkHUwyice80mjcEqk1Oy3fnkA9kXMvc8vYeichxo180HMjFoKwZOurMzfD0sKHCTRk8HibpYicHTBXmT8EzmibPUf5UibqCgSxc/640?wx_fmt=png&from=appmsg)

如图自行打开，然后设置burp转发端口，指向为mitmproxy\_port端口。

**启动**

```
start.bat
```

**添加项目**

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Pt9GgdiccmhzsRXZMcc61bCKZW2bGH2BsOryCHCGibkQOzdD8JNcOCzplhCV76B4LG2Aw8qxnuFtP7R1FHMl1hoRPzntlNyDj0Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OupU3yu079w0RJrJHXjvPErn3Aol3iaEjWUPic1Bib6jsTE6P3EmDT34PmKXX2c6EtYaXKc3yqoKibNkIR40FbiaMaicFzyOkjKayE4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Nv0Uyicfk3j1Q7T9Y8P7KBqeb4fPNib01kHc18NDbjBHCUosaL6v8Q8TdcIibPbNVdlf7Pmpowxuy8JXqIbdFoRjibBpiaaNS6n1Kw/640?wx_fmt=png&from=appmsg)

```
{    "Project": "test",    "Project_Name": "molun",    "Description": "描述",    "domain_list": [        "lulun.com",        "molun.com"    ],    "port_target": "21,22,80-89,443,1080,1433,1521,3000,3306,3389,5432,5900,6379,7001,8000,8069,8080-8099,8161,8888,9080,9081,9090,9200,9300,10000-10002,11211,11434,27016-27018,36000,50000,50070",    "clipboard_text": [        "'\"","javascript:alert``//",""    ],    "dnslog_domain":"{hash}.www.dnslog.com",    "dnslog_url":"http://www.dnslog.com/{hash}",    "browser_thread": 10,    "http_thread": 10,    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",    "timeout": 8,    "service_lock": {      "spider_service": 1,      "monitor_service": 0,      "scaner_service": 1    },    "dns_server": [        [            "119.29.29.29",            "119.28.28.28"        ],        [            "180.76.76.76",            "180.76.76.76"        ],        [            "180.184.1.1",            "180.184.2.2"        ],        [            "114.114.114.114",            "114.114.115.115"        ],        [            "223.5.5.5",            "223.6.6.6"        ]    ],    "file_type": [".php", ".asp", ".aspx", ".asa", ".assh", ".jsp", ".jspx", ".do", ".action", ".py", ".cgi", ".htm", ".html", ".fcg", ".fcgi", ".xhtml", ".shtml", ".shtm", ".rhtml", ".rhtm", ".jhtml", ".jhtm", ".pl", ".php3", ".php4", ".php5", ".phtml", ".pht", ".phar", ".phpt", ".phs", ".ph7"],    "file_type_disallowed": [".3g2", ".3gp", ".7z", ".aac", ".abw", ".aif", ".aifc", ".aiff", ".arc", ".au", ".avi", ".azw", ".bin", ".bmp", ".bz", ".bz2", ".cmx", ".cod", ".csh", ".css", ".csv", ".doc", ".docx", ".eot", ".epub", ".gif", ".gz", ".ico", ".ics", ".ief", ".jar", ".jfif", ".jpe", ".jpeg", ".jpg", ".m3u", ".mid", ".midi", ".mjs", ".mp2", ".mp3", ".mp4", ".mpa", ".mpe", ".mpeg", ".mpg", ".mpkg", ".mpp", ".mpv2", ".odp", ".ods", ".odt", ".oga", ".ogv", ".ogx", ".otf", ".pbm", ".pdf", ".pgm", ".png", ".pnm", ".ppm", ".ppt", ".pptx", ".ra", ".ram", ".rar", ".ras", ".rgb", ".rmi", ".rtf", ".snd", ".svg", ".swf", ".tar", ".tif", ".tiff", ".ttf", ".vsd", ".wav", ".weba", ".webm", ".webp", ".woff", ".woff2", ".xbm", ".xls", ".xlsx", ".xpm", ".xul", ".xwd", ".zip", ".exe", ".apk", ".msi", ".dmg", ".rpm", ".deb", ".pkg", ".ios", ".iso", ".txt", ".m3u8", ".tgz", ".md", ".xml", ".dll"],    "personal_info":{"id_card_number":"110105199503151234","passport_number":"E12345678","marital_status":"未婚","account":"zhangsan_2024","password":"P@ssw0rd!2024","name":"张三","nickname":"三儿","gender":"男","age":28,"birthday":"1995-03-15","signature":"热爱编程与旅行","email":"zhangsan@example.com","phone":"13800138000","landline":"010-12345678","address":"北京市朝阳区建国路88号SOHO现代城A座1001室","postal_code":"100022","website_url":"https://zhangsan.github.io","emergency_contact":{"name":"张建国","relationship":"父亲","phone":"13900139000"},"school":"北京大学","education_level":"硕士","major":"计算机科学","graduation_time":"2019-07-01","company":"膜沦科技有限公司","occupation":"软件工程师","position":"高级开发工程师","industry":"互联网","work_experience_years":5,"country":"中国","province":"北京市","city":"北京市","district":"朝阳区","hobbies":["编程","旅行","摄影"],"languages":["中文","英语"],"avatar":"https://example.com/avatars/zhangsan.jpg","social_media":{"wechat":"zhangsan_2024","qq":"123456789","weibo":"@张三的微博","linkedin":"linkedin.com/in/zhangsan"},"agreed_to_terms":true,"subscription_preferences":{"receive_marketing_emails":false,"receive_sms_notifications":true}}    "status_code": 1,    "created_at": "2026-01-16 16:54:25",    "updated_at": "2026-02-25 16:21:12"}
```

1. Project为项目标识，必须纯英文。
2. domain\_list为目标范围，必须域名。
3. dnslog\_domain、dnslog\_url为rce与ssrf盲打的测试url，你可以自行填写，hash是标识符，方便到时候查询是哪个请求打的。
4. personal\_info自行更改，之后爬虫会用到。

**启动项目后则可用，因为流量表里没数据，得开浏览器代理指向代理端口往里面写数据，或者在资产管理、资产管理配置导入子域名或者url，写初始启动数据。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PpGJrfuzAyQmf7mBc1ZydfHR26ozfn56ShA10gawAoZ4E06TJK0qf1ibIGolIsRgeuRlgWLc8gEh12FYxG1b1j9ibDfEaRVpkG0/640?wx_fmt=png&from=appmsg)

### 功能介绍

```
├── 项目管理                    (#projects)├── 服务管理                    (#services)├── HTTP流量                    (#traffic)├── 资产管理                    (#assets)│   ├── 资产总览                (#assets...