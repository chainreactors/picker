---
title: 7 美元 ESP32 让 AI 接管真 iPhone：不用 Mac、不用开发者账号、不用越狱
url: https://mp.weixin.qq.com/s/RcoQNCtpEI4OdpVlf6slyQ
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:16:47.623252
---

# 7 美元 ESP32 让 AI 接管真 iPhone：不用 Mac、不用开发者账号、不用越狱

# 7 美元 ESP32 让 AI 接管真 iPhone：不用 Mac、不用开发者账号、不用越狱

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Oykcu1KKiazMhLc6kIGvcqBoCEDic326XLQ73GaNUIHdBTeJEp6f7cciccKFTe4gkMSnnWv9s5PwHMhpG4PXcfl6ndTgHx7rE5bM/640?from=appmsg)
> **导语**：AirPlay 当眼睛，USB HID 当手，7 美元的 XIAO ESP32S3 就能让一个 AI 模型直接操作真机 iPhone 屏幕。不用 Mac 常驻、不用苹果开发者账号、不用越狱。项目开源 12 天，3551 星。这套方案绕开了苹果的自动化安全边界，也绕开了你自己。

---

## 一、它到底做了什么

先看架构，这套方案的核心洞察只有一句：**别在 App 里做 UI 自动化，从 USB 层接管输入。**

```
iPhone ──屏幕镜像(Wi-Fi)──▶ ESP32-S3: AirPlay 接收端 ──BLE──▶ iPhone 上的 Agent App
   ▲                                自建热点, H.264 直通               解码 → 视觉模型 → 决策
   └──────── USB HID 鼠标+键盘 ◀──────────── BLE 命令 ◀────────────────────────┘
```

三个角色分工很清楚：

**眼睛**——ESP32-S3 自己开一个 Wi-Fi 热点，以 `ESP32 Agent` 的名字出现在手机"屏幕镜像"列表里。它**不解码**画面，只把 H.264 码流原样透传，通过 BLE 塞回给同一个 iPhone 上的 App 去解码。注意这里有个巧妙的地方：手机连了板子的热点就等于断了外网 Wi-Fi，所以模型调用是走 4G/5G 蜂窝数据。

**手**——板子伪装成标准 USB 鼠标和键盘。手机上打开辅助触控（AssistiveTouch），屏幕上就出现一个指针，于是"点击"变成 tap，"拖拽"变成 swipe。整套 iOS 自动化从此跑在 HID 协议层，不碰任何系统 API。

**大脑**——iPhone 上的 SwiftUI App 解码视频帧，把截图发给任意兼容 OpenAI 接口的视觉模型，跑 planner（出计划）和 actor（出动作）两段式循环。动作指令集包括 tap、swipe、path（画线）、circle（画圆）、type、key、home、back，以及 replan / done / fail 三种状态控制。坐标是相对截图的 0-1000 整数。

![真实手机与智能体所见画面对比](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OCicEBCq39UpoxiaKCt1hcxvhfaKBkBjnNE7wDsNa9Qiab24GzzXGmBq8631CUwCleJOpBaVuxU5KwYRicU83c51x2j9stvYq0894/640?from=appmsg "真实手机与智能体所见画面对比")

上图左边是真机，右边是板子投回来的画面，第三四张是指针校准过程——App 靠晃动静针、截图定位、再纠偏来补偿相对指针的漂移。

作者 Henry Yuan 是 ex-腾讯、NYU 网络安全背景，Antler Global 投资的 AI 创业者，模型用两台 DGX Spark 跑 Qwen3.8-Flash。

## 二、三个设计得相当漂亮的细节

**BLE 协议把视频流当数据包打。** 板子对外只暴露一个 GATT 服务和五个特征：`cmd`（写命令）、`reply`、`status`（每秒心跳 JSON）、`video`（H.264 分片）、`net`（加密链路读热点密码）。每个 video 分片带 16 位序号，App 数缺口就知道丢包，然后等下一个 IDR 关键帧重建。

**降级策略写进了协议层。** BLE 带宽只有 300-500 kbps，画面被压到 480×1040、每秒不超 5 帧。当一个 P 帧超过 800 ms 还没送出去就直接丢弃，流跳到下一个 IDR——意思是链路慢的时候画面会退化成"只传关键帧"，而不是无限累积延迟。这种取舍在嵌入式流媒体里很常见，但写进协议文档的很少见。

**提示词就是提示词，纯文本可改。**`prompts/` 目录下三个 md 文件：planner 出最多 6 步的计划，actor 输出 THINK/DO 格式的动作序列，app-rules 管边界规则。改完重新编译即可，没有框架抽象。

actor 提示词里的工程经验很实在：滑动手势无惯性，建议 100-250 单位短滑后检查结果；时间滚轮先把指针移到数字中心行再打字；列表一次不超过一屏，翻到头还没找到就 `fail` 并报出最接近的选项，别闷头继续滚。

## 三、安全边界：值得红队视角细看

