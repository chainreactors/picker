---
title: 速修！开源API接口管理平台YApi爆高危漏洞（附补丁链接）
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650174812&idx=1&sn=ba9cbf3e1a073d9c787d840f4af2e7f1&chksm=f4488ee0c33f07f688256918783ef2de6e470f87d471647e9db941d8bc19f315c56705cbd3f7&scene=58&subscene=0#rd
source: 安全威胁情报
date: 2022-11-12
fetch_date: 2025-10-03T22:32:47.481566
---

# 速修！开源API接口管理平台YApi爆高危漏洞（附补丁链接）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTe4shZZN8LSluJ6YTunrrDXfyZJWc76vR2kfLzhml6zk6FFm52HFHYUElWdone6a7rGngIlA9VZg/0?wx_fmt=jpeg)

# 速修！开源API接口管理平台YApi爆高危漏洞（附补丁链接）

原创

ThreatBook

微步在线

经“X漏洞奖励计划”，微步获取到一个YApi高危漏洞信息，无需点击（0-click），无任何权限要求，即可利用。YApi在GitHub上获得超过25000颗星，包括阿里、腾讯、百度、美团等中国一大批互联网公司都在用，可谓影响广泛。**目前微步TDP支持对该漏洞的检出。**

以下为微步情报局对该漏洞的评估结果：

|  |  |
| --- | --- |
| 公开程度 | **PoC未公开** |
| 利用条件 | **无权限要求** |
| 交互要求 | **0-click** |
| 漏洞危害 | **高危**、**权限绕过、命令执行** |
| 影响版本 | **≤1.10.2** |

**漏洞复现**

经微步情报局进行复现，YApi接口管理平台通过注入获取到用户token，结合自动化测试API接口写入待命命令，并利用沙箱逃逸触发命令执行。

☞****获取用户token：****

YApi中某**函数存在拼接，导致MongoDB注入可获取所有token**，包括用户**ID、项目ID**等必要参数。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTe4shZZN8LSluJ6YTunrrDwiayuHq187bCR6Ke8Rzy2uyNe5oQ76lFV4CP4Tb4TxibaOgHfGAXibiaWA/640?wx_fmt=jpeg)

☞**命令执行**

YApi后台的pre-request和pre-response功能存在被利用风险，通过填写脚本，调用自动化测试runAutoTest()时会触发跟进变量被传入了 crossRequest 函数。

然后通过分析sandbox函数可发现vm模块，**利用vm模块构造可逃逸的命令执行数据包达到命令执行效果。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTe4shZZN8LSluJ6YTunrrDOdF6nWGicoibldMXS1QicIKXrFNRiaOKXHHwkv445eVTaFyJ4M1rnGGaOg/640?wx_fmt=jpeg)

经分析，目前**YApi所有版本（包括最新的1.12.0版本）都受此高危漏洞影响，没有例外！**

**时间轴**

1

2022.07.

● 微步“**X漏洞奖励计划**”获取该漏洞相关情报;

2

2022.07.

● 漏洞研究与分析；

3

2022.07.

● **TDP**支持对该漏洞检测；

4

2022.08.

● **OneSIG、OneEDR**支持对该漏洞检测；

5

2022.09.

● **X企业版**支持对该漏洞检测；

6

2022.10.

● 报送监管、厂商、漏洞情报订阅客户；

7

2022.11.

● 补丁发布。

**修复方案**

**目前官方已出修复补丁，以下为下载链接：**

https://github.com/YMFE/yapi/commit/59bade3a8a43e7db077d38a4b0c7c584f30ddf8c

· END ·

点击下方名片，关注我们

觉得内容不错，就点下“**赞**”和“**在看**”

如果不想错过新的内容推送，可以设为**星标**![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTYyCkc91euAiaGULJSbiaHricFHs2dd2sib20WTJKwHYD90Jia9HCKxnmJUwnkicGU7rVP3EYCVh3dMnng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)哦

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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