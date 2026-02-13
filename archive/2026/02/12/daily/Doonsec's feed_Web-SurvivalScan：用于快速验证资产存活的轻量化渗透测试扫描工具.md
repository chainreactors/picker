---
title: Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具
url: https://mp.weixin.qq.com/s/OfBuV6jjWCyW-pDC-07nog
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:29.634088
---

# Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicLTYWiazgUJEnjv5FLRWgfBKhm4NjbG6lbZx22zWcml7iaibVYzVjiaRQX8fx6fYbwiasKNMKgPbacuJUbELYsjiaSwYxDc2fYK9UUS4/0?wx_fmt=jpeg)

# Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

·[StegoScan：CTF自动化隐写识别和解密工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486301&idx=1&sn=704da2217fce796fe07611b66c3448d4&scene=21#wechat_redirect)

·[Metasploit Pro：可视化的metasploit渗透测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486276&idx=1&sn=44e00b0ee13437083417bd8c16f15f0c&scene=21#wechat_redirect)

·[Coda：实现Windows/Linux入侵痕迹抹除](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486251&idx=1&sn=c2c9dc8f482b43d9c5c0384d37eeb8a6&scene=21#wechat_redirect)

·[OSV-Scanner：一款专门于发现开源软件漏洞的扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486240&idx=1&sn=69241fc574c182a305e1c17747377ae6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicI7IWDjqzibng2Yibv0NyaPcqmVic8VGQBAEiciaRibcZYOZq2dfpHZ9CRjLReQ9M7SOcicickM64vIQN4ML0udxBJwXfJ9EaMAVZoI4wc/640?wx_fmt=png&from=appmsg)

      Web-SurvivalScan 是一款面向 Web 安全领域的轻量化渗透测试扫描套件，深度整合了资产探测、漏洞扫描、指纹识别等核心能力，基于被动扫描与主动探测双引擎架构，可对目标 Web 资产进行全维度的脆弱性挖掘，其底层依托多协议解析模块、指纹特征库匹配机制及漏洞 POC/EXP 联动执行逻辑，能够高效识别如 SQL 注入、XSS 跨站脚本、SSRF、目录遍历等常见 Web 安全漏洞，同时支持资产测绘、存活验证、端口指纹枚举等前置侦察环节，适配多场景下的 Web 安全基线检测与渗透测试前置信息收集需求，具备低误报率、高覆盖率的技术特性，是 Web 安全从业者开展安全评估、漏洞挖掘的核心工具集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装&使用**

解压安装包后，在解压后位置打开终端

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIV7mOFYSTk6j3Vaz1SHYZOTUmCiaDOgdSE5bMz6ugrTiarMicfg6zz2snA1Uay7JKgyfiaB9hiaMGCzGnEeNqbajgYaOUuVDVGH5B4/640?wx_fmt=png&from=appmsg)

输入

```
pip3 install -r requirements.txt
```

安装依赖

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIbKug7zXryiaXvypFTmhCaMeAKGMXUtCukvicicn1AiaHQCpDEuiadHww2CYne042tX9S6cnP463aBicYB8Qz98NYiaHjeicX0zGszf3k/640?wx_fmt=png&from=appmsg)

使用：

将目标Web资产批量复制到TXT内，并将该TXT放到本脚本同目录

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJC6W2oM1kJJRHTdBZFbeoBOoBUKWzNdDUtsvp7swSArLK4kbG1Hr004Zyr2GvTicjlTS2kiaMxeic4tDpdfUZLhicLRLDaJEywibHw/640?wx_fmt=png&from=appmsg)

在文件夹中打开终端，输入

python Web-SurvivalScan.py

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKicX6xY6K3JQn8MQDUYX8KSuehXDpX42yEHDm3aLnl3ES77ibA9UWoWaAh0dGUuiabfCfLjviaVc0wnWpMlBFW7JRtuSegjiagCUkc/640?wx_fmt=png&from=appmsg)

按照提示输入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJCD4XrLicJvZ7ia3JJQicLUW5DQVnPq9g9YhYwhaqsSSukTp12MqhaqG5zI5gCZIedVnnnxwycvpbxfibVfmfhSptL3aVv9Gk4QQU/640?wx_fmt=png&from=appmsg)

跑完后，即可拿到导出的两个文件：output.txt 和 outerror.txt

output.txt：导出验证存活成功（状态码200）的Web资产

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJoUkb5nlRHPdcn24vfAhfVHDa9deCrTLOIWz3ewnz6AE2yJibz0aA2myS2nztB8OxfctDOXq6co2aLzMPgNutw65hSLpIyp3IY/640?wx_fmt=png&from=appmsg)

outerror.txt：导出其他状态码的Web资产，方便后期排查遗漏和寻找其他脆弱点

.data/report.json：所有资产的运行数据，按JSON格式导出，方便处理

report.html：将所有资产进行HTML可视化导出，方便整理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKIpL8aRwAQPIp5TgNS8Q5pR50LpIX1XglrFNc66gSvAJcqArqWvSVS8tKJ3LoJERKw1kssYszMXOQO3uq67JCCibt69eO6UVOo/640?wx_fmt=png&from=appmsg)

github链接

```
https://github.com/AabyssZG/Web-SurvivalScan
```

或者

通过网盘分享的文件：

Web-SurvivalScan-1.11.zip

链接:

https://pan.baidu.com/s/1RIqKqIKKQgGcIgTxokqlew?pwd=4ghp

提取码: 4ghp

--来自百度网盘超级会员v3的分享

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