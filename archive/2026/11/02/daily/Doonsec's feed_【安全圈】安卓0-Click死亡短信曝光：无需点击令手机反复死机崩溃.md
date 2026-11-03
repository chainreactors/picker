---
title: 【安全圈】安卓0-Click死亡短信曝光：无需点击令手机反复死机崩溃
url: https://mp.weixin.qq.com/s/k_nhQyoVCRHv7Otlsi5VDg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:13.402680
---

# 【安全圈】安卓0-Click死亡短信曝光：无需点击令手机反复死机崩溃

# 【安全圈】安卓0-Click死亡短信曝光：无需点击令手机反复死机崩溃

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心事实**：安全研究员 Mark Blaszczyk 正式公开针对 Android 系统的 **0-Click 远程“死亡短信”（SMS of Death）** 漏洞深度分析。攻击者仅凭目标手机号发送特定格式的底层 WAP Push 短信，无需用户点击任何链接，甚至在短信界面毫无显示痕迹，即可在解析报文时直接击溃特权进程 `com.android.phone`。连续投递 20 条攻击短信即可引发软硬件死循环，触发系统救援机制强制恢复出厂设置；由于运营商重试机制存在，设备重置后开机将再度中招死机

## 📡 无感知静默攻击：WAP Push 协议解析陷阱

该攻击向量的核心载体并非普通文本短信（SMS），而是移动通信标准中由系统静默接收的 **WAP Push** 报文。WAP Push 本用于移动网络向终端推送彩信通知（MMS Notification）或 OTA 运营商入网配置。当基站将此类数据包下发到基带芯片后，操作系统会在后台直接唤醒解析模块，绕过普通即时通讯界面的收件箱列表

漏洞的技术机理发生在 Android 框架解析 PDU（协议数据单元）的底层逻辑中：

**1. 长度字段数值溢出：**Android 在处理特定 WAP Push 消息头部的长度字段（Content Length / Headers Length）时，进行了不当的数据类型强制转换。攻击者构造畸形边界值，导致解析函数在计算内存偏移量时抛出未捕获的运行时异常（RuntimeException）。

**2. 核心特权服务崩塌：**该异常发生在运行于高特权 UID 下的系统级应用 `com.android.phone` 中。该进程不仅负责移动网络握手、SIM 卡管理，还承担蜂窝数据与短信派发。一旦崩溃，整机所有移动网络连接瞬间归零。

**3. 0-Click 完美闭环：**因为异常发生在系统服务对广播报文的反序列化阶段，用户屏幕上不会出现任何弹窗、提示音或短信记录，攻击完全在静默状态下完成。

```
// Android WAP Push PDU 解析缺陷与异常传播路径public voidparseWapPushHeaders(byte[] pduData) {int rawLength = readLengthField(pduData);// 缺陷：未对负数或超范围边界进行严格范围截断if (rawLength > pduData.length) {// 抛出运行时异常，未被调用方捕获，导致 com.android.phone 崩溃throw newIllegalArgumentException("Invalid header length offset");}}
```

## 💀 20条短信瘫痪整机：运营商重试机制催生无限死局

单条攻击短信通常只会造成电话服务闪退并自动重启，但在真实网络对抗中，该漏洞呈现出极度致命的放大效应：

* **队列重放陷阱：**

  由于崩溃发生在消息处理完成之前，系统数据库并未向底层写入“已成功消费”标志。电话服务每次重启，系统消息分发队列会再次尝试投递该报文，从而引发连续自发性崩溃
* **Rescue Party 强制重置：**

  测试表明，若攻击者在几秒内连续发送 20 条畸形短信，进程崩溃频次将突破 Android 看门狗（Watchdog）阈值。设备将直接黑屏进入不断重启循环，最终触发 Android Rescue Party 机制，将设备引导至 Recovery 界面并锁定，提示“系统无法加载，数据可能已损坏，请恢复出厂设置”
* **运营商重传引发终极闭环：**

  这是该漏洞最棘手的物理现实——在手机因持续崩溃而无法向基站返回确认回执（ACK）时，运营商短信中心（SMSC）会严格遵循信令重试策略（通常持续 24 至 72 小时）。这意味着用户即便按照提示清空全盘数据恢复出厂，手机重新接入基站注册成功的瞬间，运营商网络会立即再次补发未接收的死亡短信，设备瞬间再次崩溃死机

## ⚖️ 披露博弈与补丁发布进展

该漏洞的披露历程经历了长达半年的技术博弈：

* **争议定性：**

  研究人员早在 2026 年 5 月 5 日便向 Google 安全团队提交了完整 PoC，但最初被谷歌以“仅造成局部服务拒绝服务（DoS）而非特权代码执行”为由评为非高优先级安全缺陷
* **AOSP 静默合入：**

  AOSP 提交记录显示，谷歌底层工程师在 6 月 15 日悄然提交了代码修复，在 PDU 解析中加入了强制 try-catch 拦截，并在捕获异常后直接丢弃该数据包，防止堵塞重试队列
* **公开分析与正式更新：**

  鉴于全球存量数十亿台 Android 设备仍完全暴露于 0-Click 拒绝服务风险之下，研究员在 10 月 29 日按期解密了技术细节。GrapheneOS 等定制固件团队确认，目前商业 Android 系统的正式安全更新（覆盖 Android 14、15、16 及 17 分支）计划于 2026 年 11 月安全补丁日全面推送

## 🛡️ 终端防护与自救措施

* **关闭自动接收彩信：**

  在系统短信设置中立即关闭“自动检索彩信/自动下载彩信”与“接收 WAP Push”选项，阻断系统级自动反序列化
* **遭遇死循环自救：**

  若手机突发持续崩溃黑屏，切勿盲目直接恢复出厂设置。应立刻**拔出 SIM 卡或开启飞行模式**，切断基站通信后重启设备，清除短信缓存或等待系统稳定，待运营商重发窗口期（通常 48 小时）过去后再行插卡
* **关注 11 月安全补丁：**

  各大手机厂商推送 2026 年 11 月安全补丁后，务必在第一时间升级

***END***

阅读推荐

[【安全圈】24小时内超6万次攻击针对WordPress RCE漏洞，更新过程无需登录就可以利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079657&idx=1&sn=0e7f6a51f91ae4c6aadcb6d7ca13c2b3&scene=21#wechat_redirect)

[【安全圈】日本航空遭遇第三方数据泄露，暴露乘客信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079657&idx=2&sn=0312f3c3c447b408d319b55721289b3e&scene=21#wechat_redirect)

[【安全圈】黑客利用 Cisco SD-WAN 漏洞部署定制的 KeyDrift 恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079657&idx=3&sn=62b5b110843a42aca0265bbe72c31840&scene=21#wechat_redirect)

[【安全圈】Gitee 725 万个公开仓库被扫出 26400 个有效凭证，9473 个是阿里云密钥](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079646&idx=1&sn=b67092a6e295dc9135d4f0304a210caa&scene=21#wechat_redirect)

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