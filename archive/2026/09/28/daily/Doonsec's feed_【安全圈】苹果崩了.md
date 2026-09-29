---
title: 【安全圈】苹果崩了
url: https://mp.weixin.qq.com/s/vqgvkWCsPpXWx0V-rgEmgg
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:39:37.707721
---

# 【安全圈】苹果崩了

# 【安全圈】苹果崩了

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGtynbKa7ZepGw8hIcoazlB4qVSEBiaNGUSHjGQtwqNiaicQs1jEq3NxexYCXLV5PszUTJ30rbXXePHSNujof9oFK1tcoXs9xdcWU/640?wx_fmt=jpeg&from=appmsg)

**事件核心要点：**苹果 2026 年最新旗舰机型发售仅 10 天，国内社交平台出现集中爆发的“Face ID 卡顿后强制黑屏关机重启”故障。苹果官方已正式证实该项严重系统漏洞，客服明确属于系统软件层缺陷、与硬件无关，工程团队已全面介入调查，后续将通过 iOS 系统版本补丁推送修复。

## 🚨 刚买10天就翻车：9999元起步旗舰频遭“面容杀”

9月18日正式开售、国内起售价高达 **9999 元**的全新 iPhone 18 Pro 与 iPhone 18 Pro Max，在发售仅 10 天后遭遇严重的软件体验“翻车”。

连日来，大量提机尝鲜的用户在社交媒体上集中晒出故障实录：**手机在进行面容识别时突然无响应卡死，数秒后直接黑屏并自动重启**。无论是日常抬手解锁屏幕、多任务 App 切换校验，还是微信与支付宝的人脸支付环节，均有概率突发此现象，不仅直接打断正在进行的操作，更导致部分用户未保存的现场数据丢失。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEC0XfPBiafHibHoO1B987aUtcfNKNCzJ5IBibbAQSVmj7VHk5wQCIVZHgKkxj1yHWWKZicdaBJotnFdhSWJricfPhmP9cdibxCicG4Tw/640?wx_fmt=other&from=appmsg)

## 🔍 诱发原因分析：Face ID 为何会引爆系统崩溃？

针对持续发酵的用户反馈，苹果官方于 **9月26日** 正式对外证实：旗下最新发布的 iPhone 18 Pro 与 iPhone 18 Pro Max 机型中，确实存在一项与 **Face ID 面容识别功能相关的严重系统漏洞**。

从目前的系统崩溃日志与机理来看，问题并非出在摄像头本身：

```
[阶段1: 特征采集] 前置原深感摄像头捕捉面部红外图像并点阵投影 [阶段2: 校验触发] 图像数据送往 Secure Enclave (安全隔离区) 处理 [阶段3: 进程死锁] 生物识别验证框架在特定场景下发生同步通信挂起 [阶段4: 看门狗超时] iOS 内核 Watchdog 判定服务无响应超时 (Hang Timeout) [阶段5: 内核死机重启] 系统保护触发 Panic，强行终止会话并整机重启
```

9月28日，针对该漏洞出现的原因等情况，记者以消费者身份联系苹果官方客服。客服人员明确回应表示，近期已接到多起类似反馈，**问题属于系统软件层缺陷，和硬件本身没有任何关系**，“已在第一时间提交工程部调查，后续会通过系统版本更新来解决”。

## 🛡️ 官方回应进展：软件问题，坐等系统更新

针对消费者的换机顾虑与返修问询，苹果技术支持给出了清晰指引：

* **无需线下跑售后拆机：**

  由于属于纯系统固件缺陷，盲目去直营店或售后换屏、拆机均无意义；
* **工程部正在加急定位：**

  苹果工程部已调取全球故障机器崩溃日志，针对死锁逻辑编写补丁；
* **依赖 OTA 紧急推送：**

  修复程序将随接下来的 iOS 紧急维护更新（如小版本迭代）直接推送到受影响设备。

## 💡 补丁发布前，机主临时规避建议

在苹果正式推送固件补丁之前，若设备出现高频崩溃死机，建议采用以下临时方案：

1. **停用高频闪退 App 的面容授权：**

   前往系统「设置」-「面容 ID 与密码」，关闭特定常用应用（如支付软件）的“使用面容 ID”权限，临时回退到数字密码解锁；
2. **重新录入面容数据：**

   部分机主测试表明，在环境光线充足条件下单次录入面容数据，能在一定程度上降低比对死锁的触发概率；
3. **避免重载运行中高频调起：**

   在后台游戏高负荷运行或 4K 高码率录制时，尽量避免快速切屏进行面部校验。

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyF8vAeWSN5ibnYYybvrEfAtSwdJSA7RwEhz858Hg8TkvBYy3mS2XR0ib5sqE7ldiaaFYibAiaHicDYxZUKHBSnEIosVkib2QafFVYIfk4/640?wx_fmt=other&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHS9biapMNdWKXfWyaUsBYqO3kkkZtwuOvReNrXiaicRiakXqU1iclbP6UUkkPx6V1hdwtHdakUvfWibdflyKiaE6xISiaQOrtQbMofjhQ/640?wx_fmt=other&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGqlHa5PuXkReqoaHaNn9l727LfB5q0DOShQDyDNJHzvSkS4iaVJPwhlTStVjCicyQbvoxE6cnBhHMtSLfvlt6ZdlicBSR7GMwpOw/640?wx_fmt=other&from=appmsg)

***END***

阅读推荐

[【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=1&sn=7df0283a6c5d51694b17203ac0b35c59&scene=21#wechat_redirect)

[【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=2&sn=df0e0e05d2843681315bf1ebf88e985d&scene=21#wechat_redirect)

[【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=3&sn=8eab1210d63abf0b373ad59028f7c1ad&scene=21#wechat_redirect)

[【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=1&sn=c15dc9fe4166f047f1ddffafc639e2e0&scene=21#wechat_redirect)

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