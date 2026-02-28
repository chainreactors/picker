---
title: 【安全圈】微软披露新型木马攻击：伪装游戏工具植入RAT，远程窃取数据
url: https://mp.weixin.qq.com/s/nSLS_as2Up8dxLNGDVoYSg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:52:10.504057
---

# 【安全圈】微软披露新型木马攻击：伪装游戏工具植入RAT，远程窃取数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGs2Hk98PdXBYCzhz6Q6VHRzQqS1uyzvib7bdRzV3Vtjs3JwNHCcfaYG0ILalZ3wXZYibdWNztNlDkdc4emFnXyws8fcZY1jfYKk/0?wx_fmt=jpeg)

# 【安全圈】微软披露新型木马攻击：伪装游戏工具植入RAT，远程窃取数据

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyGzibSC9OsatXSxXAdxia1NnaLR7OPFGDeEkdBnsZXlapYBq4FTeEBhqItbhtLcMuw3iaqtlCT0F8MvCf1wPyLUBYroqlX1e67tsg/640?wx_fmt=png&from=appmsg)

微软安全团队通过 Microsoft Defender 发现一起正在活跃的恶意软件传播活动，攻击者将木马程序伪装成常见游戏工具，通过浏览器和聊天平台传播。一旦用户运行这些看似正常的程序，系统就会被植入远程控制木马（RAT），攻击者可完全接管设备。

此次攻击主要利用名为 Xeno.exe 和 RobloxPlayerBeta.exe 的文件进行伪装，专门针对游戏用户群体，降低受害者警惕性。恶意程序会部署便携式 Java 运行环境，并执行名为 jd-gui.jar 的恶意文件，同时借助 PowerShell 和系统自带工具隐藏行为，甚至主动向安全软件添加排除项以躲避检测。

感染成功后，受害设备会与远程 C2 服务器 79.110.49[.]15 建立连接，攻击者可窃取个人文件、账号密码及敏感数据，并通过计划任务和启动脚本实现持久化控制。

安全专家建议，企业和个人应监控异常外联流量，排查可疑计划任务和安全软件排除项，及时隔离受感染设备并重置相关凭证，避免造成更大范围的数据泄露风险。

***END***

阅读推荐

[【安全圈】大疆扫地机被曝安全漏洞，6700台设备可被远程控制](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=1&sn=09a467e0d06230cc6b463f9ca34e345f&scene=21#wechat_redirect)

[【安全圈】黑客利用 Facebook 广告投放假 Windows 11 更新窃取信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=2&sn=3fc8df9b9feb952b9682755651f3f845&scene=21#wechat_redirect)

[【安全圈】全球零售巨头电商遭植入支付窃取器：PrestaShop 商城被“二次下单”攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=3&sn=e9647e8fcf5b6a5981e64ebca7f1d0ad&scene=21#wechat_redirect)

[【安全圈】黑客将 Pulsar RAT 藏进 PNG 图片：NPM 再现供应链投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=4&sn=25f3b263eaade2e01f72a50d49279106&scene=21#wechat_redirect)

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

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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