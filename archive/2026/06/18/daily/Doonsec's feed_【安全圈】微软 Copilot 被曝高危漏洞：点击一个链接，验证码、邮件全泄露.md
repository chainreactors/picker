---
title: 【安全圈】微软 Copilot 被曝高危漏洞：点击一个链接，验证码、邮件全泄露
url: https://mp.weixin.qq.com/s/1NCfwykzgi0z8KRbFDNM4A
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:17.131713
---

# 【安全圈】微软 Copilot 被曝高危漏洞：点击一个链接，验证码、邮件全泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGAqRaH3KAnUxcPRMJxMZpZPGKl7YBYHdKPr21B3eDxticlYkmbBx11082lzTJq4Pe3TChwUpJbNfXWnMhj7Oeztpic4uVaFVGaE/0?wx_fmt=jpeg)

# 【安全圈】微软 Copilot 被曝高危漏洞：点击一个链接，验证码、邮件全泄露

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

微软 Copilot AI 刚刚被曝出一个 "关键"级安全漏洞，攻击者只需诱骗你点一个链接，就能窃取你的 2FA 验证码、邮件内容、会议详情等敏感数据。

这个漏洞编号 CVE-2026-42824，由网络安全公司 Varonis Threat Labs 发现，研究员将其命名为 SearchLeak。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHLOte6KVDhV3GQh7gMlrYUokPAVbtxqYB6UUDap0RAkK1XPzxFhao2EiabotCtwiajq56PQhnXAcevwOnVs2nexUZ30VibKIcDJY/640?wx_fmt=jpeg&from=appmsg)

它怎么运作的？

这是一个三阶段攻击链：

1. 攻击者把恶意参数嵌入一个看起来正常的 URL
2. 你点了这个链接，Copilot 的 AI 引擎把 URL 内容解读为搜索指令
3. Copilot 自动执行"搜索用户邮件"等操作，把敏感信息嵌入图片 URL，通过 Bing 外传

重点来了：

传统漏洞靠的是系统缺陷，而 SearchLeak 直接利用的是 AI 对自然语言指令的"轻信"——绕过了常规安全检测。
影响范围有多大？

该漏洞影响 Microsoft 365 Copilot 企业版，意味着攻击者能获取企业内部几乎所有已索引的内容：

* 邮件

* SharePoint 文档
* OneDrive 文件
* 2FA 验证码
* 会议邀请

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHq861dT6TaBag4AIDvhDuey4n8ITXGC1hfVl9ojghC1iccomM6uLib2wdbXaiccsbm5QpeB4jhr4y0greGy3DxVO4KHLSY4qz6zg/640?wx_fmt=jpeg&from=appmsg)

目前情况：
微软已发布补丁，官方表示暂无证据显示有黑客实际利用该漏洞发起攻击。

建议：

* 企业 IT 管理员尽快确认 Copilot 已更新到最新版本
* 对来历不明的链接保持警惕，尤其是包含可疑参数的 URL
* 敏感操作（如 2FA）尽量不依赖邮件验证码
* AI 越来越强，但被利用的风险也在同步升级

***END***

阅读推荐

[【安全圈】紧急预警！哪吒监控面板曝 9.1 分高危漏洞，仅需 2 次请求即可免密接管！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=1&sn=dcf088b926d0cc3dd13df3ed9b648787&scene=21#wechat_redirect)

[【安全圈】ClickFix 活动通过新加载器和虚假更新诱饵扩大恶意软件投递](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=2&sn=1799420aeb8144065e9317cfef8dca8e&scene=21#wechat_redirect)

[【安全圈】Google Vertex AI SDK 漏洞允许攻击者通过存储桶抢占劫持模型上传](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=3&sn=8609933c2ae9419836b855460349c8ce&scene=21#wechat_redirect)

[【安全圈】高德地图崩了！！！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077442&idx=1&sn=362b0f0b5d8818cd98df9a84c93c851b&scene=21#wechat_redirect)

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