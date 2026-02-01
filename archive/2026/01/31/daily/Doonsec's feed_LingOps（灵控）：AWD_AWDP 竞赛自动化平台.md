---
title: LingOps（灵控）：AWD/AWDP 竞赛自动化平台
url: https://mp.weixin.qq.com/s/UEm_7iqn_Xsbyv9JP_llLA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:10.724019
---

# LingOps（灵控）：AWD/AWDP 竞赛自动化平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0saoqSbc8MPmzrZA6ibx1ESHgpGC0SJagIxJPUBRBnONRTptXDNP3pPQ/0?wx_fmt=jpeg)

# LingOps（灵控）：AWD/AWDP 竞赛自动化平台

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[融合AI引擎的日志应急响应溯源工具SSLogs--详细配置教程与使用方法](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486211&idx=1&sn=b6893a457752881cbef64eb8f685e0fb&scene=21#wechat_redirect)

·[AWD-H1M：AWD攻防竞赛自动化工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486193&idx=1&sn=0d299367f73c1a711d810af55196a275&scene=21#wechat_redirect)

·[DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486180&idx=1&sn=c8e5f47564ce29bf0435b6bba13828a1&scene=21#wechat_redirect)

·[FingerprintHub：识别网站和网络服务背后使用的技术栈](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486175&idx=1&sn=ff7c227b167f27367150e9f9d481be57&scene=21#wechat_redirect)

·[data-cve-poc：近两年的漏洞CVE-POC合集](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486159&idx=1&sn=d4788941d37418ed052eefd317ae631c&scene=21#wechat_redirect)

·[摄像头钓鱼工具--CamPhish](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486137&idx=1&sn=5e7489adeffa7f2b5a61b12836f06795&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

LingOps（灵控） 是一款专为 AWD/AWDP 网络攻防竞赛 设计的全流程自动化作战平台。如果你参加过CTF比赛，就知道AWD赛制特有的高压环境——多支队伍在同一网络环境中互相攻击与防守，既要快速攻破对手服务器获取Flag，又要加固自己的服务器防止被攻陷。

    灵控的核心价值在于：将分散的工具和手工操作整合为统一的自动化流程，让参赛者从重复性劳动中解放，专注于战术策略。

    在典型的AWD比赛中，每个队伍会获得多台服务器（通常3-5台），既要保护自己的服务器不被攻破，又要攻击其他队伍的服务器获取得分（Flag）。这个过程涉及：

1.管理多个服务器连接（IP地址、密码、WebShell等）

2.定时读取对手服务器的Flag（比赛得分依据）

3.加固自己的服务器防止被攻击

4.监控服务器状态和攻击流量

    手工操作这些任务极其繁琐，LingOps将攻防所有操作集成在一个可视化界面中，通过点击和简单配置就能完成复杂操作，系统自动执行重复任务，让选手专注于战术策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装说明**

我们找到LingOps在GitHub上的地址：

```
https://github.com/zhanglinglingc/lingops?tab=readme-ov-file
```

    可以从README中寻找压缩包，或者前往GitHub Releases页面进行下载，根据自己需要的版本可以选择Linux或者Windows系统进行下载，在macOS系统上的灵控还在开发中，这里讲解Windows系统的操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0iazzxib0Kl82Ld4LEgJSrArYmjHJoBHvdYyibLUapqCtGnzWeOx828Skw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0ZXyzkT21kqkH0A10KicE4F0ppLLqzib6hJbLayO0gUOqw4gc08zGcPpA/640?wx_fmt=png&from=appmsg)

    下载后可以在文件夹中看到以下文件，然后就可以使用了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0rPcTyxfPjywlOZ6WxdibH8SCdbdPhgGm3gBK0CM7lZg0LKtA8CEmh7A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍**

我们点击.exe文件后，可以看到文件开始运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0m9mkL8oRXTKia9xGAAnt800uvgK45yrEKYI1qWnREmtXLbOaiaDkAq0A/640?wx_fmt=png&from=appmsg)

    之后我们打开浏览器，在浏览器中搜索地址：

```
http://127.0.0.1:8080
```

然后便可看到LingOps的登录页面，输入用户名和密码：

```
用户名：admin秘密：admin123
```

    进入到LingOps的操作页面首页：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0kIx5UnSEgSs8BwCrKe9NsPeOc7jt1dYBha1KyWKkluL0MyRA5jENpw/640?wx_fmt=png&from=appmsg)

    可以看到有六个功能：目标探测、Shell管理、基线加固、Flag读取、WebShell扫描、数据库管理

1、目标探测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0XHPywTaE0iaH4mUGhlacp9Hf7jZW3eichBJDQWibODIhH79abfI6s7DWQ/640?wx_fmt=png&from=appmsg)

    可以看到，我们在目标主机地址填入想要进行扫描的地址，一键扫描所有存活主机，会自动识别80(Web)、22(SSH)、3306(MySQL)等关键端口，并可视化展示所有目标关系图

    在进行比赛时，可以在拿到IP地址后导入LingOps进行一件扫描，三分钟完成侦察。

2、Shell管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0uZrw0loMqX0TBssPywsAuOiclFGtI9XxjNQYZw2hKZXACc6eWIBCIvg/640?wx_fmt=png&from=appmsg)

    可以看到，我们可以对所有使用到的连接在同一个页面进行管理，自动保存连接信息包括名称、类型、目标等。点击“添加Shell”，并填写名称、IP、端口、类型(WebShell/SSH)、密码等，保存后点击"连接"按钮，然后可以在网页终端直接输入命令。

    防止了比赛中有多个WebShell和SSH连接，记不住密码和地址的情况。使得比赛过程更加顺畅便利。

3、WebShell扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL04cPHKcq7jLyhmJJe5TZh0pReunzOxF7bia7oFmShUDicOK5NYItVBPfw/640?wx_fmt=png&from=appmsg)

    可以看到这是一个WAF管理页面，可以通过添加WAF进行Web应用防火墙管理，通过简单部署防火墙的方式，进行SQL注入防护、XSS攻击防护、文件上传过滤、CC攻击防护等。

    通过WebShell扫描也可以检查自己的服务器是否被植入了后门，是一个在比赛过程中进行主动防御和自我保护的功能。

4、基线加固

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0VOn4PGkEqriae03qDUKrynxmohiayrDQjT4Hfw5M7FvZwM0eicOphsasw/640?wx_fmt=png&from=appmsg)

    可以选择要加固的SSH会话进行加固，同时也可以进行操作类型的区分，以对操作内容进行保护。

    可以修改SSH登录密码（防止被ssh入侵）、MySQL数据库密码（防止数据库被拖）、Web后台密码（防止后台被控）、系统用户密码（加固所有账号）等。

    在比赛过程中，要尽早进行密码的修改并尽量的复杂，不同服务用不同密码，以防被使用初始的默认密码而造成攻击。

5、Flag读取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ug9bYuAmibReiaZBYBVibYrKL0UEQA2tgwYgXtvMyfWlkibFl3hvtaxC5yBcPUqM7yYbhiayw5ziaYXsNfg/640?wx_fmt=png&from=appmsg)

    我们可以通过对SSH或者WebShell的选择进行特定目标Flag的读取扫描，只需配置一次便可自动运行收集。并且可以设置时间间隔，进行持续不间断的扫描收集。

    在比赛中，不需要手动连接每个对手服务器进行频繁重复操作，可以后台持续运行并同时从所有对手服务器读取不重复的Flag。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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