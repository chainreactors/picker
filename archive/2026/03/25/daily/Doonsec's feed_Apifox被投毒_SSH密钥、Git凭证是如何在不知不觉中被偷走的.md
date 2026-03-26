---
title: Apifox被投毒:SSH密钥、Git凭证是如何在不知不觉中被偷走的
url: https://mp.weixin.qq.com/s/3Pa5_-4eTPiYYjR3AN4eUA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:14.702853
---

# Apifox被投毒:SSH密钥、Git凭证是如何在不知不觉中被偷走的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nX68dP9Wa1ZJVFqU31ruCv1ktXIHcFetXp9IkiaRXGYwbzY3P914Q3nnukFb2FqpM2zS8Tkia97AdJnvLZLu65DKkwlVWlP9q41OJLaPWnIog/0?wx_fmt=jpeg)

# Apifox被投毒:SSH密钥、Git凭证是如何在不知不觉中被偷走的

原创

我真tm厉害
我真tm厉害

黑客茶话会

![]()

在小说阅读器中沉浸阅读

# [紧急预警] Apifox被投毒:SSH密钥、Git凭证是如何在不知不觉中被偷走的

**导语：**近日，工作中监测到Apifox文件存在被投毒情况。攻击者利用官方CDN篡改JavaScript文件，悄无声息地窃取SSH密钥、Git凭证等敏感信息，数百企业内网面临沦陷风险。

## 一、事件背景

Apifox是一款API一体化协作平台，其桌面端应用基于Electron框架开发。然而，由于未严格启用sandbox参数，导致Node.js API接口暴露，为攻击者提供了可乘之机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nX68dP9Wa1b4CxT7jeOgkIQLaSo6icLib7KB81mWQX6ndawaice4XTVIHysib1HMy7Glficx7ORkyKSgyVIYAxVguR3BZ2vyWb8hyo08LSYiatblk/640?wx_fmt=png)

图1：Apifox供应链投毒事件预警

## 二、攻击原理剖析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nX68dP9Wa1YczWcc3WNnOEUwxsvibYdppvUE4tibibk0ibOZkVrCFHpPCSQXEr7ATDEtDBusdOicnmDoXmd9m6pLeTXxTTlLCIxqhBmlVUKf7src/640?wx_fmt=png)

图2：Apifox供应链投毒攻击流程

### 攻击链分析

攻击者精心设计了以下五步攻击链，环环相扣，最终实现敏感数据的静默窃取：

**第一步：CDN篡改** — 自3月4日起，攻击者对官方CDN进行投毒，将正常的apifox-app-event-tracking.min.js（约34KB）替换为投毒版本（约77KB）。由于是官方域名分发，用户毫无察觉。

**第二步：恶意脚本加载** — 投毒后的JS文件会从恶意域名apifox[.]it[.]com拉取apifox-event.js恶意脚本，整个过程在后台静默执行。

**第三步：敏感信息收集** — 恶意脚本开始静默收集主机敏感信息，包括SSH密钥、Git凭证（账号密码/Token）、命令行历史、进程列表等开发者核心资产。

**第四步：数据外传** — 收集的数据被上报至hxxps://apifox[.]it[.]com/event/0/log，攻击者坐等收网。

**第五步：横向渗透** — 攻击者利用窃取的SSH密钥登录服务器、Git凭证拉取代码仓库，下载并执行后门程序，实现对系统的完全控制，并进行内网横向移动。

## 三、后果有多严重？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nX68dP9Wa1bMRxKhXK3rsUaCF2OBTwvd6Oiaa8pP0Oic2sHKdbJjPc7JWLelw2HdI8DmxciaN3OwzqHZlxmUMRqkAo6aZz4Z2566uNmx8SeVt4/640?wx_fmt=png)

图3：Apifox投毒事件影响分析

| 后果类型 | 具体危害 |
| --- | --- |
| SSH密钥泄露 | 攻击者可直接登录你的服务器，植入后门、拖走数据、控制整个业务系统 |
| Git凭证泄露 | 代码仓库被攻击者访问，核心代码被窃取或篡改，甚至可能植入恶意代码 |
| 内网横向移动 | 以被控主机为跳板，渗透整个内网，威胁企业核心数据资产 |
| RCE远程代码执行 | 攻击者可执行任意代码，完全接管受害主机 |

**⚠️ 如果你中招了：**

* SSH密钥可能已泄露 → 立即更换SSH密钥，检查服务器登录记录
* Git凭证可能已泄露 → 立即重置Git账号密码/Token，检查代码仓库访问记录
* 内网可能已被渗透 → 全面排查内网安全设备日志

## 四、影响范围

| 维度 | 情况 |
| --- | --- |
| 影响时间 | 2026年3月4日起 |
| 恶意脚本大小 | 77KB（正常约34KB） |
| 恶意域名 | apifox[.]it[.]com |
| 平台覆盖 | Windows/macOS/Linux全平台 |
| 受影响用户 | 3月4日后未更新Apifox桌面端的所有用户 |

## 五、恶意域名汇总（立即阻断）

**请立即在防火墙/DNS/Hosts中阻断以下域名：**

* apifox[.]it[.]com
* cdn[.]openroute[.]dev
* upgrade[.]feishu[.]it[.]com
* system[.]toshinkyo[.]or[.]jp
* ns[.]feishu[.]it[.]com

## 六、应急响应与防护指南

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nX68dP9Wa1bzL8GXUHIFF8d93EQG9P3iaXmRe7yBAZQAPCFribF2ibSh2fbnRXVQZ3cxRgCBTf0eJTDTQs9b9WqpkD9RJT2GZ1jHljLvtj8lv8/640?wx_fmt=png)

图4：Apifox投毒应急响应与防护指南

### 立即执行（按顺序）

1. **第一步：升级Apifox** — 升级至v2.8.19或更高版本，新版已将脚本内置，避免远程加载
2. **第二步：阻断恶意域名** — 在防火墙/路由器/Hosts文件中阻断上述所有恶意域名
3. **第三步：更换SSH密钥** — 立即生成新的SSH密钥对，删除旧的公钥，更新所有服务器的authorized\_keys
4. **第四步：重置Git凭证** — 立即修改Git账号密码，重置所有Token，检查仓库访问记录
5. **第五步：排查安全日志** — 检查防火墙、安全设备的日志，排查是否有异常连接

### 长期防护建议

* 定期更新Apifox至最新版本，保持安全防护
* 启用企业防火墙的域名过滤功能，阻断未知CDN域名
* 对开发环境实施网络隔离，降低横向渗透风险
* 建立供应链安全审查机制，谨慎使用第三方CDN资源
* 敏感操作使用硬件Token或短时效凭证

## 七、事件时间线

| 时间 | 事件 |
| --- | --- |
| 3月24日10时52分 | 使用窃取的 PyPI 令牌上传偷毒后的v1.82.8 |
| 3月24日13时03分 | 官方确认影像版本，攻击者关闭issus试图压制舆论 |
| 3月24日20时15分 | 下架恶意版本，解除隔离 |

**关键要点：**

* Apifox供应链投毒是一起典型的CDN投毒攻击，攻击者利用官方可信域名分发恶意代码
* 攻击者真正目标是SSH密钥、Git凭证等开发者核心资产
* Electron应用的sandbox配置缺失是此次攻击的技术根因
* 即使是你每天都在用的工具，也可能成为攻击者的入口

**行动建议：**如果你的Apifox是3月4日后更新的版本，请立即：1)升级到最新版 2)阻断恶意域名 3)更换SSH密钥和Git凭证。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

黑客茶话会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

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