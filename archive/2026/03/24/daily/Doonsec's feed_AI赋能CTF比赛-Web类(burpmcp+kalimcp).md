---
title: AI赋能CTF比赛-Web类(burpmcp+kalimcp)
url: https://mp.weixin.qq.com/s/uvsdPsJUuAA3uEBg_bwI6g
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:18.910009
---

# AI赋能CTF比赛-Web类(burpmcp+kalimcp)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xY9ZTT0gDw7wKJbMsAryXEALiaCWWiaChv7pquHf6xHglRXCDqEMw0gaCoCwzuuTxPspG3Gb6WCMcY7CNaBXdu1sPzq3uJnb3VLaMUJwvRwGY/0?wx_fmt=jpeg)

# AI赋能CTF比赛-Web类(burpmcp+kalimcp)

原创

huan666
huan666

huan666

![]()

在小说阅读器中沉浸阅读

一、前言

人工智能与网络安全竞赛的深度融合，已成为行业发展的必然趋势。AI 赋能 CTF，不仅提升了竞赛效率与解题能力，更为安全人才培养、攻防技术创新注入了新动能。

本文通过mcp调用burp、kali，自动获取flag。

二、工具清单

```
Trae AI IDE：https://www.trae.cn/burpmcp：https://github.com/PortSwigger/mcp-serverkalimcp：https://github.com/Wh0am123/MCP-Kali-Server/
```

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5JvtTJbV2rNRDuriasTan2zmz8a5vTNQliaOfzQPNRcSLVwfX9mbbgX6u7pvQdm61DrRzUEcqabKp1jrIx6aKIyTM3UjibVt3ztk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5DKWFvuFatFxzWkaJa6KTAagWorL6mf474wcvzlJdqUDupiaoB1sbZv52Y7PhXWX1EmXoSjcqWaCvu21RpYjpKeVNZppDJrY5U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6uneVDceeVNQWlibZ03PHxjeNDW8a5PDseAU86vyrJ8yduk9veicQPAW5D9SxswkIc4nibzYuPo0TictFicSADxmpMAf5Yv8Yk0EH8/640?wx_fmt=png&from=appmsg)

三、环境配置

1、安装Trae，默认安装即可，详细步骤参考

[基于Trae的AI自动化安全测试实战总结](https://mp.weixin.qq.com/s?__biz=MzkzMjk5MDU3Nw==&mid=2247484740&idx=1&sn=3a62e0cc4905d77278ea557791c2c20e&scene=21#wechat_redirect)

2、burpmcp配置，官方未提供编译好的版本，需要自行编译，我这边使用的java version "21.0.10"版本，可以成功

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw74FMJOCwR6oG4iasdFSfszFuEiatNU6IWvvj6yMaOJJO6hqG8hxNgjhWF94R0ibkvpqV5jicuBIMhjYzpd6xtcYuqvxBv0ib7afwHI/640?wx_fmt=png&from=appmsg)

进入到项目目录，运行 gradlew.bat embedProxyJar命令即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7GfQ0KR5I7GBrpuIAWYq2iacewRQ9ribeHQwGsPJg2YOB2CxcficHNViaCGricTYBOPVHRcWUCVIUs4oy5v0q0pH2IAVBwR2lln2UE/640?wx_fmt=png&from=appmsg)

编译好的jar包在mcp-server-main\build\libs目录下

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6HtjDQ3icssUdyiaem9UbIEGSACBrLHORbU5flMRaBq1DzkvzytIbnqKA3Kj1HIr6WafaNkib3sWPo9t3xCEeoKOtDuwe5ric57eE/640?wx_fmt=png&from=appmsg)

导入到BurpSuie中

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw48Uz2D74Fr7cvgfKicKN5zpVmUcJGNsBR9VoVUb4jMd8Wm3d2jonSS9nzh8M3vW6fqymia9ZlTlnt1eicrKHedwLRhFbYsoFAS6A/640?wx_fmt=png&from=appmsg)

启动burpmcp服务

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7gMKcia4fphnlhP19XMm8vFic6bgOyLicWPHFVhZxncaNcaOvqVk3Ax2dA9e9xJe1Ip0ZSdk0ozczRyh85BJWFAmFt7glO1yFJVw/640?wx_fmt=png&from=appmsg)

Trae连接burpmcp服务，设置->MCP->添加->手动添加

配置文件：

```
{  "mcpServers": {    "burpsuite": {      "url": "http://127.0.0.1:9876/"    }  }}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4QuACunz9czoib0eiatFgqguyVFUrkicGtUiaw8BAPAkvnZsabhzABpFeKoHp0QL0KNnLzxwiaibneVaRheverylpviagoRiaBwVmCTbk/640?wx_fmt=png&from=appmsg)

3、kalimcp配置，kali下载项目，并启动服务端，启动前先安装requirements.txt文件中的模块

```
 pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

服务端启动命令：python3 server.py --ip 0.0.0.0

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw78bm1vrnsoDTBSChtE2ZLiaJYpVZrq2ia49seMhtVToc3Uq9YyUN5M40uIew9eN10Pp9WBmRiaqUQBdlOMyv0O35v6JySHez2w0g/640?wx_fmt=png&from=appmsg)

安装Trae的机器也同样下载该项目，我这里放到

C:\Users\huan666\Desktop\Skills\MCP-Kali-Server目录下

同样安装所需模块，和上面的命令一样

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6WrFFFRdjV1mFPExibSuOZOeL3EE1mE0vJQF9OO9b58dcRAmCQ8HNibYBKaXhwibChBpeHzeRYpvWZuVMktqvhCiar5ibicq3kaWBz8/640?wx_fmt=png&from=appmsg)

Trae连接kalimcp服务，设置->MCP->添加->手动添加

配置文件：

```
{  "mcpServers": {    "mcp-kali-server": {      "command": "python",      "args": [        "C:/Users/huan666/Desktop/Skills/MCP-Kali-Server/client.py",        "--server",        "http://192.168.10.131:5000/"      ]    }  }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5KnuI6NjcLjYr1JdBQ9ILU4zrYOK7VficngwMBsrdMXJica0M0TQW3nwG4HxLhsxjQhuhcHMbZ396o5ABbB2nrua6mewPB1aEjo/640?wx_fmt=png&from=appmsg)

四、案例演示

靶场环境：

```
https://buuoj.cn/challenges#[%E7%BD%91%E9%BC%8E%E6%9D%AF%202020%20%E9%9D%92%E9%BE%99%E7%BB%84]AreUSerialz
```

提示词：

这是一道CTF题目，调用burpsuite mcp和mcp-kali-server  mcp，解题找出flag，题目地址： http://x.x.x.x.com。

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw49ib2QBqZP2vSMqP5xUMtdibd8ORU6y4KVsRfiaWnvMtNiau9HRC1MgQMpaF9WBXE3XbI72iaE9HUFcrVHZt7FRIDrAfHD47Vuo7MM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7Xic2RHmCZpfX5rtyJE0hCnSVakYwAokOCv1rg2M9ArC31rhFVJLJeSgteFEcST2ocXWJvZnHNk4HXmSlzhNItIdMFZUYBeqG0/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

huan666

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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