---
title: Ultralytics遭供应链投毒攻击，模型训练恐成挖矿！
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247513239&idx=1&sn=cb6b7ec1d59519a7949572b1b4f467b3&chksm=ea6643e0dd11caf68f73a09d94bd3938c23c7f72debb0503b130dec0e8c72f92cbe3c70c6753&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-12-07
fetch_date: 2025-10-06T19:39:49.770580
---

# Ultralytics遭供应链投毒攻击，模型训练恐成挖矿！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTxT09h3hVZIUBRMtwGS0yPWREyOztaU0EXsUvD3ycsTNfEbCR8F4vrw/0?wx_fmt=jpeg)

# Ultralytics遭供应链投毒攻击，模型训练恐成挖矿！

原创

威胁情报中心

奇安信威胁情报中心

事件概述

奇安信威胁情报中心在日常威胁狩猎中，发现一起恶性供应链投毒事件。由Ultralytics团队开发的YOLO11模型框架项目 ultralytics 遭恶意投毒，用户在使用pypi安装最新的v8.3.41版本时，机器将被植入挖矿木马，我们建议使用了该项目的用户尽快进行自查。

Ultralytics是一个开源的计算机视觉、深度学习和人工智能项目,旨在提供易于使用的工具和库,以帮助开发人员训练、评估和部署深度学习模型。‌此项目目前在github的标星数量达33.6k，具有较多的用户量。

从12月5号开始，Ultralytics的github项目上陆陆续续有人反馈问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPT5M4B1BbztKicHRY1pQ7QK1GUfr2qpeTwI5MRRqn4UqdZ7GkG6NoFdPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTibmw72UkzxfFP8hWRAkBAB7rVYc24yabbffnyvMpqH0DyrYjLqb0pqw/640?wx_fmt=png&from=appmsg)

投毒分析

本次供应链攻击中被投毒的是Pypi上的Ultralytics 库8.3.41版本，下载地址为：

hxxps://files[.]pythonhosted.org/packages/d0/99/13d92174aa6a470d348a95e31164769f2cdf77838ea3c3e3fd476285777d/ultralytics-8.3.41-py3-none-any.whl

具体被投毒文件为：

* ./ultralytics/models/yolo/model.py
* ./ultralytics/utils/download.py

攻击者在model.py文件的YOLO类中添加了额外的下载代码，当用户进行YOLO类初始化时，根据操作系统类型不同将分别请求以下链接：

* https://api.github.com/repos/ultralytics/ultralytics/git/blobs/665bb8add8c21d28a961fe3f93c12b249df10787
* https://api.github.com/repos/ultralytics/ultralytics/git/blobs/ 5e67b0e4375f63eb6892b33b1f98e900802312c2

下载攻击者上传的挖矿程序，落盘名为ultralytics\_runner

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTKUyUIsDDN8v7Rzln75rb2NGPRGP7ic2qn460ArrkLNlI5loTcvK294A/640?wx_fmt=png&from=appmsg)

在download.py文件中，攻击者额外增加了名为safe\_run的函数，其中内置了钱包地址与矿池地址，在正常版本的download.py文件并不存在该函数，安装程序在下在落盘挖矿木马后，将以内置的钱包地址与矿池地址作为参数启动, 然后即开始进行挖矿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTIGAtZcKNSicNpf2sLx3kaG2Z7EvZgYKZhpARlm2TOzQwlCgzu9QdpLw/640?wx_fmt=png&from=appmsg)

截至2024-12-05 18点, 受感染的 Ultralytics 版本已从 PyPi 中删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTnl8Y1DmeKYs2Cxo4NlQLibzibBZGecac8NKibicUTDlevBu5ichj0MouMGw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTibe4h6ticj5yNbbKexKGibicP5dIqickEYic4kFW05cLPI1YVW3VxKJAnPiaA/640?wx_fmt=png&from=appmsg)

自查方案

1. 使用pip工具命令进行ultralytics包版本查询，此次投毒事件影响版本为v8.3.41：

```
pip list
```

2. ultralytics可能作为ComfyUI-Impact-Pack等其他软件包的依赖项自动安装，此类情况仍可使用pip命令进行版本排查。

3. 由于pypi镜像源的存在，在pypi安装ultralytics包时推荐使用8.3.40以及之前的版本：

```
pip install ultralytics==8.3.40
```

4. 由于github仓库源码未被污染，也可通过指定github安全安装：

```
pip install git+https://github.com/ultralytics/ultralytics.git
```

IOC

**MD5**

ECE94F77F6BAE2E5DA89E97AC1522101

EB5506148A2D59F6D7A0DB4725DB1F05

BDA5BC07B3579CCA96D5AA5A88C096B4

8F4FFF0DED94F1141768220906ABFBB8

**URL：**

https://api.github.com/repos/ultralytics/ultralytics/git/blobs/665bb8add8c21d28a961fe3f93c12b249df10787

https://api.github.com/repos/ultralytics/ultralytics/git/blobs/ 5e67b0e4375f63eb6892b33b1f98e900802312c2

**矿池域名**

connect.consrensys.com

**钱包**

4BHRQHFexjzfVjinAbrAwJdtogpFV3uCXhxYtYnsQN66CRtypsRyVEZhGc8iWyPViEewB8LtdAEL7CdjE4szMpKzPGjoZnw

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehicibOI7icJwSaZBPXUmh28wLPTiaYibK0Wy5wewqjMUOnZVVbkezIXHDn4bbJiburMAic0bsWatjkh0R7ichg/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 7.0**

即刻助力威胁研判

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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