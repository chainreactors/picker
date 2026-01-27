---
title: 红队C2工具--vshell
url: https://mp.weixin.qq.com/s/N6aCm2Q4RUDFndkCHxfkVQ
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:35:48.976042
---

# 红队C2工具--vshell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6eMiaKGY7UXV7hOHfEdRK7623bLCkrvDNuhFoRUibSOdM3Q58x3uLZMpg/0?wx_fmt=jpeg)

# 红队C2工具--vshell

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

# 简介

* vshell是一款安全对抗模拟、红队工具。提供隧道代理和隐蔽通道，模拟长期潜伏攻击者的策略和技术。vshell 为您提供隧道代理和隐蔽通道，以模拟网络中的持久化攻击行为。支持多种协议、高兼容性、及强大的协作能力，帮助蓝队更好的评估安全设备水平，提高应急响应能力。
* 主要用于渗透测试与网络攻防演练。其核心功能包括跨平台客户端控制（支持Windows/Linux）、多协议隧道代理（如WebSocket、DNS、DoH）及反溯源设计（SSL证书伪装、CDN隐藏），可在内网穿透、横向移动等场景中构建隐蔽通道。工具采用Go语言开发，早期开源后转为闭源，常被用于生成免杀木马和模拟高级威胁攻击，但需注意法律合规性及破解版潜在风险。相较于Cobalt Strike，其优势在于轻量化与Linux环境适配能力。
* 下载：链接: https://yun.139.com/shareweb/#/w/i/2sNZWbe5LA4df  提取码:m2fy

# 支持内容

* 支持多种协议的隐蔽通道（TCP UDPKCPWebSocketDNSDOHDOTOSS）
* 支持文件管理、终端、屏幕截屏、开机启动等管理功能
* 支持内存运行多种格式的插件（exenetelfdllsodylib）
* 支持多种协议的隧道代理
* 支持正、反向连接模式，支持代理上线
* 支持Windows shellcode客户端
* 支持域名上线、CDN上线
* 支持ebpf客户端穿透防火墙

# 安装

解压，之后打开conf目录下的setting.conf文件

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6HvKDOfykOcn3HJbOjCF8TPaibVLsNXNc3TIfzh82XPgNiaO5ZsNg6koQ/640?wx_fmt=png&from=appmsg)

建议修改配置，之后启动服务端，windows中直接双击运行.exe就行

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are65yk4qKgkRCKYRqI90j9v1hwicYiaAKI9aSGgBdqaT0QFuEeXs5ibyrP7g/640?wx_fmt=png&from=appmsg)

之后访问8082端口

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6ACdbMWYjBAmOWF6bhrcKY6Vl9VghUT9IIta410mubgJf55Q5x0vkFQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are680EoupIbkflTz8qMH7iaRL0PUWrstTkC7y5VEUqqh6VTlicbZhvGUMTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6f0INlLLw4gQicUB6zjAuQsp86ialibpB9Bsy8r9ZlIW8iaclfDHUlOxMeg/640?wx_fmt=png&from=appmsg)

# 监听管理

支持七种监听方式：

* TCP

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6xkiaC4RncA1MIGibasm3tndfDYLpZGiaEkB9lCovbXE0hJCV3UORx9dfA/640?wx_fmt=png&from=appmsg)

* KCP/UDP

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6BenAibY37EPshJw9yHm90cVKnL8Y2Q1py9USThuOSbqqyEyJGvB34tw/640?wx_fmt=png&from=appmsg)

* WebSocket

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6CnU0UNmobS0fhyMMauWAKGDDLqQHJR3VKSbaq3xZorxdOU1G4JDaxQ/640?wx_fmt=png&from=appmsg)

* DNS

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6uxEm2zZL8sdtKYZQ7ptlRABtD42ibuYmMoiaFuAcjHc4ayZL416EakRA/640?wx_fmt=png&from=appmsg)

* DOH

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6sa3awY1RrPVp1EmQicHuTqkT8Kqw3smj6DNxOqoOnTM981ic619estRw/640?wx_fmt=png&from=appmsg)

* DOT

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6ib4V9sqfZjBSDs57XWcxdIommSpARSy1FoLORxg1j9OOcnHdhqXILzg/640?wx_fmt=png&from=appmsg)

* OSS

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6HMGQcAqzibVkOF21gcjdFibRedgtAJFfkN1mkWlwIH1GSKbd0TWvhr5A/640?wx_fmt=png&from=appmsg)

这里使用TCP创建监听

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are67a48PZZ5TsmjMCfJEBkIbCNP1tOkLHpNXGKQaL6iaDpW17DXAFUGFFw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6vYMia7xRFFjIPcUEuJPJJOHX8L5MnRcqSIn4Tj3QBCcTVnKnZZsP4vQ/640?wx_fmt=png&from=appmsg)

可直接使用命令上线

# 客户端生成

支持七种客户端：需自行免杀