这个项目最值得琢磨的不是技术，是它**绕过的东西**。

苹果的自动化安全模型建立在"App 在沙箱里 + 关键操作要人工确认"之上。而这套方案从 USB HID 层直接注入输入事件——不调用任何系统 API，不申请辅助功能权限，不受 App Store 审核约束。App 里还留了个私有 API `suspend` 用来挂后台，作者自己写明"上架前得换掉"。

BLE 层用 LE Secure Connections + bonding，配对模式是 Just Works，本身不提供 MITM 防护——防护逻辑全靠"读取 `net` 特征会触发 iOS 配对提示"，把热点凭据挡在加密链路后面。SECURITY.md 里作者划的范围很坦诚，其中一条是"任何能让智能体在用户未启动时执行动作的东西"，说明他清楚这东西的攻击面在哪。

**必须提的一个警告。** README 顶部有一条醒目提示：只照 README 装，永远不要跑 issues 和评论里贴的命令（比如那种 PowerShell 一行 `iex(irm ...)` "快速安装"脚本）——那些不是维护者发的。这几天已经有这类钓鱼脚本混进新项目了。刷固件的时候老实走 `hardware/flash.sh`。

## 四、目前的硬限制

想上手前先看清这几条：

* **键盘只支持 ASCII**，中文输入直接出局（作者把它列在 roadmap 里）。设中文闹钟、输中文密码这些场景现在做不了
* **锁屏即断流**，iOS 不镜像密码输入页、Apple Pay、DRM 视频
* **跑任务时手机 Wi-Fi 被板子热点占着**，模型必须走蜂窝数据，流量费自己扛
* **竖屏假设**，横屏 App 的坐标和校准全是错的
* 每步要几秒，绝大部分时间耗在模型推理上，不是硬件

## 五、下载与仓库

**仓库地址**：https://github.com/onehumanbeing/esp32-iphone-agent **官网**：https://handsy.tech **作者 X**：https://x.com/iamhenryyuan

硬件就一块 Seeed Studio XIAO ESP32S3（标准版，8MB PSRAM，非 Sense 非 Plus），约 7 美元。固件用 `arduino-cli` 烧录，必须走仓库里的 `hardware/flash.sh`，它会应用 `nimble_cfg.h` 的 BLE 缓冲区配置。App 用 Xcode 编译，免费 Apple ID 签名也行，每 7 天重签一次。

![整机实测效果](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PmtL2mBjUpB2wOveuicD5zoQCgHFH57WjuDjoSXTylPZGxESu8L2Rfj3laHSgr7kkMsw4ERruNsLDmZic0yfmxkFkZvKhawToyM/640?from=appmsg "整机实测效果")

许可要留意：主项目 MIT，但 `hardware/hid_bridge/src/airplay/` 那部分是从 UxPlay 移植的，走 GPL-3.0，链接它的固件二进制因此也是 GPL-3.0。作者还专门加了 NOTICE 文件，要求二次开发者在 README 和任何演示里署名，这点挺少见。

## 六、我的判断

这不是玩具。App Store 上架和 CLI 都在推进中，方向是做一个"给任意智能体装上手脚"的基础设施。

从红队视角看，它的现实价值不在于"让 AI 设个闹钟"，而在于把**真机操作的成本压到了 7 美元加一根线**。社工验证、流程演练、批量注册养号、设备农场自动化——过去要么需要越狱，要么需要 Mac 加 Xcode 加签名证书，现在门槛低了一个量级。

反面同样成立：一台插着板的 iPhone，如果 BLE 被远程接入或热点凭据泄露，等于交出了一台真实设备——你的账号、验证码、支付入口都在里面。

**伦理边界摆在这**：只自动化你自己拥有或明确获得授权的设备和账号。用 AI 去点别人手机屏幕，跟用任何工具入侵别人手机，在法律性质上没有区别。

**版权声明**：本文由华盟网原创发布，保留所有权利。文中信息均取自项目公开仓库、官方文档与 BLE 协议说明。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OIJ4EwXfSQQcFbiaTBsiaV4lVYnnY5zguDqaM5MiawHd5hvGWQHaBcGNSAh5GaaniaCKpoE1zeBicBWqETOWnF65TYYiaknjHiaNVx3k/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PAH0548932gTEWjvPZNzHwW1HTibsJHeDzzulBicCWaDsHVZia5RX6TQ97nrtSvL6wmGI3abDfEgURZ61eyw8LF8nCicfZc6OHyD8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MN26JAL5iczzSBtKSicuHfxTpNmFCBIvoWSusUnrribSnFzle7SiblBLw1bu7llxI7upNpC9KiaOXSGlAh8eYTnvrOc9JtXDVkwK8s/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NYLiacuBWLcUT2CyHhlkOmnMyzUiaZz6SicNUB4icjSKnRRvB1dV25FD53QiclDIzGjJjeuJT4bruA232rY60ic0vwgAuia1k4A5Kf6A/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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