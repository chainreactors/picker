---
title: Nmap 结果也能可视化？效果还真不错！
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499387&idx=1&sn=54a5165f8550eeffd584009c12717ed7&chksm=ec1dce53db6a4745e382e36bb5668eb58f24d41183105a931ce5cbf1b3d4f08abf65adb3d6b7&scene=58&subscene=0#rd
source: 信安之路
date: 2024-05-25
fetch_date: 2025-10-06T17:17:59.164940
---

# Nmap 结果也能可视化？效果还真不错！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0oiaLBscuibkrj57jVicSQCvq6Yeiaej58tBdPsnfH5VEJ1tLDL5ZoaicVI9g/0?wx_fmt=jpeg)

# Nmap 结果也能可视化？效果还真不错！

xazlsec

信安之路

众所周知，Nmap 是一款著名的端口扫描器，结果可视化后是什么效果？先来看个图：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0oNH14m4xwyxOvy6gt74sODshrabkuIennibgaqNKYCXxR6DOzb0rGDIA/640?wx_fmt=png&from=appmsg)

界面看着是不是很熟悉？借助 Grafana 的仪表盘来分析数据，Grafana 是一个跨平台、开源的数据可视化网络应用程序平台。用户配置连接的数据源之后，Grafana 可以在网络浏览器里显示数据图表和警告。该软件的企业版本提供更多的扩展功能。扩展功能通过插件的形式提供，终端用户可以自定义自己的数据面板界面以及数据请求方式。

具体如何操作，实现这个效果？

1、使用 nmap 扫描目标网络，获取基础数据

> nmap -sV -F --script=http-title,ssl-cert -oX myoutput.xml 192.168.0.0/24

命令执行的目标是扫描 192.168.0.0/24 这个 C 段，然后扫描完成后，生成一个 myoutput.xml 结果文件，包含端口开放情况和网站标题信息等。

2、基于扫描结果，格式化到 SQLite 数据包中，这里需要用到一个开源工具：

> https://github.com/hackertarget/nmap-did-what/blob/master/data/nmap-to-sqlite.py

命令：

> python3 nmap-to-sqlite.py myoutput.xml

命令执行完成后会生成一个 nmap\_results.db 数据库文件，并将其移动到 /data/ 目录下，也就是 Grafana 配置到数据源。

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0obHoxCibwgmEPy1pQib2TEicOpWIQCdHO3jS3rg8HPxUnoiaxJqMKGDgUTQ/640?wx_fmt=png&from=appmsg)

3、启动 Grafana，使用 docker 启动：

> https://github.com/hackertarget/nmap-did-what/blob/master/grafana-docker/docker-compose.yml

启动命令：

> docker-compose up -d

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0oNL6ow4d5uDjB5Kaicrb5sVZHmdd6FpVIUm8mBAdwEsUhibcsGo9hfo9w/640?wx_fmt=png&from=appmsg)

4、最后一步打开系统，默认端口 3000，默认账号密码 admin/admin，就能看到优美的效果图啦：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0oUGVUP9and0LAHP1h7vJxjp3prhLDO6eNOibpsFUd53z71eA55TSZVyQ/640?wx_fmt=png&from=appmsg)

以上就是今天的内容，有兴趣的可以自己去玩玩，用在企业内部资产可视化，是个不错的选择。

### 关于信安之路目前的几款产品定位及介绍

**成长平台**：适合小白入门、锻炼自学能力、总结能力、沉淀技术基础等场景，通过体系化的任务设置，开放性的任务要求，其他同学报告共享等方式，提升自学、总结、知识沉淀等能力，让自己在竞争中获得一些优势。

**信安之路知识星球：**稳定运营 7 年，历史沉淀三千多主题，两千多份文档，内容丰富，还能同时解锁成长平台和内部文库账号，目前正值年度特惠期间，加入仅需 299，原价 512。

**渗透测试那些事儿**：专注于渗透测试相关内容分享，包括信息收集、通用漏洞 POC、黑盒测试方法、技巧等内容，加入可解锁成长平台账号以及内部文库部分内容，目前正值年度特惠期间，加入仅需 128，原价 168。

**内部文库**：上线近三年，累计积累两千份文档，其中私密内容已有一千七百多份，均已体系化的内容方式呈现，试看目录：https://wiki.xazlsec.com/static/forder.html

![](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfcs91MOplZ8f52zvfgAkH0ogOoxcZoyDIygbjqsqAQgrLVZ6YSNIOFBnWEeUrbHDkKjMjZuH34r5A/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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