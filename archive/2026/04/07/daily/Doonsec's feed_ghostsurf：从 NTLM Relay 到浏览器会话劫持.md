---
title: ghostsurf：从 NTLM Relay 到浏览器会话劫持
url: https://mp.weixin.qq.com/s/g4E5WaSh89RB4ujkT4wh6A
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:32:02.794572
---

# ghostsurf：从 NTLM Relay 到浏览器会话劫持

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsibWeHhfHVuTvlmgvogX139mE0lsz9tE53638Riah1Nj3B46txbG4NoPk8f2jQktZmtTGKdwWN5OP0k30veiaPIPYtmd2Q1pF2dA/0?wx_fmt=jpeg)

# ghostsurf：从 NTLM Relay 到浏览器会话劫持

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

`ntlmrelayx` 的 SOCKS 代理对 SMB 和 MSSQL 很好用，
但当你试图用浏览器通过它访问 Web 应用时就会失败。

👉 我深入分析原因，发现它在 HTTP 处理上有多个根本性问题

👉 我构建了 **ghostsurf** 来解决这些问题

👉 同时还发现并绕过了一些**未公开的 Windows 内核认证行为**

👉 `ghostsurf` 可以让你通过 SOCKS5 代理，以“被中继的用户身份”浏览支持 NTLM 的 Web 应用（比如企业密码库），即使无法窃取 cookie。

工具：
https://github.com/senderend/ghostsurf

---

# 🧭 起点（Where This Started）

在一次渗透测试中：

目标环境使用 **CyberArk Privileged Access Manager**

用户/管理员流程：

* 访问内部 Web 页面
* 自动使用 Windows 登录会话认证
* 从浏览器复制密码

我们：

* 控制了一个 relay 位置
* 捕获了一个高权限域账号的 NTLM（不可破解）

👉 如果能用这个用户访问 CyberArk：

就能获取所有该账号权限范围内的秘密

---

## ❗ 问题

`ntlmrelayx` 提供 SOCKS 代理功能：

* 可以通过已认证会话转发流量

👉 对 SMB / MSSQL 非常好用

但当我们：

👉 用浏览器通过 SOCKS 访问 Web

结果：

* 出现 Basic Auth 弹窗
* 页面卡住
* 响应损坏
* 页面加载失败

👉 没人有解决方案

---

## 🔍 于是我开始读源码

我直接去看 `ntlmrelayx` 的 HTTP SOCKS 插件代码

👉 然后事情开始变得有意思了

---

# 📊 当前 ntlmrelayx 浏览器支持现状

先启动 ntlmrelayx：

![start](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnumr5ib4JD3Ghh13U9frHItojeqZj88MC2rIve1692R1DLOW3zIicYwqnWXMy0AtCSftcgPpGhJiaEpWhy2G7rv0ibYpLfv5xJ33ibg/640?wx_fmt=png&from=appmsg)

---

成功 relay 后：

* 完成 NTLM 握手
* 保存会话
* 每 30 秒 keepAlive
* 打开 SOCKS5

![success](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuKCxsEho5V085rmYXtG6wbicu2YRiccmcNwqhvDU2L8sNna4icrJOQzAUEic8gAic4dz2bn7Ccrz1KMuGxicozEYK6KCGG8nyPYsU9c/640?wx_fmt=png&from=appmsg)

---

## 🌐 浏览器测试

配置 Firefox + FoxyProxy（127.0.0.1:1080）

访问目标：

![auth](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnumkHZVibmhhTBqD2EqWQnlLzAOfy9eW0NmvWg5pyrokfH4dm6vOeG5e0kq772P7PHNSBoVqkzEntBGrgpFrLgr8xNWou7Yueg0/640?wx_fmt=png&from=appmsg)

👉 出现 Basic Auth

---

## ❗ 问题

这个弹窗和：

👉 未认证访问时完全一样

👉 很多人会以为攻击失败

---

## 🧪 实验：输入正确凭证

