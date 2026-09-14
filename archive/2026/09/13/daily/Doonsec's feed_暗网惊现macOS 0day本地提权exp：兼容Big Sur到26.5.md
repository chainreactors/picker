---
title: 暗网惊现macOS 0day本地提权exp：兼容Big Sur到26.5
url: https://mp.weixin.qq.com/s/J7BBAqVBqEAcgKW0Rf5mUQ
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:53.107659
---

# 暗网惊现macOS 0day本地提权exp：兼容Big Sur到26.5

# 暗网惊现macOS 0day本地提权exp：兼容Big Sur到26.5

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Ny6XdKv800I9ojMLibMHT5YzlMthjX3giaxDgxvhRWN42C4R3eKDTt7nibu920HTjOWN7Q34tRpqtSukAP1FKbz46Kcun5ibWzPVM/640?from=appmsg)
> **导语**：暗网情报账号DailyDarkWeb日前披露，地下论坛惊现一条macOS本地提权（LPE，本地权限提升）漏洞售卖信息。攻击者声称这是未修补的独家0day（厂商尚不知晓或未修复的漏洞），在macOS 26.5上验证通过，并兼容Big Sur（11.6）老系统、M1/M4 Apple Silicon（苹果自研芯片）及x86架构Mac，仅售一位买家。问题是：横跨五个大版本的逻辑漏洞，要么价值连城，要么精心骗局。

---

## 一、事件回顾

9月12日，X账号@DailyDarkWeb发布地下市场监测警报：卖家声称一个未修补的macOS LPE漏洞，性质为Logic-based（基于逻辑缺陷），在macOS 26.5上测试通过，兼容Big Sur到26.5五个大版本，覆盖M1/M4芯片及老款x86 Mac。销售模式独家single buyer（只卖一个买家），PoC（概念验证）未公开。

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OB9loEIN97LNJtIabQ8UliaBT7zW93aN7ibFgocpR1gWAU0Na1Jia9NYdJ6GmADZo4BvnksOdiccD2DwtJ98Cfq67JuAlYOJEMLCs/640?wx_fmt=jpeg&from=appmsg)

分析师附注："声称兼容跨度尤其值得注意。但目前没有任何独立证据能证实漏洞真实性、影响范围、利用可靠性——视为未经证实的地下市场声明。"

---

## 二、红队视角：五个可疑点

地下0day市场的水比公开漏洞赏金平台深几个数量级，每条独家listing都得用怀疑的眼光拆解。

**兼容跨度异常夸张**。从Big Sur（11.6，2022年）到26.5（2026年），苹果换过内核架构、改过系统服务、改过沙箱模型无数轮。逻辑型漏洞依赖特定代码逻辑，版本一改就失效，能跨五个大版本还能用，要么藏在极底层服务（比如XPC（跨进程通信）、launchd配置），要么就是吹牛。

**芯片架构覆盖可疑**。M1到M4同属ARM，但"老x86也受影响"等于把目标扩张到"博物馆里挖出来的机器"（最后一款x86 Mac在2020年停产），意义不大，更像话术包装——"覆盖面广 = 物超所值"。

**PoC不公开**。靠谱卖家至少提供模糊处理的PoC视频或现场演示。只挂文字描述不给证据，要么货不对板，要么拿"独家"当话术——反正独家，没人能跟别的卖家对比。

**价格不透明**。可能意味着"看人下菜"——通过询价探测买家身份、预算和需求，地下市场里这种情报收集并不少见。

**时间窗口诡异**。macOS 26.6.2已在9月8号推送。卖家却挂在"26.5验证"——要么是过时测试版本（说明漏洞可能在26.6已修），要么是故意降低买家戒心。

![暗网0day交易链条：卖家、托管平台、买家三角关系](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6O7u65u39EPSpfYUotV3zIP8MDdtvAVCOKIrpXiaWHgeM5M10lAt82y7rKEtpJ4BHxKA0qGBqYzTHOxRWUvlC99LgcYUWqI3tVM/640?from=appmsg "暗网0day交易链条：卖家、托管平台、买家三角关系")

---

## 三、暗网0day价格锚

作为参考：iOS远程代码执行+沙箱逃逸完整链100万-250万美元；Android RCE+提权链50万-150万；macOS内核LPE单点15万-60万（视利用稳定性）。能跨五个大版本+两种芯片架构+逻辑型的单点LPE，若属实市场锚定30万-80万美元。但这种货通常被APT（国家级高级持续威胁）组织和商业间谍软件厂商（NSO、Intellexa级别）消化，不会挂在公开地下论坛让散户抢。

更现实的可能：**这条listing是情报诱饵**——挂出来看谁询价，询价者就暴露了身份和需求。地下市场里"假货真卖"的局并不少见。

---

## 四、对防守方的启示

不管真假，macOS本地提权这件事本身就值得企业安全团队严肃对待。LPE在攻击链里扮演"临门一脚"角色：远程漏洞拿到代码执行 + LPE拿到root = 完全控制。中间缺一环，整个攻击链就断。

**红队建议**：

* **强制启用SIP（System Integrity Protection，系统完整性保护）**：苹果的底层防护机制，保持开启能挡掉80%的LPE利用
* **审计sudo配置**：很多Mac管理员为方便给了过宽的sudo权限
* **部署端点检测响应（EDR）工具**：CrowdStrike、SentinelOne、Microsoft Defender for Endpoint对Mac都有覆盖，能捕获LPE利用留下的异常行为链
* **按需升级**：macOS 26.6.2已经推送，所有Mac终端今天应该升上去

---

## 五、给漏洞研究者

**别去买这种listing**。苹果有官方漏洞赏金项目Apple Security Bounty，最高100万美元，直接提交苹果拿干净的钱；买来的exp是"赃物"，法律风险高；0day研究本身是门手艺，与其花钱买别人的漏洞，不如自己挖——macOS的攻击面比iOS大得多，但研究门槛更低。

暗网情报这碗饭，看个乐子就行，别真下单。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O5GCvVHOJicEfnDBb99K5IfuU406wTIcw87jU0pV9hDWHoY2FNyjErqkJ22LvHIUqkibfuN8834PXa1uvg3rruV6hVlVvz0RIRI/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OlA2gyuSSMq6mHWtMBJ4zia8QtLpsYLIG9F7kYHXRbfBw3hyXozIicA2bMcdicbwuPjcQqelVeaeMfiasNTjBicMtkJgMPHDpdcyYs/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NlUtzyWJqxVtYsvyTsEkibQiaW0hk27XtAocxibWib8NIg2AcLib0n1c77ekcQCibia5DJTbcQpLvNR8vnzL0MK7c5hT8HcYK04v75S8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Odd8JFLzia5psXBic7xzlbvsRtyknUTOz0Gsbtsx1mTibwCkJx1Usu3X3p9pJujNmtrt9z6cJE4a7PLBQLnQfcp4aQzIpIiaK8OVM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

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