---
title: 我用 165 块钱的硬件，搓了一个「无感」健康监测站
url: https://mp.weixin.qq.com/s/YjZC_Wk3wsvfiONj3zm7bA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:17.358812
---

# 我用 165 块钱的硬件，搓了一个「无感」健康监测站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TAFC5BLa6G3JsSVxDr7nfvTtBOJlpu7t3T03IicrO1HsrkauxRwOr8WDfjOrCgyEbgnuso1jicYdeDj2bsniaicNKB2qqTTBxIxJ4xn9TfgORicI/0?wx_fmt=jpeg)

# 我用 165 块钱的硬件，搓了一个「无感」健康监测站

原创

黑屋科技站
黑屋科技站

漕河泾小黑屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 不穿不戴不贴，坐在那里就能测心率、呼吸，还能估算血压。

---

事情的起因很简单——我搞到了一块 **60GHz 毫米波雷达传感器**，据说能隔空检测人的心率和呼吸。

听起来很玄学对吧？我也觉得，所以决定自己验证一下。

结果，还真做出来了。

---

## 硬件就两个东西

全部家当：

* **Seeed XIAO ESP32C6**——一块拇指盖大小的开发板，自带 WiFi 6 和蓝牙 5
* **MR60BHA2 毫米波雷达模组**——叠在 ESP32 上面，像搭积木一样

合体之后比打火机还小，USB 供电就能跑，没有屏幕没有按钮没有风扇。

安静到你会忘记它的存在。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TAFC5BLa6G3sWcL07ribqDzCVBaVuMKMLAub9gmfrgIQMQibRibSib74ickAuRY9C9kZQSicIMIGw5Z5ewicWsiaZC2Om90wsQ1iaDtrsQe5Trm31LVE/640?wx_fmt=jpeg&from=appmsg)

---

## 它到底能测什么？

这块雷达发射 60GHz 频段的毫米波信号，通过分析反射波的相位变化，能「看到」人体极其微小的运动：

| 检测项 | 原理 | 精度 |
| --- | --- | --- |
| 呼吸频率 | 胸腔起伏 | 次/分钟 |
| 心率 | 心脏搏动引起的体表微振 | bpm |
| 人体存在 | 生命体征信号有无 | 有/无 |
| 距离 | 信号反射强度 | 厘米级 |

**没有摄像头，没有麦克风，纯电磁波。** 隐私上完全没有顾虑。

我还基于心率和呼吸频率的统计关联，加了一个**血压估算**——经验回归模型，不能替代血压计，但看趋势变化够用了。

---

## 整套系统怎么跑起来的

数据从雷达到你的手机，经过这么一条链路：

```
MR60BHA2 雷达传感器    ↓ UART 串口ESP32-C6（滤波 + 血压估算 + WiFi）    ↓ TCP 长连接云服务器（Go 后端）    ↓ WebSocket手机浏览器（实时仪表盘）
```

每一层都不复杂，连起来就是一套完整的 IoT 系统。

---

## ESP32 端：数据采集和处理

雷达模组通过串口吐数据，ESP32 读取后做三件事：

**1. 滤波降噪**

原始数据波动很大，心率可能上一秒 68 下一秒 112。直接展示的话图表跟心电图似的——看着吓人但没有意义。

我用了一个**滑动平均滤波器**，心率和呼吸取最近 8 个采样点的均值，距离取 4 个点。效果立竿见影，曲线瞬间丝滑。

```
template<int N>struct Filter {  float buf[N] = {0};  int idx = 0, count = 0;  float add(float v) {    buf[idx] = v;    idx = (idx + 1) % N;    if (count < N) count++;    float sum = 0;    for (int i = 0; i < count; i++) sum += buf[i];    return sum / count;  }};
```

**2. 血压估算**

基于经验公式，用心率和呼吸频率推算收缩压和舒张压：

```
SBP = 0.5 × HR + 1.1 × BR + 49.0DBP = 0.3 × HR + 0.6 × BR + 30.0
```

