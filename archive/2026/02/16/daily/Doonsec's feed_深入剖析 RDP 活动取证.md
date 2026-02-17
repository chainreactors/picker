---
title: 深入剖析 RDP 活动取证
url: https://mp.weixin.qq.com/s/R_tHQ_5lVrTn9aQndTrVsw
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:59.078971
---

# 深入剖析 RDP 活动取证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSj2JrIxOrIzOOzrFBdzT4y9NvTWm0zZ2ydTxktLxIkdLOschaYibebdtC0ibB1aZhPylGWiaIdHAtFUKWjP1Kz8EQWynToSQ1el8c/0?wx_fmt=jpeg)

# 深入剖析 RDP 活动取证

sujay adkesar
sujay adkesar

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://thelocalh0st.com/posts/rdp/ | sujay adkesar |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaWRDO2USmTFGcdGceszNQ2g17FibTzjEzbbkKPKhVDgzicVvNr73Bq23AxGcZMNJgNa2HQbwVKyJFibGt5QeK3D96EQIBrgV5R94/640?wx_fmt=png&from=appmsg)

> *"RDP 是一把双刃剑——它提供了无缝的远程访问能力，但一旦落入攻击者手中，就成了入侵的通道。在这篇文章中，我们将追踪 RDP 在事件日志中留下的每一个痕迹。"*

---

## 🧠 RDP 取证分析

远程桌面协议（RDP）是 Windows 环境中最常见的入口点之一——无论是对系统管理员还是恶意攻击者而言。理解 **RDP 相关事件 ID 的链路**使防御者能够重建会话活动、识别未授权访问，并关联登录、重连和注销行为。

本文将拆解 **关键 RDP 事件**，并以**时间线可视化**的方式呈现 RDP 会话的完整生命周期。

---

## 🔐 成功登录：取证线索

当一个有效的 RDP 会话建立时，将触发以下**事件 ID**：

| 事件 ID | 描述 | 日志来源 |
| --- | --- | --- |
| 1149 | 用户身份验证成功 | `RemoteConnectionManager` |
| 4624 (Type 10/7) | 登录成功 | `Security.evtx` |
| 21, 22 | Shell 启动 / 会话登录 | `LocalSessionManager` |

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgsaicdcJJib8THtVicMXAefE2b5qxqiap4eY9sDr4LYIbXyvWgAHuCTzz7sC4a2hmQWUiab7ONdQmwJkYQ34J0iceKT35VDVg48Ojw0/640?wx_fmt=png&from=appmsg)

*RDP 成功登录*

🧠 *提示：*始终关联 1149 + 4624 来确认 RDP 登录。Type 10（RemoteInteractive）是最有力的证据。

---

## 🚫 登录失败尝试

攻击者偏好对 RDP 发起暴力破解攻击。使用以下事件追踪失败的登录尝试：

| **事件 ID** | **描述** | **日志来源** |
| --- | --- | --- |
| 1149 | 尝试已发起（仍会触发！） | `RemoteConnectionManager` |
| 4625 | 账户登录失败 | `Security.evtx` |

🔍 *关注高频率的 4625 事件后紧跟一个成功的 4624——这是暴力破解成功的典型特征。*

---

## 🔁 RDP 会话重连与断开

会话可能因空闲超时或网络中断而断开连接。以下是追踪方式：

| **事件 ID** | **事件含义** | **来源** |
| --- | --- | --- |
| 24, 40 | 会话已断开 | `LocalSessionManager` |
| 4634 | 账户已注销 | `Security.evtx` |
| 4779 | 会话已从 Window Station 断开 | `Security.evtx` |
| 25 | 会话重连成功 | `LSM` |
| 4778 | 会话已重连 | `Security.evtx` |

📌 *事件 40 中的原因代码可以指示断开连接是手动操作、空闲超时还是网络丢失导致的。*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShHRkF8YgRtqLTwlfFRKN9fYd3motZNPBxgBt56myO5U8wy407Cf8wN9aQFcrUP3KKOqMjKQ523sxCibaUzgycAG8miawFMjb2vQ/640?wx_fmt=png&from=appmsg)

*RDP 会话断开（关闭窗口）*

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShWWqFWK5s8stAIiaBaDXMsh71Gia8ZSMAaHqvD5RMNXvjSCX9UrlBvia97ibbyoTIPjJuwuOuY9Hh1icNvmUjqiacnR2icgNyuQHql7o/640?wx_fmt=png&from=appmsg)

*RDP 会话断开（通过开始菜单主动断开）*

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaGMOLHuHPMmGDgXB2gJ95n0BQe5b0PUHjmQIz7yyvOajOJ78ZaoRUxYySiadcCgI31a6jhRawXcJxCh88sTicMJvPuXpk2dJwmU/640?wx_fmt=png&from=appmsg)

*RDP 会话重连*

---

## 🧾 RDP 注销与会话结束

RDP 会话的尾声会记录最终的清理操作：

| **事件 ID** | **含义** | **来源** |
| --- | --- | --- |
| 23 | 注销成功 | `LSM` |
| 4647 | 用户发起注销 | `Security.evtx` |
| 9009 | 桌面窗口管理器已退出 | `System.evtx` |

📎 *使用事件 4647 来区分用户主动注销与强制注销。*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjFNK55fVL1c25X9iaI4cEK5WsJQYe3KevxavSHbdYBjSfodW1m6em1iaich8meFWpDnswsLibiar4pGib4rGOCDm55iaENQWVkVCZiaSk/640?wx_fmt=png&from=appmsg)

*RDP 会话注销*

---

## 🔧 实战用例：检测可疑的 RDP 行为

假设你观察到以下事件序列：

1. 针对用户 `admin`的大量 `4625`失败事件
2. 一条成功的 `1149`+ `4624`（Type 10）
3. 随后快速出现 `4634`注销

这可能表明一次**暴力破解攻击成功后，攻击者立即进行了侦察**并随即注销。

结合以下上下文数据进一步分析：

* 登录时间在工作时间之外
* 非企业内部 IP 地址
* 异常的主机名或会话持续时间

---

## 🎨 RDP 时间线可视化

以下是一个概念性的时间线：

```
[00:00] -> Event 1149: Auth attempt
[00:01] -> Event 4624: Success login (Type 10)
[00:02] -> Event 21/22: Shell/session initiated
[00:30] -> Event 40: Disconnected
[00:31] -> Event 25: Reconnected
[01:00] -> Event 4647: Logoff initiated
[01:00] -> Event 9009: DWM closed
```

🧭 *这样的可视化时间线有助于威胁狩猎和事后调查分析。*

---

## 🔚 总结

RDP 事件取证不仅仅是检测暴力破解攻击——更重要的是从日志中构建完整的攻击叙事。通过关联 `Security.evtx`、`System.evtx`和 `TerminalServices`日志中的事件 ID，你可以**高保真地重建攻击者的行为轨迹**。

---

### 🔗 参考资料与致谢

* Ponder The Bits - RDP 事件日志指南
* 13Cubed - YouTube 取证教程

![](https://mmbiz.qpic.cn/mmbiz_gif/h4gtbB74nSgMfy1jIn0xAUNAbYicLZcibcrhIeMpx46lC037kaiafuD0yXIUPko6tPMDvRqMFjiaJXyqYRiasGiav2ZWKiceAPe9tOjyFflAcjx3z4/640?wx_fmt=gif&from=appmsg)

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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