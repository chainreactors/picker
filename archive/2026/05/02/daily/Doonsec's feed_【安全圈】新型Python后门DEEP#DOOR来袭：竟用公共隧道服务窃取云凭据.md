---
title: 【安全圈】新型Python后门DEEP#DOOR来袭：竟用公共隧道服务窃取云凭据
url: https://mp.weixin.qq.com/s/hqODJsK-1pdkeKSkYp_P0w
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:45.716014
---

# 【安全圈】新型Python后门DEEP#DOOR来袭：竟用公共隧道服务窃取云凭据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyH4fg3UuJxefaMJmDLRUqiak7EQzl8ut0ZXntdfNQiaFyia8fUXJqo2gLLnHhicqIZJSB5LZrTVWXtmicPyIRgBXz5ZSGicGCpOibSl0g/0?wx_fmt=jpeg)

# 【安全圈】新型Python后门DEEP#DOOR来袭：竟用公共隧道服务窃取云凭据

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Python后门

> 安全研究人员发现一款名为DEEP#DOOR的Python后门框架，竞然利用公共TCP隧道服务bore.pub进行C2控制，可窃取浏览器和云凭据（AWS、Google Cloud、Azure）。当前攻击似乎有限，但具备高度模块化，值得警惕。

---

威胁概述

| 项目 | 详情 |
| --- | --- |
| **恶意软件** | DEEP#DOOR（Python后门框架） |
| **开发语言** | Python（嵌入式） |
| **C2通道** | bore.pub（公共隧道服务） |
| **目标** | 浏览器凭据、云凭据、SSH密钥 |

Securonix安全研究团队发现了这个高度隐蔽的后门框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyHDh8hcZM5DthibjiaKKJLcZsiaKXetVLGvoBTLpAHPjDKkbYx7lq9tNWtmTI5SFXiayJyibfO39dI78ib1fib3FTYw7FXFQ98SVhk6Og/640?wx_fmt=png&from=appmsg)

---

攻击链分析

### 入侵方式

攻击从**batch脚本**（install\_obf.bat）开始：

1. 💻 禁用Windows安全控制
2. 🐍 动态提取嵌入式Python payload（svc.py）
3. 🔄 通过多种机制建立持久化：

* Startup文件夹脚本
* 注册表Run键
* 计划任务
* WMI订阅（可选）

### 核心特点

**无文件落地**：Python payload直接嵌入在dropper脚本中，运行时提取重建，大大减少外部依赖和传统检测机会。

---

功能清单

一旦部署，DEEP#DOOR可以：

| 功能 | 说明 |
| --- | --- |
| 🎯 **反向shell** | 远程执行命令 |
| 🔍 **系统侦察** | 收集主机信息 |
| ⌨️ **键盘记录** | 记录用户输入 |
| 📋 **剪贴板监控** | 窃取复制内容 |
| 📸 **屏幕截图** | .capture屏幕 |
| 📷 **摄像头访问** | 遥控摄像头 |
| 🎤 \*\* Ambient录音\*\* | 环境监听 |
| 🌐 **浏览器凭据** | Chrome、Firefox |
| 🔑 **SSH密钥** | 提取SSH密钥 |
| ☁️ **云凭据** | AWS、GCP、Azure |

---

C2新玩法：公共隧道服务

### 为什么用bore.pub？

传统C2需要自己搭建服务器，但DEEP#DOOR选择公共隧道服务**bore.pub**：

* ✅ 无需搭建专属基础设施
* ✅ 流量混入正常 traffic
* ✅ 不在payload中嵌入服务器信息

**优势**：减少特征，快速切换目标。

---

防御规避

DEEP#DOOR具备大量反分析和防御规避机制：

| 机制 | 功能 |
| --- | --- |
| 🏃 **检测** | 沙箱、调试器、虚拟机检测 |
| 🔧 \*\* patching\*\* | AMSI、ETW patching |
| 🔓 **NTDLL unhooking** | 绕过安全检测 |
| 🛡️ **Defender干扰** | Microsoft Defender篡改 |
| 🚫 **SmartScreen绕过** | 绕过安全警告 |
| 🧹 **日志清除** | PowerShell日志抑制 |

---

持久化机制

多个自动持久化路径：

* 📁 Startup文件夹脚本
* 🔑 注册表Run键
* ⏰ 计划任务
* 🔄 看门狗机制：自动重建被删除的持久化文件

**难以清除**：即使删除也会自动恢复。

---

现状评估

根据Securonix研究：

> "当前观察到的攻击似乎有限且有一定针对性，而非大规模广泛传播。"

但由于框架的**模块化特性**，不同威胁参与者可能 adaptation 用于各种用例。

---

防御建议

1. 🔒 强化终端检测和响应（EDR）
2. 📊 监控异常Python进程
3. 🌐 监控bore.pub等公共隧道服务的异常连接
4. 🔑 加强云凭据保护（多因素认证）
5. 📝 定期审计启动项和计划任务

***END***

阅读推荐

[【安全圈】热门 WordPress 重定向插件暗藏休眠后门多年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076105&idx=1&sn=014791e35769c28ca8e691db19b0fbfe&scene=21#wechat_redirect)

[【安全圈】开源电子病历软件 OpenEMR 发现 38 个漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076105&idx=2&sn=69e1060f56966577b4e2d2a05cebb8cb&scene=21#wechat_redirect)

[【安全圈】有缺陷的 VECT 2.0 勒索软件对大文件充当数据擦除器](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076105&idx=3&sn=632d44c8e211f46eb699616473906d78&scene=21#wechat_redirect)

[【安全圈】Linux 内核潜伏 9 年漏洞披露：732 字节脚本攻破 Ubuntu 等发行版，提权至 root 最高权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076090&idx=1&sn=955f8155ca08aea02fa3e25775c3bcf4&scene=21#wechat_redirect)

[【安全圈】cPanel被曝惊天高危漏洞，千万级服务器面临“裸奔”，官方紧急发布补丁！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076090&idx=2&sn=e5ba8445daca48ad1bb3795002895e7c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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