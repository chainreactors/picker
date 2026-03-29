---
title: Ansible Playbook 基础知识
url: https://mp.weixin.qq.com/s/DPHNXe8XFnfwHBDykauYIw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:41:45.890733
---

# Ansible Playbook 基础知识

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dibzmm9niba055giaKgaWIP9uP7B3of9EuJIOLy9TrcMbA52LfqRHQ77FvCMYflcNX5WsYCRD6PW3udK7micXYVND4NbUY9Xapol2kCcVEso9Y4/0?wx_fmt=jpeg)

# Ansible Playbook 基础知识

原创

Lino
Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

本节我们来学习 Ansible Playbook 基础知识。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05QlUngpBCHImiccy0WulgDB2Y06We8qK9F2CtNhlYlGUWqUEJ2vSNEOeRCp0R2prWQfgOUvagVqTmTd2M7Ka2PObNFCBXIA1ZI/640?wx_fmt=png&from=appmsg)

Playbook 是由一个或多个 "play" 组成的列表。如果把自动化比作一场戏，**Play** 决定了在哪台机器（Hosts）上演，而 **Tasks** 就是具体的剧本动作。

## YAML 结构与 Play 层次

YAML 对空格极其敏感。一个基础的 Playbook 包含以下层级：

* Play 级别：定义目标主机（hosts）和执行用户。
* Tasks 级别：定义要执行的具体模块（如 ios\_command）。
* Handlers 级别：由任务触发的特殊任务，通常用于重启服务或保存配置。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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