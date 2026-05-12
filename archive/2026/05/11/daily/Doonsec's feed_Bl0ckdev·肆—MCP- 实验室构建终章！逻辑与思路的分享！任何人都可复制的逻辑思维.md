---
title: Bl0ckdev·肆—MCP- 实验室构建终章！逻辑与思路的分享！任何人都可复制的逻辑思维
url: https://mp.weixin.qq.com/s/z38DAAnSKGU6LBVCCMya5g
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:33.253020
---

# Bl0ckdev·肆—MCP- 实验室构建终章！逻辑与思路的分享！任何人都可复制的逻辑思维

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16VegrzH0ks0EaYyCzHlNrgbNpquibd0zxdlSpeoFlub5r89uiaOXLrgYrHiaEJ5cnt0rUI9icHkWCINFkl8AmIWVlic8TlKiahZuBfEQibw/0?wx_fmt=jpeg)

# Bl0ckdev·肆—MCP- 实验室构建终章！逻辑与思路的分享！任何人都可复制的逻辑思维

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> MCP不仅仅是另一个API包装器——它是将你的AI助手从聊天机器人转变为能够访问你整个数字世界的数字工作者的协议。
>
> 二次复现完整的硬件配置：
>
> - 操作系统Windows x64
>
> - 本地开源离线构建
>
> - 显卡：4Gb·8Gb·12Gb
>
> - 逆向Ghidra的基础使用
>
> - 熟悉完整的逆向流程
>
> - 熟悉的使用主流Ai.Claude/Deepseek/Gemini /Chatgpt
>
> - 熟悉完整的红队C2通讯构架和基础的恶意软件分析
>
> ###自动化逆向工程#####
>
> - 一切均在本地执行,自动化代替重复的东西
>
> - 强制使用Disocrd进行分享和交流。
>
> - 可以相互分享自己的mcp服务器/
>
> 2026年,只要有足够的MCP不管是Deepseek和Claude都可以在几个小时内就做出来强大的红队/游戏辅助工具。
>
> Darkesn—微信公众号\_MCP/AI\_逆向工程

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehrqSKyML88rSzIO8SHTISbt4rDKzt5aCwic3lbTgyC3YrianHS2wTx0XVoFK9xWbibKQrGerwtBhV4EkXrUdxExUvFpV81rj0wZ4/640?wx_fmt=png&from=appmsg)

Windows软件获取：[ spacesniffer ] 公众号回复

阅读历史：

0.[Bl0ckdev从零开始手搓MCP服务器：完全本地化运行，没有教程全是踩坑。](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492784&idx=1&sn=3551002bc4cae90e29c00fc20c70d2a1&scene=21#wechat_redirect)

1.[1.MCP 到底是什么？绝对是颠覆性的改变！因为Ai-MCP可以让任何人在 一夜之间把变成游戏作B/逆向工程/渗透.高手](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492803&idx=1&sn=bc9b1c83a9d8843664024b4ea1f042fb&scene=21#wechat_redirect).

2.[Bl0ckdev MCP — 自动化传统的渗透/专注逆向与恶意软件的高级玩法！](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492837&idx=1&sn=adc7eed9468b9957601a0de7aa6e5a63&scene=21#wechat_redirect)

3.[Bl0ckdev-MCP  | 最常规的Docker 安装|需要清楚的知道自己的完整路径。](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492872&idx=1&sn=b8b8d03039ad7c7394b0a5e06d4958f9&scene=21#wechat_redirect)

本文是序列四,也是第五篇文章；这个进度是代表着已经完成了本地安装Docer容器,安装过了Claw Code /并非是**[Claude Code](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492770&idx=1&sn=ae3b3e7d363b1f4398d80b1e3570edb0&scene=21#wechat_redirect),因为我们的一切均是以本地在进行部署,所有数据均属于本地,包括模型也是自己本地量化的。**

整个系列并不是在打造超级智能体,而是在授权给每个爪子应该去做什么,以及他可以做什么,而并非是闷头在大模型里进行无限的叠加。目前Qwen可以很会的回答出一些可重复性的技术,我们只需在自己的MCP服务器中写出自己常用的重复性技能代替即可。

Qwen3.5提供的“键盘记录”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veg4Z0bKPhpJM9EqiaWvZ1F47k9WxGF7EgUmhUC7S42icDylCtJnMo53JM4qeXmfCWDx2ZmDUcmjlnSIr2dl8LsYxgJ9r39wC67h4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRawv7IEW8zl73ahpeFic1tz8iaKS2StViaw0rt4P048n8uv1eB9ic08bHSpSrPiaQsZzBbOYdjoJVMgpfA/640?wx_fmt=png&from=appmsg)

二次复现笔记

1.Claw Code和Claude Code的对比

https://t.zsxq.com/xzmuC

2.**[Docker | 从零开始绝对控制—系统性的设置和备忘录](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492872&idx=1&sn=b8b8d03039ad7c7394b0a5e06d4958f9&scene=21#wechat_redirect)**

https://t.zsxq.com/gWp5Q

3.安装Open webUI

https://t.zsxq.com/WItIk

**4.**安装mcp必备的2个依赖****

https://t.zsxq.com/XGA5m

5.完成一次mcp配置/离线使用

https://t.zsxq.com/fbqYa

下图是逻辑参考

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejFvJHtian6fRoPRjAehOhfVr8OTkuUibutcIWRIGgQmuic1u6TE9iaBRNg9IT4B57L7gibmaUKru1KHlyZNKicOSMo2Php0253PO3qQ/640?wx_fmt=png&from=appmsg)

下边是排序完整的mcp逻辑：

1. 主机
2. MCP客户端
3. MCP服务器
4. Ai调用的工具
5. Ai访问的实际资料和应用服务器

资源：更多内容我推荐阅读官方文档说明书：任何一个新的商业性质的商品和物品都配备了足够从基础到高级应用的说明书。

https://modelcontextprotocol.io/docs/getting-started/intro

图文中心

**创建第一个MCP服务器—用于打通容器和本级**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VehKYGx4azMRQqrkjDKI0QPialVHZzt8BlPMtdJGicxjBL8IStwpFoXss5ho91wwoicRhopdBfvmDaJqbeVW8dwpic4vEXpchzfKA64/640?wx_fmt=png&from=appmsg)

**3.安装必备的2个依赖**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeiaGxj40cFuib9YdUJ5mAA0oW1icC1waOcVMsAtwwJtNFSv35N9b6S0kZ4unib8zqBwhwCwWNmQ9LticHRxtS9yExu5DINEOeXibDBfc/640?wx_fmt=png&from=appmsg)

**Docker安装open-webui|完成一次运行**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejUI9QXwFJeJgJTTVxmfBFlwdrM1ic8mcPplHLGnFXyB8aFOo3Bbb9t7JiaTmbdjOE45uVnxaJPVBxTRM4HSfcFqOxMEiap5hVF0I/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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