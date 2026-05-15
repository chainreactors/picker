---
title: 【安全圈】微软警告“ Dirty Frag ” Linux 内核漏洞已遭黑客利用
url: https://mp.weixin.qq.com/s/vO4Doq0VioQlbVQ0xRjHuA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:59.892771
---

# 【安全圈】微软警告“ Dirty Frag ” Linux 内核漏洞已遭黑客利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFSpLuN0SficXHN64dH7cXNibt1yMibRpN8JJ6ANRcnqqWb6RWBU6PiaFoAFCqSgS4Mz7TWbNJ3ibp3QqffgXIPoCGPibnH2xBIa3UiaE/0?wx_fmt=jpeg)

# 【安全圈】微软警告“ Dirty Frag ” Linux 内核漏洞已遭黑客利用

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

安全研究人员 Hyunwoo Kim 此前发现一项名为 "Dirty Frag" 的 Linux 内核漏洞。该漏洞属于本地权限提升（LPE）漏洞，允许黑客借助低权限账号直接获取 root 权限。该漏洞于 4 月 30 日向 Linux 内核团队报告，但一名 " 无关第三方 " 打破了披露禁令，导致漏洞在补丁尚未准备就绪时被公开。

对此，微软安全博客发文，提示研究人员近期已观察到有多名黑客利用了 Dirty Frag 漏洞进行 su 提权攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyG23prMUoviaQEoibxXanyKRkAvCtpJll9BJLpiaicayGpscrxYxicgibQFGoXYk5wMhQpaySKicTnqSnQauSbB12oNwmWCBZrx2cuCd8/640?wx_fmt=jpeg&from=appmsg)

参考微软监测，相应黑客建立外部 SSH 连接生成交互式 Shell，随后执行 ELF 二进制文件，再通过 su 命令完成提权。

在成功获取高权限后，黑客会篡改与 GLPI LDAP 身份认证相关的特定文件，并进一步对 GLPI 与系统配置展开侦察，之后便会尝试窃取受害者敏感数据，并擦去会话内容中的敏感信息。

微软警告，"Dirty Frag" 利用方式与今年 4 月底曝光的 Copy Fail（CVE-2026-31431）存在相似之处，均通过操控 Linux 页缓存（Page Cache）机制实现提权，但 Dirty Frag 提供了更多攻击路径，因此在漏洞利用成功率与稳定性方面可能比 Copy Fail 更高，这也意味着安全风险进一步升级。

***END***

阅读推荐

[【安全圈】苹果修复 macOS 和 iOS 系统数十个漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=1&sn=28c320ab902f356686e31c217bcd9b65&scene=21#wechat_redirect)

[【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=2&sn=8bef02564b19d5593d920a9e226b38ed&scene=21#wechat_redirect)

[【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=3&sn=4a801e88018faba5f0fdb72a80373270&scene=21#wechat_redirect)

[【安全圈】警惕！你的蓝牙可能正被监听 改一个设置就能有效防护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=1&sn=80e79d8ca786f2b8a4f2a23fe7d5bad4&scene=21#wechat_redirect)

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