![try1](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnswXsBC0zTiauaxvV1eib6TQdhiaj6KaujeZhHg9A72FAGtZcOB0EuAuA7ZRRGaicJNv7vicaSO7iaWo1pjFLLmia7mL9GGeuwEg21liaI/640?wx_fmt=png&from=appmsg)

![fail](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuQJUbfe5tH28ylLKpCbiapqeibc4svXF2CfHmAAeSGlBCWyeLEJMmfeIh6IaKptoMc1icOEiakV8Bg98wL2UbzFbXa4ntbiaSVUXR0/640?wx_fmt=png&from=appmsg)

👉 居然失败

---

## 🤯 再试一次（用 /）

![slash](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsNIf8RnwCXt2uj0W7DibY5DXAWibic5jQicFicwRQvM9n1S8SdiadEolib0wn23WGPKhdBLPy83wQG46cZosWdJPKq7iaCtMMBwPy2lxc/640?wx_fmt=png&from=appmsg)

👉 居然成功

---

## 🎉 进入系统（但…）

👉 页面严重错乱

---

## 💥 很快崩溃

👉 会话丢失

---

# ❓ 为什么会这样

总结一句话：

👉 **ntlmrelayx 根本不是为浏览器设计的**

---

# 🧠 根本原因（Why Browser Proxy Broken）

核心问题：

👉 ntlmrelayx 假设：

* 单连接
* 顺序请求

👉 但浏览器不是这样工作的

---

## ⚠️ NTLM 特性

NTLM HTTP 认证：

👉 绑定 TCP 连接（有状态）

👉 不能用 cookie 替代

---

## ❗ ntlmrelayx 限制

* 每个 session 只有一个 TCP socket
* 所有请求必须走这个 socket

---

## 💥 浏览器行为

浏览器会：

* 开多个 TCP 连接
* 并发请求资源

👉 结果：

* 请求互相覆盖
* 数据流损坏
* 页面加载失败

---

## 🚫 inUse 锁问题

ntlmrelayx 使用 `inUse` 标志：

* 防止并发访问

👉 结果：

* 浏览器 6 个连接 → 5 个被拒

---

# 🤯 为什么会出现 Basic Auth

👉 不是 Web 服务器的

👉 是 ntlmrelayx 自己的！

---

## 📌 原因

ntlmrelayx 支持多个 session

👉 需要你选择用哪个

👉 用 Basic Auth header 来传

---

## ❗ 问题

浏览器看到：

👉 和正常认证完全一样的弹窗

👉 但其实是在选 session

---

## 🤡 更离谱

* 必须用 `domain/user`（正斜杠）
* 但 Web 要求 `domain\user`

👉 完全冲突

---

# 🚀 解决方案：ghostsurf

![ghostsurf](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuTgoaE6Y0T58EfdqxG2kuLNKlcELdpAzLyb17UgVpbT2cGFRIJ4ItmoLSdcGNjwGtoibyYj2EyYibqSCnqMxs96JAbRInjCPWYE/640?wx_fmt=png&from=appmsg)

---

## 🧠 核心改进

### 1️⃣ 并发问题

👉 用 mutex 锁代替 inUse

流程：

* 获取锁
* 发送请求
* 完整读取响应
* 释放锁

👉 所有请求被序列化

---

## 结果

* 浏览器可以开多个连接
* 不会冲突
* 数据不会损坏

---

## 2️⃣ session 选择

* 单 session → 自动选
* 多 session → 页面选择

👉 用 cookie 绑定

---

![picker](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuUKzIVHoFChOFojaMJQg0uH457oLaicyWJibwxOgFXd7HRh1V3ptxfaXpArQQPuiamQc8FHZiaVcoKPl7RWkiavhNibUVs5Zl2LFKcI/640?wx_fmt=png&from=appmsg)

---

## 3️⃣ 保留 HTTP 头

ntlmrelayx 会删 header

ghostsurf：

