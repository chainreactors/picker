---
title: Kerberos TGT Monitor BOF —— 持续监控Kerberos票据的工具
url: https://mp.weixin.qq.com/s/4tUw1uczYEqU6dOvQ78tXg
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:54:18.262240
---

# Kerberos TGT Monitor BOF —— 持续监控Kerberos票据的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeXkdD8j57eTUrz4ibcJweDswkQGMdYCFt8ZiaImXiaibRLGBltkqKiaU0dcJ5ibFu4dh0nPZIZJl1Xa8q7a8y0RibehoUc90e1kCX4RE/0?wx_fmt=png&from=appmsg)

# Kerberos TGT Monitor BOF —— 持续监控Kerberos票据的工具

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Kerberos TGT Monitor BOF是一个异步的Beacon Object File，可以在后台持续监控LSA票据缓存，一旦侦测到新的Kerberos TGT，就唤醒Beacon并输出base64编码的kirbi文件，方便做接力传递票据攻击。需要Conquest框架支持，以SYSTEM权限运行。

## 01 工具概述

做内网横向渗透的人都知道Rubeus的monitor命令——它一直盯着LSA缓存，一有新的TGT就给你抓出来。但Rubeus是完整的执行文件，在某些场景下不够灵活。现在有个更轻巧的方案：**Kerberos TGT Monitor BOF**。

这是一个异步的Beacon Object File（BOF），专门用来监测Kerberos登录事件。它跑在后台，定期检查系统的LSA票据缓存。只要发现新的TGT，立刻打印票据元数据，同时输出base64编码的kirbi文件——这个文件可以直接扔给Rubeus做pass-the-ticket攻击。

> 注意：这个BOF必须配合异步对象文件加载功能使用，因为它依赖BeaconWakeup API来强制agent回连。Conquest框架（https://github.com/jakobfriedl/conquest/）正好提供了这个能力。

## 02 核心功能

* 持续轮询LSA缓存，默认60秒一次（可自定义）
* 检测新TGT时主动唤醒agent
* 输出用户名、域名、票据时间等元数据
* 输出base64编码的kirbi文件，直接用于传递票据
* 支持过滤特定用户名——只监控某台机器或某个用户的TGT

## 03 安装与使用

你需要先确保运行环境是**NT AUTHORITY\SYSTEM**权限。然后传两个参数：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| interval | int | 轮询间隔（秒） |
| targetUser | string | 目标用户名（不区分大小写）。只监控该用户的TGT；不填则监控所有用户。注意计算机账户末尾要加$ |

为了方便，这个仓库还提供了一个Conquest Module，用起来更简单：

tgt-monitor --interval 5 --user DC01$

示例中设置间隔5秒，只监控DC01$这台域控的机器账户。执行后你会看到类似下面的输出：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdiaBbup6xdI133HDciarNu3GxcVTIl9usXGOWqFSj31VVic40HVypSTOPLtHofibX9m0kJEDOHVkib5a3GPdicplAu46ibDtza5BGqDA/640?wx_fmt=png&from=appmsg)

▲ 命令执行示例

## 04 实战演示

当BOF抓到新的TGT时，会打印出完整的票据信息。输出的base64编码kirbi可以直接喂给Rubeus：

Rubeus.exe ptt /ticket:

也可以用impacket-ticketConverter转换格式。在Conquest框架里，直接用ptt命令就能把票据注入当前会话，冒充目标用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc2RQwz977hK8Sibl2eLdtHKxIvB5xmlIxTXkf2O2iaibTsDsgIEyUQ6QcXibmtjw7Qs3Yud5G6Biawrfsicxnzzrib711CStwD9ib3X0A/640?wx_fmt=png&from=appmsg)

▲ 票据注入效果

整个过程不需要落地文件，BOF在内存里执行完就结束，隐蔽性不错。

## 05 优缺点分析

先说优点：轻量，BOF代码几百行，编译出来就几KB；异步检测机制优秀，新票据出现能立刻响应；输出格式兼容Rubeus和impacket，复用成熟工具链。

缺点也很明显：必须依赖Conquest框架，不能用CS原生的BOF加载器；必须以SYSTEM权限运行；只支持Windows系统（废话，Kerberos在Windows上才有LSA缓存）；缺少图形化界面，输出全靠命令行。

## 06 编译方法

编译很简单，进了仓库目录直接敲：

make

前提是你的环境中装了MinGW或GCC for Windows。

## 07 适用场景与推荐指数

这个BOF最适合那些已经部署了Conquest框架的红队团队，用来在域环境中持续捕获高价值票据。如果你手里没有Conquest，可以先去看看它的文档，因为框架本身也很值得研究。

整体推荐指数：⭐⭐⭐⭐（满分五颗星，扣一颗是因为有依赖限制）

**获取方式：私信回复"tgt-monitor-bof"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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