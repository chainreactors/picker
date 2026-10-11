---
title: 【安全圈】P7 DarkSword新型iOS利用工具集曝光：精准劫持加密钱包
url: https://mp.weixin.qq.com/s/SMz1oAt8thBvuBUnWfNegg
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:06.380562
---

# 【安全圈】P7 DarkSword新型iOS利用工具集曝光：精准劫持加密钱包

# 【安全圈】P7 DarkSword新型iOS利用工具集曝光：精准劫持加密钱包

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

劫持

**核心威胁快报**：移动端武器库迎来高对抗性重构。商业间谍与黑客黑市流通的高危 iOS 漏洞套件 DarkSword 衍生出全新变种“P7 DarkSword”。该变种不仅抹除了系统日志与 HTTP 调试痕迹，更直接将恶意模块注入系统核心 SpringBoard 进程，针对设备本地 Keychain 钥匙串和加密货币钱包资产实施轻量化收割。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyF80cnr4RYcAZkiaiaqnllce6Angu4Y2464bbMoyCiahsEL3qhN3KsTh6IFOFDxFkjywXibxG6U17dVvA0NGLmsGTraEqhNMxjSc48/640?wx_fmt=other&from=appmsg)

## 🔍 军火级套件流入黑市：从沙箱逃逸到 SpringBoard 驻留

移动安全机构 iVerify 发布最新分析报告显示，DarkSword 最早于 2025 年 11 月在野外被捕获，并在今年 3 月由谷歌威胁情报团队（GTIG）与 Lookout 联合披露。该套件最初定位于 iOS 18.4 至 18.7 系统的 Safari 浏览器，整条链条通过浏览器沙箱逃逸、内核提权与系统进程注入，属于高度成熟的商业监视间谍武器，随后流入地下黑市被多家黑客组织采购分发。

此次捕获的新变种因大量采用 `p7_` 变量前缀而被命名为“P7”。与早期版本相比，P7 极大压缩了设备驻留足迹，专攻隐蔽性、执行稳定性以及资产窃取效率。

## 🔑 战术蜕变：机内本地解析与极简静默回传

在对抗终端安全检测方面，P7 DarkSword 实施了多项针对性改进：

* **抹除日志痕迹**

  ：彻底移除了 HTTP 请求中的调试信息输出与系统级 `syslog` 日志打印，避免在终端产生可被追溯的异常日志。
* **浏览器状态锁**

  ：利用浏览器 `localStorage` 写入感染状态标记，严格防止对同一受害者设备重复触发漏洞利用而导致应用崩溃暴露。
* **钥匙串本地 JSON 化**

  ：早期版本通常将整个 Keychain 数据库原始镜像打包外发并在攻击端离线破解；P7 则在受害 iPhone 本地实时解密提取钥匙串结构，直接格式化为干净的 JSON 数据流外传，单次网络流量特征骤降。
* **全双工 C2 控制台**

  ：植入代码直接注入掌管 iOS 桌面与应用调度的 `SpringBoard` 进程，每隔 15 秒向远端服务器发送一次 Heartbeat 心跳，回报已安装应用清单，并动态执行下发的攻击指令。

## 🎯 协同打击：暗剑 DarkSword 与 Coruna 组合拳

网络测绘平台 Censys 近期在公网识别出 5 个开放目录的主机，均存放有 DarkSword 及另一款代号为“Coruna”的伴生载荷套件。

两者的协作极为清晰：DarkSword 负责前期破防，完成浏览器逃逸与系统权限劫持；随后启动 Coruna 专用模块，定向扫描用户设备上的 Apple 备忘录、相册、以及各大移动端加密货币钱包，全自动搜刮助记词恢复短语、私钥库及账户余额。

情报显示，该套件近期不仅被用于针对沙特、土耳其、马来西亚及乌克兰特定目标的定向网络钓鱼，还被黑客团伙结合大语言模型（LLM）尝试改写以适配苹果更新的操作系统版本。

## 🛡️ 移动终端防御建议

* **保持 iOS 系统处于最新稳定版**

  ：及时安装苹果安全更新，封堵 WebKit 浏览器沙箱和底层内核历史提权漏洞。
* **冷钱包与硬件隔离**

  ：对高净值加密资产避免仅在移动端纯软件钱包存放助记词或私钥，优先使用硬件签名设备隔离。
* **谨防钓鱼诱饵**

  ：不点击来自即时通信群组、邮件中伪装的社交平台认证、邀请函等未经验证的短链接。

***END***

阅读推荐

[【安全圈】Let's Encrypt证书期砍至64天：明年2月生效，人工运维将失效](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=1&sn=ff9aab4086a8d04641b631486818b637&scene=21#wechat_redirect)

[【安全圈】号称自研解密骗千万：应急响应厂商当黑客中间商被起诉](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=2&sn=311d2c4daa23fddd601f8601c6c0d1dc&scene=21#wechat_redirect)

[【安全圈】npm包tensorlake投毒：内置Bun蠕虫狂偷AI凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=3&sn=e303e137d9e198d454eda66df7dbed73&scene=21#wechat_redirect)

[【安全圈】SonicWall曝10分满分漏洞：无需凭据直穿内网核心](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079285&idx=1&sn=40d7e7b43c34047213b376da287167d1&scene=21#wechat_redirect)

[【安全圈】大模型缓存LMCache曝严重0day：无补丁直接RCE](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079285&idx=2&sn=5e9f5b16350c4daf6a1e4984eaf8184b&scene=21#wechat_redirect)

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