* 保留 User-Agent
* 保留 cookie
* 保留其他头

---

# 🧬 内核认证研究（重点）

测试真实软件时发现新问题：

👉 Passwordstate 会突然重新认证

---

## 📊 现象

* 前 30~50 请求正常
* 然后突然 401

---

## 🔍 原因

IIS 启用了：

👉 **Kernel Mode Authentication**

👉 认证在 HTTP.sys（内核）完成

---

---

## 📌 关键发现

访问顺序：

1. 认证资源 ✅
2. 匿名资源 ✅
3. 再访问认证资源 ❌（401）

---

## 🧠 推测机制

内核模式下：

👉 认证状态像开关

访问匿名资源：

👉 重置为 Anonymous

---

![flow](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsx7sBkTPm7h9oPg53yXxC3G7k5PAEIux3NqrTeMYgzqL7eo7OwibicuibKF6v7KEjySqCeJz7oA40fhiacoEq4xKtemT2Fqypf9PA/640?wx_fmt=png&from=appmsg)

---

# 🛠 解决方法

ghostsurf 使用：

👉 **探测策略（probe-first）**

---

## 📌 逻辑

1. 先用匿名请求
2. 如果返回：

* 401 → 需要认证 → 走 relay
* 200 → 公共资源 → 直接返回

---

![probe](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntibzulAicolvc8BKB2Yq4JLUhF9ecf16Y53Y39CTvIJBWqonN6zt4K8GGZdmvlRWlAzxtv64Ms9XiaqMRO9ibyFSUAuEDTJCKfD0s/640?wx_fmt=png&from=appmsg)

---

## 📌 优化

* 结果缓存
* 后续无开销

---

# ⚙️ 使用方法

```
./ghostsurf -t https://target -k-r
```

* `-k`

  ：内核认证绕过
* `-r`

  ：允许多用户

---

![run](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuhBvvvHoNkTZlydYpSibhaDuQLichPXH1pO5icGvx3F9T1KaZB3hCVA30K2CQHiatrLaxMjvtvoSuRJAClIghE09icaJibD3zbicH1EM/640?wx_fmt=png&from=appmsg)

---

## 📌 浏览器配置

* Firefox + FoxyProxy
* SOCKS5 → 127.0.0.1:1080

---

## 📌 查看 session

```
ghostsurf> socks
```

![sessions](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnv3e1tfh3MRjCmbpMZ6w7wibO9Pa9YvAeibN6PmeibuVfTicGr9htH8DhvhfCZN29PdlxOIB81ZRNjwbpicSqd5BzibsqFAWpOLialSWk/640?wx_fmt=png&from=appmsg)

---

## 📌 浏览访问

---

# ⚠️ 使用 -k 场景

适用于：

* IIS 默认配置
* CyberArk
* Passwordstate
* SCCM 等

👉 不确定就开

---

# 🔍 进一步用途

ghostsurf 可以：

👉 用浏览器真实交互

👉 帮你分析复杂 Web 应用

👉 开发新攻击模块

---

# ⚠️ 限制

* 单 TCP → 性能有限
* 不支持 WebSocket

---

# 🍪 为什么不能直接偷 cookie？

## 情况 1：匿名 + Windows Auth

👉 有 session cookie → 可以复用

---

## 情况 2：仅 Windows Auth

👉 每次请求都要 NTLM

👉 cookie 没用

---

## ✅ 结论

👉 必须用代理（ghostsurf）

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuCJsTmUzYrdaEIG1lzeOJNXqbZ1260iats4bvYoLowDTAfzFicAPPiaOOIDuP5fkOQmC1dxDq6xJWoibHUBwaNdQdu72Pwk1LFibhs/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsJXRZhRId06dj9NnXJ44a6JqPmtMJtdYyurufSblPXFkQHmJDrWJmKZO7ho5AcicJZlbcQHbvh46jHLqSWYaZarlVn4icqXx08I/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

#

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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