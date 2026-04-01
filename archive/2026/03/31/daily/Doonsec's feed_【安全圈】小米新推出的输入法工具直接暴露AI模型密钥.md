---
title: 【安全圈】小米新推出的输入法工具直接暴露AI模型密钥
url: https://mp.weixin.qq.com/s/55W-LITXl8b14_WamLUpXg
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:58.751651
---

# 【安全圈】小米新推出的输入法工具直接暴露AI模型密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHMQPGyyjxvfmuHNKvwtGXdYoianLFl1Nl1VWTZfz0KlpN31beamPP6AEBdgrcaS7dnRqDAWIPNWeVVMx0CF53jia8KZ1FaMo6Wc/0?wx_fmt=jpeg)

# 【安全圈】小米新推出的输入法工具直接暴露AI模型密钥

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyEr6GfUialtwdEmMM0Lnp4iaHwUHEgQwGsrnDz9IWMDziaIlNXFZD8P1O3ib1ib5zfhJzYxTClicE5vjX49W3Feys5JMiceeeMAfU50ib8/640?wx_fmt=png&from=appmsg)

小米 MiClaw 团队近日推出了一款新的系统输入法，但却因为安全问题引发关注。

![实在没忍住笑出声：小米新推出的输入法工具直接暴露AI模型密钥](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyEfZdC4ribynsUnA5ypnY4wx7kX17LOEqLTdXWBxXVMYrpeLOOcSibxE145dbxMssbrYJ6CW1NhlbPQvnEHTpEKRuUk251zkNEgg/640?wx_fmt=png&from=appmsg)

有网友测试发现，只需连续点击输入法版本号即可进入调试页面。而在该页面中，竟直接暴露了完整的 AI 调用信息，包括 API 地址、模型提供商、模型名称、提示词，甚至还有明文 API Key。

从提示词内容来看，这款输入法主打语音输入后的文本优化功能，例如自动修正错别字、语法错误，并补充标点符号等。

![实在没忍住笑出声：小米新推出的输入法工具直接暴露AI模型密钥](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyHnxxpnymg02uCTicC00ibdhiah4nvy2y903gamoaicyagSTRNXM5w0JW0IticZkOyWlQ9CX5KNebZtOGqjE0ym2fsicZxLicJqJyTTKA/640?wx_fmt=png&from=appmsg)

更令人意外的是，网友对该 API Key 进行了验证，确认其为真实有效，甚至可以在其他平台调用，且权限范围较大。不过，事件曝光后，该 Key 很可能已经被官方紧急替换。

此外，小米团队此前还曾出现类似问题：在 GitHub 提交代码时误将 API Key 明文上传。相关记录显示，该 Key 来自月之暗面平台，且自 2025 年 1 月提交后未见更新或清理。

整体来看，这类问题属于较为基础的安全失误，但却出现在大型厂商中，确实令人意外。也有观点认为，这可能与当前 AI 辅助编码的使用方式有关，开发流程中的安全审查环节被弱化。

如果连头部厂商都可能出现此类问题，未来类似的安全事件或许还会持续出现。

***END***

阅读推荐

[【安全圈】DeepSeek崩了！超过11小时仍未被修复](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075204&idx=1&sn=0d5532dced2ed29ce8b6dce346ba8f9f&scene=21#wechat_redirect)

[【安全圈】Telegram 遭遇严重 0-day 漏洞，CVSS 评分高达 9.8 分](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075204&idx=2&sn=f5c0bfeaf0614eabe75d0b22d42892c3&scene=21#wechat_redirect)

[【安全圈】突发！FBI 局长遭伊朗黑客 “开盒”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075160&idx=1&sn=909870ed4b9e7d5e2a8685c55b23159a&scene=21#wechat_redirect)

[【安全圈】警惕！只需一个举动，你可能已经犯罪](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075160&idx=2&sn=17ef85e58e17f2257b11047e530dfaae&scene=21#wechat_redirect)

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