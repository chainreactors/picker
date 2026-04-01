---
title: Claude Code 源码泄露? Github瞬间20K STAR(附项目地址)
url: https://mp.weixin.qq.com/s/cPN-ZgCc0xSvygdbKZzOtg
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:42.667837
---

# Claude Code 源码泄露? Github瞬间20K STAR(附项目地址)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/De3yb4u5JSr6xquZk16rEAtKP0rCWLQObX8ibTjQ6rpCmzR5B0VbqKb6HmVmseRBQ5P6lw4Dl2rMv3D41nUES3JtFhiaxqeFUIx06IQe7Pc44/0?wx_fmt=jpeg)

# Claude Code 源码泄露? Github瞬间20K STAR(附项目地址)

星悦安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSph08n9OHqRUcazHKeHegPcuWmEgVx3PYd6IBBMWkS5SNGEtgxQSmlRtvSHt7Aq7QuN4hbAFMIH6DSlNkMATPpLWAwUNRibh6ZQ/640?wx_fmt=png&from=appmsg)

# 截止2026.3.31 20:52分 已有 20.6K Star

# Claude Code Python 移植工作区

> 此仓库的主代码`src/`树现在专门用于**Python 移植工作**。2026 年 3 月 31 日 Claude Code 源代码的公开是项目背景的一部分，但跟踪的仓库现在以 Python 源代码为中心，而不是公开的 TypeScript 快照。

## 端口状态

主源代码树现在是 Python 优先的。

* `src/`包含活跃的 Python 移植工作区
* `tests/`验证当前 Python 工作区
* 已公开的快照不再是受跟踪存储库状态的一部分

当前的 Python 工作区还不能完全一对一地替代原系统，但主要的实现界面现在是 Python。

## 为何要进行这次重写

我最初研究公开的代码库是为了了解其框架、工具连接和代理工作流程。但在深入思考了法律和伦理问题之后——并且阅读了下面链接的文章之后——我不希望公开的快照本身继续作为主要的跟踪源代码树。

该仓库现在专注于Python移植工作。

## 存储库布局

```
.├── src/                                # Python porting workspace│   ├── __init__.py│   ├── commands.py│   ├── main.py│   ├── models.py│   ├── port_manifest.py│   ├── query_engine.py│   ├── task.py│   └── tools.py├── tests/                              # Python verification├── assets/omx/                         # OmX workflow screenshots├── 2026-03-09-is-legal-the-same-as-legitimate-ai-reimplementation-and-the-erosion-of-copyleft.md└── README.md
```

## Python 工作区概述

目前，新的 Python`src/`树提供：

* **`port_manifest.py`**— 总结了当前的 Python 工作区结构
* **`models.py`**— 子系统、模块和积压状态的数据类
* **`commands.py`**— Python 端命令端口元数据
* **`tools.py`**— Python 端工具端口元数据
* **`query_engine.py`**— 从当前工作区渲染 Python 移植摘要
* **`main.py`**— 用于清单和摘要输出的 CLI 入口点

## 快速入门

### OmX工作流程截图

![OmX 工作流程截图 1](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSp4DCyZrL6Icxe6sz5Yhalib6w9pFIdPHFhDh4NibhlAOoFFHN40jhWZZZ6moNG9R74jZ8pickdZA3p45yTYWKl5GgFkdAxJg9OZk/640?wx_fmt=png&from=appmsg)

项目地址：https://github.com/instructkr/claude-code

## **0x01 源码备份下载**

****标签:代码审计，0day，渗透测试，系统，通用，0day，闲鱼，交易所****

******源码备份关注公众号发送 260331 获取.******

******免责声明:****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由读者承担全部法律及连带责任，文章作者和本公众号不承担任何法律及连带责任，望周知！！!******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

星悦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

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