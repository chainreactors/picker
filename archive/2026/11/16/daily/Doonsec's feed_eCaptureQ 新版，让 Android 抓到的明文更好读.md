---
title: eCaptureQ 新版，让 Android 抓到的明文更好读
url: https://mp.weixin.qq.com/s/4lsMX-v559C5qMW1pNTWoA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:52.075713
---

# eCaptureQ 新版，让 Android 抓到的明文更好读

# eCaptureQ 新版，让 Android 抓到的明文更好读

原创

CFC4N
CFC4N

榫卯江湖

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![eCaptureQ 主题插图：Android 加密流量转为可阅读的请求与响应](https://mmbiz.qpic.cn/sz_mmbiz_png/arjmNWXmn5Vu5iajqbibMiansBia0apjd29dA9qSvLS218dTkO4ZBZFgP32GSK9ia8naoNILWfIOKKoYzap6lXq8KrQ8UcdUcvcHzllzU7fibcibzs/640?wx_fmt=png&from=appmsg)

eCaptureQ 主题插图：Android 加密流量转为可阅读的请求与响应

*主题插图由 AI 生成；下文展示实际操作截图。*

> 调试 Android App 时，我们往往想知道：刚才点下按钮，App 请求了哪个接口？发了什么参数？服务端为什么返回错误？

**新版 eCaptureQ，把 eCapture 捕获的明文变成可以筛选、搜索和逐条查看的界面。** 手机上运行 eCapture，在电脑上打开 eCaptureQ，就能沿着进程、请求和响应检查一次通信。

![eCaptureQ 三栏界面，左侧筛选、中间选择请求、右侧查看正文](https://mmbiz.qpic.cn/mmbiz_jpg/arjmNWXmn5WtSX6FuU9ZUfITu4yCLr5d6F2dBfjTGSXic8DdHv9TEhCFgcPbKfYOrXVTHDWVcOW1vYiaGIX79dPk643Wfic4mHnibJxnxXyZ0aY/640?wx_fmt=jpeg&from=appmsg)

eCaptureQ 三栏界面，左侧筛选、中间选择请求、右侧查看正文

*左侧找进程，中间选请求，右侧看详情。下文以 App 常见的“提交订单”流程为例；操作截图来自 Linux VM 对合成测试业务的真实抓包，Android 按下面的方式接入。*

### 1. 打开 eCaptureQ 桌面版或 Web 版

喜欢独立应用，可以下载 macOS、Windows 或 Linux 桌面版；喜欢浏览器，可以运行 eCaptureQ Web。两者使用同一套分析界面，采集器另行运行在手机上。

下载 eCaptureQ[1] · 安装说明[2]

Web 版在电脑上启动后，访问 `http://127.0.0.1:8080/`。本文统一使用 **8080 作为 Web 页面端口、28257 作为 eCapture 事件端口**：

```
./ecaptureq-web --listen 127.0.0.1:8080
```

Windows 使用 `ecaptureq-web.exe`；Linux 安装包用户直接运行 `ecaptureq-web`。还没接手机，也可以先用默认的「模拟」模式熟悉操作。

### 2. 启动手机采集，并连接数据源

准备一台已取得 root 权限、内核与目标 TLS 库受 eCapture 支持的 Android 测试设备。下载对应架构的新版 eCapture[3]，将可执行文件放到 `/data/local/tmp/ecapture` 并赋予执行权限。

在手机的 root shell 中启动采集。下面以 Wi-Fi 和系统 Conscrypt 的 64 位 TLS 库为例；网卡与库路径应换成目标 App 实际使用的值：

```
/data/local/tmp/ecapture tls -m text --text-source pcapng \
  -i wlan0 \
  --libssl /apex/com.android.conscrypt/lib64/libssl.so \
  --ecaptureq ws://127.0.0.1:28257/
```

手机通过 USB 连接电脑，在电脑上转发事件端口：

```
adb forward tcp:28257 tcp:28257
```

打开 eCaptureQ 右上角的「数据源」，点击「添加数据源」，填写 `ws://127.0.0.1:28257/`，然后「添加并连接」。

![在 Web 界面填写实际使用的采集端 WebSocket 地址](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5VGnOdLPicopaJUroeGkRDtrkffw1LZ6JVTMicXeuZ9RNia21sk9YDKvMJMib1g3biaYbTViamSsDZhnaVwvGdnedzKDeMjspGvjTSco/640?wx_fmt=jpeg&from=appmsg)

在 Web 界面填写实际使用的采集端 WebSocket 地址

*名称可自定，图中连接的是 VM 演示来源。接手机时，采集需先在手机端启动，添加来源不会替你启动探针。*

看到数据源已连接后，切换「实时」，再打开目标 App、触发一次操作，让采集覆盖新连接的握手和业务请求。若 Web 服务部署在远端，转发通道也必须对那台 Web 主机可达，浏览器所在电脑的 `127.0.0.1` 不会自动共享给它。

### 3. 按进程和接口筛选，找到目标请求

先按左侧的进程名或 PID 缩小范围，再按目标主机筛选，或者搜索接口路径。分析多进程 App 时，可以结合进程命令确认归属。

![点击进程后，列表只显示该进程的相关记录](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5WLnL2wGjd1OH6ZZVanvYiaZictLuJ3RSyVdnZ7PzEw3WfhpocumqfBpDMG3ScOYibVBribOOxSib7GASDamO1hCfnyibM1gLf0twQw0/640?wx_fmt=jpeg&from=appmsg)

点击进程后，列表只显示该进程的相关记录

*图中选择实际发起请求的 curl 进程后，14 条记录缩小为 7 条。接入手机后，在这里选择目标 App 的进程。*

例如复现一次“提交订单失败”，搜索 `/v1/orders`，点开返回 422 的 POST 请求。URL、请求头和正文集中显示，格式化 JSON 后可以直接发现 `address_id` 是空字符串。

![搜索接口后查看 POST 请求头与格式化 JSON 正文](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5X9Az1lgeywqoMpic6gNiacia63ptun2pJgpGtUiafHcWQBHicLHWHRdgFksoxjwh5wtW1YicjfEZaKWhow3dJ1c48biaBe2hwoj5ShicA/640?wx_fmt=jpeg&from=appmsg)

搜索接口后查看 POST 请求头与格式化 JSON 正文

*从“提交失败”进一步定位到“这次请求没有带上收货地址”。*

### 4. 对照请求与响应，定位失败原因

切到「响应」，查看状态码、响应头和返回正文。请求与响应关联在同一条记录中，方便对照发送参数与接口返回。

![同一条请求的响应视图，显示状态码与错误 JSON](https://mmbiz.qpic.cn/mmbiz_jpg/arjmNWXmn5Wt7y1XWNWT11bvyt9LGY2GgyV54ibbFl1GG55jHicGdq9ggg37PD2FLyUZwKZcTn0osx9qHHpmaAEIQTMsia4YEG78yRzJFGZ8z8/640?wx_fmt=jpeg&from=appmsg)

同一条请求的响应视图，显示状态码与错误 JSON

*本次实际返回 HTTP 422，正文为 `ADDRESS_REQUIRED`，并指明 `address_id` 与“请选择收货地址”。*

补齐 `address_id` 后重新请求，状态变为 `201 Created`，响应中出现订单号。两次请求保留在列表里，便于回头对照。

![补齐地址后，实际捕获到 HTTP 201 与创建成功的订单响应](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5UGTxTzNXU63srrDHTJibVo4GfUiaC8GjxuUJhMbH8nnqETt0kd9qWMFCjyC8Zjr0waNibtdbMHQzyaoAiaxQ2DP15D5ibAa1dkQ34c/640?wx_fmt=jpeg&from=appmsg)

补齐地址后，实际捕获到 HTTP 201 与创建成功的订单响应

需要逐字节检查载荷时，切换「原文」或「Hex」；已有请求及目标地址的 HTTP 记录，还可以复制为 cURL，整理复现命令。

![将正文切换到 Hex，查看原始字节](https://mmbiz.qpic.cn/mmbiz_jpg/arjmNWXmn5WZ1VvkWwJ9dnrqVypYWBv5WIEibEoqjnNMmRf0rweaTkkJw4xEviawqNPI29UwVkD6HH9Mz426U4AwD5bhzdqSaLH9U3EvD18jA/640?wx_fmt=jpeg&from=appmsg)

将正文切换到 Hex，查看原始字节

*TLS 解密后，业务正文如果仍有应用自身的加密，需要继续分析；界面不会自动解开业务加密。*

如果接口返回的是图片，也可以直接预览捕获的内容，无需另存文件再打开。

![直接预览 HTTPS 响应中实际捕获的商品示意图](https://mmbiz.qpic.cn/mmbiz_jpg/arjmNWXmn5UqdHEX2edcgiaW4ficAHCoFIvKK1EzIc1Ax0cb16oaSFibxSSEMDDuqcHvYbibyT1wicnztYIkbkjKxt7Zu24lvREPkEvyIliaLwkIY/640?wx_fmt=jpeg&from=appmsg)

直接预览 HTTPS 响应中实际捕获的商品示意图

*这张测试图片来自已捕获的响应字节，预览不会重新访问原地址。*

### 5. 查看进程归属、连接和 TLS 指纹

「连接」页把进程名、PID、启动参数和连接信息放在一起。上游提供相应字段时，还能查看 TLS 版本、SNI、ALPN、密码套件以及 JA3 / JA4 指纹；缺失字段保持「未提供」。

![连接页展示进程归属、启动参数与 TLS 信息](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5VdIJictEbol1Whf1Sdaxvg75VHQicNe1rBaicZbZ6voibzSqvZgaAqf91d5bnwTbZpIC5vBnFyFFCsmfib0O1sSWTsic2KQhqVmYicNc/640?wx_fmt=jpeg&from=appmsg)

连接页展示进程归属、启动参数与 TLS 信息

![向下查看 TLS 握手与客户端指纹](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5WHWCWPbicSWogHkg2WgjLibuLYsYaGib4y6F7l5kicNV6JvmhOicuzrgeiaqXJl8XwibHcu51TibMqqbN4338ib9rlJP0A7teJN3bsKwL0/640?wx_fmt=jpeg&from=appmsg)

向下查看 TLS 握手与客户端指纹

*对 Android 逆向与调试来说，这能把“发了什么”与“哪个进程、连到哪里、用了什么 TLS 参数”放在同一处检查。*

为什么这次能提供更多上下文？eCapture 的 `text + pcapng` 链路结合 TC 层的网络包与 uprobe 捕获的 TLS 密钥，通过 eCapture Decryptor 实时解密、重组应用消息；eCaptureQ 接收这些消息并关联展示。相比按函数调用查看零散明文，更便于阅读完整请求与响应，实际完整程度仍取决于是否捕获到所需密钥和网络数据。

### 6. 导出记录，让 AI Agent 辅助分析

右上角可以导出当前页 JSON，便于留存和后续分析。暂停刷新只暂停页面更新；需要保留的记录应及时导出。

eCapture Skills[4] 提供了 AI Agent 使用 eCapture 的操作指导。按你的 Agent 的技能机制导入完整仓库，并提供测试设备的执行通道后，可以这样描述任务：

> 帮我检查这台 Android 测试机上的目标 App。我会复现一次提交失败，请先确认采集条件，捕获相关请求和响应，再根据状态码和正文分析问题。

同样的界面也能连接 Linux 数据源，辅助服务端接口排查。

eCaptureQ 项目[5] · eCapture[6] · eCapture Skills[7]

### 在线体验 eCaptureQ

无需先搭建环境，可以直接打开 eCaptureQ 在线 DEMO[8]，体验 Web 界面和演示流量。

参考资料

[1]

下载 eCaptureQ: *https://github.com/gojue/ecaptureQ/releases*

[2]

安装说明: *https://ecapture.cc/q/zh/install/*

[3]

eCapture: *https://github.com/gojue/ecapture/releases*

[4]

eCapture Skills: *https://github.com/gojue/ecapture\_skills*

[5]

eCaptureQ 项目: *https://ecapture.cnxct.com/q/zh/*

[6]

eCapture: *https://ecapture.cnxct.com/zh/*

[7]

eCapture Skills: *https://github.com/gojue/ecapture\_skills*

[8]

eCaptureQ 在线 DEMO: *https://q.cnxct.com/*

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHsLicJBSCn3XGk8WbSqyUDAQp9Gh8QjlFv4FFbGo5e8L2k4tDTXa0sYGIKfVEQibnufpIibQD7EOoWQw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过