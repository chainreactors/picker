---
title: HexStrike AI自动渗透测试平台搭建
url: https://mp.weixin.qq.com/s/4iDN2Y1V0YFmTqo-jcErjg
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:27:47.292609
---

# HexStrike AI自动渗透测试平台搭建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6P9IcTprKpeTkqkQEOY596WBqDW1ibcNL2Apm6YUjNDT88mFXVAq6Tnw/0?wx_fmt=jpeg)

# HexStrike AI自动渗透测试平台搭建

原创

【白】

白安全组

![]()

在小说阅读器中沉浸阅读

# 官方网站

https://www.hexstrike.com/

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6bK4Zu3TZUksicArZ4WXfMcM0U11oX6uTeicop6U7kTiadaQw0j86zNmJA/640?wx_fmt=png&from=appmsg)

# 开源代码库

https://github.com/0x4m4/hexstrike-ai

# 搭建视频

https://www.youtube.com/watch?v=pSoftCagCm8

# 搭建方式

该工具可以直接在kali2025版本以上通过命令下载

apt install hexstrike-ai

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6WVS9Mm9kKYicNaXUfgYsCWelm0adqNYpFm3GRm3Ria3mHubYV0ZpeSXA/640?wx_fmt=png&from=appmsg)

但是直接安装之后运行有一些问题，所以下面我是用GitHub直接拉取到本地进行

然后我们需要安装一下需要的库

```
apt install -y python3 python3-pip python3-venv git curl wget apt-transport-https software-properties-common build-essential nodejs npm golang ruby ruby-dev libpcap-dev libffi-dev libssl-dev libpq-dev default-jdk default-jre
```

安装齐全安全工具，ai在运行时候会使用到大量的安全工具

```
apt install -y nmap masscan amass subfinder nuclei fierce dnsenum autorecon theharvester responder netexec enum4linux-ng gobuster feroxbuster dirsearch ffuf dirb nikto sqlmap wpscan arjun paramspider wafw00f hydra john hashcat medusa patator crackmapexec evil-winrm hash-identifier ophcrack gdb radare2 binwalk ghidra checksec foremost steghide exiftool maltego spiderfoot autopsy scalpel bulk-extractor testdisk hakrawler subjack xsser zaproxy dotdotpwn
```

最后更新一下nuclei的模板库

nuclei -ut

然后我们需要在kali上安装一个谷歌浏览器，方便ai进行测试使用

Linux版本谷歌下载地址：https://www.google.com/chrome/next-steps.html?platform=linux&statcb=0&installdataindex=empty&defaultbrowser=0

安装命令

```
dpkg -i google-chrome-stable_current_amd64.deb
```

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6ntkL7Iobic1MthdfEGMjPZicZrtVZiaLibIicXwJdqrAWh7A0vrfUkefzpg/640?wx_fmt=png&from=appmsg)

拉取工具：

```
git clone https://github.com/havij13/Hexstrike-AI.git
```

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6e2neyMRYl8w7ZhHohyjRSqzdtVvk3yKxxpIBeADfN4WYLq58kIzgdQ/640?wx_fmt=png&from=appmsg)

使用python3创建虚拟环境

```
python3 -m venv hexstrike_env
```

加载虚拟环境

```
source hexstrike_env/bin/activate
```

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA68aoniaEPf91ETOeibs0gESyv65jTNjEn59wzNVXZWjE2cKRM7ayEqqmQ/640?wx_fmt=png&from=appmsg)

安装依赖环境

```
python3 -m pip install -r requirements.txt
```

安装好之后我们就可以直接启动了

```
python3 hexstrike_server.py
```

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6Y43JiaQQynUp6RqszBGTpia87Ro0Jq5rbzw2jYhyd9ib1Oj3iaPyxOIfQg/640?wx_fmt=png&from=appmsg)

# 配置桌面客户端访问

kali上开启的仅仅是一个可以远程调用的进程，我们需要使用一些可以引用这个进程的工具，通过API进行调用

这里官方演示的工具是5ire，这里我们也下载这个

https://github.com/nanbingxyz/5ire/releases/tag/v0.15.2

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6iahYm5hfeW2NWhBMicFFD4WMwib8mtcEibLrOZfyrYAdbKEHkKK4XPVGhA/640?wx_fmt=png&from=appmsg)

这里我直接安装在window上面进行连接虚拟机的HexStrike AI，默认语言跟随系统，要是非中文可以在设置中调整。

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6Zs0zpug4uM9UP6lqsJwYvicP4682sNABLziaLyYwlZxP6j7zdBBvgZYA/640?wx_fmt=png&from=appmsg)

这里我们主要写下面的参数

先找到命令这个参数需要填写的内容，这个里面填写的是工具中bin文件的目录

/root/Hexstrike-AI/hexstrike\_env/bin/

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6yoMaNZJJXCx4p3h9SxfNjMkNnHR5Fc54oZxDj9hgtHQXLOWUKribRkQ/640?wx_fmt=png&from=appmsg)

根据大家放置的不同目录复制不同的路径

然后最后命令后面加上python3和空格

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6AouLuibFiaOYmwFlBVEc4eBZIAUKotXqF0xEsVkSqoIviaS72ffLwMIHw/640?wx_fmt=png&from=appmsg)

空格后面写上📎hexstrike\_mcp.py这个文件的路径/root/Hexstrike-AI/hexstrike\_mcp.py

然后后面再加上空格跟上我们的服务器也就是kali的服务地址

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6bY95PzUeU24lkhVw8WPPDWibQPNxfJcYps1iaMAKunsjuPiajZWxa3B2A/640?wx_fmt=png&from=appmsg)

最后总的命令是下面这样

```
/root/Hexstrike-AI/hexstrike_env/bin/python3 /root/Hexstrike-AI/hexstrike_mcp.py --server http://192.168.3.200:8888
```

然后点击保存之后，点击右侧开启运行

最后我们设置一下大模型api

![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUYicMBOvNKomkAicD5r0HAXA6kJQJu1IFdwh7nakblTAibGjnxJwA5NHHnY3ZaQsthibMbAxibwc3bQHDw/640?wx_fmt=png&from=appmsg)

填写对应的api，记得有余额哦

最后我们开始新的对话即可

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

白安全组

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

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