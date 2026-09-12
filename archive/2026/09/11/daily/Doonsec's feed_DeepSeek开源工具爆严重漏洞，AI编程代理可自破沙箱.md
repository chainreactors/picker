---
title: DeepSeek开源工具爆严重漏洞，AI编程代理可自破沙箱
url: https://mp.weixin.qq.com/s/ISKAINAr_SMsnDsfG9ldfQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:21.021632
---

# DeepSeek开源工具爆严重漏洞，AI编程代理可自破沙箱

# DeepSeek开源工具爆严重漏洞，AI编程代理可自破沙箱

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OOY7nSRHcyib7K5XkIvOAFzWNxY5xnVAoFJoibJiaZqKmDvqopGdIOvJg1ZwrVgngY2DdPtPnao8k0TNja3CYNmicbMfRRPULcCEA/640?from=appmsg)
> **导语**：安全研究机构OX Security近日披露DeepSeek Harness一枚高危漏洞（CVE-2026-82533）。攻击者只需构造恶意文本诱导AI代理读取，即可令其执行单条命令关闭自身文件沙箱。CVSS评分9.4，npm仓库首个修复版本迟到3天。

---

## 一、漏洞速览

**漏洞编号**：CVE-2026-82533 **CVSS 3.1评分**：9.4 / 10（严重） **向量**：CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

**一句话描述**：DeepSeek Harness本地Web接口缺少认证，AI代理可通过工具自身接口将会话切换至"danger-full-access"模式，从而关闭文件沙箱并移除审批提示。

**风险等级**：🔴 严重

---

## 二、影响实体

| 项目 | 详情 |
| --- | --- |
| **受影响厂商** | DeepSeek |
| **受影响产品** | DeepSeek Harness（AI编程代理运行工具） |
| **影响版本** | v0.1.1-rc.2 及更早版本 |
| **修复版本** | v0.1.2-alpha.2（首个推送至npm的修复版本，2026-08-30） |
| **当前稳定版** | v0.1.2-rc.1（2026-09-03） |

> ⚠️ **注意**：v0.1.2-alpha.1虽包含修复，但从未发布至npm仓库，用户无法通过官方指令从npm安装该版本。

---

## 三、漏洞原理

### 3.1 沙箱机制

DeepSeek Harness在操作系统层面为AI代理命令提供文件沙箱。默认配置下，写操作仅允许在代理工作区和临时文件夹内执行；**读取和网络访问不受限**。

工具同时为代理Shell提供本地Web接口地址及当前会话ID，代理可直接访问该接口。

### 3.2 认证缺失

本地Web接口**完全无认证**。判断请求是否可到达该接口的逻辑（`api-request-trust.ts`）仅读取请求的Host请求头，不校验连接来源。这意味着同一台机器上的任何进程均可通过伪造Host头冒充本地访问。

> 代码注释明确指出："This is not an auth layer"（这不是认证层）。

### 3.3 攻击链

1. 攻击者构造恶意文本，包含诱导代理调用本地接口的指令
2. 代理读取该文本，向本地接口发送请求，将会话模式切换为"danger-full-access"
3. 该操作**不触发审批提示**（因未申请超出当前权限范围的访问）
4. 沙箱关闭，后续命令可在工作区外执行

安全厂商VulnCheck验证：两个默认配置会话执行相同命令，经接口调用切换模式的会话成功在沙箱外写入文件，另一个被拦截。

### 3.4 额外风险

攻击者利用同一接口可**无需密钥下载会话完整日志**，获取所有历史对话记录。

---

## 四、修复方案

### 4.1 升级（首选）

```
npm install -g @deepseek-ai/dsh@latest
```

确保版本 ≥ v0.1.2-alpha.2。

> ⚠️ **补丁风险**：无已知业务中断报告，但建议在非生产环境验证后再全量部署。

### 4.2 临时规避（无法升级时）

* 使用工具时，**停止Web界面**；用完即关闭
* 移除任何通向接口的隧道、代理或端口转发（SSH转发、编辑器端口转发等）
* 限制工具监听地址**不能防御**该攻击——代理已在同一台机器上

> ⚠️ **警告**：默认本地安装下，暂无从沙箱内部阻止该逃逸的方法。

### 4.3 桌面应用用户

第三方桌面应用（如Windows桌面版）自行打包Harness版本。请检查其使用版本：

* 确认已升级至含修复的版本（如 v0.1.3-alpha.1）
* 截至2026-09-06，Links2008/DeepSeek-Harness-Desktop已升级至v0.1.3-alpha.1

---

## 五、关于DeepSeek Harness的局限性

官方安全声明明确指出：

> "DeepSeek Harness**未经过安全审计**，沙箱和审批提示**不保证隔离或阻止损害**。请勿将此工具作为处理不可信工作的唯一安全控制。"

该工具的沙箱**仅覆盖文件**，读取和网络访问不受限；代理Shell仍接收本地接口地址。修复后（v0.1.2-rc.1）这些限制依然存在。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图来自The Hacker News授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NS2vw8zP8l4q26jfMa8cEpjDicQuO6Zu8nZQQd0g2J3jZVdC4ojPicuwxibz8DNcP0EIqU5VOj7yodNTgAodlIwLzBgEl7js2Xnk/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PzRoeBj5h4TTjDrErtTFU4VFK1OKm2z3PLtGX6QmhYb9kdlWGKjzZYdmSKpdiaibhPjk6HELDKVnCdw7Dic76zia4R6tuLsIG3fGc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P5DAdKXwzp9dynnPDTLQoRgaTyUYR0FRolETaKsiadiamkoicukQ0jibmORdyvUcqjZfZbyia5GYogtl8T1iaL9dnfJ5E5o3vPc8qlA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OicTibQC25bMeFHjbhLibVsk9c3UIric96vLWE3gY1HfTp1e0WMGPTrp6Lr8wJkUFLA4NrXHqKt5dmNMbIB3RGrRiavOHbfs8jMEVc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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