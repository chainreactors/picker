---
title: 【工具推荐】TongWebEJBScan-Burp
url: https://mp.weixin.qq.com/s/iq3zr51hdovTA4lW0zNG7A
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:04.455565
---

# 【工具推荐】TongWebEJBScan-Burp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DRNXoxlicJJvx5iboNT7WOfTHsY6cYUMflBDUM5O0aMHgnH7OYfvcH9ibbjXE4ic17OqMgajF1uFSfxs0hSWKicmibqnAvVBm30j8ibvnf5e1vhTzA/0?wx_fmt=jpeg)

# 【工具推荐】TongWebEJBScan-Burp

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 工具介绍

TongWeb 是北京东方通科技推出的国产 Java EE 应用服务器，在政企、金融、能源等行业的中后台系统中广泛部署，其角色对标 Oracle WebLogic 与 IBM WebSphere。与同类中间件一样，TongWeb 通过 EJB 远程调用协议对外提供业务组件访问能力，而该协议在传输序列化对象时若缺乏类白名单校验，就会形成经典的 Java 反序列化攻击面，可直接导致远程代码执行。

TongWebEJBScan-Burp 是一款针对上述漏洞场景设计的 Burp Suite 被动扫描插件。它在用户正常浏览代理流量的同时，自动对途经的 Host 发起 EJB 协议探测，无需手工逐个测试，发现漏洞后在独立的 Tab 中聚合展示，适合在攻防演练与 SRC 挖掘中批量梳理资产暴露面。

# 安装使用

插件基于 Java 17 编译，使用前请确认 Burp Suite 自带 JRE 版本不低于 17。安装流程为标准的 Burp 扩展加载：

```
下载地址：https://github.com/Axyanzzzz/TongWebEJBScan-Burp/releases/download/V1.0/TongWebEJB-Burp-1.0-SNAPSHOT-all.jar
```

打开 Extensions　Burp 顶部菜单 → Extensions（Extender）Tab，点击 Add在 Installed 子 Tab 中点击 Add 按钮，Extension type 选择 Java，在 Extension file 中选择下载的 JAR 文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJtGzgib4NKUGz2aul5JwnE4XcIbYlk6rJatVx5Frx82OQKThKKtnjDQSEbI9fiax61wrY038yibuxL2EwKvM9GrUUvucMVBMdMfrk/640?wx_fmt=png)

加载完成点击 Next，输出无报错即加载成功，「TongWeb 扫描」Tab 出现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJu839ZzMLzYOSGa4UHTiaIGmSCSDZICCsDcS7AdicZnNadDF6FxVLJhQql2iaNT7jBKiaPCL1U5KaZzsI05p8W52yKWmmLRruzqQia0/640?wx_fmt=png)

使用浏览器访问目标系统，执行登录、跳转、查询等业务操作，插件会自动从代理流量中提取途经的 Host 清单。

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJvLnVFgl8NjVEmficr8tdXqzicvQA1HVibrBCYPAS43qCUPZBvK6qz22Xp0gMtamEFp3HfPEwf59NtbJeR4ia9ibXibbaslPnAFVPQP8/640?wx_fmt=png)

插件对每个新出现的 Host 主动发起 EJB 协议探测，整个过程无需手动干预，不影响业务正常浏览。

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJvjkz5hSia7VEgCg02TbG3iaU0VtUgHk6slURwkQiba0osBjWbYXUyeb4Rd2RbLibDlm1GhD6CIJcBxyVTfXKhxdFTMA03DichF4vKw/640?wx_fmt=png)

# 功能及特点

相较于主动扫描器或 PoC 脚本，本插件主打「流量驱动 + 被动探测」路线，在业务浏览过程中自动完成资产梳理与漏洞验证。核心能力如下：

* Montoya API 原生集成基于 Burp Montoya API 开发，兼容 Burp Suite Community 与 Professional，加载即用，无需额外配置运行时环境。
* 流量驱动被动扫描从代理流量中自动提取 Host 清单，避免手工维护目标列表，适合大型资产梳理场景。
* EJB 协议主动探测对每个 Host 主动发起 EJB 协议探测，通过构造反序列化对象验证 TongWeb EJB 通信链路是否存在类白名单缺失。
* 多策略回显判定采用时间盲注、DNSLog / OOB 回连、异常特征匹配等组合策略，覆盖无回显与有回显两类漏洞场景，降低误报率。
* 独立结果面板独立的「TongWeb 扫描」Tab 聚合展示扫描结果，包含 Host、状态、漏洞证据等字段，便于结果复盘与报告导出。
* 非侵入式探测扫描过程与业务浏览完全解耦，不向目标注入破坏性 payload，适合在生产环境授权测试中使用。
* 轻量分发以单个 JAR 文件分发，Java 17 编译，跨平台运行，无第三方依赖冲突风险。

```
项目地址：https://github.com/Axyanzzzz/TongWebEJBScan-Burp
```

免责声明：本工具仅供安全研究与授权测试使用，请勿用于非法用途。未经授权对他人系统进行任何形式的测试均属违法行为，与作者及本文无关。请严格遵守《网络安全法》《数据安全法》以及目标 SRC 的测试范围约定。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

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