* Stage 反向客户端：

+ 小体积客户端，反连模式上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6uunz9zKia3czzyWy1sz0WC2wOaMqPvvHoRbMOhKPJ9Y1M2N0ffZwcJw/640?wx_fmt=png&from=appmsg)

* Shellcode 反向客户端：

+ Windows shellcode 客户端，反连模式上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6VIwlABcr7KMAJfG2pPXCicibrqHyuQ3nTq7NE6RqWLsoX0GK8bL8xYZQ/640?wx_fmt=png&from=appmsg)

* Stageless 反向客户端：

+ 完整客户端，反连模式上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6uoZIfcFvMYExiceXKZMibmvCqibNLJ8eWvXwPDBrYcgQ0E1tgS8bibJ8xw/640?wx_fmt=png&from=appmsg)

* DLL 反向客户端：

+ Windows dll 客户端，反连模式上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6We4xel0ibcvkzznfW7nCiaaibXEeDib8r7eEE49JwIfVXlKjcHBEaZ1TAA/640?wx_fmt=png&from=appmsg)

* 正向客户端：

+ 监听模式客户端，正向连接上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6rD7YvBFgSXGRD9SYHWE8VXMTJ7M99rZKEiaLWib0lQf9vQheBzjicNZOg/640?wx_fmt=png&from=appmsg)

* 正向客户端：

+ Windows dll 监听模式客户端，正向连接上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6woM8zyMJPlnz3nywsnT2LXOeg0ubV03Iw1icWYNBtoiajcahK9oRibyCQ/640?wx_fmt=png&from=appmsg)

* ebpf 正向客户端：

+ Linux ebpf 监听模式客户端，正向连接进行上线

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6go55aNj3xxwZoXfzFvMOT9EKaMOrTKonqE0fkU8VjsVMdJAQRjpIdg/640?wx_fmt=png&from=appmsg)

这里生成linux反向客户端

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6hut1iczySjJwaYfh3TmOLPURfv8Tw2JhwtvN1EQlv9SXpriaOU5zdWIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6AOhnzq31Qoz2EuLicvOQw4GdfR0n2jg4VZia9cicpRibhiaicIYaD93TrcMA/640?wx_fmt=png&from=appmsg)

# 客户端管理

支持两种操作：主机管理、隧道代理

## 主机管理

* 命令控制

+ 支持交互式终端和非交互式终端

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6cibOnslYIqrUdFZuAALoRMAXrV18esiaWN5WZJaTnnSEnPC3s3ySJySw/640?wx_fmt=png&from=appmsg)

* 文件管理

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6mqOOaNvjRbOldtiax8DvQt4mXcY0mt1vgmnm5z0oGy4eak3Wquic0haw/640?wx_fmt=png&from=appmsg)

* 屏幕截屏

+ 不支持Linux

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6Hnkj7KAbvibLHaZibWJtRMpMVURqDe6ATLEYibeicuTaYP7ajGNB19ZXSw/640?wx_fmt=png&from=appmsg)

* 屏幕监控

+ 不支持Linux

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6xnicKOuYpGibGM1DJuBkp6bCNW2qInRRvODF8N1pfpcIibbY28d3EqsgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6flnD4eXxliaOrVwicWU6fO2UV4OuYKZgHAIY04vc70iblmKXMXJSNC68g/640?wx_fmt=png&from=appmsg)

* 插件运行
* 开机启动

+ Windows 需要有管理员或添加服务的权限。Linux 需要root权限

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6D49Niao49bflF6rZvMb3rZibv3hJeonRC5PraOIwphlowC5NRWp5LricA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6wBqOInyZ7qaw8djib1laEfF8Ou98z6DZ8ZNFtrC9eLIvtwNibMM9Ns3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6Raeziciaic9fuwlJtoiaxvzZqvNjcTmPNx8bYOpeKSH1YicV7UG54XFVM5A/640?wx_fmt=png&from=appmsg)

# 插件运行

* plugins 目录内的文件都视为插件，使用内存加载模式运行，支持 exe、.net、elf、dll、so、dylib，自行添加插件需遵循后缀规范，如（.net插件以net为后缀，elf以elf为后缀）
* 可自行添加插件，但插件需免杀
* 如果运行插件一直超时，建议使用管理员身份运行尝试

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6IWaFNb9EyqJibQqcfhBVj1ynk5P4eZSk1ZN8SDDCNreDgMh7dKgKicgw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6CrodQAGkxIfrSRTnlf1VNv0j197libfr4qHAwfic5sw4OkoEzDDcS5Yg/640?wx_fmt=png&from=appmsg)

# 隧道代理

* 支持 TCP、UDP、HTTP、SOCKS5 隧道代理

![](https://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RztBtWEnSFUbTeNPMic8Are6Zt3TaO8EAYmBx57ERrAS09u5X4t3HBzCuXp8rQXUwic977GZMm5I1mw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

一个努力的学渣

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

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