这不是医学级别的测量，但能反映趋势——比如你连续几天收缩压在爬升，那确实该注意一下。

**3. WiFi 配网 + 数据上传**

第一次使用时，ESP32 会创建一个叫 `MR60BHA2_Setup` 的 WiFi 热点，手机连上后浏览器弹出配置页面，输入家里 WiFi 的账号密码就行。

之后每次通电自动连接，通过 TCP 长连接把 JSON 数据推到云服务器。

想换 WiFi？3 秒内按两下 RESET 按钮，清除记忆重新配网。

---

## 服务器端：Go 写的后端

后端用 Go 写的，一共四个模块：

* **TCP Server**：监听 9000 端口，接收 ESP32 推上来的 JSON Lines 数据
* **WebSocket Hub**：把收到的数据实时广播给所有在线的浏览器客户端
* **JWT 认证**：登录接口 + token 校验中间件，防止数据被随便看
* **静态文件服务**：托管前端页面

整个后端交叉编译成 Linux 二进制，丢到服务器上用 systemd 管理，稳定运行。

---

## 前端：手机上打开就能看

原生 HTML + Chart.js，没用任何框架。

打开浏览器 → 输入地址 → 登录 → 看到实时仪表盘：

* 心率卡片（滤波值 + 原始值）
* 呼吸频率卡片
* 血压估算卡片（收缩压/舒张压）
* 检测距离 + 人体存在状态
* 四张实时趋势图（心率、呼吸、血压、相位波形）

所有数据通过 WebSocket 推送，100ms 刷新一次。手机端自适应布局，竖屏横屏都能看。

全程中文界面。

---

## 踩过的坑

**蓝牙配网在 ESP32-C6 上不好使。** 一开始想用 BLE Provisioning 配网，折腾了一晚上发现 ESP32-C6 的 NimBLE 协议栈在 Arduino 框架下有兼容性问题，扫不到蓝牙设备。果断换成 SoftAP + 网页配网，反而更简单——不用装 App，手机浏览器直接搞定。

**nohup 在服务器上根本不靠谱。** 用 `nohup ./server &` 跑后端，SSH 一断进程就挂。试了 `setsid`、`screen`，都不稳定。最后老老实实写了 systemd service 文件，开机自启 + 崩溃自动重启，才算彻底解决。

**串口监视器抢端口。** 开着 Go 后端占着串口，Arduino 就烧不了固件。每次改代码都要先杀进程再上传，来回切换很烦。后来改成 WiFi + TCP 模式，彻底解放了串口。

---

## 成本

| 物料 | 价格 |
| --- | --- |
| XIAO ESP32C6 | ≈ 45 元 |
| MR60BHA2 雷达模组 | ≈ 120 元 |
| USB-C 数据线 | 家里找的 |
| 云服务器 | 已有的闲置机器 |
| **合计** | **≈ 165 元** |

代码量：ESP32 固件 280 行 + Go 后端 200 行 + 前端 300 行，总共不到 800 行。

---

## 接下来可以玩什么

这个项目目前还是个 MVP，但有不少有意思的方向可以继续：

* **数据持久化**——存到数据库里，做历史回看和趋势分析
* **异常告警**——心率过高/过低时推个微信通知
* **睡眠分析**——通过呼吸和心率变化模式判断深睡/浅睡
* **跌倒检测**——毫米波雷达天然适合做这个，MR60BHA2 本身就支持
* **多设备管理**——一个后台同时看多个房间的数据
* **接大模型**——让 AI 分析健康趋势，给出建议

---

## 最后

整个项目从硬件接线到服务器部署，一个人一天搞定。

最有意思的地方在于：165 块钱的硬件 + 不到 800 行代码，就能搭出一套**完整的、可远程访问的、实时的**生命体征监测系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TAFC5BLa6G2muBhvwubp0iaUt1ibyJraL9UUC5aevEak0SWicLnqUTH1hh161u4VnpaoE7oMOG1PbRWcGdWeHL5IZyOviaZKic3RWudZXdqZsODs/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

漕河泾小黑屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

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