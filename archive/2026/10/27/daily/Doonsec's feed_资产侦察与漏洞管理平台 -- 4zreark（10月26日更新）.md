---
title: 资产侦察与漏洞管理平台 -- 4zreark（10月26日更新）
url: https://mp.weixin.qq.com/s/YvqIWnIoc9GZFgzp56V2yA
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:46:14.978666
---

# 资产侦察与漏洞管理平台 -- 4zreark（10月26日更新）

# 资产侦察与漏洞管理平台 -- 4zreark（10月26日更新）

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

资产侦察与漏洞管理平台：从企业/域名种子出发做资产展开、企业股权穿透、数字资产采集、指纹与服务识别、漏洞复核，并把结果归并成可检索、可下钻的资产图谱。任务：

```
项目种子
  └─ 巡航计划 / 手工任务
       └─ TaskService.Create
            └─ River 入队（按 task_id 唯一）
                 └─ master 取 job → NodeHub.Dispatch(capability)
                      └─ WebSocket 下发 scan 指令
                           └─ worker 拉任务 → StreamingPipeline
                                └─ 子域 → 接管 → 端口 → 指纹 → 爬虫 → 目录 → 敏感 → 漏洞
                                     └─ 结果/资产/路由回传 → master 落库
```

**0x02 安装与使用**

一、环境要求

```
- Go **1.26.3+**- Node.js 20+（建议 22）- PostgreSQL **16**- Linux 建议安装 `ca-certificates`、`tzdata`
```

二、初始化数据库

```
createuser zre --pwpromptcreatedb -O zre zrearkpsql -d zreark -c 'CREATE SCHEMA IF NOT EXISTS zre AUTHORIZATION zre;'
```

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20261027获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U7LDNXUGXQvxMTm2RMVbQWjJu8QKNicspVHqtJ76WbXIFHkXWHGlN2yU6kfKqsU6GCia0ZOkRRp6GXRsF2iaOBvNgz6n7eq1mayJRNEcBwpds0/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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